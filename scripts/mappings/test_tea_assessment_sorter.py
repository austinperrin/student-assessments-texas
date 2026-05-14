from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from lib.tea_assessment_sorter import classify_file, load_mapping_buckets, process_input_dir


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def make_mapping(mapping_path: Path, regexes: list[str]) -> None:
    payload = {
        "metadata": [
            {
                "author": "Test",
                "date_created": "2026-05-13",
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


class TeaAssessmentSorterTests(unittest.TestCase):
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
                            "date_created": "2026-05-13",
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

    def test_process_input_dir_extracts_nested_archives_and_creates_unsorted_zip(self) -> None:
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
            write_zip(nested_zip, {"SF_0526_5_8_G05_A.txt": b"matched nested"})

            outer_zip = input_dir / "batch.zip"
            write_zip(
                outer_zip,
                {
                    "SF_0526_5_8_G08_B.txt": b"matched top level",
                    "notes.txt": b"unmatched",
                    "Readme.txt": b"metadata",
                    "nested.zip": nested_zip.read_bytes(),
                },
            )
            nested_zip.unlink()

            run_dir = process_input_dir(
                input_dir=input_dir,
                output_root=output_root,
                keep_extracted=False,
                include_archives=True,
                mapping_root=mapping_root,
                tmp_root=tmp_root,
                processed_root=processed_root,
            )

            outputs_root = run_dir / "outputs"
            matched_zip = outputs_root / "2026-staar-3-8.zip"
            metadata_zip = outputs_root / "metadata.zip"
            unsorted_zip = outputs_root / "unsorted.zip"
            summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
            log_files = list(run_dir.glob("run-*.log"))

            self.assertTrue(matched_zip.exists())
            self.assertTrue(metadata_zip.exists())
            self.assertTrue(unsorted_zip.exists())
            self.assertFalse((run_dir / "extracted").exists())
            self.assertEqual(1, len(log_files))
            self.assertEqual(["batch.zip"], summary["processed_archives"])
            self.assertEqual([], summary["processed_loose_files"])
            self.assertEqual(1, len(summary["nested_archives"]))
            self.assertEqual(1, summary["unmatched_file_count"])
            self.assertEqual(1, summary["metadata_file_count"])
            self.assertEqual(3, summary["created_archive_count"])
            self.assertIn("start_time", summary)
            self.assertIn("end_time", summary)
            self.assertIn("execution_seconds", summary)
            self.assertFalse(outer_zip.exists())
            self.assertTrue((processed_root / run_dir.name / "batch.zip").exists())

            with zipfile.ZipFile(matched_zip) as zf:
                self.assertEqual(
                    sorted(zf.namelist()),
                    [
                        "SF_0526_5_8_G05_A.txt",
                        "SF_0526_5_8_G08_B.txt",
                    ],
                )

            with zipfile.ZipFile(metadata_zip) as zf:
                self.assertEqual(["batch/Readme.txt"], zf.namelist())

            with zipfile.ZipFile(unsorted_zip) as zf:
                self.assertEqual(["notes.txt"], zf.namelist())

    def test_process_input_dir_processes_loose_files_by_default(self) -> None:
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
            (input_dir / "Readme.txt").write_bytes(b"metadata loose")
            (input_dir / "notes.txt").write_bytes(b"unmatched loose")

            run_dir = process_input_dir(
                input_dir=input_dir,
                output_root=output_root,
                keep_extracted=False,
                mapping_root=mapping_root,
                tmp_root=tmp_root,
                processed_root=processed_root,
            )

            outputs_root = run_dir / "outputs"
            matched_zip = outputs_root / "2026-staar-eoc.zip"
            metadata_zip = outputs_root / "metadata.zip"
            unsorted_zip = outputs_root / "unsorted.zip"
            summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))

            self.assertEqual([], summary["processed_archives"])
            self.assertEqual(
                ["notes.txt", "Readme.txt", "SF_1326_DISTRICT_A_V01.txt"],
                summary["processed_loose_files"],
            )
            self.assertEqual(3, len(summary["processed_input_destinations"]))
            self.assertTrue((processed_root / run_dir.name / "SF_1326_DISTRICT_A_V01.txt").exists())
            self.assertTrue(matched_zip.exists())
            self.assertTrue(metadata_zip.exists())
            self.assertTrue(unsorted_zip.exists())

            with zipfile.ZipFile(matched_zip) as zf:
                self.assertEqual(["SF_1326_DISTRICT_A_V01.txt"], zf.namelist())

            with zipfile.ZipFile(metadata_zip) as zf:
                self.assertEqual(["uploads/Readme.txt"], zf.namelist())

            with zipfile.ZipFile(unsorted_zip) as zf:
                self.assertEqual(["notes.txt"], zf.namelist())

    def test_duplicate_names_use_source_archive_stem_suffix(self) -> None:
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

            write_zip(input_dir / "first source.zip", {"SAME_NAME.txt": b"first"})
            write_zip(input_dir / "second source.zip", {"SAME_NAME.txt": b"second"})

            run_dir = process_input_dir(
                input_dir=input_dir,
                output_root=output_root,
                keep_extracted=False,
                include_archives=True,
                mapping_root=mapping_root,
                tmp_root=tmp_root,
                processed_root=processed_root,
            )

            with zipfile.ZipFile(run_dir / "outputs" / "2026-staar-3-8.zip") as zf:
                self.assertEqual(
                    sorted(zf.namelist()),
                    [
                        "SAME_NAME.txt",
                        "SAME_NAME__from_second-source.txt",
                    ],
                )

    def test_repo_mapping_patterns_cover_documented_loose_file_variants(self) -> None:
        buckets = load_mapping_buckets()
        cases = {
            "SF_0524_3-8_068901_ECTOR COUNTY IS_V01.txt": "2024-staar-3-8",
            "SP_0525_3-8_068901_ECTOR COUNTY IS_V01.txt": "2025-staar-3-8",
            "SF_0424_3_8ALT_068901_ECTOR_COUNTY_IS_V01.txt": "2024-staar-alt2-3-8",
            "SF_1324_EOC_068901_ECTOR COUNTY IS_V02.txt": "2025-staar-eoc",
            "SF_1524_EOCALT_068901_ECTOR_COUNTY_IS_V01.txt": "2024-staar-alt2-eoc",
            "SF_0324_TELPAS_068901_ECTOR COUNTY IS_V01.txt": "2024-telpas",
            "SP_0325_TELPASALT_068901_ECTOR COUNTY IS_V02.txt": "2025-telpas-alt",
        }

        for file_name, expected_bucket in cases.items():
            winner, _, _ = classify_file(file_name, buckets)
            self.assertIsNotNone(winner, msg=file_name)
            self.assertEqual(expected_bucket, winner.output_stem, msg=file_name)

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
                keep_extracted=False,
                mapping_root=mapping_root,
                tmp_root=tmp_root,
                processed_root=processed_root,
            )

            summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
            self.assertEqual([], summary["processed_archives"])
            self.assertEqual(["SF_1326_DISTRICT_A_V01.txt"], summary["processed_loose_files"])
            self.assertTrue((input_dir / "batch.zip").exists())
            self.assertTrue((processed_root / run_dir.name / "SF_1326_DISTRICT_A_V01.txt").exists())


if __name__ == "__main__":
    unittest.main()
