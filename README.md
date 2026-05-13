# Texas Assessments Fixed-Width Mappings

This repository curates year-specific JSON mapping files for assessment data layouts, with current coverage focused on Texas assessment families from TEA and Texas Assessments.

The mappings are built from official source layouts and normalized into a consistent JSON structure so the files can be reviewed, maintained, and used programmatically across assessment families and years. Today the active corpus is TEA-specific, but the repository structure is intentionally prepared for future non-TEA vendors under `assessments/`.

## Repository Structure

- [assessments](./assessments/)
  Canonical assessment mappings and maintenance docs grouped by vendor or source system
- [assessments/tea](./assessments/tea/)
  Current TEA and Texas Assessments mapping families, including `staar`, `telpas`, `tfar`, `ttap`, and `crs`
- [docs](./docs/)  
  Local project documentation and reference materials, including the TEA data file format archive
- [services](./services/)  
  Reserved for future application or runtime services
- [packages](./packages/)  
  Reserved for future shared libraries, schemas, and reusable tooling
- [infra](./infra/)  
  Shared infrastructure and environment-oriented repository artifacts

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

Common rules used across the repo:

- store mapping values as strings
- omit blank source fields from `mapped_fields`
- preserve original source ordering in `column_num`, including gaps caused by omitted blanks
- normalize headers to lowercase snake case
- use the official `metadata.pdf_url` as the canonical source link

## Normalization Conventions

Recurring identifiers and shared concepts are normalized where the source meaning is the same:

- `peims_id`
- `local_student_id`
- `tx_unique_student_id`
- `family_portal_unique_access_code`
- `emergent_bilingual_indicator_code`
- `gifted_and_talented_indicator_code`

Year-specific terminology is preserved when TEA changed the actual field meaning rather than just the label.

## Coverage

Current mapping coverage in the repo:

- `assessments/tea/staar/3_8`: `2012`-`2026`
- `assessments/tea/staar/eoc`: `2012`-`2026`
- `assessments/tea/staar/alt2_3_8`: `2016`-`2019`, `2021`-`2026`
- `assessments/tea/staar/alt2_eoc`: `2016`-`2019`, `2021`-`2026`
- `assessments/tea/staar/interim`: `2023`, `2024`, `2026`
- `assessments/tea/staar/consolidated_accountability`: `2014`-`2019`, `2021`-`2025`
- `assessments/tea/telpas/telpas`: `2012`-`2026`
- `assessments/tea/telpas/telpas_alt`: `2019`-`2026`
- `assessments/tea/tfar`: `2024`-`2025`
- `assessments/tea/ttap`: `2023`-`2025`
- `assessments/tea/crs`: `2023`-`2026`

Notes:

- school-year PDFs use the ending year as the mapping filename year
- some families intentionally skip years where no official PDF could be confirmed locally or online
- `assessments/tea/staar/interim` includes the separate `2022-2023` interim and BOY student-results layout under the `2023` mapping year

## Local Reference Documents

The [docs](./docs/) folder is the home for local project documentation and reference materials.

The TEA and Texas Assessments PDF archive currently lives under:

- [docs/tea-data-file-formats-archive](./docs/tea-data-file-formats-archive/)

Examples:

- [docs/tea-data-file-formats-archive/2024/2023-2024-staar-interim-data-file-format.pdf](./docs/tea-data-file-formats-archive/2024/2023-2024-staar-interim-data-file-format.pdf)
- [docs/tea-data-file-formats-archive/2025/2024-2025-crs-data-file-format.pdf](./docs/tea-data-file-formats-archive/2025/2024-2025-crs-data-file-format.pdf)
- [docs/tea-data-file-formats-archive/2026/2025-2026-file-naming-convention.pdf](./docs/tea-data-file-formats-archive/2026/2025-2026-file-naming-convention.pdf)

The local archive is for reference and maintenance. The official online TEA or Texas Assessments documentation remains the source of truth, and the local PDF copy should be kept up to date with that source. The official source URL for each mapping should remain in that file's `metadata.pdf_url`.

The docs area also includes human-readable working standards under:

- [docs/standards](./docs/standards/)
- [docs/overview](./docs/overview/)
- [docs/roadmap](./docs/roadmap/)
- [docs/adr](./docs/adr/)

## Working In This Repo

When adding or updating mappings:

1. Start with the current year's official online documentation as the source of truth, and make sure the local archived PDF matches it.
2. Check the relevant folder-level documentation before making changes.
3. Apply the established normalization rules only when the source meaning truly matches.
4. Validate that the JSON parses cleanly and that `column_header` values remain unique.

Most families include their own `README.md` files with family-specific exceptions, year gaps, and naming notes.

## Validation And Tooling

Repository-level scripts live under [scripts](./scripts/), with CI validation in [scripts/ci](./scripts/ci/), shared config in [configs](./configs/), and GitHub automation in [.github](./.github/).

Run the baseline checks locally with:

```powershell
python scripts/ci/validate_repo.py
```

The current baseline validates:

- mapping JSON structure and duplicate `column_header` values
- metadata and filename consistency
- lowercase snake case headers and basic numeric position sanity checks
- documentation for machine-specific absolute paths and broken repo-relative links

For repo-wide formatting and commit consistency, install the Node tooling once:

```powershell
npm install
```

Then use:

```powershell
npm run format
npm run lint
```

The Node tooling provides:

- `prettier` for consistent formatting of JSON, Markdown, and YAML
- `husky` plus `lint-staged` to format staged files before commit
- `commitlint` to enforce conventional commit messages through the `commit-msg` hook

After `npm install`, Husky will install the Git hooks automatically through the `prepare` script.

## Platform-Ready Structure

The repository is still mapping-first, but a few top-level areas are reserved so
future application work can land cleanly:

- [services](./services/)
- [packages](./packages/)
- [infra](./infra/)
