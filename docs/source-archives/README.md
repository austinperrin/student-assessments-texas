# Source Archives

This folder is the shared local archive root for source reference material used
by the project.

## Purpose

Group vendor-specific source archives under a single directory so the docs root
does not grow unbounded as new assessment vendors and product families are
added.

## Current Subdirectories

- `tea/`
  TEA and Texas Assessments source document archives.
- `collegeboard/`
  College Board delivery-family and product-format archives.
- `nwea/`
  NWEA assessment-family and export-format archives.

## Usage

- add new vendor archives under `docs/source-archives/`
- keep vendor-specific layout docs under the matching subfolder
- prefer delivery-family or reporting-family subfolders when that structure
  best matches the emitted result files
- use repo-relative links to reference these source documents from mapping
  metadata and assessment `README.md` files

## Structure

- `tea/`
  uses a year-based archive layout under `docs/source-archives/tea/`
- `collegeboard/`
  should use delivery-family and year folders as needed, for example
  `docs/source-archives/collegeboard/sat_suite/k12_reporting/sat/2026/`
- `nwea/`
  should use assessment-family and delivery-format folders such as
  `docs/source-archives/nwea/map_growth/data_exports/`
- add new vendor folders under `docs/source-archives/` rather than creating
  archive directories directly under `docs/`
