# AP Agent Guide

This file guides AI agents working inside `assessments/collegeboard/ap/`.

## Scope

Use this folder for AP product mappings and related maintenance docs.

## Working Rules

- keep AP mapping assets under `assessments/collegeboard/ap/`
- preserve official AP source-document metadata and archive references
- keep K-12 and higher-ed AP score-report families separate when the source
  docs describe different delivered files
- update `docs/source-archives/collegeboard/ap/` with AP source files before
  publishing mapping changes

## Agent Expectations

- create year- or product-specific mapping files only after the AP format is
  confirmed
- choose the correct score-report family before creating year-specific mappings
- distinguish K-12 educator report layouts from higher-ed score-report layouts
  when the source docs split them
- keep field names aligned with College Board source semantics
- preserve source ordering, omitted blanks, and header uniqueness in mappings
