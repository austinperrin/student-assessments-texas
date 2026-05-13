# TELPAS Alternate Fixed-Width Mappings

This folder contains fixed-width mapping files for TELPAS Alternate reporting student data files.

Each mapping follows the same structure as the STAAR and TELPAS mapping files:

- `metadata`
- `filename_patterns` when the file also documents supported delivered filename styles
- `mapped_fields`

Blank fields from the published layouts are intentionally omitted from `mapped_fields`, while `column_num` preserves the source layout sequence including those blanks.
When `filename_patterns` is present, each entry should include a `regex` string and a `references` array that ties the pattern back to source documentation.

Do not create duplicate `column_header` values. Normalize identifier fields as `peims_id`, `local_student_id`, and `tx_unique_student_id`; normalize portal access code fields as `family_portal_unique_access_code`.
