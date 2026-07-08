# Chapter Order Validation

Mission: 14C.5 -- Manuscript Structure Refactor  
Target file: `manuscript/main.tex`  
Validation date: 2026-07-08

## Validation Result

Status: Passed with repository-level note.

The LaTeX manuscript structure now follows the approved publication-unit sequence. Completed prose in Chapters 1, 2, and 3 was not rewritten. Research data, bibliography files, and figure assets were not modified.

## Approved Chapter Sequence

| Unit | Include file | Title |
|---|---|---|
| 01 | `manuscript/chapters/01-executive-assessment.tex` | Executive Summary |
| 02 | `manuscript/chapters/02-methodology.tex` | Methodology and Evidence Standards |
| 03 | `manuscript/chapters/03-sources-and-evidence.tex` | Sources, Evidence, and Research Corpus |
| 04 | `manuscript/chapters/04-historical-operational-context.tex` | Historical, Social, and Operational Context |
| 05 | `manuscript/chapters/05-discovery-investigation-chronology.tex` | Discovery, Investigation, and Master Chronology |
| 06 | `manuscript/chapters/06-physical-evidence.tex` | Physical Evidence |
| 07 | `manuscript/chapters/07-witnesses-testimony.tex` | Witnesses and Testimony |
| 08 | `manuscript/chapters/08-victimology-identity.tex` | Victimology and Identity |
| 09 | `manuscript/chapters/09-forensic-medical-assessment.tex` | Forensic and Medical Assessment |
| 10 | `manuscript/chapters/10-intelligence-assessment-hypotheses.tex` | Intelligence Assessment and Competing Hypotheses |
| 11 | `manuscript/chapters/11-outstanding-questions-gaps.tex` | Outstanding Questions and Intelligence Gaps |
| 12 | `manuscript/chapters/12-conclusions-future-research.tex` | Conclusions and Future Research |

## Structural Changes

- `main.tex` now includes `03-sources-and-evidence.tex` immediately after Methodology.
- The old chronology placeholder was renumbered to Unit 05.
- Historical context was moved to Unit 04 and renamed to `Historical, Social, and Operational Context`.
- Physical evidence, witnesses, victimology, forensic-medical, intelligence-assessment, intelligence-gaps, and conclusions placeholders were renumbered to match the approved sequence.
- The obsolete Rubaiyat-only and alternative-model placeholder files were removed because the approved architecture folds those topics into Physical Evidence and Intelligence Assessment.
- Chapter numbering is continuous from 1 through 12 in the compiled manuscript.

## Build Check

Command run:

```sh
latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -outdir=manuscript/build manuscript/main.tex
```

Result: Passed.

The build produced `manuscript/build/main.pdf` with 44 pages. The recurring `xdvipdfmx` object warning appears at the document build layer and was already present before this refactor.

## Boundary Check

- Completed chapter prose changed: No.
- Research data changed: No.
- Bibliography changed: No.
- Figures changed: No.
- Main include order changed: Yes, intentionally.
- Placeholder filenames/titles changed: Yes, intentionally.

## Next Publication Unit

The next unit is:

`manuscript/chapters/04-historical-operational-context.tex`

Working title:

Historical, Social, and Operational Context
