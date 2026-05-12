# Scripts

This folder stores shared repository automation grouped by intent, following the
same high-level pattern used in larger repos while staying relative to this
repository's current mapping-first scope.

## Structure

- `bootstrap/`
  Project setup and environment bootstrapping scripts.
- `ci/`
  Validation and other CI-facing entrypoint scripts.
- `dev/`
  Local contributor workflow helpers such as wrapper scripts for repeated checks.
- `docs/`
  Documentation maintenance helpers.
- `mappings/`
  Mapping-specific automation such as normalization, audits, or future file scaffolding.
- `lib/`
  Shared helper code reused across multiple scripts.

## Current Bias

This repo is still primarily a mapping and documentation repository, so only
`ci/` is active today. The other folders establish a clean growth path without
forcing application-oriented categories that do not fit this project yet.

## Current Entry Points

- `python scripts/ci/validate_repo.py`
  Runs the baseline repository validation suite.

Add future script families as purpose-based subdirectories instead of growing a
flat list at the top of `scripts/`.
