# Somerton Man: A Multidisciplinary Forensic and Intelligence Assessment

This repository is the working archive for a long-term, evidence-controlled public assessment of the Somerton Man case.

The project is designed as a research dossier, not as advocacy for any theory. It separates established fact, analytical assessment, working hypothesis, and speculative scenario. Claims from previous analysis, media reports, books, official records, and research notes must be independently verified before they can appear as findings in the manuscript.

## Repository Status

Current phase: post-Mission 9 analytical review.

The repository has moved beyond manuscript setup into a structured investigative knowledge base. Missions 1-9 have created the project foundation, evidence database, primary-source inventory, verification matrix, chronology, witness/exhibit index, victimology package, forensic-medical layer, and physical-evidence/scene reconstruction layer.

The manuscript is intentionally not being drafted yet. The next phase is analytical: witness reliability, historical/intelligence context, and structured analytic assessment. The LaTeX dossier should be assembled only after those layers are complete.

## Build

Requirements:

- TeX Live or MacTeX with `latexmk`, `xelatex`, and `biber`
- GNU Make, optional but recommended

Build the manuscript:

```bash
make pdf
```

Clean generated TeX artifacts:

```bash
make clean
```

The compiled PDF is written to `generated_output/pdf/somerton-man-assessment.pdf`.

## Research Standard

Evidence priority:

1. Primary records and official documents
2. Contemporary records
3. Peer-reviewed or specialist secondary sources
4. Later media reports and commentary
5. Prior internal analysis and hypotheses

Every factual statement intended for publication must trace to the structured research database, including the verification matrix, chronology, source registers, witness/exhibit indexes, forensic registers, and physical-evidence catalogue.

## Research Release Model

This project should be treated as a versioned research archive, not a one-time book file. The PDF dossier is one output of the evidence database. Future public releases should preserve the underlying CSV registers and explain what changed between versions, such as new primary sources, chronology corrections, DNA updates, medical review changes, or expanded structured analysis.

## Repository Description

Suggested GitHub description:

> Evidence-controlled LaTeX research dossier for a multidisciplinary forensic, historical, and intelligence assessment of the Somerton Man case.

Suggested topics:

`somerton-man`, `tamam-shud`, `forensic-history`, `cold-war-history`, `intelligence-analysis`, `latex`, `open-research`, `case-review`, `source-verification`, `australian-history`

## License

See `LICENSE`. Research text is released under CC BY 4.0 unless otherwise stated. Source code and build tooling are released under MIT.
