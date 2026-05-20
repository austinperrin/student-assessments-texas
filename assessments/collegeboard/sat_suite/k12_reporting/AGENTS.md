# SAT Suite K-12 Reporting Agent Guide

This file guides AI agents working inside
`assessments/collegeboard/sat_suite/k12_reporting/`.

## Scope

Use this folder for K-12 SAT Suite result-file mappings and related
maintenance docs.

## Working Rules

- keep K-12 SAT Suite mappings under
  `assessments/collegeboard/sat_suite/k12_reporting/`
- use the matching assessment child folder before creating year-specific
  mappings
- update `docs/source-archives/collegeboard/sat_suite/k12_reporting/` with the
  matching source files before publishing mapping changes

## Agent Expectations

- confirm the source document is a K-12 reporting artifact rather than a
  higher-ed reporting artifact
- preserve source ordering, omitted blanks, and header uniqueness in mappings
- keep field names aligned with College Board source semantics
