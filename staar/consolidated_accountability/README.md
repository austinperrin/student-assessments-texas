# STAAR Consolidated Accountability Fixed-Width Mappings

This folder is reserved for year-specific fixed-width mapping files for STAAR consolidated accountability data files.

Each JSON file in this folder should represent one school year's published STAAR consolidated accountability data file layout from the Texas Education Agency.

## Planned File Naming

Each file should follow this pattern:

`YYYY-staar-consolidated-accountability-fixed-width-mapping.json`

Examples:

- `2014-staar-consolidated-accountability-fixed-width-mapping.json`
- `2022-staar-consolidated-accountability-fixed-width-mapping.json`

## Expected JSON Structure

Each mapping file should contain:

- `metadata`
- `mapped_fields`

The `metadata` section is expected to include:

- `author`
- `date_created`
- `file_name`
- `school_year`
- `administration_periods`
- `pdf_url`

The `mapped_fields` section should contain the fixed-width column definitions:

- `start_pos`
- `end_pos`
- `column_header`
- `column_num`

## Source of Truth

Mappings in this folder should be curated against the corresponding PDF layout in the appropriate year-based subfolder under [docs](../../docs) and the official TEA/Texas Assessments PDF URL stored in each file's `metadata`.

## Notes

- Header names should be normalized into lowercase snake case
- Blank fields from the published layout should be omitted from `mapped_fields`
- `column_num` should still preserve the original source column order
- Use normalized identifier names when applicable:
  - `peims_id`
  - `local_student_id`
  - `tx_unique_student_id`
- Use `family_portal_unique_access_code` as the normalized name for portal access code fields
- Because these layouts merge multiple assessment programs into one record, preserve year-specific field groupings from the source PDF rather than forcing them into another STAAR family's schema
