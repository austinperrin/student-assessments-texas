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
- Execution: Assigned family reviewers
- Verification: Assigned independent verifiers

## Milestone Pre-Checklist

- [ ] Pilot process changes are merged.
- [ ] Family/year inventories and missing-year facts are confirmed.
- [ ] Review and verification assignments are recorded.
- [ ] Create each family branch from the current `main` when its phase begins.

<a id="m2-phase-1"></a>

## Phase 1: STAAR EOC

- Family branch: `audit/tea-staar-eoc`
- Year branches: one per represented year, 2026 through 2012 in descending order
- Final PR: `audit/tea-staar-eoc` to `main`
- [ ] Complete all review layers for 15 represented years.
- [ ] Reconcile EOC-specific subject, course, administration, and history rules.
- Exit: all 15 year branches are merged, family reconciliation is complete,
  and the family PR is reviewable.

<a id="m2-phase-2"></a>

## Phase 2: STAAR Alternate 2 Grades 3-8

- Family branch: `audit/tea-staar-alt2-3-8`
- Year branches: 2026 through 2021, then 2019 through 2016, one at a time
- Final PR: `audit/tea-staar-alt2-3-8` to `main`
- [ ] Complete all review layers for 10 represented years.
- [ ] Record missing years as investigated coverage facts.
- Exit: all 10 year branches are merged, family reconciliation is complete,
  and the family PR is reviewable.

<a id="m2-phase-3"></a>

## Phase 3: STAAR Alternate 2 EOC

- Family branch: `audit/tea-staar-alt2-eoc`
- Year branches: 2026 through 2021, then 2019 through 2016, one at a time
- Final PR: `audit/tea-staar-alt2-eoc` to `main`
- [ ] Complete all review layers for 10 represented years.
- [ ] Compare shared Alternate 2 concepts without assuming identical layouts.
- Exit: all 10 year branches are merged, family reconciliation is complete,
  and the family PR is reviewable.

## Milestone Review Checklist

- [ ] All three phase exits are complete.
- [ ] Material cross-family inconsistencies are recorded as findings or rejected.
- [ ] Findings have owners and dispositions.
- [ ] Roadmap actual dates, variance, and status are updated.

## Next Step

Proceed to [Milestone 3: Accountability and TELPAS](./m3-accountability-and-telpas.md).
