# TFAR Fixed-Width Mappings

This folder contains fixed-width mapping files for TFAR data files.

Available mappings:

- `2024-tfar-fixed-width-mapping.json`
- `2025-tfar-fixed-width-mapping.json`
- `2026-tfar-fixed-width-mapping.json`

## 2026 Source Notes

The 2026 layout changes Total Raw Score to a three-byte whole number at
positions 255-257. Subsequent fields shift two positions earlier, and the
record ends at position 2242.

The published table contains two internal inconsistencies near the beginning
of the record. It prints District ID as positions 12-17 with a length of five,
and prints the two 15-byte student-name fields with endpoints 48-52 and 53-77.
The mapping retains the printed District ID range and uses the uniquely
continuous 15-byte name ranges 48-62 and 63-77. An operational result sample
was not available to resolve the printed inconsistencies independently.

Blank fields from published layouts are intentionally omitted from `mapped_fields`, while `column_num` preserves the source layout sequence including those blanks.

Do not create duplicate `column_header` values. Normalize identifier fields as `peims_id`, `local_student_id`, and `tx_unique_student_id`.
