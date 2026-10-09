# Milestone 2: Core STAAR Families

- Status: Completed
- Estimate: 90 business days
- Dependencies: Milestone 1 completed and roadmap rebaselined
- Planned dates: 2027-01-04 through 2027-05-07

## Goal

Apply the pilot-tested process to STAAR EOC and both STAAR Alternate 2
families, preserving each year's distinct layout and behavior.

## Owners

- Milestone owner: Program owner
- Execution: Assigned Reviewer 1 teams
- Verification: Assigned Reviewer 2 teams

## Milestone Pre-Checklist

- [x] Pilot process changes are merged.
- [x] Family/year inventories and missing-year facts are confirmed.
- [x] Review and verification assignments are recorded.
- [x] Create one integration branch per family from current `main`, then create
      every assigned year branch from its family branch.

<a id="m2-phase-1"></a>

## Phase 1: STAAR EOC

- Year branches: one independent `audit-fix/tea-staar-eoc-<year>` branch per
  represented year
- Family branch: `audit/tea-staar-eoc`; year PRs target this branch
- Final family PR: shared family and coverage closeout to `main`
- [x] Complete all review layers for 15 represented years.
- [x] Confirm EOC-specific rules against each assigned year's own source.
- Actual completion: 2026-10-01. The approved year PRs merged directly to
  `main` under the legacy workflow; M5 pre-work records that integration in the
  [family record](../reviews/staar-eoc/README.md).
- Exit: all 15 approved year PRs are merged directly to `main` under the legacy
  workflow, and the family-level integration history is reconciled in the M5
  pre-work record.

<a id="m2-phase-2"></a>

## Phase 2: STAAR Alternate 2 Grades 3-8

- Year branches: one independent `audit-fix/tea-staar-alt2-3-8-<year>`
  branch per represented year
- Family branch: `audit/tea-staar-alt2-3-8`; year PRs target this branch
- Final family PR: shared family and coverage closeout to `main`
- [x] Complete all review layers for 10 represented years.
- [x] Record missing years as investigated coverage facts.
- Actual completion: 2026-10-01. The approved year PRs merged directly to
  `main` under the legacy workflow; 2020 is absent because the administration
  was canceled. M5 pre-work records the integration in the
  [family record](../reviews/staar-alt2-3-8/README.md).
- Exit: all 10 approved year PRs are merged directly to `main` under the legacy
  workflow, the canceled 2020 administration is documented, and the
  family-level integration history is reconciled in the M5 pre-work record.

<a id="m2-phase-3"></a>

## Phase 3: STAAR Alternate 2 EOC

- Year branches: one independent `audit-fix/tea-staar-alt2-eoc-<year>`
  branch per represented year
- Family branch: `audit/tea-staar-alt2-eoc`; year PRs target this branch
- Final family PR: shared family and coverage closeout to `main`
- [x] Complete all review layers for 10 represented years.
- [x] Confirm Alternate 2 concepts independently from each year's source.
- Actual completion: 2026-10-02; family PR #110 merged to `main` as
  `fe1870b`.
- Exit: all 10 year PRs are merged into the family branch, then the completed
  family PR is merged to `main`.

## Milestone Review Checklist

- [x] All three phase exits are complete.
- [x] Every year used only its assigned source as audit evidence.
- [x] Findings have owners and dispositions.
- [x] Roadmap actual dates, variance, and status are updated.

Actual completion: 2026-10-02. M5 pre-work reconciled the previously stale M2
status against the approved year records and merged PR history without
reopening mapping conclusions.

## Next Step

Proceed to [Milestone 3: Accountability and TELPAS](./m3-accountability-and-telpas.md).
