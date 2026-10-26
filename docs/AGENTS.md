# Docs AI Agent Guide

This file guides AI agents working inside `docs/`.

## Scope

Use this area for:

- project overview and roadmap docs
- task-oriented runbooks for recurring human workflows
- standards and ADRs
- local source-document archives used to maintain mappings

## Working Rules

- keep docs portable and use repo-relative links
- keep human-facing docs aligned with the current repository structure
- give mutable workflow facts one authoritative home and link to them instead
  of copying complete procedures across pages
- keep command indexes concise and put operational details in `docs/runbooks/`
- preserve `docs/index.md` as the primary task-oriented learning hub
- give each major documentation area a local landing page that links to its
  parent path or the documentation hub
- store local reference source documents under the matching vendor subtree in
  `docs/source-archives/`
- for future vendors, describe archive structure in terms of delivery families
  when those families are more stable than product branding alone
- record durable structural decisions in `adr/` instead of scattering them across multiple docs
- keep AI-agent-specific instructions in `AGENTS.md`, not in `README.md`
- add or update local `AGENTS.md` files in deeper doc hubs when a sub-area
  develops distinct agent workflows
