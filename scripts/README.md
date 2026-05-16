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

This repo is still primarily a mapping and documentation repository, so `ci/`
and `mappings/` are the primary active script families today. The other
folders establish a clean growth path without forcing application-oriented
categories that do not fit this project yet.

## Current Entry Points

- `python scripts/ci/validate_repo.py`
  Runs the baseline repository validation suite.
- `npm run lint:format`
  Runs the formatting gate used by CI.
- `python scripts/mappings/sort_tea_assessments.py`
  Sorts TEA assessment files into assessment buckets with configurable input,
  output, and grouping behavior.
- `python scripts/mappings/sort_archive_outputs.py`
  Runs the sorter with archive output selected by default.
- `python scripts/mappings/merge_tea_assessment_files.py`
  Merges matched TEA assessment files into one text output per mapping bucket.

For the full glossary of repository commands and sorter terminology, see
[docs/overview/scripts-and-commands.md](../docs/overview/scripts-and-commands.md).

Add future script families as purpose-based subdirectories instead of growing a
flat list at the top of `scripts/`.
