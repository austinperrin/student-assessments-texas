# MAP Growth Data Exports AI Agent Guide

This file guides AI agents working inside
`assessments/nwea/map_growth/data_exports/`.

## Scope

Use this folder for machine-readable MAP Growth export layouts documented by
NWEA.

## Working Rules

- keep scheduled export layouts under this folder
- model combined and comprehensive exports as separate mapping families if the
  field sets differ
- keep auxiliary export files such as `StudentBySchool.csv`,
  `AssessmentResults.csv`, `ClassAssignments.csv`, `ProgramAssignments.csv`,
  and `AccommodationAssignment.csv` aligned to the official NWEA references
- update `docs/source-archives/nwea/map_growth/data_exports/` with matching
  local references when those documents are archived
- note automated retrieval assumptions in family docs when they affect how a
  district receives the files
