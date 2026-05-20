# College Board Assessments

This folder is the vendor-level home for College Board assessment mapping
families and related maintenance guidance.

## Purpose

Add College Board assessment mapping folders here. For College Board, the
primary grouping below the vendor should usually reflect the result-delivery or
reporting family that emits the files districts, schools, or universities
receive.

Current scaffolded families include:

- `sat_suite/`
  - `sat_suite/k12_reporting/sat/`
  - `sat_suite/k12_reporting/psat_nmsqt/`
  - `sat_suite/k12_reporting/psat_10/`
  - `sat_suite/k12_reporting/psat_8_9/`
  - `sat_suite/higher_ed_reporting/sat/`
- `ap/`
  - `ap/k12_score_reports/`
  - `ap/higher_ed_score_reports/`
- `pre_ap/`
  - `pre_ap/classroom_assessments/`
- `accuplacer/`
  - `accuplacer/platform_reports/`
  - `accuplacer/tsia2/`

This scaffold combines two rules:

- the SAT, PSAT/NMSQT, PSAT 10, and PSAT 8/9 are grouped under the SAT Suite
  of Assessments
- result delivery families come before year-specific mappings when those
  reporting outputs are more durable than the assessment brand alone

Each delivery family or mapping family includes its own `README.md` describing
source coverage, naming expectations, and any vendor-specific mapping guidance.

## Current Status

This is an initial scaffold for College Board assessments. No mappings have
been added yet.

Historic source material should stay aligned to the same family structure unless
the source documentation shows that the delivered file family itself changed.

## Related References

- [../README.md](../README.md)
  Top-level assessments corpus entrypoint.
- [../../docs/source-archives/collegeboard/](../../docs/source-archives/collegeboard/)
  College Board source document archive.
