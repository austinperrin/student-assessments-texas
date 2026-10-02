# TEA Audit Review Records

Store completed audit records by family and reporting year:

```text
reviews/
  <family>/
    README.md
    <year>.md
```

The family `README.md` is created from
[the family audit template](../family-audit-template.md). Each `<year>.md` is
created from [the year review template](../review-template.md).

Examples:

```text
reviews/
  staar-3-8/
    README.md
    2026.md
    2025.md
  telpas/
    README.md
    2026.md
```

A year branch adds or completes only its own `<year>.md` and associated
findings, then merges into the family integration branch. After all year pull
requests have merged there, the coordinator updates coverage and the family
`README.md` before the family pull request merges to `main`.

Do not create empty family directories in advance. Create each family folder
when its first year work unit or coordination record begins.
