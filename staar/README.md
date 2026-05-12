# STAAR Mapping Folders

This directory groups STAAR fixed-width mapping sets by assessment family.

## Structure

- `3_8/` contains STAAR grades 3-8 fixed-width mapping files
- `eoc/` contains STAAR End-of-Course fixed-width mapping files
- `alt2_3_8/` contains STAAR Alternate 2 grades 3-8 fixed-width mapping files
- `alt2_eoc/` contains STAAR Alternate 2 End-of-Course fixed-width mapping files
- `consolidated_accountability/` contains STAAR consolidated accountability fixed-width mapping files
- `interim/` contains STAAR Interim fixed-width mapping files

## Source PDFs

The source layout PDFs remain in [`../docs`](../docs).

## Maintenance Guides

- See [`AGENTS.md`](./AGENTS.md) for top-level STAAR structure guidance
- Each subdirectory also includes its own `README.md` and `AGENTS.md`

## Header Conventions

Mapping files should not contain duplicate `column_header` values. Identifier fields should use the shared names `peims_id`, `local_student_id`, and `tx_unique_student_id`; portal access code fields should use `family_portal_unique_access_code` when present in the source layout.
