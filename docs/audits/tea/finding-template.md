# TEA Audit Finding Template

Copy this section into the applicable review record.

```markdown
## TEA-<FAMILY>-<YEAR>-<NNN>: <short title>

- Status: candidate
- Severity: low | medium | high | critical
- Reviewer 1:
- Reviewer 2:
- Disposition owner:
- Target date:
- Next review date (required for deferred, accepted-risk, or blocked):
- Disposition reason:
- Accepted by and acceptance date:
- Mapping:
- Source document:
- Official URL:
- Source page/table:
- Source positions/columns:
- Current mapping positions:

### Source fact

State exactly what the source establishes.

### Current implementation

Describe the mapping behavior without proposing a fix.

### Impact

Describe affected fields, records, imports, or interpretations. Quantify when
evidence permits.

### Proposed disposition

Describe the correction, further investigation, deferral, or accepted risk.

### Reviewer 2 Verification

Record how Reviewer 2 independently reproduced or rejected the finding,
including identity, reviewer type, date, evidence, and conclusion. Reviewer 2
must be distinct from Reviewer 1. High- and critical-severity findings require
explicit independent reproduction.

### Resolution

- Year audit-and-correction PR:
- Correcting commit:
- Validation:
- Historical-data decision:
```
