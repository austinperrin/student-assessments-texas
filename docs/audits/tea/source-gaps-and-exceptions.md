# TEA Source Gaps And Exceptions

- Milestone: [M5 Program Verification](./roadmap/m5-cross-family-verification.md)
- Inventory date: 2026-10-09
- Program owner: Austin Perrin
- Reviewer 1: Codex
- Reviewer 2: pending independent confirmation

## Scope And Method

This record consolidates unresolved source limitations and accepted exceptions
after all 96 represented mapping years completed family review. It does not
reopen a year conclusion or use another year as evidence. Each entry below is
derived from the affected same-year review record and its closed family
integration record.

The review confirmed that all 11 family records preserve same-year source
isolation. Resolved historical URL changes and superseded URLs are not open
source gaps when a current official source was verified against the archive.

## Accepted Exception

| Family                           |                           Year | Affected layer                                     | Evidence gap and disposition                                                                                                                                                                                                                                                                                                        | Owner         | Recheck                                                                                               |
| -------------------------------- | -----------------------------: | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------- |
| [TFAR](./reviews/tfar/README.md) | [2024](./reviews/tfar/2024.md) | Numeric fixed-width positions, ranges, and lengths | The official PDF and byte-matching archive leave every Start, End, and Field Length cell blank. Positions 1-2158 and ordinals 1-45 are internally consistent but remain source-unverified. Austin Perrin accepted the exception on 2026-10-09; Reviewer 2 confirmed the exception without promoting the numeric values to verified. | Austin Perrin | 2027-10-09, or earlier if authoritative same-year evidence or an operational sample becomes available |

This is the program's only accepted block. It remains open as an evidence
exception, not as an unassigned correction.

## Current Official-Source Access Gaps

These mappings were fully reconciled against their same-year repository
archives. Their year conclusions are approved, but current official PDF bytes
could not be compared with the archived evidence.

| Family                                                                      | Years                                                                                                                                                  | Recorded limitation                                                                         | Disposition                                                                              |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [CRS Custom](./reviews/crs/README.md)                                       | [2023](./reviews/crs/2023.md)                                                                                                                          | Historical and attempted current-route URLs returned 404.                                   | Archive-based approval; monitor for a restored official source.                          |
| [CRS Custom](./reviews/crs/README.md)                                       | [2024](./reviews/crs/2024.md)                                                                                                                          | TEA's index identified the same-year source, but direct PDF-byte retrieval was unavailable. | Approved from indexed same-year identity plus archive; byte identity remains unverified. |
| [STAAR consolidated accountability](./reviews/staar-consolidated/README.md) | [2018](./reviews/staar-consolidated/2018.md)                                                                                                           | Historical and attempted current-route URLs returned 404; no replacement was verified.      | Archive-based approval; monitor for a restored official source.                          |
| [STAAR interim](./reviews/staar-interim/README.md)                          | [2023](./reviews/staar-interim/2023.md), [2024](./reviews/staar-interim/2024.md)                                                                       | Recorded official URLs returned 404.                                                        | Archive-based approvals; monitor for restored official sources.                          |
| [TELPAS](./reviews/telpas/README.md)                                        | [2012](./reviews/telpas/2012.md), [2020](./reviews/telpas/2020.md), [2022](./reviews/telpas/2022.md), [2024](./reviews/telpas/2024.md)                 | Recorded official URLs returned error/404 responses and no verified replacement was found.  | Archive-based approvals; monitor for restored official sources.                          |
| [TELPAS Alternate](./reviews/telpas-alt/README.md)                          | [2019](./reviews/telpas-alt/2019.md), [2023](./reviews/telpas-alt/2023.md), [2025](./reviews/telpas-alt/2025.md), [2026](./reviews/telpas-alt/2026.md) | Recorded official URLs returned 404 or other not-found content.                             | Archive-based approvals; monitor for restored official sources.                          |
| [TTAP](./reviews/ttap/README.md)                                            | [2023](./reviews/ttap/2023.md), [2024](./reviews/ttap/2024.md)                                                                                         | Recorded official URLs returned an error page or 404.                                       | Archive-based approvals; monitor for restored official sources.                          |

Austin Perrin owns the source-monitoring disposition. These access gaps do not
invalidate the completed same-year archive reconciliations. They should be
rechecked when TEA republishes a source, when an archive changes, or during the
next scheduled program review.

## Reconciled Source-URL History

Historical URLs that returned 404 during a review are not listed as current
gaps when the year record also documents a working replacement and a matching
official/archive comparison. For example, the [2018 TELPAS
record](./reviews/telpas/2018.md) documents a superseded historical route and a
verified current source. Those cases are resolved provenance history, not open
exceptions.

The TELPAS family summary groups 2018 with years having “unavailable current
online sources or other online/archive comparison limitations.” The year record
is more specific and establishes a working current source with matching bytes;
therefore 2018 is excluded from the open-gap table above.

## Program-Wide Operational Evidence Limitation

No family had an operational delivered-file sample available during its audit.
Consequently, delivered basename behavior, real-record parsing, value-level
behavior, and affected-record counts remain unverified where applicable. This
is a program-wide evidence limitation, not a source-layout defect or accepted
block.

Filename evidence also varies by year. Where a layout did not establish a
delivered basename, reviewers either omitted filename patterns or retained
inherited patterns only as explicitly provenance-limited compatibility
metadata. No family record treats an unsupported basename as verified.

Austin Perrin owns follow-up if an operational sample becomes available.
Operational validation and any resulting reprocessing decision belong in
[M6 Remediation Plan And Closeout](./roadmap/m6-remediation-plan-and-closeout.md).

## Phase 1 Reconciliation Result

- All 96 represented year conclusions remain tied to their own same-year
  sources; no cross-year or cross-family source substitution was identified.
- Missing or inaccessible official sources are explicitly assigned above and
  do not conceal a pending mapping correction.
- Superseded URL cases with verified replacements are resolved provenance
  history and are not counted as open gaps.
- TFAR 2024 is the only program-owner-accepted source exception and retains a
  named owner and recheck date.
- Operational samples and delivered-basename evidence remain documented
  limitations with program-owner follow-up if new evidence appears.

Reviewer 1 considers the Phase 1 exit satisfied. Independent Reviewer 2
confirmation is required before this record and the milestone phase are closed.

## Reviewer 2 Checklist

- [ ] Confirm that the TFAR 2024 exception scope, owner, acceptance date, and
      recheck date agree with the year and family records.
- [ ] Confirm every year in the official-source access table is supported by
      its linked same-year record.
- [ ] Confirm resolved or superseded URL history is not mislabeled as an open
      source gap.
- [ ] Confirm the operational-sample and filename limitations agree with all 11
      family integration records.
- [ ] Confirm this inventory changes no mapping conclusion and introduces no
      cross-year evidence.
- [ ] Confirm repository validation passes on the current pull-request head.
