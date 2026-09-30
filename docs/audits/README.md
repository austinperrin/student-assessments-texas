# Repository Audits

This area contains durable plans, coverage records, review evidence, and closed
findings for source-fidelity audits. Each family/year is an independent work
unit in which Reviewer 1 completes the audit and supported corrections before
Reviewer 2 independently validates the final package.

## Contents

- [TEA assessment audit program](./tea/README.md)
- [TEA review checklist](./tea/review-checklist.md)
- [TEA finding template](./tea/finding-template.md)
- [TEA review record template](./tea/review-template.md)
- [TEA family audit template](./tea/family-audit-template.md)
- [TEA review record layout](./tea/reviews/README.md)
- [TEA coverage](./tea/coverage.md)
- [TEA audit roadmap](./tea/roadmap/index.md)
- [TEA audit workflow](./tea/workflow.md)

## Record Boundary

Track material needed to understand, verify, resume, and close an audit:

- scope and baseline
- coverage and reviewer assignments
- source citations and confirmed findings
- dispositions, remediation links, and verification results

Keep disposable material under `.tmp/audits/`, including PDF text extraction,
screenshots, ad hoc comparisons, and intermediate notes. Tracked audit records
must not link to `.tmp` artifacts.

## Audit And Correction

A year pull request contains the audit record, supported mapping corrections,
resolutions, and validation for exactly one family/year. Multiple year work
units may run in parallel from `main`. Shared coverage, family, and roadmap
files are updated separately by the program coordinator after a work wave.
