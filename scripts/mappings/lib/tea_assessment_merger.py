from __future__ import annotations

import argparse
import io
import json
import sys
import time
import zipfile
from collections import deque
from datetime import datetime
from pathlib import Path, PurePosixPath

from lib.tea_assessment_sorter import (
    DEFAULT_INPUT_ROOT,
    DEFAULT_MAPPING_ROOT,
    DEFAULT_OUTPUT_ROOT,
    DEFAULT_PROCESSED_ROOT,
    DEFAULT_UPLOADS_DIR,
    classify_file,
    create_run_dir,
    ensure_subpath,
    is_known_metadata_file,
    list_loose_files,
    list_source_archives,
    load_mapping_buckets,
    move_processed_inputs,
    safe_member_path,
    sanitize_name,
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Process TEA assessment files from a .tmp input directory, classify files "
            "using mapping filename_patterns, and merge one text file per mapping bucket."
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
        "--include-archives",
        action="store_true",
        help=(
            "Also include top-level .zip archives from the input directory. "
            "Only flat files directly inside the input directory are processed by default."
        ),
    )
    parser.add_argument(
        "--unique",
        action="store_true",
        help=(
            "Keep only the first occurrence of each logical row in every merged output file. "
            "Duplicate rows are skipped."
        ),
    )
    return parser.parse_args(argv)


class MergedOutputManager:
    def __init__(self, outputs_root: Path, unique_rows: bool = False):
        self.outputs_root = outputs_root
        self.unique_rows = unique_rows
        self.handles: dict[str, io.BufferedWriter] = {}
        self.files_written: dict[str, dict[str, object]] = {}
        self.seen_rows: dict[str, set[bytes]] = {}

    def append_bytes(self, output_name: str, src, source_path: str) -> None:
        handle = self.handles.get(output_name)
        if handle is None:
            destination = self.outputs_root / output_name
            destination.parent.mkdir(parents=True, exist_ok=True)
            handle = destination.open("ab")
            self.handles[output_name] = handle
            self.files_written[output_name] = {
                "file": output_name,
                "matched_files": [],
                "written_row_count": 0,
                "skipped_duplicate_row_count": 0,
            }
            self.seen_rows[output_name] = set()

        if self.unique_rows:
            self._append_unique_rows(output_name, src)
        else:
            self._append_all_bytes(output_name, src)
        matched_files = self.files_written[output_name]["matched_files"]
        assert isinstance(matched_files, list)
        matched_files.append(source_path)

    def _append_all_bytes(self, output_name: str, src) -> None:
        handle = self.handles[output_name]
        output_info = self.files_written[output_name]
        data = src.read()
        handle.write(data)
        output_info["written_row_count"] += self._count_logical_rows(data)

    def _append_unique_rows(self, output_name: str, src) -> None:
        handle = self.handles[output_name]
        seen_rows = self.seen_rows[output_name]
        output_info = self.files_written[output_name]

        for line in src:
            row_key = line.rstrip(b"\r\n")
            if row_key in seen_rows:
                output_info["skipped_duplicate_row_count"] += 1
                continue

            seen_rows.add(row_key)
            handle.write(line)
            output_info["written_row_count"] += 1

    @staticmethod
    def _count_logical_rows(data: bytes) -> int:
        if not data:
            return 0
        return len(data.splitlines())

    def build_created_outputs(self) -> list[dict[str, object]]:
        return [self.files_written[name] for name in sorted(self.files_written)]

    def close(self) -> None:
        for handle in self.handles.values():
            handle.close()


def build_log_lines(summary: dict[str, object]) -> list[str]:
    lines = [
        f"Run timestamp: {summary['run_timestamp']}",
        f"Start time: {summary['start_time']}",
        f"End time: {summary['end_time']}",
        f"Execution seconds: {summary['execution_seconds']}",
        f"Input directory: {summary['input_dir']}",
        f"Output root: {summary['output_root']}",
        f"Run directory: {summary['run_dir']}",
        f"Processed archive count: {len(summary['processed_archives'])}",
        f"Processed loose file count: {len(summary['processed_loose_files'])}",
        f"Created merged file count: {summary['created_merged_file_count']}",
        f"Nested archive count: {len(summary['nested_archives'])}",
        f"Matched file count: {summary['matched_file_count']}",
        f"Written row count: {summary['written_row_count']}",
        f"Skipped duplicate row count: {summary['skipped_duplicate_row_count']}",
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

    if summary["created_merged_files"]:
        lines.append("")
        lines.append("Created merged files:")
        for item in summary["created_merged_files"]:
            lines.append(
                f"- {item['file']} ({len(item['matched_files'])} source files, "
                f"{item['written_row_count']} rows written, "
                f"{item['skipped_duplicate_row_count']} duplicate rows skipped)"
            )

    if summary["metadata_files"]:
        lines.append("")
        lines.append("Known metadata files:")
        lines.extend(f"- {name}" for name in summary["metadata_files"])

    if summary["unmatched_files"]:
        lines.append("")
        lines.append("Unmatched files:")
        lines.extend(f"- {name}" for name in summary["unmatched_files"])

    if summary["ambiguous_matches"]:
        lines.append("")
        lines.append("Ambiguous matches:")
        for item in summary["ambiguous_matches"]:
            lines.append(
                f"- {item['file']} -> {item['selected_bucket']} "
                f"(also matched: {', '.join(item['matching_buckets'])})"
            )

    return lines


def process_archives_streaming(
    source_archives: list[Path],
    buckets,
    outputs_root: Path,
    loose_files: list[Path] | None = None,
    loose_source_label: str | None = None,
    unique_rows: bool = False,
) -> tuple[list[dict[str, object]], list[str], list[str], list[str], list[dict[str, object]]]:
    nested_archives: list[str] = []
    metadata_files: list[str] = []
    unmatched_files: list[str] = []
    ambiguous_matches: list[dict[str, object]] = []
    queue: deque[tuple[Path | None, bytes | None, tuple[str, ...], str, str]] = deque()
    writer = MergedOutputManager(outputs_root, unique_rows=unique_rows)

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

                    extracted_name = safe_path.name

                    if is_known_metadata_file(extracted_name):
                        metadata_files.append(archive_member_path)
                        continue

                    winner, matching_buckets, matching_patterns = classify_file(extracted_name, buckets)
                    if winner is None:
                        unmatched_files.append(archive_member_path)
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
                        writer.append_bytes(f"{winner.output_stem}.txt", src, archive_member_path)

        if loose_files:
            loose_source_label = loose_source_label or "loose-files"
            loose_source_stem = sanitize_name(loose_source_label)
            for loose_file in loose_files:
                logical_path = PurePosixPath(loose_source_stem, loose_file.name).as_posix()

                if is_known_metadata_file(loose_file.name):
                    metadata_files.append(logical_path)
                    continue

                winner, matching_buckets, matching_patterns = classify_file(loose_file.name, buckets)
                if winner is None:
                    unmatched_files.append(logical_path)
                    continue

                if len(matching_buckets) > 1:
                    ambiguous_matches.append(
                        {
                            "file": logical_path,
                            "selected_bucket": winner.output_stem,
                            "matching_buckets": matching_buckets,
                            "matching_patterns": matching_patterns,
                        }
                    )

                with loose_file.open("rb") as src:
                    writer.append_bytes(f"{winner.output_stem}.txt", src, logical_path)

        return (
            writer.build_created_outputs(),
            nested_archives,
            metadata_files,
            unmatched_files,
            ambiguous_matches,
        )
    finally:
        writer.close()


def process_input_dir(
    input_dir: Path,
    output_root: Path,
    include_archives: bool = False,
    unique_rows: bool = False,
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

    loose_files = list_loose_files(input_dir)
    source_archives = list_source_archives(input_dir) if include_archives else []
    if not loose_files and not source_archives:
        if include_archives:
            raise ValueError(f"No loose files or .zip archives found in {input_dir}")
        raise ValueError(
            f"No loose files found in {input_dir}. Pass --include-archives to also process .zip files."
        )

    buckets = load_mapping_buckets(mapping_root)
    run_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = create_run_dir(output_root, run_stamp)
    outputs_root = run_dir / "outputs"
    outputs_root.mkdir(parents=True, exist_ok=True)

    created_merged_files, nested_archives, metadata_files, unmatched_files, ambiguous_matches = (
        process_archives_streaming(
            source_archives,
            buckets,
            outputs_root,
            loose_files=loose_files,
            loose_source_label=sanitize_name(input_dir.name),
            unique_rows=unique_rows,
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
        "processed_archives": [path.name for path in source_archives],
        "processed_archive_destinations": moved_archive_destinations,
        "processed_loose_files": [path.name for path in loose_files],
        "processed_loose_file_destinations": moved_loose_file_destinations,
        "processed_input_destinations": moved_inputs,
        "nested_archives": nested_archives,
        "created_merged_files": created_merged_files,
        "created_merged_file_count": len(created_merged_files),
        "metadata_files": metadata_files,
        "unmatched_files": unmatched_files,
        "ambiguous_matches": ambiguous_matches,
        "mapping_count": len(buckets),
        "matched_file_count": sum(len(item["matched_files"]) for item in created_merged_files),
        "written_row_count": sum(item["written_row_count"] for item in created_merged_files),
        "skipped_duplicate_row_count": sum(
            item["skipped_duplicate_row_count"] for item in created_merged_files
        ),
        "metadata_file_count": len(metadata_files),
        "unmatched_file_count": len(unmatched_files),
        "unique_rows": unique_rows,
    }
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (run_dir / f"run-{run_dir.name}.log").write_text(
        "\n".join(build_log_lines(summary)) + "\n",
        encoding="utf-8",
    )

    return run_dir


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    try:
        run_dir = process_input_dir(
            input_dir=args.input_dir,
            output_root=args.output_root,
            include_archives=args.include_archives,
            unique_rows=args.unique,
        )
    except Exception as exc:
        print(f"TEA assessment merge failed: {exc}", file=sys.stderr)
        return 1

    print(f"TEA assessment merge complete. Run output: {run_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
