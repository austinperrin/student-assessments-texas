# STAAR Mapping Folders

This directory groups STAAR fixed-width mapping sets by assessment family.

## Navigate Families

- [3_8/](./3_8/)
  STAAR grades 3-8 fixed-width mapping files.
- [eoc/](./eoc/)
  STAAR End-of-Course fixed-width mapping files.
- [alt2_3_8/](./alt2_3_8/)
  STAAR Alternate 2 grades 3-8 fixed-width mapping files.
- [alt2_eoc/](./alt2_eoc/)
  STAAR Alternate 2 End-of-Course fixed-width mapping files.
- [consolidated_accountability/](./consolidated_accountability/)
  STAAR consolidated accountability fixed-width mapping files.
- [interim/](./interim/)
  STAAR Interim fixed-width mapping files.

## Source PDFs

The source layout PDFs remain in
[../../../docs/source-archives/tea/](../../../docs/source-archives/tea/).

## Maintenance Guides

- Each subdirectory includes its own `README.md` with local coverage notes and
  maintenance guidance

## Header Conventions

Mapping files should not contain duplicate `column_header` values. Identifier
fields should use the shared names `peims_id`, `local_student_id`, and
`tx_unique_student_id`; portal access code fields should use
`family_portal_unique_access_code` when present in the source layout.

## Related References

- [../README.md](../README.md)
  TEA assessment family overview.
- [../../../docs/standards/coding-standards.md](../../../docs/standards/coding-standards.md)
  Shared project mapping and documentation standards.
