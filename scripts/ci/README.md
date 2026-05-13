# CI Scripts

This folder contains scripts used by repository validation and other CI-facing automation.

Current scripts:

- `validate_repo.py`
  Runs the baseline repository validation suite.
- `validate_mappings.py`
  Validates mapping JSON structure and shared field rules.
- `validate_docs.py`
  Validates documentation path portability and repo-relative links.

Node-based repo tooling complements these scripts:

- `npm run format`
  Applies `prettier` formatting across repo-managed text files.
- `npm run lint`
  Runs `prettier --check` plus `validate_repo.py`.
- `npm run commitlint -- --edit <path>`
  Validates a commit message against the conventional commit rules used by the Git hook.
