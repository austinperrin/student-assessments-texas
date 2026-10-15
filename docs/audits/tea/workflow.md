# TEA Audit Workflow

This workflow governs the TEA assessment audit roadmap. The
[roadmap index](./roadmap/index.md) owns schedule and status, and
[coverage.md](./coverage.md) records completed review coverage. Review records
and findings contain the supporting evidence.

## Work-Unit Model

One work unit covers one mapping family and one reporting year. Every work unit
has two distinct reviewers. Either role may be performed by a human or an AI.

- **Reviewer 1** owns the complete year package: source review, findings,
  corrections, resolutions, validation, and the pull request.
- **Reviewer 2** independently checks the final mapping against that year's
  source and returns one consolidated approval or correction request.
- **Program owner** assigns work, resolves consequential dispositions, and
  coordinates shared family and roadmap updates.

Reviewer 1 and Reviewer 2 must not be the same person or agent for a work unit.
Record each reviewer's identity and type. When AI performs a role, identify the
agent or review session clearly enough to distinguish the two reviews.

Reviewer 1 completes the full pass before handoff. Do not pause after each
finding for confirmation. Reviewer 2 reports all corrections together when
practical; Reviewer 1 applies them in one pass, and Reviewer 2 performs the
final confirmation.

## Family Scope Discovery

Before creating year work units, build a durable family source inventory from
the current official TEA or Texas Assessments pages. Start with the official
family page and central data-file-format pages, not the repository's existing
mappings or their stored URLs. Record the discovery page URLs, retrieval date,
published or updated labels, every listed year and layout, and the direct
official source URL using the
[source inventory template](./source-inventory-template.md).

Reconcile three sets in both directions:

1. layouts listed by the official sources;
2. mappings present in the repository; and
3. PDFs present in the local source archive.

An official layout without a mapping is required audit scope and must produce
a planned work unit or tracked issue. A mapping without a discoverable official
source is a source gap. A missing archive requires retrieval or a documented
block. Record an evidence-backed disposition for every difference; absence
from the repository is never evidence that an official layout is out of scope.

A reviewer other than the inventory preparer must independently revisit the
official discovery pages and confirm the enumerated years, layouts, direct
links, and set differences. Counts alone are insufficient. Repeat this
inventory check immediately before family closeout so sources published or
revised during a long-running audit are not missed.

## Source Isolation

The assigned year's official source and matching archive are the evidence for
that year's conclusions. Do not inspect another year's mapping or source to
establish, suggest, or normalize a field during the year review. Shared naming
rules may be applied only when the assigned year's source independently
supports the same meaning.

Cross-year analysis is a separate, explicitly authorized activity. It must not
change a year conclusion without reopening that year against its own source.

The required family source inventory lists documents and years only. It does
not change the rule that no tracked field-level source-row manifest or
dedicated source-to-mapping validator is required. Temporary extraction and
working notes belong under `.tmp/audits/` and are not authoritative evidence.

## Branch And Pull Request Model

Create one family integration branch from an up-to-date `main`. Create every
year branch from that family branch, and target every year pull request back to
the family branch. A year branch remains an independent work unit and must not
depend on another year's source or mapping evidence.

| Work                      | Branch pattern                  | Pull request target  |
| ------------------------- | ------------------------------- | -------------------- |
| Framework or roadmap      | `docs/tea-audit-<topic>`        | `main`               |
| Family integration        | `audit/tea-<family>`            | `main`               |
| Year audit and correction | `audit-fix/tea-<family>-<year>` | `audit/tea-<family>` |

Examples:

- `audit-fix/tea-staar-eoc-2026`
- `audit-fix/tea-telpas-2021`
- `audit/tea-staar-eoc`

The year pull request may change only its year mapping, year review record,
year-specific findings, and the matching source archive when needed. Reviewer 1
may correct the mapping in the same pull request as the audit record.

Shared files such as coverage summaries, family records, and roadmap milestones
are owned by the program coordinator. Year branches do not edit them. After all
year pull requests merge into the family branch, the coordinator updates shared
state once on that family branch before its final pull request to `main`.

## Parallel Execution

Multiple work units may run simultaneously across families and within a family.
Each unit must have:

- a unique family/year assignment;
- named Reviewer 1 and Reviewer 2;
- a branch created from the assigned family integration branch;
- a single year review record and pull request; and
- no edits to coordinator-owned shared files.

Track active assignments in GitHub issues or project fields instead of a
frequently edited repository registry. The same reviewer may work on multiple
units, but nobody may verify their own work.

## Year Work-Unit Lifecycle

1. The coordinator prepares the family source inventory, obtains its
   independent review, and resolves or assigns every source-to-repository
   difference.
2. The program owner assigns every required family/year or layout work unit and
   two distinct reviewers.
3. Reviewer 1 creates the year branch from the assigned family integration
   branch and records the repository and source baselines.
4. Reviewer 1 audits the entire source, applies all supported corrections,
   resolves findings, runs validation, and opens one pull request.
5. Reviewer 2 independently compares the final mapping with the same year's
   source and submits one consolidated review.
6. If corrections are requested, Reviewer 1 addresses them together and reruns
   validation.
7. Reviewer 2 confirms the final package, and required CI passes.
8. Merge the year pull request into the family integration branch without
   squashing away the year work-unit boundary, then delete the year branch.
9. Immediately before closeout, refresh and independently recheck the official
   source inventory. Add work units for newly published or newly discovered
   layouts.
10. After every inventoried year is approved and merged or has an accepted
    block, the coordinator updates shared coverage, family, and roadmap records
    on the family branch.
11. Validate the integrated family branch, obtain program-owner approval, and
    merge its final pull request to `main` using the repository's normal policy.

An accepted block is not a passing review. Record the affected layer, missing
evidence, reason, owner, program-owner acceptance, and next review date. Keep
the work unit `blocked` until the unfinished layer is completed or explicitly
accepted under the program's exception policy.

## Tracked Record Layout

Use `reviews/<family>/README.md` for the coordinator-owned family record and
`reviews/<family>/<year>.md` for each year work unit. For example:

```text
reviews/staar-eoc/README.md
reviews/staar-eoc/2026.md
reviews/staar-eoc/2025.md
```

The year branch updates only its year record and related finding evidence. The
coordinator updates the family record, coverage, and roadmap on the family
branch during closeout.

## Review Statuses

Use these work-unit statuses:

`planned` -> `reviewer-1-active` -> `ready-for-reviewer-2` -> `approved` ->
`merged`

Use `corrections-requested` when Reviewer 2 returns the package and `blocked`
when required evidence or authority is unavailable. After corrections,
Reviewer 1 returns the unit to `ready-for-reviewer-2`.

Finding states remain evidence-focused:

`candidate` -> `confirmed` or `rejected` -> `corrected` -> `verified` ->
`closed`

Use `deferred`, `accepted-risk`, or `blocked` only with an owner, reason, and
next review date.

## Reviewer 1 Handoff

Before requesting Reviewer 2 review, the pull request and year record must
contain:

- repository baseline, source URL, archive, retrieval date, and version;
- the complete source and mapping coverage result;
- every finding, correction, and resolution;
- limitations and unavailable operational samples;
- validation commands and results;
- any historical-data or reprocessing decision; and
- a statement that only the assigned year's source was used as audit evidence.

## Reviewer 2 Consolidated Review

Reviewer 2 checks the source independently rather than merely confirming
Reviewer 1's claims. Record one consolidated result containing:

- items independently verified;
- corrections requested, with source page and positions;
- any newly discovered findings;
- limitations or disagreements; and
- final status: `approved`, `corrections-requested`, or `blocked`.

High- and critical-severity findings always require explicit independent
reproduction. Lower-severity findings are still covered by the independent
final-package review.

## Validation And Merge Gates

1. **Scope gate:** an independently reviewed official-source inventory is
   reconciled against repository mappings and archives, and every difference
   has a disposition.
2. **Baseline gate:** repository commit, scope, reviewers, and sources are
   recorded.
3. **Reviewer 1 gate:** the full year is audited, supported corrections are
   applied, findings are resolved, and validation passes.
4. **Reviewer 2 gate:** an independent consolidated review is recorded.
5. **Correction gate:** every requested correction is resolved or explicitly
   blocked, and Reviewer 2 confirms the result.
6. **Year merge gate:** required CI passes, the pull request contains only the
   assigned work-unit files, and the PR targets the family branch.
7. **Closeout gate:** the refreshed official-source inventory has no
   undispositioned difference, every inventoried year is integrated or has an
   accepted block, and the coordinator updates shared coverage and program
   state on the family branch.
8. **Family merge gate:** integrated validation and program-owner approval pass
   before the family pull request merges to `main`.

Required repository checks include valid JSON, required mapping shape, string
values, unique headers, the 63-character header limit, regex compilation where
applicable, formatting, and lint. Direct PDF inspection remains required for
ambiguous or wrapped source rows.

## Commit And Merge Guidance

Use focused conventional commits, for example:

- `fix: audit and correct 2026 STAAR EOC mapping`
- `docs: record reviewer 2 approval for 2026 STAAR EOC`
- `docs: close STAAR EOC audit wave`

Year pull requests merge into the family integration branch without squashing
away their work-unit boundaries. Do not stack year branches or rewrite commits
after Reviewer 2 approval. Only the completed family integration pull request
merges to `main` using the repository's normal merge policy.
