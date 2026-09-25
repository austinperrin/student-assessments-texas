# TEA Audit Review Checklist

Use one review record per family and year. Check items only
when evidence is recorded or the review explicitly states that no issue was
found.

## Baseline

- [ ] Record repository commit and review date.
- [ ] Identify the mapping, archived source, official URL, and parser.
- [ ] Record source retrieval date and archive/online agreement.
- [ ] Record missing, inaccessible, superseded, or ambiguous sources.

## Source Fidelity

- [ ] Compare every source field in order, including blank ranges.
- [ ] Verify start, end, and length.
- [ ] Verify the normalized header preserves the source meaning.
- [ ] Verify acceptable values, notes, and administration-specific behavior.
- [ ] Verify omitted blank fields explain `column_num` gaps.
- [ ] Verify metadata and filename patterns against their cited sources.
- [ ] Check boundaries before and after every suspected insertion or deletion.

## Mapping Integrity

- [ ] Confirm valid JSON and required shape.
- [ ] Confirm string values, unique headers, and the 63-character limit.
- [ ] Check for overlaps, unintended gaps, duplicate ranges, and spillover text.
- [ ] Compare adjacent years only to locate changes requiring source review.

## Parser Review

- [ ] Confirm every parser field exists with the intended meaning that year.
- [ ] Confirm current results are not populated from history fields.
- [ ] Confirm student matching and administration joins are appropriate.
- [ ] Confirm subjects, tested grade, language, and test version are handled.
- [ ] Confirm score-code, participation, exclusion, and discrepancy behavior.
- [ ] Confirm duplicate handling does not choose an unsupported winner.
- [ ] Record years without parsers or without fields needed for a rule.

## Operational Evidence

- [ ] Record available result-file samples and provenance.
- [ ] Test confirmed parser rules in memory without changing source files.
- [ ] Quantify affected records when possible.
- [ ] Remove or de-identify student data from tracked audit evidence.
- [ ] Record limitations when samples are unavailable.

## Closure

- [ ] Assign stable finding IDs and severity.
- [ ] Obtain required independent verification.
- [ ] Record rejected candidates and why they were rejected.
- [ ] Link remediation PRs/commits and validation evidence.
- [ ] Record whether previously processed data needs reprocessing.
- [ ] Update the coverage matrix.
