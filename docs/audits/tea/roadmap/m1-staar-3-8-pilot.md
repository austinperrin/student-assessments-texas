# Milestone 1: STAAR Grades 3-8 Pilot

- Status: Completed
- Actual start: 2026-09-25
- Estimate: 45 business days
- Dependencies: Milestone 0 completed
- Planned dates: 2026-10-05 through 2026-12-04

## Owners

- Milestone owner: Austin Perrin
- Execution: Codex
- Verification: Austin Perrin (actual independent review required)

## Goal

Audit the complete STAAR grades 3-8 history, validate the review framework, and
rebaseline the remaining program from measured effort.

## Milestone Pre-Checklist

- [x] Framework is merged and the templates are stable.
- [x] Reviewer and verifier assignments are recorded in coverage.
- [x] Official and archived sources are inventoried for 2012-2026.
- [x] Operational samples are confirmed unavailable; record this limitation in
      each year review.
- [x] Create `audit/tea-staar-3-8` from the current `main`.
- [x] Initialize the family integration record and year sequence.

<a id="m1-phase-1"></a>

## Phase 1: 2022-2026

### Checklist

- [x] Complete source/mapping and available-sample review for A3.
- [x] Examine subject records, score codes, duplicates, and result eligibility.
- [x] Record candidates and independently verify high/critical findings.

### Branch and PR Plan

- Family branch: `audit/tea-staar-3-8`
- Year branches, in order: `audit/tea-staar-3-8-2026`, `-2025`, `-2024`,
  `-2023`, and `-2022`
- Each year branch starts from and merges into the updated family branch.

### Exit Criteria

- [x] All five year branches and review records are merged into the family branch.
- [x] Every finding has evidence, status, severity, and owner.

<a id="m1-phase-2"></a>

## Phase 2: 2017-2021

### Checklist

- [x] Complete all review layers for A2.
- [x] Identify year-specific layout changes.
- [x] Challenge assumptions learned from current-year files against each source.

### Branch and PR Plan

- Family branch: `audit/tea-staar-3-8`
- Year branches, in order: `audit/tea-staar-3-8-2021`, `-2020`, `-2019`,
  `-2018`, and `-2017`
- Each year branch starts after the preceding year merges.

### Exit Criteria

- [x] All five year branches and review records are merged into the family branch.
- [x] Cross-year observations are supported by year-specific evidence.

<a id="m1-phase-3"></a>

## Phase 3: 2012-2016 and Rebaseline

### Checklist

- [x] Complete all review layers for A1.
- [x] Reconcile findings across 2012-2026.
- [x] Record actual effort and revise M2-M6 dates or estimates as needed.

### Branch and PR Plan

- Family branch: `audit/tea-staar-3-8`
- Year branches, in order: `audit/tea-staar-3-8-2016`, `-2015`, `-2014`,
  `-2013`, and `-2012`
- Final PR: `audit/tea-staar-3-8` to `main`

### Exit Criteria

- [x] All 15 years have a completed review or documented block.
- [x] All year branches are merged and the family PR is reviewable.
- [x] The roadmap reflects pilot evidence rather than initial estimates alone.

## Milestone Review Checklist

- [x] A1, A2, and A3 exit criteria are complete.
- [x] Coverage totals and review records agree.
- [x] Confirmed findings have dispositions and remediation owners.
- [x] Pilot lessons are incorporated into templates or workflow when needed.
- [x] Family-wide reconciliation and final family PR review are complete.
- [x] Milestone status and actual dates are updated.

Actual completion: 2026-09-30. M5 pre-work reconciled this roadmap status to
the closed 15/15 family record; no mapping conclusion was reopened.

## Next Step

Proceed to [Milestone 2: Core STAAR Families](./m2-core-staar-families.md).
