# TEA Audit Review Checklist

Use one review record and one pull request per family/year work unit. Check an
item only when its evidence is recorded.

## Family Scope Discovery

- [ ] Inventory the current official family page and central data-format pages
      without deriving the source list from repository mappings.
- [ ] Record discovery-page URLs, retrieval dates, update labels, every listed
      year/layout, and every direct source URL.
- [ ] Compare official layouts, repository mappings, and local archives in both
      directions.
- [ ] Record an evidence-backed disposition for every difference.
- [ ] Obtain independent review of the enumerated sources and differences.
- [ ] Create a work unit or issue for every official layout without a mapping.

## Assignment And Baseline

- [ ] Record two distinct reviewers and whether each is human or AI.
- [ ] Record repository commit, branch, scope, and review date.
- [ ] Identify the mapping, archived source, and official URL.
- [ ] Record source retrieval date and archive/online agreement.
- [ ] Record missing, inaccessible, superseded, or ambiguous sources.
- [ ] Confirm both reviewers will use only the assigned year's source as audit
      evidence.

## Reviewer 1: Complete Year Pass

- [ ] Compare every source field in order, including blank ranges.
- [ ] Verify start, end, length, and source order.
- [ ] Verify each normalized header preserves the source meaning.
- [ ] Verify acceptable values, notes, and administration-specific behavior.
- [ ] Verify omitted blank fields explain `column_num` gaps.
- [ ] Confirm every `column_num` is unique within the mapping.
- [ ] Confirm opaque multi-byte source rows remain one mapping field rather
      than being divided using another year's schema.
- [ ] Verify metadata and filename patterns against this year's cited source.
- [ ] Check boundaries around every suspected insertion or deletion.
- [ ] Confirm valid JSON, required shape, and string values.
- [ ] Confirm unique headers and the 63-character limit.
- [ ] Check overlaps, unintended gaps, duplicate ranges, and spillover text.
- [ ] Apply every supported correction in the year branch.
- [ ] Record stable findings, resolutions, and validation evidence.

## Operational Evidence

- [ ] Record available result-file samples and provenance.
- [ ] Quantify affected records when possible.
- [ ] Remove or de-identify student data from tracked audit evidence.
- [ ] Record limitations when samples are unavailable.

## Reviewer 1 Handoff

- [ ] Complete the entire year before requesting review.
- [ ] Summarize all corrections and reviewed-with-no-findings areas.
- [ ] Record validation commands and results.
- [ ] Record the historical-data or reprocessing decision.
- [ ] Confirm the pull request contains no shared coordinator-owned files.

## Reviewer 2: Independent Consolidated Review

- [ ] Independently compare the final mapping with the same year's source.
- [ ] Verify all source ranges, including blank and omitted ranges.
- [ ] Reproduce every high- and critical-severity finding explicitly.
- [ ] Return one consolidated list of corrections and new findings.
- [ ] Record approval, corrections requested, or a documented block.
- [ ] After corrections, verify the final mapping and resolutions again.

## Merge And Closeout

- [ ] Reviewer 2 has approved the final package.
- [ ] Required repository validation and CI pass.
- [ ] The pull request contains only the assigned work-unit files.
- [ ] Merge the year pull request into the family integration branch.
- [ ] The coordinator updates coverage, family records, and roadmap state after
      the applicable wave.
- [ ] Immediately before family closeout, refresh and independently recheck the
      official source inventory.
- [ ] Confirm every inventoried layout is mapped and reviewed or has an accepted
      block; no undispositioned difference remains.
