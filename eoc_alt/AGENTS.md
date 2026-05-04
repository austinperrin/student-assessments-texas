# EOC Alt 2 Mapping Maintenance Guide

This file documents how to maintain the STAAR Alternate 2 EOC fixed-width mapping files in this folder and how to create new ones in future years.

## Purpose

The files in this folder are year-specific JSON mappings for STAAR Alternate 2 End-of-Course reporting student data files published by the Texas Education Agency.

These mappings are intended to be maintained manually against the source PDF for each year.

## Source of Truth

For each file:

- the corresponding TEA PDF is the source of truth
- the local PDF in `../docs` should match the `pdf_url` stored in the JSON `metadata`
- do not infer field names from neighboring JSON files unless the current year's PDF is unclear

When updating a file, review the current year's PDF only.

## File Naming

Each file must follow:

`YYYY-staar-alt2-eoc-fixed-width-mapping.json`

Examples:

- `2026-staar-alt2-eoc-fixed-width-mapping.json`
- `2027-staar-alt2-eoc-fixed-width-mapping.json`

## Required JSON Structure

Each file must contain:

```json
{
  "metadata": [
    {
      "author": "Austin Perrin",
      "date_created": "2026-05-04",
      "file_name": "2026-staar-alt2-eoc-fixed-width-mapping.json",
      "school_year": "2025-2026",
      "pdf_url": "https://tea.texas.gov/student-assessment/student-assessment-results/2025-2026-staar-alt2-eoc-data-file-layout.pdf"
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

Use these rules when creating or updating `metadata`:

- `author`: the maintainer name
- `date_created`: ISO format `YYYY-MM-DD`
- `file_name`: exact JSON filename
- `school_year`: format `YYYY-YYYY`
- `pdf_url`: official TEA/Texas Assessments URL for that file's PDF

Examples:

- `2026` file -> `school_year: "2025-2026"`
- `2025` file -> `school_year: "2024-2025"`
- `2016` file -> `school_year: "2015-2016"`

## Field Mapping Rules

Each object in `mapped_fields` must include:

- `start_pos`
- `end_pos`
- `column_header`
- `column_num`

All values are stored as strings.

## Blank Field Rules

Blank fields from the TEA layout are intentionally omitted from `mapped_fields`.

Important:

- omitted blank fields still count when determining `column_num`
- `column_num` must preserve the original TEA column order
- gaps in `column_num` are expected when the omitted source field is blank

## Header Naming Rules

Use these rules for `column_header`:

- use lowercase snake case
- base the name on the PDF field title only
- do not pull descriptive note text into the header
- remove punctuation unless it is needed for clarity in words
- use readable semantic names instead of OCR fragments

Good examples:

- `administration_date`
- `student_portal_unique_access_code`
- `item_reporting_category_numbers`
- `item_student_responses`

## Common Cleanup Patterns

Watch for these common PDF extraction problems:

- note text leaking into the header
- wrapped field titles being cut off
- section headers being captured as fields
- blank ranges being turned into fake fields
- long answer-code descriptions being appended to `column_header`

Examples of problems to fix:

- long note text such as score ranges should not appear in `column_header`
- `..._00_99` and `..._0000_9999` should usually be trimmed back to the field title
- blank placeholder headers like `blank_*` should not remain in the final JSON
- `opportunity_key_alphanumeric_and` should be reduced to `opportunity_key`

## Review Workflow For Existing Files

When maintaining an existing year:

1. Open the JSON file in this folder.
2. Open the corresponding PDF in `../docs`.
3. Review suspicious or wrapped field titles directly in that PDF.
4. Confirm that `column_header` reflects the field title only.
5. Remove any note spillover.
6. Remove any section headers or blank blocks accidentally captured as fields.
7. Keep `start_pos`, `end_pos`, and `column_num` aligned to the PDF.
8. Validate that the file still parses as JSON.

Do not rename fields only to match nearby years if the current year's PDF uses different terminology.

## Workflow For Creating A New Year

When adding a new year, follow this process:

1. Obtain the official TEA STAAR Alternate 2 EOC PDF.
2. Save the PDF into `../docs`.
3. Create the new file using the naming pattern:
   `YYYY-staar-alt2-eoc-fixed-width-mapping.json`
4. Add the `metadata` block with:
   - correct `file_name`
   - correct `school_year`
   - official `pdf_url`
   - current `date_created`
5. Build `mapped_fields` from the PDF layout.
6. Omit blank fields from the JSON.
7. Preserve blank positions in `column_num`.
8. Normalize headers into lowercase snake case.
9. Review all wrapped titles for note spillover.
10. Validate the final JSON.

## Validation

After any update, confirm the file parses as valid JSON.

A PowerShell check:

```powershell
Get-Content 'eoc_alt/2026-staar-alt2-eoc-fixed-width-mapping.json' | ConvertFrom-Json | Out-Null
```

For all Alt 2 EOC files:

```powershell
Get-ChildItem eoc_alt -Filter '*-staar-alt2-eoc-fixed-width-mapping.json' |
  ForEach-Object {
    Get-Content $_.FullName | ConvertFrom-Json | Out-Null
  }
```

## Maintenance Principles

- Prefer accuracy to forced cross-year consistency
- Keep headers readable and stable
- Preserve year-specific terminology when the PDF clearly uses it
- Use the current year's PDF as the final authority
- Treat omitted blanks as structural positions, not deletions from the source layout
