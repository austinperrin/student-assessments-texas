# Milestone 2: Core STAAR Families

- Status: Not Started
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

- [ ] Pilot process changes are merged.
- [ ] Family/year inventories and missing-year facts are confirmed.
- [ ] Review and verification assignments are recorded.
- [ ] Create one integration branch per family from current `main`, then create
      every assigned year branch from its family branch.

<a id="m2-phase-1"></a>

## Phase 1: STAAR EOC

- Year branches: one independent `audit-fix/tea-staar-eoc-<year>` branch per
  represented year
- Family branch: `audit/tea-staar-eoc`; year PRs target this branch
- Final family PR: shared family and coverage closeout to `main`
- [ ] Complete all review layers for 15 represented years.
- [ ] Confirm EOC-specific rules against each assigned year's own source.
- Exit: all 15 year PRs are merged into the family branch, then the completed
  family PR is merged to `main`.

<a id="m2-phase-2"></a>

## Phase 2: STAAR Alternate 2 Grades 3-8

- Year branches: one independent `audit-fix/tea-staar-alt2-3-8-<year>`
  branch per represented year
- Family branch: `audit/tea-staar-alt2-3-8`; year PRs target this branch
- Final family PR: shared family and coverage closeout to `main`
- [ ] Complete all review layers for 10 represented years.
- [ ] Record missing years as investigated coverage facts.
- Exit: all 10 year PRs are merged into the family branch, then the completed
  family PR is merged to `main`.

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

- [ ] All three phase exits are complete.
- [ ] Every year used only its assigned source as audit evidence.
- [ ] Findings have owners and dispositions.
- [ ] Roadmap actual dates, variance, and status are updated.

## Next Step

Proceed to [Milestone 3: Accountability and TELPAS](./m3-accountability-and-telpas.md).
