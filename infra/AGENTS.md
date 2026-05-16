# Infra AI Agent Guide

This file guides AI agents working inside `infra/`.

## Scope

Do not place active mappings, shared human docs, or general project contracts
here.

Use this area only when the project gains real infrastructure needs such as:

- deployment definitions
- scheduled runtime jobs
- environment-specific infrastructure notes

## Working Rules

- keep infra additions lightweight until a concrete runtime need exists
- prefer documenting why an infra artifact exists when the folder begins to fill out
- do not create speculative deployment structure without a real execution need
