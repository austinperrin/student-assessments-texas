# Scripts And Commands Reference

This page is the quick-reference glossary for repository entrypoints, common
commands, and sorter terminology.

## Command glossary

- `npm run format`
  Formats tracked repository docs, JSON, and config files with Prettier.
- `npm run format:check`
  Checks formatting without rewriting files.
- `npm run lint`
  Runs repository formatting checks plus the repository validation suite.
- `npm run lint:repo`
  Runs `python scripts/ci/validate_repo.py`.
- `python scripts/ci/validate_repo.py`
  Validates repository structure, documentation, mappings, and other shared
  repo rules.
- `python scripts/mappings/sort_tea_assessments.py [input_dir]`
  Sorts matched TEA assessment files into output buckets using configurable
  input mode, output mode, and grouping.
- `python scripts/mappings/sort_archive_outputs.py [input_dir]`
  Runs the sorter with archive output selected by default.
- `python scripts/mappings/merge_tea_assessment_files.py [input_dir]`
  Merges matched TEA assessment files into one `.txt` output per mapping file.

## Sorter defaults

The main sorter defaults are:

- input directory: `.tmp/uploads/`
- input mode: `loose`
- output mode: `directory`
- grouping: `assessment-by-year`
- output root: `.tmp/exports/`
- processed inputs root: `.tmp/processed_files/`

## Sorter option glossary

- `input mode`
  Controls which source items are eligible for sorting.
- `output mode`
  Controls whether each bucket is written as a directory or archive.
- `grouping`
  Controls whether outputs stay year-specific or collapse all years into one
  assessment bucket.
- `loose`
  Process only top-level non-archive files from the input directory.
- `archive`
  Process top-level `.zip` files from the input directory and recurse through
  nested archives.
- `all`
  Process both loose files and top-level archives.
- `directory`
  Write each output bucket as a normal directory.
- `assessment-by-year`
  Write year-specific output buckets such as `2026-staar-eoc`.
- `assessment`
  Write assessment-family buckets such as `staar/eoc` that combine all years.

## Sorter command patterns

Sort only loose files into year-specific directories:

```powershell
python scripts/mappings/sort_tea_assessments.py
```

Sort both loose files and archive contents into year-specific directories:

```powershell
python scripts/mappings/sort_tea_assessments.py --input-mode all
```

Sort only archive contents into year-specific directories:

```powershell
python scripts/mappings/sort_tea_assessments.py --input-mode archive
```

Sort both loose files and archive contents into year-specific archives:

```powershell
python scripts/mappings/sort_tea_assessments.py --input-mode all --output-mode archive
```

Sort loose files into assessment buckets that combine all years:

```powershell
python scripts/mappings/sort_tea_assessments.py --grouping assessment
```

Use the archive-output wrapper:

```powershell
python scripts/mappings/sort_archive_outputs.py --input-mode all
```

## Notes

- `--include-archives` is still accepted by the sorter as a compatibility
  shortcut for `--input-mode all`.
- The merger currently keeps its older archive-selection model and does not yet
  support the sorter's new grouping or output-mode concepts.
