# ADR 0003: NWEA Vendor Structure

- **Status**: In Progress
- **Date**: 2026-05-20
- **Owners**: Repository Maintainers

## Context

NWEA is expected to be added as another vendor in this repository.

As with other vendors, the repository needs a stable rule for how NWEA result
files should be organized across time. NWEA products may include multiple
assessment lines and multiple export or reporting surfaces, so a brand-only
folder layout may not always be durable enough for historic and current files.

## Decision

- Reserve `assessments/nwea/` as the vendor root for future NWEA mappings.
- Prefer delivery-family, reporting-system, or result-export boundaries below
  `assessments/nwea/` when those are the stable units of file delivery.
- Use branded assessment families below the vendor root only when the source
  documents show that the brand boundary also matches the delivered file family.
- Mirror confirmed NWEA source structures under
  `docs/source-archives/nwea/`.
- Keep the initial NWEA scaffold lightweight until official current and
  historic source documents are archived.

## Consequences

- Positive:
  - keeps the NWEA structure compatible with the repository-wide
    vendor-first, delivery-family-aware model
  - leaves room for multiple NWEA products without another top-level
    reorganization
  - supports future historic file mapping work cleanly
- Tradeoffs:
  - early NWEA scaffolding may remain generic until source docs are collected
  - maintainers must resist inventing product splits before official source
    evidence exists

## Alternatives Considered

- Model NWEA only by product brands from the start.
  - Rejected because result delivery boundaries may prove more durable than the
    brand names alone.
- Delay any NWEA structural decision until mappings are added.
  - Rejected because a vendor-level ADR helps future scaffolding stay
    consistent with the rest of the repository.

## Follow-Up

- add `assessments/nwea/` and `docs/source-archives/nwea/` scaffolding when
  NWEA source collection begins
- document NWEA family boundaries based on official delivered-file references,
  not assumptions from other vendors
- add family-level READMEs once source-backed NWEA result formats are known

## Related

- [ADR 0001: Repository Shape and Platform Intent](./0001-repo-shape-and-platform-intent.md)
- [Assessments Corpus Overview](../../assessments/README.md)
- [Source Archives Overview](../source-archives/README.md)
