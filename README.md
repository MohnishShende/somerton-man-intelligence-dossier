# Somerton Man Intelligence Dossier

The Somerton Man Intelligence Dossier is a version-controlled scholarly research repository documenting an evidence-based historical, forensic, and intelligence-style assessment of the Somerton Man case.

This repository contains the publication-ready LaTeX manuscript, the supporting research architecture used to produce it, and the editorial and governance records needed to audit, reproduce, and review the work.

## Current Status

- Edition of record: `v1.1.0`
- Edition name: `Editorial & Design Edition`
- Release date: `2026-07-09`
- Status: `Content frozen`
- External review: `Pending`

Version `v1.1.0` is the current edition of record. The manuscript's content, evidence, conclusions, confidence assessments, chronology, and methodology are frozen pending external review or a qualifying revision trigger.

## What This Project Is

The repository is intended to preserve:

- a publication-ready scholarly edition of the manuscript
- the supporting evidence and verification framework
- the editorial history and quality-assurance trail
- the governance rules controlling future revision

It is not intended to advocate a preferred theory, promote speculation, replace primary records, or provide legal advice.

## Repository Structure

```text
assets/             Repository graphics and supporting visual assets
bibliography/       BibLaTeX reference database
documentation/      Project and release-process documentation
evidence/           Primary and secondary source archive
figures/            Figure assets and image material
manuscript/         LaTeX manuscript source and compiled build output
research/           Structured research data, registers, and publication controls
release/            Versioned release artifacts
tables/             Table source material used in the manuscript workflow
verification/       Claim-verification framework
```

## Key Documents

- [README.md](README.md): repository overview
- [EDITORIAL_HISTORY.md](EDITORIAL_HISTORY.md): editorial history and revision governance
- [RESEARCH_SCOPE.md](RESEARCH_SCOPE.md): scope, non-objectives, and repository boundaries
- [CHANGELOG.md](CHANGELOG.md): public release summary
- [publication_readiness_assessment_v1.1.0.md](publication_readiness_assessment_v1.1.0.md): current publication-readiness assessment
- [visual_style_guide_v1.1.0.md](visual_style_guide_v1.1.0.md): design and presentation standards for `v1.1.0`
- [version_1.1.0_implementation_report.md](version_1.1.0_implementation_report.md): implementation summary for the Editorial & Design Edition
- [manuscript/main.tex](manuscript/main.tex): main LaTeX entry point
- [manuscript/build/main.pdf](manuscript/build/main.pdf): current compiled PDF

## Building the Manuscript

Build from the repository root:

```sh
make pdf
```

This compiles [manuscript/main.tex](manuscript/main.tex) and writes:

- build output to `manuscript/build/`
- a copied PDF to `generated_output/pdf/somerton-man-assessment.pdf`

If `biber` needs local bootstrapping on macOS, the repository includes:

```sh
make bootstrap-biber-macos
```

To clean generated output:

```sh
make clean
```

## Citation Guidance

Citation metadata is provided in [CITATION.cff](CITATION.cff).

When citing this work, cite the specific release consulted rather than the repository in the abstract. The current edition of record is `v1.1.0`, `Editorial & Design Edition`, dated `2026-07-09`.

## Revision Policy

The repository is content frozen as of `v1.1.0`.

Future substantive revision should occur only in response to:

- new primary evidence
- official findings
- demonstrable factual correction
- authenticated new forensic evidence
- major scholarly developments

Future work should branch from the frozen edition of record rather than revise it casually in place.

## External Review Status

Independent external review is pending.

The preferred next step is review by qualified subject-matter readers from relevant disciplines such as history, forensic science, archival practice, or intelligence analysis.

## Governance Files

Governance and editorial-control documents are located at the repository root:

- [EDITORIAL_HISTORY.md](EDITORIAL_HISTORY.md)
- [RESEARCH_SCOPE.md](RESEARCH_SCOPE.md)
- [CHANGELOG.md](CHANGELOG.md)
- [publication_readiness_assessment_v1.1.0.md](publication_readiness_assessment_v1.1.0.md)

## License

This repository is released under the terms of [LICENSE](LICENSE).

Third-party archival or reproduced source materials referenced in the repository may remain subject to their own archival, copyright, or usage conditions.
