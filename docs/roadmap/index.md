# Repository Roadmap

This roadmap tracks repository evolution from a mapping-first data curation
workspace into a more complete assessment tooling platform.

## Milestone 0: Mapping Coverage Baseline

Status: `Completed`

- establish the core mapping families
- organize local TEA source documents
- normalize recurring field names across families where appropriate
- add family-level `README.md` and `AGENTS.md` guidance

## Milestone 1: Repository Guardrails

Status: `In Progress`

- add root documentation and agent guidance
- establish shared validation scripts and repository config
- add baseline GitHub workflow automation
- formalize coding and commit standards

## Milestone 2: Documentation System

Status: `In Progress`

- expand `docs/` beyond a PDF archive into a durable project knowledge base
- document standards, ADRs, roadmap, and repository intent
- keep human-facing docs and agent-facing docs clearly separated

## Milestone 3: Platform-Ready Scaffold

Status: `Planned`

- reserve `services/` for future application services
- reserve `packages/` for shared libraries and schemas
- expand `infra/` as deployment and runtime needs become concrete
- keep scaffolding lightweight until real code paths exist

## Milestone 4: Assessment Tooling Baseline

Status: `Planned`

- introduce application or service code only when a clear workflow needs it
- support mapping validation, inspection, or ingestion workflows programmatically
- define runtime and framework decisions through ADRs before large-scale code is added

## Working Rule

Scaffolding should be added early when it reduces future churn, but heavyweight
framework choices should wait until the repository has a concrete need for them.
