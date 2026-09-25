# TEA Audit Framework Readiness Review

- Review date: 2026-09-24
- Reviewer: Codex
- Repository baseline: `d3648a33da07b144924f82e3d62373c91b3c6a8c`
- Working branch: `docs/tea-audit-readiness`
- Governing milestone: [M0](./roadmap/m0-audit-framework.md)
- Scope: framework walkthrough, repository inventory, and pilot readiness.
- Status: framework feedback resolved, pilot roles agreed, and full lint passed;
  framework review and merge are complete. This is not a source/mapping audit.

## Baseline Evidence

The working tree was clean before this review. The framework is present in the
baseline commit, whose subject identifies merged pull request #15. Local
`main` and `origin/main` pointed to that commit; remote freshness was not checked.

The inventory contains 96 TEA mappings across all 11 documented families.
Counts and represented years agree with the audit overview and coverage matrix;
the matrix has 96 mapping links. All families have milestone assignments in
M1 through M4. No year review records exist yet.

- `python scripts/ci/validate_repo.py`: passed using the local virtual
  environment; 96 mappings and 147 Markdown files validated before edits.
- Separate scan of all mapped headers: 23,140 headers, maximum length 63,
  zero over the limit. The existing mapping validator does not enforce this
  length limit, so passing it alone does not establish compliance.
- `npm run lint`: passed after restoring dependencies through the configured
  Yarn registry; formatting and repository validation both pass.
- Documentation validation checks relative target paths, but does not validate
  Markdown fragment anchors or external URLs.

These checks establish structural readiness only. Official sources have not
been retrieved or compared with archived PDFs during this framework review.

## Framework Walkthrough

This hypothetical case exercises the process; it is not a real finding and
does not count toward coverage.

1. After M0 acceptance, create the STAAR 3-8 family branch from current `main`,
   initialize its family record, and create its 2026 year branch.
2. Record the repository commit, mapping, source retrieval date, and
   archived/online agreement in the year template.
3. If a source comparison suggests incorrect result eligibility, record a
   candidate using `TEA-STAAR38-2026-001`, exact source page and positions,
   observed implementation, and separately stated proposed disposition.
4. If classified high or critical, obtain an independent verifier's reproduction
   before confirmation. An unverified candidate remains a candidate.
5. Record sample limitations. Missing samples limit runtime and record-impact
   conclusions.
6. Give a confirmed finding an owner and disposition. Any correction uses a
   separate `fix/tea-*` branch and includes a historical-data decision.
7. Close the year review only after its review requirements and dispositions
   are recorded, then merge it into the family branch without squashing.
   A finding may remain open after the year review closes.
8. After all 15 years, reconcile the family record and coverage and obtain
   family sign-off before the family PR merges into `main`.
9. Close the finding only after correction verification and the required
   downstream-data decision are recorded.

The roadmap owns schedule, coverage owns completed review layers, and records
own evidence. Those responsibilities are distinct in the existing workflow.

## Feedback Resolution

- Template portability: the year template now specifies how to rebase its
  finding-template link when copied into a family review folder.
- Finding ownership: the finding template now includes disposition owner,
  target date, next review date, reason, and acceptance fields.
- Accepted blocks: workflow and review template distinguish incomplete layers
  from accepted closure exceptions and specify the required evidence.
- Independent verification: high/critical confirmation explicitly requires a
  verifier other than the original reviewer and a recorded reproduction.
- Schedule prose: removed the unsupported holiday-buffer references between
  M3 and M4. Planned dates remain unchanged.
- Source inputs: year records now include source version/hash fields so source
  evidence is reproducible.

## Agreed Pilot Assignments

Confirmed by the program owner in this session:

- Program owner: Austin Perrin.
- Reviewer: Codex.
- Independent verifier: Austin Perrin. Assignment does not constitute completed
  verification; high/critical candidates require his actual review.
- Operational samples: unavailable. Source review can proceed once M0 closes;
  runtime and record-impact conclusions remain limited.
- Staffing and calendar: provisional. The existing 10-12 reviewer hours and
  3-4 verifier hours per week are planning assumptions, not capacity commitments.
  Rebaseline after the pilot as required by M1.

## Validation And Framework Closeout

System Node `v24.21.0` and npm `11.19.0` are available on PATH. After the
user configured `https://registry.yarnpkg.com/`, the locked dependency restore
(`npm ci --ignore-scripts --no-audit --no-fund`) installed 128 packages.
No package manifest or lockfile changes were needed. Installation lifecycle
scripts were skipped for this validation run.

Full `npm run lint` passes with the repository virtual environment's Python
on PATH: Prettier accepts all matched files, and repository validation accepts
96 mappings and 148 Markdown files. Separate checks confirm header uniqueness
and the 63-character limit across all 96 mappings. `git diff --check` passes.

M0 completed on 2026-09-24 after PR #16 merged as
`a48227f94faa57c29bfb8564e392015056c20f16`. GitHub's Validate Repository
workflow passed before merge. Codex completed the framework review; Austin
Perrin authorized review, merge, and pilot initialization in this session.
This acceptance does not constitute verification of any year-level finding.

The family branch can now start from updated `main`, followed by the 2026 year
branch. No year audit was performed on the framework branch.

## Pilot Handoff

The first planned year is 2026, followed by 2025 through 2012 in descending
order, as specified by [M1](./roadmap/m1-staar-3-8-pilot.md).

- Mapping: [2026 STAAR 3-8](../../../assessments/tea/staar/3_8/2026-staar-3-8-fixed-width-mapping.json).
- Archived source: [2026 layout](../../source-archives/tea/2026/2026-staar-3-8-data-file-layout-final-tagged.pdf).
- Archived PDF SHA-256:
  `268062469be138f57ef413df7a6148717607137558a3d3c50b254e47936da774`.
- Official URL is recorded in mapping metadata; retrieval and archive agreement
  remain pending for the year audit.
- Operational samples: unavailable, as confirmed by the program owner.

Next, initialize the family and first year branches. No mapping changes were
made, and no source or sample review layer is marked complete.
