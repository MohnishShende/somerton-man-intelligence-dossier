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
- `Unknown man found at Somerton`: Use for pre-official identity phrasing.
- `Carl Charles Webb attribution`: Use only with official-status caveat.
- `South Australia Police`: Use full name on first use, abbreviation thereafter.
- `Forensic Science SA`: Use for modern forensic agency references.
- `DOC-0001 1949 inquest reproduction`: Abbott-hosted copy is a later reproduction.
- `Tamam Shud slip`: Use one spelling in manuscript; note variant spellings in glossary.
- `Rubaiyat copy`: Use neutral documentary-evidence wording.
- `Somerton Beach`: Use scene/location, not crime scene unless legal finding supports it.
- `No common poison detected`: Preserves toxicology limitation.
- `Exact cause of death undetermined`: Required medical wording.
- `Researcher/lab-led identification lead`: Use until coroner/SAPOL record obtained.
- `Historical context`: Context does not prove linkage.

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
- Use `\gls{}` and `\acrshort{}` only for glossary terms already defined in the preamble.
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
