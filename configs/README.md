# Configs

This folder stores shared project configuration and validation reference files.

## Current Contents

- [mapping-file.schema.json](./mapping-file.schema.json)
  High-level schema reference for mapping JSON files across assessment families.

## Role In The Project

Validation in this repo is intentionally lightweight and script-driven. The
schema is a shared contract reference, while the scripts in
[../scripts/ci/](../scripts/ci/) enforce the practical checks used in CI,
including shared mapping-field shape checks and documentation link safety.

## Related References

- [../scripts/README.md](../scripts/README.md)
  Automation and validation entrypoints.
- [../docs/standards/scripts.md](../docs/standards/scripts.md)
  Shared working standards for project scripts and validation tooling.
