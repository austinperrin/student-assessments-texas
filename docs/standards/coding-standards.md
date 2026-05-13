# Coding Standards

This repository is mostly a mapping and documentation repository rather than an application codebase, so the standards here focus on data accuracy, maintainability, and low-noise collaboration.

## Core Principles

- prefer source accuracy over cross-year uniformity
- preserve meaningful year-specific differences when the PDF meaning changes
- keep naming readable, stable, and intentionally normalized
- avoid adding clutter to the repository while working

## Mapping File Standards

- keep the top-level JSON shape consistent: `metadata` plus `mapped_fields`, with optional `filename_patterns`
- store mapping values as strings
- omit blank source fields from `mapped_fields`
- preserve source ordering in `column_num`, including gaps caused by omitted blanks
- use lowercase snake case for `column_header`
- do not allow duplicate `column_header` values in a file
- remove note spillover, wrapped-title spillover, and OCR debris from field names
- when `filename_patterns` is present, each entry should contain a `regex` string plus a `references` array of source-truth strings

## Normalization Standards

Use the established shared normalized names when the source meaning matches:

- `peims_id`
- `local_student_id`
- `tx_unique_student_id`
- `family_portal_unique_access_code`
- `emergent_bilingual_indicator_code`
- `gifted_and_talented_indicator_code`

Do not normalize fields across years when TEA changed the field concept rather than just the wording.

## Documentation Standards

- use repo-relative links in tracked documentation
- keep documentation portable across users and environments
- prefer concise explanations with examples when needed
- keep human-facing docs focused on how the repo works, not on internal scratch process

## Working Standards

- use the current-year official online documentation as the source of truth, and keep the local PDF archive aligned to it
- do not infer changes from neighboring years unless the current PDF is unclear
- do not create local `tmp_*.txt` or similar extracted scratch files in the repo when reviewing PDFs
- validate changes after editing, especially when touching multiple mapping files or shared docs

## Tooling Standards

- use the shared scripts in `scripts/`, especially `scripts/ci/` for repo-wide checks
- keep shared rules and contracts in `configs/`
- prefer small, reviewable repo scaffolding over heavyweight tooling that does not fit the project
- use ADRs for structural or long-term platform decisions rather than burying them in commits alone
