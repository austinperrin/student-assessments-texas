# STAAR Interim Fixed-Width Mappings

This folder contains fixed-width mapping files for STAAR Interim data files.

Files in this folder use the ending school year as the filename year.
For example, the `2023-2024` PDF maps to `2024-staar-interim-fixed-width-mapping.json`, and the `2025-2026` PDF maps to `2026-staar-interim-fixed-width-mapping.json`.

The local `docs/tea-data-file-formats-archive/2023/2023-crs-layout-interim-boy.pdf` file should be treated as interim-related reference material, not as part of the separate CRS Custom family.
By contrast, the official `CRS Custom Data File Layout` PDFs belong in `assessments/tea/crs/`.

Each mapping follows the same structure as the other STAAR mapping files:

- `metadata`
- `filename_patterns` when the file also documents supported delivered filename styles
- `mapped_fields`

Blank fields from the published layouts are intentionally omitted from `mapped_fields`, while `column_num` preserves the source layout sequence including those blanks.
When `filename_patterns` is present, each entry should include a `regex` string and a `references` array that ties the pattern back to source documentation.

Do not create duplicate `column_header` values. Normalize identifier fields as `peims_id`, `local_student_id`, and `tx_unique_student_id`.

Unlike the main STAAR 3-8 and EOC files, Interim mappings do not use a `metadata.administration_periods` field.
