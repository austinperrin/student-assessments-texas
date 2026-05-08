# TELPAS Alternate Fixed-Width Mappings

This folder contains fixed-width mapping files for TELPAS Alternate reporting student data files.

Each mapping follows the same structure as the STAAR and TELPAS mapping files:

- `metadata`
- `mapped_fields`

Blank fields from the published layouts are intentionally omitted from `mapped_fields`, while `column_num` preserves the source layout sequence including those blanks.
