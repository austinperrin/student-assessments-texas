# STAAR Consolidated Accountability Mapping Maintenance Guide

This file documents how to maintain the STAAR consolidated accountability fixed-width mapping files in this folder and how to create new ones in future years.

## Purpose

The files in this folder are year-specific JSON mappings for STAAR consolidated accountability data files published by the Texas Education Agency.

## Source of Truth

For each file:

- the corresponding TEA PDF is the source of truth
- the local PDF in `../../docs` should match the `pdf_url` stored in the JSON `metadata`
- do not infer field names from neighboring JSON files unless the current year's PDF is unclear

When updating a file, review the current year's PDF only.

## File Naming

Each file should follow:

`YYYY-staar-consolidated-accountability-fixed-width-mapping.json`

Examples:

- `2014-staar-consolidated-accountability-fixed-width-mapping.json`
- `2022-staar-consolidated-accountability-fixed-width-mapping.json`

## Required JSON Structure

Each file should contain:

```json
{
  "metadata": [
    {
      "author": "Austin Perrin",
      "date_created": "2026-05-10",
      "file_name": "2014-staar-consolidated-accountability-fixed-width-mapping.json",
      "school_year": "2013-2014",
      "administration_periods": [],
      "pdf_url": "https://tea.texas.gov/"
    }
  ],
  "mapped_fields": [
    {
      "start_pos": "1",
      "end_pos": "4",
      "column_header": "year",
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
- `administration_periods`: use an empty array unless the PDF provides explicit administration-period codes that belong in metadata rather than field content
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
- Preserve distinct assessment-program sections when the PDF combines multiple programs into one record
- Do not collapse fields that have meaningfully different TEA definitions across years unless the schema decision is explicit and documented

## Workflow For Creating A New Year

1. Obtain the official TEA STAAR consolidated accountability PDF for that school year.
2. Save the PDF into `../../docs`.
3. Create the new file using the naming pattern:
   `YYYY-staar-consolidated-accountability-fixed-width-mapping.json`
4. Add the `metadata` block with the correct file name, school year, PDF URL, and current date.
5. Build `mapped_fields` from the PDF layout.
6. Validate that the final JSON parses correctly.

## Validation

After any update, confirm the file parses as valid JSON.

```powershell
Get-Content 'staar/consolidated_accountability/2014-staar-consolidated-accountability-fixed-width-mapping.json' | ConvertFrom-Json | Out-Null
```
