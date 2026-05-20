# SAT Suite of Assessments

This folder stores mapping scaffolding and maintenance guidance for the
College Board SAT Suite of Assessments.

## Purpose

Use this family for current and historic materials tied to the integrated SAT
Suite product line, organized first by the delivery family that produces the
result files.

Current scaffolded delivery families include:

- `k12_reporting/`
  - `sat/`
  - `psat_nmsqt/`
  - `psat_10/`
  - `psat_8_9/`
- `higher_ed_reporting/`
  - `sat/`

Keep suite-level documents with this family even when a specific mapping lives
under one delivery family or child assessment.

## Current Status

This folder is a scaffold. Add mapping files once the relevant SAT Suite source
formats are confirmed and archived in the matching delivery-family archive under
`docs/source-archives/collegeboard/sat_suite/`.

## Working Notes

- College Board describes the SAT, PSAT/NMSQT, PSAT 10, and PSAT 8/9 as one SAT
  Suite of Assessments product line.
- Within that suite, keep separate delivery families when districts and higher
  education institutions receive different result files.
- PSAT/NMSQT and PSAT 10 are the same test offered in different
  administrations; do not create divergent mappings unless the source layout
  actually differs.
- Preserve historic source naming inside each year, but keep the folder
  placement under the correct SAT Suite delivery family unless the archived
  source clearly uses a different emitting system.

## Related References

- [../README.md](../README.md)
  College Board vendor overview.
- [../../../docs/source-archives/collegeboard/](../../../docs/source-archives/collegeboard/)
  College Board source archive.
