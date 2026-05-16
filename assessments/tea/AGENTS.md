# TEA Assessments AI Agent Guide

This file guides AI agents working inside `assessments/tea/`.

## Scope

Use this area for mappings and maintenance docs tied to TEA and Texas
Assessments source layouts.

Current families:

- `staar/`
- `telpas/`
- `tfar/`
- `ttap/`
- `crs/`

## Working Rule

Keep TEA-specific assets and family guidance under this folder so future
non-TEA assessment vendors can be added alongside it under `assessments/`
without changing the broader project structure.

## Agent Expectations

- prefer the nearest family-level `AGENTS.md` when editing `staar/`, `telpas/`,
  `tfar/`, `ttap/`, or `crs/`
- keep TEA-specific workflow assumptions out of non-TEA folders
- preserve year-specific meaning differences instead of forcing cross-family
  uniformity
