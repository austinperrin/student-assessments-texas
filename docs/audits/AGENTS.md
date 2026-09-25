# Audit Documentation AI Agent Guide

## Scope

This directory contains durable audit governance, coverage, review records, and
evidence-backed findings.

## Working Rules

- treat audit work as read-only for the assets under review
- establish the repository commit and source-document baseline before review
- compare each asset with its own source; adjacent years may identify questions
  but cannot establish correctness
- cite the source document, page, positions or columns, and official URL for a
  confirmed finding
- distinguish source facts, reviewer interpretations, and proposed corrections
- record completed coverage, including reviewed areas with no findings
- do not confirm a finding solely from extracted PDF text when page layout or
  wrapped content makes the meaning ambiguous
- require an independent verifier for high- and critical-severity findings
- keep extraction, screenshots, and other disposable evidence in `.tmp/audits/`
- do not link tracked records to `.tmp` files
- do not edit mappings in an audit-only change
- treat `tea/roadmap/index.md` as the canonical audit schedule and status view
- preserve the legend-defined HTML color treatment when adding or changing
  roadmap status cells; do not introduce new status labels or colors casually
- update roadmap dates, the affected milestone, and coverage together when a
  schedule or scope change would otherwise make them disagree
- use the branch and pull request boundaries in `tea/workflow.md`
- keep one reporting year per year audit branch and review record
- merge year audit branches only into their family audit branch; merge the
  family branch into `main` only after family reconciliation and sign-off
