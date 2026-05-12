# ADR Standards

Architecture Decision Records are used to capture decisions that are important
enough to revisit later.

## Use ADRs For

- repository structure changes with long-term consequences
- new runtime, framework, or deployment baselines
- shared schema or validation contract decisions
- changes that affect how future services or packages should be organized

## Do Not Use ADRs For

- ordinary year-by-year mapping additions
- simple typo fixes or one-off documentation edits
- decisions that are purely local to one small file and unlikely to matter later

## Required Structure

Each ADR should include:

- `Status`
- `Date`
- `Context`
- `Decision`
- `Consequences`
- `Alternatives Considered`
- `Follow-Up`

## Lifecycle

- create ADRs as `Proposed` when a decision still needs alignment
- mark them `Accepted` once the direction is chosen
- mark them `Superseded` when replaced by a later ADR
- keep old ADRs for historical context instead of deleting them
