# AP K-12 Score Reports Agent Guide

This file guides AI agents working inside
`assessments/collegeboard/ap/k12_score_reports/`.

## Scope

Use this folder for AP K-12 score-report mappings and related maintenance docs.

## Working Rules

- keep AP K-12 score-report mappings under
  `assessments/collegeboard/ap/k12_score_reports/`
- update `docs/source-archives/collegeboard/ap/k12_score_reports/` with the
  matching source files before publishing mapping changes

## Agent Expectations

- confirm the source document is a K-12 AP reporting artifact
- keep field names aligned with College Board source semantics
- preserve source ordering, omitted blanks, and header uniqueness in mappings
