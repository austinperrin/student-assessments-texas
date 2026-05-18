# Texas Student Assessments

This project curates year-specific JSON mappings, reference materials, and
supporting tooling for Texas student assessment data workflows.

The current working focus is TEA and Texas Assessments fixed-width layouts, but
the project is structured so future assessment programs, tooling, and
runtime consumers can be added without another top-level reorganization.

## Start Here

- [assessments/](./assessments/)
  Assessment mappings grouped by vendor or source system.
- [docs/index.md](./docs/index.md)
  Documentation index for standards, roadmap, ADRs, workflow references, and
  the TEA source-document archive.
- [scripts/](./scripts/)
  Shared automation for validation, sorting, merging, and project
  maintenance.
- [configs/](./configs/)
  Shared schema and project-level configuration references.

## Project Structure

The project is organized around a few durable responsibilities:

- [assessments/](./assessments/)
  Stores the current assessment mapping corpus.
- [docs/](./docs/)
  Stores human-facing documentation, standards, roadmap material, and source
  reference archives.
- [scripts/](./scripts/)
  Stores shared automation and maintenance tooling.
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

Most family folders include their own `README.md` files for year coverage
notes, naming expectations, and local maintenance guidance.

## TEA Mapping File Shape

The current TEA assessment mappings in this project generally follow this
high-level shape:

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
  "filename_patterns": [
    {
      "regex": "^SF_0526_.*\\.txt$",
      "references": ["https://www.texasassessment.gov/..."]
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

This example is TEA-specific. Other assessment programs added in the future may
use a different JSON shape when their source materials or workflow needs differ.

Shared TEA mapping rules include:

- store mapping values as strings
- omit blank source fields from `mapped_fields`
- preserve original source ordering in `column_num`, including gaps caused by
  omitted blanks
- normalize headers to lowercase snake case
- keep `metadata.pdf_url` aligned to the official source document

## Coverage Snapshot

Current TEA mapping coverage in the project:

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
  Project purpose and long-term direction.
- [docs/overview/repository-navigation.md](./docs/overview/repository-navigation.md)
  Navigation guide for the top-level project areas and documentation system.
- [docs/overview/scripts-and-commands.md](./docs/overview/scripts-and-commands.md)
  Script glossary and common command patterns.
- [docs/standards/](./docs/standards/)
  Human-readable project standards.
- [docs/roadmap/index.md](./docs/roadmap/index.md)
  Milestone-level project roadmap.
- [docs/adr/README.md](./docs/adr/README.md)
  Architecture Decision Record guidance.
- [docs/tea-data-file-formats-archive/](./docs/tea-data-file-formats-archive/)
  Local PDF archive of TEA and Texas Assessments source layouts.

The local archive is for maintenance and reference. The official online TEA or
Texas Assessments documentation remains the governing reference, and each
mapping's `metadata.pdf_url` should stay aligned to that official source.

## Validation And Tooling

Validation and automation are documented in
[scripts/README.md](./scripts/README.md). Common entrypoints include:

- `python scripts/ci/validate_repo.py`
- `npm run format`
- `npm run lint`
- `python scripts/mappings/sort_tea_assessments.py`
- `python scripts/mappings/merge_tea_assessment_files.py`
  Supports `--include-archives` and optional `--unique` row deduplication.

The sorter and merger workflows are documented in
[scripts/mappings/README.md](./scripts/mappings/README.md).

## Working Expectations

When adding or updating mappings:

1. Start from the current-year official source documentation.
2. Check the relevant folder-level guidance before editing.
3. Preserve real year-specific meaning changes instead of normalizing them away.
4. Validate JSON shape, header uniqueness, and documentation portability after
   edits.

For shared project standards and workflow expectations, see:

- [docs/standards/coding-standards.md](./docs/standards/coding-standards.md)
- [docs/standards/commits.md](./docs/standards/commits.md)
- [docs/standards/scripts.md](./docs/standards/scripts.md)
