# Texas Assessments Fixed-Width Mappings

This repository is the source of truth for year-specific JSON mappings of Texas
assessment fixed-width data layouts.

The current working corpus is TEA-specific, but the repository is structured so
future vendors, tooling, and runtime consumers can be added without another
top-level reorganization.

## Start Here

- [assessments/](./assessments/)
  Canonical assessment mappings grouped by vendor or source system.
- [docs/index.md](./docs/index.md)
  Documentation index for standards, roadmap, ADRs, workflow references, and
  the TEA source-document archive.
- [scripts/](./scripts/)
  Shared automation for validation, sorting, merging, and repository
  maintenance.
- [configs/](./configs/)
  Shared schema and repository-level configuration references.

## Repository Model

The repository is organized around a few durable responsibilities:

- [assessments/](./assessments/)
  Stores the authoritative mapping corpus.
- [docs/](./docs/)
  Stores human-facing documentation, standards, roadmap material, and source
  reference archives.
- [scripts/](./scripts/)
  Stores repository automation and maintenance tooling.
- [configs/](./configs/)
  Stores shared schemas and validation contracts.
- [services/](./services/)
  Reserved for future application or runtime services.
- [packages/](./packages/)
  Reserved for future shared libraries, loaders, or reusable tooling modules.
- [infra/](./infra/)
  Reserved for future infrastructure and environment-oriented artifacts.

## Navigate The Corpus

Assessment mappings currently live under [assessments/tea/](./assessments/tea/)
with the following families:

- [assessments/tea/staar/3_8](./assessments/tea/staar/3_8/)
- [assessments/tea/staar/eoc](./assessments/tea/staar/eoc/)
- [assessments/tea/staar/alt2_3_8](./assessments/tea/staar/alt2_3_8/)
- [assessments/tea/staar/alt2_eoc](./assessments/tea/staar/alt2_eoc/)
- [assessments/tea/staar/interim](./assessments/tea/staar/interim/)
- [assessments/tea/staar/consolidated_accountability](./assessments/tea/staar/consolidated_accountability/)
- [assessments/tea/telpas/telpas](./assessments/tea/telpas/telpas/)
- [assessments/tea/telpas/telpas_alt](./assessments/tea/telpas/telpas_alt/)
- [assessments/tea/tfar](./assessments/tea/tfar/)
- [assessments/tea/ttap](./assessments/tea/ttap/)
- [assessments/tea/crs](./assessments/tea/crs/)

Most family folders include their own `README.md` and, where needed, `AGENTS.md`
files for local rules, year coverage notes, and maintenance exceptions.

## Mapping File Shape

Each mapping file follows the same high-level structure:

```json
{
  "metadata": [
    {
      "author": "Austin Perrin",
      "date_created": "2026-05-11",
      "file_name": "2026-example-fixed-width-mapping.json",
      "school_year": "2025-2026",
      "pdf_url": "https://tea.texas.gov/..."
    }
  ],
  "mapped_fields": [
    {
      "start_pos": "1",
      "end_pos": "4",
      "column_header": "example_field",
      "column_num": "1"
    }
  ]
}
```

Shared repository rules include:

- store mapping values as strings
- omit blank source fields from `mapped_fields`
- preserve original source ordering in `column_num`, including gaps caused by
  omitted blanks
- normalize headers to lowercase snake case
- keep `metadata.pdf_url` aligned to the official source document

## Coverage Snapshot

Current TEA mapping coverage in the repository:

- `staar/3_8`: `2012`-`2026`
- `staar/eoc`: `2012`-`2026`
- `staar/alt2_3_8`: `2016`-`2019`, `2021`-`2026`
- `staar/alt2_eoc`: `2016`-`2019`, `2021`-`2026`
- `staar/interim`: `2023`, `2024`, `2026`
- `staar/consolidated_accountability`: `2014`-`2019`, `2021`-`2025`
- `telpas/telpas`: `2012`-`2026`
- `telpas/telpas_alt`: `2019`-`2026`
- `tfar`: `2024`-`2025`
- `ttap`: `2023`-`2025`
- `crs`: `2023`-`2026`

Notes:

- school-year PDFs use the ending year in the mapping filename
- some families intentionally skip years where no official source could be
  confirmed
- `staar/interim` includes the separate `2022-2023` interim and BOY
  student-results layout under the `2023` mapping year

## Documentation System

The documentation hub is [docs/index.md](./docs/index.md). The most useful
entrypoints are:

- [docs/overview/README.md](./docs/overview/README.md)
  Repository purpose and long-term direction.
- [docs/overview/repository-navigation.md](./docs/overview/repository-navigation.md)
  Navigation guide for the top-level repository areas and documentation system.
- [docs/overview/scripts-and-commands.md](./docs/overview/scripts-and-commands.md)
  Script glossary and common command patterns.
- [docs/standards/](./docs/standards/)
  Human-readable repository standards.
- [docs/roadmap/index.md](./docs/roadmap/index.md)
  Milestone-level repository roadmap.
- [docs/adr/README.md](./docs/adr/README.md)
  Architecture Decision Record guidance.
- [docs/tea-data-file-formats-archive/](./docs/tea-data-file-formats-archive/)
  Local PDF archive of TEA and Texas Assessments source layouts.

The local archive is for maintenance and reference. The official online TEA or
Texas Assessments documentation remains the source of truth, and each mapping's
`metadata.pdf_url` should stay aligned to that official source.

## Validation And Tooling

Repository validation and automation are documented in
[scripts/README.md](./scripts/README.md). Common entrypoints include:

- `python scripts/ci/validate_repo.py`
- `npm run format`
- `npm run lint`
- `python scripts/mappings/sort_tea_assessments.py`
- `python scripts/mappings/merge_tea_assessment_files.py`

The sorter and merger workflows are documented in
[scripts/mappings/README.md](./scripts/mappings/README.md).

## Working Expectations

When adding or updating mappings:

1. Start from the current-year official source documentation.
2. Check the relevant folder-level guidance before editing.
3. Preserve real year-specific meaning changes instead of normalizing them away.
4. Validate JSON shape, header uniqueness, and documentation portability after
   edits.

For shared repository standards and workflow expectations, see:

- [AGENTS.md](./AGENTS.md)
- [docs/standards/coding-standards.md](./docs/standards/coding-standards.md)
- [docs/standards/commits.md](./docs/standards/commits.md)
- [docs/standards/scripts.md](./docs/standards/scripts.md)
