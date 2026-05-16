# Project Navigation

This guide describes the responsibility of each major project area and the
best entrypoint for navigating it.

## Top-Level Areas

- [../..](../../)
  Project root and primary overview.
- [../../assessments/](../../assessments/)
  Canonical assessment mappings grouped by vendor or source system.
- [../../docs/](../../docs/)
  Human-facing documentation, standards, roadmap material, ADRs, and source
  archives.
- [../../scripts/](../../scripts/)
  Shared automation, validation, and maintenance tooling.
- [../../configs/](../../configs/)
  Shared schemas and configuration references used by validation and tooling.
- [../../services/](../../services/)
  Reserved for future application or runtime services.
- [../../packages/](../../packages/)
  Reserved for future shared libraries, loaders, and reusable modules.
- [../../infra/](../../infra/)
  Reserved for future infrastructure and environment-oriented artifacts.
- [../../.github/overview.md](../../.github/overview.md)
  Workflow automation and contribution-template overview.

## Recommended Navigation Paths

If you are trying to understand the project:

- start at [../../README.md](../../README.md)
- move to [../README.md](../README.md)
- then use [../index.md](../index.md)

If you are trying to work on mappings:

- start at [../../assessments/README.md](../../assessments/README.md)
- move to [../../assessments/tea/README.md](../../assessments/tea/README.md)
- then open the family-specific `README.md` for the folder you plan to edit

If you are trying to understand validation or tooling:

- start at [../../scripts/README.md](../../scripts/README.md)
- then review [scripts-and-commands.md](./scripts-and-commands.md)
- then use [../../scripts/ci/README.md](../../scripts/ci/README.md) for CI
  validation details

If you are trying to understand policies and durable decisions:

- use [../standards/](../standards/)
- review [../roadmap/index.md](../roadmap/index.md)
- check [../adr/README.md](../adr/README.md)

## Documentation Design Rules

The documentation system follows a few navigation rules:

- major folders should expose a local `README.md`
- top-level and shared-system docs should link laterally, not only downward
- links should remain repo-relative and machine-portable
- human-facing docs should explain responsibility and entrypoints, not just list
  files
- family-specific guidance should stay close to the family folder rather than
  being buried in central docs

## Related References

- [README.md](./README.md)
  Project purpose and scope.
- [scripts-and-commands.md](./scripts-and-commands.md)
  Command glossary for the active automation surface.
