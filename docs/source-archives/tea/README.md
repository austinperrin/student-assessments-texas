# TEA Source Archive

This folder stores local TEA and Texas Assessments source-format reference
material used to curate and validate the JSON mappings.

## Purpose

Keep the TEA archive content in a shared vendor-specific subfolder under
`docs/source-archives/`.

## Usage

- keep PDF and source layout files organized by year under this folder
- reference matching source documents using repo-relative links from TEA
  `README.md` and mapping metadata
- preserve official TEA source URLs in metadata while keeping local copies in
  the archive

## Structure

- create one subfolder per source year under `docs/source-archives/tea/`
- use the ending year for school-year PDFs when that is the official naming
  convention
- keep local PDF file names stable and aligned with the current TEA source
  document semantics
