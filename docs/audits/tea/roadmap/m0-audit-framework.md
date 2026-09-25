# Milestone 0: Audit Framework

- Status: In Progress
- Estimate: 7 business days
- Dependencies: none
- Planned dates: 2026-09-24 through 2026-10-02

## Owners

- Milestone owner: Program owner
- Execution: Docs and standards reviewer
- Review: Audit reviewer and verifier representatives

## Goal

Establish a durable, evidence-based audit process that people and AI reviewers
can execute consistently without changing the assets under review.

## Milestone Pre-Checklist

- [x] Confirm all TEA mapping families and represented years.
- [x] Separate durable records from disposable `.tmp` evidence.
- [x] Define audit and remediation as separate changes.
- [ ] Confirm the baseline staffing and calendar assumptions.

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

- [ ] A reviewer can create a complete record without inventing required fields.
- [ ] High- and critical-severity verification requirements are unambiguous.

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

- [ ] Schedule, milestone files, and coverage have distinct ownership.
- [ ] Every planned family appears in a milestone.

<a id="m0-phase-3"></a>

## Phase 3: Framework Review

### Checklist

- [ ] Walk through one hypothetical review and finding from start to closure.
- [ ] Check all repository-relative links.
- [ ] Run repository documentation validation.
- [ ] Record reviewer feedback and resolve material ambiguity.

### Branch and PR Plan

- Branch: `docs/tea-audit-framework`
- PR target: `main`

### Exit Criteria

- [ ] Framework PR is approved and ready to merge.
- [ ] Pilot owners and assignments are recorded.

## Milestone Review Checklist

- [ ] All phase exit criteria are complete.
- [ ] Roadmap dates and status match actual execution.
- [ ] Coverage counts match the repository inventory.
- [ ] Framework validation passes.
- [ ] Milestone status is set to `Completed` after merge.

## Next Step

Proceed to [Milestone 1: STAAR Grades 3-8 Pilot](./m1-staar-3-8-pilot.md).
