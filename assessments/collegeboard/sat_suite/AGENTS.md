# SAT Suite Agent Guide

This file guides AI agents working inside
`assessments/collegeboard/sat_suite/`.

## Scope

Use this folder for SAT Suite product mappings and related maintenance docs.

## Working Rules

- keep SAT Suite mapping assets under `assessments/collegeboard/sat_suite/`
- preserve official SAT Suite source-document metadata and archive references
- keep K-12 and higher-ed reporting outputs in separate delivery-family folders
- keep the SAT, PSAT/NMSQT, PSAT 10, and PSAT 8/9 as child assessments of the
  relevant delivery family
- keep suite-level guides and manuals with this family even when a source file
  covers multiple assessments
- update `docs/source-archives/collegeboard/sat_suite/` with the matching
  source files before publishing mapping changes

## Agent Expectations

- create year- or product-specific mapping files only after the SAT Suite
  format is confirmed
- choose the delivery-family folder before choosing the assessment child folder
- preserve shared layouts between PSAT/NMSQT and PSAT 10 unless the source
  document proves a real difference
- keep field names aligned with College Board source semantics
- preserve source ordering, omitted blanks, and header uniqueness in mappings
