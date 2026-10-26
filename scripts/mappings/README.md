# Mapping Scripts

This folder contains mapping-specific automation and its tests. Operator-facing
procedures live in `docs/runbooks/`; this page focuses on implementation and
contributor navigation.

## Entrypoints

- `sort_tea_assessments.py`
  Thin entrypoint for the TEA sorter.
- `sort_archive_outputs.py`
  Sorter wrapper that selects archive output.
- `merge_tea_assessment_files.py`
  Thin entrypoint for the TEA merger.

## Reusable Modules

- `lib/tea_assessment_sorter.py`
  Argument parsing, mapping-pattern loading, recursive archive processing,
  classification, output management, run artifacts, and the sorter `main`.
- `lib/tea_assessment_merger.py`
  Argument parsing, recursive input processing, byte-preserving concatenation,
  row deduplication, bundled output, run artifacts, and the merger `main`.

## Tests

- `test_tea_assessment_sorter.py`
- `test_tea_assessment_merger.py`

Run the mapping-script tests from the repository root with the available Python
interpreter:

```powershell
python -m unittest discover -s scripts/mappings -p "test_tea_assessment_*.py"
```

Changes to classification, archive handling, naming, deduplication, output
layout, or CLI behavior should include corresponding tests.

## Documentation Ownership

- [Sort TEA assessment files](../../docs/runbooks/tea/sort-assessment-files.md)
  owns sorter defaults, options, examples, side effects, and verification.
- [Merge TEA assessment files](../../docs/runbooks/tea/merge-assessment-files.md)
  owns merger defaults, options, examples, side effects, and verification.
- [Troubleshoot TEA processing](../../docs/runbooks/tea/troubleshoot-processing.md)
  owns diagnosis and safe rerun guidance.
- [Scripts and commands index](../../docs/overview/scripts-and-commands.md)
  provides the concise repository-wide entrypoint list.

When a human-facing argument or behavior changes, update parser help, tests, and
the owning runbook in the same change. Follow the
[script standards](../../docs/standards/scripts.md) and
[documentation standards](../../docs/standards/documentation.md).
