# <Family> Official Source Inventory

Create this record before opening year audit work units. Its purpose is to
establish which family years and layouts exist independently of what the
repository already contains. It is not a field-level source-row manifest.

## Inventory Metadata

- Family:
- Inventory date:
- Repository baseline:
- Prepared by:
- Independently reviewed by:
- Review date:

## Official Discovery Pages

Record every authoritative landing page used to discover layouts, including a
family-specific page when one exists. Do not rely only on URLs already stored
in mapping metadata.

| Official page | Retrieval date | Page version, update label, or archived evidence | Notes |
| ------------- | -------------- | ------------------------------------------------ | ----- |

## Published Layouts

List every family/year layout discovered on the official pages. Record
separate layouts when one reporting year has multiple delivered file families.

| Reporting year | Layout or file family | Official source URL | Published/update label | Repository mapping | Local archive | Disposition |
| -------------: | --------------------- | ------------------- | ---------------------- | ------------------ | ------------- | ----------- |

Allowed dispositions:

- `matched`: source, mapping, and archive are present;
- `mapping-required`: an official source exists without a mapping;
- `archive-required`: the mapping exists but its official source is not
  archived;
- `source-gap`: a repository mapping exists but no current official source can
  be located;
- `not-applicable`: evidence shows the published item is not a layout consumed
  by this repository; or
- `accepted-block`: completion is prevented by missing evidence and the block
  satisfies the audit exception rules.

For `not-applicable` and `accepted-block`, record the evidence, owner, approval,
and next review date. A blank disposition is not allowed.

## Reconciliation

- Official layout count:
- Repository mapping count:
- Local archive count:
- Years or layouts present only online:
- Years or layouts present only in the repository:
- Required work units or issues:

The preparer must compare the official-source set with the repository mapping
and archive sets in both directions. A source that lacks a mapping must become
a work unit before family closeout; it may not be omitted merely because it was
absent from the initial repository inventory.

## Independent Review

The independent reviewer must revisit the recorded discovery pages, confirm
that all displayed family years and layouts are listed, and check every set
difference and disposition. Reviewing counts alone is insufficient.

- [ ] Family-specific and central data-format pages were checked where
      available.
- [ ] Official links were enumerated without using repository mappings as the
      source list.
- [ ] Official, mapping, and archive sets were compared in both directions.
- [ ] Every difference has an evidence-backed disposition.
- [ ] Every `mapping-required` item has a planned work unit or issue.
- [ ] No undispositioned difference remains.

## Sign-Off

- Prepared by:
- Independent reviewer:
- Program owner accepted:
- Related issue or pull request:
