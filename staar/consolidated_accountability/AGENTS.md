# STAAR Consolidated Accountability Mapping Maintenance Guide

## Purpose

This folder contains year-specific JSON mappings for STAAR consolidated accountability data files published by the Texas Education Agency.

## Source of Truth

- the corresponding TEA PDF is the source of truth
- the local PDF should come from the matching year folder under `../../docs/tea-data-file-formats-archive/`
- keep `metadata.pdf_url` aligned to the official source URL
- do not infer field names from neighboring JSON files unless the current year's PDF is genuinely unclear
- do not create local `tmp_*.txt`, extracted plain-text PDF dumps, or similar scratch files in the repo when reviewing PDFs

## File Naming

Use:

`YYYY-staar-consolidated-accountability-fixed-width-mapping.json`

Examples:

- `2014-staar-consolidated-accountability-fixed-width-mapping.json`
- `2025-staar-consolidated-accountability-fixed-width-mapping.json`

## Required JSON Structure

Each file should contain:

- `metadata`
- `mapped_fields`

Each `mapped_fields` entry should contain:

- `start_pos`
- `end_pos`
- `column_header`
- `column_num`

## Metadata Rules

- store metadata values as strings unless the family already uses a structured array such as `administration_periods`
- keep `author`, `date_created`, `file_name`, `school_year`, and `pdf_url` accurate
- use an empty `administration_periods` array unless a future PDF clearly requires metadata-level administration values

## Field Mapping Rules

- store mapping values as strings
- omit blank source fields from `mapped_fields`
- preserve source ordering in `column_num`, including gaps caused by omitted blanks
- normalize `column_header` values to lowercase snake case
- remove note spillover, wrapped-title spillover, and OCR debris from field names
- do not allow duplicate `column_header` values

## Normalization Rules

- normalize identifier fields to `peims_id`, `local_student_id`, and `tx_unique_student_id`
- normalize portal access code fields to `family_portal_unique_access_code`
- preserve distinct assessment-program sections when the PDF combines multiple programs into one record
- do not collapse meaningfully different TEA definitions unless the schema choice is explicit

## Family-Specific Notes

- `2020` is intentionally absent because no official consolidated accountability PDF was confirmed for that year
- `2025` is the current confirmed endpoint in this repo unless a later official PDF is posted
- this family often combines multiple assessment programs into one record, so preserve section boundaries carefully

## Workflow For Existing Files

1. Open the JSON file in this folder.
2. Review the matching PDF from `../../docs/tea-data-file-formats-archive/<year>/`.
3. Confirm suspicious or wrapped fields directly against that PDF.
4. Remove note spillover or OCR artifacts from headers.
5. Keep `start_pos`, `end_pos`, and `column_num` aligned to the PDF.
6. Validate the final JSON.

## Workflow For Creating A New Year

1. Obtain the official TEA consolidated accountability PDF for that year.
2. Save the PDF into the matching year folder under `../../docs/tea-data-file-formats-archive/`.
3. Create the new JSON file using the family naming pattern.
4. Add accurate `metadata` values.
5. Build `mapped_fields` directly from the PDF layout.
6. Validate the final JSON.

## Validation

Use PowerShell to confirm a file parses:

```powershell
Get-Content 'staar/consolidated_accountability/2025-staar-consolidated-accountability-fixed-width-mapping.json' | ConvertFrom-Json | Out-Null
```

For all files in this family:

```powershell
Get-ChildItem staar/consolidated_accountability -Filter '*-staar-consolidated-accountability-fixed-width-mapping.json' |
  ForEach-Object {
    Get-Content $_.FullName | ConvertFrom-Json | Out-Null
  }
```

## Maintenance Principles

- prefer PDF accuracy over forced cross-year consistency
- keep headers readable and stable
- preserve year-specific terminology when the PDF clearly uses it
