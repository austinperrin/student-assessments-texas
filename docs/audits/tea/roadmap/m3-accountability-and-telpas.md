# Milestone 3: Accountability and TELPAS

- Status: Not Started
- Estimate: 65 business days
- Dependencies: Milestone 2 completed
- Planned dates: 2027-05-10 through 2027-08-06

## Goal

Audit consolidated accountability and TELPAS with focused review of their
multi-assessment, language-domain, and historical-result semantics.

## Owners

- Milestone owner: Program owner
- Execution: Assigned Reviewer 1 teams
- Verification: Assigned Reviewer 2 teams

## Milestone Pre-Checklist

- [ ] Source inventories and assignments are current.
- [ ] Holiday availability and verification capacity are confirmed.
- [ ] Distinct Reviewer 1 and Reviewer 2 assignments are recorded.

<a id="m3-phase-1"></a>

## Phase 1: Consolidated Accountability

- Year branches: one independent `audit-fix/tea-staar-consolidated-<year>`
  branch per represented year
- Family branch: `audit/tea-staar-consolidated`; year PRs target this branch
- Final family PR: shared family and coverage closeout to `main`
- [x] Complete all review layers for 11 represented years.
- [x] Check how multiple assessment families and administrations coexist.
- Actual completion: 2026-10-06; family PR #124 merged to `main` as
  `d49780f`.
- Exit: all 11 year PRs are merged into the family branch, then the completed
  family PR is merged to `main`.

<a id="m3-phase-2"></a>

## Phase 2: TELPAS 2012-2021

- Year branches: one independent `audit-fix/tea-telpas-<year>` branch for
  each represented 2012-2021 year
- Family branch: `audit/tea-telpas`; year PRs target this branch
- [ ] Complete all review layers for 10 years.
- [ ] Verify domain, composite, proficiency, score-code, and history handling.
- Exit: all 10 year PRs are approved and merged into the family branch.

<a id="m3-phase-3"></a>

## Phase 3: TELPAS 2022-2026

- Year branches: one independent `audit-fix/tea-telpas-<year>` branch for
  each represented 2022-2026 year
- Family branch: `audit/tea-telpas`; year PRs target this branch
- Final family PR: shared TELPAS and coverage closeout to `main`
- [ ] Complete all review layers for five years.
- [ ] Confirm each layout independently from its assigned year's source.
- Exit: all 15 year PRs are merged into the family branch, then the completed
  TELPAS family PR is merged to `main`.

## Milestone Review Checklist

- [ ] All phase exits are complete or blocked with an owner and review date.
- [ ] Coverage, review records, and findings agree.
- [ ] Roadmap actual dates, variance, and status are updated.

## Next Step

Proceed to [Milestone 4: Remaining Families](./m4-remaining-families.md)
on the dates in the canonical roadmap schedule.
