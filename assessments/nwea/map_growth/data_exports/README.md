# MAP Growth Data Exports

This folder is reserved for MAP Growth machine-readable export layouts.

## Expected Coverage

Current official NWEA help describes:

- a combined export delivered as a single CSV file
- a comprehensive export delivered as a ZIP package containing core CSV files
  and optional auxiliary CSV files
- automated retrieval support for scheduled export files

The first mapping pass here will likely split by delivered file shape rather
than collapsing all MAP Growth exports into one generic family.

## Suggested Future Layout

When mappings are added, a durable structure will likely look like:

- combined export mapping(s)
- comprehensive export mapping(s)
- auxiliary file mapping(s) for optional comprehensive export members

## Related References

- [../README.md](../README.md)
  MAP Growth family overview.
- [../../../../docs/source-archives/nwea/map_growth/data_exports/](../../../../docs/source-archives/nwea/map_growth/data_exports/)
  Local archive for MAP Growth export references.
