# ADR 0004: i-Ready Vendor Structure

- **Status**: Accepted
- **Date**: 2026-05-20
- **Owners**: Repository Maintainers

## Context

i-Ready is expected to be added as another vendor in this repository.

Like other non-TEA vendors, i-Ready may expose multiple result exports or
reporting surfaces over time. The repository needs a durable decision for how
to add i-Ready without assuming that a single product label will always match
the actual delivered file family.

## Decision

- Reserve `assessments/iready/` as the vendor root for future i-Ready mappings.
- Prefer result-delivery, reporting, or export-family folders below the vendor
  root when those are the stable source units for current and historic files.
- Use product or assessment labels as subfolders only when they match the file
  family described in the official source documents.
- Mirror confirmed i-Ready source structures under
  `docs/source-archives/iready/`.
- Keep the initial scaffold lightweight until official source documents are
  collected and verified.

## Consequences

- Positive:
  - keeps i-Ready aligned with the repository-wide vendor-first model
  - supports current and historic i-Ready file layouts without forcing a
    premature taxonomy
  - makes future source-archive mirroring straightforward
- Tradeoffs:
  - the initial i-Ready ADR is intentionally high-level until source documents
    are available
  - future maintainers must document actual file-family evidence before adding
    deeper scaffolding

## Alternatives Considered

- Create an assessment-brand-first i-Ready structure now.
  - Rejected because the durable routing unit may turn out to be a reporting or
    export family instead.
- Wait until after i-Ready mappings exist to define the vendor structure.
  - Rejected because the repository benefits from having vendor-level guidance
    before additional scaffolding work begins.

## Follow-Up

- add `assessments/iready/` and `docs/source-archives/iready/` scaffolding
  when i-Ready source collection begins
- capture official i-Ready source references before creating family-level
  folders
- add more specific ADRs later if i-Ready introduces materially distinct export
  systems or delivery channels

## Related

- [ADR 0001: Repository Shape and Platform Intent](./0001-repo-shape-and-platform-intent.md)
- [Assessments Corpus Overview](../../assessments/README.md)
- [Source Archives Overview](../source-archives/README.md)
