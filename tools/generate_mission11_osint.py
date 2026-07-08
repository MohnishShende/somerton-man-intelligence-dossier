#!/usr/bin/env python3
"""Generate Mission 11 OSINT expansion artifacts."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "osint"


def write_csv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


sources = [
    ["M11-SRC-0001", "SA Police report to coroner into Somerton Man case complete 'very soon'", "Ethan Rix", "ABC News", "2026-07-06", "Current reporting / official-process update", "Secondary reporting with direct Abbott statements and SAPOL position", "ABC", "https://www.abc.net.au/news/2026-07-06/sa-police-report-coroner-into-somerton-man-case-very-soon/106869302", "2026-07-08", "High for current official-process status; medium for Abbott's account of expected timing", "ABC reports SAPOL had not yet presented report to coroner; Abbott says police told him it would be soon.", "Webb identity; DNA; official status"],
    ["M11-SRC-0002", "Body of Somerton Man exhumed, South Australia", "South Australia Police / Mirage News republication", "Mirage News / originating SAPOL release", "2021-05-19", "Official police public release republication", "Primary official release republished by media site", "Mirage News / SAPOL", "https://www.miragenews.com/body-of-somerton-man-exhumed-south-australia-562286/", "2026-07-08", "High for exhumation/FSSA intent; use original SAPOL URL if accessible", "Records official exhumation, Operation Persevere/Persist and planned DNA recovery attempts.", "Exhumation; DNA; FSSA"],
    ["M11-SRC-0003", "Somerton Man identified as Melbourne electrical engineer, researcher says", "Daniel Keane; Gabriella Marchant", "ABC News", "2022-07-26", "Researcher-identification report", "Secondary reporting of researcher announcement", "ABC", "https://www.abc.net.au/news/2022-07-26/somerton-man-identified-melbourne-born-engineer-researcher-says/101272182", "2026-07-08", "High for Abbott announcement; not official identity determination", "Reports Abbott's claim that the man was Carl Charles Webb using DNA from hairs in the plaster bust.", "Webb identity; DNA"],
    ["M11-SRC-0004", "The DNA, the code and the conspiracies - your top questions answered", "Bridget Judd", "ABC News", "2022-08-03", "Expert Q&A / explanatory reporting", "Secondary reporting with direct expert statements", "ABC", "https://www.abc.net.au/news/2022-08-03/somerton-man-live-blog-top-questions-from-experts/101296556", "2026-07-08", "Medium-high; expert statements but not formal lab report", "Explains genetic genealogy workflow, Keane match pathway, GEDmatch and continuing uncertainty.", "DNA; genealogy; code; future work"],
    ["M11-SRC-0005", "The Somerton Man has been named. What do we know about Carl 'Charles' Webb?", "Rebecca Opie", "ABC News", "2022-08-02", "Biographical reporting", "Secondary reporting citing documents", "ABC", "https://www.abc.net.au/news/2022-08-02/somerton-man-who-was-carl-charles-webb/101288890", "2026-07-08", "Medium; direct civil records should be acquired separately", "Summarizes Webb birth, marriage, occupations, case chronology and Thomson/Jestyn timeline.", "Carl Webb; civil records; Jestyn"],
    ["M11-SRC-0006", "Is Carl Webb really the Somerton Man and if so, was he a spy?", "ABC News", "ABC News", "2022-09-02", "Conflict / sceptical reporting", "Secondary reporting with named dissent", "ABC", "https://www.abc.net.au/news/2022-09-02/is-carl-webb-really-the-somerton-man-and-was-he-a-spy/101375542", "2026-07-08", "Medium; useful for conflict mapping, not proof of alternative theory", "Records Gordon Cramer's concerns and SAPOL/coroner formal-determination boundary.", "Conflicts; DNA; spy claims"],
    ["M11-SRC-0007", "What do we know about Carl Webb? Researchers find ads, photographs", "ABC News", "ABC News", "2022-09-08", "Biographical / clothing-link reporting", "Secondary reporting of researcher leads", "ABC", "https://www.abc.net.au/news/2022-09-08/somerton-man-found-in-nephews-clothe-researchers-believes/101405152", "2026-07-08", "Medium; clothing connection remains inferential", "Reports possible John Keane clothing link, family photos and handwriting lead.", "Clothing; Keane; Webb family"],
    ["M11-SRC-0008", "Somerton Man Charles Webb's true identity revealed in family photographs and divorce papers", "Ben Cheshire", "ABC Australian Story / ABC News", "2022-11-21", "Family photograph / divorce-document reporting", "Secondary reporting with family album and divorce-file material", "ABC", "https://www.abc.net.au/news/2022-11-21/somerton-manfamily-photographs-revealed-/101643524", "2026-07-08", "Medium-high for family-photo existence; direct documents still needed", "Reports family photographs and divorce-paper evidence; says Webb finding remained unverified by SAPOL.", "Webb photos; divorce; identity"],
    ["M11-SRC-0009", "Somerton Man, Australia's Oldest Cold Case, Solved with DNA from a Single Hair", "Astrea Forensics", "Astrea Forensics", "2022", "Laboratory participant blog", "Primary/participant account, not official police/coroner record", "Astrea Forensics", "https://www.astreaforensics.com/new-blog/somerton-man-australias-oldest-cold-case-solved-with-dna-from-a-single-hair", "2026-07-08", "Medium-high for lab-process claim; lacks formal peer-reviewed/public validation", "States DNA was extracted, sequenced and genotyped at Astrea from a single 5 cm rootless hair strand.", "DNA; lab process"],
    ["M11-SRC-0010", "Somerton body inquest", "Unknown reporter", "The News via Trove", "1949-06-17", "Contemporary newspaper report", "Contemporary press", "Trove / NLA", "https://trove.nla.gov.au/newspaper/article/130195091", "2026-07-08", "Medium-high for contemporary public record; lower than transcript", "Reports opening inquest, non-natural/poison language and murder not ruled out.", "Inquest; poison; homicide"],
    ["M11-SRC-0011", "Somerton body for burial", "Unknown reporter", "The Mail via Trove", "1949-02-12", "Contemporary newspaper report", "Contemporary press", "Trove / NLA", "https://trove.nla.gov.au/newspaper/article/55922068", "2026-07-08", "Medium-high for contemporary identification efforts", "Reports embalmed body, fingerprint circulation and failure to identify body before burial.", "Witnesses; fingerprints; burial"],
    ["M11-SRC-0012", "Torn book gives new hope in body case", "Unknown reporter", "The Mail via Trove", "1949-07-23", "Contemporary newspaper report", "Contemporary press", "Trove / NLA", "https://trove.nla.gov.au/newspaper/article/56059849", "2026-07-08", "Medium-high for contemporary Rubaiyat lead; needs police-file confirmation", "Reports book finder, torn page, phone numbers and capital-letter sequence not deciphered.", "Rubaiyat; code; Taman Shud"],
    ["M11-SRC-0013", "EX-OFFICER FOUND - AND HIS RUBAIYAT", "Unknown reporter", "The Advertiser via Trove", "1949-07-28", "Contemporary newspaper report", "Contemporary press", "Trove / NLA", "https://trove.nla.gov.au/newspaper/article/36678225", "2026-07-08", "Medium-high for Boxall clue public reporting", "Reports the Boxall/Jestyn-related clue broke down after Sydney detectives located Boxall.", "Jestyn; Boxall; Rubaiyat"],
    ["M11-SRC-0014", "Advertising - divorce notice to Carl Webb", "Dorothy Jean Webb / solicitor notice", "The Age via Trove", "1951-10-05", "Legal notice / newspaper advertisement", "Contemporary legal public notice", "Trove / NLA", "https://trove.nla.gov.au/newspaper/article/205334969", "2026-07-08", "High for existence of public divorce notice; not proof of Somerton identity alone", "Public notice says Dorothy Jean Webb instituted divorce proceedings against Carl Webb, formerly of Bromby Street, South Yarra, then parts unknown.", "Carl Webb; divorce; biography"],
    ["M11-SRC-0015", "'But what poison?' Mystery of the Somerton Man", "State Records of South Australia", "State Records SA", "2015", "Official archival guide", "Official repository guide", "State Records SA", "https://archives.sa.gov.au/finding-information/discover-our-collection/stories-from-the-archive/but-what-poison-mystery-of-the-somerton-man", "2026-07-08", "High for repository holdings; medium for narrative summary", "States State Records holds open 1949 coroner file, not police files because the case remains open; later inquest restricted.", "Archives; primary records"],
    ["M11-SRC-0016", "The Enduring Mystery of the Somerton Man", "Mike Dash; updated by Meilan Solly", "Smithsonian Magazine", "Updated 2025-02-19; originally 2011-08-12", "High-quality longform reporting", "Secondary synthesis", "Smithsonian", "https://www.smithsonianmag.com/history/the-enduring-mystery-somerton-man-one-of-australias-most-puzzling-cold-cases-50795611/", "2026-07-08", "Medium; useful synthesis, not primary proof", "Updated synthesis notes Webb identification claim and continued official non-finality as of update.", "Context; code; DNA; public narrative"],
]

findings = [
    ["M11-FND-0001", "FACT", "As of ABC's 6 July 2026 report, SA Police had not yet presented its findings to the coroner, while Abbott said he expected a report soon.", "M11-SRC-0001", "2026-07-06", "Secondary current reporting", "Weakens any claim that the Webb identity is officially closed; supports an intelligence requirement for coroner/SAPOL confirmation.", "High", "Official SAPOL/coroner report not yet obtained."],
    ["M11-FND-0002", "FACT", "The 2021 exhumation was an official SAPOL/FSSA action, part of Operation Persevere and linked to DNA recovery attempts.", "M11-SRC-0002", "2021-05-19", "Primary official release republication", "Supports DNA/exhumation development; neutral on all death-mechanism hypotheses.", "High", "Original SAPOL page should be archived if reachable."],
    ["M11-FND-0003", "FACT", "Abbott announced in July 2022 that the Somerton Man was Carl Charles Webb, based on DNA from hairs in the plaster bust and genealogical matching.", "M11-SRC-0003; M11-SRC-0004; M11-SRC-0009", "2022-07-26 to 2022-08-03", "Researcher/lab participant plus reporting", "Strongly supports Webb identity as a research claim; weakens generic unknown-foreigner/spy identity claims, but does not close official identity.", "Moderate-High", "Needs official coroner/SAPOL determination and lab documentation."],
    ["M11-FND-0004", "FACT", "Astrea Forensics states it extracted, sequenced and genotyped DNA from a single 5 cm rootless hair strand.", "M11-SRC-0009", "2022", "Lab participant blog", "Supports feasibility of the hair-based DNA result; neutral on cause of death.", "Medium", "No public chain-of-custody/lab report or peer-reviewed article was located."],
    ["M11-FND-0005", "FACT", "Fitzpatrick described the genealogy method as matching DNA data to relatives through GEDmatch and family-tree reconstruction; she reported a Keane-line match and maternal-side confirmation.", "M11-SRC-0004", "2022-08-03", "Expert Q&A reporting", "Supports Webb identification pathway; supports investigation of Keane clothing link.", "Medium-High", "Full match list, kits, consent, and bioinformatics report unavailable."],
    ["M11-FND-0006", "FACT", "ABC reports civil-record details for Carl Webb: born 16 Nov 1905 in Footscray, married Dorothy Jean Robertson on 4 Oct 1941, instrument maker.", "M11-SRC-0005", "2022-08-02", "Secondary reporting citing documents", "Supports Webb biographical reconstruction; neutral on cause/manner.", "Medium", "Acquire birth/marriage certificates directly."],
    ["M11-FND-0007", "FACT", "A 5 Oct 1951 Trove legal notice states Dorothy Jean Webb instituted divorce proceedings against Carl Webb, formerly of Bromby Street, South Yarra, then parts unknown.", "M11-SRC-0014", "1951-10-05", "Contemporary legal notice", "Supports Webb disappearance/desertion timeline if Webb is the deceased; supports personal-context inquiries.", "High for notice; Moderate for linkage", "Need full divorce file and direct civil documents."],
    ["M11-FND-0008", "FACT", "ABC Australian Story reported family photographs from the 1920s said to show Charles Webb, supplied by Webb family members; it also stated the finding was not yet verified by SAPOL.", "M11-SRC-0008", "2022-11-21", "Family-photo reporting", "Supports facial/biographical reconstruction; neutral on death mechanism; reinforces official-status gap.", "Medium", "Need image rights, original album provenance and comparative method."],
    ["M11-FND-0009", "INFERENCE", "The John Keane name on clothing may be explainable through Webb family links to nephew John Russell Keane, but this remains inferential.", "M11-SRC-0007; M11-SRC-0004", "2022-08-03 to 2022-09-08", "Researcher reporting", "Supports ordinary-family clothing transfer alternative; weakens label/name-as-spy-clue readings.", "Medium-Low", "Need original garments, handwriting/label analysis and John Keane property records."],
    ["M11-FND-0010", "FACT", "Contemporary reporting in February 1949 said fingerprints were sent to all Australian and many foreign police headquarters and were not on file.", "M11-SRC-0011", "1949-02-12", "Contemporary newspaper report", "Supports long-running unidentified status; neutral on cause/manner; weakens claim that non-identification alone proves espionage.", "Medium", "Prefer original police circulation log."],
    ["M11-FND-0011", "FACT", "Contemporary July 1949 reporting says the Rubaiyat book was handed to Det.-Sgt. Leane by an Adelaide businessman, had the last-page words torn out, and contained phone numbers plus capital letters not deciphered.", "M11-SRC-0012", "1949-07-23", "Contemporary newspaper report", "Supports Rubaiyat/code evidence; neutral toward spy unless operational linkage appears.", "Medium-High", "Need original police report, book photos, paper/print test results."],
    ["M11-FND-0012", "FACT", "The Boxall/Jestyn Rubaiyat lead was publicly reported as having broken down after police located Alfred Boxall and his book.", "M11-SRC-0013", "1949-07-28", "Contemporary newspaper report", "Weakens a direct Boxall-as-deceased lead; neutral on broader Thomson/Jestyn relevance.", "Medium", "Need police interview record and Boxall service file cross-reference."],
    ["M11-FND-0013", "FACT", "State Records SA says it holds the open 1949 inquest file but not police files, because the case remained open; the later inquest file was restricted at the time of the guide.", "M11-SRC-0015", "2015", "Official archive guide", "Supports archive acquisition strategy and explains missing police-primary materials.", "High", "Need current access status check for 1958 file and police files."],
    ["M11-FND-0014", "FACT", "Contemporary inquest reporting says the coroner treated murder as not ruled out, death as probably poison and identity as unknown.", "M11-SRC-0010", "1949-06-17", "Contemporary newspaper report", "Supports conservative handling of homicide/poisoning possibilities; does not prove either.", "Medium", "Prefer DOC-0001 transcript for final wording."],
    ["M11-FND-0015", "INFERENCE", "The Webb identification, if officially confirmed, would materially weaken broad foreign-agent identity theories, but would not by itself determine cause or manner of death.", "M11-SRC-0001; M11-SRC-0003; M11-SRC-0006", "2022-2026", "Analytical inference from OSINT", "Weakens espionage identity framing; neutral on poisoning/suicide/homicide without more records.", "Moderate", "Requires official identity finding."],
    ["M11-FND-0016", "FACT", "No peer-reviewed public DNA identification paper or official coroner finding was located in this OSINT pass.", "OSINT search log; M11-SRC-0001; M11-SRC-0009", "2026-07-08", "Absence-of-source finding", "Weakens overconfident wording; supports intelligence gap IR-identity.", "Moderate", "Repeat search in academic databases and request official records."],
    ["M11-FND-0017", "FACT", "No reliable primary isotope-analysis report was located in this OSINT pass; isotope claims remain leads only.", "OSINT search log", "2026-07-08", "Absence-of-source finding", "Neutral; prevents unsupported isotope statements.", "Moderate", "Locate original Abbott/ACAD hair isotope documentation if extant."],
    ["M11-FND-0018", "FACT", "Smithsonian's 2025 update treats the Webb identity as believed/identified by researchers while also noting the official confirmation gap.", "M11-SRC-0016", "2025-02-19", "High-quality secondary synthesis", "Supports public-narrative update; does not add primary proof.", "Medium", "Use only as synthesis, not core evidence."],
]

reliability_rows = [
    ["M11-REL-0001", "Official primary/custodial records", "SAPOL/FSSA releases; State Records SA holdings", "M11-SRC-0002; M11-SRC-0015", "High", "Official but may be incomplete or point-in-time.", "Use for event existence, custody and access status."],
    ["M11-REL-0002", "Contemporary legal notices", "Trove divorce advertisement", "M11-SRC-0014", "High", "Public notice only; does not include full court file.", "Use as fact of proceeding/notice, not full marital history."],
    ["M11-REL-0003", "Contemporary newspapers", "The News, The Mail, The Advertiser via Trove", "M11-SRC-0010; M11-SRC-0011; M11-SRC-0012; M11-SRC-0013", "Medium-High", "May contain OCR errors and press simplification.", "Use as contemporary leads; confirm against inquest/police files."],
    ["M11-REL-0004", "Researcher/lab participant accounts", "Abbott/Fitzpatrick/Astrea reporting", "M11-SRC-0003; M11-SRC-0004; M11-SRC-0009", "Medium", "Not official coroner finding; limited public methods.", "Use as high-value lead requiring official/lab documentation."],
    ["M11-REL-0005", "High-quality reporting", "ABC; Smithsonian", "M11-SRC-0001; M11-SRC-0005; M11-SRC-0006; M11-SRC-0007; M11-SRC-0008; M11-SRC-0016", "Medium", "May blend source facts with expert inference.", "Use for leads, direct quotes and current status; trace back to original records."],
    ["M11-REL-0006", "Blogs/forums/Academia self-posts", "Cipher Mysteries, Medium, Academia critical draft", "Not promoted to source register except as leads", "Low-Medium", "Often valuable but not primary; may mix evidence and argument.", "Use only to locate records or map conflicts."],
]

gaps = [
    ["M11-IG-0001", "Critical", "Official coroner/SAPOL identity determination for Carl Webb", "M11-FND-0001; M11-FND-0003", "Open", "Request/monitor coroner report and SAPOL/FSSA statement."],
    ["M11-IG-0002", "Critical", "Underlying DNA laboratory report, chain of custody and match methodology", "M11-FND-0003; M11-FND-0004; M11-FND-0005", "Open", "Seek Astrea/Identifinders/Abbott technical documentation or official forensic report."],
    ["M11-IG-0003", "High", "Full Carl Webb civil/court record package", "M11-FND-0006; M11-FND-0007; M11-FND-0008", "Open", "Acquire birth, marriage, divorce, electoral, employment and probate/death absence records."],
    ["M11-IG-0004", "High", "Original Rubaiyat book custody and paper/print test results", "M11-FND-0011", "Open", "Locate police file, exhibit photos, forensic paper comparison records."],
    ["M11-IG-0005", "High", "Original body/suitcase evidence destruction or retention files", "Mission 9 custody matrix", "Open", "Request SAPOL/State Records/Historical Society property records."],
    ["M11-IG-0006", "High", "Reliable isotope-analysis source", "M11-FND-0017", "Open", "Locate original hair isotope data or remove isotope claims from manuscript."],
    ["M11-IG-0007", "Medium", "Peer-reviewed or official evaluation of code analyses", "M11-FND-0011", "Open", "Defer to Mission 12 cryptographic/document analysis."],
    ["M11-IG-0008", "High", "Primary Thomson/Jestyn interview records", "M11-FND-0012", "Open", "Acquire police interview materials or Lawson diary/source images."],
]

questions = [
    ["M11-Q-0001", "Has the South Australian coroner formally determined the Somerton Man's identity?", "Critical", "M11-IG-0001"],
    ["M11-Q-0002", "Do official body-remains DNA results match the death-mask hair result?", "Critical", "M11-IG-0002"],
    ["M11-Q-0003", "Can the Webb divorce file establish last known contact, threats, self-harm claims or location?", "High", "M11-IG-0003"],
    ["M11-Q-0004", "Can the Keane clothing link be upgraded from inference to documented transfer?", "Medium", "M11-IG-0003"],
    ["M11-Q-0005", "Did police paper/print tests conclusively associate the slip with the recovered Rubaiyat?", "High", "M11-IG-0004"],
    ["M11-Q-0006", "Was any isotope analysis ever formally published or archived?", "Medium", "M11-IG-0006"],
    ["M11-Q-0007", "Which previous claims should be downgraded if Webb is officially confirmed?", "High", "M11-IG-0001"],
]

write_csv(
    OUT / "source_register_mission11.csv",
    ["source_id", "title", "author", "publication", "date", "document_type", "primary_or_secondary", "repository", "url", "date_accessed", "reliability", "notes", "topics"],
    sources,
)

write_csv(
    OUT / "newly_identified_evidence.csv",
    ["finding_id", "classification", "finding", "source_ids", "publication_or_record_date", "source_type", "effect_on_hypotheses", "confidence", "outstanding_questions"],
    findings,
)

write_csv(
    OUT / "evidence_reliability_matrix.csv",
    ["reliability_id", "source_class", "examples", "source_ids", "reliability", "limitations", "use_rule"],
    reliability_rows,
)

write_csv(
    OUT / "intelligence_gaps_mission11.csv",
    ["gap_id", "priority", "gap", "related_findings", "status", "recommended_action"],
    gaps,
)

write_csv(
    OUT / "new_research_questions.csv",
    ["question_id", "question", "priority", "related_gap"],
    questions,
)

conflicts_md = """
# Conflicts With Previous Assessment

Mission 11 rule: conflict means a source changes, weakens or qualifies prior wording. It does not mean the newer source is automatically correct.

## Identity

- Prior conservative status: Webb attribution was unable to verify from acquired primary case records.
- OSINT update: Abbott/Fitzpatrick/Astrea/ABC reporting provides a strong researcher/lab lead for Carl Charles Webb.
- Conflict/qualification: ABC's 6 July 2026 report states SA Police still had not presented findings to the coroner. Therefore, final wording should be: `researcher/lab-led identification of Carl Charles Webb, pending official coroner/SAPOL determination`.

## DNA

- Prior conservative status: official DNA records not acquired.
- OSINT update: Astrea Forensics states DNA was extracted, sequenced and genotyped from a single rootless hair; ABC explains genealogy workflow.
- Conflict/qualification: this is not the same as a public official forensic report or peer-reviewed paper. Do not describe the DNA result as officially settled until the coroner/SAPOL record is acquired.

## Keane Clothing

- Prior conservative status: names on suitcase/body clothing are evidence items but not identity proof.
- OSINT update: ABC reports a possible John Russell Keane family connection through Webb's nephew.
- Conflict/qualification: the clothing link remains inferential unless transfer/provenance records or garment examinations are located.

## Rubaiyat and Code

- Prior conservative status: slip/book/code are real evidence clusters with unresolved interpretation.
- OSINT update: Trove contemporary reporting strengthens the public chronology of the recovered Rubaiyat book and shows code undeciphered in 1949 reporting.
- Conflict/qualification: this supports the existence of the lead, not an espionage or suicide interpretation.

## Poisoning

- Prior conservative status: no specific poison detected; cause unresolved.
- OSINT update: no new official toxicology or medical report was found.
- Conflict/qualification: do not upgrade poisoning claims. Mission 11 supports continued caution.

## Isotope Analysis

- Prior conservative status: not verified.
- OSINT update: no reliable primary/public isotope-analysis source was located.
- Conflict/qualification: isotope claims should remain excluded or marked lead-only.
"""
write_text(OUT / "conflicts_with_previous_assessment.md", conflicts_md)

updates_md = """
# Recommended Updates to Missions 1-10

## Mission 2 - Evidence Database

- Add Mission 11 sources to the main source register after review.
- Add Carl Webb civil-record leads as source leads, not verified facts unless direct documents are acquired.
- Add an explicit status value: `Researcher/Lab Lead - Pending Official Confirmation`.

## Mission 3 - Primary Source Acquisition

- Prioritize coroner/SAPOL/FSSA identity finding once available.
- Acquire direct civil records for Webb: birth, marriage, divorce file, electoral rolls and any employment records.
- Attempt to acquire original police/coroner exhibit records for the Rubaiyat book, slip and paper/print tests.

## Mission 4 - Claim Verification

- Re-open identity-related claims using Mission 11 source IDs.
- Keep official-identity status separate from researcher-identification status.
- Add a claim revision: `Carl Webb identification is supported by researcher/lab OSINT but is not yet confirmed by acquired official coroner/SAPOL record.`

## Mission 5 - Chronology

- Add 1951 divorce notice as a post-case Webb biographical record only if Webb identity is handled as conditional.
- Add 2026-07-06 ABC current-status event: SAPOL report to coroner not yet delivered, according to ABC reporting.

## Mission 6 - Witness and Exhibit Index

- Add Trove articles on Rubaiyat book recovery and Boxall clue as newspaper-reported statement leads.

## Mission 7 - Victimology

- Create a conditional Webb victimology annex, separating confirmed Webb civil records from the unresolved official identity issue.

## Mission 8 - Forensic-Medical

- No change to cause-of-death confidence. No new medical/toxicology evidence was located.

## Mission 9 - Physical Evidence

- Update death-mask/hair preservation record with Astrea/ABC source leads.
- Keep custody confidence fragmentary until official chain-of-custody records are acquired.

## Mission 10 - Context / Analysis

- Update intelligence confidence: identity confidence rises as a research lead, but official closure remains open.
- Reduce weight of espionage identity claims if Webb is officially confirmed, but do not infer cause/manner from identity alone.
"""
write_text(OUT / "recommended_updates_missions_1_10.md", updates_md)

exec_summary = """
# Mission 11 Executive Summary

Mission 11 shifted the project back toward evidence acquisition. The most important OSINT update is current status: ABC reported on 6 July 2026 that SA Police had not yet presented its Somerton Man findings to the coroner, although Professor Derek Abbott said he expected movement soon. This means the dossier should not state that the Carl Webb identification is officially closed.

The strongest new evidence cluster is the Webb/DNA cluster. ABC reporting, expert Q&A material, and Astrea Forensics' participant account all support a serious researcher/lab-led identification pathway: DNA from hair in the plaster bust, genealogical matching, a Keane-line match, and maternal-side confirmation. This is stronger than ordinary media speculation. It is still weaker than an official coroner finding, a public SAPOL/FSSA report, or a peer-reviewed DNA paper.

The best primary OSINT addition is the 5 October 1951 Trove legal notice to Carl Webb. It records Dorothy Jean Webb instituting divorce proceedings against Carl Webb, formerly of Bromby Street, South Yarra, then of parts unknown. If Webb is officially confirmed as the decedent, this becomes important biographical and movement-context evidence. Until then, it remains conditional.

Contemporary Trove sources strengthen the Rubaiyat and investigation chronology: the book was reportedly handed to Det.-Sgt. Leane in July 1949; it contained phone numbers and capital letters not then deciphered; the Boxall lead was reported as broken down; fingerprints had reportedly been circulated widely before burial without identification.

No new reliable public evidence was found for isotope analysis, a specific poison, a final medical cause of death, or an official security/intelligence link. The intelligence posture should therefore be updated, not relaxed: identity may be moving toward resolution, but cause, place of death, Rubaiyat meaning, code interpretation and custody remain open.
"""
write_text(OUT / "executive_summary.md", exec_summary)

refs = ["# References\n"]
for s in sources:
    refs.append(f"- {s[0]}: {s[1]}. {s[3]}, {s[4]}. {s[8]}")
write_text(OUT / "references.md", "\n".join(refs))

summary = f"""
# Mission 11 Summary

## Historical Topics Completed

- Carl Webb evidence
- DNA and genealogy developments
- Exhumation findings/status
- Facial/family photograph leads
- Clothing and Keane-name leads
- Suitcase/Rubaiyat/Tamam Shud paper chronology
- Code-analysis status from contemporary reporting
- Jestyn/Boxall lead status
- Military/intelligence claims as unsupported by new primary OSINT
- Medical/poison hypotheses update
- Witness/fingerprint/public-identification efforts
- Newly located archival/news/legal records

## Outputs Created

- `executive_summary.md`
- `newly_identified_evidence.csv` ({len(findings)} findings)
- `evidence_reliability_matrix.csv` ({len(reliability_rows)} reliability classes)
- `source_register_mission11.csv` ({len(sources)} sources)
- `conflicts_with_previous_assessment.md`
- `intelligence_gaps_mission11.csv` ({len(gaps)} gaps)
- `recommended_updates_missions_1_10.md`
- `new_research_questions.csv` ({len(questions)} questions)
- `references.md`

## Major Analytical Findings

- Webb identification should be upgraded from unsupported/unknown to `strong researcher/lab lead pending official confirmation`.
- Official coroner/SAPOL confirmation remains the controlling missing record.
- The 1951 Carl/Dorothy Webb divorce notice is a high-value primary lead if Webb identity is confirmed.
- The Keane clothing link has become more plausible as an ordinary-family explanation but remains inferential.
- No new OSINT found a specific poison, official cause of death, reliable isotope report or intelligence-service linkage.

## Major Unresolved Questions

- Has the coroner formally identified the deceased?
- Does official remains DNA match the death-mask hair DNA?
- What does the full Webb divorce file contain?
- What is the original Rubaiyat/slip custody trail?
- Were hair, biological samples, clothing, suitcase, paper or code materials preserved?

## Recommended Manuscript Updates

- Avoid `identity solved` phrasing unless quoting a source and immediately qualifying official status.
- Use `Carl Charles Webb attribution` or `researcher/lab-led Webb identification` until official confirmation is acquired.
- Keep cause of death and poison mechanism unresolved.
- Treat the Rubaiyat/code as documentary evidence, not proof of espionage.
- Move isotope analysis to an intelligence gap unless primary documentation is obtained.
"""
write_text(OUT / "mission_11_summary.md", summary)

print(f"Mission 11 OSINT artifacts written to {OUT}")
