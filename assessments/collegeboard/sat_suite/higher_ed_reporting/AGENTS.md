# SAT Suite Higher-Ed Reporting Agent Guide

This file guides AI agents working inside
`assessments/collegeboard/sat_suite/higher_ed_reporting/`.

## Scope

Use this folder for higher-ed SAT Suite result-file mappings and related
maintenance docs.

## Working Rules

- keep higher-ed SAT Suite mappings under
  `assessments/collegeboard/sat_suite/higher_ed_reporting/`
- use the matching assessment child folder before creating year-specific
  mappings
- update
  `docs/source-archives/collegeboard/sat_suite/higher_ed_reporting/` with the
  matching source files before publishing mapping changes

## Agent Expectations

- confirm the source document is a higher-ed reporting artifact rather than a
  K-12 reporting artifact
- preserve source ordering, omitted blanks, and header uniqueness in mappings
- keep field names aligned with College Board source semantics
