# TELPAS Fixed-Width Mappings

This folder contains fixed-width mapping files for TELPAS and TELPAS Alternate reporting student data files.

## Folders

- `telpas/`: TELPAS mappings
- `telpas_alt/`: TELPAS Alternate mappings

Each mapping uses the same top-level structure as the STAAR mapping files:

- `metadata`
- `mapped_fields`

Blank fields from the published layouts are intentionally omitted from `mapped_fields`, while `column_num` preserves the source layout sequence including those blanks.
