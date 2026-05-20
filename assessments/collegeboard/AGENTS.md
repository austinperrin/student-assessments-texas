# College Board Assessments AI Agent Guide

This file guides AI agents working inside `assessments/collegeboard/`.

## Scope

Use this area for mapping and maintenance assets tied to College Board
assessment products and data formats.

Typical College Board programs include:

- SAT Suite of Assessments
- AP
- Pre-AP
- ACCUPLACER
- Other College Board product formats as needed

## Working Rules

- keep this vendor grouping separate from `assessments/tea/`
- add result-delivery or reporting-family folders under
  `assessments/collegeboard/` rather than relying only on marketing program
  names
- keep the SAT, PSAT/NMSQT, PSAT 10, and PSAT 8/9 together under
  `assessments/collegeboard/sat_suite/`, but separate K-12 and higher-ed
  delivery families when the reporting outputs differ
- separate AP K-12 and higher-ed score-report families when the source docs
  describe different delivered files
- treat TSIA2 as a College Board subfamily only when the College Board
  ACCUPLACER materials are the governing source
- keep vendor-specific workflow assumptions in this folder and family-level
  docs
- update nearby docs in `docs/` when the vendor grouping or archive structure
  changes

## Agent Expectations

- create a `README.md` for each College Board delivery family or mapping family
  before adding mapping files
- preserve source-document accuracy and official College Board PDF or product
  guidance links in metadata
- preserve the delivery-family boundary used by the source year instead of
  inferring a new taxonomy from neighboring products
- do not infer College Board field semantics from TEA or Texas Assessments
  mapping conventions
- link archive files using repo-relative paths in
  `docs/source-archives/collegeboard/`
