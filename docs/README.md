# Docs

This folder stores local project documentation and reference material used to support the mapping files in this repository.

## Current Primary Archive

The TEA and Texas Assessments PDF archive is stored under:

- [tea-data-file-formats-archive](./tea-data-file-formats-archive/)

The official online TEA or Texas Assessments documentation remains the source of truth. The local archive is a synced working reference and should be kept current with the online source whenever a document changes.

## Standards

Shared human-readable standards live under:

- [standards](./standards/)

## Additional Documentation Areas

The docs folder also includes:

- [overview](./overview/)
- [roadmap](./roadmap/)
- [adr](./adr/)

## Archive Rules

PDFs in the TEA archive are organized into year-based subfolders to mirror the way the source documents are grouped online.

Use the ending year when a PDF is labeled by school year.

Examples:

- `docs/tea-data-file-formats-archive/2024/2023-2024-staar-interim-data-file-format.pdf`
- `docs/tea-data-file-formats-archive/2025/2024-2025-crs-data-file-format.pdf`
- `docs/tea-data-file-formats-archive/2026/2025-2026-file-naming-convention.pdf`

For single-year PDFs, use that same year as the folder name.

Examples:

- `docs/tea-data-file-formats-archive/2018/2018-staar-eoc-data-file-format.pdf`
- `docs/tea-data-file-formats-archive/2024/2024-tfar-data-file.pdf`

The authoritative source link for each mapping file should remain the `metadata.pdf_url` value stored in the JSON.
When a mapping file also defines `filename_patterns`, each pattern's `references` array should point to the naming-convention or layout sources that justify that regex.

See [index.md](./index.md) for a lightweight directory of what lives in this folder.
