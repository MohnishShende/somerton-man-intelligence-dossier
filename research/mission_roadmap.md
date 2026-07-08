# Mission Roadmap

This roadmap records the current project posture after Mission 9. The project is not ready for dossier prose yet; it is ready for higher-value analytical review.

## Completed Investigative Phase

| Mission | Status | Output Layer |
|---|---:|---|
| Mission 1 - Project Foundation | Complete | Repository architecture and LaTeX shell |
| Mission 2 - Evidence Database | Complete | Core registers and source catalogue |
| Mission 3 - Primary Source Acquisition | Complete | Primary-source inventory and preservation manifest |
| Mission 4 - Claim Verification | Complete | Evidence matrix and claim revision register |
| Mission 5 - Master Chronology | Complete | Source-mapped chronology |
| Mission 6 - Witness, Exhibit & Document Indexing | Complete | Page, witness, exhibit and cross-reference indexes |
| Mission 7 - Victimology & Personal Reconstruction | Complete | Victim profile, movements, possessions, relationships |
| Mission 8 - Forensic & Medical Assessment | Complete | Medical, toxicology, TOD and identifier registers |
| Mission 9 - Physical Evidence & Scene Reconstruction | Complete | Object catalogue, scene database, custody matrix |

## Remaining Analytical Missions

### Mission 10 - Witness Reliability & Testimonial Analysis

Assess each witness or declarant without making moral findings such as truthful or lying. Use structured criteria:

- Opportunity to observe
- Internal consistency
- External consistency
- Memory limitations
- Possible bias
- Relationship to events
- Corroboration
- Evidentiary value
- Testimony type
- Confidence

Expected outputs:

- `research/witness_analysis/witness_reliability_matrix.csv`
- `research/witness_analysis/testimony_consistency_register.csv`
- `research/witness_analysis/corroboration_map.csv`
- `research/witness_analysis/witness_reliability_summary.md`

### Mission 11 - Intelligence & Historical Context

Build contextual evidence without proving or disproving espionage. This mission should describe the operating environment around the case:

- Australia and South Australia in 1948
- Policing and coronial practice
- Forensic science and toxicology limits
- Rail, bus and luggage systems
- Clothing manufacturing and identity documents
- Migration and postwar identity conditions
- Cold War, ASIO, Venona, Woomera and related intelligence context

Expected outputs:

- `research/context/context_source_register.csv`
- `research/context/context_timeline.csv`
- `research/context/context_evidence_matrix.csv`
- `research/context/context_summary.md`

### Mission 12 - Structured Analytic Assessment

Apply structured analytic techniques to competing hypotheses. Do not write narrative conclusions first.

Core techniques:

- Analysis of Competing Hypotheses
- Key Assumptions Check
- Devil's Advocate Review
- Indicators and Warnings
- Argument Mapping
- Bias Review
- Source Reliability Review
- Intelligence Confidence Assessment

Hypothesis set:

- Suicide
- Homicide
- Accidental poisoning
- Espionage-related death
- Natural death
- Unknown/insufficient evidence

Expected outputs:

- `research/analysis/ach_matrix.csv`
- `research/analysis/key_assumptions_check.md`
- `research/analysis/devils_advocate_review.md`
- `research/analysis/indicators_warnings.csv`
- `research/analysis/argument_map.csv`
- `research/analysis/bias_review.md`
- `research/analysis/intelligence_confidence_assessment.md`

## Publication Phase

### Mission 13 - Manuscript Writing

Only after Mission 12, assemble the LaTeX dossier from the verified database and analytical registers. The manuscript should cite internal IDs during drafting, even if those IDs are later hidden from the reader.

### Mission 14 - Technical Review & Publication

Final review should check source traceability, LaTeX build health, figure rights, reproducibility, public release notes and version tags.

## Strategic Rule

The dossier must be built from the evidence matrix and structured registers, not from the earlier PDF or from narrative memory. The database is the source of truth; the manuscript is an output.
