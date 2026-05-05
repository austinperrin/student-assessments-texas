# STAAR Mapping Maintenance Guide

This file documents how to work within the `staar/` directory and how the STAAR mapping sets are organized.

## Purpose

The `staar/` directory groups STAAR fixed-width mapping files by assessment family so related mappings can be maintained together under one parent folder.

## Directory Structure

The current structure is:

- `staar/3_8/` for STAAR grades 3-8 mapping files
- `staar/eoc/` for STAAR End-of-Course mapping files
- `staar/alt2_3_8/` for STAAR Alternate 2 grades 3-8 mapping files
- `staar/alt2_eoc/` for STAAR Alternate 2 End-of-Course mapping files

Each subdirectory contains its own:

- year-specific JSON mapping files
- `README.md`
- `AGENTS.md`

## Source PDFs

The source layout PDFs remain in `../docs`.

When maintaining a mapping in a STAAR subdirectory:

- use the PDF that matches that mapping's `pdf_url`
- follow the folder-specific maintenance guidance in that subdirectory's `AGENTS.md`
- keep metadata and field definitions aligned to the source PDF for that specific year

## Routing Rules

Use these rules when deciding where a file belongs:

- STAAR grades 3-8 files belong in `staar/3_8/`
- STAAR EOC files belong in `staar/eoc/`
- STAAR Alternate 2 grades 3-8 files belong in `staar/alt2_3_8/`
- STAAR Alternate 2 EOC files belong in `staar/alt2_eoc/`

Do not mix EOC and Alt 2 EOC mapping files in the same folder.

## Naming Rules

Keep the existing per-folder file naming conventions:

- `staar/3_8/`: `YYYY-staar-3-8-fixed-width-mapping.json`
- `staar/eoc/`: `YYYY-staar-eoc-fixed-width-mapping.json`
- `staar/alt2_3_8/`: `YYYY-staar-alt2-3-8-fixed-width-mapping.json`
- `staar/alt2_eoc/`: `YYYY-staar-alt2-eoc-fixed-width-mapping.json`

## Maintenance Principles

- Keep the `staar/` folder focused on STAAR mappings only
- Preserve the separation between assessment families
- Prefer source-PDF accuracy over forced cross-folder consistency
- Update the folder-specific docs when a structural convention changes
