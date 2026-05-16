# CI Scripts AI Agent Guide

This file guides AI agents working inside `scripts/ci/`.

## Scope

Use this area for:

- project validation entrypoints
- mapping and documentation checks used by CI
- lightweight automation that defines the validation baseline

## Working Rules

- keep validation scripts runnable from the project root
- prefer deterministic checks with clear failure messages
- keep CI-facing scripts lightweight and dependency-conscious
- update `scripts/ci/README.md`, `.github/workflows/validate-repo.yml`, and
  related docs when validation behavior changes
- avoid mixing sorting, merging, or other operational workflows into `scripts/ci/`
