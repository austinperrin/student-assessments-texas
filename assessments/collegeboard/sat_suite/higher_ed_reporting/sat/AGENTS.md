# SAT Higher-Ed Reporting Agent Guide

This file guides AI agents working inside
`assessments/collegeboard/sat_suite/higher_ed_reporting/sat/`.

## Scope

Use this folder for SAT higher-ed reporting mappings and related maintenance
docs.

## Working Rules

- keep SAT higher-ed reporting mappings under
  `assessments/collegeboard/sat_suite/higher_ed_reporting/sat/`
- preserve official SAT higher-ed reporting metadata and archive references
- update
  `docs/source-archives/collegeboard/sat_suite/higher_ed_reporting/sat/` with
  SAT source files before publishing mapping changes

## Agent Expectations

- create year-specific mappings only after the higher-ed SAT format is
  confirmed
- keep field names aligned with College Board source semantics
- preserve source ordering, omitted blanks, and header uniqueness in mappings
