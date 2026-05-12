# TELPAS Fixed-Width Mappings

This folder contains year-specific fixed-width mapping files for TELPAS reporting student data files.

## File Naming

`YYYY-telpas-fixed-width-mapping.json`

## Source PDFs

Mappings are curated from the matching TELPAS data file layout PDFs in the appropriate year-based subfolder under [docs](../../../../docs) and the official TEA PDF URL stored in each file's `metadata`.

## Notes

- Blank fields are omitted from `mapped_fields`.
- `column_num` preserves the source layout sequence, including omitted blank fields.
- Field titles are normalized into lowercase snake case.
- `column_header` values must be unique within each JSON file.
- Identifier fields are normalized as `peims_id`, `local_student_id`, and `tx_unique_student_id` where present.
- Portal access code fields are normalized as `family_portal_unique_access_code`.
