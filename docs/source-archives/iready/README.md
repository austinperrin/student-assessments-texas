# i-Ready Source Archive

This folder stores local i-Ready source reference material used to curate and
validate mapping files.

## Purpose

Add official Curriculum Associates source documents here as they are
downloaded and validated.

## Usage

- create delivery-family, export-family, product, or year directories as needed
  beneath this folder only after the source boundary is confirmed
- keep official source documents aligned to current Curriculum Associates
  product and support documentation
- reference these files using repo-relative links from i-Ready mapping metadata
  and `README.md` documentation

## Current Public References

The following official public pages were reviewed on `2026-05-27` to guide the
initial scaffold:

- <https://www.curriculumassociates.com/programs/i-ready-assessment/admin-resources/diagnostic>
- <https://www.curriculumassociates.com/resources/guides/i-ready-reports-book>
- <https://www.curriculumassociates.com/programs/i-ready-assessment/growth-monitoring>
- <https://www.curriculumassociates.com/programs/i-ready-assessment/i-ready-inform-announcement>

Those pages show that:

- Curriculum Associates is renaming `i-Ready Diagnostic` to `i-Ready Inform`
  for the `2026-2027` school year
- public program pages reference administrator-facing exports through the
  `FAQ: i-Ready Export Dictionary`
- the export dictionary asset is publicly retrievable from the admin resources
  page, but deeper file-family boundaries still need to be confirmed from the
  archived source set

## Current Status

Archived on `2026-05-27`:

- `iready-faq-exports-dictionary-and-guide-with-projected-proficiency.pdf`
  Official export dictionary and related guide linked from the admin resources
  page.
- `iready-reports-book-2024.pdf`
  Public reports book PDF linked from the reports guide page.
- `iready-progress-monitoring.pdf`
  Public Growth Monitoring PDF linked from the Growth Monitoring page.

Keep the supporting product and guide pages as live web references in this
README instead of archiving HTML snapshots unless an offline copy becomes
necessary for maintenance.

## Known Gaps

- the current archive confirms source assets for export guidance, reports, and
  Growth Monitoring, but it does not yet prove the final durable folder split
  that should live under `assessments/iready/`
- if Curriculum Associates exposes additional authenticated export references,
  sample files, or year-versioned dictionaries, those should be added before
  creating year-specific mappings
