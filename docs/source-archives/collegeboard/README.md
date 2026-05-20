# College Board Data File Formats Archive

This folder stores local College Board source-format reference material used to
curate and validate mapping files.

## Purpose

Add College Board data format files and product reference documents here as they
are downloaded and validated.

## Usage

- create delivery-family, assessment, and year directories as needed beneath
  this folder
- keep official source documents aligned to the current College Board product
  documentation
- reference these files using repo-relative links from the College Board mapping
  metadata and `README.md` documentation

## Structure

- prefer a product-first layout such as
- prefer a vendor-family plus delivery-family layout such as
  `docs/source-archives/collegeboard/sat_suite/k12_reporting/sat/2026/`
- use vendor-specific folder structure rather than mixing multiple delivery
  families at the top level
- keep SAT Suite materials together unless the official source clearly belongs
  to another top-level College Board family such as `ap/`, `pre_ap/`, or
  `accuplacer/`
- keep audience-specific delivery families separate when districts, schools,
  and higher-ed institutions receive different source documents
- update this README when a new College Board family or archive
  structure is added

## Current Status

Archived source documents currently include:

- SAT Suite K-12 electronic score report layouts for `2025-26` and `2024-25`
- SAT Suite higher-ed electronic score report layouts for `2025-26` and
  `2024-25`
- AP K-12 datafile layouts for `2026`, `2025`, and `2024`
- AP higher-ed student data record layouts for `2026` and `2025` in both TXT
  and CSV variants

Known gaps:

- older SAT Suite `2023-24` PDFs still appear in public search indexing, but
  College Board's current public `media/pdf`, `media/xlsx`, and sample-file
  URLs returned `404 Not Found` during checks on May 20, 2026
- the remaining likely official source for those retired SAT Suite files is the
  authenticated K-12 Reporting Portal or Higher Education Reporting Portal
- no public Pre-AP result-file layout documents have been archived yet
