#!/usr/bin/env python3
"""Generate Mission 13 manuscript authoring framework assets."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "documentation" / "authoring"
TEMPLATES = OUT / "chapter_templates"
OUT.mkdir(parents=True, exist_ok=True)
TEMPLATES.mkdir(parents=True, exist_ok=True)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


chapter_map = read_csv(ROOT / "research" / "manuscript_blueprint" / "chapter_evidence_map.csv")
intelligence_sources = (
    "research/intelligence/context_assessment.md; "
    "research/intelligence/capability_assessment.csv; "
    "research/intelligence/analysis_of_competing_hypotheses.csv; "
    "research/intelligence/key_assumptions.csv; "
    "research/intelligence/indicators_and_signposts.csv; "
    "research/intelligence/source_reliability_matrix.csv; "
    "research/intelligence/evidence_weight_matrix.csv; "
    "research/intelligence/intelligence_confidence_register.csv; "
    "research/intelligence/intelligence_requirements.csv"
)
for chapter in chapter_map:
    chapter["unresolved_gaps"] = chapter["unresolved_gaps"].replace(
        "Official SAPOL/coroner identification; complete toxicology/lab records; exhibit custody; Mission 10 structured registers not yet integrated as project files",
        "Official SAPOL/coroner identification; complete toxicology/lab records; exhibit custody; use Mission 10 project-native intelligence registers for context and structured analysis",
    )
    if chapter["chapter_id"] in {"CH-09", "CH-10", "CH-11"}:
        chapter["source_files"] = chapter["source_files"].replace(
            "/Users/mohnish/Downloads/deep-research-report.md", intelligence_sources
        )
        chapter["unresolved_gaps"] = chapter["unresolved_gaps"].replace(
            "Mission 10 context/ACH outputs need to be converted into project CSV/MD registers before final drafting",
            "Mission 10 context/ACH outputs are available as project-native intelligence registers; use them rather than the standalone downloaded report",
        ).replace(
            "No project-native ACH/intelligence register files; ASIO/MI5/other archive search logs not complete",
            "Project-native ACH/intelligence register files exist; ASIO/MI5/other archive search logs remain incomplete",
        ).replace(
            "Structured analytic registers should be generated from Mission 10 background before final prose",
            "Structured analytic registers are generated; final prose must preserve their confidence limits",
        )
table_plan = read_csv(ROOT / "research" / "manuscript_blueprint" / "table_and_figure_plan.csv")
vocab = read_csv(ROOT / "research" / "publication" / "controlled_vocabulary.csv")


def write(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def chapter_short(chapter_id: str) -> str:
    return chapter_id.replace("CH-", "")


guide = f"""
# Manuscript Authoring Guide

Mission 13 establishes the writing engine for the Somerton Man intelligence dossier. It governs all future chapter drafting. It does not add evidence or alter conclusions.

## Governing Inputs

- Manuscript blueprint: `research/manuscript_blueprint/manuscript_blueprint.md`
- Chapter map: `research/manuscript_blueprint/chapter_evidence_map.csv`
- Publication controls: `research/publication/`
- Intelligence assets: `research/intelligence/`
- Bibliography: `bibliography/master_references.bib`
- LaTeX root: `manuscript/main.tex`

## Voice

Use restrained intelligence-assessment prose. The voice is precise, calm, source-aware and non-sensational. The manuscript should sound like a forensic historical review, not a mystery retelling.

Prefer:

- `The acquired record supports...`
- `The evidence indicates...`
- `The available source does not establish...`
- `This remains unresolved in the project archive.`
- `A competing interpretation is possible, but not presently evidenced.`

Avoid:

- `proved`, unless a primary/official record actually proves the point
- `clearly`, `obviously`, `mysteriously`, `bizarre`, `sinister`, `spy-like`
- theory-first framing
- adjectives that create drama without evidence

## Tone

Tone should be neutral, economical and disciplined. The reader should always know whether the paragraph is describing a fact, an inference, a hypothesis, historical context or an intelligence gap.

## Narrative Style

Use analytical sequencing rather than true-crime suspense. Start each chapter with purpose and evidentiary status, then proceed from strongest evidence to weaker or unresolved material. Do not withhold key facts for dramatic effect.

## Objectivity Rules

- Do not advocate for a hypothesis.
- Do not resolve conflicts by assumption.
- Do not turn absence of evidence into evidence of absence unless the search corpus is defined.
- Do not use historical context as case proof.
- Do not collapse researcher attribution into official determination.

## Evidence Hierarchy

1. Original official records and primary case documents.
2. Certified copies and official scans.
3. Contemporary official statements and contemporary legal/public records.
4. Contemporary newspapers, with caution.
5. Academic or specialist secondary publications.
6. Researcher/lab participant accounts, used as high-value leads unless official/lab documentation is available.
7. Later reporting and synthesis.
8. Commentary, blogs, forums and prior internal analysis.

## Paragraph Structure

Each factual paragraph should contain:

1. Claim or topic sentence.
2. Evidence basis or source class.
3. Limitation or uncertainty if applicable.
4. Consequence for the chapter question.

Short paragraphs are preferred. Avoid burying uncertainty at the end of a long paragraph.

## Sentence Style

- Use active voice where it improves clarity.
- Keep sentences direct.
- Place qualifications near the claim they qualify.
- Do not stack multiple uncertain claims in one sentence.
- Use dates in ISO form in tables and clear prose form in text where readability matters.

## Terminology

Use `research/publication/controlled_vocabulary.csv`. Deprecated terms are not permitted in final prose except when quoting a source or explaining a prior unsupported claim.

Key controlled terms:
{chr(10).join(f"- `{row['preferred_term']}`: {row['usage_note']}" for row in vocab)}

## Citation Style

The dossier uses end references only. Avoid dense in-text citation strings. Use source IDs, document IDs, exhibit IDs or table references where auditability helps, then rely on end references and appendices for bibliographic detail.

Rules:

- Every factual statement must be traceable to a source register, evidence register, table or end reference.
- Page references belong in tables, source notes or concise parenthetical references when needed.
- The old PDF is prior-claim background only, never factual authority.
- Direct quotations should be short and only used when exact wording matters.

## Table Style

- Use `longtable` for multi-page evidence tables.
- Use compact columns and source IDs.
- Do not use decorative formatting.
- Every table must have a label, caption, source basis and chapter relevance.
- Tables should preserve uncertainty rather than smooth it.

## Figure Captions

Every figure caption must include:

- What the figure shows.
- Source/custodian.
- Date or approximate date.
- Rights/licence status.
- Processing note, if cropped, enhanced, redrawn or schematic.
- Evidence limitation, if not primary or if reconstruction is interpretive.

No rights-uncleared image may be inserted into a final chapter.

## Quotation Rules

- Quote only where exact wording affects interpretation.
- Keep quotations short.
- Prefer paraphrase for routine factual matter.
- Preserve OCR uncertainty and mark uncertain readings.
- Never silently modernize or repair source wording.

## Appendix Rules

Appendices carry audit detail: registers, source catalogues, verification matrices, conflicting claims and correction logs. Main chapters should synthesize; appendices should preserve traceability.

## Glossary and Abbreviation Rules

- Define acronyms on first use in a chapter where helpful.
- Use `\\gls{{}}` and `\\acrshort{{}}` only for glossary terms already defined in the preamble.
- Do not invent abbreviations for one-off concepts.

## Uncertainty Language

Use:

- `verified` only for evidence-supported statements.
- `partially verified` where only part of the wording is supported.
- `unresolved` where evidence is insufficient or conflicting.
- `unsupported` where searched evidence does not support the claim.
- `unable to verify` where required records are unavailable or not yet acquired.

## Confidence Wording

Confidence reflects evidence quality, not theory probability.

- Very High: authoritative primary evidence or multiple independent high-quality sources.
- High: strong source support with minor limitations.
- Moderate: credible support with material gaps.
- Low: plausible but weakly supported.
- Very Low: contextually possible but case-specific evidence is absent.
- Unknown: not assessed or source base unavailable.

## Hypothesis Wording

Hypotheses must be framed as models under assessment, not conclusions. Use `supports`, `weakens`, `is neutral toward`, `requires`, and `would change confidence if`. Avoid `explains everything`, `most likely`, or `obvious`.
"""

write(OUT / "manuscript_authoring_guide.md", guide)


generic_template = r"""
% Generic chapter template for the Somerton Man intelligence dossier.
% Copy this structure into a chapter file only when beginning a controlled chapter mission.
% Do not leave TODO markers in completed chapters.

\chapter{<Chapter Title>}
\label{chap:<chapter-slug>}

\classification{Evidence status: <Verified / Partially Verified / Mixed / Context Only / Analytical>. Confidence: <Very High / High / Moderate / Low / Very Low / Unknown>.}

\section{Purpose}
<State the chapter question and why it matters.>

\section{Scope}
<Define what this chapter covers and explicitly state what it does not cover.>

\section{Evidence Summary}
<Summarize the source base: primary records, registers, tables, and limitations.>

\section{Assessment}
<Write evidence-led prose. Separate fact, inference, hypothesis, context and unknowns.>

\section{Tables}
<Insert or reference tables. Every table must compile and have a source basis.>

\section{Figures}
<Insert only rights-cleared figures. If no figures are used, state that figures are deferred or unnecessary.>

\section{Outstanding Questions}
\begin{itemize}
  \item <Question ID and concise wording.>
\end{itemize}

\section{Confidence Statement}
<State chapter-level confidence and explain the evidence limitations.>

\section{References}
<End references are handled globally by BibLaTeX. Note key source IDs or appendix links where needed.>
"""

write(OUT / "chapter_template.tex", generic_template)


for chapter in chapter_map:
    num = chapter_short(chapter["chapter_id"])
    slug = Path(chapter["latex_file"]).stem
    template = rf"""
% Chapter-specific authoring template generated by Mission 13.
% Target chapter file: {chapter['latex_file']}
% Do not paste substantive findings without checking mapped source files.

\chapter{{{chapter['title']}}}
\label{{chap:{slug}}}

\classification{{Evidence status: <set during drafting>. Confidence baseline: {chapter['confidence_level']}.}}

\section{{Purpose}}
{chapter['purpose']}

\section{{Scope}}
Use only the mapped source files and related registers. Do not add new research unless a critical evidentiary defect is discovered and logged.

\section{{Evidence Summary}}
Inputs: {chapter['evidence_inputs']}.

Source files: \texttt{{{chapter['source_files']}}}

\section{{Key Findings To Address}}
{chapter['key_findings']}

\section{{Body}}
<Draft evidence-led chapter prose here. Separate established fact, supported inference, hypothesis, context and unknowns.>

\section{{Tables}}
Planned tables: {chapter['tables_needed']}.

\section{{Figures}}
Planned figures: {chapter['figures_needed']}.

\section{{Outstanding Questions}}
{chapter['unresolved_gaps']}

\section{{Confidence Statement}}
Baseline confidence: {chapter['confidence_level']}. Explain changes only if drafting exposes a documented source limitation.

\section{{References}}
Use end references from \texttt{{bibliography/master_references.bib}} and source/register IDs.
"""
    write(TEMPLATES / f"{num}-{slug}-template.tex", template)


editorial = """
# Editorial Style Guide

## Core Editorial Rule

The manuscript must read as an intelligence assessment. It must not read as advocacy, entertainment, theory promotion or true-crime narrative.

## Mandatory Distinctions

Every material claim must be one of:

- Fact: directly supported by evidence.
- Inference: reasoned from evidence but not directly observed.
- Hypothesis: explanatory model under assessment.
- Historical context: background that may explain plausibility but does not prove case linkage.
- Unknown: unresolved, unavailable, conflicting or insufficiently evidenced.

## Prohibited Moves

- Never overstate certainty.
- Never mix fact and speculation in one sentence.
- Never describe a hypothesis as a finding.
- Never use Cold War context as direct case evidence.
- Never use the Webb attribution as official identity unless an official record is acquired.
- Never convert `not detected` into `not present`.
- Never infer motive from object placement or literary material.
- Never treat OCR text as exact if the OCR is marked uncertain.

## Active Voice

Use active voice where it identifies the actor accurately:

- Good: `Cowan reported no signs of common poison in the submitted specimens.`
- Weak: `It was determined that poison was not present.`

Passive voice is acceptable where the actor is unknown:

- `The Tamam Shud slip was reportedly found in the trouser fob pocket.`

## Sensational Language Ban

Avoid: `sinister`, `bizarre`, `cryptic` unless quoting, `spy clue`, `killer`, `assassin`, `murder plot`, `secret lover`, `codebook` as fact.

## Adjective Test

Every adjective must either describe a documented attribute or be removed. `Fragmentary custody` is allowed if supported by the custody matrix. `Mysterious clue` is not.

## Conflict Handling

If sources conflict, describe the conflict and cite both sides. Do not decide by narrative convenience.

## Negative Claims

Do not state broad negatives unless the searched corpus is defined. Use `no acquired source establishes...` rather than `no source exists...`.
"""
write(OUT / "editorial_style_guide.md", editorial)


latex_conventions = r"""
# LaTeX Authoring Conventions

## File Structure

- Main file: `manuscript/main.tex`
- Chapter files: `manuscript/chapters/NN-slug.tex`
- Appendices: `manuscript/appendices/letter-slug.tex`
- Tables: `manuscript/tables/descriptive_name_ready_for_latex.tex`
- Figures: `manuscript/figures/`
- Bibliography: `bibliography/master_references.bib`

## Section Hierarchy

Use:

- `\chapter{}`
- `\section{}`
- `\subsection{}`
- `\subsubsection{}` only where necessary

Do not use deeper hierarchy without a documented reason.

## Labels

Use stable labels:

- Chapters: `chap:identity-biography`
- Sections: `sec:identity-webb-attribution`
- Tables: `tab:chain-of-custody`
- Figures: `fig:rubaiyat-code`
- Appendices: `app:verification-register`

## Cross References

Use `\Cref{}` at the start of sentences and `\cref{}` inside sentences where `cleveref` supports the object. Do not hard-code table or chapter numbers.

## Tables

- Use `longtable` for multi-page evidence tables.
- Use `booktabs` rules: `\toprule`, `\midrule`, `\bottomrule`.
- Keep column text concise.
- If a table is generated, edit the source generator rather than hand-editing output.
- Every table must have a caption and label.

## Landscape Pages

Use landscape only for tables that cannot be responsibly compressed. Prefer splitting wide tables into multiple narrower tables before using landscape.

## Figures

- Use only rights-cleared or project-generated figures.
- Store figures under `manuscript/figures/`.
- Use descriptive filenames: `somerton_scene_map_v1.pdf`.
- Caption must include source, rights, processing and evidentiary limitation.
- Do not insert documentary images as decoration.

## Footnotes

Footnotes are for short clarifications, not hidden citations. Use sparingly. End references remain the citation system.

## Bibliography Commands

- Use `\autocite{key}` only where a direct source reference is needed in prose.
- Use source/register IDs in prose where auditability is more useful than a citation.
- Global bibliography is printed in `manuscript/main.tex`.

## Glossary Commands

- Use `\gls{}` for defined terms.
- Use `\acrshort{}` after first definition where appropriate.
- Add new glossary entries only in the preamble and only if used more than once.

## Index Commands

Use `\index{}` for major people, evidence items, locations and concepts. Do not index routine words.

## Placeholders

Draft placeholders may use `<angle brackets>` in templates only. Completed chapters must contain no placeholder text and no `TODO`.
"""
write(OUT / "latex_authoring_conventions.md", latex_conventions)


blocks = """
# Standard Text Blocks

These blocks may be adapted during chapter drafting. They are not chapter prose by themselves.

## Evidence Note

`Evidence note: This section relies on [register/source set]. The source base supports [scope of claim] but does not establish [limitation].`

## Methodology Note

`Methodology note: Claims in this chapter are classified according to the project verification workflow. Unsupported prior claims are retained in the archive but are not promoted into findings.`

## Historical Context Notice

`Context notice: This material describes the historical environment in which the case occurred. It does not establish a direct connection to the Somerton investigation unless a case-specific source is cited.`

## Source Limitation Notice

`Source limitation: The acquired record is a later reproduction or secondary account. Where official custodian copies are unavailable, conclusions are framed provisionally.`

## OCR Limitation Notice

`OCR limitation: The relevant source text contains OCR distortion. Exact wording should be confirmed against the page image before quotation or fine-grained interpretation.`

## Identity Wording Block

`Identity status: The Carl Charles Webb attribution is treated as a researcher/lab-led identification lead pending official coroner/SAPOL determination. It is not used here as a settled legal identity.`

## Confidence Wording Block

`Confidence statement: Confidence is [level]. This reflects [source quality and limitations], not the probability of any explanatory theory.`

## Research Limitation Block

`Research limitation: No acquired source presently establishes [claim]. This remains an intelligence gap and should not be converted into a factual finding.`

## Figure Rights Block

`Figure status: This figure is deferred pending rights, source and custodian review. A schematic may be substituted only if it is clearly marked as project-generated and evidence-based.`

## Conflict Block

`Conflict note: The sources do not align on [issue]. This chapter records the conflict without resolving it by assumption.`
"""
write(OUT / "standard_text_blocks.md", blocks)


qc_items = """
# Chapter Quality Checklist

Use this checklist before a chapter is considered ready for review.

## Universal Checklist

- Chapter follows the mapped purpose and scope.
- Every factual paragraph maps to a source, register, table or end reference.
- Fact, inference, hypothesis, context and unknowns are clearly separated.
- Confidence statement is included.
- Webb identity wording follows `identity_status_guidance.md`.
- Controlled vocabulary is followed.
- No unsupported prior-PDF claims are promoted.
- No new research is introduced without a decision-log entry.
- Tables compile.
- Figures are rights-cleared or deferred.
- Cross references resolve.
- End references exist in `bibliography/master_references.bib`.
- No `TODO`, `<placeholder>`, or drafting notes remain.

## Chapter-Specific Checklists
"""
for chapter in chapter_map:
    qc_items += f"""

### {chapter['chapter_id']} - {chapter['title']}

- Purpose checked: {chapter['purpose']}
- Source files reviewed: `{chapter['source_files']}`
- Planned tables checked: {chapter['tables_needed']}
- Planned figures checked: {chapter['figures_needed']}
- Unresolved gaps preserved: {chapter['unresolved_gaps']}
- Baseline confidence preserved or explicitly justified: {chapter['confidence_level']}
"""
write(OUT / "chapter_quality_checklist.md", qc_items)


consistency = """
# Manuscript Consistency Rules

## Names

Use the controlled vocabulary and person register. Do not vary names for style. Use full name on first mention in each chapter where useful, then a consistent short form.

## Dates

- Tables use ISO dates where possible: `1948-12-01`.
- Prose may use readable dates: `1 December 1948`.
- Approximate, range, month-only and unknown dates must be marked as such.

## Evidence Identifiers

- Use stable IDs exactly as registered.
- Do not invent new IDs during drafting.
- If a new ID is unavoidable, stop drafting and update the relevant register first.

## Confidence Wording

Use the confidence scale from the authoring guide. Do not introduce synonyms such as `near certain`, `probably true`, or `basically proven`.

## References

- Use `bibliography/master_references.bib`.
- New bibliography entries require source-register or reference-audit updates.
- Do not cite sources that are not in the master bibliography.

## Figures

Figure status must match `research/publication/figure_rights_register.csv`. Rights-uncleared figures are deferred, not inserted.

## Webb Identity

All Webb wording must follow `research/publication/identity_status_guidance.md`. The approved short phrase is `researcher/lab-led Carl Charles Webb attribution, pending official coroner/SAPOL determination`.

## Toxicology

Use `No common poison detected` and `exact cause of death undetermined`. Do not write `no poison was present` or `death by poison` as fact.

## Context

Historical context belongs in Chapter 9 and analytical chapters. It must not be imported into evidence chapters as proof.

## Old PDF

The old PDF is an internal prior-assessment source only. It may appear in methodology or claim-history discussion, not as case evidence.
"""
write(OUT / "manuscript_consistency_rules.md", consistency)


criteria = """
# Chapter Completion Criteria

A chapter is complete only when every criterion below is satisfied.

## Evidence Criteria

- Every factual statement maps to documented evidence.
- Every inference is explicitly framed as inference.
- Every hypothesis is labelled as a hypothesis.
- Every intelligence gap remains visible.
- Unsupported claims are removed, downgraded or placed in a controlled prior-claims discussion.

## Source Criteria

- Source IDs, document IDs and page references are present where needed.
- End references are present in `bibliography/master_references.bib`.
- No uncatalogued source is cited.
- OCR-dependent claims have been checked against source images if exact wording matters.

## LaTeX Criteria

- Chapter compiles under `latexmk`.
- Tables compile.
- Figures compile or are intentionally deferred.
- Labels and cross references resolve.
- No overfull table design is accepted without review.

## Editorial Criteria

- No sensational language.
- No advocacy.
- No unsupported adjectives.
- Active voice is used where it improves clarity.
- Webb, toxicology, context and hypothesis wording follow the controlled guidance.

## Review Criteria

- Chapter passes the universal quality checklist.
- Chapter-specific checklist is complete.
- Confidence statement is included.
- Outstanding questions section is present.
- No `TODO`, `<placeholder>`, or drafting notes remain.
"""
write(OUT / "chapter_completion_criteria.md", criteria)


summary = f"""
# Mission 13 Summary

Mission 13 created the manuscript authoring framework. No manuscript chapters were drafted and no new evidence was added.

## Outputs Created

- `manuscript_authoring_guide.md`
- `chapter_template.tex`
- `editorial_style_guide.md`
- `latex_authoring_conventions.md`
- `standard_text_blocks.md`
- `chapter_quality_checklist.md`
- `manuscript_consistency_rules.md`
- `chapter_completion_criteria.md`
- `mission_13_summary.md`
- `chapter_templates/` with {len(chapter_map)} chapter-specific templates

## Framework Scope

- Voice, tone and narrative style fixed.
- Evidence hierarchy and uncertainty language fixed.
- Citation, table, figure, appendix, glossary and abbreviation rules fixed.
- Editorial rules and prohibited wording fixed.
- LaTeX section, label, table, figure, bibliography, glossary and index conventions fixed.
- Quality-control and completion criteria fixed.

## Writing Readiness

READY FOR CHAPTER MISSIONS.

Future chapter drafting should proceed one chapter at a time, following `research/manuscript_blueprint/manuscript_writing_order.md` and this authoring framework.
"""
write(OUT / "mission_13_summary.md", summary)

print(f"Mission 13 authoring framework written to {OUT}")
