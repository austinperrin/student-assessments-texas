# Runbooks

Runbooks are the authoritative operating procedures for recurring repository
workflows. They describe how to select and run a tool, what it changes, how to
verify the result, and how to recover safely from common failures.

## TEA Processing

- [Sort TEA assessment files](./tea/sort-assessment-files.md)
  Classify inputs into assessment buckets while keeping files separate.
- [Merge TEA assessment files](./tea/merge-assessment-files.md)
  Combine content into one text output per mapping bucket.
- [Troubleshoot TEA processing](./tea/troubleshoot-processing.md)
  Diagnose classifications, missing output, duplicate handling, and reruns.

If you are unsure whether to sort or merge, decide whether downstream work
needs the original files kept separate. Sort to retain separate files; merge to
produce one combined output per mapping.

For a concise list of repository entrypoints, see the
[scripts and commands index](../overview/scripts-and-commands.md).

Return to the [Documentation Hub](../index.md) to choose another task path.
