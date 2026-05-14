from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from sort_zip_archives import classify_file, load_mapping_buckets, process_input_dir


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


class SortZipArchivesTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
