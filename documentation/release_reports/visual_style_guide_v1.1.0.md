# Version 1.1.0 Visual Style Guide

Date: 2026-07-09

## Design Character

The manuscript uses a restrained academic-forensic style: sober, archival, readable, and evidence-first. Visual design should support navigation, source discipline, and analytical clarity rather than decoration.

## Typography

- Body: TeX Gyre Pagella.
- Sans serif: TeX Gyre Heros.
- Monospace: TeX Gyre Cursor.
- Body leading: slightly opened with `\linespread{1.035}`.
- Paragraphs: indented, no paragraph spacing.
- Headings: sans serif, dark navy, left aligned.

## Colour

- `AssessmentNavy`: primary heading/link color.
- `AssessmentAccent`: restrained archival accent rule.
- `AssessmentRule`: neutral rule color.
- `AssessmentSoft`: analytical-status background.
- `AssessmentPale`: table row tint.
- `AssessmentLine`: table rule color.
- `AssessmentMuted`: running-head and page-number color.
- `AssessmentInfo`: intelligence/context accent.
- `AssessmentWarn`: caution accent.

All colors must remain readable in grayscale. No conclusion may depend on color alone.

## Page Layout

- Letter page size.
- One-sided layout for digital and desktop reading.
- Slightly asymmetric inner/outer margins for monograph feel.
- Running heads identify current chapter context.
- Plain chapter-opening pages use centered footer page numbers.

## Heading Hierarchy

- Chapter: large sans serif title with chapter number and accent rule.
- Section: bold sans serif, numbered.
- Subsection: bold sans serif, numbered.
- Avoid decorative heading graphics.

## Caption Standards

- Captions use small sans serif type.
- Caption labels are bold and navy.
- Captions should describe the table or figure without adding unsupported interpretation.
- Captions should not contain new evidence unless already supported in the relevant section.

## Table Standards

- Use `booktabs` rules.
- Use restrained alternating row tinting.
- Prefer ragged-right paragraph columns for dense evidence tables.
- Keep table content source-bounded.
- Reduce font size table-by-table only when needed for fit.
- Do not use vertical rules.

## Box Styles

Use boxes sparingly for navigational and evidentiary functions.

- `\classification`: chapter-level analytical status.
- `\evidencebox`: evidence summaries.
- `\findingbox`: findings already supported in text.
- `\assessmentbox`: intelligence assessment statements.
- `\cautionbox`: source, inference, or legal caution.
- `\gapbox`: intelligence or research gaps.

Boxes must not introduce new claims or elevate hypotheses.

## Figures and Maps

- Figures remain deferred until rights and provenance are resolved.
- Maps must include clear source, scale/extent where applicable, and non-color-dependent readability.
- Do not use atmospheric or decorative imagery as evidence.

## Timeline Standards

- Timelines should distinguish observed time, reported time, estimated time, and later reconstruction.
- Approximate times must remain visibly approximate.
- Timeline design must not imply chronology precision beyond the source.

## Accessibility

- Maintain readable font sizes.
- Preserve high contrast in text and rules.
- Do not rely on color alone.
- Preserve PDF bookmarks and navigable table of contents.
- A future PDF/UA pass is recommended for public archival distribution.
