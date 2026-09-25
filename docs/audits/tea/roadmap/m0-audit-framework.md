# Milestone 0: Audit Framework

- Status: In Review
- Estimate: 7 business days
- Dependencies: none
- Planned dates: 2026-09-24 through 2026-10-02

## Owners

- Milestone owner: Austin Perrin
- Execution: Codex
- Review: Austin Perrin

## Goal

Establish a durable, evidence-based audit process that people and AI reviewers
can execute consistently without changing the assets under review.

## Milestone Pre-Checklist

- [x] Confirm all TEA mapping families and represented years.
- [x] Separate durable records from disposable `.tmp` evidence.
- [x] Define audit and remediation as separate changes.
- [x] Confirm the baseline staffing and calendar assumptions as provisional.

<a id="m0-phase-1"></a>

## Phase 1: Governance and Templates

### Checklist

- [x] Define scope, roles, source precedence, finding states, and severity.
- [x] Add the review checklist, review record template, and finding template.
- [x] Add the family coverage matrix.

### Branch and PR Plan

- Branch: `docs/tea-audit-framework`
- PR target: `main`

### Exit Criteria

- [x] A reviewer can create a complete record without inventing required fields.
- [x] High- and critical-severity verification requirements are unambiguous.

<a id="m0-phase-2"></a>

## Phase 2: Roadmap and Workflow

### Checklist

- [x] Establish a canonical schedule and allowed status values.
- [x] Split the program into milestones, phases, and work packages.
- [x] Define branch, commit, PR, merge-gate, and closure conventions.
- [x] Link roadmap, workflow, templates, and coverage from audit navigation.

### Branch and PR Plan

- Branch: `docs/tea-audit-framework`
- PR target: `main`

### Exit Criteria

- [x] Schedule, milestone files, and coverage have distinct ownership.
- [x] Every planned family appears in a milestone.

<a id="m0-phase-3"></a>

## Phase 3: Framework Review

### Checklist

- [x] Walk through one hypothetical review and finding from start to closure.
- [x] Check all repository-relative links.
- [x] Run repository documentation validation.
- [x] Record reviewer feedback and resolve material ambiguity.

### Branch and PR Plan

- Branch: `docs/tea-audit-framework`
- PR target: `main`

### Exit Criteria

- [ ] Framework PR is approved and ready to merge.
- [x] Pilot owners and assignments are recorded.

## Milestone Review Checklist

- [ ] All phase exit criteria are complete.
- [x] Roadmap dates and status match actual execution.
- [x] Coverage counts match the repository inventory.
- [x] Framework validation passes.
- [ ] Milestone status is set to `Completed` after merge.

## Readiness Review

The [2026-09-24 readiness review](../framework-readiness.md) records the
repository baseline, inventory checks, hypothetical walkthrough, pilot inputs,
and feedback resolutions. Austin Perrin owns the pilot and independent
verification; Codex performs the initial review. Samples are unavailable and
calendar assumptions remain provisional. Full lint passes; review/merge remain
open on the follow-up branch `docs/tea-audit-readiness`.

## Next Step

Proceed to [Milestone 1: STAAR Grades 3-8 Pilot](./m1-staar-3-8-pilot.md).
