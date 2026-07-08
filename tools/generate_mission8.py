#!/usr/bin/env python3
"""Generate Mission 8 forensic-medical research artifacts."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "forensic_medical"
TABLES = ROOT / "manuscript" / "tables"


def write_csv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


transcription_rows = [
    ["MTX-0001", "DOC-0001", "5", "Thomas Erskine Cleland / coroner remarks", "Extractable OCR with minor errors", "High", "body discovery; Bennett time-of-death; body position; property; Tamam Shud slip", "Targeted transcription only; not a full diplomatic transcript."],
    ["MTX-0002", "DOC-0001", "7", "Thomas Erskine Cleland / coroner remarks", "Extractable OCR with minor errors", "High", "postmortem summary; common-poison analysis; non-natural death language", "Coroner summary contains legal/medical conclusion language; register preserves it as coroner wording."],
    ["MTX-0003", "DOC-0001", "9", "Thomas Erskine Cleland / coroner remarks", "Extractable OCR with minor errors", "High", "cause-of-death uncertainty; poison speculation; place of death uncertainty", "Important distinction: coroner says evidence too inconclusive for final finding."],
    ["MTX-0004", "DOC-0001", "27", "Paul Francis Lawson", "Extractable OCR with moderate errors", "Moderate", "death mask/cast; body condition; feet and nails observations", "Some Lawson statements are explicitly assumptions and must not be treated as proved habits."],
    ["MTX-0005", "DOC-0001", "35", "John Matthew Dwyer", "Extractable OCR with medical term errors", "High", "postmortem start; external condition; rigor/lividity; dental observations; pupils; saliva", "Visual page image rendered for check; exact dental notation deferred to DOC-0017."],
    ["MTX-0006", "DOC-0001", "37", "John Matthew Dwyer", "Extractable OCR with medical term errors", "High", "internal pathology; stomach; heart; lungs; spleen; final meal timing", "Medical terms require official-copy confirmation before quotation."],
    ["MTX-0007", "DOC-0001", "39", "John Matthew Dwyer", "Extractable OCR with medical term errors and handwriting overlay", "Moderate", "blood in stomach; liver microscopy; heart failure opinion; barbiturate hypothesis; exhibits C.2/C.3", "Handwritten/overstrike content is not fully transcribed."],
    ["MTX-0008", "DOC-0001", "41", "John Matthew Dwyer", "Extractable OCR with moderate errors", "Moderate", "barbiturate timing; dose discussion; last meal; dental plate", "Poison names and dose values need manual confirmation before use."],
    ["MTX-0009", "DOC-0001", "43", "John Matthew Dwyer", "Extractable OCR with moderate errors", "Moderate", "blood in stomach; injection marks; abrasions; insulin; diphtheria toxin; botulism; nicotine; aconite", "OCR is damaged around some poison names."],
    ["MTX-0010", "DOC-0001", "45", "John Matthew Dwyer", "Extractable OCR with moderate errors", "Moderate", "poison timing; prussic acid; sunburn distribution", "Sunburn testimony is medical observation, not movement proof."],
    ["MTX-0011", "DOC-0001", "47", "Robert James Cowan", "Extractable OCR with minor chemical term errors", "High", "specimens received; testing for common poisons; cyanides; alkaloids; barbiturates; carbolic acid", "Central toxicology page."],
    ["MTX-0012", "DOC-0001", "49", "Robert James Cowan", "Extractable OCR with minor errors", "High", "negative poison findings; rare poison caveat; natural-cause opinion", "Cowan's opinion conflicts in emphasis with Dwyer/Cleland/Hicks."],
    ["MTX-0013", "DOC-0001", "63", "Patrick James Durham", "Extractable OCR with name/date distortions", "Moderate", "body photographs; fingerprints; circulation of prints/photos; paper photograph", "Date OCR reads 1943 but context/source indicates 1948; must visually confirm."],
    ["MTX-0014", "DOC-0001", "77", "Raymond Lionel Leane recalled", "Extractable OCR with minor errors", "High", "clothing exhibit; suitcase exhibit; bust exhibit; police custody order", "Forensic custody reference."],
    ["MTX-0015", "DOC-0001", "79", "John Burton Cleland", "Extractable OCR with clothing term errors", "Moderate", "clothing/suitcase comparison; thread; fit; shoes/slippers", "Mainly forensic association rather than medical pathology."],
    ["MTX-0016", "DOC-0001", "81", "John Burton Cleland", "Extractable OCR with moderate errors", "Moderate", "age estimate; cleanliness; shoes; fob pocket; tags; non-natural/poison opinion", "Contains interpretive language that must be separated from direct observation."],
    ["MTX-0017", "DOC-0001", "83", "John Burton Cleland", "Extractable OCR with moderate errors", "Moderate", "natural-cause discussion; lividity; poison possibility; Cowan negative finding", "Some wording blends medical opinion and scenario reconstruction."],
    ["MTX-0018", "DOC-0001", "85", "John Burton Cleland", "Extractable OCR with moderate errors", "Moderate", "barbiturates/alkaloids; uncommon poison reasoning; vomiting/cyanide/curare discussion", "Do not convert possibility language into confirmed poison."],
    ["MTX-0019", "DOC-0001", "87", "John Burton Cleland", "Extractable OCR with moderate errors", "Moderate", "injection mark limits; circumcision/vaccination observations; insulin question", "Includes non-medical pocket/money inference; not used as medical fact."],
    ["MTX-0020", "DOC-0001", "89", "John Burton Cleland", "Extractable OCR with minor errors", "High", "liver microscopy; insulin as possible suicide method in general", "Short page; limited evidentiary value."],
    ["MTX-0021", "DOC-0001", "91", "Cedric Stanton Hicks", "Extractable OCR with minor errors", "High", "Hicks sworn; coroner reads Dwyer evidence; Bennett interposed", "Introductory page."],
    ["MTX-0022", "DOC-0001", "93", "John Barkly Bennett", "Extractable OCR with moderate errors", "High", "9:40 a.m. examination; rigor-mortis basis; 2 a.m. earliest death estimate", "Bennett calls examination cursory."],
    ["MTX-0023", "DOC-0001", "95", "Cedric Stanton Hicks", "Extractable OCR with chemical-name distortion", "Moderate", "not-natural opinion; barbiturate/morphine discussion; contracted heart; engorged organs; stomach blood", "Specific group names partly obscured by exhibit handling/OCR."],
    ["MTX-0024", "DOC-0001", "97", "Cedric Stanton Hicks", "Extractable OCR with chemical-name distortion", "Low", "drug group causing systole; detection limitations; oral toxicity; vomiting caveat", "Critical but damaged; manual visual transcription required before naming substances."],
    ["MTX-0025", "DOC-0001", "99", "Cedric Stanton Hicks", "Extractable OCR with moderate errors", "Moderate", "self-administration assumption; body relocation caveat; convulsions; sand disturbance limits", "Important scenario caveat; not a homicide/suicide evaluation."],
    ["MTX-0026", "DOC-0001", "101", "Cedric Stanton Hicks", "Extractable OCR with handwriting/strike-through distortion", "Low", "convulsions; arm movement; insulin/diabetic coma exclusion; oral route", "Needs manual transcription before quotation."],
]


observation_rows = [
    ["MED-0001", "external body condition", "Tallish male, estimated about 45 years, greying hair and good physical condition.", "John Matthew Dwyer", "DOC-0001", "p.35", "Concise paraphrase of Dwyer external examination.", "Partially Verified", "High", "Age estimate is medical impression, not identity proof."],
    ["MED-0002", "external body condition", "Fingernails and feet appeared cared for; nails carefully trimmed.", "John Matthew Dwyer", "DOC-0001", "p.35", "Concise paraphrase.", "Partially Verified", "High", "Do not infer occupation or social status."],
    ["MED-0003", "injuries/trauma", "No external markings of note recorded by Dwyer.", "John Matthew Dwyer", "DOC-0001", "p.35", "Concise paraphrase.", "Partially Verified", "High", "Does not equal a complete trauma exclusion without full autopsy file."],
    ["MED-0004", "lividity/rigor", "Postmortem rigidity described as intense; deep lividity noted behind/above ears and neck.", "John Matthew Dwyer", "DOC-0001", "p.35", "Concise paraphrase.", "Verified", "High", "Supports time/body-position discussion but not exact place of death."],
    ["MED-0005", "anatomical identifiers", "Several teeth were missing; Dwyer prepared a missing-teeth chart.", "John Matthew Dwyer", "DOC-0001", "p.35; DOC-0017", "Concise paraphrase.", "Verified", "High", "Exact tooth notation remains visually unresolved."],
    ["MED-0006", "external body condition", "Pupils were small, unusual/uneven in outline, and about the same size.", "John Matthew Dwyer", "DOC-0001", "p.35", "Concise paraphrase.", "Partially Verified", "Moderate", "Dwyer cautioned drug association is broad and not distinguishing."],
    ["MED-0007", "external body condition", "Small patch of dried saliva was noted at the right of the mouth.", "John Matthew Dwyer", "DOC-0001", "p.35", "Concise paraphrase.", "Verified", "High", "Interpretation of timing/ability to swallow remains opinion."],
    ["MED-0008", "external body condition", "Sand was in the hair but not in nostrils or mouth.", "John Matthew Dwyer", "DOC-0001", "p.37", "Concise paraphrase.", "Verified", "High", "Useful for scene/body-position assessment later."],
    ["MED-0009", "internal pathology", "Scalp, skull and brain were normal except small brain vessels were readily visible with congestion.", "John Matthew Dwyer", "DOC-0001", "p.37", "Concise paraphrase.", "Verified", "High", "Coroner also summarized brain congestion at p.7."],
    ["MED-0010", "internal pathology", "Pharynx was congested; gullet showed superficial whitening and a patch of ulceration.", "John Matthew Dwyer", "DOC-0001", "p.37", "Concise paraphrase.", "Verified", "High", "Exact mucosal description should be checked before quotation."],
    ["MED-0011", "stomach contents", "Stomach deeply congested with superficial redness and small submucosal haemorrhages.", "John Matthew Dwyer", "DOC-0001", "p.37", "Concise paraphrase.", "Verified", "High", "Observed pathology; poison interpretation separate."],
    ["MED-0012", "stomach contents", "Blood was mixed with food in the stomach.", "John Matthew Dwyer", "DOC-0001", "p.37; p.39; p.43", "Concise paraphrase.", "Verified", "High", "Dwyer said he considered it present before postmortem."],
    ["MED-0013", "organ congestion", "Kidneys, liver, lungs, spleen and brain/upper vessels were described with congestion or engorgement.", "John Matthew Dwyer", "DOC-0001", "pp.37-39", "Concise paraphrase.", "Verified", "High", "Exact organ-by-organ language should be quoted from official copy only."],
    ["MED-0014", "heart findings", "Heart was normal in size and otherwise normal; muscle was tough/firm; heart was if anything contracted.", "John Matthew Dwyer", "DOC-0001", "p.37", "Concise paraphrase.", "Verified", "High", "Hicks later relied on contracted-heart observation."],
    ["MED-0015", "internal pathology", "Spleen described as strikingly large and firm, about three times normal size.", "John Matthew Dwyer", "DOC-0001", "p.37", "Concise paraphrase.", "Verified", "High", "No final cause inferred."],
    ["MED-0016", "stomach contents", "Food in stomach estimated by Dwyer as present up to 3 or 4 hours before death, with anxiety caveat.", "John Matthew Dwyer", "DOC-0001", "p.37", "Concise paraphrase.", "Partially Verified", "Moderate", "Meal timing is uncertain and physiologically caveated."],
    ["MED-0017", "internal pathology", "Microscopy showed destruction of centres of liver lobules; otherwise congestion signs predominated.", "John Matthew Dwyer", "DOC-0001", "p.39", "Concise paraphrase.", "Partially Verified", "Moderate", "OCR damaged; Cleland later found liver section not explanatory."],
    ["MED-0018", "uncertainty", "Dwyer stated death was not natural and immediate cause was heart failure, but he could not state what caused heart failure.", "John Matthew Dwyer", "DOC-0001", "p.39", "Concise paraphrase.", "Verified", "High", "Do not convert to final cause of death."],
    ["MED-0019", "toxicology", "Dwyer initially suggested a barbiturate or soluble hypnotic, then accepted Cowan's negative finding while preserving possibility language.", "John Matthew Dwyer", "DOC-0001", "pp.39-41", "Concise paraphrase.", "Partially Verified", "Moderate", "Hypothesis by medical witness, not detected substance."],
    ["MED-0020", "injuries/trauma", "Dwyer saw no evidence of hypodermic needle use; two recent abrasions on right hand did not appear significant.", "John Matthew Dwyer", "DOC-0001", "p.43", "Concise paraphrase.", "Partially Verified", "Moderate", "A tiny injection mark could still be missed per later witnesses."],
    ["MED-0021", "external body condition", "Legs were sunburned to the crotch; trunk was not sunburned; Dwyer attributed burn to previous season or older.", "John Matthew Dwyer", "DOC-0001", "p.45", "Concise paraphrase.", "Partially Verified", "Moderate", "Do not infer residence/travel from this alone."],
    ["MED-0022", "toxicology", "Cowan received stomach contents, liver/muscle, urine and blood on 2 December 1948.", "Robert James Cowan", "DOC-0001", "p.47", "Concise paraphrase.", "Verified", "High", "Specimen chain from P.C. Sutherland; full lab file missing."],
    ["MED-0023", "toxicology", "Cowan tested for common poisons and found no signs of any common poison in the submitted specimens.", "Robert James Cowan", "DOC-0001", "p.47", "Concise paraphrase.", "Verified", "High", "Not equivalent to no poison present."],
    ["MED-0024", "toxicology", "Cowan identified cyanides, alkaloids, barbiturates and carbolic acid as among common poisons tested/considered.", "Robert James Cowan", "DOC-0001", "p.47", "Concise paraphrase.", "Verified", "High", "Exact list may not be exhaustive."],
    ["MED-0025", "uncertainty", "Cowan said if death were by poison, it would be a very rare poison; he thought natural causes more likely than poisoning.", "Robert James Cowan", "DOC-0001", "p.49", "Concise paraphrase.", "Verified", "High", "Conflicts with other medical witnesses' emphasis."],
    ["MED-0026", "post-mortem handling", "Lawson made a mould/cast of the body features on 7 June 1949; formalin embalming affected appearance.", "Paul Francis Lawson", "DOC-0001", "p.27", "Concise paraphrase.", "Verified", "High", "Relevant to death mask limitations."],
    ["MED-0027", "fingerprints", "Durham photographed and fingerprinted the deceased and circulated prints/photos to Australian states, New Zealand and overseas fingerprint bureaus.", "Patrick James Durham", "DOC-0001", "p.63; DOC-0016", "Concise paraphrase.", "Verified", "High", "No identification resulted according to testimony; full circulation log unavailable."],
    ["MED-0028", "post-mortem handling", "Clothing, suitcase and bust were marked as exhibits and ordered kept in police custody.", "Raymond Lionel Leane recalled / Coroner", "DOC-0001", "p.77", "Concise paraphrase.", "Verified", "High", "Current custody not established."],
    ["MED-0029", "external body condition", "Cleland agreed with age range about 40-45 or 40-50 and noted clean nails, clean shoes and cared-for appearance.", "John Burton Cleland", "DOC-0001", "p.81", "Concise paraphrase.", "Partially Verified", "Moderate", "Observation after embalming; avoid status inference."],
    ["MED-0030", "uncertainty", "Cleland considered death not natural and probably poison, but accepted Cowan found no poison present.", "John Burton Cleland", "DOC-0001", "pp.81-85", "Concise paraphrase.", "Partially Verified", "Moderate", "Opinion not final cause determination."],
    ["MED-0031", "lividity/rigor", "Cleland discussed lividity around ears/neck as perhaps surprising but explainable by head support.", "John Burton Cleland", "DOC-0001", "p.83", "Concise paraphrase.", "Partially Verified", "Moderate", "Interpretive; not proof of original death location."],
    ["MED-0032", "toxicology", "Cleland discussed barbiturates, alkaloids, cyanide, curare/tubarine and injection possibilities but found no poison fully fit the circumstances.", "John Burton Cleland", "DOC-0001", "pp.85-87", "Concise paraphrase.", "Partially Verified", "Moderate", "Considered substances only."],
    ["MED-0033", "time of death", "Bennett examined the body at 9:40 a.m. on 1 December and estimated death up to eight hours earlier, not more than eight hours.", "John Barkly Bennett", "DOC-0001", "p.93", "Concise paraphrase.", "Verified", "High", "Estimate based on cursory look/rigor and cyanosis."],
    ["MED-0034", "toxicology", "Hicks thought barbiturates and morphine were unlikely causes under the timing and pathology described.", "Cedric Stanton Hicks", "DOC-0001", "p.95", "Concise paraphrase.", "Partially Verified", "Moderate", "Chemical names in page are distorted; preserve category only."],
    ["MED-0035", "toxicology", "Hicks suspected a drug group capable of stopping the heart in systole and difficult to detect by ordinary chemical tests.", "Cedric Stanton Hicks", "DOC-0001", "p.97", "Concise paraphrase.", "Partially Verified", "Low", "Specific group/member names are obscured; do not name without manual transcription."],
    ["MED-0036", "uncertainty", "Hicks stated body relocation would remove some time-of-death difficulties; this was framed as conditional.", "Cedric Stanton Hicks", "DOC-0001", "p.99", "Concise paraphrase.", "Partially Verified", "Moderate", "Scenario caveat, not finding."],
    ["MED-0037", "lividity/rigor", "Hicks stated convulsions may precede death and the 7 p.m. arm movement could have been convulsive.", "Cedric Stanton Hicks", "DOC-0001", "p.101", "Concise paraphrase.", "Partially Verified", "Low", "OCR/handwriting damage; use cautiously."],
    ["MED-0038", "toxicology", "Hicks excluded diabetic coma/insulin on liver and other findings and stated oral route would act less rapidly than injection.", "Cedric Stanton Hicks", "DOC-0001", "p.101", "Concise paraphrase.", "Partially Verified", "Low", "Needs manual transcription before quotation."],
]


toxicology_rows = [
    ["TOX-0001", "Common poisons", "Robert James Cowan", "DOC-0001", "p.47", "Specimens of stomach contents, liver/muscle, urine and blood were analyzed.", "No signs of common poison found.", "Analyses of submitted specimens.", "Exact analytical methods and full panel unknown.", "No", "No; only common poisons in submitted specimens not detected.", "Not detected"],
    ["TOX-0002", "Cyanides", "Robert James Cowan; John Burton Cleland", "DOC-0001", "pp.47,85", "Cowan listed cyanides among common poisons; Cleland discussed rapidity/no smell/no bottle.", "Negative common-poison analysis; Cleland said cyanide would be very quick and no bottle/smell noted.", "Cowan common-poison analysis.", "No specific cyanide method recorded in acquired text.", "No", "Not categorically excluded beyond Cowan testimony.", "Not detected"],
    ["TOX-0003", "Alkaloids", "Robert James Cowan; John Burton Cleland", "DOC-0001", "pp.47,85", "Cowan listed alkaloids among common poisons; Cleland said some alkaloids may not be detectable.", "Cowan found no common poison.", "Cowan common-poison analysis.", "Specific alkaloids and methods not listed.", "No", "No; class remains broad.", "Not detected"],
    ["TOX-0004", "Barbiturates", "John Matthew Dwyer; Robert James Cowan; John Burton Cleland; Cedric Stanton Hicks", "DOC-0001", "pp.39-41,47,85,95", "Dwyer initially suggested barbiturate/soluble hypnotic; other witnesses discussed detectability and timing.", "Cowan found none; Hicks/Cleland considered timing and pathology problematic.", "Cowan common-poison analysis included barbiturates.", "Decomposition/non-detection debated; no laboratory detail.", "No", "Not completely excluded by all witnesses, but not detected and considered unlikely by Hicks/Cowan.", "Considered but unproven"],
    ["TOX-0005", "Soluble hypnotic", "John Matthew Dwyer", "DOC-0001", "p.39", "Dwyer said his report suggested a barbiturate or soluble hypnotic.", "No supporting detection; Cowan negative.", "Cowan common-poison analysis.", "Class not defined in extracted testimony.", "No", "No.", "Suggested by witness"],
    ["TOX-0006", "Carbolic acid", "Robert James Cowan", "DOC-0001", "p.47", "Listed among common poisons.", "No signs of any common poison found.", "Cowan common-poison analysis.", "Specific test not recorded.", "No", "Not detected in submitted specimens.", "Not detected"],
    ["TOX-0007", "Morphine", "Cedric Stanton Hicks", "DOC-0001", "p.95", "Hicks discussed a dose sufficient to kill within the timing window.", "Hicks said such a dose would have been detectable/measurable.", "No specific morphine test details in acquired text.", "Chemical name OCR around passage distorted but morphine is readable.", "No", "Considered unlikely by Hicks.", "Ruled unlikely"],
    ["TOX-0008", "Insulin", "John Matthew Dwyer; John Burton Cleland; Cedric Stanton Hicks", "DOC-0001", "pp.43,87,101", "Witnesses considered insulin/injection possibilities.", "Dwyer and Hicks referenced liver/diabetic findings against it; Cleland noted blood sugar might have helped if suspected.", "No insulin-specific test documented.", "No retained sample/lab method documented; injection mark could be missed.", "No", "Not conclusively excluded by testing; medically discounted in testimony.", "Ruled unlikely"],
    ["TOX-0009", "Diphtheria toxin", "John Matthew Dwyer", "DOC-0001", "p.43", "Dwyer said access to diphtheria toxin could be a possible but very unusual explanation.", "Requires access to manufacturing context; no detection or corroboration.", "None documented.", "No test recorded.", "No", "No.", "Suggested by witness"],
    ["TOX-0010", "Botulism toxin", "John Matthew Dwyer", "DOC-0001", "p.43", "Dwyer considered botulism but noted timing/incubation difficulty.", "Timing made it unlikely in his testimony.", "None documented.", "No test recorded.", "No", "Considered unlikely by Dwyer.", "Ruled unlikely"],
    ["TOX-0011", "Nicotine", "John Matthew Dwyer", "DOC-0001", "p.43", "Dwyer said nicotine poisoning entered his mind.", "Cowan said none was found according to Dwyer testimony.", "Cowan analysis as referenced by Dwyer.", "Specific nicotine method not recorded.", "No", "Not detected per testimony.", "Not detected"],
    ["TOX-0012", "Aconite/aconitine class", "John Matthew Dwyer", "DOC-0001", "p.43", "Dwyer mentioned possibilities around aconite with isolation difficulties.", "No detection or direct evidence.", "None documented in acquired text.", "OCR damaged; exact name requires confirmation.", "No", "No.", "Considered but unproven"],
    ["TOX-0013", "Curare/tubarine", "John Matthew Dwyer; John Burton Cleland", "DOC-0001", "pp.43,85", "Dwyer considered curare-like injection/asphyxia; Cleland discussed tubarine/curare.", "Dwyer saw no injection evidence and did not think findings supported it.", "No test documented.", "Injection route and detection limitations unresolved.", "No", "No.", "Considered but unproven"],
    ["TOX-0014", "Unspecified cardiac glycoside/drug group", "Cedric Stanton Hicks; coroner remarks", "DOC-0001", "pp.9,95-99", "Hicks suspected an unnamed group causing heart to stop in systole; coroner later used probable glucoside language.", "Specific agent not detected; group/member names obscured in transcript.", "No specific test documented.", "Names and methods unavailable in current OCR; official transcript/visual transcription needed.", "No", "No; only considered/suggested.", "Suggested by witness"],
]


tod_rows = [
    ["TOD-0001", "Thomas Erskine Cleland / coroner remarks", "Bennett examined body at 9:40 a.m. and thought death occurred around 2 a.m.", "CHR-0008; CHR-0010", "Around 2:00 a.m. on 1948-12-01", "Coroner summary of Bennett opinion", "Moderate", "Secondary within inquest remarks; exact basis in Bennett testimony p.93."],
    ["TOD-0002", "John Barkly Bennett", "Death could have occurred up to eight hours before his 9:40 a.m. examination, not more than eight hours.", "CHR-0008; CHR-0010", "No earlier than about 1:40 a.m.; Bennett put earliest at 2:00 a.m.", "Rigor mortis; cursory look; cyanosis", "Moderate", "Bennett did not record extent of rigor at the time and described examination as cursory."],
    ["TOD-0003", "John Matthew Dwyer", "Food had been in the stomach for up to 3 or 4 hours before death, with anxiety caveat.", "CHR-0019", "Final meal up to 3-4 hours before death, per Dwyer estimate", "Stomach contents", "Low", "Not a precise time-of-death estimate; digestion variable."],
    ["TOD-0004", "John Matthew Dwyer", "Poison, if involved, must have been taken a few hours before death.", "CHR-0019", "A few hours before death", "Medical inference from pathology and poison discussion", "Low", "Conditional on poison involvement; no agent detected."],
    ["TOD-0005", "Cedric Stanton Hicks", "If death occurred seven hours after the 7 p.m. sighting, a massive dose would be implied for the suspected drug group.", "CHR-0006; CHR-0008", "Conditional seven-hour interval from 7 p.m. movement to about 2 a.m.", "Pharmacological timing reasoning", "Low", "Depends on unproved identity of the man seen at 7 p.m. and unproved poison."],
    ["TOD-0006", "Cedric Stanton Hicks", "If body had been brought there, doubts about time of death would change/remove some difficulties.", "CHR-0008", "Unknown", "Conditional scenario caveat", "Low", "No evidence here that body was moved; recorded only as caveat."],
    ["TOD-0007", "John Burton Cleland", "Estimated probable death at or before midnight in one passage, while other evidence supported around 2 a.m.", "CHR-0008", "At or before midnight per Cleland estimate", "Interpretive timing from scenario/toxicology", "Very Low", "Conflicts with Bennett; not adopted as master chronology event."],
]


identifier_rows = [
    ["FID-0001", "dental chart", "Dwyer prepared a missing-teeth chart; separate chart reproduction preserved as DOC-0017.", "John Matthew Dwyer; DOC-0017", "DOC-0001; DOC-0017", "DOC-0001 p.35; DOC-0017 p.1", "High for existence; moderate for exact notation.", "Chart image has no OCR and exact dental notation needs specialist/manual transcription."],
    ["FID-0002", "dental characteristics", "Several teeth missing; Dwyer stated missing teeth would be noticeable if the man laughed but not necessarily if speaking.", "John Matthew Dwyer", "DOC-0001", "p.35", "High as identification feature.", "No comparative dental records acquired."],
    ["FID-0003", "fingerprints", "Fingerprint chart of deceased male found at Somerton; separate visual reproduction preserved.", "DOC-0016", "DOC-0016", "DOC-0016 p.1", "High for existence; limited for comparison without original/search logs.", "Image quality moderate; fingerprint classification annotations need specialist review."],
    ["FID-0004", "fingerprints", "Durham fingerprinted deceased and circulated copies to Australian states, New Zealand and important overseas bureaus.", "Patrick James Durham", "DOC-0001", "p.63", "High for process.", "Full bureau response file not acquired."],
    ["FID-0005", "photographs", "Durham produced full-face and side-face photographs marked as exhibits.", "Patrick James Durham", "DOC-0001", "p.63", "High for existence.", "Original photos/exhibit images not fully catalogued in Mission 8."],
    ["FID-0006", "death mask/bust", "Lawson made a cast of the features; bust was later marked as exhibit C.17.", "Paul Francis Lawson; Raymond Lionel Leane", "DOC-0001", "pp.27,77", "High for existence.", "Embalming/formalin and postmortem changes limit living-appearance inference."],
    ["FID-0007", "physical measurements", "Height/build not precisely measured in extracted medical pages; described as tallish and in good physical condition.", "John Matthew Dwyer", "DOC-0001", "p.35", "Moderate.", "Need autopsy sheet or police physical description for exact measurements."],
    ["FID-0008", "scars/marks", "Light scar on left upper arm; uncertain vaccination mark; two recent right-hand abrasions noted.", "John Matthew Dwyer; John Burton Cleland", "DOC-0001", "pp.43,87", "Moderate.", "No complete body map acquired."],
    ["FID-0009", "biological samples", "Stomach contents, liver/muscle, urine and blood were submitted to Cowan.", "Robert James Cowan", "DOC-0001", "p.47", "High for 1948 submission; low for present availability.", "Physical sample retention/disposal unknown."],
    ["FID-0010", "death certificate", "Certified copy records unidentified male body and death registration details.", "Registrar of Births, Deaths and Marriages", "DOC-0003", "p.1", "Moderate.", "OCR is poor; visual certificate review needed before exact transcription."],
]


uncertainty_rows = [
    ["MU-0001", "What was the exact medical cause of death?", "Dwyer: heart failure but unknown factor; Cowan: no common poison; Hicks/Cleland: non-natural/poison opinions.", "Unresolved", "Official autopsy report; official toxicology report; modern forensic review of preserved remains if available.", "Critical"],
    ["MU-0002", "Was any toxic agent present?", "No common poison detected; several agents/classes considered; no agent detected in acquired record.", "Unresolved", "Original lab notebooks; retained specimens; modern toxicology only if legally and materially possible.", "Critical"],
    ["MU-0003", "Which drug group did Hicks identify in exhibit form?", "DOC-0001 pp.95-99 references a group and exhibit, but OCR/visual text obscures names.", "Unresolved", "Official transcript; high-resolution page/exhibit scan; pharmacology expert review.", "Critical"],
    ["MU-0004", "How reliable was the 2 a.m. time-of-death estimate?", "Bennett estimate based on cursory look, rigor and cyanosis; Dwyer stomach timing caveated.", "Partially documented", "Full Bennett notes; official medical reports; forensic pathology review.", "High"],
    ["MU-0005", "Did the body die where found?", "Coroner explicitly said no proof the evening man was the deceased and could not say where death occurred.", "Unresolved", "Scene reports; witness transcripts; photographs; lividity/body-position review.", "High"],
    ["MU-0006", "Can stomach contents narrow the final meal window?", "Dwyer estimated up to 3-4 hours but noted anxiety may suspend digestion.", "Partially documented", "Autopsy report; lab description of stomach contents; forensic pathology review.", "Medium"],
    ["MU-0007", "Were injection marks conclusively absent?", "Dwyer saw no evidence; Cleland noted a hypodermic mark could be overlooked despite care.", "Unresolved", "Autopsy body map; high-resolution body photographs.", "High"],
    ["MU-0008", "What are the exact dental identifiers?", "Dwyer chart exists; chart image visible but exact notation remains unresolved.", "Partially documented", "Specialist dental chart transcription; original chart if available.", "Medium"],
    ["MU-0009", "What was the present fate of biological specimens?", "Cowan received specimens in 1948; no retention/disposal record acquired.", "Unknown", "Laboratory archive inquiry; Coroner/SAPOL/FSSA holdings search.", "High"],
    ["MU-0010", "What was the medical significance of liver-lobule findings?", "Dwyer noted destruction of liver lobule centres; Cleland later did not find liver section explanatory.", "Unresolved", "Microscopy slides if extant; full pathology report; modern hepatopathology review.", "Medium"],
]


write_csv(
    OUT / "medical_transcription_index.csv",
    ["transcription_id", "document_id", "page_number", "witness_source", "ocr_status", "transcription_confidence", "relevant_medical_topic", "notes"],
    transcription_rows,
)

write_csv(
    OUT / "medical_observation_register.csv",
    ["observation_id", "observation_category", "description", "witness_source", "document_id", "page_reference", "exact_wording_or_concise_paraphrase", "verification_status", "confidence", "notes"],
    observation_rows,
)

write_csv(
    OUT / "toxicology_register.csv",
    ["toxicology_id", "substance_or_class", "mentioned_by", "document_id", "page_reference", "evidence_for_consideration", "evidence_against", "testing_performed", "testing_limitation", "whether_detected", "whether_excluded", "current_status"],
    toxicology_rows,
)

write_csv(
    OUT / "time_of_death_register.csv",
    ["tod_id", "source", "statement", "related_event", "time_estimate", "basis", "confidence", "limitations"],
    tod_rows,
)

write_csv(
    OUT / "forensic_identifiers_register.csv",
    ["identifier_id", "type", "description", "source", "document_id", "page_file_reference", "current_evidentiary_value", "limitations"],
    identifier_rows,
)

write_csv(
    OUT / "medical_uncertainties.csv",
    ["uncertainty_id", "question", "evidence_bearing_on_question", "current_status", "possible_future_tests", "priority"],
    uncertainty_rows,
)

transcription_md = """
# Medical Transcriptions

Mission 8 transcription rule: this file records targeted medical extracts and conservative paraphrases from priority pages. It is not a full diplomatic transcript. OCR confidence is recorded in `medical_transcription_index.csv`; pages with low or moderate confidence require manual visual transcription before direct quotation in the dossier.

## DOC-0001 Priority Pages

### Pages 5, 7, 9 - Coroner's Adjournment Remarks

- p.5 records the body discovery at Somerton about 7 a.m. on 1 December 1948, Bennett's 9:40 a.m. examination, Bennett's approximate 2 a.m. death estimate, body position, visible property, the partly smoked cigarette, and the later-found Tamam Shud slip.
- p.7 summarizes postmortem findings: brain-vessel congestion, deeply congested stomach, superficial redness, submucosal haemorrhages, normal/contracted heart, extensive liver and spleen congestion, liver-lobule destruction, Dwyer's heart-failure opinion with unidentified causal factor, retained specimens, and no common poison found on analysis.
- p.9 preserves the coroner's uncertainty: the evidence was too inconclusive for a final finding; the coroner could not say where the deceased died; poison/glucoside language appears as a conditional/prepared finding rather than a settled medical identification.

### Page 27 - Lawson

- Lawson made a mould and cast of the deceased's features at the City Mortuary on 7 June 1949.
- He stated embalming/formalin and postmortem change affected appearance.
- He observed cared-for nails and unusual foot/calf features, but explicitly framed some footwear/body-habit statements as his own assumptions.

### Pages 35-45 - Dwyer

- p.35: Dwyer performed a postmortem at 7:30 a.m. on 2 December 1948 at the City Mortuary. He described a tallish, approximately 45-year-old man with greying hair, good physical condition, cared-for nails/feet, no external markings of note, intense rigor, deep lividity around/above ears and neck, missing teeth, small/uneven pupils, and dried saliva near the mouth.
- p.37: Dwyer described sand in the hair but not nostrils/mouth; normal scalp/skull/brain except visible small vessels with congestion; congested pharynx; gullet mucosal changes; deeply congested stomach with redness, small haemorrhages and blood mixed with food; congestion in kidneys, liver, lungs and spleen; normal strong heart, if anything contracted; spleen enlarged/firm; food timing estimated up to 3 or 4 hours before death with a caveat.
- p.39: Dwyer said blood in the stomach suggested an irritant poison but no visible finding in the food; specimens were sent for analysis. He described liver-lobule changes, stated death was not natural, identified immediate cause as heart failure, but could not say what factor caused it. He had suggested a barbiturate or soluble hypnotic in his report, but accepted Cowan's negative analysis.
- p.41: Dwyer discussed barbiturate timing/dose issues and considered barbiturates unlikely in view of the chemist's findings, while preserving them as a possible explanation. He also commented on missing back teeth and no dental plates being present.
- p.43: Dwyer said stomach blood was present before postmortem and likely mixed with food during life. He saw no evidence of hypodermic injection, noted recent right-hand abrasions as not significant, and discussed insulin, diphtheria toxin, botulism, nicotine and aconite-class possibilities without confirming any.
- p.45: Dwyer said any poison would have needed to be taken a few hours before death and discussed prussic acid as too rapid for observed findings. He also described leg sunburn distribution as likely from a previous season or older.

### Pages 47-49 - Cowan

- p.47: Cowan received stomach contents, liver/muscle, urine and blood from P.C. Sutherland on 2 December 1948 and analyzed them at Sutherland's request. He found no signs of common poison. The page lists cyanides, alkaloids, barbiturates and carbolic acid among common poisons.
- p.49: Cowan stated that if death were caused by any common poison, he expected his examination would reveal it. If poison caused death, he thought it would be rare in the sense of rarely used for suicide or homicide. He also stated death was more likely due to natural causes than poisoning because no poison was detected.

### Page 63 - Durham

- Durham photographed the body full-face and side-face, fingerprinted the deceased, circulated prints/photos to Australian states, New Zealand and overseas fingerprint bureaus, and reported no identification response.

### Page 77 - Exhibit Custody

- Leane was recalled. Clothing from the body, the suitcase, and the bust were marked as exhibits; the coroner ordered them kept in police custody.

### Pages 79-89 - John Burton Cleland

- p.79: Cleland compared clothing and suitcase contents, including unusual warm-sepia thread, garment fit, and related physical association evidence.
- p.81: Cleland described the deceased as appearing European/British, noted clean/cared-for nails and shoes, discussed the fob pocket where the paper was found, and stated his opinion that death was almost certainly not natural and probably involved poison. This is opinion evidence, not a detected toxicology result.
- p.83: Cleland discussed absence of obvious natural-cause explanation, lividity around ears/neck, and the possibility that some poisons could be excreted or not noticeable on analysis.
- p.85: Cleland discussed barbiturates, alkaloids, cyanide, vomiting, curare/tubarine and detection issues. He repeatedly framed substances as difficult to fit to all circumstances.
- p.87: Cleland stated certainty was impossible, but he had very little doubt death was unnatural. He noted limits around vaccination marks, hypodermic marks, and insulin testing.
- p.89: Cleland found the liver section did not explain the cause of death and briefly discussed insulin as a possible method in general.

### Pages 91-101 - Hicks and Bennett

- p.91: Hicks was sworn as Professor of Physiology and Pharmacology; the coroner read part of Dwyer's evidence and then Bennett's evidence was interposed.
- p.93: Bennett examined the body at 9:40 a.m. on 1 December 1948 in a police ambulance outside Adelaide Hospital. He said life was extinct and death could have occurred up to eight hours earlier, not more than eight hours. He based this on rigor mortis but had not recorded its extent at the time; he also described the look as cursory.
- p.95: Hicks agreed death was not natural and accepted Cowan's competence. He considered barbiturates and morphine unlikely under the described timing/pathology and described reasons for suspecting a different poison group: contracted heart, engorged lungs/liver/spleen, and blood in the stomach.
- p.97: Hicks described an unnamed drug group that could stop the heart in systole and could be extremely difficult to identify by ordinary chemical tests. Specific group/member names are obscured in the OCR and must not be named from this reproduction alone.
- p.99: Hicks said if the body had been brought to the location, some time-of-death difficulties would be removed. He discussed convulsions and emphasized the limitations of drawing conclusions from disturbed sand or lack of vomit.
- p.101: Hicks discussed convulsions and the 7 p.m. arm movement as possibly convulsive, rejected diabetic coma/insulin in relation to liver and other findings, and stated the substance could have been taken orally; injection would have acted more rapidly.

## Non-OCR Identifier Files

- DOC-0016 `fingerprints.pdf`: visual record headed as fingerprints of the deceased male person found at Somerton Beach, Adelaide, South Australia, 1 December 1948. Print images and classification marks require specialist review.
- DOC-0017 `teeth.pdf`: visual dental chart with left/right notation and handwritten missing-teeth note. Exact dental notation requires specialist transcription before use.
"""

write_text(OUT / "medical_transcriptions.md", transcription_md)

summary = f"""
# Mission 8 Forensic-Medical Summary

Scope: forensic-medical evidence assessment only. This file does not evaluate motive, espionage, suicide, homicide, or final cause of death.

## Outputs Created

- `medical_transcription_index.csv`: {len(transcription_rows)} priority transcription records.
- `medical_transcriptions.md`: targeted medical page extracts/paraphrases.
- `medical_observation_register.csv`: {len(observation_rows)} medical observations.
- `toxicology_register.csv`: {len(toxicology_rows)} toxicology entries.
- `time_of_death_register.csv`: {len(tod_rows)} timing entries.
- `forensic_identifiers_register.csv`: {len(identifier_rows)} forensic identifier entries.
- `medical_uncertainties.csv`: {len(uncertainty_rows)} unresolved medical questions.

## Documented

- Dwyer performed the postmortem at the City Mortuary at 7:30 a.m. on 2 December 1948.
- Bennett examined the body at 9:40 a.m. on 1 December 1948 and estimated death up to eight hours earlier, with the estimate based on a cursory examination and rigor/cyanosis.
- Cowan received stomach contents, liver/muscle, urine and blood on 2 December 1948 and reported no signs of common poison in the submitted specimens.
- Dwyer documented external condition, rigor/lividity, dental loss, stomach congestion/blood mixed with food, organ congestion and heart findings.
- Durham documented body photographs and fingerprinting; separate fingerprint and tooth-chart reproductions are preserved.

## Partially Documented

- Poison was considered by multiple medical witnesses, but no poison was detected in the acquired primary text.
- Dwyer suggested barbiturate/soluble hypnotic possibility, Cowan found no common poison, Cleland and Hicks discussed uncommon/difficult-to-detect poison possibilities.
- Hicks's specific drug-group/exhibit terminology remains obscured in the OCR reproduction and must not be named until manually transcribed from a better source.
- Dental and fingerprint records exist, but exact specialist interpretation is not yet complete.

## Not Documented

- No acquired file provides a complete laboratory toxicology report with method-by-method analytical detail.
- No acquired file documents alcohol testing.
- No acquired file proves a specific poison was present.
- No acquired file proves the body died where it was found.
- No acquired file establishes retained biological sample status.

## Medically Unresolved

- Exact cause of death.
- Whether any toxic agent was present.
- Exact Hicks poison group/member names.
- Reliability and precision of the time-of-death estimate.
- Place of death.
- Full significance of stomach contents and liver-lobule findings.
- Whether any injection mark could have been missed.

## Claims Requiring Revision

- Revise broad claims that toxicology ruled out all poisons. The primary record supports only no signs of common poison in submitted specimens.
- Revise claims naming a specific poison unless tied to a document that directly names it and distinguishes consideration from detection.
- Revise claims that the cause of death was known. The acquired record preserves uncertainty.
- Revise any claim that alcohol testing was negative; this remains unable to verify in acquired material.
- Revise final-meal timing claims to preserve Dwyer's digestion/anxiety caveat.

## Recommendations for Mission 9

1. Build the physical evidence assessment around clothing, suitcase, Tamam Shud slip, tickets, cigarette items, thread, death mask, fingerprints and dental chart.
2. Manually transcribe DOC-0001 pages 57-77 and the non-OCR police files before making property/custody claims.
3. Treat medical exhibits C.2/C.3 and Hicks's poison-group exhibit as priority archival targets.
4. Keep toxicology phrasing strict: considered, not detected, medically discounted, unresolved.
"""

write_text(OUT / "forensic_medical_summary.md", summary)


def latex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("&", "\\&")
        .replace("%", "\\%")
        .replace("$", "\\$")
        .replace("#", "\\#")
        .replace("_", "\\_")
        .replace("{", "\\{")
        .replace("}", "\\}")
    )


def write_latex_table(path: Path, caption: str, label: str, columns: list[str], rows: list[list[str]], max_rows: int) -> None:
    body = [
        "\\begin{longtable}{p{0.16\\textwidth}p{0.23\\textwidth}p{0.19\\textwidth}p{0.14\\textwidth}p{0.18\\textwidth}}",
        f"\\caption{{{latex_escape(caption)}}}\\label{{{label}}}\\\\",
        "\\toprule",
        " & ".join(latex_escape(c) for c in columns) + " \\\\",
        "\\midrule",
        "\\endfirsthead",
        "\\toprule",
        " & ".join(latex_escape(c) for c in columns) + " \\\\",
        "\\midrule",
        "\\endhead",
    ]
    for row in rows[:max_rows]:
        body.append(" & ".join(latex_escape(cell) for cell in row) + " \\\\")
    body.extend(["\\bottomrule", "\\end{longtable}", ""])
    write_text(path, "\n".join(body))


write_latex_table(
    TABLES / "medical_observations_ready_for_latex.tex",
    "Selected Forensic-Medical Observations",
    "tab:medical-observations",
    ["ID", "Category", "Observation", "Source", "Confidence"],
    [[r[0], r[1], r[2], f"{r[3]} {r[5]}", r[8]] for r in observation_rows],
    18,
)

write_latex_table(
    TABLES / "toxicology_ready_for_latex.tex",
    "Toxicology Issues Mentioned in Primary Evidence",
    "tab:toxicology",
    ["ID", "Substance/Class", "Mentioned By", "Status", "Limitation"],
    [[r[0], r[1], r[2], r[11], r[8]] for r in toxicology_rows],
    14,
)

write_latex_table(
    TABLES / "forensic_identifiers_ready_for_latex.tex",
    "Forensic Identifiers",
    "tab:forensic-identifiers",
    ["ID", "Type", "Description", "Source", "Limitations"],
    [[r[0], r[1], r[2], r[3], r[7]] for r in identifier_rows],
    10,
)

print(f"Mission 8 artifacts written to {OUT}")
