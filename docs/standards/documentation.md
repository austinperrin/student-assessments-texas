# Documentation Standards

These standards define where durable project information belongs and how pages
should reference one another without creating competing sources of truth.

## Documentation Roles

- `README.md` files orient readers to an area and link to deeper guidance.
- `docs/overview/` explains project structure and provides concise indexes.
- `docs/runbooks/` contains authoritative, task-oriented operating procedures.
- `docs/standards/` records durable rules and maintenance expectations.
- `docs/adr/` records decisions whose rationale should survive implementation
  changes.
- `AGENTS.md` files contain AI-agent-specific routing and guardrails.

## Ownership And References

Give each maintained fact one authoritative home. Other pages should summarize
only enough to route the reader and then link to that source.

Use this reference direction for recurring script workflows:

```text
project README -> command index -> runbook -> implementation README and code
```

- command indexes list entrypoints and link to the owning runbook
- runbooks own operator-facing defaults, options, examples, side effects,
  outputs, verification, and recovery steps
- implementation READMEs explain code organization, tests, and contributor
  concerns without duplicating the operator procedure
- CLI `--help` owns the accepted argument names, choices, and short descriptions
- do not copy complete option lists or default-path descriptions into multiple
  human-facing pages

When a short summary must repeat a fact, link to its authoritative page and
avoid details likely to change, such as a default value or output path.

## Navigation And Learning Paths

Use `docs/index.md` as the primary documentation hub. It should help readers
choose a task and follow a recommended sequence instead of reproducing the
repository tree.

- the project `README.md` should route readers to the documentation hub
- every major documentation area should have a `README.md` or index that states
  its purpose and links back to the hub or its parent index
- indexes should organize links by reader goal or workflow before listing raw
  files
- a reader should be able to move from overview, to governing standard or
  procedure, to implementation details without searching the repository
- large inventories belong in their owning section, not in the documentation
  hub
- use meaningful link labels that describe the destination or task

## Runbook Expectations

Create a runbook for a recurring human-operated workflow when it has meaningful
inputs, side effects, generated artifacts, verification steps, or recovery
considerations.

Each runbook should include, where relevant:

1. purpose and selection guidance
2. prerequisites and expected input layout
3. the safest default command
4. common scenarios with exact commands
5. a complete option table
6. output and artifact layout
7. important side effects
8. verification steps
9. troubleshooting and safe rerun guidance
10. links to the implementation and tests

Write procedures from the repository root unless a different working directory
is an intentional part of the workflow.

## Change Requirements

When a human-facing CLI changes, update all of the following in the same change:

- parser help text
- relevant tests
- the authoritative runbook
- the command index when an entrypoint is added, removed, or renamed
- nearby navigation when the workflow's location or ownership changes

Review summaries in higher-level READMEs for stale claims, but prefer removing
duplicated details instead of synchronizing multiple copies.

## Link And Content Rules

- use repo-relative links in tracked documentation
- never commit machine-specific paths or scratch output
- use human-facing `README.md` files for orientation, not AI instructions
- keep AI-specific guidance in the nearest applicable `AGENTS.md`
- prefer links to stable documentation pages over direct links to incidental
  generated artifacts
