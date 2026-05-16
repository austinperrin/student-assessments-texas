# Infra

This project does not currently ship runtime infrastructure or deployment stacks.

This folder exists as a placeholder for future shared infrastructure artifacts if the project later needs them, such as:

- scheduled validation jobs outside GitHub Actions
- storage or ingestion environment definitions
- deployment notes for companion tooling

Until then, infrastructure expectations for this project are intentionally minimal:

- local maintenance is script-driven
- validation is handled through `scripts/` and `.github/workflows/`
- canonical assessment mappings remain under `assessments/`
- assessment source PDFs remain local reference material under `docs/tea-data-file-formats-archive/`

## Related References

- [../README.md](../README.md)
  Project overview and top-level navigation.
- [../scripts/README.md](../scripts/README.md)
  Automation and validation entrypoints.
- [../.github/overview.md](../.github/overview.md)
  Current workflow automation baseline.
