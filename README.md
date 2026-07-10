<div align="center">

# 📖 Somerton Man Intelligence Dossier

### A Version-Controlled Historical, Forensic & Intelligence Analysis

*An evidence-based historical investigation applying scholarly research methods, forensic reasoning, and intelligence-style analytical workflows.*

![Version](https://img.shields.io/badge/Version-v1.1.0-blue)
![Status](https://img.shields.io/badge/Status-Content%20Frozen-success)
![LaTeX](https://img.shields.io/badge/Built%20with-LaTeX-008080)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# Overview

The **Somerton Man Intelligence Dossier** is a version-controlled scholarly research repository documenting an evidence-based historical, forensic, and intelligence-style assessment of the Somerton Man case.

The repository contains the publication-ready LaTeX manuscript, the supporting research architecture used to produce it, and the editorial, verification, and governance records required to audit, reproduce, and review the work.

Rather than promoting a preferred theory, this project applies structured analytical methodologies to distinguish **documented evidence**, **supported findings**, **analytical inference**, and **unverified hypotheses**.

---

# Research Principles

This project is guided by four core principles:

- 📚 **Evidence before interpretation**
- 🔍 **Reproducible analytical methodology**
- ⚖️ **Explicit confidence assessment**
- 📝 **Transparent editorial governance**

Every substantive conclusion within the manuscript is intended to remain traceable to supporting evidence or clearly identified as interpretation.

---

# Current Status

| Item | Value |
|------|-------|
| 📘 Edition of Record | **v1.1.0** |
| 🏷 Edition Name | **Editorial & Design Edition** |
| 📅 Release Date | **2026-07-09** |
| 📌 Status | **Content Frozen** |
| 👨‍⚖️ External Review | **Pending** |

Version **v1.1.0** is the current edition of record.

The manuscript's evidence base, chronology, confidence assessments, conclusions, and analytical methodology are frozen pending external review or a qualifying revision trigger.

---

# Project Objectives

The repository is intended to preserve:

- 📄 A publication-ready scholarly manuscript
- 📚 A structured evidence and verification framework
- 🧾 Editorial history and quality assurance records
- 📈 Research methodology and analytical workflow
- 🗂 Version-controlled publication artefacts
- ⚖️ Governance controlling future revision

The project is **not** intended to:

- promote speculative theories
- advocate a preferred conclusion
- replace official records
- provide legal advice
- substitute for primary archival research

---

# Methodology

The dossier applies an intelligence-style analytical workflow incorporating:

- Evidence collection
- Source evaluation
- Claim verification
- Chronology reconstruction
- Behavioural analysis
- Competing hypothesis assessment (ACH)
- Confidence evaluation
- Editorial governance

The objective is to separate **observation**, **evidence**, **inference**, and **hypothesis**, while maintaining complete traceability between conclusions and supporting material.

---

# Repository Structure

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

---

# Key Documents

| Document | Description |
|----------|-------------|
| `README.md` | Repository overview |
| `EDITORIAL_HISTORY.md` | Editorial history and revision governance |
| `RESEARCH_SCOPE.md` | Project scope, objectives, and repository boundaries |
| `CHANGELOG.md` | Public release history |
| `publication_readiness_assessment_v1.1.0.md` | Publication readiness assessment |
| `visual_style_guide_v1.1.0.md` | Editorial and visual design standards |
| `version_1.1.0_implementation_report.md` | Editorial & Design Edition implementation summary |
| `manuscript/main.tex` | Main LaTeX entry point |
| `manuscript/build/main.pdf` | Current compiled manuscript |

---

# Repository Overview

Current release includes:

- 📖 Publication-ready scholarly manuscript
- 📚 Comprehensive reference database
- 🗂 Structured evidence registers
- ✔ Claim verification framework
- 📅 Chronological reconstruction
- 🧠 Behavioural and contextual assessment
- 📊 Confidence assessment methodology
- ⚖️ Editorial governance documentation

---

# Building the Manuscript

Build from the repository root:

```bash
make pdf
```

This compiles:

```text
manuscript/main.tex
```

Generated output is written to:

```text
manuscript/build/
```

A release-ready PDF is additionally copied to:

```text
generated_output/pdf/somerton-man-assessment.pdf
```

If **Biber** requires local bootstrapping on macOS:

```bash
make bootstrap-biber-macos
```

To remove generated files:

```bash
make clean
```

---

# Citation

Citation metadata is provided in:

```text
CITATION.cff
```

When citing this work, reference the specific repository release consulted rather than the repository generally.

Current edition:

> **Somerton Man Intelligence Dossier**
>
> **Version 1.1.0 – Editorial & Design Edition**
>
> Release Date: **2026-07-09**

---

# Revision Policy

The repository is **content frozen** as of **v1.1.0**.

Substantive revision should occur only in response to:

- Newly released primary evidence
- Official findings
- Demonstrable factual correction
- Authenticated forensic evidence
- Significant scholarly developments

Future work should branch from the frozen edition rather than modify it directly.

Routine editorial changes should never alter analytical conclusions.

---

# External Review

This edition is considered publication-ready within the repository's internal workflow.

Independent review by qualified subject-matter specialists remains the preferred next step before future substantive revision.

Relevant disciplines include:

- History
- Forensic Science
- Archival Practice
- Intelligence Analysis
- Criminal Investigation
- Behavioural Science

---

# Governance

Repository governance and publication controls are documented in:

- `EDITORIAL_HISTORY.md`
- `RESEARCH_SCOPE.md`
- `CHANGELOG.md`
- `publication_readiness_assessment_v1.1.0.md`

These documents define the editorial workflow, revision policy, publication standards, and quality assurance procedures governing the project.

---

# License

This repository is released under the terms of the repository's **LICENSE**.

Third-party archival documents, historical records, photographs, and reproduced source material referenced within the repository may remain subject to their respective copyright, archival, or usage restrictions.

Users are responsible for complying with any conditions imposed by the original custodians of those materials.

---

<div align="center">

### 📚 Evidence Before Interpretation

*Building reproducible historical research through structured evidence, transparent methodology, and disciplined analysis.*

</div>
