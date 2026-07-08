#!/usr/bin/env python3
"""Generate Mission 12 manuscript blueprint artifacts."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "manuscript_blueprint"
OUT.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


chapters = [
    {
        "chapter_id": "CH-01",
        "latex_file": "manuscript/chapters/01-executive-assessment.tex",
        "title": "Executive Assessment",
        "purpose": "State the dossier's key judgments, evidence posture, confidence levels, and unresolved issues.",
        "key_findings": "Exact cause of death remains unresolved; Webb attribution is a strong researcher/lab lead pending official confirmation; poisoning/intelligence claims remain unproven; custody gaps limit later interpretations.",
        "evidence_inputs": "verification matrix; analytical confidence register; Mission 11 OSINT summary; decision log; physical and medical summaries",
        "tables_needed": "Key judgments and confidence table; major intelligence gaps table",
        "figures_needed": "None required; optional evidence-map schematic after source permissions review",
        "unresolved_gaps": "Official SAPOL/coroner identification; complete toxicology/lab records; exhibit custody; Mission 10 structured registers not yet integrated as project files",
        "confidence_level": "Moderate",
        "source_files": "research/verification/verification_summary.md; research/verification/analytical_confidence_register.csv; research/osint/executive_summary.md; research/database/decision_log.csv",
    },
    {
        "chapter_id": "CH-02",
        "latex_file": "manuscript/chapters/02-methodology.tex",
        "title": "Methodology and Evidence Standards",
        "purpose": "Define source hierarchy, verification status, confidence language, claim handling, and end-reference policy.",
        "key_findings": "Prior analysis must remain a claim source only; official/primary records outrank later commentary; end references should carry citations while prose uses evidence IDs where needed.",
        "evidence_inputs": "decision log; verification workflow; source transparency policy; Mission 2-4 summaries",
        "tables_needed": "Evidence hierarchy; verification status definitions; confidence scale",
        "figures_needed": "Research workflow diagram optional",
        "unresolved_gaps": "Final house style for visible evidence IDs in prose",
        "confidence_level": "High",
        "source_files": "documentation/workflows/VERIFICATION_WORKFLOW.md; documentation/governance/SOURCE_TRANSPARENCY_POLICY.md; research/database/decision_log.csv; research/verification/verification_matrix.csv",
    },
    {
        "chapter_id": "CH-03",
        "latex_file": "manuscript/chapters/03-case-chronology.tex",
        "title": "Case Chronology",
        "purpose": "Present the conservative master chronology with uncertainty and source mapping preserved.",
        "key_findings": "24 admitted events; 11 verified; 11 partially verified; major gaps include final movements, ticket purchaser identity, exact death time, and Rubaiyat/suitcase recovery sequence.",
        "evidence_inputs": "chronology master; chronology uncertainties; event-source map; verification matrix",
        "tables_needed": "timeline_ready_for_latex.tex; chronology uncertainty table",
        "figures_needed": "Map of Somerton Beach, Adelaide Railway Station, Henley Beach and Glenelg only after coordinates/source rights are settled",
        "unresolved_gaps": "Exact movements between Adelaide transport evidence and beach sightings; date/time of Tamam Shud slip discovery",
        "confidence_level": "High for discovery events; Moderate for pre-discovery movements",
        "source_files": "research/chronology/chronology_master.csv; research/chronology/chronology_uncertainties.csv; research/chronology/event_source_map.csv; manuscript/tables/timeline_ready_for_latex.tex",
    },
    {
        "chapter_id": "CH-04",
        "latex_file": "manuscript/chapters/04-identity-biography.tex",
        "title": "Identity and Biographical Reconstruction",
        "purpose": "Separate verified unidentified-decedent evidence from conditional Webb attribution and biographical leads.",
        "key_findings": "Primary archive supports the unknown man's physical identifiers and possessions; Mission 11 upgrades Webb to a strong researcher/lab lead, not official closure.",
        "evidence_inputs": "victim profile; movement reconstruction; possession inventory; forensic identifiers; OSINT Webb/DNA findings",
        "tables_needed": "Movement reconstruction; possession inventory; forensic identifiers; conditional Webb evidence table",
        "figures_needed": "Death mask/bust, fingerprint chart, tooth chart, Webb/family photographs only if rights and source status are resolved",
        "unresolved_gaps": "Official coroner/SAPOL identity finding; DNA lab report; full Webb civil/court records; body-hair/remains match",
        "confidence_level": "High for physical identifiers; Moderate for Webb attribution; Unknown for official identification",
        "source_files": "research/victimology/victim_profile.md; research/victimology/movement_reconstruction.csv; research/victimology/possession_inventory.csv; research/forensic_medical/forensic_identifiers_register.csv; research/osint/newly_identified_evidence.csv",
    },
    {
        "chapter_id": "CH-05",
        "latex_file": "manuscript/chapters/05-scene-forensics.tex",
        "title": "Scene, Body, and Physical Evidence",
        "purpose": "Describe scene observations, physical exhibits, clothing, suitcase material, and chain-of-custody limits.",
        "key_findings": "Body/property existence layer is strong; custody trail is fragmentary for most objects; no item currently has complete custody confidence.",
        "evidence_inputs": "physical evidence catalogue; scene reconstruction database; chain-of-custody confidence matrix; exhibit index; document page index",
        "tables_needed": "physical_evidence_catalogue_ready_for_latex.tex; scene_reconstruction_ready_for_latex.tex; chain_of_custody_ready_for_latex.tex; exhibit index table",
        "figures_needed": "Scene map; body/property photographs; suitcase photographs; clothing images only after rights and quality review",
        "unresolved_gaps": "Current custodian of many exhibits; full suitcase inventory; sand/vegetation/fibre preservation; cigarette collection/examination",
        "confidence_level": "Moderate-High for object existence; Low-Moderate for custody continuity",
        "source_files": "research/physical_evidence/physical_evidence_catalogue.csv; research/physical_evidence/scene_reconstruction_database.csv; research/physical_evidence/chain_of_custody_confidence_matrix.csv; research/indexes/exhibit_index.csv",
    },
    {
        "chapter_id": "CH-06",
        "latex_file": "manuscript/chapters/06-toxicology.tex",
        "title": "Forensic Medical and Toxicology Assessment",
        "purpose": "Present documented medical observations, toxicology testimony, time-of-death statements, and unresolved cause-of-death issues.",
        "key_findings": "No common poison was detected in submitted specimens; this does not prove no poison was present; exact cause of death remains undetermined in the acquired record.",
        "evidence_inputs": "medical transcriptions; medical observation register; toxicology register; time-of-death register; medical uncertainties",
        "tables_needed": "medical_observations_ready_for_latex.tex; toxicology_ready_for_latex.tex; time-of-death table; medical uncertainty table",
        "figures_needed": "None required unless autopsy diagrams or medical exhibits become rights-cleared",
        "unresolved_gaps": "Complete lab report; exact Hicks terminology; retained sample status; alcohol testing status; modern forensic review",
        "confidence_level": "High for recorded observations; Moderate for toxicology limitations; Unknown for cause",
        "source_files": "research/forensic_medical/medical_observation_register.csv; research/forensic_medical/toxicology_register.csv; research/forensic_medical/time_of_death_register.csv; research/forensic_medical/medical_uncertainties.csv",
    },
    {
        "chapter_id": "CH-07",
        "latex_file": "manuscript/chapters/07-rubaiyat-cipher.tex",
        "title": "Rubaiyat, Tamam Shud Slip, and Cipher Material",
        "purpose": "Handle the book, slip, markings/code, phone-number lead, Boxall/Jestyn material, and interpretation limits.",
        "key_findings": "The slip/book/code cluster is central documentary evidence but its meaning remains unresolved; contemporary reporting strengthens chronology but not espionage interpretation.",
        "evidence_inputs": "evidence register; physical evidence catalogue; OSINT Trove findings; witness/exhibit index; verification matrix",
        "tables_needed": "Rubaiyat evidence chronology; documentary-custody table; code-interpretation status table",
        "figures_needed": "Tamam Shud slip image; Rubaiyat code image; book comparison image only from rights-cleared sources",
        "unresolved_gaps": "Original book custody; paper/print comparison records; phone-number police notes; high-resolution image provenance; accepted cryptanalytic result absent",
        "confidence_level": "High for existence of artefact cluster; Low for interpretation",
        "source_files": "research/database/evidence_register.csv; research/physical_evidence/physical_evidence_catalogue.csv; research/osint/newly_identified_evidence.csv; research/indexes/exhibit_index.csv",
    },
    {
        "chapter_id": "CH-08",
        "latex_file": "manuscript/chapters/08-social-network.tex",
        "title": "Witnesses, Contacts, and Social Network",
        "purpose": "Present witness evidence, contact leads, relationship map, and reliability constraints without assigning motive.",
        "key_findings": "Witnesses support discovery and some evening sightings, but identity continuity and memory limits are material; Thomson/Boxall/Webb relationship claims require careful source separation.",
        "evidence_inputs": "witness index; cross-reference map; relationship map; person register; transcription queue",
        "tables_needed": "witness_index_ready_for_latex.tex; witness reliability table; relationship map table",
        "figures_needed": "Network diagram optional; no family/person photographs until rights-cleared and evidentiary relevance is established",
        "unresolved_gaps": "Manual transcription of priority pages; original police statements; Thomson interview notes; full Boxall/Jestyn source trail",
        "confidence_level": "Moderate",
        "source_files": "research/indexes/witness_index.csv; research/indexes/cross_reference_map.csv; research/victimology/relationship_map.csv; research/database/person_register.csv",
    },
    {
        "chapter_id": "CH-09",
        "latex_file": "manuscript/chapters/09-historical-context.tex",
        "title": "Historical and Institutional Context",
        "purpose": "Explain late-1940s policing, transport, identity systems, forensic capability, media environment, and Cold War setting as context only.",
        "key_findings": "Cold War and Woomera/ASIO context are historically real but not direct case evidence; pre-digital identity and forensic limitations explain uncertainty without proving clandestine activity.",
        "evidence_inputs": "downloaded Mission 10 contextual report; source register; Mission 11 current-status layer; bibliography",
        "tables_needed": "Context relevance table; capability-vs-case-linkage table",
        "figures_needed": "Institutional timeline optional",
        "unresolved_gaps": "Mission 10 context/ACH outputs need to be converted into project CSV/MD registers before final drafting",
        "confidence_level": "High for broad context; Low for direct case linkage",
        "source_files": "/Users/mohnish/Downloads/deep-research-report.md; research/database/source_register.csv; research/osint/source_register_mission11.csv",
    },
    {
        "chapter_id": "CH-10",
        "latex_file": "manuscript/chapters/10-intelligence-hypotheses.tex",
        "title": "Intelligence-Related Hypotheses",
        "purpose": "Assess intelligence-related hypotheses using structured analytic language and strict source-weighting.",
        "key_findings": "Espionage remains historically possible but evidentially weak; no acquired case-specific intelligence-service linkage has been found.",
        "evidence_inputs": "hypothesis register; analytical confidence register; Mission 10 report; OSINT conflicts/gaps; verification corrections",
        "tables_needed": "Intelligence hypothesis evidence table; source reliability and diagnosticity table",
        "figures_needed": "None required",
        "unresolved_gaps": "No project-native ACH/intelligence register files; ASIO/MI5/other archive search logs not complete",
        "confidence_level": "Very Low for direct intelligence involvement; High for contextual plausibility",
        "source_files": "research/database/hypothesis_register.csv; research/verification/analytical_confidence_register.csv; research/osint/intelligence_gaps_mission11.csv; /Users/mohnish/Downloads/deep-research-report.md",
    },
    {
        "chapter_id": "CH-11",
        "latex_file": "manuscript/chapters/11-alternative-models.tex",
        "title": "Alternative Explanatory Models",
        "purpose": "Compare natural death, accidental poisoning, suicide, homicide, espionage, and unknown/undetermined using ACH-style evidence tables.",
        "key_findings": "Unknown/undetermined best preserves the current evidence posture; poisoning, suicide, homicide and espionage remain possible but under-evidenced at different points.",
        "evidence_inputs": "verification matrix; hypothesis register; analytical confidence register; medical/physical/victimology layers; Mission 10 report",
        "tables_needed": "ACH table; key assumptions check; indicators and signposts; evidence-weight matrix",
        "figures_needed": "Argument map optional",
        "unresolved_gaps": "Structured analytic registers should be generated from Mission 10 background before final prose",
        "confidence_level": "Moderate for undetermined posture; Low for specific explanatory models",
        "source_files": "research/verification/verification_matrix.csv; research/database/hypothesis_register.csv; research/forensic_medical/forensic_medical_summary.md; research/physical_evidence/physical_evidence_summary.md; /Users/mohnish/Downloads/deep-research-report.md",
    },
    {
        "chapter_id": "CH-12",
        "latex_file": "manuscript/chapters/12-findings-unknowns.tex",
        "title": "Findings, Unknowns, and Future Research",
        "purpose": "Close with established facts, supported inferences, working hypotheses, speculation exclusions, and prioritized intelligence requirements.",
        "key_findings": "The dossier should publish as a versioned research project with explicit gaps, corrigible findings, and future acquisition targets.",
        "evidence_inputs": "intelligence gaps; research questions; OSINT gaps; physical/medical uncertainties; release strategy",
        "tables_needed": "Priority intelligence requirements; excluded/downgraded claims; future acquisition plan",
        "figures_needed": "None required",
        "unresolved_gaps": "Final readiness depends on integrating Mission 10 structured registers and completing references",
        "confidence_level": "High for gap register; Moderate for research prioritization",
        "source_files": "research/database/intelligence_gap_register.csv; research/database/research_question_register.csv; research/osint/intelligence_gaps_mission11.csv; research/physical_evidence/physical_evidence_uncertainties.csv; documentation/release_strategy.md",
    },
]

output_map = [
    ("verification_matrix.csv", "CH-01; CH-02; CH-03; CH-06; CH-10; CH-11", "Claim-status backbone and downgrade guardrail"),
    ("claim_revision_register.csv", "CH-02; CH-12", "Revision language and excluded/downgraded claims"),
    ("conflicting_sources_register.csv", "CH-03; CH-06; CH-12", "Conflicts to preserve rather than smooth"),
    ("analytical_confidence_register.csv", "CH-01; CH-10; CH-11", "Analytical conclusions and confidence reasons"),
    ("chronology_master.csv", "CH-03", "Master event sequence"),
    ("chronology_uncertainties.csv", "CH-03; CH-12", "Timeline gaps and conflicts"),
    ("witness_index.csv", "CH-08", "Witness/declarant layer"),
    ("exhibit_index.csv", "CH-05; CH-07", "Exhibit/property references"),
    ("document_page_index.csv", "CH-02; CH-05; CH-08", "Page-level source control"),
    ("victim_profile.md", "CH-04", "Victimology narrative source, not final prose"),
    ("movement_reconstruction.csv", "CH-03; CH-04", "Movement table"),
    ("possession_inventory.csv", "CH-04; CH-05", "Possession inventory"),
    ("relationship_map.csv", "CH-08", "Relationship/contact structure"),
    ("medical_observation_register.csv", "CH-06", "Medical observations"),
    ("toxicology_register.csv", "CH-06; CH-11", "Toxicology status"),
    ("time_of_death_register.csv", "CH-03; CH-06", "Timing statements"),
    ("forensic_identifiers_register.csv", "CH-04; CH-06", "Fingerprints/dental/death mask identifiers"),
    ("physical_evidence_catalogue.csv", "CH-05; CH-07", "Museum-style evidence catalogue"),
    ("scene_reconstruction_database.csv", "CH-05", "Scene components"),
    ("chain_of_custody_confidence_matrix.csv", "CH-05; CH-12", "Custody confidence"),
    ("source_register.csv", "CH-02; appendices", "Main source metadata"),
    ("source_register_mission11.csv", "CH-04; CH-07; CH-09; CH-12", "OSINT source update layer"),
    ("newly_identified_evidence.csv", "CH-04; CH-07; CH-09; CH-12", "Mission 11 findings"),
    ("evidence_reliability_matrix.csv", "CH-02; CH-09; CH-12", "OSINT source quality"),
    ("decision_log.csv", "CH-02; CH-12; appendices", "Methodological decisions"),
    ("deep-research-report.md", "CH-09; CH-10; CH-11", "Contextual and structured analytic background only"),
]

dependencies = [
    ("CH-02", "None", "Write first after blueprint", "Sets terminology and claim discipline for every chapter."),
    ("CH-03", "CH-02", "Write before identity, scene and analytic chapters", "All later reconstruction chapters rely on chronology IDs and uncertainty labels."),
    ("CH-04", "CH-02; CH-03", "Write after chronology", "Identity claims depend on chronology and OSINT guardrail."),
    ("CH-05", "CH-02; CH-03", "Write after chronology", "Scene/exhibit handling depends on discovery sequence."),
    ("CH-06", "CH-02; CH-03", "Write after chronology", "Medical timing statements must be anchored to the event sequence."),
    ("CH-07", "CH-02; CH-03; CH-05; CH-08", "Write after scene and witness layers", "Rubaiyat/cipher interpretation depends on exhibit custody and witnesses."),
    ("CH-08", "CH-02; CH-03", "Write before Rubaiyat and models", "Social-network constraints shape later hypotheses."),
    ("CH-09", "CH-02", "Write after evidence chapters or in parallel as context", "Must remain context, not proof."),
    ("CH-10", "CH-02; CH-04; CH-05; CH-07; CH-09", "Write after factual and context chapters", "Intelligence hypotheses require prior fact/context separation."),
    ("CH-11", "CH-02; CH-03; CH-04; CH-05; CH-06; CH-07; CH-08; CH-09; CH-10", "Write near the end", "ACH-style comparison needs all evidence clusters."),
    ("CH-01", "CH-02 through CH-12", "Draft last despite appearing first", "Executive assessment must reflect final chapter evidence."),
    ("CH-12", "CH-02 through CH-11", "Draft immediately before executive assessment", "Findings/unknowns synthesize the full dossier."),
]

tables = [
    ("TAB-001", "Key judgments and confidence", "CH-01", "research/verification/analytical_confidence_register.csv; research/osint/executive_summary.md", "Needs generation", "Core assessment table"),
    ("TAB-002", "Evidence hierarchy and confidence definitions", "CH-02", "documentation/workflows/VERIFICATION_WORKFLOW.md; research/database/decision_log.csv", "Needs generation", "Controls wording"),
    ("TAB-003", "Master chronology", "CH-03", "manuscript/tables/timeline_ready_for_latex.tex", "Available", "Existing LaTeX table"),
    ("TAB-004", "Chronology uncertainty register", "CH-03", "research/chronology/chronology_uncertainties.csv", "Needs generation", "Preserve contested entries"),
    ("TAB-005", "Movement reconstruction", "CH-04", "manuscript/tables/movement_reconstruction_ready_for_latex.tex", "Available", "Conditional identity caveats needed"),
    ("TAB-006", "Possession inventory", "CH-04", "manuscript/tables/possession_inventory_ready_for_latex.tex", "Available", "Use with source IDs"),
    ("TAB-007", "Forensic identifiers", "CH-04; CH-06", "manuscript/tables/forensic_identifiers_ready_for_latex.tex", "Available", "Fingerprints/dental/death mask"),
    ("TAB-008", "Physical evidence catalogue", "CH-05", "manuscript/tables/physical_evidence_catalogue_ready_for_latex.tex", "Available", "Museum-style exhibit table"),
    ("TAB-009", "Scene reconstruction", "CH-05", "manuscript/tables/scene_reconstruction_ready_for_latex.tex", "Available", "No narrative smoothing"),
    ("TAB-010", "Chain of custody confidence", "CH-05", "manuscript/tables/chain_of_custody_ready_for_latex.tex", "Available", "Important weight-control table"),
    ("TAB-011", "Medical observations", "CH-06", "manuscript/tables/medical_observations_ready_for_latex.tex", "Available", "Observation not interpretation"),
    ("TAB-012", "Toxicology register", "CH-06", "manuscript/tables/toxicology_ready_for_latex.tex", "Available", "Separate not detected from not present"),
    ("TAB-013", "Witness index", "CH-08", "manuscript/tables/witness_index_ready_for_latex.tex", "Available", "Add reliability classification later"),
    ("TAB-014", "Rubaiyat documentary evidence table", "CH-07", "research/physical_evidence/physical_evidence_catalogue.csv; research/osint/newly_identified_evidence.csv", "Needs generation", "Book/slip/code custody and interpretation"),
    ("TAB-015", "Context relevance matrix", "CH-09", "/Users/mohnish/Downloads/deep-research-report.md", "Needs project-native source conversion", "Context only"),
    ("TAB-016", "Intelligence hypothesis evidence table", "CH-10", "research/database/hypothesis_register.csv; research/verification/analytical_confidence_register.csv", "Needs generation", "Do not overstate espionage"),
    ("TAB-017", "ACH matrix", "CH-11", "/Users/mohnish/Downloads/deep-research-report.md; research/verification/verification_matrix.csv", "Needs project-native source conversion", "Structured analytic assessment"),
    ("TAB-018", "Priority intelligence requirements", "CH-12", "research/database/intelligence_gap_register.csv; research/osint/intelligence_gaps_mission11.csv", "Needs generation", "Future research agenda"),
    ("TAB-019", "Excluded/downgraded claims", "CH-12", "research/manuscript_blueprint/excluded_or_downgraded_claims.csv", "Generated by Mission 12", "Manuscript gatekeeping"),
]

figures = [
    ("FIGPLAN-001", "Case location map", "CH-03; CH-05", "Future generated/rights-cleared map", "Required eventually", "Must use exact locations and avoid unsourced route lines."),
    ("FIGPLAN-002", "Somerton Man photograph or reconstruction", "CH-04", "FIG-0001", "Rights unresolved", "Use only if custodian/licensing is clear."),
    ("FIGPLAN-003", "Death mask/bust", "CH-04", "FIG-0004", "Rights unresolved", "Central to DNA/hair discussion if permitted."),
    ("FIGPLAN-004", "Fingerprint chart", "CH-04", "FIG-0007", "Rights unresolved", "Identifier figure only."),
    ("FIGPLAN-005", "Tooth chart", "CH-04", "FIG-0008", "Rights unresolved", "Identifier figure only."),
    ("FIGPLAN-006", "Scene/body-position schematic", "CH-05", "research/physical_evidence/scene_reconstruction_database.csv", "Needs generation", "Must be schematic and source-labeled."),
    ("FIGPLAN-007", "Tamam Shud slip", "CH-07", "FIG-0002", "Rights unresolved", "Do not redraw as evidence substitute."),
    ("FIGPLAN-008", "Rubaiyat code markings", "CH-07", "FIG-0003", "Rights unresolved", "Use original/high-res source where possible."),
    ("FIGPLAN-009", "Evidence graph / relationship network", "CH-08; CH-12", "research/indexes/cross_reference_map.csv; research/victimology/relationship_map.csv", "Optional generation", "Must distinguish confirmed links from leads."),
    ("FIGPLAN-010", "Research workflow diagram", "CH-02", "documentation/workflows", "Optional generation", "Useful for reproducibility."),
]

downgrades = [
    ("EXC-0001", "Poisoning by Digitalis/strophanthin/exotic agent", "Unsupported", "Exclude as factual claim; may appear only as historical hypothesis if sourced and clearly marked.", "research/verification/claim_revision_register.csv CRR-0008 to CRR-0010; research/forensic_medical/forensic_medical_summary.md", "CH-06; CH-11"),
    ("EXC-0002", "All poisons were ruled out", "Overstated", "Downgrade to: common poisons were not detected in submitted specimens.", "research/forensic_medical/toxicology_register.csv; CRR-0006 to CRR-0007", "CH-06"),
    ("EXC-0003", "Cause of death was known", "Unsupported/overstated", "Use: precise cause of death remained undetermined in available coronial material.", "CRR-0012; research/forensic_medical/medical_uncertainties.csv", "CH-06; CH-12"),
    ("EXC-0004", "Melbourne-Adelaide train-ticket claim", "Unsupported", "Remove unless future source directly supports it; use Adelaide-to-Henley Beach rail-ticket evidence.", "CRR-0018; CRR-0019", "CH-03"),
    ("EXC-0005", "Woomera/Maralinga as verified case locations", "Unsupported", "Move to historical context only; no direct case-location claim.", "conflicting_sources_register.csv CON-0004; Mission 10 contextual report", "CH-09; CH-10"),
    ("EXC-0006", "Espionage linkage as conclusion", "Unsupported", "Retain only as hypothesis/context; no direct intelligence-service linkage currently acquired.", "verification_summary.md; research/osint/mission_11_summary.md", "CH-10; CH-11"),
    ("EXC-0007", "Carl Webb identity officially solved", "Overstated/current-status conflict", "Use: researcher/lab-led Carl Webb attribution pending official coroner/SAPOL determination.", "research/database/decision_log.csv DEC-0009; research/osint/executive_summary.md", "CH-01; CH-04; CH-12"),
    ("EXC-0008", "Jessica Thomson shock/denial as established fact", "Unable to Verify", "Exclude unless direct interview notes or reliable transcript are acquired.", "CRR-0015", "CH-08"),
    ("EXC-0009", "Robin Thomson physical/DNA linkage", "Unsupported", "Exclude from factual narrative; may be listed as prior unsupported claim.", "CRR-0016; CRR-0017; CRR-0028", "CH-08; CH-11"),
    ("EXC-0010", "Clothing label removal intent/timing", "Partially verified but over-interpreted", "Use: identifying tags appeared removed; actor, timing and intent unknown.", "CRR-0038; CON-0002; research/physical_evidence/physical_evidence_summary.md", "CH-05"),
    ("EXC-0011", "Rubaiyat/code proves espionage", "Unsupported interpretation", "Use as documentary evidence with unresolved meaning.", "research/osint/mission_11_summary.md; research/physical_evidence/physical_evidence_summary.md", "CH-07; CH-10"),
    ("EXC-0012", "Isotope analysis as established evidence", "Not located/reliable", "Move to intelligence gap unless primary documentation is acquired.", "research/osint/mission_11_summary.md; research/osint/intelligence_gaps_mission11.csv", "CH-12"),
]

writing_order = [
    ("01", "Methodology and Evidence Standards", "Locks terminology before any fact chapter."),
    ("02", "Case Chronology", "Provides the time backbone for identity, scene, witness and medical material."),
    ("03", "Scene, Body, and Physical Evidence", "Establishes physical evidence before interpretation."),
    ("04", "Forensic Medical and Toxicology Assessment", "Clarifies cause-of-death limits before explanatory models."),
    ("05", "Identity and Biographical Reconstruction", "Can now separate physical identifiers from Webb attribution and OSINT caveats."),
    ("06", "Witnesses, Contacts, and Social Network", "Builds social/testimonial layer after event and evidence facts are fixed."),
    ("07", "Rubaiyat, Tamam Shud Slip, and Cipher Material", "Depends on physical custody and witness/contact records."),
    ("08", "Historical and Institutional Context", "Adds context after case facts are protected from context-driven overreach."),
    ("09", "Intelligence-Related Hypotheses", "Uses the evidence chapters plus context without concluding beyond evidence."),
    ("10", "Alternative Explanatory Models", "ACH-style comparison after all clusters are available."),
    ("11", "Findings, Unknowns, and Future Research", "Synthesizes the final confidence and gap posture."),
    ("12", "Executive Assessment", "Draft last; it is the front chapter but depends on all others."),
]

write_csv(
    OUT / "chapter_evidence_map.csv",
    [
        "chapter_id",
        "latex_file",
        "title",
        "purpose",
        "key_findings",
        "evidence_inputs",
        "tables_needed",
        "figures_needed",
        "unresolved_gaps",
        "confidence_level",
        "source_files",
    ],
    chapters,
)

write_csv(
    OUT / "chapter_dependency_map.csv",
    ["chapter_id", "dependencies", "writing_position", "reason"],
    [
        {
            "chapter_id": chapter_id,
            "dependencies": deps,
            "writing_position": position,
            "reason": reason,
        }
        for chapter_id, deps, position, reason in dependencies
    ],
)

write_csv(
    OUT / "excluded_or_downgraded_claims.csv",
    ["exclusion_id", "claim_or_topic", "status", "manuscript_instruction", "basis", "affected_chapters"],
    [
        {
            "exclusion_id": row[0],
            "claim_or_topic": row[1],
            "status": row[2],
            "manuscript_instruction": row[3],
            "basis": row[4],
            "affected_chapters": row[5],
        }
        for row in downgrades
    ],
)

write_csv(
    OUT / "table_and_figure_plan.csv",
    ["item_id", "description", "destination_chapter", "source", "status", "notes"],
    [
        {
            "item_id": row[0],
            "description": row[1],
            "destination_chapter": row[2],
            "source": row[3],
            "status": row[4],
            "notes": row[5],
        }
        for row in tables + figures
    ],
)

write_csv(
    OUT / "research_output_destination_map.csv",
    ["research_output", "destination_chapters", "use_in_manuscript"],
    [
        {
            "research_output": row[0],
            "destination_chapters": row[1],
            "use_in_manuscript": row[2],
        }
        for row in output_map
    ],
)

toc_lines = [
    "# Manuscript Blueprint",
    "",
    "Mission 12 converts the completed research database into a controlled LaTeX writing plan. It does not draft substantive chapter prose.",
    "",
    "## Final Table of Contents",
    "",
]
for chapter in chapters:
    toc_lines.append(f"{chapter['chapter_id']}. {chapter['title']} -> `{chapter['latex_file']}`")

toc_lines += [
    "",
    "## Intelligence-Dossier Sequence",
    "",
    "The manuscript should move from method, to facts, to context, to structured assessment, to findings. It should not open with mystery-story framing or unresolved speculation.",
    "",
    "## Chapter Plans",
    "",
]
for chapter in chapters:
    toc_lines += [
        f"### {chapter['chapter_id']} - {chapter['title']}",
        f"- Purpose: {chapter['purpose']}",
        f"- Key findings: {chapter['key_findings']}",
        f"- Evidence inputs: {chapter['evidence_inputs']}",
        f"- Tables needed: {chapter['tables_needed']}",
        f"- Figures needed: {chapter['figures_needed']}",
        f"- Unresolved gaps: {chapter['unresolved_gaps']}",
        f"- Confidence: {chapter['confidence_level']}",
        f"- Source files: `{chapter['source_files']}`",
        "",
    ]

toc_lines += [
    "## Duplicate Material To Merge",
    "",
    "- Physical evidence, exhibit index, and possession inventory overlap: merge object descriptions in Chapter 5 and reserve Chapter 4 for identity/biographical relevance.",
    "- Medical observations and toxicology registers overlap: Chapter 6 should separate observation, test, limitation, and uncertainty instead of repeating testimony chronologically.",
    "- Chronology and movement reconstruction overlap: Chapter 3 should carry case chronology; Chapter 4 should cite only movements relevant to identity/victimology.",
    "- Rubaiyat/code material appears in evidence, physical evidence, OSINT, and witness indexes: Chapter 7 should be the single interpretive home.",
    "- Intelligence gaps, research questions, OSINT gaps, and physical/medical uncertainties overlap: consolidate in Chapter 12 with source-specific appendix references.",
    "- Mission 10 context and Mission 11 OSINT both address Webb/identity status: use Mission 11 as current-status control and Mission 10 as contextual background only.",
    "",
    "## Prior PDF Treatment",
    "",
    "The old PDF analysis may be cited only as an internal prior-assessment source showing what claims were extracted for verification. It must not be used as evidence for factual assertions unless a claim has independent source support in the verification matrix or later registers.",
    "",
    "## Manuscript Gatekeeping Rules",
    "",
    "- Established fact: directly supported by primary/official or high-quality contemporary evidence.",
    "- Supported inference: clearly linked to evidence but not directly observed.",
    "- Working hypothesis: plausible explanatory model awaiting diagnostic evidence.",
    "- Speculation: excluded from main findings; may appear only in a controlled prior-claims or historiography discussion.",
    "- Intelligence gap: unanswered question requiring further source acquisition or analysis.",
]
(OUT / "manuscript_blueprint.md").write_text("\n".join(toc_lines) + "\n", encoding="utf-8")

writing_lines = [
    "# Manuscript Writing Order",
    "",
    "Write in evidence-dependency order, not table-of-contents order.",
    "",
]
for order, title, reason in writing_order:
    writing_lines.append(f"{order}. {title}: {reason}")

writing_lines += [
    "",
    "## Dependency Warnings",
    "",
    "- Do not draft the Executive Assessment until all body chapters have final confidence language.",
    "- Do not draft Intelligence-Related Hypotheses before the physical, medical, witness, Rubaiyat and context chapters are mapped.",
    "- Do not state Webb as officially identified unless a coroner/SAPOL record is acquired or the text explicitly says the attribution is researcher/lab-led and pending official determination.",
    "- Do not turn context into proof. Woomera, ASIO, Venona and Cold War material belong in context unless a case-specific record is found.",
]
(OUT / "manuscript_writing_order.md").write_text("\n".join(writing_lines) + "\n", encoding="utf-8")

refs_lines = [
    "# References Integration Plan",
    "",
    "The dossier should use end references only. Main text should avoid dense in-text citation strings and instead use controlled wording, source IDs where needed, and endnote/bibliography entries.",
    "",
    "## Source Integration Steps",
    "",
    "1. Normalize `research/database/source_register.csv` and `research/osint/source_register_mission11.csv` into `bibliography/references.bib`.",
    "2. Preserve document IDs such as `DOC-0001` in prose or tables only when they improve auditability.",
    "3. Use end references for public sources and appendix/source-register references for archival reproductions.",
    "4. Do not cite the prior PDF as evidence. Cite it only as the source of prior claims when discussing methodology.",
    "5. Add access dates for web sources and archival call numbers for primary records.",
    "6. Keep direct quotations short and only where exact wording affects interpretation.",
    "",
    "## Bibliography Classes",
    "",
    "- Primary archival/coronial/police records: highest-weight references.",
    "- Contemporary newspapers/legal notices: useful for chronology and public-record leads.",
    "- Official modern statements: use for current status and institutional position.",
    "- Researcher/lab participant accounts: important leads, not official closure unless corroborated.",
    "- Secondary synthesis/reporting: background and leads only.",
    "",
    "## Immediate Bibliography Tasks",
    "",
    "- Add Mission 11 ABC, Trove, State Records SA, Smithsonian and Astrea entries to `bibliography/references.bib`.",
    "- Create BibTeX keys that align with source IDs where practical.",
    "- Review existing bibliography for duplicate ABC/Trove/State Records entries before drafting.",
]
(OUT / "references_integration_plan.md").write_text("\n".join(refs_lines) + "\n", encoding="utf-8")

summary_lines = [
    "# Mission 12 Summary",
    "",
    "Mission 12 prepared the manuscript architecture without writing final chapters.",
    "",
    "## Outputs Created",
    "",
    "- `manuscript_blueprint.md`",
    "- `chapter_evidence_map.csv`",
    "- `chapter_dependency_map.csv`",
    "- `excluded_or_downgraded_claims.csv`",
    "- `table_and_figure_plan.csv`",
    "- `research_output_destination_map.csv`",
    "- `manuscript_writing_order.md`",
    "- `references_integration_plan.md`",
    "- `mission_12_summary.md`",
    "",
    "## Counts",
    "",
    f"- Final chapter count: {len(chapters)}",
    f"- Tables planned: {len(tables)}",
    f"- Figures planned: {len(figures)}",
    f"- Excluded/downgraded claim groups: {len(downgrades)}",
    f"- Research outputs mapped: {len(output_map)}",
    "",
    "## Manuscript Readiness",
    "",
    "Readiness for Mission 13: conditionally ready for controlled drafting. The factual/evidence chapters can begin once the writer follows the writing order and preserves uncertainty labels.",
    "",
    "## Remaining Dependencies",
    "",
    "- Convert the downloaded Mission 10 contextual/structured analytic report into project-native registers before final Chapter 9-11 drafting.",
    "- Integrate Mission 11 source records into the main bibliography.",
    "- Resolve image rights before inserting figures.",
    "- Keep Webb identity wording conditional until official SAPOL/coroner confirmation is acquired.",
    "- Use the old PDF only as prior-claim background, never as factual evidence.",
]
(OUT / "mission_12_summary.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

print(f"Mission 12 blueprint artifacts written to {OUT}")
