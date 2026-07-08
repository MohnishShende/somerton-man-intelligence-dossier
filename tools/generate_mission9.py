#!/usr/bin/env python3
"""Generate Mission 9 physical-evidence and scene-reconstruction artifacts."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "physical_evidence"
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


catalogue_header = [
    "physical_evidence_id",
    "existing_evidence_id",
    "item_class",
    "description",
    "photographs",
    "measurements",
    "condition",
    "discovery",
    "recovery",
    "collector",
    "chain_of_custody",
    "custody_confidence",
    "examinations",
    "laboratory_examinations",
    "testimony_mentions",
    "report_mentions",
    "current_location",
    "current_custodian",
    "outstanding_questions",
    "confidence",
    "notes",
]

catalogue_rows = [
    ["PE-0001", "EV-0005", "body / scene", "Body of unknown male found at Somerton Beach near seawall/opposite Somerton Crippled Children's Home.", "Body photographs C.5-C.8 referenced; original set not fully preserved in repo.", "Leane later described height as 5 ft 11 in; full autopsy measurements not acquired.", "Cold, damp and stiff by Moss; later embalmed before Lawson cast.", "Found about 7 a.m. on 1948-12-01; evening observations at 7 p.m. and about 7:30 p.m. on 1948-11-30.", "Taken by Moss in police ambulance to Royal Adelaide Hospital then City Morgue.", "John Moss / police; medical examination by Bennett; postmortem by Dwyer.", "Beach to hospital to City Morgue is documented; later remains/burial/exhumation custody not fully reconstructed here.", "Fragmentary", "Scene inspection by Moss; Bennett examination; Dwyer postmortem; Lawson cast; Durham photographs/fingerprints.", "Cowan biological specimen analysis; no body-wide modern report acquired.", "DOC-0001 pp.5,15-21,27,35,63,67,93.", "DOC-0003 death certificate; DOC-0001 coroner remarks.", "Burial/exhumation status outside acquired primary detail.", "Unknown / official authorities pending current records.", "Exact body recovery log, burial/remains chain, and current official records.", "High for discovery and initial movement; Moderate for full preservation history.", "Body is catalogued as evidence context, not a cause-of-death conclusion."],
    ["PE-0002", "EV-0014", "scene object", "Partly smoked cigarette located between/right cheek and right lapel or on right collar area.", "No preserved photograph separately catalogued.", "Not recorded.", "Partly smoked; no cheek blistering or coat scorching recorded.", "Observed at body location morning of 1948-12-01; evening witness said no cigarette in raised hand.", "Collection status not established; Moss observed it and compared/considered it.", "John Moss observed; unknown if collected.", "Observation documented; physical recovery and later custody unknown.", "Fragmentary", "Moss observation; possible comparison with cigarette packet not performed by Moss.", "No laboratory/fingerprint/saliva examination documented.", "DOC-0001 pp.5,17,19,21.", "Coroner remarks p.5.", "Unknown.", "Unknown.", "Was it collected; was brand or saliva/fingerprint examined; relation to body cigarette packet?", "Moderate", "Do not treat as proven administration method."],
    ["PE-0003", "EV-0005", "clothing ensemble", "Clothing worn by deceased: coat, shoes, shirt, pullover, jockey underpants, singlet, socks, trousers and one tie.", "Clothing exhibit C.15 referenced; no full image set preserved locally.", "Garment measurements not acquired; Cleland compared fit/lengths.", "Clothing fairly good quality; shoes very clean/practically new; tags missing or removed from some items.", "On body at Somerton Beach.", "Body/clothing search by Moss; later produced by Leane as clothing found on body.", "John Moss; Raymond Leane; later Cleland examined.", "Body search to inquest exhibit documented; current custody unknown.", "Fragmentary", "Moss inventory; Leane production; Brown/Cleland comparison; label/tag observations.", "Thread/fibre microscopy by Cleland; no modern lab record.", "DOC-0001 pp.5,21,57,59,61,71,77,79,81.", "Coroner remarks p.5; exhibit index EXH-0011.", "Unknown.", "Unknown; police custody ordered in 1949.", "Exact clothing list, garment measurements, present status, destruction/loss record.", "High for existence; Moderate for item-level details.", "Keep clothing as a set plus subitems below."],
    ["PE-0004", "EV-0004", "clothing subitem", "Tie worn by deceased and two ties in suitcase, one bearing the name T. Keane.", "No item photograph preserved locally.", "Not recorded.", "One body tie; suitcase tie with name; condition not fully recorded.", "Body tie on deceased; suitcase ties recovered from luggage.", "Body clothing search / suitcase possession by Leane.", "Moss for body clothing; Leane for suitcase.", "Documented in testimony; current custody unknown.", "Fragmentary", "Inventory and name/tag relevance.", "None documented.", "DOC-0001 p.57.", "Possession inventory POS-0001/POS-0010.", "Unknown.", "Unknown.", "Which tie carried which name/mark; did any survive?", "Moderate", "Existing EV-0004 was broad; Mission 9 splits body and suitcase ties conceptually."],
    ["PE-0005", "EV-0005", "clothing subitem", "Shoes worn by deceased.", "No item photograph preserved locally.", "Size not recorded; Cleland noted fit against Cowan; Lawson inferred foot form with caution.", "Leane: practically new and very clean; Cleland: remarkably clean/polished with little sand around toe marks.", "On body.", "Body recovery and clothing search.", "Moss / Leane; examined by Cleland and Lawson.", "Documented through testimony; current custody unknown.", "Fragmentary", "Condition/fit observations; foot/calf observations.", "None documented.", "DOC-0001 pp.27,57,79,81.", "Victimology/forensic registers.", "Unknown.", "Unknown.", "Exact make, size, sole wear, photographs, survival status.", "High for existence and condition observations.", "Do not infer gait/occupation beyond witness wording."],
    ["PE-0006", "EV-0005", "clothing subitem", "Socks worn by deceased.", "No item photograph preserved locally.", "Not recorded.", "A barley-grass seed reportedly stuck in a sock; otherwise condition not fully recorded.", "On body.", "Body recovery.", "Moss / Leane; examined by Cleland.", "Documented in clothing set; current custody unknown.", "Fragmentary", "Cleland noted vegetation; did not place strong weight on it.", "None documented.", "DOC-0001 pp.57,79,81.", "Possession inventory POS-0001.", "Unknown.", "Unknown.", "Exact sock type/condition; whether vegetation retained.", "Moderate", "Vegetation context is weak due widespread barley grass."],
    ["PE-0007", "N/A", "clothing alteration / labels", "Removed/missing tags or labels from clothing and suitcase articles.", "No photographs preserved locally.", "Not applicable.", "Tags missing; Leane said some had been torn out; Cleland did not find threads proving recent removal.", "Observed on body clothing and suitcase items.", "Observed during clothing/suitcase examination.", "Leane; Cleland.", "Observation only; removed tags themselves not recovered.", "Fragmentary", "Leane and Cleland examination; coroner remarks.", "No laboratory examination documented.", "DOC-0001 pp.5,7,59,61,81.", "Verification matrix claims on label removal.", "Removed labels not located.", "None.", "Which labels were removed, when, by whom; whether any threads/remnants survive.", "Moderate", "Deliberateness remains an analytical question, not catalogued as fact."],
    ["PE-0008", "EV-0008", "ticket", "Single uncancelled second-class Adelaide-to-Henley Beach railway ticket.", "No item photograph preserved locally.", "Ticket number/serial not fully transcribed in Mission 9.", "Uncancelled per coroner remarks; physical condition unknown.", "Found in clothing search on body.", "Recovered during Moss search; produced in inquest for Townsend.", "John Moss; Douglas Townsend identified issue context.", "Body search to inquest testimony documented; current physical custody unknown.", "Fragmentary", "Ticket clerk evidence; issue window established.", "None documented.", "DOC-0001 pp.5,21,75.", "Chronology CHR-0002/0003.", "Unknown.", "Unknown.", "Exact ticket serial; current status; purchaser unknown.", "High", "Supports issued ticket, not purchaser identity."],
    ["PE-0009", "EV-0009", "ticket", "Municipal Tramways Trust bus ticket, 7d ticket tied to Holdernesse route/journal.", "No item photograph preserved locally.", "Hall: ticket serial/punch evidence; OCR gives serial-like CN 88708 but needs visual confirmation.", "Physical condition unknown.", "Found in clothing search on body.", "Recovered during Moss search; examined by Hall; Holdernesse had no recollection.", "John Moss; Edmund Leslie Hall; Arthur Holdernesse.", "Body search to inquest testimony documented; current physical custody unknown.", "Fragmentary", "Ticket punch/serial/running journal examination.", "None documented.", "DOC-0001 pp.5,21,23,25.", "Chronology CHR-0004.", "Unknown.", "Unknown.", "Exact serial; holder identity; boarding/alighting location.", "High", "Supports route/ticket issue, not that deceased personally rode."],
    ["PE-0010", "EV-0012", "cigarette packet", "Army Club cigarette packet containing Kensitas cigarettes.", "No item photograph preserved locally.", "Not recorded.", "Packet brand and contents brand differed; exact count not recorded in clean primary text.", "Found on body per Leane/Moss inventory.", "Body search.", "John Moss; Raymond Leane.", "Documented as body property; current custody unknown.", "Fragmentary", "Inventory only; Moss did not compare packet with partly smoked cigarette.", "No documented print/saliva/brand lab exam.", "DOC-0001 pp.21,57.", "Evidence register EV-0012.", "Unknown.", "Unknown.", "Was mismatch investigated; exact count; survival status.", "Moderate", "Brand mismatch is factual only if page visually confirmed."],
    ["PE-0011", "EV-0013", "matches", "Bryant and May matches box, about one quarter full per Leane OCR.", "No item photograph preserved locally.", "Quantity approx. one quarter full per OCR; needs confirmation.", "Physical condition unknown.", "Found on body.", "Body search.", "John Moss; Raymond Leane.", "Documented as body property; current custody unknown.", "Fragmentary", "Inventory only.", "None documented.", "DOC-0001 pp.21,57.", "Evidence register EV-0013.", "Unknown.", "Unknown.", "Exact match count/condition; survival status.", "Moderate", "No fire/scorch inference beyond Moss/Cleland observations."],
    ["PE-0012", "EV-0010", "personal item", "Two combs / metal comb reported in body property.", "No item photograph preserved locally.", "Not recorded.", "Condition not recorded.", "Found on body.", "Body search.", "John Moss; Raymond Leane.", "Documented as body property; current custody unknown.", "Fragmentary", "Inventory only.", "None documented.", "DOC-0001 pp.5,21,57.", "Evidence register EV-0010.", "Unknown.", "Unknown.", "Exact type/manufacturer; survival status.", "Moderate", "Prior US-manufactured claim not verified here."],
    ["PE-0013", "EV-0011", "personal item", "Juicy Fruit chewing gum packet, about half full per Leane OCR.", "No item photograph preserved locally.", "Quantity approx. half full per OCR; needs confirmation.", "Physical condition unknown.", "Found on body.", "Body search.", "John Moss; Raymond Leane.", "Documented as body property; current custody unknown.", "Fragmentary", "Inventory only.", "None documented.", "DOC-0001 pp.5,21,57.", "Evidence register EV-0011.", "Unknown.", "Unknown.", "Exact quantity/packaging; survival status.", "Moderate", "Catalogue only; no behavioural inference."],
    ["PE-0014", "EV-0001", "paper/document", "Tamam Shud paper slip found in concealed trouser fob pocket.", "Slip image lead exists; no locally preserved high-resolution exhibit photo except source leads.", "Paper described by Brown as coated wood-free art paper with stated substance; exact dimensions not acquired.", "Physical condition unknown; paper text present.", "Found in fob pocket of trousers; not found during initial Moss search; found some time afterwards.", "Found/handled by Cleland/Leane per testimony; Brown received from Leane for inquiries.", "Professor Cleland; Raymond Leane; Leonard Brown.", "Finding and inquiry documented; exact discovery date and current custody unknown.", "Fragmentary", "Paper/type comparison; bookshop/library inquiries; exhibit C.9.", "No fibre/chemical lab exam documented.", "DOC-0001 pp.5,57,71,73,81.", "Verification matrix PA2025-044/065; exhibit EXH-0009.", "Unknown.", "Unknown.", "Exact discovery date/time; original survival; paper match to recovered Rubaiyat; current custodian.", "High for existence; Moderate for custody.", "Do not infer purpose or intent."],
    ["PE-0015", "EV-0002", "book/document", "Rubaiyat copy/reference book associated with Tamam Shud comparison.", "No locally preserved image of associated original book; code image exists separately as DOC-0012/IMG lead.", "Not recorded.", "Associated original book status unknown.", "Brown compared slip to bookshop/library copies; coroner associated slip with a second edition Fitzgerald Rubaiyat.", "Associated recovery/provenance unresolved in acquired DOC-0001 pages.", "Leonard Brown; unknown finder/custody for alleged associated copy.", "Reference-copy comparison documented; original associated copy custody not complete.", "Fragmentary", "Typographic/paper comparison and library/bookshop inquiries.", "No definitive physical tear-match lab report acquired.", "DOC-0001 pp.5,71,73.", "Evidence register EV-0002; exhibit EXH-0015.", "Unknown.", "Unknown.", "Exact recovery, owner/finder, edition, tear-match, current status.", "Moderate", "Do not treat all Rubaiyat/code claims as verified by this record."],
    ["PE-0016", "N/A", "document/code image", "Rubaiyat code/markings image preserved as SM-code_full_res.jpg.", "SM-code_full_res.jpg locally preserved; 1802x1440 from prior manifest context.", "Image 1802x1440; original book/page dimensions not acquired.", "Digital image preserved; original document status unknown.", "Original code context not established from DOC-0001 testimony used in Mission 9.", "Digital acquisition from Abbott archive.", "Derek Abbott archive copy; original police/book custody unknown.", "Digital file preserved; original chain unresolved.", "Fragmentary", "No Mission 9 examination beyond preservation record.", "None documented here.", "DOC-0012 / SM-code_full_res.jpg; source register lead.", "Digital preservation manifest.", "Local digital copy in evidence/primary_sources/abbott_archive.", "Local repo copy; original custodian unknown.", "Original document provenance; relation to associated Rubaiyat; handwriting/code analysis deferred.", "Moderate for digital preservation; Low for original custody.", "Mission 12 should handle cryptographic/document analysis."],
    ["PE-0017", "EV-0003", "luggage", "Suitcase found unclaimed at Adelaide Railway Station luggage/cloak room.", "Photographs of case marked C.10-C.14 referenced; image set not preserved locally.", "Not recorded; case practically new per Leane.", "Practically new; luggage label removed; current physical status unknown.", "Located by Leane in unclaimed luggage on 1949-01-14; taken into police possession on 1949-01-19.", "Police took possession from Railway Station cloakroom/luggage office.", "Raymond Leane; Harold North produced ticket; A. Craig issued ticket but not heard directly here.", "Ticket issue and police possession documented; later custody/destruction not established.", "Fragmentary", "Inventory; ticket linkage; clothing/thread comparison; photographs C.10-C.14.", "Cowan tested stencil brush residue, not suitcase as whole.", "DOC-0001 pp.5,7,53,57,61,75,77,79.", "Chronology CHR-0017/0018.", "Unknown; reported destroyed in secondary trails but not primary-verified here.", "Unknown.", "Current status/destruction authority; full inventory; original photographs.", "High for inquest existence; Moderate for full custody.", "Do not treat suitcase ownership as proved beyond internal association evidence."],
    ["PE-0018", "N/A", "luggage ticket", "Railway Station luggage ticket no. 52703 for suitcase, issued 1948-11-30 between 11 a.m. and noon per North.", "No item photograph preserved locally.", "Ticket number 52703 per OCR; requires visual confirmation.", "Physical condition unknown.", "Produced by Harold North; associated with unclaimed suitcase.", "Ticket held/produced by cloakroom; connected to police-recovered case.", "Harold Rolfe North; A. Craig issuer absent/on holiday.", "Documented ticket production; current physical status unknown.", "Fragmentary", "Cloakroom ticket/stamp examination.", "None documented.", "DOC-0001 pp.53,57.", "Exhibit EXH-0006.", "Unknown.", "Unknown.", "Exact ticket number; retained half; depositor identity.", "High", "Ticket links case to cloakroom record, not to deceased identity by itself."],
    ["PE-0019", "EV-0003", "suitcase contents / clothing", "Suitcase clothing/textiles: dressing gown/cord, laundry bag, singlets, underpants, ties, slippers, trousers, sports coat, coat/shirt/pajamas/scarf/towel and related textiles.", "Photographs C.10-C.14 may include case contents; not preserved locally.", "Garment sizes compared generally; no full measurements.", "Well kept and tidy per Leane; some name tags missing/torn; some items with Keane/T. Keane.", "Inside suitcase.", "Recovered when Leane took possession of case.", "Raymond Leane; later Brown/Cleland examined comparisons.", "Suitcase inventory to inquest documented; later custody unknown.", "Fragmentary", "Inventory; size/brand/thread comparisons.", "Microscopic thread comparison by Cleland.", "DOC-0001 pp.57,59,61,71,79.", "Possession inventory POS-0010.", "Unknown.", "Unknown.", "Full clean transcript; exact item count; current status.", "Moderate", "OCR distortion makes full inventory provisional."],
    ["PE-0020", "N/A", "suitcase contents / tools", "Suitcase tools and personal articles: scissors, knife, stencil brush, razor strop, lighter, razor, shaving brush, screwdriver, pencils, toothbrush/paste, dish, soap dish, hair pin, safety pins, collar studs, button, spoon, broken scissors, boot polish, air-mail stickers.", "No item photographs preserved locally.", "Counts partly recorded by OCR; exact list needs confirmation.", "Condition mostly not recorded; case contents described as tidy.", "Inside suitcase.", "Recovered when Leane took possession of case.", "Raymond Leane.", "Inventory documented; current custody unknown.", "Fragmentary", "Inventory; Gray examined knife/stencilling relation; Cowan tested brush residue.", "Cowan tested stencil brush and found black substance but not composition.", "DOC-0001 pp.57,59,61.", "Possession inventory POS-0011.", "Unknown.", "Unknown.", "Exact items/counts; whether tools had occupational relevance; current status.", "Moderate", "Do not infer occupation from tools without external evidence."],
    ["PE-0021", "N/A", "pencils / writing implements", "Six pencils in suitcase; most Royal Sovereign; three H-type/drafting pencil per Leane OCR.", "No item photographs preserved locally.", "Six pencils per OCR.", "Condition not recorded.", "Inside suitcase.", "Recovered from suitcase.", "Raymond Leane.", "Inventory documented; current custody unknown.", "Fragmentary", "Inventory only.", "None documented.", "DOC-0001 p.59.", "Possession inventory POS-0011.", "Unknown.", "Unknown.", "Exact brands/grades; relation, if any, to code or drafting work.", "Moderate", "Mission 12 should handle code/writing connection, if any."],
    ["PE-0022", "N/A", "fibres/thread", "Orange/tan/warm sepia thread found in suitcase and used on body clothing repairs.", "No macro/micro photographs preserved locally.", "No measurements; Cleland says colour and fibre size corresponded microscopically.", "Physical current status unknown.", "Observed in suitcase and clothing repairs.", "Examined during property review.", "Raymond Leane; John Burton Cleland.", "Observation and microscopy documented; physical thread custody unknown.", "Fragmentary", "Cleland microscopic comparison; Leane mending notes.", "Microscopic comparison only, no report acquired.", "DOC-0001 pp.7,59,61,79.", "Chronology CHR-0018.", "Unknown.", "Unknown.", "Where samples retained; exact fibre type; lab notes/photos.", "High for testimony; Moderate for physical evidence.", "Association evidence, not ownership proof alone."],
    ["PE-0023", "N/A", "sand", "Sand at scene and sand/white beach sand particles in trouser cuffs/suitcase clothing.", "No photographs preserved locally.", "No measurements.", "Moss saw no undue disturbance; Dwyer found sand in hair; Brown/Leane noted sand in clothing/cuffs.", "Scene/body/clothing/suitcase context.", "Observed, not clearly collected.", "Moss; Dwyer; Brown; Cleland.", "Observation only; no sample custody documented.", "Unknown", "Visual/medical/property observations.", "No sand lab comparison documented.", "DOC-0001 pp.17,19,37,71,81.", "Medical observation MED-0008.", "No preserved sample documented.", "None.", "Were samples collected; did sand match Somerton/Glenelg/other locations?", "Moderate", "Scene reconstruction should treat sand evidence as observational."],
    ["PE-0024", "N/A", "vegetation", "Barley grass/stump/seed material found in trouser leg/sock according to Cleland.", "No photographs preserved locally.", "Not recorded.", "Cleland discounted significance because barley grass was widespread.", "Found in suitcase trouser leg and sock worn by deceased per Cleland testimony.", "Observed during clothing examination.", "John Burton Cleland.", "Observation only; no collection/custody documented.", "Unknown", "Cleland observation.", "No botanical lab exam documented.", "DOC-0001 pp.79,81.", "None.", "No preserved sample documented.", "None.", "Exact plant material; whether retained; environmental origin.", "Low", "Low weight due witness caveat and lack of custody."],
    ["PE-0025", "EV-0015", "fingerprints", "Fingerprints/fingerprint chart of deceased.", "DOC-0016 fingerprints.pdf preserved; Durham photographs/prints referenced.", "Chart image size not formally measured; classification marks visible.", "Digital reproduction legible but image quality moderate; original chart unknown.", "Fingerprinted at City Morgue on 1948-12-03 per Durham testimony.", "Durham took prints and circulated copies.", "Patrick James Durham.", "Print-taking/circulation documented; original chart and bureau replies incomplete.", "Fragmentary", "Fingerprint circulation to Australian states, New Zealand and overseas bureaus.", "Fingerprint comparison/search; no hit per Durham testimony.", "DOC-0001 pp.63,67; DOC-0016.", "Forensic identifiers FID-0003/FID-0004.", "Local digital reproduction; original unknown.", "Local repo copy; original police/archive custodian unknown.", "Original chart; complete circulation log; comparison standards/results.", "High for existence; Moderate for custody.", "Specialist fingerprint review remains future work."],
    ["PE-0026", "EV-0016", "dental chart/teeth", "Teeth chart and dental observations for deceased.", "DOC-0017 teeth.pdf preserved.", "Chart notation visible but not specialist-transcribed; several/many missing teeth.", "Digital chart legible enough for indexing; original unknown.", "Prepared from postmortem/dental examination; Dwyer handed chart to Constable Sutherland.", "Chart put in as exhibit C.2.", "John Matthew Dwyer; Constable Sutherland.", "Chart creation and exhibit marking documented; original custody unknown.", "Fragmentary", "Dental charting; Dwyer/Cleland observations.", "No comparative dental lab record acquired.", "DOC-0001 pp.35,39,41,67; DOC-0017.", "Forensic identifiers FID-0001/FID-0002.", "Local digital reproduction; original unknown.", "Local repo copy; original police/archive custodian unknown.", "Exact notation; comparative dental search; original chart custody.", "High for existence; Moderate for exact details.", "Requires forensic odontologist/manual transcription."],
    ["PE-0027", "EV-0007", "death mask / bust", "Mould/cast/bust of deceased features made by Lawson and marked exhibit C.17.", "No local image of bust; image catalogue lead FIG-0004.", "Bust/cast dimensions not acquired.", "Lawson said formalin/embalming and postmortem change affected appearance.", "Made at City Mortuary on 1949-06-07.", "Produced in court; coroner ordered police custody.", "Paul Francis Lawson; Raymond Leane.", "Creation and inquest custody order documented; present custodian unknown.", "Fragmentary", "Identification/death-mask documentation.", "No lab examination documented in acquired primary material.", "DOC-0001 pp.27,77.", "FID-0006; EXH-0013.", "Unknown in acquired primary material.", "Unknown; secondary trails require verification.", "Current custodian, accession, hair sampling status, preservation history.", "High for creation; Low for current custody.", "Hair/DNA claims not verified in Mission 9 primary archive."],
    ["PE-0028", "EV-0006", "hair", "Hair associated with body/death mask/remains as later potential evidence.", "No local primary hair image.", "Not recorded.", "No primary preservation condition acquired.", "Possible death-mask or exhumation context in later source trails; not established by acquired DOC-0001.", "Not documented in acquired primary case file.", "Unknown.", "Primary custody not established.", "Unknown", "None in acquired primary material except hair description on body.", "No acquired DNA/hair lab record.", "DOC-0001 pp.35,67 for hair appearance only.", "Evidence register EV-0006.", "Unknown.", "Unknown official custodian.", "Official sample source, chain, lab reports, current status.", "Low", "Included because user-specified and prior register exists, but primary support is weak."],
    ["PE-0029", "EV-0017", "biological samples", "Stomach contents, liver/muscle, urine and blood submitted for toxicology.", "No photographs preserved locally.", "Containers: glass jars/bottles per Cowan; volumes not recorded.", "Submitted specimens analyzed in 1948; current physical availability likely unknown.", "Taken from body/postmortem; received by Cowan 1948-12-02.", "Cowan received from P.C. Sutherland.", "P.C. Sutherland; Robert James Cowan; Dwyer retained specimens.", "Creation/submission documented; lab retention/disposal not documented.", "Fragmentary", "Cowan toxicology; Dwyer specimen retention.", "Common-poison analysis; no common poison detected.", "DOC-0001 pp.39,47,49.", "Toxicology register TOX-0001.", "Unknown; likely unavailable but not primary-verified.", "Unknown.", "Original lab report; retention/disposal; analyte methods.", "High for 1948 submission; Low for present preservation.", "Separate medical/toxicology layer has details."],
    ["PE-0030", "EV-0003", "suitcase preservation / photographs", "Photographs of the suitcase/case marked exhibits C.10-C.14.", "Photographs referenced; no local copies identified.", "Not recorded.", "Original photograph condition unknown.", "Produced/marked during inquest.", "Inquest exhibit process.", "Unknown photographer/investigator; Townsend page references marking.", "Existence as exhibit reference documented; actual photos/custody unknown.", "Fragmentary", "Photographic property documentation.", "None documented.", "DOC-0001 p.75.", "EXH-0010.", "Unknown.", "Unknown.", "Locate photographs C.10-C.14; rights/custody; image quality.", "Moderate", "Priority acquisition target."],
    ["PE-0031", "EV-0005", "body photographs", "Full-face and side-face photographs of body, exhibits C.5-C.8.", "Photos referenced; some reproductions may exist but not fully catalogued here.", "Not recorded.", "Original photograph condition unknown.", "Taken at City Morgue on 1948-12-03.", "Durham photographed body and produced photographs.", "Patrick James Durham.", "Photo creation/circulation documented; original custody unknown.", "Fragmentary", "Identification circulation; exhibit production.", "Photographic identification only.", "DOC-0001 p.63.", "EXH-0007; FID-0005.", "Unknown.", "Unknown.", "Locate full set C.5-C.8; current rights/custody.", "High for creation; Moderate for custody.", "Do not use public images until rights/custody cleared."],
    ["PE-0032", "N/A", "scene environment", "Weather/environmental conditions around 30 November 1948 and scene openness/publicness.", "No scene photographs preserved locally.", "Temperatures and visibility recorded by Leane; exact distances from body to steps/wall partly witness-estimated.", "Warm/hazy conditions; scene public/open; sand disturbance not undue per Moss.", "Observed/reported in witness and police testimony.", "Not a recoverable object.", "Moss; beach witnesses; Leane.", "Not applicable.", "N/A", "Witness observations and weather record testimony.", "None.", "DOC-0001 pp.15,17,19,21,51,67.", "Chronology/scene reconstruction.", "Not applicable.", "Not applicable.", "Need official weather record and scene diagrams/photos.", "Moderate", "Environmental context, not physical exhibit."],
    ["PE-0033", "N/A", "money/cash", "2s 6d in cash reportedly found in trousers pocket per Leane OCR.", "No photograph preserved locally.", "2s 6d per OCR; requires visual confirmation.", "Physical status unknown.", "Trousers pocket, likely body clothing inventory.", "Inventory/recovery context unclear due OCR.", "Raymond Leane.", "Mention documented in OCR; current custody unknown.", "Unknown", "Inventory only.", "None.", "DOC-0001 p.59.", "Victimology note.", "Unknown.", "Unknown.", "Confirm exact amount and whether body or suitcase trousers.", "Low", "Needs manual page confirmation before narrative use."],
    ["PE-0034", "N/A", "stencil materials", "Stencil brush, cut-down knife, tinned zinc/folders used or possibly used for stencilling.", "No photographs preserved locally.", "Not recorded.", "Brush had black substance; exact composition unknown.", "Inside suitcase.", "Recovered from suitcase.", "Raymond Leane; examined by Mr Gray and Cowan.", "Inventory and limited examination documented; custody unknown.", "Fragmentary", "Gray examined knife/zinc relation; Cowan tested brush use/residue.", "Cowan found brush had been used but substance unidentified.", "DOC-0001 pp.59,61.", "Possession inventory POS-0011.", "Unknown.", "Unknown.", "Full item list; residue report; occupational relevance.", "Moderate", "Do not infer trade without employment records."],
]


scene_header = [
    "scene_component_id",
    "scene_component",
    "location",
    "orientation",
    "position",
    "nearby_objects",
    "distances",
    "environmental_conditions",
    "witnesses",
    "photographs",
    "source",
    "confidence",
    "uncertainty_flags",
]

scene_rows = [
    ["SCN-0001", "Body location", "Somerton Beach foreshore near seawall/opposite Somerton Crippled Children's Home.", "Near seawall; feet toward sea/west per Moss/coroner.", "On back; head/shoulders supported by seawall; head inclined right.", "Partly smoked cigarette near right cheek/lapel/collar.", "Evening witness estimated within a yard of steps; closest viewing 15-20 yards.", "Warm morning; previous evening public summer beach context.", "WIT-0001; WIT-0002; WIT-0006; WIT-0009.", "Body photos C.5-C.8 referenced but not locally preserved as image set.", "DOC-0001 pp.5,15,17,19,51.", "High", "Exact coordinates and scene diagram absent; evening body identity not proven."],
    ["SCN-0002", "Body orientation", "Beach against seawall.", "Feet towards sea/west; head/right shoulder against wall.", "Right arm doubled over palm upward/fingers bent; left arm alongside body per Moss.", "Cigarette near cheek/collar; clothing and pocket items on body.", "Not measured.", "Open public location; steps used often on summer evenings.", "WIT-0002.", "Body photos referenced.", "DOC-0001 p.19.", "High", "No original scene sketch acquired."],
    ["SCN-0003", "Evening 7 p.m. observation", "Same place where body later found, per coroner/witness.", "Man lying near steps/seawall.", "Witness saw right arm extend upward and fall.", "No cigarette seen in hand by witness.", "Witness distance 15-20 yards per page 15.", "Fairly light; summer evening.", "WIT-0001.", "None acquired.", "DOC-0001 pp.5,15,17.", "High for reported observation", "Witness did not see face; not proof observed man was deceased."],
    ["SCN-0004", "Evening 7:20-7:30 observation", "Somerton Beach near body location.", "Limited view of legs/body from steps/beach.", "Neill saw legs; position did not alter while she watched.", "None observed.", "Not precisely recorded.", "Not many people nearby; public place.", "WIT-0006; WIT-0009.", "None acquired.", "DOC-0001 pp.31-33,51.", "Moderate", "Identity not proved; visibility and attention limited."],
    ["SCN-0005", "Morning body discovery", "Same location near seawall.", "Body visible from right at distance; open not secluded.", "Cold, damp and stiff; no visible violence.", "Partly smoked cigarette; no hat; no suspicious nearby object.", "No measured distance; witness/body near steps.", "Hot morning; no undue sand disturbance per Moss.", "WIT-0001; WIT-0002.", "Body photos later at morgue, not scene photos.", "DOC-0001 pp.17,19,21.", "High", "Exact first-discovery sequence and witness name still need visual check."],
    ["SCN-0006", "Sand/disturbance", "Around body at Somerton Beach.", "Around body/near head/feet.", "Moss found no undue disturbance; later witnesses note sand constraints.", "Sand in hair; sand around toe marks; possible beach sand in clothing/suitcase.", "Not measured.", "Sand surface likely disturbed by later activity, per Hicks caveat.", "WIT-0001; WIT-0002; WIT-0007; WIT-0016; WIT-0017.", "No close scene photos acquired.", "DOC-0001 pp.17,19,37,71,81,99.", "Moderate", "No collected sand sample or scene grid."],
    ["SCN-0007", "Cigarette placement", "Right cheek/lapel/collar area.", "Held by cheek/collar; no scorch/blister.", "Partly smoked; not smoked as far as ordinary person might smoke per Cleland questioning.", "Body clothing.", "Not measured.", "No scorching despite placement.", "WIT-0002; WIT-0001.", "No specific photo acquired.", "DOC-0001 pp.5,17,19,21.", "Moderate", "Collection status unknown; relation to packet unknown."],
    ["SCN-0008", "Initial body property", "Body clothing/pockets.", "On/in clothing.", "Rail ticket, bus ticket, cigarettes/matches, combs, gum; Tamam Shud slip not found initially.", "Body/clothing ensemble.", "Not applicable.", "Initial search at beach/hospital/mortuary sequence needs more detail.", "WIT-0002; WIT-0011.", "No property photos acquired.", "DOC-0001 pp.5,21,57.", "High", "Exact search sequence and pocket locations incomplete."],
    ["SCN-0009", "Fob pocket", "Trousers on body, right of fly per Cleland.", "Concealed/difficult pocket.", "Tamam Shud slip found there; Cleland said pocket easily missed.", "Body trousers/clothing.", "Not applicable.", "Not applicable.", "WIT-0016; WIT-0011; WIT-0014.", "Slip photo lead only.", "DOC-0001 pp.5,57,71,81.", "High", "Exact discovery date/time unresolved."],
    ["SCN-0010", "Suitcase location", "Adelaide Railway Station luggage office/cloak room.", "On rack among unclaimed luggage.", "Case lodged 1948-11-30; unclaimed; seen 1949-01-14; taken 1949-01-19.", "Luggage ticket no. 52703; suitcase contents.", "Not applicable.", "Railway station storage context.", "WIT-0010; WIT-0011.", "Case photos C.10-C.14 referenced.", "DOC-0001 pp.53,57,75,77.", "High", "Depositor identity unknown; A. Craig not directly heard."],
    ["SCN-0011", "Suitcase contents arrangement", "Inside suitcase.", "Not recorded.", "Clothing, tools, toiletries, thread, stencil items, cash/other items listed by Leane.", "Suitcase and luggage ticket.", "Not recorded.", "Unclaimed luggage storage.", "WIT-0011; WIT-0016.", "Case photos referenced.", "DOC-0001 pp.57-61,79.", "Moderate", "OCR distortion; no complete verified layout."],
    ["SCN-0012", "Clothing association", "Body clothing and suitcase clothing.", "Comparison across body and suitcase.", "Similar sizes, similar shirts/underpants, warm sepia/orange thread, missing tags.", "Clothing, thread, labels.", "Garment lengths/fits not precisely measured in acquired text.", "Not applicable.", "WIT-0011; WIT-0014; WIT-0016.", "No garment photos acquired.", "DOC-0001 pp.7,59,61,71,79,81.", "High for association observations", "Ownership and timing of tag removal unresolved."],
    ["SCN-0013", "Photographic evidence creation", "City Morgue / inquest.", "Full-face and side-face body photos; suitcase photos.", "Photographs produced/marked but not fully acquired.", "Body, suitcase, Tamam Shud paper photo.", "Not recorded.", "Post-discovery documentation.", "WIT-0012; WIT-0011.", "C.5-C.8 and C.10-C.14 referenced.", "DOC-0001 pp.63,75.", "Moderate", "Original image set/custody missing."],
    ["SCN-0014", "Biological sample path", "Postmortem to analyst.", "Specimens in jars/bottles.", "Stomach contents, liver/muscle, urine, blood received by Cowan.", "Body/postmortem.", "Volumes not recorded.", "Medical evidence context.", "WIT-0007; WIT-0008.", "No photos acquired.", "DOC-0001 pp.39,47.", "High for 1948 transfer", "Retention/disposal unknown."],
]


custody_header = [
    "custody_id",
    "physical_evidence_id",
    "item",
    "creation_or_discovery",
    "first_collector_or_observer",
    "documented_handoffs",
    "current_location",
    "custody_status",
    "confidence",
    "custody_gaps",
    "recommended_action",
]

custody_rows = []
for idx, row in enumerate(catalogue_rows, start=1):
    pe_id, _, _, description = row[0], row[1], row[2], row[3]
    discovery, collector, current, status, confidence = row[7], row[9], row[16], row[11], row[19]
    gaps = row[18]
    action = "Locate original custodian file or destruction/preservation record; update catalogue when verified."
    custody_rows.append([
        f"PECOC-{idx:04d}",
        pe_id,
        description[:120],
        discovery,
        collector,
        row[10],
        current,
        status,
        confidence,
        gaps,
        action,
    ])


source_map_header = [
    "map_id",
    "physical_evidence_id",
    "document_id",
    "page_reference",
    "witness_or_source",
    "evidence_relation",
    "mapped_content",
    "confidence",
]

source_map_rows = [
    ["PSM-0001", "PE-0001", "DOC-0001", "pp.5,19", "Coroner; John Moss", "scene/body", "Body found near seawall, position and initial movement to hospital/morgue.", "High"],
    ["PSM-0002", "PE-0001", "DOC-0001", "pp.35,93", "Dwyer; Bennett", "medical/body", "Postmortem/examination references to body.", "High"],
    ["PSM-0003", "PE-0002", "DOC-0001", "pp.5,17,19,21", "Coroner; beach witness; Moss", "scene object", "Partly smoked cigarette observed near body; no cigarette in raised hand previous evening.", "Moderate"],
    ["PSM-0004", "PE-0003", "DOC-0001", "pp.21,57,77,79,81", "Moss; Leane; Cleland", "clothing", "Body clothing searched, produced, exhibited and compared.", "High"],
    ["PSM-0005", "PE-0007", "DOC-0001", "pp.5,7,59,81", "Coroner; Leane; Cleland", "labels", "Tags/labels missing or removed; recency uncertain.", "Moderate"],
    ["PSM-0006", "PE-0008", "DOC-0001", "pp.5,21,75", "Moss; Townsend", "ticket", "Rail ticket found on body and issue window identified.", "High"],
    ["PSM-0007", "PE-0009", "DOC-0001", "pp.5,21,23,25", "Moss; Hall; Holdernesse", "ticket", "Bus ticket found and tied to route/journal; conductor had no recollection.", "High"],
    ["PSM-0008", "PE-0010", "DOC-0001", "pp.21,57", "Moss; Leane", "body property", "Cigarette packet and contents described.", "Moderate"],
    ["PSM-0009", "PE-0011", "DOC-0001", "pp.21,57", "Moss; Leane", "body property", "Matches box described.", "Moderate"],
    ["PSM-0010", "PE-0012", "DOC-0001", "pp.5,21,57", "Coroner; Moss; Leane", "body property", "Combs found on body.", "Moderate"],
    ["PSM-0011", "PE-0013", "DOC-0001", "pp.5,21,57", "Coroner; Moss; Leane", "body property", "Chewing gum packet found on body.", "Moderate"],
    ["PSM-0012", "PE-0014", "DOC-0001", "pp.5,57,71,73,81", "Coroner; Leane; Brown; Cleland", "paper slip", "Tamam Shud slip, fob pocket, paper/type inquiry and exhibit marking.", "High"],
    ["PSM-0013", "PE-0015", "DOC-0001", "pp.5,71,73", "Coroner; Brown", "Rubaiyat", "Reference-copy comparison and meaning inquiry.", "Moderate"],
    ["PSM-0014", "PE-0016", "DOC-0012", "file", "Abbott archive digital file", "code image", "Preserved code image; original custody unresolved.", "Moderate"],
    ["PSM-0015", "PE-0017", "DOC-0001", "pp.53,57,75,77", "North; Leane; coroner", "suitcase", "Suitcase ticket, police possession, photos and exhibit C.16.", "High"],
    ["PSM-0016", "PE-0018", "DOC-0001", "pp.53,57", "North; Leane", "luggage ticket", "Ticket no. 52703 and cloakroom issue context.", "High"],
    ["PSM-0017", "PE-0019", "DOC-0001", "pp.57,59,61,79", "Leane; Cleland", "suitcase contents", "Clothing/textile inventory and fit/thread comparisons.", "Moderate"],
    ["PSM-0018", "PE-0020", "DOC-0001", "pp.57,59,61", "Leane", "suitcase contents", "Tools/toiletries/personal articles inventory.", "Moderate"],
    ["PSM-0019", "PE-0021", "DOC-0001", "p.59", "Leane", "pencils", "Six pencils and H-type/drafting mention.", "Moderate"],
    ["PSM-0020", "PE-0022", "DOC-0001", "pp.7,59,61,79", "Coroner; Leane; Cleland", "fibres/thread", "Thread used on body clothing and suitcase items; microscopy comparison.", "High"],
    ["PSM-0021", "PE-0023", "DOC-0001", "pp.17,19,37,71,81,99", "Witnesses; Dwyer; Brown; Cleland; Hicks", "sand", "Sand disturbance and sand in hair/clothing observations.", "Moderate"],
    ["PSM-0022", "PE-0024", "DOC-0001", "pp.79,81", "Cleland", "vegetation", "Barley grass/seed observation with low-weight caveat.", "Low"],
    ["PSM-0023", "PE-0025", "DOC-0001", "pp.63,67", "Durham; Leane", "fingerprints", "Fingerprinting, circulation and no identification.", "High"],
    ["PSM-0024", "PE-0025", "DOC-0016", "p.1", "Fingerprint chart", "fingerprints", "Preserved fingerprint chart reproduction.", "High"],
    ["PSM-0025", "PE-0026", "DOC-0001", "pp.35,39,41,67", "Dwyer; Leane", "teeth", "Missing teeth and dental chart exhibit.", "High"],
    ["PSM-0026", "PE-0026", "DOC-0017", "p.1", "Dental chart", "teeth", "Preserved dental chart reproduction.", "High"],
    ["PSM-0027", "PE-0027", "DOC-0001", "pp.27,77", "Lawson; Leane", "death mask/bust", "Cast creation and exhibit C.17 custody order.", "High"],
    ["PSM-0028", "PE-0029", "DOC-0001", "pp.39,47,49", "Dwyer; Cowan", "biological samples", "Specimens retained/sent/analysed.", "High"],
    ["PSM-0029", "PE-0030", "DOC-0001", "p.75", "Inquest exhibit record", "photographs", "Case photographs marked C.10-C.14.", "Moderate"],
    ["PSM-0030", "PE-0031", "DOC-0001", "p.63", "Durham", "photographs", "Body photographs C.5-C.8 and circulation.", "High"],
    ["PSM-0031", "PE-0032", "DOC-0001", "pp.15,17,19,21,51,67", "Witnesses; Leane", "environment", "Open/public beach and weather context.", "Moderate"],
    ["PSM-0032", "PE-0033", "DOC-0001", "p.59", "Leane", "cash", "2s 6d in trousers pocket per OCR.", "Low"],
    ["PSM-0033", "PE-0034", "DOC-0001", "pp.59,61", "Leane", "stencil materials", "Knife, zinc, stencil brush and Cowan residue test.", "Moderate"],
]


preservation_header = [
    "preservation_id",
    "physical_evidence_id",
    "item",
    "known_preserved_form",
    "local_file_or_record",
    "archive_or_current_custodian",
    "preservation_status",
    "rights_or_access_notes",
    "next_preservation_action",
]

preservation_rows = [
    ["PRH-0001", "PE-0016", "Rubaiyat code image", "Digital JPG reproduction", "evidence/primary_sources/abbott_archive/SM-code_full_res.jpg", "Abbott archive reproduction; original unknown", "Preserved locally as digital copy", "Rights/custody unclear", "Document checksum/resolution in image catalogue and acquire provenance."],
    ["PRH-0002", "PE-0025", "Fingerprint chart", "Digital PDF reproduction", "evidence/primary_sources/abbott_archive/fingerprints.pdf", "Abbott archive reproduction; original police/archive unknown", "Preserved locally as digital copy", "Rights/custody unclear", "Specialist transcription and original custody inquiry."],
    ["PRH-0003", "PE-0026", "Dental chart", "Digital PDF reproduction", "evidence/primary_sources/abbott_archive/teeth.pdf", "Abbott archive reproduction; original police/archive unknown", "Preserved locally as digital copy", "Rights/custody unclear", "Forensic odontology transcription and original custody inquiry."],
    ["PRH-0004", "PE-0031", "Body photographs", "Referenced in DOC-0001 as exhibits", "Not separately preserved in Mission 9", "Original custodian unknown", "Located as reference only", "Need rights before publication", "Locate C.5-C.8 image set."],
    ["PRH-0005", "PE-0030", "Suitcase photographs", "Referenced in DOC-0001 as exhibits", "Not separately preserved in Mission 9", "Original custodian unknown", "Located as reference only", "Need rights before publication", "Locate C.10-C.14 image set."],
    ["PRH-0006", "PE-0027", "Death mask/bust", "Physical object reported in testimony; possible current secondary trails", "No local image/object file", "Unknown in acquired primary archive", "Unverified current status", "Custodian permission required", "Identify current custodian and accession number."],
    ["PRH-0007", "PE-0017", "Suitcase", "Physical object/exhibit in 1949; current status unknown", "DOC-0001 testimony only", "Police custody ordered in 1949", "Unknown; destruction not primary-verified", "Access by custodian record", "Seek police/coroner destruction or retention record."],
    ["PRH-0008", "PE-0003", "Body clothing", "Physical exhibit in 1949; current status unknown", "DOC-0001 testimony only", "Police custody ordered in 1949", "Unknown", "Access by custodian record", "Seek evidence inventory/preservation/destruction record."],
    ["PRH-0009", "PE-0014", "Tamam Shud slip", "Physical exhibit in 1949; current status unknown", "DOC-0001 testimony only; image lead exists", "Police/coroner custody unknown", "Unknown", "Access by custodian record", "Locate original or best scan and custody file."],
    ["PRH-0010", "PE-0029", "Biological specimens", "1948 specimens documented; current status unknown", "DOC-0001 testimony only", "Government analyst/lab/coroner unknown", "Likely unavailable but not primary-verified", "Potentially restricted medical/legal records", "Seek lab retention/disposal record."],
]


uncertainty_header = ["uncertainty_id", "physical_evidence_id", "question", "evidence_bearing_on_question", "current_status", "priority", "recommended_source_or_action"]
uncertainty_rows = [
    ["PEU-0001", "PE-0014", "When exactly was the Tamam Shud slip found and by whom?", "Coroner says not found for some time; Brown says received from Leane; Cleland describes fob pocket.", "Unresolved", "Critical", "Official inquest file pages beyond OCR; police property notes."],
    ["PEU-0002", "PE-0017", "Who deposited the suitcase and does the ticket prove association with the deceased?", "North/Leane prove unclaimed suitcase and internal association evidence; depositor unidentified.", "Unresolved", "Critical", "Railway cloakroom records; police notebook; A. Craig statement if extant."],
    ["PEU-0003", "PE-0007", "Were labels deliberately removed before death?", "Tags missing/torn; Cleland did not find threads showing recent removal.", "Unresolved", "High", "High-resolution garment photos; textile examination report."],
    ["PEU-0004", "PE-0002", "Was the partly smoked cigarette collected and examined?", "Moss observed; no collection/lab record found.", "Unknown", "High", "Scene property inventory; police evidence receipt."],
    ["PEU-0005", "PE-0022", "Was the thread physically retained or only observed?", "Cleland testified microscopic correspondence; no lab record acquired.", "Unknown", "High", "Exhibit/property custody file; microscope notes."],
    ["PEU-0006", "PE-0031", "Where are the body photographs C.5-C.8?", "Durham produced them and they were marked/returned in part.", "Unknown", "High", "Archive/photo collection inquiry."],
    ["PEU-0007", "PE-0030", "Where are suitcase photographs C.10-C.14?", "Marked on p.75; not preserved locally.", "Unknown", "High", "Archive/photo collection inquiry."],
    ["PEU-0008", "PE-0029", "Were biological samples retained?", "Cowan received and tested specimens; no retention/disposal file acquired.", "Unknown", "Critical", "Government analyst/lab archive; coroner/SAPOL/FSSA records."],
    ["PEU-0009", "PE-0027", "What is the current status/custodian of the death mask or bust?", "Lawson made it and police custody ordered; present status not in acquired primary text.", "Unknown", "High", "SAPOL Historical Society / museum / coroner archive inquiry."],
    ["PEU-0010", "PE-0015", "What happened to the associated Rubaiyat copy?", "Brown compared slip to copies; original associated book provenance unresolved here.", "Unresolved", "Critical", "Police file 1958 visual review; CIB records; Abbott archive source trail."],
]


write_csv(OUT / "physical_evidence_catalogue.csv", catalogue_header, catalogue_rows)
write_csv(OUT / "scene_reconstruction_database.csv", scene_header, scene_rows)
write_csv(OUT / "chain_of_custody_confidence_matrix.csv", custody_header, custody_rows)
write_csv(OUT / "physical_evidence_source_map.csv", source_map_header, source_map_rows)
write_csv(OUT / "preservation_history.csv", preservation_header, preservation_rows)
write_csv(OUT / "physical_evidence_uncertainties.csv", uncertainty_header, uncertainty_rows)


summary = f"""
# Mission 9 Physical Evidence & Scene Reconstruction Summary

Scope: physical evidence and scene reconstruction only. This is not dossier narrative and does not evaluate motive, suicide, homicide, espionage, or final cause of death.

## Outputs Created

- `physical_evidence_catalogue.csv`: {len(catalogue_rows)} museum-style physical evidence entries.
- `scene_reconstruction_database.csv`: {len(scene_rows)} scene reconstruction components.
- `chain_of_custody_confidence_matrix.csv`: {len(custody_rows)} custody confidence entries.
- `physical_evidence_source_map.csv`: {len(source_map_rows)} evidence-source mappings.
- `preservation_history.csv`: {len(preservation_rows)} preservation-status entries.
- `physical_evidence_uncertainties.csv`: {len(uncertainty_rows)} unresolved physical-evidence questions.

## Custody Confidence Distribution

- Complete: 0
- Mostly complete: 0
- Fragmentary: 29
- Unknown: 4
- Lost: 0
- N/A: 1

The custody picture is the real signal of Mission 9: the case has many documented objects, but few complete custody trails. The body/property existence layer is strong; the preservation/current-custodian layer is weak.

## Strongest Physical Evidence Facts

- The body position near the seawall is well supported by coroner remarks and Moss testimony.
- The body clothing and initial pocket items are supported by Moss and Leane testimony.
- The rail and bus tickets are supported by Moss plus ticket/transport witnesses.
- The suitcase was an unclaimed Adelaide Railway Station item seen by Leane on 14 January 1949 and taken by police on 19 January 1949.
- The Tamam Shud slip existed, was associated with the trouser fob pocket, and was compared by Brown with Rubaiyat copies.
- Fingerprints, body photographs, dental chart and bust/cast were created or marked in the 1949 inquest record.

## Major Gaps

- Current location/custodian for most physical objects.
- Exact discovery date/time and finder sequence for the Tamam Shud slip.
- Full clean suitcase inventory and layout.
- Complete custody of the associated Rubaiyat copy.
- Whether cigarette, sand, vegetation, labels, thread, or biological samples were retained.
- Original body/suitcase photographs and publication rights.
- Evidence destruction or retention records.

## Claims Requiring Careful Revision

- Do not state suitcase ownership as fact; the acquired record supports internal association evidence, not depositor identity.
- Do not state label removal timing or intent as fact.
- Do not state the cigarette was examined or linked to poisoning.
- Do not treat sand/vegetation as location proof without samples or lab comparison.
- Do not use code/Rubaiyat claims until Mission 12 documentary analysis.

## Recommendations for Mission 10

1. Build witness reliability around object-specific testimony: Moss, early beach witness, Neill/Strapps, North, Leane, Brown, Durham, Cleland.
2. Assign each witness statement to direct observation, memory/recollection, expert examination, or inference.
3. Flag contradictions between scene position, evening sightings, body identity, and property assumptions.
4. Prioritize manual transcription of DOC-0001 pp.15-25 and 51-77 before final witness scoring.
"""

write_text(OUT / "physical_evidence_summary.md", summary)


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


def write_latex_table(path: Path, caption: str, label: str, columns: list[str], rows: list[list[str]]) -> None:
    body = [
        "\\begin{longtable}{p{0.14\\textwidth}p{0.24\\textwidth}p{0.18\\textwidth}p{0.16\\textwidth}p{0.18\\textwidth}}",
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
    for row in rows:
        body.append(" & ".join(latex_escape(cell) for cell in row) + " \\\\")
    body.extend(["\\bottomrule", "\\end{longtable}", ""])
    write_text(path, "\n".join(body))


write_latex_table(
    TABLES / "physical_evidence_catalogue_ready_for_latex.tex",
    "Selected Physical Evidence Catalogue",
    "tab:physical-evidence-catalogue",
    ["ID", "Item", "Source", "Custody", "Confidence"],
    [[r[0], r[3], r[14], r[11], r[19]] for r in catalogue_rows[:16]],
)

write_latex_table(
    TABLES / "scene_reconstruction_ready_for_latex.tex",
    "Scene Reconstruction Components",
    "tab:scene-reconstruction",
    ["ID", "Component", "Position", "Source", "Confidence"],
    [[r[0], r[1], r[4], r[10], r[11]] for r in scene_rows],
)

write_latex_table(
    TABLES / "chain_of_custody_ready_for_latex.tex",
    "Chain-of-Custody Confidence Matrix",
    "tab:chain-of-custody",
    ["ID", "Item", "Discovery", "Custody", "Gaps"],
    [[r[1], r[2], r[3], r[7], r[9]] for r in custody_rows[:18]],
)

print(f"Mission 9 artifacts written to {OUT}")
