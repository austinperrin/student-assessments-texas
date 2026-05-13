# TELPAS Alternate Mapping Maintenance Guide

## Purpose

This folder contains year-specific JSON mappings for TELPAS Alternate reporting student data files.

## Source of Truth

- the corresponding official online TEA documentation is the source of truth
- the local PDF should come from the matching year folder under `../../../../docs/tea-data-file-formats-archive/` and should match the current online source
- keep `metadata.pdf_url` aligned to the official source URL
- do not infer field names from neighboring JSON files unless the current year's PDF is genuinely unclear
- do not create local `tmp_*.txt`, extracted plain-text PDF dumps, or similar scratch files in the repo when reviewing PDFs

## File Naming

Use:

`YYYY-telpas-alt-fixed-width-mapping.json`

Examples:

- `2024-telpas-alt-fixed-width-mapping.json`
- `2026-telpas-alt-fixed-width-mapping.json`

## Required JSON Structure

Each file should contain:

- `metadata`
- `filename_patterns` when filename matching guidance is stored in the same file
- `mapped_fields`

Each `mapped_fields` entry should contain:

- `start_pos`
- `end_pos`
- `column_header`
- `column_num`

## Metadata Rules

- store metadata values as strings
- keep `author`, `date_created`, `file_name`, `school_year`, and `pdf_url` accurate
- preserve any family-specific metadata keys already established in this folder

## Filename Pattern Rules

- use `filename_patterns` only when the mapping file needs to document supported delivered filename formats
- store each `filename_patterns` entry as an object with `regex` and `references`
- keep `references` tied to the source documents that justify the pattern, such as the TEA naming convention PDF or the family layout PDF

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
- preserve TELPAS Alternate-specific scoring meaning exactly as described in the PDF

## Family-Specific Notes

- this family starts in `2019` in the current repo coverage
- use the ending year for school-year-labeled source PDFs when applicable

## Workflow For Existing Files

1. Open the JSON file in this folder.
2. Review the matching PDF from `../../../../docs/tea-data-file-formats-archive/<year>/`.
3. Confirm suspicious or wrapped fields directly against that PDF.
4. Remove note spillover or OCR artifacts from headers.
5. Keep `start_pos`, `end_pos`, and `column_num` aligned to the PDF.
6. Validate the final JSON.

## Workflow For Creating A New Year

1. Obtain the official TEA TELPAS Alternate online source for that year.
2. Save the PDF into the matching year folder under `../../../../docs/tea-data-file-formats-archive/`.
3. Create the new JSON file using the family naming pattern.
4. Add accurate `metadata` values.
5. Build `mapped_fields` directly from the PDF layout.
6. Validate the final JSON.

## Validation

Use PowerShell to confirm a file parses:

```powershell
Get-Content 'assessments/tea/telpas/telpas_alt/2026-telpas-alt-fixed-width-mapping.json' | ConvertFrom-Json | Out-Null
```

For all files in this family:

```powershell
Get-ChildItem assessments/tea/telpas/telpas_alt -Filter '*-telpas-alt-fixed-width-mapping.json' |
  ForEach-Object {
    Get-Content $_.FullName | ConvertFrom-Json | Out-Null
  }
```

## Maintenance Principles

- prefer PDF accuracy over forced cross-year consistency
- keep headers readable and stable
- preserve year-specific terminology when the PDF clearly uses it
