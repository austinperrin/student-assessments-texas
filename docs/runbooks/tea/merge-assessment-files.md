# Merge TEA Assessment Files

Use the merger when all source content classified to the same mapping should be
combined into one text output. Use the [sort runbook](./sort-assessment-files.md)
when source files should remain separate inside assessment buckets.

## Prerequisites

- run commands from the repository root
- place source files in `.tmp/uploads/tea/`, or choose another input directory
  below `.tmp/`
- ensure the relevant mapping JSON has a matching `filename_patterns` entry

The merger moves successfully processed top-level input files into the run's
`processed_files/` directory. It preserves source bytes while concatenating
content and does not insert separators or newlines.

## Default Run

```powershell
python scripts/mappings/merge_tea_assessment_files.py
```

The default run processes top-level loose files and keeps only the first
occurrence of each logical row in every merged output.

## Common Scenarios

Include top-level zip files and recursively process nested archives:

```powershell
python scripts/mappings/merge_tea_assessment_files.py --include-archives
```

Keep duplicate rows:

```powershell
python scripts/mappings/merge_tea_assessment_files.py --allow-duplicates
```

Write merged text files inside one zip archive:

```powershell
python scripts/mappings/merge_tea_assessment_files.py --zip-outputs
```

Choose the bundle name:

```powershell
python scripts/mappings/merge_tea_assessment_files.py --zip-outputs --zip-output-name district-results.zip
```

Use another input directory below `.tmp/` and another run-output root:

```powershell
python scripts/mappings/merge_tea_assessment_files.py .tmp/my-batch --output-root .tmp/my-exports
```

## Options

| Argument                 | Default             | Behavior                                                                        |
| ------------------------ | ------------------- | ------------------------------------------------------------------------------- |
| `[input_dir]`            | `.tmp/uploads/tea/` | Input directory; it must resolve below `.tmp/`.                                 |
| `--output-root PATH`     | `.tmp/exports/tea/` | Parent directory for timestamped runs.                                          |
| `--include-archives`     | off                 | Also process top-level zip files and nested archives.                           |
| `--allow-duplicates`     | off                 | Keep every logical row instead of deduplicating.                                |
| `--unique`               | enabled             | Compatibility flag; deduplication is already the default.                       |
| `--zip-outputs`          | off                 | Put merged text outputs in one zip instead of separate files.                   |
| `--zip-output-name NAME` | generated           | Override the bundle name used by `--zip-outputs`; `.zip` is added when omitted. |

Use `python scripts/mappings/merge_tea_assessment_files.py --help` for the
parser's current argument syntax.

## Outputs And Merge Behavior

Each run creates `.tmp/exports/tea/<run_timestamp>/` by default, containing:

```text
<run_timestamp>/
├── outputs/
├── processed_files/
├── summary-<run_timestamp>.json
└── run-<run_timestamp>.log
```

- matching uses every TEA mapping JSON that exposes `filename_patterns`
- each mapping bucket becomes one output such as `2026-staar-3-8.txt`
- row deduplication is enabled by default and preserves the first occurrence
- `--allow-duplicates` retains every row
- `--unique` remains accepted only for compatibility
- known metadata and unmatched files are excluded from merged outputs and
  recorded in run artifacts
- ambiguous multi-match classifications are recorded in the summary and log
- with `--zip-outputs`, `outputs/` contains the single bundle and the merged
  text files live inside it

## Verify The Run

1. Open `summary-<run_timestamp>.json` and confirm the processed-input counts
   and `unique_rows` setting.
2. Review written-row and skipped-duplicate-row counts for every output.
3. Review metadata, unmatched files, and ambiguous matches.
4. Inspect `run-<run_timestamp>.log` for a readable execution summary.
5. Spot-check expected merged files or bundle members.
6. Confirm the original top-level inputs moved to `processed_files/`.

## Safe Reruns And Troubleshooting

Moving a processed input back into uploads will merge it again. Before rerunning,
determine whether duplicate-row handling and the selected input set match the
intended result. Preserve the original run directory and follow the
[troubleshooting runbook](./troubleshoot-processing.md).

## Implementation References

- [Mapping scripts implementation notes](../../../scripts/mappings/README.md)
- [Merger entrypoint](../../../scripts/mappings/merge_tea_assessment_files.py)
- [Merger tests](../../../scripts/mappings/test_tea_assessment_merger.py)
