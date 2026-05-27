# i-Ready Assessments

This folder is the vendor-level home for i-Ready assessment mapping families
and related maintenance guidance.

## Purpose

Add i-Ready mapping folders here. For i-Ready, the first grouping below the
vendor should usually reflect the delivered export, reporting, or result family
that districts or schools actually receive.

Current public Curriculum Associates references indicate that the i-Ready
Assessment suite centers on:

- i-Ready Inform for Reading and Mathematics
- i-Ready Growth Monitoring
- district, school, class, student, and family reporting surfaces
- administrator-facing data exports described by the `FAQ: i-Ready Export Dictionary`

This scaffold combines two rules:

- keep the vendor root aligned with the repository ADR that reserves
  `assessments/iready/`
- wait to create deeper family folders until official source documents confirm
  the durable file-delivery boundary

## Current Status

This is an initial scaffold for i-Ready assessments. No i-Ready mappings have
been added yet.

Based on official public references reviewed on `2026-05-27`, the first likely
machine-readable mapping target is the export surface associated with
i-Ready Inform, which Curriculum Associates still describes publicly as
`i-Ready Inform (formerly i-Ready Diagnostic)` ahead of the broader
`2026-2027` naming transition.

Until the actual export dictionary or equivalent source file is archived, keep
the vendor scaffold lightweight and avoid guessing at deeper family names.

## Suggested Next Step

When official source files are collected, the first deeper scaffold will likely
be an export-oriented family beneath this vendor root rather than a generic
reporting folder.

## Related References

- [../README.md](../README.md)
  Top-level assessments corpus entrypoint.
- [../../docs/adr/0004-iready-vendor-structure.md](../../docs/adr/0004-iready-vendor-structure.md)
  Repository ADR for the i-Ready vendor root.
- [../../docs/source-archives/iready/](../../docs/source-archives/iready/)
  Local archive root for i-Ready source references.
