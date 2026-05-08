# STAAR Interim Fixed-Width Mappings

This folder contains fixed-width mapping files for STAAR Interim data files.

Each mapping follows the same structure as the other STAAR mapping files:

- `metadata`
- `mapped_fields`

Blank fields from the published layouts are intentionally omitted from `mapped_fields`, while `column_num` preserves the source layout sequence including those blanks.

Do not create duplicate `column_header` values. Normalize identifier fields as `peims_id`, `local_student_id`, and `tx_unique_student_id`.
