# CRS Custom Mapping Maintenance Guide

This folder contains year-specific fixed-width mapping files for the CRS Custom family.

## Scope

Use this folder only for official TEA PDFs named like:

- `CRS Custom Data File Layout`
- `CRS Data File Format`

Do not use this folder for interim-only student-results layouts that happen to contain `CRS` in the filename.

## Source of Truth

For each mapping file:

- use the matching PDF in `../docs`
- keep `metadata.pdf_url` aligned to the official TEA PDF URL
- build field definitions from that exact year's layout

## File Naming

Use the ending school year as the filename year when the source PDF uses a school-year label.

Suggested pattern:

`YYYY-crs-custom-fixed-width-mapping.json`

Examples:

- `2023-crs-custom-fixed-width-mapping.json`
- `2025-crs-custom-fixed-width-mapping.json`

## Required JSON Structure

Each file contains:

- `metadata`
- `mapped_fields`

The `mapped_fields` entries use:

- `start_pos`
- `end_pos`
- `column_header`
- `column_num`

## Field Rules

- Store all values as strings.
- Omit blank fields.
- Keep `column_num` aligned to the source layout sequence, including omitted blank fields.
- Normalize field titles into lowercase snake case.
- Ensure `column_header` values are unique within each JSON file.
- Normalize identifier headers as `peims_id`, `local_student_id`, and `tx_unique_student_id` when those source fields appear.
- Use `family_portal_unique_access_code` for family or student portal unique access code fields when present in the source layout.
