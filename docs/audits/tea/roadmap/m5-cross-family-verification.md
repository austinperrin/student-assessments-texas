# Milestone 5: Program Verification

- Status: In Progress
- Estimate: 15 business days
- Dependencies: Milestones 1-4 completed or explicitly blocked
- Planned dates: 2027-10-11 through 2027-10-29

## Goal

Reconcile program records after every family has been reviewed without using
cross-year or cross-family comparisons as source evidence.

## Owners

- Milestone owner: Program owner
- Execution: Program coordinator
- Verification: Reviewers who did not author the affected work-unit finding

## Milestone Pre-Checklist

- [x] Coverage lists every represented year and review limitation.
- [ ] Candidate, confirmed, rejected, and blocked findings are queryable.
- [ ] Open verification work has an assigned verifier.

## Pre-Work: Historical Coverage Reconciliation

- Branch: `docs/tea-audit-m5-prework-reconciliation`
- [x] Reconcile the closed STAAR grades 3-8 family with M1 status.
- [x] Reconcile all 15 approved STAAR EOC records and merged PRs with coverage.
- [x] Reconcile all 10 approved STAAR Alternate 2 grades 3-8 records and merged
      PRs with coverage, including canceled 2020.
- [x] Record legacy direct-to-`main` integration without rewriting history as
      family-branch integration.
- [x] Obtain independent review of the reconciled program state.

Independent reconciliation review approved by External AI on 2026-10-09 in
[PR #173](https://github.com/austinperrin/student-assessments-texas/pull/173).

<a id="m5-phase-1"></a>

## Phase 1: Source Gaps And Exceptions

- Branch: `docs/tea-audit-m5-source-gaps`
- [ ] Inventory unresolved source gaps and accepted blocks.
- [ ] Confirm each year conclusion cites only that year's source.
- [ ] Reconcile missing, superseded, inaccessible, or conflicting sources.
- Exit: every source exception is resolved or assigned for follow-up.

<a id="m5-phase-2"></a>

## Phase 2: Findings and Coverage Reconciliation

- Branch: `docs/tea-audit-m5-program-reconciliation`
- [ ] Confirm review records and coverage totals agree.
- [ ] Confirm required independent verifications are complete.
- [ ] Check finding IDs, severity, state, owner, and disposition.
- [ ] Identify audit limitations that remain at closeout.
- Exit: the audit evidence set is internally consistent and reviewable.

## Milestone Review Checklist

- [ ] Both phase exits are complete.
- [ ] No cross-year or cross-family comparison was used as year-level evidence.
- [ ] All unresolved work has an owner and target.
- [ ] Roadmap actual dates, variance, and status are updated.

## Next Step

Proceed to
[Milestone 6: Remediation Plan and Closeout](./m6-remediation-plan-and-closeout.md).
