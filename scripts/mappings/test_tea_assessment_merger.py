from __future__ import annotations

import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.tea_assessment_merger import parse_args, process_input_dir
from lib.tea_assessment_sorter import DEFAULT_OUTPUT_ROOT, DEFAULT_UPLOADS_DIR, classify_file, load_mapping_buckets


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def make_mapping(mapping_path: Path, regexes: list[str]) -> None:
    payload = {
        "metadata": [
            {
                "author": "Test",
                "date_created": "2026-05-14",
                "file_name": mapping_path.name,
                "school_year": "2025-2026",
                "pdf_url": "https://example.com/layout.pdf",
            }
        ],
        "filename_patterns": [
            {"regex": regex, "references": ["https://example.com/ref"]} for regex in regexes
        ],
        "mapped_fields": [
            {"start_pos": "1", "end_pos": "1", "column_header": "sample_field", "column_num": "1"}
        ],
    }
    write_json(mapping_path, payload)


def write_zip(path: Path, members: dict[str, bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, contents in members.items():
            zf.writestr(name, contents)


class TeaAssessmentMergerTests(unittest.TestCase):
    def test_parse_args_defaults_to_tea_tmp_directories(self) -> None:
        args = parse_args([])

        self.assertEqual(DEFAULT_UPLOADS_DIR, args.input_dir)
        self.assertEqual(DEFAULT_OUTPUT_ROOT, args.output_root)
        self.assertTrue(str(DEFAULT_UPLOADS_DIR).endswith(".tmp\\uploads\\tea"))
        self.assertTrue(str(DEFAULT_OUTPUT_ROOT).endswith(".tmp\\exports\\tea"))

    def test_load_mapping_buckets_only_includes_mappings_with_filename_patterns(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            mapping_root = temp_root / "assessments" / "tea"
            make_mapping(mapping_root / "staar" / "2026-staar-3-8-fixed-width-mapping.json", [r"^SF_0526_"])
            write_json(
                mapping_root / "staar" / "2026-staar-eoc-fixed-width-mapping.json",
                {
                    "metadata": [
                        {
                            "author": "Test",
                            "date_created": "2026-05-14",
                            "file_name": "2026-staar-eoc-fixed-width-mapping.json",
                            "school_year": "2025-2026",
                            "pdf_url": "https://example.com/layout.pdf",
                        }
                    ],
                    "mapped_fields": [
                        {
                            "start_pos": "1",
                            "end_pos": "1",
                            "column_header": "sample_field",
                            "column_num": "1",
                        }
                    ],
                },
            )

            buckets = load_mapping_buckets(mapping_root)

            self.assertEqual(1, len(buckets))
            self.assertEqual("2026-staar-3-8", buckets[0].output_stem)

    def test_classify_file_uses_deterministic_first_match(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            mapping_root = temp_root / "assessments" / "tea"
            make_mapping(mapping_root / "a-family" / "2026-a-fixed-width-mapping.json", [r"^FILE_"])
            make_mapping(mapping_root / "b-family" / "2026-b-fixed-width-mapping.json", [r"^FILE_"])

            buckets = load_mapping_buckets(mapping_root)
            winner, matching_buckets, _ = classify_file("FILE_SAMPLE.txt", buckets)

            self.assertIsNotNone(winner)
            self.assertEqual("2026-a", winner.output_stem)
            self.assertEqual(["2026-a", "2026-b"], matching_buckets)

    def test_process_input_dir_merges_loose_files_with_exact_contents(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            tmp_root = temp_root / ".tmp"
            input_dir = tmp_root / "uploads"
            output_root = tmp_root / "exports"
            processed_root = tmp_root / "processed_files"
            mapping_root = temp_root / "assessments" / "tea"

            make_mapping(
                mapping_root / "staar" / "2026-staar-eoc-fixed-width-mapping.json",
                [r"^SF_1326_.*\.txt$"],
            )

            input_dir.mkdir(parents=True, exist_ok=True)
            (input_dir / "SF_1326_DISTRICT_A_V01.txt").write_bytes(b"ROW0001\r\n")
            (input_dir / "SF_1326_DISTRICT_B_V01.txt").write_bytes(b"ROW0002\r\n")
            (input_dir / "Readme.txt").write_bytes(b"metadata loose")
            (input_dir / "notes.txt").write_bytes(b"unmatched loose")

            run_dir = process_input_dir(
                input_dir=input_dir,
                output_root=output_root,
                include_archives=False,
                mapping_root=mapping_root,
                tmp_root=tmp_root,
                processed_root=processed_root,
            )

            merged_file = run_dir / "outputs" / "2026-staar-eoc.txt"
            summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
            log_files = list(run_dir.glob("run-*.log"))

            self.assertTrue(merged_file.exists())
            self.assertEqual(b"ROW0001\r\nROW0002\r\n", merged_file.read_bytes())
            self.assertEqual([], summary["processed_archives"])
            self.assertEqual(
                sorted(
                    [
                        "Readme.txt",
                        "SF_1326_DISTRICT_A_V01.txt",
                        "SF_1326_DISTRICT_B_V01.txt",
                        "notes.txt",
                    ],
                    key=str.lower,
                ),
                sorted(summary["processed_loose_files"], key=str.lower),
            )
            self.assertEqual(1, summary["created_merged_file_count"])
            self.assertEqual(2, summary["matched_file_count"])
            self.assertEqual(2, summary["written_row_count"])
            self.assertEqual(0, summary["skipped_duplicate_row_count"])
            self.assertEqual(1, summary["metadata_file_count"])
            self.assertEqual(1, summary["unmatched_file_count"])
            self.assertEqual(["uploads/Readme.txt"], summary["metadata_files"])
            self.assertEqual(["uploads/notes.txt"], summary["unmatched_files"])
            self.assertEqual(1, len(log_files))
            self.assertTrue((processed_root / run_dir.name / "SF_1326_DISTRICT_A_V01.txt").exists())
            self.assertTrue((processed_root / run_dir.name / "SF_1326_DISTRICT_B_V01.txt").exists())

    def test_process_input_dir_merges_top_level_and_nested_archives(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            tmp_root = temp_root / ".tmp"
            input_dir = tmp_root / "uploads"
            output_root = tmp_root / "exports"
            processed_root = tmp_root / "processed_files"
            mapping_root = temp_root / "assessments" / "tea"

            make_mapping(
                mapping_root / "staar" / "2026-staar-3-8-fixed-width-mapping.json",
                [r"^SF_0526_5_8_G0[58](?:_.*)?(?:\.txt)?$"],
            )

            nested_zip = input_dir / "nested.zip"
            write_zip(nested_zip, {"SF_0526_5_8_G05_A.txt": b"NESTED\r\n"})

            outer_zip = input_dir / "batch.zip"
            write_zip(
                outer_zip,
                {
                    "SF_0526_5_8_G08_B.txt": b"TOPLEVEL\r\n",
                    "Readme.txt": b"metadata",
                    "notes.txt": b"unmatched",
                    "nested.zip": nested_zip.read_bytes(),
                },
            )
            nested_zip.unlink()

            run_dir = process_input_dir(
                input_dir=input_dir,
                output_root=output_root,
                include_archives=True,
                mapping_root=mapping_root,
                tmp_root=tmp_root,
                processed_root=processed_root,
            )

            merged_file = run_dir / "outputs" / "2026-staar-3-8.txt"
            summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))

            self.assertTrue(merged_file.exists())
            self.assertEqual(b"TOPLEVEL\r\nNESTED\r\n", merged_file.read_bytes())
            self.assertEqual(["batch.zip"], summary["processed_archives"])
            self.assertEqual([], summary["processed_loose_files"])
            self.assertEqual(1, len(summary["nested_archives"]))
            self.assertEqual(["batch/Readme.txt"], summary["metadata_files"])
            self.assertEqual(["batch/notes.txt"], summary["unmatched_files"])
            self.assertTrue((processed_root / run_dir.name / "batch.zip").exists())

    def test_duplicate_source_filenames_merge_cleanly_into_single_bucket(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            tmp_root = temp_root / ".tmp"
            input_dir = tmp_root / "uploads"
            output_root = tmp_root / "exports"
            processed_root = tmp_root / "processed_files"
            mapping_root = temp_root / "assessments" / "tea"

            make_mapping(
                mapping_root / "staar" / "2026-staar-3-8-fixed-width-mapping.json",
                [r"^SAME_NAME\.txt$"],
            )

            write_zip(input_dir / "first source.zip", {"SAME_NAME.txt": b"FIRST\r\n"})
            write_zip(input_dir / "second source.zip", {"SAME_NAME.txt": b"SECOND\r\n"})

            run_dir = process_input_dir(
                input_dir=input_dir,
                output_root=output_root,
                include_archives=True,
                mapping_root=mapping_root,
                tmp_root=tmp_root,
                processed_root=processed_root,
            )

            merged_file = run_dir / "outputs" / "2026-staar-3-8.txt"
            summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))

            self.assertEqual(b"FIRST\r\nSECOND\r\n", merged_file.read_bytes())
            self.assertEqual(1, summary["created_merged_file_count"])
            self.assertEqual(2, summary["matched_file_count"])
            self.assertEqual(2, summary["written_row_count"])
            self.assertEqual(0, summary["skipped_duplicate_row_count"])
            self.assertEqual(
                ["first-source/SAME_NAME.txt", "second-source/SAME_NAME.txt"],
                summary["created_merged_files"][0]["matched_files"],
            )

    def test_process_input_dir_ignores_archives_unless_requested(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            tmp_root = temp_root / ".tmp"
            input_dir = tmp_root / "uploads"
            output_root = tmp_root / "exports"
            processed_root = tmp_root / "processed_files"
            mapping_root = temp_root / "assessments" / "tea"

            make_mapping(
                mapping_root / "staar" / "2026-staar-eoc-fixed-width-mapping.json",
                [r"^SF_1326_.*\.txt$"],
            )

            input_dir.mkdir(parents=True, exist_ok=True)
            (input_dir / "SF_1326_DISTRICT_A_V01.txt").write_bytes(b"matched loose")
            write_zip(input_dir / "batch.zip", {"SF_1326_ARCHIVE_A_V01.txt": b"matched archive"})

            run_dir = process_input_dir(
                input_dir=input_dir,
                output_root=output_root,
                include_archives=False,
                mapping_root=mapping_root,
                tmp_root=tmp_root,
                processed_root=processed_root,
            )

            summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
            self.assertEqual([], summary["processed_archives"])
            self.assertEqual(["SF_1326_DISTRICT_A_V01.txt"], summary["processed_loose_files"])
            self.assertTrue((input_dir / "batch.zip").exists())
            self.assertTrue((processed_root / run_dir.name / "SF_1326_DISTRICT_A_V01.txt").exists())

    def test_process_input_dir_unique_rows_skips_duplicate_rows(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            tmp_root = temp_root / ".tmp"
            input_dir = tmp_root / "uploads"
            output_root = tmp_root / "exports"
            processed_root = tmp_root / "processed_files"
            mapping_root = temp_root / "assessments" / "tea"

            make_mapping(
                mapping_root / "staar" / "2026-staar-eoc-fixed-width-mapping.json",
                [r"^SF_1326_.*\.txt$"],
            )

            input_dir.mkdir(parents=True, exist_ok=True)
            (input_dir / "SF_1326_DISTRICT_A_V01.txt").write_bytes(b"ROW0001\r\nROW0002\r\n")
            (input_dir / "SF_1326_DISTRICT_B_V01.txt").write_bytes(b"ROW0002\r\nROW0003\r\n")

            run_dir = process_input_dir(
                input_dir=input_dir,
                output_root=output_root,
                include_archives=False,
                unique_rows=True,
                mapping_root=mapping_root,
                tmp_root=tmp_root,
                processed_root=processed_root,
            )

            merged_file = run_dir / "outputs" / "2026-staar-eoc.txt"
            summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))

            self.assertEqual(b"ROW0001\r\nROW0002\r\nROW0003\r\n", merged_file.read_bytes())
            self.assertTrue(summary["unique_rows"])
            self.assertEqual(2, summary["matched_file_count"])
            self.assertEqual(3, summary["written_row_count"])
            self.assertEqual(1, summary["skipped_duplicate_row_count"])
            self.assertEqual(3, summary["created_merged_files"][0]["written_row_count"])
            self.assertEqual(1, summary["created_merged_files"][0]["skipped_duplicate_row_count"])


if __name__ == "__main__":
    unittest.main()
