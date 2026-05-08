# TELPAS Fixed-Width Mappings

This folder contains fixed-width mapping files for TELPAS and TELPAS Alternate reporting student data files.

## Folders

- `telpas/`: TELPAS mappings
- `telpas_alt/`: TELPAS Alternate mappings

Each mapping uses the same top-level structure as the STAAR mapping files:

- `metadata`
- `mapped_fields`

Blank fields from the published layouts are intentionally omitted from `mapped_fields`, while `column_num` preserves the source layout sequence including those blanks.

## Header Conventions

Mapping files should not contain duplicate `column_header` values. Identifier fields should use `peims_id`, `local_student_id`, and `tx_unique_student_id` where those fields exist in the source layout. Portal access code fields should use `family_portal_unique_access_code`.
