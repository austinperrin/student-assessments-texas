# Milestone 4: Remaining Families

- Status: Not Started
- Estimate: 45 business days
- Dependencies: Milestone 3 completed
- Planned dates: 2027-08-09 through 2027-10-08

## Goal

Complete initial review coverage for TELPAS Alternate and the smaller TEA
families without reducing the evidence standard for lower-volume work.

## Owners

- Milestone owner: Program owner
- Execution: Assigned family reviewers
- Verification: Assigned independent verifiers

## Milestone Pre-Checklist

- [ ] Reconfirm represented years after the holiday buffer.
- [ ] Assign reviewers with relevant family context.
- [ ] Record source or sample gaps before execution.

<a id="m4-phase-1"></a>
## Phase 1: TELPAS Alternate

- Family branch: `audit/tea-telpas-alt`
- Year branches: 2026 through 2019, one at a time
- Final PR: `audit/tea-telpas-alt` to `main`
- [ ] Complete all review layers for eight years.
- [ ] Compare related TELPAS concepts only where source meanings match.
- Exit: all eight year branches are merged, family reconciliation is complete,
  and the family PR is reviewable.

<a id="m4-phase-2"></a>
## Phase 2: Interim, TFAR, and TTAP

- Family branches: `audit/tea-staar-interim`, `audit/tea-tfar`, and
  `audit/tea-ttap`
- Year branches: one branch per represented year, newest to oldest within each
  family
- Final PR: one family branch to `main` for each family
- [ ] Audit each year in its own review record and branch.
- [ ] Investigate missing years and distinguish expected absence from source gaps.
- Exit: every year branch is merged and each of the three family PRs is
  reviewable.

<a id="m4-phase-3"></a>
## Phase 3: CRS Custom

- Family branch: `audit/tea-crs`
- Year branches: 2026, 2025, 2024, and 2023, one at a time
- Final PR: `audit/tea-crs` to `main`
- [ ] Complete all review layers for four years.
- [ ] Clearly separate custom-file conventions from statewide file assumptions.
- Exit: all four year branches are merged, family reconciliation is complete,
  and the family PR is reviewable.

## Milestone Review Checklist

- [ ] Every represented TEA mapping year has an initial review or documented block.
- [ ] Smaller families remain independently traceable.
- [ ] Roadmap actual dates, variance, and status are updated.

## Next Step

Proceed to [Milestone 5: Cross-Family Verification](./m5-cross-family-verification.md).
