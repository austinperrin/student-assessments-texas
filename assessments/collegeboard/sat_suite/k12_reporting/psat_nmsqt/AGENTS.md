# PSAT/NMSQT Agent Guide

This file guides AI agents working inside
`assessments/collegeboard/sat_suite/k12_reporting/psat_nmsqt/`.

## Scope

Use this folder for PSAT/NMSQT product mappings and related maintenance docs.

## Working Rules

- keep PSAT/NMSQT mapping assets under
  `assessments/collegeboard/sat_suite/k12_reporting/psat_nmsqt/`
- preserve official PSAT/NMSQT source-document metadata and archive references
- keep PSAT/NMSQT within the SAT Suite family rather than a standalone PSAT
  family
- update
  `docs/source-archives/collegeboard/sat_suite/k12_reporting/psat_nmsqt/` with
  PSAT/NMSQT source files before publishing mapping changes

## Agent Expectations

- create year- or product-specific mapping files only after the PSAT/NMSQT
  format is confirmed
- confirm the source document is a K-12 reporting artifact
- do not invent differences from PSAT 10 unless the source file proves them
- keep field names aligned with College Board source semantics
- preserve source ordering, omitted blanks, and header uniqueness in mappings
