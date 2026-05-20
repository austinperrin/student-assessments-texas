# Architecture Decision Records

This folder stores Architecture Decision Records (ADRs) for repository-level and
platform-level choices that should remain easy to revisit later.

Use ADRs when a decision has non-obvious tradeoffs, long-term structural impact,
or is likely to influence future implementation work.

## When To Write An ADR

- introducing a new top-level repository area
- choosing a framework or runtime baseline
- changing the long-term repository structure
- standardizing a validation, CI, or deployment pattern
- defining a durable data or schema contract

## Naming

Use sequential numbering and a concise slug:

- `0001-repo-shape-and-platform-intent.md`
- `0002-runtime-and-tooling-baseline.md`

## Status Values

- `Proposed`
- `In Progress`
- `Accepted`
- `Superseded`
- `Rejected`

## Minimum Sections

- `Status`
- `Date`
- `Context`
- `Decision`
- `Consequences`
- `Alternatives Considered`
- `Follow-Up`

See [0001-repo-shape-and-platform-intent.md](./0001-repo-shape-and-platform-intent.md)
for the initial example.

## Current ADRs

- [0001: Repository Shape and Platform Intent](./0001-repo-shape-and-platform-intent.md)
- [0002: College Board Vendor Structure](./0002-collegeboard-vendor-structure.md)
- [0003: NWEA Vendor Structure](./0003-nwea-vendor-structure.md)
- [0004: i-Ready Vendor Structure](./0004-iready-vendor-structure.md)
