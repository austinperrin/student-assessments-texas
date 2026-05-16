# Services AI Agent Guide

This file guides AI agents working inside `services/`.

## Scope

Use this area for executable surfaces such as:

- web backends
- APIs
- desktop-support services
- CLI-oriented runtime wrappers when they need a service boundary

## Working Rules

- keep canonical assessment mappings under `assessments/`
- treat `services/` as consumers of the shared assessment corpus, not the
  primary location for maintaining mappings
- isolate framework-specific code here rather than pushing it into repo-wide docs or configs
- avoid creating service scaffolding unless the change has a concrete runtime use
