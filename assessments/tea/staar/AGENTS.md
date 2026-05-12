# STAAR Mapping Maintenance Guide

This file documents how to work within the `assessments/tea/staar/` directory and how the STAAR mapping sets are organized.

## Purpose

The `assessments/tea/staar/` directory groups STAAR fixed-width mapping files by assessment family so related mappings can be maintained together under one parent folder.

## Directory Structure

The current structure is:

- `assessments/tea/staar/3_8/` for STAAR grades 3-8 mapping files
- `assessments/tea/staar/eoc/` for STAAR End-of-Course mapping files
- `assessments/tea/staar/alt2_3_8/` for STAAR Alternate 2 grades 3-8 mapping files
- `assessments/tea/staar/alt2_eoc/` for STAAR Alternate 2 End-of-Course mapping files
- `assessments/tea/staar/consolidated_accountability/` for STAAR consolidated accountability mapping files
- `assessments/tea/staar/interim/` for STAAR Interim mapping files

Each subdirectory contains its own:

- year-specific JSON mapping files
- `README.md`
- `AGENTS.md`

## Source PDFs

The source layout PDFs remain in `../../../docs`.

When maintaining a mapping in a STAAR subdirectory:

- use the PDF that matches that mapping's `pdf_url`
- follow the folder-specific maintenance guidance in that subdirectory's `AGENTS.md`
- keep metadata and field definitions aligned to the source PDF for that specific year

## Routing Rules

Use these rules when deciding where a file belongs:

- STAAR grades 3-8 files belong in `assessments/tea/staar/3_8/`
- STAAR EOC files belong in `assessments/tea/staar/eoc/`
- STAAR Alternate 2 grades 3-8 files belong in `assessments/tea/staar/alt2_3_8/`
- STAAR Alternate 2 EOC files belong in `assessments/tea/staar/alt2_eoc/`
- STAAR consolidated accountability files belong in `assessments/tea/staar/consolidated_accountability/`
- STAAR Interim files belong in `assessments/tea/staar/interim/`

Do not mix EOC and Alt 2 EOC mapping files in the same folder.

## Naming Rules

Keep the existing per-folder file naming conventions:

- `assessments/tea/staar/3_8/`: `YYYY-staar-3-8-fixed-width-mapping.json`
- `assessments/tea/staar/eoc/`: `YYYY-staar-eoc-fixed-width-mapping.json`
- `assessments/tea/staar/alt2_3_8/`: `YYYY-staar-alt2-3-8-fixed-width-mapping.json`
- `assessments/tea/staar/alt2_eoc/`: `YYYY-staar-alt2-eoc-fixed-width-mapping.json`
- `assessments/tea/staar/consolidated_accountability/`: `YYYY-staar-consolidated-accountability-fixed-width-mapping.json`
- `assessments/tea/staar/interim/`: `YYYY-staar-interim-fixed-width-mapping.json`

## Maintenance Principles

- Keep the `assessments/tea/staar/` folder focused on STAAR mappings only
- Preserve the separation between assessment families
- Prefer source-PDF accuracy over forced cross-folder consistency
- Update the folder-specific docs when a structural convention changes

## Header Consistency Checks

Before committing any mapping file:

- confirm every `column_header` is unique within that JSON file
- use `peims_id` for PEIMS ID fields
- use `local_student_id` for Local Student ID fields
- use `tx_unique_student_id` for TSDS ID, TSDS UID, TX Unique Student ID, or Texas Student Data System Unique Student ID fields
- use `family_portal_unique_access_code` for Family Portal or Student Portal unique access code fields when that field exists in the source layout
- do not use legacy variants such as `student_portal_unique_access_code`, `tsds_id`, or raw `student_id` when the source field is one of the normalized identifiers above
