# TELPAS Mapping Maintenance Guide

The `assessments/tea/telpas/` directory groups TELPAS fixed-width mapping files by assessment family.

## Directory Structure

- `assessments/tea/telpas/telpas/` for TELPAS mapping files
- `assessments/tea/telpas/telpas_alt/` for TELPAS Alternate mapping files

Source layout PDFs remain in `../../../docs`.

## Naming Rules

- TELPAS: `YYYY-telpas-fixed-width-mapping.json`
- TELPAS Alternate: `YYYY-telpas-alt-fixed-width-mapping.json`

## Maintenance Principles

- Use the current year's official online documentation as the source of truth, and keep the local archived PDF aligned to it.
- Omit blank fields from `mapped_fields`.
- Preserve blank fields in the `column_num` sequence.
- Normalize field titles into lowercase snake case.
- Store fixed-width positions and column numbers as strings.
- Ensure `column_header` values are unique within each JSON file.
- Normalize identifier headers as `peims_id`, `local_student_id`, and `tx_unique_student_id`.
- Use `family_portal_unique_access_code` for Family Portal or Student Portal unique access code fields.
- Do not use legacy variants such as `student_portal_unique_access_code`, `tsds_id`, or raw `student_id` when the source field is one of the normalized identifiers above.
