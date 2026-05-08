# TFAR Mapping Maintenance Guide

This folder contains year-specific fixed-width mapping files for TFAR data files.

## Source of Truth

For each file:

- use the corresponding TEA PDF in `../docs`
- keep `metadata.pdf_url` aligned to the official PDF URL
- build field definitions from that year's PDF layout

## File Naming

Use:

`YYYY-tfar-fixed-width-mapping.json`

Example:

`2025-tfar-fixed-width-mapping.json`

## Field Rules

- Store all values as strings.
- Omit blank fields.
- Keep `column_num` aligned to the source layout sequence, including omitted blank fields.
- Normalize field titles into lowercase snake case.
