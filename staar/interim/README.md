# STAAR Interim Fixed-Width Mappings

This folder contains fixed-width mapping files for STAAR Interim data files.

Files in this folder use the ending school year as the filename year.
For example, the `2023-2024` PDF maps to `2024-staar-interim-fixed-width-mapping.json`, and the `2025-2026` PDF maps to `2026-staar-interim-fixed-width-mapping.json`.

The local `docs/2023/2023-crs-layout-interim-boy.pdf` file should be treated as interim-related reference material, not as part of the separate CRS Custom family.
By contrast, the official `CRS Custom Data File Layout` PDFs belong in the top-level `crs/` family.

Each mapping follows the same structure as the other STAAR mapping files:

- `metadata`
- `mapped_fields`

Blank fields from the published layouts are intentionally omitted from `mapped_fields`, while `column_num` preserves the source layout sequence including those blanks.

Do not create duplicate `column_header` values. Normalize identifier fields as `peims_id`, `local_student_id`, and `tx_unique_student_id`.

Unlike the main STAAR 3-8 and EOC files, Interim mappings do not use a `metadata.administration_periods` field.
