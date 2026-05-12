# Scripts Standards

These standards apply to repository scripts in `scripts/` and to future shared
automation added elsewhere in the repo.

## Core Rules

- keep scripts small and single-purpose
- prefer safe, repeatable behavior by default
- validate inputs explicitly and fail with clear messages
- avoid hidden side effects
- document any required local dependencies

## Repository Expectations

- repository validation scripts should be runnable from the repo root
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
