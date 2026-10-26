# Scripts And Commands Index

This page is the concise index of repository entrypoints. Operational defaults,
options, examples, side effects, verification, and recovery guidance live in
the linked runbooks.

## Repository Maintenance

- `npm run format`
  Formats repository-managed documentation, JSON, and configuration files.
- `npm run format:check`
  Checks formatting without rewriting files.
- `npm run lint:format`
  Runs the formatting gate used by CI.
- `npm run lint:repo`
  Runs `python scripts/ci/validate_repo.py`.
- `npm run lint`
  Runs the formatting gate and repository validation suite.
- `npm run commitlint -- --edit <path>`
  Validates a commit-message file against the repository convention.
- `python scripts/ci/validate_repo.py`
  Validates repository structure, documentation, and mappings.

`npm run prepare` installs the repository's Husky hooks automatically during
normal npm installation; it is not a routine operator command.

## TEA Assessment Processing

- `python scripts/mappings/sort_tea_assessments.py [input_dir]`
  Classifies files into output buckets while keeping source files separate.
  See [Sort TEA assessment files](../runbooks/tea/sort-assessment-files.md).
- `python scripts/mappings/sort_archive_outputs.py [input_dir]`
  Runs the same sorter with per-bucket archive output selected.
  See [Sort TEA assessment files](../runbooks/tea/sort-assessment-files.md).
- `python scripts/mappings/merge_tea_assessment_files.py [input_dir]`
  Combines matched content into one text output per mapping bucket.
  See [Merge TEA assessment files](../runbooks/tea/merge-assessment-files.md).

For unexpected classifications, missing output, or safe rerun guidance, see
[Troubleshoot TEA processing](../runbooks/tea/troubleshoot-processing.md).

## Contributor References

- [Script standards](../standards/scripts.md)
- [Documentation standards](../standards/documentation.md)
- [Scripts implementation overview](../../scripts/README.md)
- [Mapping scripts implementation notes](../../scripts/mappings/README.md)
