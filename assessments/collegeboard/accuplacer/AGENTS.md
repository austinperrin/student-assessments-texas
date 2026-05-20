# Accuplacer Agent Guide

This file guides AI agents working inside `assessments/collegeboard/accuplacer/`.

## Scope

Use this folder for ACCUPLACER product mappings and related maintenance docs.

## Working Rules

- keep ACCUPLACER mapping assets under
  `assessments/collegeboard/accuplacer/`
- preserve official ACCUPLACER source-document metadata and archive references
- keep generic ACCUPLACER platform reports separate from TSIA2-specific files
- keep TSIA2 nested here when the source document comes from College Board's
  ACCUPLACER platform
- update `docs/source-archives/collegeboard/accuplacer/` with ACCUPLACER
  source files before publishing mapping changes

## Agent Expectations

- create year- or product-specific mapping files only after the ACCUPLACER
  format is confirmed
- choose between `platform_reports/` and `tsia2/` before creating year-specific
  mappings
- keep field names aligned with College Board source semantics
- preserve source ordering, omitted blanks, and header uniqueness in mappings
