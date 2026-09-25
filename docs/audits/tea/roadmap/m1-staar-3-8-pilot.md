# Milestone 1: STAAR Grades 3-8 Pilot

- Status: In Progress
- Actual start: 2026-09-25
- Estimate: 45 business days
- Dependencies: Milestone 0 completed
- Planned dates: 2026-10-05 through 2026-12-04

## Owners

- Milestone owner: Austin Perrin
- Execution: Codex
- Verification: Austin Perrin (actual independent review required)

## Goal

Audit the complete STAAR grades 3-8 history, validate the review framework on a
known multi-record parser question, and rebaseline the remaining program from
measured effort.

## Milestone Pre-Checklist

- [x] Framework is merged and the templates are stable.
- [x] Reviewer and verifier assignments are recorded in coverage.
- [ ] Official and archived sources are inventoried for 2012-2026.
- [x] Operational samples are confirmed unavailable; record this limitation in
      each year review.
- [x] Create `audit/tea-staar-3-8` from the current `main`.
- [x] Initialize the family integration record and year sequence.

<a id="m1-phase-1"></a>

## Phase 1: 2022-2026

### Checklist

- [ ] Complete source/mapping, parser, and available-sample review for A3.
- [ ] Examine subject records, score codes, duplicates, and result eligibility.
- [ ] Record candidates and independently verify high/critical findings.

### Branch and PR Plan

- Family branch: `audit/tea-staar-3-8`
- Year branches, in order: `audit/tea-staar-3-8-2026`, `-2025`, `-2024`,
  `-2023`, and `-2022`
- Each year branch starts from and merges into the updated family branch.

### Exit Criteria

- [ ] All five year branches and review records are merged into the family branch.
- [ ] Every finding has evidence, status, severity, and owner.

<a id="m1-phase-2"></a>

## Phase 2: 2017-2021

### Checklist

- [ ] Complete all review layers for A2.
- [ ] Identify year-specific layout and parser behavior changes.
- [ ] Challenge assumptions learned from current-year files against each source.

### Branch and PR Plan

- Family branch: `audit/tea-staar-3-8`
- Year branches, in order: `audit/tea-staar-3-8-2021`, `-2020`, `-2019`,
  `-2018`, and `-2017`
- Each year branch starts after the preceding year merges.

### Exit Criteria

- [ ] All five year branches and review records are merged into the family branch.
- [ ] Cross-year observations are supported by year-specific evidence.

<a id="m1-phase-3"></a>

## Phase 3: 2012-2016 and Rebaseline

### Checklist

- [ ] Complete all review layers for A1.
- [ ] Reconcile findings across 2012-2026.
- [ ] Record actual effort and revise M2-M6 dates or estimates as needed.

### Branch and PR Plan

- Family branch: `audit/tea-staar-3-8`
- Year branches, in order: `audit/tea-staar-3-8-2016`, `-2015`, `-2014`,
  `-2013`, and `-2012`
- Final PR: `audit/tea-staar-3-8` to `main`

### Exit Criteria

- [ ] All 15 years have a completed review or documented block.
- [ ] All year branches are merged and the family PR is reviewable.
- [ ] The roadmap reflects pilot evidence rather than initial estimates alone.

## Milestone Review Checklist

- [ ] A1, A2, and A3 exit criteria are complete.
- [ ] Coverage totals and review records agree.
- [ ] Confirmed findings have dispositions and remediation owners.
- [ ] Pilot lessons are incorporated into templates or workflow when needed.
- [ ] Family-wide reconciliation and final family PR review are complete.
- [ ] Milestone status and actual dates are updated.

## Next Step

Proceed to [Milestone 2: Core STAAR Families](./m2-core-staar-families.md).
