# Audit Documentation AI Agent Guide

## Scope

This directory contains durable audit governance, coverage, review records, and
evidence-backed findings.

## Working Rules

- treat one family/year as an independent audit work unit
- establish the repository commit and source-document baseline before review
- use only the assigned year's source as evidence; do not inspect adjacent-year
  mappings or sources during the year review
- cite the source document, page, positions or columns, and official URL for a
  confirmed finding
- distinguish source facts, reviewer interpretations, and proposed corrections
- record completed coverage, including reviewed areas with no findings
- do not confirm a finding solely from extracted PDF text when page layout or
  wrapped content makes the meaning ambiguous
- assign distinct Reviewer 1 and Reviewer 2 identities to every work unit;
  either may be human or AI, but an agent must not verify its own work
- keep extraction, screenshots, and other disposable evidence in `.tmp/audits/`
- do not link tracked records to `.tmp` files
- let Reviewer 1 audit, correct, resolve, and validate the entire year in one
  branch and pull request before Reviewer 2 begins the consolidated review
- treat `tea/roadmap/index.md` as the canonical audit schedule and status view
- preserve the legend-defined HTML color treatment when adding or changing
  roadmap status cells; do not introduce new status labels or colors casually
- update roadmap dates, the affected milestone, and coverage together when a
  schedule or scope change would otherwise make them disagree
- use the branch and pull request boundaries in `tea/workflow.md`
- create one family integration branch from current `main`; create each year
  branch from that family branch and merge it back into the family branch
- allow independent family/year work units to run in parallel
- keep one reporting year per branch, pull request, and review record
- reserve coverage, family summaries, and roadmap files for a coordinator
  closeout change on the family branch after all year pull requests merge
- do not add a tracked source-row manifest or require a dedicated
  source-to-mapping validator unless the program owner changes that decision
