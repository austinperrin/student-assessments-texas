# STAAR EOC Fixed-Width Mappings

This folder contains year-specific fixed-width mapping files for STAAR End-of-Course reporting student data files.

Each JSON file is intended to represent one school year's published EOC data file layout from the Texas Education Agency.

## File Naming

Each file follows this pattern:

`YYYY-staar-eoc-fixed-width-mapping.json`

Examples:

- `2012-staar-eoc-fixed-width-mapping.json`
- `2026-staar-eoc-fixed-width-mapping.json`

## JSON Structure

Each mapping file contains:

- `metadata`
- `mapped_fields`

The `metadata` section includes:

- `author`
- `date_created`
- `file_name`
- `school_year`
- `administration_periods`
- `pdf_url`

The `mapped_fields` section contains the fixed-width column definitions:

- `start_pos`
- `end_pos`
- `column_header`
- `column_num`

## Blank Fields

Blank fields from the published TEA layouts are intentionally omitted from the JSON files.

Even though blank fields are not included as `mapped_fields`, the `column_num` values still respect their original position in the source layout.

Example:

- if TEA column `7` is blank, the JSON may go from `column_num` `6` to `column_num` `8`
- this is expected and preserves alignment with the original file layout

## Source of Truth

These mappings are curated against the corresponding PDF layout for each year in the [docs](../../docs) folder and the official TEA/Texas Assessments PDF URLs stored in each file's `metadata`. The `administration_periods` metadata should also be sourced from that same PDF's administration date legend.

The mappings should be maintained manually as layout changes are introduced for a given year.

## Notes

- Header names are normalized into lowercase snake case
- Field titles are based on the PDF field title, not the descriptive note text
- When a PDF title wraps across lines, the header is reconstructed from the field title only
