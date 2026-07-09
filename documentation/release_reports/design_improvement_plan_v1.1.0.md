# Version 1.1.0 Design Improvement Plan

Date: 2026-07-09

Revision rule: Presentation only. Do not change factual content, conclusions, chronology, evidence, confidence assessments, citations, or analytical wording.

## Implemented in Version 1.1.0

1. Title page
   - Reframed as `Version 1.1.0: Editorial & Design Edition`.
   - Added restrained title-page rule and left-aligned monograph composition.
   - Improved hierarchy between version, title, subtitle, dossier description, author, date, and edition note.

2. Page architecture
   - Refined page geometry for better line length and page rhythm.
   - Added more deliberate head separation and bottom margin balance.
   - Preserved one-sided output for digital/desktop reading compatibility.

3. Typography
   - Retained TeX Gyre Pagella/Heros/Cursor for archival reliability.
   - Added slight leading improvement.
   - Strengthened widow, orphan, and broken-line penalties.
   - Improved chapter, section, and subsection hierarchy.

4. Navigation
   - Added explicit `bookmark` support.
   - Opened PDF bookmarks by default to chapter level.
   - Updated PDF metadata for Version 1.1.0.
   - Replaced generic running heads with chapter-aware running heads.

5. Tables and captions
   - Added professional caption styling.
   - Added restrained alternating table rows.
   - Standardized rule color and table spacing.
   - Preserved existing table content and numbering.
   - Applied one table-only font-size adjustment to eliminate a minor overfull line.

6. Visual communication system
   - Refined `\classification`.
   - Added reusable macros for evidence, findings, intelligence assessment, cautions, and intelligence gaps.
   - Used restrained print-safe colors rather than decorative graphics.

## Deferred

- Figure insertion and figure redesign, pending rights and provenance resolution.
- Map redesign, pending authoritative map assets or source-cleared base maps.
- Full timeline redesign, pending a dedicated timeline environment or external figure workflow.
- Full PDF/UA tagging, pending a specialized accessibility production pass.
- Two-sided print imposition, pending a print-edition decision.

## Recommended Next Steps

1. Obtain external subject-matter review from a historian, forensic scientist, archivist, or experienced investigator.
2. Resolve image and map rights before adding figures.
3. Consider a separate print edition with `twoside` geometry after final page count stabilizes.
4. Run a dedicated accessibility pass if the PDF will be publicly distributed as the definitive digital edition.
