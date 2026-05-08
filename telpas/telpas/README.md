# TELPAS Fixed-Width Mappings

This folder contains year-specific fixed-width mapping files for TELPAS reporting student data files.

## File Naming

`YYYY-telpas-fixed-width-mapping.json`

## Source PDFs

Mappings are curated from the matching TELPAS data file layout PDFs in [docs](../../docs) and the official TEA PDF URL stored in each file's `metadata`.

## Notes

- Blank fields are omitted from `mapped_fields`.
- `column_num` preserves the source layout sequence, including omitted blank fields.
- Field titles are normalized into lowercase snake case.
