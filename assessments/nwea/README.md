# NWEA Assessments

This folder is the vendor-level home for NWEA assessment mapping families and
related maintenance guidance.

## Purpose

Add NWEA assessment mapping folders here. For NWEA, the first grouping below
the vendor should usually reflect the assessment family used in current NWEA
documentation, with export or reporting-format folders underneath when the
delivered files differ.

Current scaffolded families include:

- `map_growth/`
  - `map_growth/data_exports/`

This scaffold combines two rules:

- NWEA currently presents MAP Growth as a core assessment product in the MAP
  Suite
- file mappings should align to durable delivered formats such as scheduled
  data exports or report exports, rather than to instructional add-ons or
  product marketing alone

MAP Spanish is not scaffolded as a separate top-level family because current
NWEA product guidance describes Spanish assessment support as part of MAP
Growth.

Each assessment family or export-format family includes its own `README.md`
describing source coverage, naming expectations, and any vendor-specific
mapping guidance.

## Current Status

This is an initial scaffold for NWEA assessments. No NWEA mappings have been
added yet.

The first mapping target is MAP Growth data exports, because NWEA documents
stable CSV export packages and automated retrieval workflows for those files.

## Related References

- [../README.md](../README.md)
  Top-level assessments corpus entrypoint.
- [../../docs/source-archives/nwea/](../../docs/source-archives/nwea/)
  NWEA source-document archive.
