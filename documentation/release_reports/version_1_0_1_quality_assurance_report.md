# Version 1.0.1 Quality Assurance Report

Date: 2026-07-09

Manuscript: `manuscript/main.tex`

Compiled output: `manuscript/build/main.pdf`

## Executive Result

Version 1.0.1 implements the methodology, historiography, source-criticism, uncertainty-management, and evidentiary-boundary recommendations from `comprehensive_scholarly_editorial_assessment_2026-07-09.md`.

The revision is controlled rather than expansive. It strengthens the manuscript's academic framework and internal safeguards without altering supported findings, chronology, confidence assessments, or conclusions.

## Change Totals

- Substantive register entries: 38
- Critical changes resolved: 12
- Important changes resolved: 22
- Editorial changes resolved: 4
- Optional changes implemented: 0
- Conclusions changed: 0
- Chronology changed: 0
- New factual findings introduced: 0
- New bibliography records invented: 0

## Critical Issues Resolved

- Added explicit historical method and source criticism.
- Added custody, provenance, and reproduction-status controls.
- Added forensic reasoning and evidentiary-boundary rules.
- Added a source-to-claim-to-assessment analytical framework.
- Added bias-control safeguards for narrative closure, source cascade, hindsight, and identity anchoring.
- Added absence/non-detection rules to prevent unsupported negative conclusions.
- Added a dedicated historiography section.
- Added a formal `Preface to the Reader` after the title page to orient readers to the manuscript's evidentiary philosophy.
- Preserved conservative wording for the Webb attribution and ongoing SAPOL/coronial status.
- Reinforced toxicology limits: no common poison detected is not a universal poison exclusion.
- Reinforced espionage limits: interpretive tradition and hypothesis class, not finding.

## Audit Results

### Factual Consistency

Pass. The new language clarifies source status and limits rather than adding new case facts. New factual references were tied to existing bibliography keys and project registers.

### Chronological Consistency

Pass. No chronology event was added, removed, reordered, or re-dated. The revision added only a caveat that exclusion from the admitted chronology does not prove an excluded event false.

### Terminology Consistency

Pass. The revision standardizes recurring distinctions:

- researcher/lab-led Webb attribution versus official identity determination
- no common poison detected versus no poison present
- contextual plausibility versus case-specific proof
- object existence versus complete custody
- reliability as evidentiary use rather than moral credibility

### Citation Consistency

Pass. Added citations use existing bibliography keys only:

- `src-src-0003`
- `doc-doc-0001`
- `src-src-0005`
- `src-src-0018`
- `src-src-0014`
- `m11-m11-src-0001`
- `m11-m11-src-0003`
- `m11-m11-src-0009`

No invented source, citation, or bibliography record was added.

### Figure and Table Numbering

Pass at compile level. LaTeX rebuilt successfully and emitted no undefined-reference or rerun warnings in the scanned logs.

### Appendix References

Pass at compile level. Appendix auxiliary files were generated during the final build, and no undefined-reference warnings were detected.

### Glossary Consistency

Pass at compile level. The glossary system remains enabled in `manuscript/main.tex`, and no glossary-related build errors were detected.

### Bibliography Consistency

Pass. Biber ran through `latexmk`; no undefined-citation warnings were detected in `main.log` or `main.blg`.

### Cross-Reference Integrity

Pass. The manuscript source files contain 104 label/reference/caption-related commands and compiled without undefined-reference warnings.

### Duplicate Material

Pass with residual watch item. The added methodological material intentionally reinforces recurring distinctions across chapters, but the repetition is functional: Chapter 2 states the governing method, while later chapters apply it to identity, toxicology, custody, chronology, witnesses, and intelligence hypotheses.

### Contradictory Statements

Pass. The new language reduces contradiction risk by stating that public Webb attribution remains distinct from official custodial/legal closure, and by separating contextual espionage plausibility from evidentiary finding.

### Unsupported Assertions

Pass for implemented changes. New claims are framed as methodological controls, register-derived counts, or source-bounded status notes. No unsupported factual assertion was knowingly introduced.

## Build Verification

Command run:

```sh
latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -outdir=manuscript/build manuscript/main.tex
```

Result:

- Exit status: 0
- Output PDF: `manuscript/build/main.pdf`
- Page count: 108
- PDF engine: `xdvipdfmx`
- Log scan: no LaTeX errors, package errors, undefined citations, undefined references, rerun warnings, overfull warnings, or underfull warnings detected by the QA scan.

Inventory checks:

- Citation commands in manuscript source files: 12
- Label/reference/caption commands in manuscript source files: 104
- Preface length: 956 words

## Remaining Unresolved Issues

- Official identity closure remains unresolved because no acquired coroner, SAPOL, or Forensic Science SA determination was added to the repository for this revision.
- Cause and mechanism of death remain unresolved under the manuscript's evidence rules.
- Current custody of several physical-evidence items remains incomplete or unknown.
- Rubaiyat provenance, code interpretation, and telephone-number implications remain unresolved.
- Intelligence-service linkage remains unsupported by case-specific official records.
- Some source reproductions remain preferable to replace with official custodian copies in a future archival pass.

## Recommendations Deferred

- Full visual redesign and theme work were deferred because this pass was limited to methodology, historiography, source criticism, and traceable scholarly implementation.
- Detailed table redesign, callout-panel redesign, and typography/package modernization were deferred to a later design/typesetting pass.
- Any deeper chapter rewriting was deferred unless needed to implement the approved scholarly recommendations.
- No new source acquisition was attempted in this implementation pass.

## Publication Readiness Assessment

Score: 8.1/10

Version 1.0.1 is substantially stronger as an academic forensic and intelligence reference manuscript. Its major improvement is not a change in conclusion but a clearer evidentiary architecture: the reader can now see how sources, claims, custody, uncertainty, historiography, and analytical confidence interact.

The principal remaining barriers to university-press readiness are external to this controlled revision: official custodian copies, official identity-status records, deeper permissions/figure clearance, final typographic design, and any future official forensic or coronial updates.
