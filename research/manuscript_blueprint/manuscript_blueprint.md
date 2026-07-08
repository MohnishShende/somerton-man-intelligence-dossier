# Manuscript Blueprint

Mission 12 converts the completed research database into a controlled LaTeX writing plan. It does not draft substantive chapter prose.

## Final Table of Contents

CH-01. Executive Assessment -> `manuscript/chapters/01-executive-assessment.tex`
CH-02. Methodology and Evidence Standards -> `manuscript/chapters/02-methodology.tex`
CH-03. Case Chronology -> `manuscript/chapters/03-case-chronology.tex`
CH-04. Identity and Biographical Reconstruction -> `manuscript/chapters/04-identity-biography.tex`
CH-05. Scene, Body, and Physical Evidence -> `manuscript/chapters/05-scene-forensics.tex`
CH-06. Forensic Medical and Toxicology Assessment -> `manuscript/chapters/06-toxicology.tex`
CH-07. Rubaiyat, Tamam Shud Slip, and Cipher Material -> `manuscript/chapters/07-rubaiyat-cipher.tex`
CH-08. Witnesses, Contacts, and Social Network -> `manuscript/chapters/08-social-network.tex`
CH-09. Historical and Institutional Context -> `manuscript/chapters/09-historical-context.tex`
CH-10. Intelligence-Related Hypotheses -> `manuscript/chapters/10-intelligence-hypotheses.tex`
CH-11. Alternative Explanatory Models -> `manuscript/chapters/11-alternative-models.tex`
CH-12. Findings, Unknowns, and Future Research -> `manuscript/chapters/12-findings-unknowns.tex`

## Intelligence-Dossier Sequence

The manuscript should move from method, to facts, to context, to structured assessment, to findings. It should not open with mystery-story framing or unresolved speculation.

## Chapter Plans

### CH-01 - Executive Assessment
- Purpose: State the dossier's key judgments, evidence posture, confidence levels, and unresolved issues.
- Key findings: Exact cause of death remains unresolved; Webb attribution is a strong researcher/lab lead pending official confirmation; poisoning/intelligence claims remain unproven; custody gaps limit later interpretations.
- Evidence inputs: verification matrix; analytical confidence register; Mission 11 OSINT summary; decision log; physical and medical summaries
- Tables needed: Key judgments and confidence table; major intelligence gaps table
- Figures needed: None required; optional evidence-map schematic after source permissions review
- Unresolved gaps: Official SAPOL/coroner identification; complete toxicology/lab records; exhibit custody; Mission 10 structured registers not yet integrated as project files
- Confidence: Moderate
- Source files: `research/verification/verification_summary.md; research/verification/analytical_confidence_register.csv; research/osint/executive_summary.md; research/database/decision_log.csv`

### CH-02 - Methodology and Evidence Standards
- Purpose: Define source hierarchy, verification status, confidence language, claim handling, and end-reference policy.
- Key findings: Prior analysis must remain a claim source only; official/primary records outrank later commentary; end references should carry citations while prose uses evidence IDs where needed.
- Evidence inputs: decision log; verification workflow; source transparency policy; Mission 2-4 summaries
- Tables needed: Evidence hierarchy; verification status definitions; confidence scale
- Figures needed: Research workflow diagram optional
- Unresolved gaps: Final house style for visible evidence IDs in prose
- Confidence: High
- Source files: `documentation/workflows/VERIFICATION_WORKFLOW.md; documentation/governance/SOURCE_TRANSPARENCY_POLICY.md; research/database/decision_log.csv; research/verification/verification_matrix.csv`

### CH-03 - Case Chronology
- Purpose: Present the conservative master chronology with uncertainty and source mapping preserved.
- Key findings: 24 admitted events; 11 verified; 11 partially verified; major gaps include final movements, ticket purchaser identity, exact death time, and Rubaiyat/suitcase recovery sequence.
- Evidence inputs: chronology master; chronology uncertainties; event-source map; verification matrix
- Tables needed: timeline_ready_for_latex.tex; chronology uncertainty table
- Figures needed: Map of Somerton Beach, Adelaide Railway Station, Henley Beach and Glenelg only after coordinates/source rights are settled
- Unresolved gaps: Exact movements between Adelaide transport evidence and beach sightings; date/time of Tamam Shud slip discovery
- Confidence: High for discovery events; Moderate for pre-discovery movements
- Source files: `research/chronology/chronology_master.csv; research/chronology/chronology_uncertainties.csv; research/chronology/event_source_map.csv; manuscript/tables/timeline_ready_for_latex.tex`

### CH-04 - Identity and Biographical Reconstruction
- Purpose: Separate verified unidentified-decedent evidence from conditional Webb attribution and biographical leads.
- Key findings: Primary archive supports the unknown man's physical identifiers and possessions; Mission 11 upgrades Webb to a strong researcher/lab lead, not official closure.
- Evidence inputs: victim profile; movement reconstruction; possession inventory; forensic identifiers; OSINT Webb/DNA findings
- Tables needed: Movement reconstruction; possession inventory; forensic identifiers; conditional Webb evidence table
- Figures needed: Death mask/bust, fingerprint chart, tooth chart, Webb/family photographs only if rights and source status are resolved
- Unresolved gaps: Official coroner/SAPOL identity finding; DNA lab report; full Webb civil/court records; body-hair/remains match
- Confidence: High for physical identifiers; Moderate for Webb attribution; Unknown for official identification
- Source files: `research/victimology/victim_profile.md; research/victimology/movement_reconstruction.csv; research/victimology/possession_inventory.csv; research/forensic_medical/forensic_identifiers_register.csv; research/osint/newly_identified_evidence.csv`

### CH-05 - Scene, Body, and Physical Evidence
- Purpose: Describe scene observations, physical exhibits, clothing, suitcase material, and chain-of-custody limits.
- Key findings: Body/property existence layer is strong; custody trail is fragmentary for most objects; no item currently has complete custody confidence.
- Evidence inputs: physical evidence catalogue; scene reconstruction database; chain-of-custody confidence matrix; exhibit index; document page index
- Tables needed: physical_evidence_catalogue_ready_for_latex.tex; scene_reconstruction_ready_for_latex.tex; chain_of_custody_ready_for_latex.tex; exhibit index table
- Figures needed: Scene map; body/property photographs; suitcase photographs; clothing images only after rights and quality review
- Unresolved gaps: Current custodian of many exhibits; full suitcase inventory; sand/vegetation/fibre preservation; cigarette collection/examination
- Confidence: Moderate-High for object existence; Low-Moderate for custody continuity
- Source files: `research/physical_evidence/physical_evidence_catalogue.csv; research/physical_evidence/scene_reconstruction_database.csv; research/physical_evidence/chain_of_custody_confidence_matrix.csv; research/indexes/exhibit_index.csv`

### CH-06 - Forensic Medical and Toxicology Assessment
- Purpose: Present documented medical observations, toxicology testimony, time-of-death statements, and unresolved cause-of-death issues.
- Key findings: No common poison was detected in submitted specimens; this does not prove no poison was present; exact cause of death remains undetermined in the acquired record.
- Evidence inputs: medical transcriptions; medical observation register; toxicology register; time-of-death register; medical uncertainties
- Tables needed: medical_observations_ready_for_latex.tex; toxicology_ready_for_latex.tex; time-of-death table; medical uncertainty table
- Figures needed: None required unless autopsy diagrams or medical exhibits become rights-cleared
- Unresolved gaps: Complete lab report; exact Hicks terminology; retained sample status; alcohol testing status; modern forensic review
- Confidence: High for recorded observations; Moderate for toxicology limitations; Unknown for cause
- Source files: `research/forensic_medical/medical_observation_register.csv; research/forensic_medical/toxicology_register.csv; research/forensic_medical/time_of_death_register.csv; research/forensic_medical/medical_uncertainties.csv`

### CH-07 - Rubaiyat, Tamam Shud Slip, and Cipher Material
- Purpose: Handle the book, slip, markings/code, phone-number lead, Boxall/Jestyn material, and interpretation limits.
- Key findings: The slip/book/code cluster is central documentary evidence but its meaning remains unresolved; contemporary reporting strengthens chronology but not espionage interpretation.
- Evidence inputs: evidence register; physical evidence catalogue; OSINT Trove findings; witness/exhibit index; verification matrix
- Tables needed: Rubaiyat evidence chronology; documentary-custody table; code-interpretation status table
- Figures needed: Tamam Shud slip image; Rubaiyat code image; book comparison image only from rights-cleared sources
- Unresolved gaps: Original book custody; paper/print comparison records; phone-number police notes; high-resolution image provenance; accepted cryptanalytic result absent
- Confidence: High for existence of artefact cluster; Low for interpretation
- Source files: `research/database/evidence_register.csv; research/physical_evidence/physical_evidence_catalogue.csv; research/osint/newly_identified_evidence.csv; research/indexes/exhibit_index.csv`

### CH-08 - Witnesses, Contacts, and Social Network
- Purpose: Present witness evidence, contact leads, relationship map, and reliability constraints without assigning motive.
- Key findings: Witnesses support discovery and some evening sightings, but identity continuity and memory limits are material; Thomson/Boxall/Webb relationship claims require careful source separation.
- Evidence inputs: witness index; cross-reference map; relationship map; person register; transcription queue
- Tables needed: witness_index_ready_for_latex.tex; witness reliability table; relationship map table
- Figures needed: Network diagram optional; no family/person photographs until rights-cleared and evidentiary relevance is established
- Unresolved gaps: Manual transcription of priority pages; original police statements; Thomson interview notes; full Boxall/Jestyn source trail
- Confidence: Moderate
- Source files: `research/indexes/witness_index.csv; research/indexes/cross_reference_map.csv; research/victimology/relationship_map.csv; research/database/person_register.csv`

### CH-09 - Historical and Institutional Context
- Purpose: Explain late-1940s policing, transport, identity systems, forensic capability, media environment, and Cold War setting as context only.
- Key findings: Cold War and Woomera/ASIO context are historically real but not direct case evidence; pre-digital identity and forensic limitations explain uncertainty without proving clandestine activity.
- Evidence inputs: downloaded Mission 10 contextual report; source register; Mission 11 current-status layer; bibliography
- Tables needed: Context relevance table; capability-vs-case-linkage table
- Figures needed: Institutional timeline optional
- Unresolved gaps: Mission 10 context/ACH outputs need to be converted into project CSV/MD registers before final drafting
- Confidence: High for broad context; Low for direct case linkage
- Source files: `/Users/mohnish/Downloads/deep-research-report.md; research/database/source_register.csv; research/osint/source_register_mission11.csv`

### CH-10 - Intelligence-Related Hypotheses
- Purpose: Assess intelligence-related hypotheses using structured analytic language and strict source-weighting.
- Key findings: Espionage remains historically possible but evidentially weak; no acquired case-specific intelligence-service linkage has been found.
- Evidence inputs: hypothesis register; analytical confidence register; Mission 10 report; OSINT conflicts/gaps; verification corrections
- Tables needed: Intelligence hypothesis evidence table; source reliability and diagnosticity table
- Figures needed: None required
- Unresolved gaps: No project-native ACH/intelligence register files; ASIO/MI5/other archive search logs not complete
- Confidence: Very Low for direct intelligence involvement; High for contextual plausibility
- Source files: `research/database/hypothesis_register.csv; research/verification/analytical_confidence_register.csv; research/osint/intelligence_gaps_mission11.csv; /Users/mohnish/Downloads/deep-research-report.md`

### CH-11 - Alternative Explanatory Models
- Purpose: Compare natural death, accidental poisoning, suicide, homicide, espionage, and unknown/undetermined using ACH-style evidence tables.
- Key findings: Unknown/undetermined best preserves the current evidence posture; poisoning, suicide, homicide and espionage remain possible but under-evidenced at different points.
- Evidence inputs: verification matrix; hypothesis register; analytical confidence register; medical/physical/victimology layers; Mission 10 report
- Tables needed: ACH table; key assumptions check; indicators and signposts; evidence-weight matrix
- Figures needed: Argument map optional
- Unresolved gaps: Structured analytic registers should be generated from Mission 10 background before final prose
- Confidence: Moderate for undetermined posture; Low for specific explanatory models
- Source files: `research/verification/verification_matrix.csv; research/database/hypothesis_register.csv; research/forensic_medical/forensic_medical_summary.md; research/physical_evidence/physical_evidence_summary.md; /Users/mohnish/Downloads/deep-research-report.md`

### CH-12 - Findings, Unknowns, and Future Research
- Purpose: Close with established facts, supported inferences, working hypotheses, speculation exclusions, and prioritized intelligence requirements.
- Key findings: The dossier should publish as a versioned research project with explicit gaps, corrigible findings, and future acquisition targets.
- Evidence inputs: intelligence gaps; research questions; OSINT gaps; physical/medical uncertainties; release strategy
- Tables needed: Priority intelligence requirements; excluded/downgraded claims; future acquisition plan
- Figures needed: None required
- Unresolved gaps: Final readiness depends on integrating Mission 10 structured registers and completing references
- Confidence: High for gap register; Moderate for research prioritization
- Source files: `research/database/intelligence_gap_register.csv; research/database/research_question_register.csv; research/osint/intelligence_gaps_mission11.csv; research/physical_evidence/physical_evidence_uncertainties.csv; documentation/release_strategy.md`

## Duplicate Material To Merge

- Physical evidence, exhibit index, and possession inventory overlap: merge object descriptions in Chapter 5 and reserve Chapter 4 for identity/biographical relevance.
- Medical observations and toxicology registers overlap: Chapter 6 should separate observation, test, limitation, and uncertainty instead of repeating testimony chronologically.
- Chronology and movement reconstruction overlap: Chapter 3 should carry case chronology; Chapter 4 should cite only movements relevant to identity/victimology.
- Rubaiyat/code material appears in evidence, physical evidence, OSINT, and witness indexes: Chapter 7 should be the single interpretive home.
- Intelligence gaps, research questions, OSINT gaps, and physical/medical uncertainties overlap: consolidate in Chapter 12 with source-specific appendix references.
- Mission 10 context and Mission 11 OSINT both address Webb/identity status: use Mission 11 as current-status control and Mission 10 as contextual background only.

## Prior PDF Treatment

The old PDF analysis may be cited only as an internal prior-assessment source showing what claims were extracted for verification. It must not be used as evidence for factual assertions unless a claim has independent source support in the verification matrix or later registers.

## Manuscript Gatekeeping Rules

- Established fact: directly supported by primary/official or high-quality contemporary evidence.
- Supported inference: clearly linked to evidence but not directly observed.
- Working hypothesis: plausible explanatory model awaiting diagnostic evidence.
- Speculation: excluded from main findings; may appear only in a controlled prior-claims or historiography discussion.
- Intelligence gap: unanswered question requiring further source acquisition or analysis.
