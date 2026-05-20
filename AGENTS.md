# AI Agent Guide

This file is the top-level working guide for AI agents operating in this
project.

## Scope

This project currently focuses on Texas student assessment mappings,
documentation, and maintenance tooling, with active work centered on TEA and
Texas Assessments fixed-width layouts.

The broader repository direction is to model vendor-delivered assessment result
files across time, including both current and historic layouts.

Primary active mapping families:

- `assessments/tea/staar/3_8`
- `assessments/tea/staar/eoc`
- `assessments/tea/staar/alt2_3_8`
- `assessments/tea/staar/alt2_eoc`
- `assessments/tea/staar/interim`
- `assessments/tea/staar/consolidated_accountability`
- `assessments/tea/telpas/telpas`
- `assessments/tea/telpas/telpas_alt`
- `assessments/tea/tfar`
- `assessments/tea/ttap`
- `assessments/tea/crs`

Use the nearest folder-level `AGENTS.md` before making changes inside a more
specific area.

## Agent Priorities

- preserve source-document accuracy over cross-year uniformity
- keep tracked docs portable with repo-relative links only
- keep human-facing `README.md` files scoped to human readers
- use `AGENTS.md` files for AI-agent-specific instructions, routing, and guardrails
- prefer focused, reviewable changes over broad speculative restructuring

## Source Material Rules

- the current official online TEA or Texas Assessments documentation is the
  governing reference for active TEA mappings
- local reference PDFs live under `docs/source-archives/tea/<year>/`
  and should stay aligned to the current online source
- `metadata.pdf_url` should remain aligned to the official source URL
- do not infer field names from neighboring years when the current source is
  clear
- do not create tracked scratch artifacts such as extracted PDF text dumps

## Shared Mapping Rules

- preserve the current TEA mapping JSON shape of `metadata` plus
  `mapped_fields`, with optional top-level `filename_patterns`
- store mapping values as strings
- omit blank source fields from `mapped_fields`
- preserve source ordering in `column_num`, including gaps caused by omitted
  blank fields
- use lowercase snake case for `column_header`
- remove note spillover, wrapped-title spillover, and OCR debris from field
  names
- do not allow duplicate `column_header` values in a file
- when `filename_patterns` is present, store it as an array of objects with
  `regex` and `references`

## Shared Normalization Rules

Normalize these identifiers and recurring concepts when the source meaning
matches:

- `peims_id`
- `local_student_id`
- `tx_unique_student_id`
- `family_portal_unique_access_code`
- `emergent_bilingual_indicator_code`
- `gifted_and_talented_indicator_code`

Do not normalize away real meaning changes when TEA changed the field concept
rather than just the label.

## Documentation Rules

- use repo-relative links in tracked documentation
- do not write machine-specific absolute paths into tracked docs
- keep human-facing docs aligned with the current project structure
- describe future vendor structures in terms of delivered file families when
  that is more durable than assessment branding alone
- keep AI-agent-specific instructions in `AGENTS.md`, not in `README.md`
- update nearby docs when folder structure, commands, or workflow expectations
  change

## Validation

After editing mappings, shared docs, or project structure:

1. confirm JSON files still parse cleanly
2. confirm `column_header` values remain unique where relevant
3. confirm docs still use valid repo-relative links
4. run `npm run lint` when the change touches tracked docs, shared structure, or
   multiple mappings

## Project Areas

- `assessments/`
  Canonical assessment mappings and area-specific maintenance guidance.
- `docs/`
  Human-facing project documentation and local reference archives.
- `scripts/`
  Validation, sorting, merging, and maintenance automation.
- `configs/`
  Shared schemas and validation contracts.
- `.github/`
  Workflow automation and contribution templates.
- `services/`, `packages/`, `infra/`
  Reserved for future implementation areas and should stay lightweight until
  concrete needs exist.
