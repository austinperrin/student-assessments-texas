# PSAT 10 Agent Guide

This file guides AI agents working inside
`assessments/collegeboard/sat_suite/k12_reporting/psat_10/`.

## Scope

Use this folder for PSAT 10 product mappings and related maintenance docs.

## Working Rules

- keep PSAT 10 mapping assets under
  `assessments/collegeboard/sat_suite/k12_reporting/psat_10/`
- preserve official PSAT 10 source-document metadata and archive references
- keep PSAT 10 within the SAT Suite family rather than a standalone PSAT family
- update `docs/source-archives/collegeboard/sat_suite/k12_reporting/psat_10/`
  with PSAT 10 source files before publishing mapping changes

## Agent Expectations

- create year- or product-specific mapping files only after the PSAT 10 format
  is confirmed
- confirm the source document is a K-12 reporting artifact
- do not invent differences from PSAT/NMSQT unless the source file proves them
- keep field names aligned with College Board source semantics
- preserve source ordering, omitted blanks, and header uniqueness in mappings
