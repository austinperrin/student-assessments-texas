# Packages AI Agent Guide

This folder is reserved for future shared libraries, schemas, and reusable modules.

## Scope

Use this area for reusable code that should be shared across multiple surfaces,
such as future CLI, web, desktop, or background-service tooling.

Possible future examples:

- assessment loaders
- mapping validators
- shared schemas and domain models
- parsing or normalization libraries

## Working Rules

- keep package code platform-neutral when it supports multiple surfaces
- avoid moving canonical assessment data into `packages/`
- document package purpose clearly when the first real module is added
