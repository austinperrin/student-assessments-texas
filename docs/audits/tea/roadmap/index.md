# TEA Assessment Audit Roadmap

This index is the canonical schedule and status view for the TEA assessment
audit. Milestone files contain the detailed work, while
[coverage](../coverage.md) remains the authoritative record of family and
review-layer completion.

## Team Model

| Role          | Responsibility                                                  |
| ------------- | --------------------------------------------------------------- |
| Program owner | Scope, sequence, assignments, dispositions, and rebaselining    |
| Reviewer      | Source comparison, parser review, sample analysis, and evidence |
| Verifier      | Independent reproduction and challenge of material findings     |
| Remediator    | Confirmed mapping or parser corrections on separate branches    |
| Approver      | Correction acceptance and downstream-data decision              |

One person may hold multiple roles. The reviewer and verifier should differ for
high- and critical-severity findings. An accountable human owns consequential
dispositions when AI reviewers contribute evidence.

## Planning Basis

The baseline assumes one primary reviewer contributing 10-12 focused hours per
week and one verifier contributing 3-4 hours per week. Dates use Monday-Friday
business days. The schedule begins with the already-started framework work and
must be rebaselined after the STAAR grades 3-8 pilot.

## Status and Variance Legend

Use only these styled status values so the schedule remains visually
consistent:

- <span style="color: #b91c1c;">Not Started</span>: work has not begun
- <span style="color: #ca8a04;">In Progress</span>: work is actively underway
- <span style="color: #dc2626; font-weight: 600;">Blocked</span>: work cannot
  proceed until its recorded blocker is resolved
- <span style="color: #2563eb;">In Review</span>: execution is complete and the
  required review or verification is underway
- <span style="color: green;">Completed</span>: work and review are complete on
  the governing branch

Use only these variance values: `TBD`, `On Track`, `Started Early`,
`Completed Early`, `Completed Late`, and `Delayed`.

Status cells in the schedule use the matching HTML span from this legend.
Variance values remain inline code because they describe schedule performance
rather than execution state.

## Schedule

| Milestone                                                                  | Phase                                                                                    | Estimate | Planned start | Planned end | Actual start | Actual end | Variance      | Status                                           |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------: | ------------: | ----------: | -----------: | ---------: | ------------- | ------------------------------------------------ |
| [M0: Audit framework](./m0-audit-framework.md)                             |                                                                                          |   7 days |    2026-09-24 |  2026-10-02 |   2026-09-24 |        TBD | On Track      | <span style="color: #ca8a04;">In Progress</span> |
|                                                                            | [P1: Governance and templates](./m0-audit-framework.md#m0-phase-1)                       |   3 days |    2026-09-24 |  2026-09-28 |   2026-09-24 |        TBD | On Track      | <span style="color: #ca8a04;">In Progress</span> |
|                                                                            | [P2: Roadmap and workflow](./m0-audit-framework.md#m0-phase-2)                           |   2 days |    2026-09-29 |  2026-09-30 |   2026-09-24 |        TBD | Started Early | <span style="color: #ca8a04;">In Progress</span> |
|                                                                            | [P3: Framework review](./m0-audit-framework.md#m0-phase-3)                               |   2 days |    2026-10-01 |  2026-10-02 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
| [M1: STAAR grades 3-8 pilot](./m1-staar-3-8-pilot.md)                      |                                                                                          |  45 days |    2026-10-05 |  2026-12-04 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P1: 2022-2026](./m1-staar-3-8-pilot.md#m1-phase-1)                                      |  15 days |    2026-10-05 |  2026-10-23 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P2: 2017-2021](./m1-staar-3-8-pilot.md#m1-phase-2)                                      |  15 days |    2026-10-26 |  2026-11-13 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P3: 2012-2016 and rebaseline](./m1-staar-3-8-pilot.md#m1-phase-3)                       |  15 days |    2026-11-16 |  2026-12-04 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
| [M2: Core STAAR families](./m2-core-staar-families.md)                     |                                                                                          |  90 days |    2027-01-04 |  2027-05-07 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P1: STAAR EOC](./m2-core-staar-families.md#m2-phase-1)                                  |  40 days |    2027-01-04 |  2027-02-26 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P2: Alternate 2 grades 3-8](./m2-core-staar-families.md#m2-phase-2)                     |  25 days |    2027-03-01 |  2027-04-02 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P3: Alternate 2 EOC](./m2-core-staar-families.md#m2-phase-3)                            |  25 days |    2027-04-05 |  2027-05-07 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
| [M3: Accountability and TELPAS](./m3-accountability-and-telpas.md)         |                                                                                          |  65 days |    2027-05-10 |  2027-08-06 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P1: Consolidated accountability](./m3-accountability-and-telpas.md#m3-phase-1)          |  25 days |    2027-05-10 |  2027-06-11 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P2: TELPAS 2012-2021](./m3-accountability-and-telpas.md#m3-phase-2)                     |  25 days |    2027-06-14 |  2027-07-16 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P3: TELPAS 2022-2026](./m3-accountability-and-telpas.md#m3-phase-3)                     |  15 days |    2027-07-19 |  2027-08-06 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
| [M4: Remaining families](./m4-remaining-families.md)                       |                                                                                          |  45 days |    2027-08-09 |  2027-10-08 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P1: TELPAS Alternate](./m4-remaining-families.md#m4-phase-1)                            |  20 days |    2027-08-09 |  2027-09-03 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P2: Interim, TFAR, and TTAP](./m4-remaining-families.md#m4-phase-2)                     |  15 days |    2027-09-06 |  2027-09-24 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P3: CRS custom](./m4-remaining-families.md#m4-phase-3)                                  |  10 days |    2027-09-27 |  2027-10-08 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
| [M5: Cross-family verification](./m5-cross-family-verification.md)         |                                                                                          |  15 days |    2027-10-11 |  2027-10-29 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P1: Shared concepts and source gaps](./m5-cross-family-verification.md#m5-phase-1)      |   8 days |    2027-10-11 |  2027-10-20 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P2: Findings and coverage reconciliation](./m5-cross-family-verification.md#m5-phase-2) |   7 days |    2027-10-21 |  2027-10-29 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
| [M6: Remediation plan and closeout](./m6-remediation-plan-and-closeout.md) |                                                                                          |   5 days |    2027-11-01 |  2027-11-05 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P1: Prioritize remediation](./m6-remediation-plan-and-closeout.md#m6-phase-1)           |   3 days |    2027-11-01 |  2027-11-03 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |
|                                                                            | [P2: Program closeout](./m6-remediation-plan-and-closeout.md#m6-phase-2)                 |   2 days |    2027-11-04 |  2027-11-05 |          TBD |        TBD | TBD           | <span style="color: #b91c1c;">Not Started</span> |

December 7-18, 2026 is reserved for pilot rebaselining, source preparation,
and family assignments. No review work is planned for December 21, 2026
through January 1, 2027. Open work carries forward explicitly when the
schedule resumes.

## Dependency Rules

- M0 and M1 are sequential because the pilot validates the framework.
- M1 completion includes schedule rebaselining before M2 begins.
- M2 through M4 are planned sequentially for the baseline staffing model.
  The program owner may approve parallel family branches when independent
  review capacity exists. Years within one family remain sequential.
- M5 begins only after all represented years have a completed initial review or
  a documented block.
- M6 begins only after coverage and finding records are reconciled.
- Remediation may start after a family review closes; confirmed critical
  findings do not wait for the full audit.

## Required Controls

Every milestone contains:

- a pre-checklist for scope and drift control
- phase checklists sized for focused pull requests
- a branch and pull request plan
- one year branch and review record per represented year
- a family integration branch and final family pull request
- review checks and exit criteria
- a milestone-level reconciliation and sign-off

If the plan changes, update this schedule, the affected milestone, and coverage
in the same pull request so they do not report conflicting states.
