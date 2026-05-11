# TTAP Fixed-Width Mappings

This folder contains fixed-width mapping files for Texas Through-year Assessment Pilot data files.

Files in this folder use the ending school year as the filename year.
For example, the `2022-2023` PDF maps to `2023-ttap-fixed-width-mapping.json`, and the `2023-2024` PDF maps to `2024-ttap-fixed-width-mapping.json`.

Blank fields from published layouts are intentionally omitted from `mapped_fields`, while `column_num` preserves the source layout sequence including those blanks.

Do not create duplicate `column_header` values. Normalize identifier fields as `peims_id`, `local_student_id`, and `tx_unique_student_id`.
