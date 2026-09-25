# TEA Audit Workflow

This workflow governs the TEA assessment audit roadmap. The
[roadmap index](./roadmap/index.md) owns schedule and status, milestone files
own execution checklists, and [coverage.md](./coverage.md) records completed
review coverage. Review records and findings contain the supporting evidence.

## Working Model

- The program owner maintains roadmap status, assignments, and priorities.
- A reviewer compares each year with its own source and records the evidence.
- A verifier other than the original reviewer independently reproduces high-
  and critical-severity findings before they are confirmed.
- A remediator changes mappings only after a finding is confirmed.
- Audit and remediation changes use separate branches and pull requests.
- Only one year is audited on a year branch. Years within a family are merged
  into that family's audit branch one at a time.
- Different family branches may run in parallel when reviewers do not overlap.

## Branch Model

Each family has an integration branch created from an up-to-date `main`. Each
year branch is created from that family branch and merges back into it after
year-level review. When every represented year is complete, one family pull
request merges the family audit branch into `main`.

| Work                     | Branch pattern                                                           | Pull request target                       |
| ------------------------ | ------------------------------------------------------------------------ | ----------------------------------------- |
| Framework or roadmap     | `docs/tea-audit-<topic>`                                                 | `main`                                    |
| Family audit integration | `audit/tea-<family>`                                                     | `main`, after all represented years close |
| Single-year audit        | `audit/tea-<family>-<year>`                                              | `audit/tea-<family>`                      |
| Finding verification     | the open year branch; otherwise `audit/tea-<family>-<year>-verification` | family audit branch                       |
| Mapping correction       | `fix/tea-<family>-<finding-or-years>`                                    | `main`                                    |

Examples:

- `audit/tea-staar-3-8`
- `audit/tea-staar-3-8-2026`
- `audit/tea-telpas-2021-verification`
- `fix/tea-staar-3-8-2026-result-eligibility`

The family branch is an integration and reconciliation branch. Do not perform
the year audit directly on it. A year branch contains exactly one reporting
year, even when adjacent years share a layout.

## Family Audit Lifecycle

1. Create `audit/tea-<family>` from the current `main` after its prerequisite
   milestone is ready.
2. Add the family audit index and initialize its represented-year checklist.
3. Create the first `audit/tea-<family>-<year>` branch from the family branch.
4. Complete that year's source/mapping and available-sample review.
5. Review the year branch and merge it into the family branch.
6. Create the next year branch from the updated family branch and repeat.
7. Reconcile family-wide findings, coverage, and cross-year observations on
   the family branch after the final year merges.
8. Open one family audit pull request from `audit/tea-<family>` to `main`.
9. Merge only after every represented year is closed or has an explicitly
   accepted block with an owner and review date.

For family closure, an accepted block is a documented exception to completed
review, not a passing review layer. Record the affected year and layer, missing
evidence, reason, owner, program-owner acceptance, and next review date in the
year and family records. Merge that year record through its year branch and
retain `blocked` for unfinished layers in coverage. Family sign-off must name
these exceptions explicitly; never count them as completed review layers.

Audit years in the order defined by the governing milestone. The branch
sequence must be recorded in the family audit index.

## Tracked Record Layout

Use `reviews/<family>/README.md` for the family integration record and
`reviews/<family>/<year>.md` for each year review. For example, the STAAR
grades 3-8 family uses:

```text
reviews/staar-3-8/README.md
reviews/staar-3-8/2026.md
reviews/staar-3-8/2025.md
```

The year branch updates its year record, its coverage row, and any findings
created from that year's evidence. The family branch updates the family record,
summary coverage, and roadmap state during reconciliation.

## Merge Strategy

- Each year branch uses a pull request whose base is the family branch.
- Year branches merge into the family branch with a non-squash merge so the
  year-level commits and review boundary remain visible.
- The family pull request merges into `main` with a non-squash merge so the
  individual year audit history remains visible on `main`.
- Delete a year branch after it merges. Delete the family branch after the
  family pull request merges.
- Resolve family-branch drift before creating the next year branch. Do not
  rebase or rewrite year commits after they have been reviewed.

This is a documented exception to any default squash preference for audit
branches because retaining the one-year evidence trail is part of the audit
control.

## Commit Naming

Use the repository's conventional prefixes and keep each commit focused:

- `docs: record 2026 STAAR 3-8 audit`
- `docs: verify STAAR38-2026-001`
- `docs: close 2026 STAAR 3-8 audit`
- `docs: reconcile STAAR 3-8 family audit`
- `fix: apply 2026 STAAR 3-8 score eligibility rules`

Do not introduce an `audit:` commit type unless the repository commit standard
is changed separately.

## Audit Pull Request

### Year Branch Review

Before a year branch merges into its family branch, its review records:

- roadmap milestone and phase
- repository baseline and source versions
- the single year and review layers completed
- findings by severity and status
- limitations and unavailable operational samples
- verifier status and required follow-up

The year review may close with confirmed findings still open when each one has
an owner and disposition. It must not edit the mappings under review.

### Family Pull Request

The family pull request contains the accumulated year records plus family-wide
reconciliation. Its description records:

- every represented year and year-branch merge
- family coverage totals
- confirmed, rejected, deferred, and blocked findings
- cross-year conclusions and remaining limitations
- remediation links already opened
- reviewer, verifier, and program-owner sign-off

## Remediation Pull Request

A remediation pull request links the confirmed finding and records:

- behavior before and after the change
- exact source evidence supporting the correction
- validation performed
- effect on previously processed data
- whether reprocessing is required, unnecessary, deferred, or unknown

Critical findings may use an expedited remediation branch after independent
confirmation. Coverage and finding records are updated when the correction is
verified, not merely when code is merged.

## Review Gates

1. **Baseline gate:** repository commit, scope, and sources are recorded.
2. **Candidate gate:** evidence identifies the source page and exact positions.
3. **Confirmation gate:** the required verifier reproduces the comparison.
4. **Remediation gate:** correction scope and downstream impact are accepted.
5. **Merge gate:** required validation passes and unrelated files are absent.
6. **Closure gate:** coverage, finding status, remediation link, and
   reprocessing decision are recorded.

## Status Updates

Update the narrowest governing document in the same branch as the work:

- update the review record as evidence is gathered
- update coverage when a review layer is completed
- update a milestone checklist when its exit evidence exists
- update roadmap dates and status when work starts or completes

Do not mark a milestone complete until every phase meets its exit criteria and
the milestone review checklist is complete.
