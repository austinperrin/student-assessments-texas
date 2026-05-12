# STAAR Alt 2 3-8 Fixed-Width Mappings

This folder is reserved for year-specific fixed-width mapping files for STAAR Alternate 2 grades 3-8 reporting student data files.

Each JSON file in this folder should represent one school year's published STAAR Alt 2 3-8 data file layout from the Texas Education Agency.

## Planned File Naming

Each file should follow this pattern:

`YYYY-staar-alt2-3-8-fixed-width-mapping.json`

Examples:

- `2016-staar-alt2-3-8-fixed-width-mapping.json`
- `2026-staar-alt2-3-8-fixed-width-mapping.json`

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

- The first confirmed official STAAR Alternate 2 grades 3-8 data file format currently supported in this folder is `2016`
- TEA materials indicate STAAR Alternate 2 existed in the `2014-2015` school year, but no `2015` grades 3-8 data file format PDF is currently present anywhere under `../../docs` or confirmed on the TEA archive page
- Header names should be normalized into lowercase snake case
- Blank fields from the published layout should be omitted from `mapped_fields`
- `column_num` should still preserve the original source column order
- Use normalized identifier names when applicable:
  - `peims_id`
  - `local_student_id`
  - `tx_unique_student_id`
- Use `family_portal_unique_access_code` as the normalized name for portal access code fields
- If subject naming varies by year, prefer stable subject namespaces such as `reading_language_arts` over shorter legacy variants
