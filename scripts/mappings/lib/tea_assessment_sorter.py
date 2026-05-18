from __future__ import annotations

import argparse
import io
import json
import re
import shutil
import sys
import time
import zipfile
from collections import deque
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_INPUT_ROOT = REPO_ROOT / ".tmp"
DEFAULT_UPLOADS_DIR = DEFAULT_INPUT_ROOT / "uploads" / "tea"
DEFAULT_OUTPUT_ROOT = REPO_ROOT / ".tmp" / "exports" / "tea"
DEFAULT_PROCESSED_ROOT = REPO_ROOT / ".tmp" / "processed_files" / "tea"
DEFAULT_MAPPING_ROOT = REPO_ROOT / "assessments" / "tea"
KNOWN_METADATA_PATTERNS = (
    re.compile(r"^readme(?:\..+)?$", re.IGNORECASE),
    re.compile(r"^nomatch(?:\..+)?$", re.IGNORECASE),
    re.compile(r"^manifest(?:\..+)?$", re.IGNORECASE),
    re.compile(r"^metadata(?:\..+)?$", re.IGNORECASE),
)
INPUT_MODE_LOOSE = "loose"
INPUT_MODE_ARCHIVE = "archive"
INPUT_MODE_ALL = "all"
OUTPUT_MODE_ARCHIVE = "archive"
OUTPUT_MODE_DIRECTORY = "directory"
GROUPING_ASSESSMENT = "assessment"
GROUPING_ASSESSMENT_BY_YEAR = "assessment-by-year"


@dataclass(frozen=True)
class MappingBucket:
    mapping_path: Path
    output_stem: str
    assessment_key: str
    regex_strings: tuple[str, ...]
    regexes: tuple[re.Pattern[str], ...]


@dataclass(frozen=True)
class ExtractedFile:
    disk_path: Path
    archive_path: str
    source_archive: str
    source_archive_stem: str


@dataclass(frozen=True)
class ArchiveJob:
    archive_path: Path
    extract_root: Path
    logical_prefix: tuple[str, ...]
    source_archive: str


@dataclass
class OutputState:
    output_name: str
    preserve_source_dir: bool
    zip_handle: zipfile.ZipFile | None
    output_dir: Path | None
    used_names_by_prefix: dict[str, set[str]]
    members: list[str]


class OutputManager:
    def __init__(self, outputs_root: Path, output_mode: str):
        self.outputs_root = outputs_root
        self.output_mode = output_mode
        self.states: dict[str, OutputState] = {}

    def write_from_stream(
        self,
        output_name: str,
        extracted_file: ExtractedFile,
        src,
        preserve_source_dir: bool = False,
    ) -> str:
        state = self.states.get(output_name)
        if state is None:
            destination = self.outputs_root / output_name
            destination.parent.mkdir(parents=True, exist_ok=True)
            zip_handle: zipfile.ZipFile | None = None
            output_dir: Path | None = None
            if self.output_mode == OUTPUT_MODE_ARCHIVE:
                zip_handle = zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED)
            else:
                output_dir = destination
                output_dir.mkdir(parents=True, exist_ok=True)
            state = OutputState(
                output_name=output_name,
                preserve_source_dir=preserve_source_dir,
                zip_handle=zip_handle,
                output_dir=output_dir,
                used_names_by_prefix={},
                members=[],
            )
            self.states[output_name] = state

        source_prefix = ""
        if preserve_source_dir:
            source_prefix = PurePosixPath(extracted_file.archive_path).parts[0]

        used_names = state.used_names_by_prefix.setdefault(source_prefix.lower(), set())
        final_name = get_unique_member_name(
            base_name=Path(extracted_file.archive_path).name,
            source_stem=extracted_file.source_archive_stem,
            used_names=used_names,
        )
        if preserve_source_dir:
            member_name = PurePosixPath(source_prefix, final_name).as_posix()
        else:
            member_name = final_name

        if self.output_mode == OUTPUT_MODE_ARCHIVE:
            assert state.zip_handle is not None
            with state.zip_handle.open(member_name, "w") as dst:
                shutil.copyfileobj(src, dst, length=1024 * 1024)
        else:
            assert state.output_dir is not None
            destination = state.output_dir.joinpath(*PurePosixPath(member_name).parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open("wb") as dst:
                shutil.copyfileobj(src, dst, length=1024 * 1024)
        state.members.append(member_name)
        return member_name

    def build_created_outputs(self) -> list[dict[str, object]]:
        outputs: list[dict[str, object]] = []
        for output_name in sorted(self.states):
            state = self.states[output_name]
            outputs.append(
                {
                    "output": state.output_name,
                    "file_count": len(state.members),
                    "members": list(state.members),
                }
            )
        return outputs

    def close(self) -> None:
        for state in self.states.values():
            if state.zip_handle is not None:
                state.zip_handle.close()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Process TEA assessment files from a .tmp input directory, classify files "
            "using mapping filename_patterns, and write one output bucket per mapping file."
        )
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        nargs="?",
        default=DEFAULT_UPLOADS_DIR,
        help=(
            "Path to a .tmp subdirectory containing TEA assessment files. "
            f"Defaults to {DEFAULT_UPLOADS_DIR}."
        ),
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help=f"Directory for run outputs. Defaults to {DEFAULT_OUTPUT_ROOT}.",
    )
    parser.add_argument(
        "--keep-extracted",
        action="store_true",
        help="Keep extracted working files in the run directory after repacking.",
    )
    parser.add_argument(
        "--input-mode",
        choices=[INPUT_MODE_LOOSE, INPUT_MODE_ARCHIVE, INPUT_MODE_ALL],
        default=INPUT_MODE_LOOSE,
        help=(
            "Choose whether to process loose files only, archive contents only, "
            "or both. Defaults to loose."
        ),
    )
    parser.add_argument(
        "--include-archives",
        action="store_true",
        help=(
            "Compatibility shortcut for --input-mode all. "
            "Only flat files directly inside the input directory are processed by default."
        ),
    )
    parser.add_argument(
        "--output-mode",
        choices=[OUTPUT_MODE_DIRECTORY, OUTPUT_MODE_ARCHIVE],
        default=OUTPUT_MODE_DIRECTORY,
        help="Write sorted outputs as directories or archive files. Defaults to directory.",
    )
    parser.add_argument(
        "--grouping",
        choices=[GROUPING_ASSESSMENT_BY_YEAR, GROUPING_ASSESSMENT],
        default=GROUPING_ASSESSMENT_BY_YEAR,
        help=(
            "Group outputs by assessment and year, or by assessment across all years. "
            "Defaults to assessment-by-year."
        ),
    )
    args = parser.parse_args(argv)
    if args.include_archives and args.input_mode == INPUT_MODE_LOOSE:
        args.input_mode = INPUT_MODE_ALL
    return args


def ensure_subpath(path: Path, root: Path, label: str) -> Path:
    resolved_path = path.expanduser().resolve()
    resolved_root = root.expanduser().resolve()
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"{label} must be inside {resolved_root}") from exc
    return resolved_path


def sanitize_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    cleaned = cleaned.strip(".-")
    return cleaned or "item"


def is_zip_path(path: Path) -> bool:
    return path.suffix.lower() == ".zip"


def list_source_archives(input_dir: Path) -> list[Path]:
    return sorted(path for path in input_dir.iterdir() if path.is_file() and is_zip_path(path))


def list_loose_files(input_dir: Path) -> list[Path]:
    return sorted(path for path in input_dir.iterdir() if path.is_file() and not is_zip_path(path))


def safe_member_path(member_name: str) -> PurePosixPath:
    candidate = PurePosixPath(member_name)
    if candidate.is_absolute():
        raise ValueError(f"archive member '{member_name}' must not be absolute")

    safe_parts: list[str] = []
    for part in candidate.parts:
        if part in ("", "."):
            continue
        if part == "..":
            raise ValueError(f"archive member '{member_name}' must not contain '..'")
        safe_parts.append(part)

    if not safe_parts:
        raise ValueError(f"archive member '{member_name}' does not point to a file")

    return PurePosixPath(*safe_parts)


def load_mapping_buckets(mapping_root: Path = DEFAULT_MAPPING_ROOT) -> list[MappingBucket]:
    buckets: list[MappingBucket] = []

    for mapping_path in sorted(mapping_root.rglob("*.json")):
        data = json.loads(mapping_path.read_text(encoding="utf-8"))
        filename_patterns = data.get("filename_patterns")
        if not isinstance(filename_patterns, list) or not filename_patterns:
            continue

        regex_strings: list[str] = []
        regexes: list[re.Pattern[str]] = []
        for idx, pattern in enumerate(filename_patterns):
            if not isinstance(pattern, dict):
                raise ValueError(f"{mapping_path}: filename_patterns[{idx}] must be an object")

            regex = pattern.get("regex")
            if not isinstance(regex, str) or not regex.strip():
                raise ValueError(
                    f"{mapping_path}: filename_patterns[{idx}].regex must be a non-empty string"
                )

            regex_strings.append(regex)
            regexes.append(re.compile(regex))

        relative_parent = mapping_path.relative_to(mapping_root).parent
        assessment_key = relative_parent.as_posix() if relative_parent.parts else mapping_path.stem
        buckets.append(
            MappingBucket(
                mapping_path=mapping_path,
                output_stem=mapping_path.name.removesuffix("-fixed-width-mapping.json"),
                assessment_key=assessment_key,
                regex_strings=tuple(regex_strings),
                regexes=tuple(regexes),
            )
        )

    if not buckets:
        raise ValueError(f"No mapping files with filename_patterns found under {mapping_root}")

    return buckets


def classify_file(
    file_name: str, buckets: list[MappingBucket]
) -> tuple[MappingBucket | None, list[str], list[str]]:
    matching_buckets: list[str] = []
    matching_patterns: list[str] = []
    winner: MappingBucket | None = None

    for bucket in buckets:
        matched_patterns_for_bucket: list[str] | None = None
        for regex in bucket.regexes:
            if not regex.search(file_name):
                continue
            if matched_patterns_for_bucket is None:
                matched_patterns_for_bucket = []
            matched_patterns_for_bucket.append(regex.pattern)

        if matched_patterns_for_bucket is None:
            continue

        matching_buckets.append(bucket.output_stem)
        matching_patterns.extend(matched_patterns_for_bucket)
        if winner is None:
            winner = bucket

    return winner, matching_buckets, matching_patterns


def is_known_metadata_file(file_name: str) -> bool:
    return any(pattern.search(file_name) for pattern in KNOWN_METADATA_PATTERNS)


def write_member(zf: zipfile.ZipFile, member: zipfile.ZipInfo, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zf.open(member) as src, destination.open("wb") as dst:
        shutil.copyfileobj(src, dst)


def extract_archives(source_archives: list[Path], extracted_root: Path) -> tuple[list[ExtractedFile], list[str]]:
    extracted_files: list[ExtractedFile] = []
    nested_archives: list[str] = []
    queue: deque[ArchiveJob] = deque()
    nested_counter = 0

    for index, source_archive in enumerate(source_archives, start=1):
        source_label = source_archive.name
        source_stem = sanitize_name(source_archive.stem)
        queue.append(
            ArchiveJob(
                archive_path=source_archive,
                extract_root=extracted_root / f"{index:03d}_{source_stem}",
                logical_prefix=(source_stem,),
                source_archive=source_label,
            )
        )

    while queue:
        job = queue.popleft()
        with zipfile.ZipFile(job.archive_path) as zf:
            for member in zf.infolist():
                if member.is_dir():
                    continue

                safe_path = safe_member_path(member.filename)
                destination = job.extract_root.joinpath(*safe_path.parts)
                write_member(zf, member, destination)

                archive_parts = (*job.logical_prefix, *safe_path.parts)
                archive_path = PurePosixPath(*archive_parts).as_posix()

                if is_zip_path(destination):
                    nested_counter += 1
                    nested_archives.append(archive_path)
                    queue.append(
                        ArchiveJob(
                            archive_path=destination,
                            extract_root=job.extract_root
                            / "__nested__"
                            / f"{nested_counter:03d}_{sanitize_name(destination.stem)}",
                            logical_prefix=(
                                *job.logical_prefix,
                                *safe_path.with_suffix("").parts,
                            ),
                            source_archive=job.source_archive,
                        )
                    )
                    continue

                extracted_files.append(
                    ExtractedFile(
                        disk_path=destination,
                        archive_path=archive_path,
                        source_archive=job.source_archive,
                        source_archive_stem=sanitize_name(Path(job.source_archive).stem),
                    )
                )

    return extracted_files, nested_archives


def process_archives_streaming(
    source_archives: list[Path],
    buckets: list[MappingBucket],
    outputs_root: Path,
    output_mode: str,
    grouping: str,
    loose_files: list[Path] | None = None,
    loose_source_label: str | None = None,
) -> tuple[list[dict[str, object]], list[str], list[str], list[str], list[dict[str, object]]]:
    nested_archives: list[str] = []
    metadata_files: list[str] = []
    unmatched_files: list[str] = []
    ambiguous_matches: list[dict[str, object]] = []
    queue: deque[tuple[Path | None, bytes | None, tuple[str, ...], str, str]] = deque()
    writer = OutputManager(outputs_root, output_mode)

    for source_archive in source_archives:
        queue.append(
            (
                source_archive,
                None,
                (sanitize_name(source_archive.stem),),
                source_archive.name,
                sanitize_name(source_archive.stem),
            )
        )

    try:
        while queue:
            archive_path, archive_bytes, logical_prefix, source_archive, source_archive_stem = queue.popleft()
            zip_source = archive_path if archive_path is not None else io.BytesIO(archive_bytes or b"")
            with zipfile.ZipFile(zip_source) as zf:
                for member in zf.infolist():
                    if member.is_dir():
                        continue

                    safe_path = safe_member_path(member.filename)
                    archive_parts = (*logical_prefix, *safe_path.parts)
                    archive_member_path = PurePosixPath(*archive_parts).as_posix()

                    if safe_path.suffix.lower() == ".zip":
                        with zf.open(member) as nested_src:
                            nested_bytes = nested_src.read()
                        nested_archives.append(archive_member_path)
                        queue.append(
                            (
                                None,
                                nested_bytes,
                                (*logical_prefix, *safe_path.with_suffix("").parts),
                                source_archive,
                                source_archive_stem,
                            )
                        )
                        continue

                    extracted_file = ExtractedFile(
                        disk_path=Path(),
                        archive_path=archive_member_path,
                        source_archive=source_archive,
                        source_archive_stem=source_archive_stem,
                    )
                    extracted_name = safe_path.name

                    if is_known_metadata_file(extracted_name):
                        metadata_files.append(archive_member_path)
                        with zf.open(member) as src:
                            writer.write_from_stream(
                                build_output_name("metadata", output_mode),
                                extracted_file,
                                src,
                                preserve_source_dir=True,
                            )
                        continue

                    winner, matching_buckets, matching_patterns = classify_file(extracted_name, buckets)
                    if winner is None:
                        unmatched_files.append(archive_member_path)
                        with zf.open(member) as src:
                            writer.write_from_stream(
                                build_output_name("unsorted", output_mode),
                                extracted_file,
                                src,
                            )
                        continue

                    if len(matching_buckets) > 1:
                        ambiguous_matches.append(
                            {
                                "file": archive_member_path,
                                "selected_bucket": winner.output_stem,
                                "matching_buckets": matching_buckets,
                                "matching_patterns": matching_patterns,
                            }
                        )

                    with zf.open(member) as src:
                        writer.write_from_stream(
                            build_output_name(build_bucket_name(winner, grouping), output_mode),
                            extracted_file,
                            src,
                        )

        if loose_files:
            loose_source_label = loose_source_label or "loose-files"
            loose_source_stem = sanitize_name(loose_source_label)
            for loose_file in loose_files:
                extracted_file = ExtractedFile(
                    disk_path=loose_file,
                    archive_path=PurePosixPath(loose_source_stem, loose_file.name).as_posix(),
                    source_archive=loose_source_label,
                    source_archive_stem=loose_source_stem,
                )

                if is_known_metadata_file(loose_file.name):
                    metadata_files.append(extracted_file.archive_path)
                    with loose_file.open("rb") as src:
                        writer.write_from_stream(
                            build_output_name("metadata", output_mode),
                            extracted_file,
                            src,
                            preserve_source_dir=True,
                        )
                    continue

                winner, matching_buckets, matching_patterns = classify_file(loose_file.name, buckets)
                if winner is None:
                    unmatched_files.append(extracted_file.archive_path)
                    with loose_file.open("rb") as src:
                        writer.write_from_stream(
                            build_output_name("unsorted", output_mode),
                            extracted_file,
                            src,
                        )
                    continue

                if len(matching_buckets) > 1:
                    ambiguous_matches.append(
                        {
                            "file": extracted_file.archive_path,
                            "selected_bucket": winner.output_stem,
                            "matching_buckets": matching_buckets,
                            "matching_patterns": matching_patterns,
                        }
                    )

                with loose_file.open("rb") as src:
                    writer.write_from_stream(
                        build_output_name(build_bucket_name(winner, grouping), output_mode),
                        extracted_file,
                        src,
                    )

        return (
            writer.build_created_outputs(),
            nested_archives,
            metadata_files,
            unmatched_files,
            ambiguous_matches,
        )
    finally:
        writer.close()


def get_unique_member_name(base_name: str, source_stem: str, used_names: set[str]) -> str:
    candidate = base_name
    stem = Path(base_name).stem
    suffix = Path(base_name).suffix
    if candidate.lower() not in used_names:
        used_names.add(candidate.lower())
        return candidate

    source_stem = sanitize_name(source_stem)
    candidate = f"{stem}__from_{source_stem}{suffix}"
    counter = 2
    while candidate.lower() in used_names:
        candidate = f"{stem}__from_{source_stem}_{counter}{suffix}"
        counter += 1
    used_names.add(candidate.lower())
    return candidate


def build_bucket_name(bucket: MappingBucket, grouping: str) -> str:
    if grouping == GROUPING_ASSESSMENT:
        return bucket.assessment_key
    return bucket.output_stem


def build_output_name(stem: str, output_mode: str) -> str:
    if output_mode == OUTPUT_MODE_DIRECTORY:
        return stem
    return f"{stem}.zip"


def create_output(
    destination: Path,
    files: list[ExtractedFile],
    output_mode: str,
    preserve_source_dir: bool = False,
) -> list[str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    members_written: list[str] = []
    used_names_by_prefix: dict[str, set[str]] = {}
    if output_mode == OUTPUT_MODE_ARCHIVE:
        with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for item in sorted(files, key=lambda value: value.archive_path.lower()):
                source_prefix = ""
                if preserve_source_dir:
                    source_prefix = PurePosixPath(item.archive_path).parts[0]

                used_names = used_names_by_prefix.setdefault(source_prefix.lower(), set())
                final_name = get_unique_member_name(
                    base_name=Path(item.archive_path).name,
                    source_stem=item.source_archive_stem,
                    used_names=used_names,
                )

                if preserve_source_dir:
                    member_name = PurePosixPath(source_prefix, final_name).as_posix()
                else:
                    member_name = final_name

                zf.write(item.disk_path, arcname=member_name)
                members_written.append(member_name)
        return members_written

    destination.mkdir(parents=True, exist_ok=True)
    for item in sorted(files, key=lambda value: value.archive_path.lower()):
        source_prefix = ""
        if preserve_source_dir:
            source_prefix = PurePosixPath(item.archive_path).parts[0]

        used_names = used_names_by_prefix.setdefault(source_prefix.lower(), set())
        final_name = get_unique_member_name(
            base_name=Path(item.archive_path).name,
            source_stem=item.source_archive_stem,
            used_names=used_names,
        )

        if preserve_source_dir:
            member_name = PurePosixPath(source_prefix, final_name).as_posix()
        else:
            member_name = final_name

        output_path = destination.joinpath(*PurePosixPath(member_name).parts)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item.disk_path, output_path)
        members_written.append(member_name)
    return members_written


def create_run_dir(output_root: Path, run_stamp: str) -> Path:
    candidate = output_root / run_stamp
    suffix = 1
    while candidate.exists():
        candidate = output_root / f"{run_stamp}-{suffix:02d}"
        suffix += 1
    candidate.mkdir(parents=True, exist_ok=False)
    return candidate


def copy_loose_files_for_debug(
    loose_files: list[Path], extracted_root: Path, source_prefix: str
) -> list[ExtractedFile]:
    extracted_files: list[ExtractedFile] = []
    debug_root = extracted_root / "__loose__"
    debug_root.mkdir(parents=True, exist_ok=True)

    for loose_file in loose_files:
        destination = debug_root / loose_file.name
        shutil.copy2(loose_file, destination)
        extracted_files.append(
            ExtractedFile(
                disk_path=destination,
                archive_path=PurePosixPath(source_prefix, loose_file.name).as_posix(),
                source_archive=source_prefix,
                source_archive_stem=sanitize_name(source_prefix),
            )
        )

    return extracted_files


def move_processed_inputs(
    source_archives: list[Path],
    loose_files: list[Path],
    processed_root: Path,
    run_dir_name: str,
) -> list[str]:
    processed_run_dir = processed_root / run_dir_name
    processed_run_dir.mkdir(parents=True, exist_ok=False)

    moved_paths: list[str] = []
    for item in [*source_archives, *loose_files]:
        destination = processed_run_dir / item.name
        shutil.move(str(item), str(destination))
        moved_paths.append(str(destination))

    return moved_paths


def build_log_lines(summary: dict[str, object]) -> list[str]:
    output_label = "archive" if summary["output_mode"] == OUTPUT_MODE_ARCHIVE else "directory"
    lines = [
        f"Run timestamp: {summary['run_timestamp']}",
        f"Start time: {summary['start_time']}",
        f"End time: {summary['end_time']}",
        f"Execution seconds: {summary['execution_seconds']}",
        f"Input directory: {summary['input_dir']}",
        f"Output root: {summary['output_root']}",
        f"Run directory: {summary['run_dir']}",
        f"Input mode: {summary['input_mode']}",
        f"Output mode: {summary['output_mode']}",
        f"Grouping: {summary['grouping']}",
        f"Processed archive count: {len(summary['processed_archives'])}",
        f"Processed loose file count: {len(summary['processed_loose_files'])}",
        f"Created {output_label} count: {summary['created_output_count']}",
        f"Nested archive count: {len(summary['nested_archives'])}",
        f"Matched file count: {summary['matched_file_count']}",
        f"Metadata file count: {summary['metadata_file_count']}",
        f"Unmatched file count: {summary['unmatched_file_count']}",
        "",
        "Processed archives:",
    ]

    lines.extend(f"- {name}" for name in summary["processed_archives"])
    if summary["processed_loose_files"]:
        lines.append("")
        lines.append("Processed loose files:")
        lines.extend(f"- {name}" for name in summary["processed_loose_files"])

    lines.append("")
    lines.append(f"Created {output_label}s:")
    for item in summary["created_outputs"]:
        lines.append(f"- {item['output']} ({item['file_count']} files)")

    if summary["metadata_files"]:
        lines.append("")
        lines.append("Known metadata files:")
        lines.extend(f"- {name}" for name in summary["metadata_files"])

    if summary["unmatched_files"]:
        lines.append("")
        lines.append("Unmatched files:")
        lines.extend(f"- {name}" for name in summary["unmatched_files"])

    return lines


def process_input_dir(
    input_dir: Path,
    output_root: Path,
    keep_extracted: bool = False,
    include_archives: bool = False,
    input_mode: str = INPUT_MODE_LOOSE,
    output_mode: str = OUTPUT_MODE_DIRECTORY,
    grouping: str = GROUPING_ASSESSMENT_BY_YEAR,
    mapping_root: Path = DEFAULT_MAPPING_ROOT,
    tmp_root: Path = DEFAULT_INPUT_ROOT,
    processed_root: Path = DEFAULT_PROCESSED_ROOT,
) -> Path:
    start_dt = datetime.now()
    start_perf = time.perf_counter()
    input_dir = ensure_subpath(input_dir, tmp_root, "input_dir")
    if not input_dir.is_dir():
        raise ValueError(f"input_dir must be an existing directory: {input_dir}")

    output_root = output_root.expanduser().resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    processed_root = processed_root.expanduser().resolve()
    processed_root.mkdir(parents=True, exist_ok=True)

    if include_archives and input_mode == INPUT_MODE_LOOSE:
        input_mode = INPUT_MODE_ALL

    available_loose_files = list_loose_files(input_dir)
    available_source_archives = list_source_archives(input_dir)
    loose_files = available_loose_files if input_mode in {INPUT_MODE_LOOSE, INPUT_MODE_ALL} else []
    source_archives = (
        available_source_archives if input_mode in {INPUT_MODE_ARCHIVE, INPUT_MODE_ALL} else []
    )
    if not loose_files and not source_archives:
        if input_mode == INPUT_MODE_ALL:
            raise ValueError(f"No loose files or .zip archives found in {input_dir}")
        if input_mode == INPUT_MODE_ARCHIVE:
            raise ValueError(f"No .zip archives found in {input_dir}")
        raise ValueError(
            f"No loose files found in {input_dir}. Pass --input-mode all or --input-mode archive to process .zip files."
        )

    buckets = load_mapping_buckets(mapping_root)

    run_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = create_run_dir(output_root, run_stamp)

    extracted_root = run_dir / "extracted"
    outputs_root = run_dir / "outputs"
    outputs_root.mkdir(parents=True, exist_ok=True)

    if keep_extracted:
        extracted_root.mkdir(parents=True, exist_ok=True)
        extracted_files, nested_archives = extract_archives(source_archives, extracted_root)
        if loose_files:
            extracted_files.extend(
                copy_loose_files_for_debug(
                    loose_files=loose_files,
                    extracted_root=extracted_root,
                    source_prefix=sanitize_name(input_dir.name),
                )
            )

        grouped_files: dict[str, list[ExtractedFile]] = {}
        output_names: dict[str, str] = {}
        unmatched_files: list[str] = []
        metadata_files: list[str] = []
        ambiguous_matches: list[dict[str, object]] = []

        for extracted in extracted_files:
            extracted_name = Path(extracted.archive_path).name
            if is_known_metadata_file(extracted_name):
                key = "metadata"
                output_names[key] = build_output_name("metadata", output_mode)
                metadata_files.append(extracted.archive_path)
                grouped_files.setdefault(key, []).append(extracted)
                continue

            winner, matching_buckets, matching_patterns = classify_file(
                extracted_name,
                buckets,
            )

            if winner is None:
                key = "unsorted"
                output_names[key] = build_output_name("unsorted", output_mode)
                unmatched_files.append(extracted.archive_path)
            else:
                key = str(winner.mapping_path)
                output_names[key] = build_output_name(build_bucket_name(winner, grouping), output_mode)
                if len(matching_buckets) > 1:
                    ambiguous_matches.append(
                        {
                            "file": extracted.archive_path,
                            "selected_bucket": winner.output_stem,
                            "matching_buckets": matching_buckets,
                            "matching_patterns": matching_patterns,
                        }
                    )

            grouped_files.setdefault(key, []).append(extracted)

        created_outputs: list[dict[str, object]] = []
        for key, files in sorted(grouped_files.items(), key=lambda item: output_names[item[0]].lower()):
            output_name = output_names[key]
            destination = outputs_root / output_name
            members_written = create_output(
                destination,
                files,
                output_mode=output_mode,
                preserve_source_dir=(output_name == build_output_name("metadata", output_mode)),
            )
            created_outputs.append(
                {
                    "output": output_name,
                    "file_count": len(files),
                    "members": members_written,
                }
            )
    else:
        created_outputs, nested_archives, metadata_files, unmatched_files, ambiguous_matches = (
            process_archives_streaming(
                source_archives,
                buckets,
                outputs_root,
                output_mode=output_mode,
                grouping=grouping,
                loose_files=loose_files,
                loose_source_label=sanitize_name(input_dir.name),
            )
        )

    moved_inputs = move_processed_inputs(source_archives, loose_files, processed_root, run_dir.name)
    moved_archive_destinations = moved_inputs[: len(source_archives)]
    moved_loose_file_destinations = moved_inputs[len(source_archives) :]
    end_dt = datetime.now()
    execution_seconds = round(time.perf_counter() - start_perf, 3)

    summary = {
        "run_timestamp": run_dir.name,
        "start_time": start_dt.isoformat(timespec="seconds"),
        "end_time": end_dt.isoformat(timespec="seconds"),
        "execution_seconds": execution_seconds,
        "input_dir": str(input_dir),
        "output_root": str(output_root),
        "run_dir": str(run_dir),
        "input_mode": input_mode,
        "output_mode": output_mode,
        "grouping": grouping,
        "processed_archives": [path.name for path in source_archives],
        "processed_archive_destinations": moved_archive_destinations,
        "processed_loose_files": [path.name for path in loose_files],
        "processed_loose_file_destinations": moved_loose_file_destinations,
        "processed_input_destinations": moved_inputs,
        "nested_archives": nested_archives,
        "created_outputs": created_outputs,
        "created_output_count": len(created_outputs),
        "metadata_files": metadata_files,
        "unmatched_files": unmatched_files,
        "ambiguous_matches": ambiguous_matches,
        "mapping_count": len(buckets),
        "matched_file_count": sum(
            item["file_count"]
            for item in created_outputs
            if item["output"]
            not in {
                build_output_name("unsorted", output_mode),
                build_output_name("metadata", output_mode),
            }
        ),
        "metadata_file_count": len(metadata_files),
        "unmatched_file_count": len(unmatched_files),
    }
    summary["created_archives"] = created_outputs
    summary["created_archive_count"] = len(created_outputs)
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (run_dir / f"run-{run_dir.name}.log").write_text(
        "\n".join(build_log_lines(summary)) + "\n",
        encoding="utf-8",
    )

    if not keep_extracted and extracted_root.exists():
        shutil.rmtree(extracted_root)

    return run_dir


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    try:
        run_dir = process_input_dir(
            input_dir=args.input_dir,
            output_root=args.output_root,
            keep_extracted=args.keep_extracted,
            include_archives=args.include_archives,
            input_mode=args.input_mode,
            output_mode=args.output_mode,
            grouping=args.grouping,
        )
    except Exception as exc:
        print(f"TEA assessment sorting failed: {exc}", file=sys.stderr)
        return 1

    print(f"TEA assessment sorting complete. Run output: {run_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
