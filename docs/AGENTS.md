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
- store local reference source documents under the matching vendor subtree in
  `docs/source-archives/`
- for future vendors, describe archive structure in terms of delivery families
  when those families are more stable than product branding alone
- record durable structural decisions in `adr/` instead of scattering them across multiple docs
- keep AI-agent-specific instructions in `AGENTS.md`, not in `README.md`
- add or update local `AGENTS.md` files in deeper doc hubs when a sub-area
  develops distinct agent workflows
