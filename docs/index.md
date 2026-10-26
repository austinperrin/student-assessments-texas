# Documentation Hub

This is the primary entrypoint for learning and using the repository. Choose a
path based on what you need to do rather than browsing the folder tree.

## First Visit

Read these pages in order:

1. [Project overview](./overview/README.md)
   Understand the repository's purpose, current scope, and planned direction.
2. [Repository navigation](./overview/repository-navigation.md)
   Learn what belongs in each major project area.
3. [Assessment corpus](../assessments/README.md)
   Explore mappings by vendor, delivery family, assessment variant, and year.
4. [Standards](./standards/README.md)
   Review the shared rules before changing mappings, documentation, or tools.

## Choose A Task

### Operate the TEA processing tools

1. Use the [command index](./overview/scripts-and-commands.md) to select an
   entrypoint.
2. Follow the authoritative [runbook](./runbooks/README.md) for preparation,
   options, side effects, verification, and recovery.
3. Use [mapping script implementation notes](../scripts/mappings/README.md) only
   when changing the code or tests.

### Maintain an assessment mapping

1. Start at the [assessment corpus](../assessments/README.md) and navigate to the
   closest family `README.md`.
2. Review the [coding and mapping standards](./standards/coding-standards.md).
3. Find the governing material in the
   [source archive](./source-archives/README.md), while treating the current
   official online source as authoritative.
4. Run the validation described by the family guidance and project standards.

### Audit TEA source fidelity

1. Start at [Repository audits](./audits/README.md).
2. Follow the [TEA audit program](./audits/tea/README.md).
3. Use its workflow, checklist, templates, coverage, and review records rather
   than creating a separate audit process.

### Change repository structure or policy

1. Review the [standards index](./standards/README.md).
2. Check existing [architecture decisions](./adr/README.md).
3. Review the [repository roadmap](./roadmap/index.md).
4. Record a new ADR when the decision has durable structural consequences.

## Documentation Map

- [Overview](./overview/README.md)
  Project purpose, repository navigation, and command index.
- [Runbooks](./runbooks/README.md)
  Authoritative procedures for recurring operations.
- [Standards](./standards/README.md)
  Durable rules for mappings, scripts, documentation, commits, and ADRs.
- [Assessment mappings](../assessments/README.md)
  Canonical mapping corpus and family-level maintenance guidance.
- [Source archives](./source-archives/README.md)
  Local copies of vendor source material organized by vendor and delivery
  family or year as appropriate.
- [Audits](./audits/README.md)
  Source-fidelity programs, evidence, coverage, and findings.
- [Architecture decisions](./adr/README.md)
  Durable structural decisions and their rationale.
- [Roadmap](./roadmap/index.md)
  Repository evolution and planned work.
- [GitHub workflows](../.github/overview.md)
  CI automation and contribution templates.

## Where Information Belongs

| Information                   | Authoritative location                  |
| ----------------------------- | --------------------------------------- |
| Project purpose and structure | `docs/overview/`                        |
| Commands available            | `docs/overview/scripts-and-commands.md` |
| How to perform an operation   | `docs/runbooks/`                        |
| Durable working rules         | `docs/standards/`                       |
| Mapping-family specifics      | nearest `assessments/**/README.md`      |
| AI-agent guidance             | nearest `AGENTS.md`                     |
| Official-source local copies  | `docs/source-archives/`                 |
| Audit evidence and status     | `docs/audits/`                          |
| Structural decision rationale | `docs/adr/`                             |

See the [documentation standard](./standards/documentation.md) for ownership and
cross-reference rules.
