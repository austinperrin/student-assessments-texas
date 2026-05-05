# EOC Mapping Maintenance Guide

This file documents how to maintain the STAAR EOC fixed-width mapping files in this folder and how to create new ones in future years.

## Purpose

The files in this folder are year-specific JSON mappings for STAAR End-of-Course reporting student data files published by the Texas Education Agency.

These mappings are intended to be maintained manually against the source PDF for each year.

## Source of Truth

For each file:

- the corresponding TEA PDF is the source of truth
- the local PDF in `../../docs` should match the `pdf_url` stored in the JSON `metadata`
- do not infer field names from neighboring JSON files unless the current year's PDF is unclear

When updating a file, review the current year's PDF only.

## File Naming

Each file must follow:

`YYYY-staar-eoc-fixed-width-mapping.json`

Examples:

- `2026-staar-eoc-fixed-width-mapping.json`
- `2027-staar-eoc-fixed-width-mapping.json`

## Required JSON Structure

Each file must contain:

```json
{
  "metadata": [
    {
      "author": "Austin Perrin",
      "date_created": "2026-05-04",
      "file_name": "2026-staar-eoc-fixed-width-mapping.json",
      "school_year": "2025-2026",
      "administration_periods": [
        { "code": "1325", "label": "Fall 2025" },
        { "code": "1526", "label": "Spring 2026" },
        { "code": "1626", "label": "Summer 2026" }
      ],
      "pdf_url": "https://tea.texas.gov/student-assessment/student-assessment-results/2026-eoc-data-file-layout.pdf"
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
- `administration_periods`: array of `{ "code", "label" }` objects sourced from the PDF's administration date legend
- `pdf_url`: official TEA/Texas Assessments URL for that file's PDF

Examples:

- `2026` file -> `school_year: "2025-2026"`
- `2026` file -> `administration_periods: [{ "code": "1325", "label": "Fall 2025" }, { "code": "1526", "label": "Spring 2026" }, { "code": "1626", "label": "Summer 2026" }]`
- `2025` file -> `school_year: "2024-2025"`
- `2012` file -> `school_year: "2011-2012"`

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

Example:

- if TEA column `13` is blank, the JSON may contain `12` and then `14`

## Header Naming Rules

Use these rules for `column_header`:

- use lowercase snake case
- base the name on the PDF field title only
- do not pull descriptive note text into the header
- remove punctuation unless it is needed for clarity in words
- use readable semantic names rather than OCR fragments

Good examples:

- `administration_date`
- `family_portal_unique_access_code`
- `biology_reporting_category_1_raw_score`
- `ttt_tester_english_ii_reading_raw_score`

Avoid:

- OCR fragments
- note spillover
- wrapped-title spillover
- placeholder text like `blank`

## Common Cleanup Patterns

Watch for these common PDF extraction problems:

- note text leaking into the header
- wrapped field titles being cut off
- line-break artifacts from hyphenated or wrapped words
- repeated fragments from OCR-like extraction

Examples of problems to fix:

- `..._raw` should often be `..._raw_score`
- `..._at_the` usually means the rest of the title wrapped onto the next line
- long note text such as score ranges should not appear in `column_header`
- `T/T/T Tester` fields should be represented as `ttt_tester_*`

## Review Workflow For Existing Files

When maintaining an existing year:

1. Open the JSON file in this folder.
2. Open the corresponding PDF in `../../docs`.
3. Review the PDF field title for each suspicious or wrapped field.
4. Confirm that `column_header` reflects the field title only.
5. Remove any note spillover.
6. Keep `start_pos`, `end_pos`, and `column_num` aligned to the PDF.
7. Validate that the file still parses as JSON.

Do not rename fields only to match nearby years if the current year's PDF uses different terminology.

## Workflow For Creating A New Year

When adding a new year, follow this process:

1. Obtain the official TEA EOC PDF for that school year.
2. Save the PDF into `../../docs`.
3. Create the new file using the naming pattern:
   `YYYY-staar-eoc-fixed-width-mapping.json`
4. Add the `metadata` block with:
   - correct `file_name`
   - correct `school_year`
   - official `pdf_url`
   - current `date_created`
5. Build `mapped_fields` from the PDF layout.
6. Omit blank fields from the JSON.
7. Preserve blank positions in `column_num`.
8. Normalize headers into lowercase snake case.
9. Review every wrapped title for note spillover.
10. Validate the final JSON.

## Validation

After any update, confirm the file parses as valid JSON.

A PowerShell check:

```powershell
Get-Content 'staar/eoc/2026-staar-eoc-fixed-width-mapping.json' | ConvertFrom-Json | Out-Null
```

For all EOC files:

```powershell
Get-ChildItem staar/eoc -Filter '*-staar-eoc-fixed-width-mapping.json' |
  ForEach-Object {
    Get-Content $_.FullName | ConvertFrom-Json | Out-Null
  }
```

## Maintenance Principles

- Prefer accuracy to forced cross-year consistency
- Keep headers readable and stable
- Preserve year-specific terminology when the PDF clearly uses it
- Use the current year's PDF as the final authority
- Use the current year's PDF as the final authority for `administration_periods` values as well
- Treat omitted blanks as structural positions, not deletions from the source layout
