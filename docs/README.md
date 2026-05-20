# Docs

This folder stores the human-facing documentation system for the project,
including standards, roadmap material, durable decisions, and the local archive
of source reference documents.

## Start Here

- [index.md](./index.md)
  Main documentation directory and navigation index.
- [overview/README.md](./overview/README.md)
  Project purpose, current scope, and long-term direction.
- [overview/repository-navigation.md](./overview/repository-navigation.md)
  Navigation guide for major project areas and their responsibilities.
- [overview/scripts-and-commands.md](./overview/scripts-and-commands.md)
  Script glossary and common command patterns.

## Documentation Areas

- [overview/](./overview/)
  Project intent, navigation, and operational reference docs.
- [standards/](./standards/)
  Human-readable standards for coding, commits, scripts, and ADR usage.
- [roadmap/](./roadmap/)
  Milestone-level project evolution and priority tracking.
- [adr/](./adr/)
  Architecture Decision Records and ADR usage guidance.
- [source-archives/](./source-archives/)
  Shared local source archives for vendor-specific reference documents.

## Archive Rules

Archive rules are vendor-specific, but should follow a common pattern:

- keep source files under the matching vendor subtree in `docs/source-archives/`
- preserve the source grouping that best explains the delivered result files
- prefer delivery-family or reporting-family folders when those are more stable
  than assessment branding alone
- keep current and historic source files together under the same durable family
  unless the emitting system itself changed

TEA PDFs are organized into year-based folders to mirror the way source
documents are grouped online.

Use the ending year when a PDF is labeled by school year.

Examples:

- `docs/source-archives/tea/2024/2023-2024-staar-interim-data-file-format.pdf`
- `docs/source-archives/tea/2025/2024-2025-crs-data-file-format.pdf`
- `docs/source-archives/tea/2026/2025-2026-file-naming-convention.pdf`

For single-year PDFs, use that same year as the folder name.

Examples:

- `docs/source-archives/tea/2018/2018-staar-eoc-data-file-format.pdf`
- `docs/source-archives/tea/2024/2024-tfar-data-file.pdf`

The authoritative source link for each mapping file should remain the
`metadata.pdf_url` value stored in the JSON. When a mapping file also defines
`filename_patterns`, each pattern's `references` array should point to the
naming-convention or layout sources that justify that regex.

## Related References

- [../README.md](../README.md)
  Project-level overview and working expectations.
- [../assessments/README.md](../assessments/README.md)
  Entry point for the canonical mapping corpus.
- [../scripts/README.md](../scripts/README.md)
  Automation and validation entrypoints used by the project.
