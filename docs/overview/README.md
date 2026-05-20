# Project Overview

This project curates year-specific JSON mappings, reference materials, and
supporting workflows for Texas student assessment data.

Today, the project is primarily focused on TEA and Texas Assessments
fixed-width layouts. Over time, it is expected to grow into a broader
assessment tooling platform that can validate, inspect, transform, and
operationalize these mappings and related artifacts.

The intended data-model direction for the corpus is to represent the assessment
result files districts, schools, and higher-ed institutions actually receive,
including both current and historic layouts.

## Current Focus

- preserve PDF-to-JSON mapping accuracy
- apply stable normalization standards where the field meaning truly matches
- keep family-level documentation and project standards aligned
- maintain a clean local archive of vendor source documents under `docs/source-archives/`
- keep the assessment corpus grouped under `assessments/` so future vendors can
  be added without reshaping the repo again
- organize non-TEA vendors around durable delivery or reporting families when
  those better explain the emitted files than assessment branding alone

## Navigation

- [repository-navigation.md](./repository-navigation.md)
  Guide to the major project areas and how to move between them.
- [scripts-and-commands.md](./scripts-and-commands.md)
  Command glossary for the active automation surface.
- [../index.md](../index.md)
  Central docs index.

## Planned Direction

The project is intentionally being prepared for future growth without forcing
an application stack too early.

Expected future expansion areas include:

- `services/` for application or runtime services
- `packages/` for shared libraries, schemas, or reusable tooling
- `infra/` for deployment, runtime, or environment artifacts
- `scripts/` for project automation grouped by purpose, including CI validation under `scripts/ci/`

Until those areas are actively used, the mapping families and their supporting
docs remain the primary working surface of the project.
