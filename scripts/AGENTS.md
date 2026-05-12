# Scripts Agent Guide

This folder stores repository automation grouped by intent.

## Structure

- `bootstrap/`
  Project setup and environment bootstrapping scripts.
- `ci/`
  Validation and CI entrypoint scripts.
- `dev/`
  Local contributor workflow helpers that are safe to run during normal development.
- `docs/`
  Documentation maintenance and documentation-generation helpers.
- `mappings/`
  Mapping-specific automation such as normalization, auditing, or future scaffold helpers.
- `lib/`
  Shared helper modules used by multiple scripts.

## Working Rules

- keep scripts small and single-purpose
- prefer safe, repeatable behavior by default
- validate inputs explicitly and fail with actionable output
- document new script entrypoints in the nearest `README.md`
- keep this folder structure aligned with `docs/standards/scripts.md`

Do not add app- or platform-specific script categories unless the repository actually grows into those workflows.
