# CRS Custom Fixed-Width Mappings

This folder is reserved for CRS Custom fixed-width mapping files.

The CRS Custom family is separate from the STAAR Interim family.
Use this folder for the official TEA `CRS Custom Data File Layout` / `CRS Data File Format` PDFs.

Current confirmed CRS Custom source years in `docs/tea-data-file-formats-archive/<year>/` are:

- `2023`
- `2024`
- `2025`
- `2026`

Use the ending school year as the filename year when the PDF is labeled by school year.
For example, `2024-2025-crs-data-file-format.pdf` should map to a `2025-...json` filename.

Do not treat `docs/tea-data-file-formats-archive/2023/2023-crs-layout-interim-boy.pdf` as part of this family.
That file is an Interim and Beginning of Year student-results layout and should be treated as interim-related reference material instead.

Each mapping file in this folder should follow the same structure used elsewhere in the repo:

- `metadata`
- `filename_patterns` when the file also documents supported delivered filename styles
- `mapped_fields`

Blank fields from the published layouts should be omitted from `mapped_fields`, while `column_num` should preserve the source layout order including omitted blanks.
When `filename_patterns` is present, each entry should include a `regex` string and a `references` array that ties the pattern back to source documentation.
