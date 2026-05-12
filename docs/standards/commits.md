# Commit Standards

These commit conventions are intended to keep the history clear for a repository that mixes mapping data, reference docs, and shared repo tooling.

## General Rules

- keep commits scoped to one logical change
- avoid mixing mapping edits, repo scaffolding, and unrelated documentation cleanup in the same commit when they can be separated
- prefer a follow-up commit over a noisy multi-purpose commit
- exclude local scratch files and untracked experiments

## Message Style

Use short conventional-style prefixes when they fit:

- `feat:` for new mapping families, new year files, or meaningful new repo capabilities
- `fix:` for data corrections, duplicate header fixes, range corrections, or broken links
- `docs:` for README, AGENTS, standards, or archive organization changes
- `chore:` for low-level repo maintenance that is not a feature or documentation change
- `refactor:` for structural cleanup that preserves behavior

## Good Commit Shapes

- one family added or normalized
- one year added to a family
- one repo-standard docs change
- one validation/tooling addition
- one archive or layout reorganization
- one platform-scaffold improvement such as `services/`, `packages/`, `.github/`, or shared standards

## Good Examples

- `feat: add crs custom mapping family`
- `fix: remove stray standard field from 2025 eoc mapping`
- `docs: reorganize reference PDFs by year`
- `chore: add repo validation and pr scaffolding`

## Avoid

- vague messages like `updates` or `misc fixes`
- combining unrelated families in one commit without a strong reason
- committing generated scratch files such as `tmp_*.txt`
- hiding data changes inside a docs-only commit message

## Before Committing

1. confirm the staged files match one logical purpose
2. confirm scratch files and local-only artifacts are excluded
3. run relevant validation when the change touches mappings or shared docs
4. make sure the commit message reflects what actually changed
