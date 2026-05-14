# Mapping Scripts

This folder stores mapping-specific automation.

Use this area for scripts that normalize, audit, scaffold, or otherwise assist
with assessment mapping maintenance outside the top-level CI entrypoints.

## Current Scripts

- `python scripts/mappings/sort_tea_assessments.py [input_dir]`
  Processes TEA assessment files from `.tmp/`, classifies files using mapping
  `filename_patterns`, and writes sorted output archives plus run artifacts.

The reusable sorter logic lives in `scripts/mappings/lib/tea_assessment_sorter.py`.

## ZIP Sorter

### Default workflow

Run the sorter from the repo root:

```powershell
python scripts/mappings/sort_tea_assessments.py
```

By default it uses:

- input: `.tmp/uploads/`
- output runs: `.tmp/exports/<run_timestamp>/`
- processed source inputs: `.tmp/processed_files/<run_timestamp>/`

You can also point it at another `.tmp` subdirectory:

```powershell
python scripts/mappings/sort_tea_assessments.py .tmp/my-batch
```

To also include archive `.zip` files from the base input directory:

```powershell
python scripts/mappings/sort_tea_assessments.py --include-archives
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
- matching is deterministic and produces one output zip per mapping file, for
  example `2026-staar-3-8.zip`
- assessment output zips are flat and contain only final file names
- `metadata.zip` preserves one source-folder level using
  `<source_folder_name>/<metadata_file_name>`
- files that match no mapping `filename_patterns` are written to `unsorted.zip`
- once a run completes, processed source files are moved out of uploads so
  the default workflow is safe to run multiple times per day

### Run artifacts

Each run creates a timestamped folder under `.tmp/exports/` containing:

- sorted output archives
- `metadata.zip` when known metadata files are found
- `unsorted.zip` when unmatched files remain
- `summary.json`
- `run-<run_timestamp>.log`

`summary.json` and the run log include:

- processed source archives
- processed loose files
- processed source archives when `--include-archives` is used
- nested archives encountered
- created output archives
- metadata files and unmatched files
- total archive count created by the run
- start time, end time, and total execution time

### Performance and debugging

- the default loose-file path is straightforward and avoids archive extraction
- `--include-archives` uses a streaming archive path that writes file contents
  directly from source archives into output archives where possible
- use `--keep-extracted` only when you need extracted working files for
  debugging, since that path keeps more on-disk artifacts and is slower
