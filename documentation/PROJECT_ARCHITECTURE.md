# Project Architecture

## Operating Principle

The repository is a controlled research archive. The manuscript is only one output. The deeper asset is the traceable chain from question, to claim, to source, to verification status, to published conclusion.

## Directory Structure

```text
manuscript/
  main.tex
  chapters/
  appendices/
  frontmatter/
  backmatter/
  styles/
  figures/
  tables/
bibliography/
figures/
  source/
  processed/
  exported/
tables/
  source/
  generated/
research/
  source_logs/
  notes/
  questions/
  people/
  organizations/
  locations/
  timelines/
verification/
  claims/
  logs/
  matrices/
  protocols/
evidence/
  primary_sources/
  secondary_sources/
  government_records/
  police_records/
  coronial_documents/
  newspapers/
  photographs/
  maps/
  genealogy/
  forensic_reports/
  media_articles/
generated_output/
archive/
documentation/
```

## Data Flow

1. A source is discovered and entered into `research/source_logs/`.
2. Claims are extracted into `verification/claims/`.
3. Each claim receives a status, source pointer, and uncertainty note.
4. Verified or qualified claims may be promoted into chapter notes.
5. Manuscript text cites only source-backed claims.
6. Releases preserve the claim register used for that version.

## Claim Classes

- Established Fact: directly supported by reliable evidence.
- Analytical Assessment: reasoned inference from established facts.
- Working Hypothesis: plausible explanation requiring further testing.
- Speculative Scenario: low-confidence possibility retained only for comparison or exclusion.

## Chapter Organization

1. Executive Assessment
2. Methodology and Evidence Standards
3. Case Chronology
4. Identity and Biographical Reconstruction
5. Scene, Body, and Forensic Evidence
6. Toxicology and Cause-of-Death Assessment
7. The Rubaiyat, Tamam Shud Slip, and Cipher Material
8. Witnesses, Contacts, and Social Network
9. Historical and Institutional Context
10. Intelligence-Related Hypotheses
11. Alternative Explanatory Models
12. Findings, Unknowns, and Future Research

## Appendix Organization

- Appendix A: Verification Register
- Appendix B: Source Catalogue
- Appendix C: Timeline Tables
- Appendix D: People and Organizations Index
- Appendix E: Location Register and Maps
- Appendix F: Forensic Methods Notes
- Appendix G: Cryptographic Methods Notes
- Appendix H: Conflicting Claims Matrix
- Appendix I: Correction Log

## Bibliography Architecture

Use BibLaTeX with Biber. Keep source categories in separate files when the archive grows:

- `bibliography/primary.bib`
- `bibliography/government-records.bib`
- `bibliography/newspapers.bib`
- `bibliography/books-articles.bib`
- `bibliography/media.bib`
- `bibliography/internal.bib`

Every entry should include the best available locator: archive, collection, series, item number, page, image, URL, access date, and rights note.

## Figure Management

- Store raw files in `figures/source/`.
- Store corrected or cropped derivatives in `figures/processed/`.
- Store publication-ready assets in `figures/exported/`.
- Never overwrite raw source images.
- Every figure needs a source ID, rights status, processing note, and caption draft.

## Table Management

- Store hand-maintained source tables in `tables/source/`.
- Store generated tables in `tables/generated/`.
- Publication tables should be generated or copied into `manuscript/tables/`.
- Tables must include data provenance.

## Build System

The primary build path is `make pdf`, which uses `latexmk`, `xelatex`, and `biber`. Generated PDFs go to `generated_output/pdf/`.

## Scalability Recommendations

- Keep chapters short and modular.
- Split bibliography files by source class once the source list exceeds 150 entries.
- Use CSV or YAML registers for machine-readable verification data.
- Archive public releases with fixed claim-register snapshots.
- Avoid embedding large binary evidence files unless rights and file size are manageable.

