# Repository Agent Guide

This file is the top-level maintenance guide for AI agents working in this repository.

## Scope

This repository stores fixed-width JSON mapping files for Texas assessment data layouts plus the local reference documents used to curate them.

Primary mapping families:

- `staar/3_8`
- `staar/eoc`
- `staar/alt2_3_8`
- `staar/alt2_eoc`
- `staar/interim`
- `staar/consolidated_accountability`
- `telpas/telpas`
- `telpas/telpas_alt`
- `tfar`
- `ttap`
- `crs`

Use the family-specific `AGENTS.md` files inside those folders for family-level rules and exceptions.

## Source Material

- the official TEA PDF for the current mapping year is the source of truth
- local reference PDFs live under `docs/tea-data-file-formats-archive/<year>/`
- `metadata.pdf_url` should remain aligned to the official source URL
- do not infer field names from neighboring years when the current PDF is clear
- do not create local `tmp_*.txt`, extracted plain-text PDF dumps, or similar scratch files in the repo when reviewing PDFs

## Documentation Link Rules

- use repo-relative links in repository documentation
- do not write machine-specific absolute paths such as `C:/Users/...` into `README.md`, `AGENTS.md`, or other tracked docs
- keep documentation portable across users, machines, and environments

## Shared Mapping Rules

- preserve the repository-wide JSON shape of `metadata` plus `mapped_fields`
- store mapping values as strings
- omit blank source fields from `mapped_fields`
- preserve source ordering in `column_num`, including gaps caused by omitted blank fields
- use lowercase snake case for `column_header`
- remove note spillover, wrapped-title spillover, and OCR debris from field names
- do not allow duplicate `column_header` values in a file

## Shared Normalization Rules

Normalize these identifiers and recurring concepts when the source meaning matches:

- `peims_id`
- `local_student_id`
- `tx_unique_student_id`
- `family_portal_unique_access_code`
- `emergent_bilingual_indicator_code`
- `gifted_and_talented_indicator_code`

Do not normalize away real meaning changes when TEA changed the field concept rather than just the label.

## Year Naming

- for single-year PDFs, use that year in the mapping filename
- for school-year PDFs, use the ending year in the mapping filename

Examples:

- `2023-2024-staar-interim-data-file-format.pdf` -> `2024-staar-interim-fixed-width-mapping.json`
- `2024-2025-crs-data-file-format.pdf` -> `2025-crs-custom-fixed-width-mapping.json`

## Validation

After editing or adding mappings:

1. confirm the JSON parses cleanly
2. confirm `column_header` values are unique
3. confirm the file still reflects the current year's PDF rather than a neighboring year
4. keep folder-specific `README.md` and `AGENTS.md` guidance aligned when the local doc layout changes
