# Configs

This folder stores shared repository configuration and validation reference files.

Current contents:

- `mapping-file.schema.json`
  High-level schema reference for mapping JSON files across assessment families.

Validation in this repo is intentionally lightweight and script-driven. The schema is a shared contract reference, while the scripts in `../scripts` enforce the practical checks used in CI.

