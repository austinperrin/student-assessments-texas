# GitHub Workflow Overview

This folder holds workflow automation and contribution templates for the
project.

## Current Contents

- [workflows/](./workflows/)
  CI-style validation for project changes
- [PULL_REQUEST_TEMPLATE.md](./PULL_REQUEST_TEMPLATE.md)
  Pull request checklist aligned to mapping and documentation work
- [ISSUE_TEMPLATE/](./ISSUE_TEMPLATE/)
  Lightweight intake forms for mapping and project improvement work

## Current Automation Baseline

The current workflow automation favors a lightweight validation model:

- run formatting checks and project validation on pull requests
- run the same validation on pushes to main working branches
- keep automation aligned to the project's current data-first scope

As the project grows into services or packages, this folder can expand to
include additional workflows for linting, tests, security checks, packaging, or
deployment.

## Related References

- [../README.md](../README.md)
  Project overview and top-level navigation.
- [../scripts/ci/README.md](../scripts/ci/README.md)
  Current CI validation tooling.
- [../docs/overview/scripts-and-commands.md](../docs/overview/scripts-and-commands.md)
  Common project command reference.
