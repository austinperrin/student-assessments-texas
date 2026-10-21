# Troubleshoot TEA Processing

Use this runbook when a sorter or merger run has unexpected classifications,
missing outputs, duplicate rows, or a failure that may require a rerun.

## Preserve Evidence First

Do not delete or modify the timestamped run directory. Preserve:

- `summary-<run_timestamp>.json`
- `run-<run_timestamp>.log`
- `outputs/`
- `processed_files/`
- extracted working files when `--keep-extracted` was used

Do not immediately move inputs back to uploads. Both tools move successfully
processed top-level inputs, and returning them will make a later run process
them again.

## Triage Checklist

1. Confirm the command, input directory, and timestamped run directory.
2. Check the summary's processed loose files and source archives.
3. Check `unmatched_files` for files sent to `unsorted` or excluded from a
   merge.
4. Check `ambiguous_matches` for filenames matching multiple mapping patterns.
5. Check nested-archive counts when archives were expected.
6. For merges, check `unique_rows`, written rows, and skipped duplicate rows.
7. Compare the filename with `filename_patterns` in the expected mapping JSON.

## Common Outcomes

### A file was unmatched

Confirm that the filename is correct and that an official source supports the
expected pattern. Update a mapping pattern only when source documentation
justifies it; do not broaden a regex only to make one local file pass.

### A file matched more than one mapping

Use the summary's ambiguity record to identify every candidate. Compare those
patterns with their referenced source documents before changing precedence or
regexes.

### A merged row is missing

Deduplication is on by default. Check the skipped duplicate count and rerun with
`--allow-duplicates` only when retaining repeated logical rows is intended.

### An archive was ignored

The sorter needs `--input-mode archive`, `--input-mode all`, or the compatibility
flag `--include-archives`. The merger needs `--include-archives`.

### Output filenames changed

The sorter flattens assessment outputs. When source files have the same final
name, it adds a deterministic `__from_<source>` suffix to prevent overwrite.

## Safe Rerun Procedure

1. Preserve the original run directory.
2. Identify exactly which top-level inputs require reprocessing.
3. Copy those inputs from `processed_files/` into a new input directory below
   `.tmp/`; do not move them out of the original evidence directory.
4. Run the corrected command against that new input directory.
5. Compare the new summary and outputs with the original run.

For normal operation, return to the [sort runbook](./sort-assessment-files.md)
or [merge runbook](./merge-assessment-files.md).
