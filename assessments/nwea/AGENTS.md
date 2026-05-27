# NWEA Assessments AI Agent Guide

This file guides AI agents working inside `assessments/nwea/`.

## Scope

Use this area for mapping and maintenance assets tied to NWEA assessment
products and delivered result-file formats.

Current scaffolded NWEA families:

- `map_growth/`

## Working Rules

- keep this vendor grouping separate from `assessments/tea/` and
  `assessments/collegeboard/`
- add assessment-family folders under `assessments/nwea/` before adding
  year-specific mappings
- within an assessment family, prefer durable export or reporting-format
  folders when NWEA delivers more than one distinct machine-readable layout
- keep MAP Spanish notes inside the relevant assessment family when the source
  describes Spanish as part of MAP Growth rather than as a separate file family
- keep vendor-specific workflow assumptions in this folder and family-level
  docs
- update nearby docs in `docs/` when the vendor grouping or archive structure
  changes

## Agent Expectations

- create a `README.md` for each NWEA assessment family or export-format family
  before adding mapping files
- preserve source-document accuracy and official NWEA product or help-center
  links in mapping metadata
- model the delivered file family described by NWEA instead of inferring a
  cross-vendor taxonomy
- link archive files using repo-relative links in `docs/source-archives/nwea/`
