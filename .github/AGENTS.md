# GitHub AI Agent Guide

This file guides AI agents working inside `.github/`.

## Scope

Use this area for:

- workflow definitions under `workflows/`
- pull request and issue templates
- contributor-facing automation guidance

## Working Rules

- keep workflow names, step names, and validation commands aligned with current
  scripts and `package.json`
- prefer explicit, readable CI steps over dense one-liners
- update `.github/overview.md` when workflow responsibilities or template
  expectations materially change
- keep contributor templates human-readable and consistent with current project
  standards
- avoid adding workflow complexity that does not match the current project size
