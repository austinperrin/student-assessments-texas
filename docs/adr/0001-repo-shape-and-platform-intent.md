# ADR 0001: Repository Shape and Platform Intent

- **Status**: Accepted
- **Date**: 2026-05-11
- **Owners**: Repository Maintainers

## Context

This repository began as a curated collection of Texas assessment fixed-width
mapping files and supporting TEA PDF references.

The immediate need is still data curation, validation, and documentation.
However, the repository is expected to evolve into a broader application,
platform, or tooling workspace that can use these mappings operationally.

That future direction creates a structural tension:

- keep the current repository simple and mapping-focused
- avoid painting the repository into a shape that becomes awkward once code,
  services, and shared libraries are introduced

## Decision

- Keep `assessments/` as the primary source-of-truth root for canonical
  assessment mappings.
- Group assessment assets by vendor or source system under `assessments/`
  so future non-TEA vendors can be added without another top-level reorganization.
- Within a vendor, allow delivery-family or reporting-system folders when those
  are the stable units for current and historic result-file layouts.
- Treat the repository as data-first today and platform-ready for later growth.
- Reserve top-level areas for future implementation work:
  - `services/` for application or runtime services
  - `packages/` for shared libraries, schemas, or reusable modules
  - `infra/` for deployment and runtime artifacts
- Expand `docs/` into a real documentation system instead of using it only as
  a PDF archive.
- Use ADRs for future structural, runtime, framework, and deployment decisions
  once the repository begins adding application code.

## Consequences

- Positive:
  - preserves the current mapping workflow without unnecessary app complexity
  - keeps canonical assessment assets decoupled from any single runtime surface
  - makes future vendor expansion easier to introduce incrementally
  - reduces future restructuring when services or packages are introduced
  - makes documentation, standards, and tooling easier to scale
- Tradeoffs:
  - introduces some empty or lightly used scaffolding before all of it is needed
  - requires discipline to avoid adding heavyweight platform choices too early

## Alternatives Considered

- Keep the repository as a flat mapping-only workspace indefinitely.
  - Rejected because the expected growth into tooling and application code would
    likely force a noisier reorganization later.
- Fully adopt an application-monorepo shape immediately.
  - Rejected because the repository does not yet have enough application code to
    justify framework-first complexity.

## Follow-Up

- add lightweight placeholders for future `services/` and `packages/`
- keep `assessments/` and vendor-level docs aligned as new vendors, delivery
  families, or mapping families are introduced
- continue expanding documentation for standards, roadmap, and ADR usage
- record future runtime or framework choices in separate ADRs when they become concrete

## Related

- [Repository Overview](../overview/README.md)
- [Repository Roadmap](../roadmap/index.md)
- [ADR Standards](../standards/adr.md)
