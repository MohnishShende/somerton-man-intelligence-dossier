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
