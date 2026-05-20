# SAT K-12 Reporting Agent Guide

This file guides AI agents working inside
`assessments/collegeboard/sat_suite/k12_reporting/sat/`.

## Scope

Use this folder for SAT K-12 reporting mappings and related maintenance docs.

## Working Rules

- keep SAT K-12 reporting mappings under
  `assessments/collegeboard/sat_suite/k12_reporting/sat/`
- preserve official SAT K-12 reporting metadata and archive references
- update `docs/source-archives/collegeboard/sat_suite/k12_reporting/sat/` with
  SAT source files before publishing mapping changes

## Agent Expectations

- create year-specific mappings only after the K-12 SAT format is confirmed
- keep field names aligned with College Board source semantics
- preserve source ordering, omitted blanks, and header uniqueness in mappings
