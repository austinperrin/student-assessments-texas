# Sort TEA Assessment Files

Use the sorter when source files should remain separate and be classified into
assessment output buckets. Use the [merge runbook](./merge-assessment-files.md)
when each mapping bucket should become one combined text file instead.

## Prerequisites

- run commands from the repository root
- place source files in `.tmp/uploads/tea/`, or choose another input directory
  below `.tmp/`
- ensure the relevant mapping JSON has a matching `filename_patterns` entry

The sorter moves successfully processed top-level input files into the run's
`processed_files/` directory. Keep another copy outside the upload directory if
the original placement must be preserved.

## Default Run

```powershell
python scripts/mappings/sort_tea_assessments.py
```

The default run processes top-level loose files, writes year-specific output
directories, and creates a timestamped run below `.tmp/exports/tea/`.

## Common Scenarios

Process loose files and top-level archives, including nested archives:

```powershell
python scripts/mappings/sort_tea_assessments.py --input-mode all
```

Process archives only:

```powershell
python scripts/mappings/sort_tea_assessments.py --input-mode archive
```

Write each bucket as a zip archive:

```powershell
python scripts/mappings/sort_tea_assessments.py --input-mode all --output-mode archive
```

Use the archive-output wrapper, which selects archive output regardless of the
main sorter's default:

```powershell
python scripts/mappings/sort_archive_outputs.py --input-mode all
```

Combine years into assessment-family buckets:

```powershell
python scripts/mappings/sort_tea_assessments.py --grouping assessment
```

Bundle everything created under `outputs/` into one zip file:

```powershell
python scripts/mappings/sort_tea_assessments.py --zip-outputs
```

Use another input directory below `.tmp/` and another run-output root:

```powershell
python scripts/mappings/sort_tea_assessments.py .tmp/my-batch --output-root .tmp/my-exports
```

## Options

| Argument                        | Default             | Behavior                                                                        |
| ------------------------------- | ------------------- | ------------------------------------------------------------------------------- |
| `[input_dir]`                   | `.tmp/uploads/tea/` | Input directory; it must resolve below `.tmp/`.                                 |
| `--output-root PATH`            | `.tmp/exports/tea/` | Parent directory for timestamped runs.                                          |
| `--input-mode loose`            | selected            | Process top-level non-zip files only.                                           |
| `--input-mode archive`          |                     | Process top-level zip files and nested archives only.                           |
| `--input-mode all`              |                     | Process loose files and top-level zip files.                                    |
| `--include-archives`            | off                 | Compatibility shortcut that changes the default loose mode to `all`.            |
| `--output-mode directory`       | selected            | Write each bucket as a directory.                                               |
| `--output-mode archive`         |                     | Write each bucket as a zip archive.                                             |
| `--grouping assessment-by-year` | selected            | Create buckets such as `2026-staar-eoc`.                                        |
| `--grouping assessment`         |                     | Combine years into paths such as `staar/eoc`.                                   |
| `--keep-extracted`              | off                 | Retain extracted working files for debugging.                                   |
| `--zip-outputs`                 | off                 | Add one zip containing everything created in `outputs/`.                        |
| `--zip-output-name NAME`        | generated           | Override the bundle name used by `--zip-outputs`; `.zip` is added when omitted. |

Use `python scripts/mappings/sort_tea_assessments.py --help` for the parser's
current argument syntax.

## Outputs And Classification

Each run creates `.tmp/exports/tea/<run_timestamp>/` by default, containing:

```text
<run_timestamp>/
├── outputs/
├── processed_files/
├── summary-<run_timestamp>.json
└── run-<run_timestamp>.log
```

- matching uses every TEA mapping JSON that exposes `filename_patterns`
- `assessment-by-year` creates names such as `2026-staar-3-8`
- `assessment` creates family paths such as `staar/eoc`
- unmatched files go to an `unsorted` output
- recognized metadata goes to a `metadata` output and preserves one source
  folder level
- ambiguous matches are classified deterministically and recorded in the
  summary and log
- colliding final filenames receive a deterministic `__from_<source>` suffix
- nested zip files are processed recursively when archives are enabled
- `--keep-extracted` retains an additional working area; otherwise it is
  removed after a successful run

## Verify The Run

1. Open `summary-<run_timestamp>.json` and confirm the input mode, output mode,
   grouping, and processed-input counts.
2. Review `ambiguous_matches`, `unmatched_files`, and created output buckets.
3. Inspect `run-<run_timestamp>.log` for a readable execution summary.
4. Spot-check expected files in `outputs/`.
5. Confirm the original top-level inputs moved to `processed_files/`.

## Safe Reruns And Troubleshooting

Do not move a processed input back into uploads until you understand why a
rerun is needed; doing so will process it again. If the run was unexpected,
preserve the timestamped run directory and follow the
[troubleshooting runbook](./troubleshoot-processing.md).

## Implementation References

- [Mapping scripts implementation notes](../../../scripts/mappings/README.md)
- [Sorter entrypoint](../../../scripts/mappings/sort_tea_assessments.py)
- [Archive-output wrapper](../../../scripts/mappings/sort_archive_outputs.py)
- [Sorter tests](../../../scripts/mappings/test_tea_assessment_sorter.py)
