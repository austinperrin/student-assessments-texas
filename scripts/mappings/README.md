# Mapping Scripts

This folder stores mapping-specific automation.

Use this area for scripts that normalize, audit, scaffold, sort, merge, or
otherwise assist with assessment mapping maintenance outside the top-level CI
entrypoints.

For a repository-wide command glossary, see
[docs/overview/scripts-and-commands.md](../../docs/overview/scripts-and-commands.md).

## Current Scripts

- `python scripts/mappings/sort_tea_assessments.py [input_dir]`
  Sorts TEA assessment files into assessment buckets using mapping
  `filename_patterns`.
- `python scripts/mappings/sort_archive_outputs.py [input_dir]`
  Runs the same sorter in archive-output mode by default.
- `python scripts/mappings/merge_tea_assessment_files.py [input_dir]`
  Merges matched fixed-width files into one `.txt` output per assessment
  bucket.

The reusable sorter logic lives in `scripts/mappings/lib/tea_assessment_sorter.py`.
The reusable merger logic lives in `scripts/mappings/lib/tea_assessment_merger.py`.

## Sorter

### Default workflow

Run the sorter from the repo root:

```powershell
python scripts/mappings/sort_tea_assessments.py
```

By default it uses:

- input: `.tmp/uploads/`
- output runs: `.tmp/exports/<run_timestamp>/`
- processed source inputs: `.tmp/processed_files/<run_timestamp>/`
- input mode: `loose`
- output mode: `directory`
- grouping: `assessment-by-year`

You can also point it at another `.tmp` subdirectory:

```powershell
python scripts/mappings/sort_tea_assessments.py .tmp/my-batch
```

### Common examples

Sort only loose files into directories by assessment and year:

```powershell
python scripts/mappings/sort_tea_assessments.py
```

Sort loose files and archive contents into directories by assessment and year:

```powershell
python scripts/mappings/sort_tea_assessments.py --input-mode all
```

Sort only archive contents into directories by assessment and year:

```powershell
python scripts/mappings/sort_tea_assessments.py --input-mode archive
```

Sort loose files and archive contents into archive outputs by assessment and year:

```powershell
python scripts/mappings/sort_tea_assessments.py --input-mode all --output-mode archive
```

Sort loose files into directories by assessment across all years:

```powershell
python scripts/mappings/sort_tea_assessments.py --grouping assessment
```

Use the archive-output wrapper instead of passing `--output-mode archive`:

```powershell
python scripts/mappings/sort_archive_outputs.py --input-mode all
```

### Option glossary

- `--input-mode loose`
  Process only top-level non-archive files from the input directory.
- `--input-mode archive`
  Process only top-level `.zip` files from the input directory, including
  nested archives recursively.
- `--input-mode all`
  Process both loose files and top-level `.zip` files.
- `--output-mode directory`
  Write each output bucket as a plain directory.
- `--output-mode archive`
  Write each output bucket as a `.zip` archive.
- `--grouping assessment-by-year`
  Keep year-specific output buckets such as `2026-staar-eoc` or
  `2025-telpas-alt`.
- `--grouping assessment`
  Collapse all years into assessment-family buckets such as `staar/eoc` or
  `telpas/telpas_alt`.
- `--keep-extracted`
  Keep extracted working files in the run directory for debugging.
- `--include-archives`
  Compatibility shortcut for `--input-mode all`.

### Behavior

- input directories must live under `.tmp/`
- nested `.zip` files are processed recursively when archive inputs are enabled
- files are matched against every mapping JSON under `assessments/tea/` that
  exposes `filename_patterns`
- matching is deterministic and produces one output bucket per selected
  grouping rule
- `assessment-by-year` buckets are flat names such as `2026-staar-3-8/` or
  `2026-staar-3-8.zip`
- `assessment` buckets can be nested paths such as `staar/eoc/` or
  `staar/eoc.zip`
- assessment outputs are flat within each bucket and contain only final file
  names
- metadata output preserves one source-folder level using
  `<source_folder_name>/<metadata_file_name>`
- files that match no mapping `filename_patterns` are written to `unsorted`
  output in the selected mode
- once a run completes, processed source files are moved out of uploads so the
  default workflow is safe to run multiple times per day

### Run artifacts

Each run creates a timestamped folder under `.tmp/exports/` containing:

- sorted output directories or archives, depending on `--output-mode`
- `metadata` output when known metadata files are found
- `unsorted` output when unmatched files remain
- `summary.json`
- `run-<run_timestamp>.log`

`summary.json` and the run log include:

- input mode, output mode, and grouping
- processed source archives
- processed loose files
- nested archives encountered
- created output buckets
- metadata files and unmatched files
- total output bucket count created by the run
- start time, end time, and total execution time

### Performance and debugging

- the default loose-file path is straightforward and avoids archive extraction
- archive input processing uses a streaming path that writes file contents
  directly from source archives into output buckets where possible
- use `--keep-extracted` only when you need extracted working files for
  debugging, since that path keeps more on-disk artifacts and is slower

## Merge Tool

### Default workflow

Run the merger from the repo root:

```powershell
python scripts/mappings/merge_tea_assessment_files.py
```

By default it uses:

- input: `.tmp/uploads/`
- output runs: `.tmp/exports/<run_timestamp>/`
- processed source inputs: `.tmp/processed_files/<run_timestamp>/`

You can also point it at another `.tmp` subdirectory:

```powershell
python scripts/mappings/merge_tea_assessment_files.py .tmp/my-batch
```

To also include archive `.zip` files from the base input directory:

```powershell
python scripts/mappings/merge_tea_assessment_files.py --include-archives
```

### Behavior

- input directories must live under `.tmp/`
- top-level non-`.zip` files in the input directory are processed by default
- top-level `.zip` files are ignored by default and can be included with
  `--include-archives`
- when `--include-archives` is used, both loose files and top-level `.zip`
  files directly inside the input directory are processed
- nested `.zip` files are processed recursively
- files are matched against every mapping JSON under `assessments/tea/` that
  exposes `filename_patterns`
- matching is deterministic and produces one merged output text file per
  mapping file, for example `2026-staar-3-8.txt`
- merged outputs preserve source bytes exactly; the tool concatenates matched
  file contents without adding separators or extra newlines
- known metadata files and unmatched files are excluded from merged outputs and
  are recorded in run artifacts instead
- once a run completes, processed source files are moved out of uploads so the
  default workflow is safe to run multiple times per day

### Run artifacts

Each run creates a timestamped folder under `.tmp/exports/` containing:

- merged assessment text files
- `summary.json`
- `run-<run_timestamp>.log`

`summary.json` and the run log include:

- processed source archives
- processed loose files
- nested archives encountered
- created merged output files
- metadata files and unmatched files
- ambiguous multi-match classifications
- start time, end time, and total execution time
