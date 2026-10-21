# Mapping Scripts AI Agent Guide

This file guides AI agents working inside `scripts/mappings/`.

## Scope

Use this area for:

- sorter and merger workflows
- mapping-specific automation
- helper logic that operates on assessment mapping files or related inputs

## Working Rules

- keep mapping automation aligned with the operator workflows in
  `docs/runbooks/tea/`
- preserve safe defaults for file-moving, sorting, and validation behavior
- prefer explicit option models over hidden mode-switching behavior
- update tests when changing sorter or merger behavior
- update parser help, tests, and the owning runbook when user-facing script
  behavior changes
