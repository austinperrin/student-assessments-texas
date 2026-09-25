# TEA Assessment Audit Program

## Objective

Verify that every tracked TEA mapping and related parser represents the
corresponding source layout accurately, and record enough evidence for another
reviewer to reproduce each conclusion.

## Program Navigation

- [Roadmap](./roadmap/index.md): canonical milestones, schedule, status, and
  dependencies
- [Workflow](./workflow.md): branch, commit, pull request, review-gate, and
  closure rules
- [Coverage](./coverage.md): family-level completion and assignments
- [Review checklist](./review-checklist.md): required checks for each package
- [Review record template](./review-template.md): evidence and sign-off record
- [Family audit template](./family-audit-template.md): year sequence,
  reconciliation, and final family sign-off
- [Review record layout](./reviews/README.md): tracked family and year record
  paths
- [Finding template](./finding-template.md): stable finding evidence and
  disposition

The roadmap reports when work is planned and underway. Coverage reports what
has actually been reviewed. Review records and findings support those claims.

Each represented year has its own review record and branch. Those year
branches merge one at a time into a family audit branch. The family branch
merges into `main` through one pull request after all represented years and the
family-wide reconciliation are complete.

## Scope

The program covers these 11 mapping families and 96 current mapping files:

| Workstream | Family                            | Mapping files | Years represented    |
| ---------- | --------------------------------- | ------------: | -------------------- |
| A          | STAAR grades 3-8                  |            15 | 2012-2026            |
| B          | STAAR EOC                         |            15 | 2012-2026            |
| C          | STAAR Alternate 2 grades 3-8      |            10 | 2016-2019, 2021-2026 |
| D          | STAAR Alternate 2 EOC             |            10 | 2016-2019, 2021-2026 |
| E          | STAAR consolidated accountability |            11 | 2014-2019, 2021-2025 |
| F          | STAAR interim                     |             3 | 2023, 2024, 2026     |
| G          | TELPAS                            |            15 | 2012-2026            |
| H          | TELPAS Alternate                  |             8 | 2019-2026            |
| I          | TFAR                              |             2 | 2024-2025            |
| J          | TTAP                              |             3 | 2023-2025            |
| K          | CRS custom                        |             4 | 2023-2026            |

Missing years are coverage facts to investigate; they are not automatically
defects.

## Review Layers

Each family/year receives three separately recorded reviews:

1. **Source and mapping:** official URL, archived copy, version alignment,
   positions, lengths, titles, codes, blanks, order, and metadata.
2. **Parser:** field references, joins, subject selection, score eligibility,
   history/current-year separation, and duplicate handling.
3. **Operational evidence:** representative delivered records when available,
   including edge cases. A missing sample is recorded as a limitation.

## Roles

- **Program owner:** maintains scope, priorities, and final dispositions.
- **Reviewer:** performs the first source comparison and records evidence.
- **Verifier:** reproduces findings and challenges unsupported conclusions.
- **Remediator:** implements confirmed corrections in a separate change.
- **Approver:** accepts the correction and any downstream-data decision.

One person may hold multiple roles, but the reviewer and verifier should differ
for high- and critical-severity findings. AI reviewers may perform review and
verification work; an accountable human owns consequential dispositions.

## Finding States

`candidate` -> `confirmed` or `rejected` -> `planned` -> `corrected` ->
`verified` -> `closed`

`deferred`, `accepted-risk`, and `blocked` are terminal only when the record
names the owner, reason, and review date.

## Severity

- **Critical:** can associate results with the wrong student or materially alter
  high-stakes interpretation across many records.
- **High:** can select, omit, or materially misinterpret results.
- **Medium:** mapping meaning, range, metadata, or parser behavior is inaccurate
  but the primary result remains usable.
- **Low:** documentation, normalization, or maintainability issue with limited
  operational effect.

## Source Precedence

The current official TEA or Texas Assessments source governs active mappings.
The matching archived PDF is compared with it. If they differ, record a source
version finding before judging the mapping. Do not infer a field from a nearby
year when the reviewed year's source is clear.

## Completion Criteria

A family is complete when every represented year has a closed review record,
all source gaps are documented, all confirmed findings have dispositions, and
the family coverage entry links to remediation and verification where needed.
