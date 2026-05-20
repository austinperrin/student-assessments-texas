# ADR 0002: College Board Vendor Structure

- **Status**: In Progress
- **Date**: 2026-05-20
- **Owners**: Repository Maintainers

## Context

College Board result files do not always map cleanly to a single branded
assessment name.

Some College Board products are better modeled by the reporting or
delivery-family boundary that emits the files districts, schools, and higher-ed
institutions actually receive. At the same time, not every possible College
Board product family is documented enough yet to justify deep scaffolding.

The repository needed a durable rule for how to structure College Board assets
while preserving room for current and historic layouts.

## Decision

- Keep `assessments/collegeboard/` as the vendor root for College Board mapping
  work.
- Organize confirmed College Board families by stable delivery or reporting
  units when those are more durable than the assessment brand alone.
- Use `sat_suite/` as a top-level College Board family and separate:
  - `k12_reporting/`
  - `higher_ed_reporting/`
- Use `ap/` as a top-level College Board family and separate:
  - `k12_score_reports/`
  - `higher_ed_score_reports/`
- Keep `pre_ap/` as a lightweight placeholder family until durable public
  result-file layouts are confirmed.
- Keep `accuplacer/` only as a top-level placeholder for now, without nested
  delivery-family scaffolding until official source materials justify it.
- Mirror the same vendor and family structure under
  `docs/source-archives/collegeboard/` for local source references.

## Consequences

- Positive:
  - keeps College Board structure aligned to the files institutions actually
    receive
  - supports current and historic layouts without forcing all products into the
    same taxonomy
  - avoids over-modeling ACCUPLACER before source evidence exists
  - makes archive and mapping paths easier to line up
- Tradeoffs:
  - College Board structure is less uniform than a brand-only hierarchy
  - some top-level placeholders may remain lightly used until more sources are
    confirmed

## Alternatives Considered

- Organize College Board only by marketing program names.
  - Rejected because reporting families such as SAT Suite K-12 and higher-ed
    outputs have materially different delivered layouts.
- Create deep scaffolding for every suspected College Board family immediately.
  - Rejected because some families, especially ACCUPLACER, are not yet backed
    by sufficient public source documents.
- Flatten all College Board layouts directly under `assessments/collegeboard/`.
  - Rejected because it would make historic layout routing and archive mirroring
    harder to maintain.

## Follow-Up

- keep adding year-specific mapping files only after official source layouts are
  confirmed
- document missing or retired College Board source files in the vendor archive
  README when they cannot be retrieved publicly
- expand placeholder families only when official College Board source documents
  justify deeper scaffolding

## Related

- [ADR 0001: Repository Shape and Platform Intent](./0001-repo-shape-and-platform-intent.md)
- [College Board Assessments](../../assessments/collegeboard/README.md)
- [College Board Data File Formats Archive](../source-archives/collegeboard/README.md)
