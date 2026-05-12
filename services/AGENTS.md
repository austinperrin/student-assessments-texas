# Services Agent Guide

This folder is reserved for future application or runtime services.

## Scope

Use this area for executable surfaces such as:

- web backends
- APIs
- desktop-support services
- CLI-oriented runtime wrappers when they need a service boundary

## Working Rules

- keep canonical assessment mappings under `assessments/`
- treat `services/` as consumers of the shared assessment corpus, not the source of truth itself
- isolate framework-specific code here rather than pushing it into repo-wide docs or configs
