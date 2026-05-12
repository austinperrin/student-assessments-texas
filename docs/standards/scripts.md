# Scripts Standards

These standards apply to repository scripts in `scripts/` and to future shared
automation added elsewhere in the repo.

Group scripts by purpose so the layout can scale as the repository grows.
For this repo, prefer intent-based directories such as `scripts/ci/`,
`scripts/bootstrap/`, `scripts/dev/`, `scripts/docs/`, `scripts/mappings/`,
and `scripts/lib/` when those workflows exist.

## Core Rules

- keep scripts small and single-purpose
- prefer safe, repeatable behavior by default
- validate inputs explicitly and fail with clear messages
- avoid hidden side effects
- document any required local dependencies

## Repository Expectations

- repository validation scripts should be runnable from the repo root
- prefer purpose-based subdirectories over a flat script list when adding new automation
- keep script categories relative to this repository's actual workflows rather than copying unrelated app-specific buckets
- scripts that mutate tracked files should be intentional and easy to review
- destructive behavior should require an explicit confirmation flag or be clearly documented
- if a script is introduced for recurring work, document it in a nearby `README.md` or standard

## Interface Expectations

- exit `0` on success and non-zero on failure
- print actionable error output
- support `--help` when the script interface is intended for repeated human use

## Current Bias

This repository is still data- and docs-first. Favor lightweight Python or
shell-based repo utilities over heavyweight toolchains unless a stronger runtime
need emerges.
