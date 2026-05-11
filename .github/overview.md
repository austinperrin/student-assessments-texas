# GitHub Workflow Overview

This folder holds repository workflow automation and contribution templates.

## Current Contents

- `workflows/`
  CI-style validation for repository changes
- `PULL_REQUEST_TEMPLATE.md`
  Pull request checklist aligned to mapping and documentation work
- `ISSUE_TEMPLATE/`
  Lightweight intake forms for mapping and repository improvement work

## Current Automation Baseline

The repository currently favors a lightweight validation model:

- run repository validation on pull requests
- run the same validation on pushes to main working branches
- keep automation aligned to the repository's current data-first scope

As the repository grows into services or packages, this folder can expand to
include additional workflows for linting, tests, security checks, packaging, or
deployment.
