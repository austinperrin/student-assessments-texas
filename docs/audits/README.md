# Repository Audits

This area contains durable plans, coverage records, review evidence, and closed
findings for source-fidelity audits. Audit work is separate from remediation:
reviewers record what the source says before changing canonical mappings or
documentation.

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

## Audit And Remediation

An audit pull request may add or update audit records but must not modify the
assets being audited. Corrections belong in later remediation pull requests so
the source finding and the proposed change can be reviewed independently.
