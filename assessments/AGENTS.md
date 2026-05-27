# Assessments AI Agent Guide

This file guides AI agents working inside `assessments/`.

## Scope

Use this area for maintained assessment mapping assets such as:

- mapping JSON files
- family-level `README.md` and `AGENTS.md` files
- vendor-, delivery-family-, or assessment-specific organizational structure

## Working Rules

- keep canonical assessment assets under `assessments/` rather than under `services/`
- group content first by vendor or source system
- within a vendor, prefer durable result-delivery or reporting families before
  assessment variants when the delivered file layouts differ by audience,
  platform, or reporting system
- keep platform-specific code in `services/` or `packages/`, not alongside
  maintained mappings
- update nearby docs when folder structure or vendor grouping changes
- use the nearest deeper `AGENTS.md` before changing a specific vendor or
  family folder

Current active vendor grouping:

- `tea/`
- `collegeboard/`
- `iready/`
- `nwea/`

Future vendors should be added alongside existing vendor roots rather than at
the repo root.
