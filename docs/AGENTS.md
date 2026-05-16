# Docs AI Agent Guide

This file guides AI agents working inside `docs/`.

## Scope

Use this area for:

- project overview and roadmap docs
- standards and ADRs
- local source-document archives used to maintain mappings

## Working Rules

- keep docs portable and use repo-relative links
- keep human-facing docs aligned with the current repository structure
- store local reference PDFs under `tea-data-file-formats-archive/` and keep them aligned with the current official online source
- record durable structural decisions in `adr/` instead of scattering them across multiple docs
- keep AI-agent-specific instructions in `AGENTS.md`, not in `README.md`
- add or update local `AGENTS.md` files in deeper doc hubs when a sub-area
  develops distinct agent workflows
