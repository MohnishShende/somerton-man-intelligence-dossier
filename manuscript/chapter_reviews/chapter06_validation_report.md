# Chapter 6 Validation Report

Publication unit: Physical Evidence  
Target file: `manuscript/chapters/06-physical-evidence.tex`  
Build file: `manuscript/main.tex`

## Validation Result

Status: Passed with repository-level note.

Chapter 6 replaces the placeholder with a physical-evidence inventory chapter and compiles through the full manuscript build. The build produces `manuscript/build/main.pdf`. The recurring `xdvipdfmx` object warning appears at the document build layer and was present in earlier publication-unit validation. Chapter 6 preserves the required section structure:

1. Overview of Physical Evidence
2. Discovery Scene
3. Clothing
4. Personal Property
5. Suitcase and Contents
6. Tamam Shud Slip
7. Rubaiyat
8. Biological Evidence
9. Chain of Custody
10. Preservation History
11. Physical Evidence Assessment

## Quality Checklist

- Evidence mapped: Passed. See `manuscript/chapter_reviews/chapter06_paragraph_evidence_map.csv`.
- Evidence fact check: Passed. See `manuscript/chapter_reviews/chapter06_evidence_fact_check.csv`.
- Exhibit cross-reference: Passed. See `manuscript/chapter_reviews/chapter06_exhibit_cross_reference.csv`.
- Every major exhibit maps to an evidence identifier or documented N/A status: Passed.
- Chain-of-custody wording matches repository records: Passed.
- Preservation wording matches repository records: Passed.
- No unsupported ownership claims: Passed.
- No unsupported significance claims: Passed.
- No hypothesis evaluation: Passed.
- No copyrighted figures inserted: Passed. A text-only placeholder is used where publication-cleared image rights are not established.
- Controlled vocabulary: Passed. The chapter uses `Tamam Shud`, `Rubaiyat`, `Adelaide Railway Station`, and evidence IDs from the repository.
- Database boundary: Passed. No research registers were modified.

## Build Check

Command run:

```sh
latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -outdir=manuscript/build manuscript/main.tex
```

Result: Passed. The recurring document-level `xdvipdfmx` object warning remains non-blocking.

## Source Boundary

No new research was performed. Chapter 6 draws from authorized repository assets, especially `research/physical_evidence/physical_evidence_catalogue.csv`, `research/indexes/exhibit_index.csv`, `research/physical_evidence/scene_reconstruction_database.csv`, `research/physical_evidence/chain_of_custody_confidence_matrix.csv`, `research/physical_evidence/preservation_history.csv`, `research/physical_evidence/physical_evidence_source_map.csv`, `research/physical_evidence/physical_evidence_uncertainties.csv`, `research/forensic_medical/forensic_identifiers_register.csv`, `research/database/evidence_register.csv`, `research/chronology/chronology_master.csv`, and `research/physical_evidence/physical_evidence_summary.md`.

## Chapter Boundary

Only `manuscript/chapters/06-physical-evidence.tex` was modified among chapter files. Review artifacts were added under `manuscript/chapter_reviews/`.

## Editorial Note

The chapter is intentionally conservative. It treats the suitcase, Rubaiyat, Tamam Shud slip, label removal, cigarette, thread, sand, vegetation, hair, and biological specimens as physical-evidence records with custody and preservation limits, not as proof of ownership, motive, cause of death, or any competing hypothesis.
