# STAAR Interim Mapping Maintenance Guide

This folder contains year-specific fixed-width mapping files for STAAR Interim data files.

## Source of Truth

For each file:

- use the corresponding TEA PDF in `../../docs`
- keep `metadata.pdf_url` aligned to the official PDF URL
- build field definitions from that year's PDF layout
- omit `metadata.administration_periods`

## File Naming

Use the ending school year:

`YYYY-staar-interim-fixed-width-mapping.json`

Example:

`2026-staar-interim-fixed-width-mapping.json`

## Routing Note

Treat `2023-crs-layout-interim-boy.pdf` as interim-related source material if it is ever mapped.
Do not route official `CRS Custom Data File Layout` / `CRS Data File Format` PDFs into this folder; those belong in the top-level `crs/` family.

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
- Normalize identifier headers as `peims_id`, `local_student_id`, and `tx_unique_student_id`.
- Use `family_portal_unique_access_code` if a future STAAR Interim layout adds a family or student portal unique access code field.
