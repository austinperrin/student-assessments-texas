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
- [tea-data-file-formats-archive/](./tea-data-file-formats-archive/)
  Local TEA and Texas Assessments PDF archive used to curate mappings.

## Archive Rules

PDFs in the TEA archive are organized into year-based folders to mirror the
way source documents are grouped online.

Use the ending year when a PDF is labeled by school year.

Examples:

- `docs/tea-data-file-formats-archive/2024/2023-2024-staar-interim-data-file-format.pdf`
- `docs/tea-data-file-formats-archive/2025/2024-2025-crs-data-file-format.pdf`
- `docs/tea-data-file-formats-archive/2026/2025-2026-file-naming-convention.pdf`

For single-year PDFs, use that same year as the folder name.

Examples:

- `docs/tea-data-file-formats-archive/2018/2018-staar-eoc-data-file-format.pdf`
- `docs/tea-data-file-formats-archive/2024/2024-tfar-data-file.pdf`

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
