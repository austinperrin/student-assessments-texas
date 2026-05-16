# Configs AI Agent Guide

This file guides AI agents working inside `configs/`.

## Scope

Use this area for:

- schemas
- shared validation contracts
- small repository-wide configuration files used by scripts or future tooling

## Working Rules

- keep configs framework-neutral unless a config is truly service-specific
- prefer placing shared contracts here when they are consumed by multiple scripts or future services
- update the nearest `README.md` when adding a new durable config artifact
- do not turn `configs/` into a dumping ground for one-off local settings
