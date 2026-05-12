# Assessments Agent Guide

This folder stores canonical assessment mappings and maintenance docs grouped by
vendor or source system.

## Scope

Use this area for source-of-truth assessment assets such as:

- mapping JSON files
- family-level `README.md` and `AGENTS.md` guidance
- vendor- or assessment-specific organizational structure

## Working Rules

- keep canonical assessment assets under `assessments/` rather than under `services/`
- group content first by vendor or source system
- keep platform-specific code in `services/` or `packages/`, not alongside the source mappings
- update nearby docs when folder structure or vendor grouping changes

Current active vendor grouping:

- `tea/`

Future vendors should be added alongside `tea/` rather than at the repo root.
