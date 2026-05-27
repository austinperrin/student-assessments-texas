# Assessments

This folder stores the current assessment mapping corpus grouped first by
vendor or source system.

## Navigate

- [tea/](./tea/)
  Texas Education Agency and Texas Assessments mapping families and related
  maintenance docs.
- [collegeboard/](./collegeboard/)
  College Board result-delivery families, assessment variants, and associated
  mapping guidance.
- [iready/](./iready/)
  i-Ready assessment scaffolding and future export-family mapping guidance.
- [nwea/](./nwea/)
  NWEA MAP Suite assessment families and source-aligned delivery-format
  scaffolding.

## Working Rule

Add future vendor or platform groupings here rather than creating new
assessment families directly at the project root.

Within a vendor, prefer durable delivery-format or reporting-family folders over
marketing-program folders when the file layouts are emitted through distinct
systems or audiences.

When useful, the default structure should read as:

- vendor
- delivery family or reporting system
- assessment variant
- year or effective period

## Related References

- [../README.md](../README.md)
  Project overview and validation entrypoints.
- [../docs/index.md](../docs/index.md)
  Documentation system index.
- [../docs/source-archives/](../docs/source-archives/)
  Shared local archive root for vendor-specific source documents.
- [../configs/README.md](../configs/README.md)
  Shared schema and configuration references used by the corpus.
