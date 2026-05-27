# i-Ready Assessments AI Agent Guide

This file guides AI agents working inside `assessments/iready/`.

## Scope

Use this area for mapping and maintenance assets tied to i-Ready assessment
products and delivered data formats.

Current publicly visible i-Ready assessment surfaces include:

- i-Ready Inform for Reading and Mathematics
- i-Ready Growth Monitoring
- administrator-facing exports referenced by Curriculum Associates as the
  `FAQ: i-Ready Export Dictionary`

## Working Rules

- keep this vendor grouping separate from `assessments/tea/`,
  `assessments/collegeboard/`, and `assessments/nwea/`
- add delivery-family or export-family folders under `assessments/iready/`
  only after official source documents confirm the file boundary
- prefer delivered export families over human-facing report names when the
  repository is modeling machine-readable layouts
- treat the public `i-Ready Inform` and `i-Ready Diagnostic` naming as the
  same active assessment line during the `2026-2027` rename transition unless
  source files show a real file-family split
- keep vendor-specific workflow assumptions in this folder and any later
  family-level docs
- update nearby docs in `docs/` when the vendor grouping or archive structure
  changes

## Agent Expectations

- create a `README.md` for each i-Ready delivery family before adding mapping
  files
- preserve source-document accuracy and official Curriculum Associates links in
  metadata and docs
- avoid inventing field families from screenshots, marketing copy, or secondary
  summaries when the export dictionary has not been captured
- link archive files using repo-relative paths in `docs/source-archives/iready/`
