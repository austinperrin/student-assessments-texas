# TEA Audit Dispositions And Reprocessing Plan

- Milestone: [M6 Program Closeout](./roadmap/m6-remediation-plan-and-closeout.md)
- Disposition date: 2026-10-09
- Program owner: Austin Perrin
- Reviewer 1: Codex
- Reviewer 2: pending independent confirmation

## Scope

This record resolves the remaining program-level dispositions identified by
the [M5 program reconciliation](./program-reconciliation.md). It does not
change a mapping, reopen a year finding, or infer evidence from another year.
The 96 year records remain the authority for their individual corrections and
downstream-impact statements.

## Correction Completion

All confirmed mapping corrections were completed and independently verified in
their year work units. Coverage reports 96 of 96 represented years complete,
and no year has a corrected finding awaiting verification. No repository data
artifact or operational result file was modified during the audit.

The remaining work concerns consumer-owned derived data, unavailable
operational evidence, one accepted source exception, and documentation policy.

## Reprocessing Dispositions

| Class                                                                        | Decision                                                                                   | Scope and trigger                                                                                                                                                                                                                 | Owner         | Target                                                          |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------- |
| Repository mappings and source archives                                      | `unnecessary`                                                                              | Canonical corrections are already merged. The repository contains no parsed historical result dataset requiring regeneration.                                                                                                     | Austin Perrin | Complete, 2026-10-09                                            |
| Metadata, source URL, and filename-reference-only corrections                | `unnecessary` for record reprocessing                                                      | These corrections do not change fixed-width extraction. Consumers must refresh routing or provenance metadata only if they use the affected values.                                                                               | Austin Perrin | Before the next affected import                                 |
| Header-only corrections                                                      | `deferred` for derived schemas; raw re-ingestion generally unnecessary                     | Consumers using former output keys must rename, alias, or regenerate materialized schemas when adopting the corrected mappings. Re-ingest raw files only when their pipeline binds persisted columns directly to mapping headers. | Austin Perrin | Before the next affected schema release; review by 2027-10-09   |
| Restored named fields, removed mapped blanks, or corrected extraction ranges | `required` when an affected historical extract must contain the corrected fields or values | Reprocess from retained raw files before relying on affected historical extracts. The year record defines the exact affected fields and ranges.                                                                                   | Austin Perrin | Before the affected extract is used or republished              |
| Corrected source ordinals only                                               | `deferred` unless a consumer uses `column_num` as source metadata                          | Byte extraction remains unchanged. Regenerate metadata-dependent outputs if source ordinals are operationally consumed.                                                                                                           | Austin Perrin | Before the next ordinal-dependent release; review by 2027-10-09 |
| Operational behavior and affected-record counts                              | `unknown`                                                                                  | No operational samples or consumer inventory were available. Validate when a de-identified sample or downstream inventory becomes available.                                                                                      | Austin Perrin | Event-triggered; annual review by 2027-10-09                    |

Year records with explicit conditional or required historical reconciliation
include [STAAR consolidated accountability 2014](./reviews/staar-consolidated/2014.md),
[2017](./reviews/staar-consolidated/2017.md), and
[2024](./reviews/staar-consolidated/2024.md), plus
[TELPAS 2013](./reviews/telpas/2013.md). The STAAR grades 3-8 records retain
their per-finding deferred downstream decisions because no consumer inventory
or operational samples were available. Other year records preserve their own
header, ordinal, filename, and optional-reprocessing guidance.

This program plan does not claim that historical consumer datasets exist. A
`required` decision applies only when a consumer has an affected extract and
needs corrected content. The program owner must identify the consumer and raw
input before ordering reprocessing.

## Accepted Exception

| ID                            | Severity and impact                                   | State           | Owner         | Target and trigger                                                                                                | Disposition                                                                                                                                                                     |
| ----------------------------- | ----------------------------------------------------- | --------------- | ------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TFAR-2024-POSITIONAL-EVIDENCE | High evidence impact; operational data impact unknown | `accepted-risk` | Austin Perrin | Recheck by 2027-10-09, or earlier if authoritative same-year positional evidence or an operational sample appears | Retain positions 1-2158 and ordinals 1-45 as internally consistent but source-unverified. Do not represent the numeric positions, ranges, or lengths as independently verified. |

This is the only accepted source block. Its evidence and acceptance remain in
the [TFAR 2024 review record](./reviews/tfar/2024.md) and
[source-gap inventory](./source-gaps-and-exceptions.md).

## Legacy Finding-Identifier Decision

`TEA-M5-DOC-001` is resolved as `unnecessary` for the closed historical work.
The program will not invent identifiers or owner fields retroactively for
legacy findings whose year records already preserve their evidence,
correction, verification, and final disposition. Rewriting those records would
create artificial history without changing an audit conclusion.

New findings must follow the current [finding template](./finding-template.md)
and include a stable ID, severity, state, owner, evidence, disposition, and
verification. A generated legacy index may be added later only if a concrete
reporting or automation requirement justifies it.

## Residual Triggers

Open a new audit or remediation work unit when any of the following occurs:

- TEA republishes or revises an inaccessible official layout;
- authoritative TFAR 2024 positional evidence becomes available;
- an operational result-file sample becomes available;
- a downstream consumer identifies an affected historical extract;
- a source revision changes positions, meanings, codes, or filename evidence;
  or
- a concrete reporting requirement needs a normalized legacy finding index.

## Phase 1 Result

Every remaining disposition now has a decision, owner, and target or event
trigger. No confirmed mapping correction remains open. Reviewer 1 considers
the M6 Phase 1 exit satisfied, pending independent Reviewer 2 confirmation.

## Reviewer 2 Checklist

- [ ] Confirm all mapping corrections are complete and no year verification is
      pending.
- [ ] Confirm the reprocessing classes preserve the more specific decisions in
      the linked year records.
- [ ] Confirm repository reprocessing is unnecessary because no parsed
      historical result dataset is tracked here.
- [ ] Confirm downstream reprocessing remains conditional on an affected
      consumer, retained raw input, and the year-specific correction.
- [ ] Confirm the TFAR 2024 exception is the sole accepted block and retains its
      owner, limitation, and recheck date.
- [ ] Confirm the disposition of `TEA-M5-DOC-001` does not rewrite historical
      records and that future findings remain governed by the current template.
- [ ] Confirm every remaining action has an owner and date or event trigger.
- [ ] Confirm no mapping or JSON file changed and repository validation passes.
