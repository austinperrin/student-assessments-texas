# Milestone 4: Remaining Families

- Status: In Progress
- Estimate: 45 business days
- Dependencies: Milestone 3 completed
- Planned dates: 2027-08-09 through 2027-10-08

## Goal

Complete initial review coverage for TELPAS Alternate and the smaller TEA
families without reducing the evidence standard for lower-volume work.

## Owners

- Milestone owner: Program owner
- Execution: Assigned Reviewer 1 teams
- Verification: Assigned Reviewer 2 teams

## Milestone Pre-Checklist

- [x] Reconfirm represented years before this milestone begins.
- [x] Assign reviewers with relevant family context.
- [x] Record source or sample gaps before execution.

<a id="m4-phase-1"></a>

## Phase 1: TELPAS Alternate

- Year branches: one independent `audit-fix/tea-telpas-alt-<year>` branch per
  represented year
- Family branch: `audit/tea-telpas-alt`; year PRs target this branch
- Final family PR: shared family and coverage closeout to `main`
- [x] Complete all review layers for eight years.
- [x] Confirm every concept independently from its assigned year's source.
- Actual completion: 2026-10-08; all eight year PRs merged into the family
  branch.
- Exit: all eight year PRs are merged into the family branch, then the completed
  family PR is merged to `main`.

<a id="m4-phase-2"></a>

## Phase 2: Interim, TFAR, and TTAP

- Year branches: one independent `audit-fix/tea-<family>-<year>` branch per
  represented year
- Family branches: one `audit/tea-<family>` branch per family; year PRs target
  the matching family branch
- Final family PRs: shared closeout from each family branch to `main`
- [ ] Audit each year in its own review record and branch.
- [ ] Investigate missing years and distinguish expected absence from source gaps.
- STAAR Interim completed 2026-10-08: all three represented year PRs were
  approved and merged into `audit/tea-staar-interim`; the family closeout is in
  review.
- Exit: every year PR is merged into its family branch, then each completed
  family PR is merged to `main`.

<a id="m4-phase-3"></a>

## Phase 3: CRS Custom

- Year branches: one independent `audit-fix/tea-crs-<year>` branch for 2023
  through 2026
- Family branch: `audit/tea-crs`; year PRs target this branch
- Final family PR: shared CRS and coverage closeout to `main`
- [ ] Complete all review layers for four years.
- [ ] Clearly separate custom-file conventions from statewide file assumptions.
- Exit: all four year PRs are merged into the family branch, then the completed
  CRS family PR is merged to `main`.

## Milestone Review Checklist

- [ ] Every represented TEA mapping year has an initial review or documented block.
- [ ] Smaller families remain independently traceable.
- [ ] Roadmap actual dates, variance, and status are updated.

## Next Step

Proceed to [Milestone 5: Cross-Family Verification](./m5-cross-family-verification.md).
