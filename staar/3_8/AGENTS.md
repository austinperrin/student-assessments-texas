# STAAR 3-8 Mapping Maintenance Guide

This file documents how to maintain the STAAR grades 3-8 fixed-width mapping files in this folder and how to create new ones in future years.

## Purpose

The files in this folder are year-specific JSON mappings for STAAR grades 3-8 reporting student data files published by the Texas Education Agency.

## Source of Truth

For each file:

- the corresponding TEA PDF is the source of truth
- the local PDF in the appropriate year-based subfolder under `../../docs` should match the `pdf_url` stored in the JSON `metadata`
- do not infer field names from neighboring JSON files unless the current year's PDF is unclear

When updating a file, review the current year's PDF only.

## File Naming

Each file should follow:

`YYYY-staar-3-8-fixed-width-mapping.json`

Examples:

- `2026-staar-3-8-fixed-width-mapping.json`
- `2027-staar-3-8-fixed-width-mapping.json`

## Required JSON Structure

Each file should contain:

```json
{
  "metadata": [
    {
      "author": "Austin Perrin",
      "date_created": "2026-05-05",
      "file_name": "2026-staar-3-8-fixed-width-mapping.json",
      "school_year": "2025-2026",
      "administration_periods": [],
      "pdf_url": "https://tea.texas.gov/"
    }
  ],
  "mapped_fields": [
    {
      "start_pos": "1",
      "end_pos": "4",
      "column_header": "administration_date",
      "column_num": "1"
    }
  ]
}
```

## Metadata Rules

- `author`: the maintainer name
- `date_created`: ISO format `YYYY-MM-DD`
- `file_name`: exact JSON filename
- `school_year`: format `YYYY-YYYY`
- `administration_periods`: array of `{ "code", "label" }` objects sourced from the PDF's administration date legend when applicable
- `pdf_url`: official TEA/Texas Assessments URL for that file's PDF

## Field Mapping Rules

- Store all values as strings
- Omit blank fields from `mapped_fields`
- Preserve original TEA column order in `column_num`
- Normalize `column_header` values into lowercase snake case

## Normalization Rules

- Normalize student identifier fields to:
  - `peims_id`
  - `local_student_id`
  - `tx_unique_student_id`
- Normalize portal access code fields to `family_portal_unique_access_code`
- Use `reading_language_arts` as the canonical subject namespace for grades 3-8 reading / RLA fields, even when older PDFs say `reading`
- Use `previous_year_reading_language_arts_*` for previous-year RLA history fields
- Keep descriptive phrase fields as written when `reading` is part of the label rather than the subject namespace
  - Example: `approaches_grade_level_in_reading`
- Do not normalize distinct program concepts into one field name when TEA changed the meaning
  - Examples: `lep_indicator_code` vs `emergent_bilingual_indicator_code`
  - Examples: `spell_check_*` vs `spelling_assistance_*`

## Workflow For Creating A New Year

1. Obtain the official TEA STAAR 3-8 PDF for that school year.
2. Save the PDF into the appropriate year-based subfolder under `../../docs`.
3. Create the new file using the naming pattern:
   `YYYY-staar-3-8-fixed-width-mapping.json`
4. Add the `metadata` block with the correct file name, school year, PDF URL, and current date.
5. Build `mapped_fields` from the PDF layout.
6. Validate that the final JSON parses correctly.

## Validation

After any update, confirm the file parses as valid JSON.

```powershell
Get-Content 'staar/3_8/2026-staar-3-8-fixed-width-mapping.json' | ConvertFrom-Json | Out-Null
```

For all STAAR 3-8 files:

```powershell
Get-ChildItem staar/3_8 -Filter '*-staar-3-8-fixed-width-mapping.json' |
  ForEach-Object {
    Get-Content $_.FullName | ConvertFrom-Json | Out-Null
  }
```
