# TELPAS Alternate Mapping Maintenance Guide

This folder contains year-specific fixed-width mapping files for TELPAS Alternate reporting student data files.

## Source of Truth

For each file:

- use the corresponding TEA PDF in `../../docs`
- keep `metadata.pdf_url` aligned to the official PDF URL
- build field definitions from that year's PDF layout

## File Naming

Use:

`YYYY-telpas-alt-fixed-width-mapping.json`

Example:

`2026-telpas-alt-fixed-width-mapping.json`

## Required JSON Structure

Each file contains:

- `metadata`
- `mapped_fields`

The `mapped_fields` entries use:

- `start_pos`
- `end_pos`
- `column_header`
- `column_num`

## Field Rules

- Store all values as strings.
- Omit blank fields.
- Keep `column_num` aligned to the source layout sequence, including omitted blank fields.
- Normalize field titles into lowercase snake case.
