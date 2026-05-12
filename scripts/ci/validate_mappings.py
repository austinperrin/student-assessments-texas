from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
FAMILY_DIRS = [
    REPO_ROOT / "staar",
    REPO_ROOT / "telpas",
    REPO_ROOT / "tfar",
    REPO_ROOT / "ttap",
    REPO_ROOT / "crs",
]
SCHOOL_YEAR_RE = re.compile(r"^\d{4}-\d{4}$")
INT_STRING_RE = re.compile(r"^\d+$")
HEADER_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")


def iter_mapping_files() -> list[Path]:
    files: list[Path] = []
    for family_dir in FAMILY_DIRS:
        if not family_dir.exists():
            continue
        files.extend(sorted(family_dir.rglob("*mapping.json")))
    return files


def validate_metadata(path: Path, metadata: list[dict], errors: list[str]) -> None:
    if not isinstance(metadata, list) or not metadata:
        errors.append(f"{path}: metadata must be a non-empty array")
        return

    first = metadata[0]
    required = ["author", "date_created", "file_name", "school_year", "pdf_url"]
    for key in required:
        if key not in first or not isinstance(first[key], str) or not first[key].strip():
            errors.append(f"{path}: metadata[0].{key} must be a non-empty string")

    if first.get("file_name") != path.name:
        errors.append(
            f"{path}: metadata[0].file_name '{first.get('file_name')}' does not match filename '{path.name}'"
        )

    school_year = first.get("school_year")
    if isinstance(school_year, str) and not SCHOOL_YEAR_RE.match(school_year):
        errors.append(f"{path}: metadata[0].school_year must match YYYY-YYYY")


def validate_mapped_fields(path: Path, mapped_fields: list[dict], errors: list[str]) -> None:
    if not isinstance(mapped_fields, list):
        errors.append(f"{path}: mapped_fields must be an array")
        return

    seen_headers: set[str] = set()
    duplicate_headers: set[str] = set()
    for idx, field in enumerate(mapped_fields):
        if not isinstance(field, dict):
            errors.append(f"{path}: mapped_fields[{idx}] must be an object")
            continue

        for key in ["start_pos", "end_pos", "column_header"]:
            if key not in field or not isinstance(field[key], str) or not field[key].strip():
                errors.append(f"{path}: mapped_fields[{idx}].{key} must be a non-empty string")

        column_num = field.get("column_num")
        numeric_values: dict[str, int] = {}
        if "column_num" in field and not isinstance(column_num, str):
            errors.append(f"{path}: mapped_fields[{idx}].column_num must be a string when present")

        for key in ["start_pos", "end_pos", "column_num"]:
            value = field.get(key)
            if isinstance(value, str) and value.strip():
                if not INT_STRING_RE.match(value):
                    errors.append(f"{path}: mapped_fields[{idx}].{key} must contain only digits")
                else:
                    numeric_values[key] = int(value)

        header = field.get("column_header")
        if isinstance(header, str):
            if not HEADER_RE.match(header):
                errors.append(
                    f"{path}: mapped_fields[{idx}].column_header '{header}' must be lowercase snake case"
                )
            if header in seen_headers:
                duplicate_headers.add(header)
            seen_headers.add(header)

        start_pos = numeric_values.get("start_pos")
        end_pos = numeric_values.get("end_pos")

        if start_pos is not None and end_pos is not None and end_pos < start_pos:
            errors.append(
                f"{path}: mapped_fields[{idx}] has end_pos '{end_pos}' before start_pos '{start_pos}'"
            )

    for header in sorted(duplicate_headers):
        errors.append(f"{path}: duplicate column_header '{header}'")


def main() -> int:
    errors: list[str] = []
    files = iter_mapping_files()

    if not files:
        print("No mapping files found.")
        return 1

    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # pragma: no cover
            errors.append(f"{path}: failed to parse JSON ({exc})")
            continue

        if not isinstance(data, dict):
            errors.append(f"{path}: top-level JSON must be an object")
            continue

        validate_metadata(path, data.get("metadata"), errors)
        validate_mapped_fields(path, data.get("mapped_fields"), errors)

    if errors:
        print("Mapping validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(files)} mapping files successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
