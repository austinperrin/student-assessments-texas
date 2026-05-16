# Repository Overview

This repository is the source of truth for year-specific JSON mappings of Texas
assessment fixed-width student data layouts.

Today, the repository is primarily a curated data and documentation workspace.
Over time, it is expected to grow into a broader application and tooling
platform that can validate, inspect, transform, and operationalize these
mapping files.

## Current Focus

- preserve PDF-to-JSON mapping accuracy
- apply stable normalization standards where the field meaning truly matches
- keep family-level documentation and repository standards aligned
- maintain a clean local archive of TEA and Texas Assessments source documents
- keep the assessment corpus grouped under `assessments/` so future vendors can
  be added without reshaping the repo again

## Navigation

- [repository-navigation.md](./repository-navigation.md)
  Guide to the major repository areas and how to move between them.
- [scripts-and-commands.md](./scripts-and-commands.md)
  Command glossary for the active automation surface.
- [../index.md](../index.md)
  Central docs index.

## Planned Direction

The repository is intentionally being prepared for future growth without forcing
an application stack too early.

Expected future expansion areas include:

- `services/` for application or runtime services
- `packages/` for shared libraries, schemas, or reusable tooling
- `infra/` for deployment, runtime, or environment artifacts
- `scripts/` for repository automation grouped by purpose, including CI validation under `scripts/ci/`

Until those areas are actively used, the mapping families and their supporting
docs remain the primary working surface of the repository.
