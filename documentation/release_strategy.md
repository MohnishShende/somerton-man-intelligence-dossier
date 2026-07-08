# Release Strategy

This project should be published as a versioned research archive rather than a static PDF.

## Release Contents

Each public release should include:

- LaTeX-generated PDF dossier
- Complete evidence database CSV files
- Source register and bibliography
- Verification matrix
- Chronology database
- Person, location, witness and exhibit registers
- Forensic-medical and physical-evidence registers
- Structured analytic assessment files
- Public-domain or permission-cleared images only
- Methodology notes explaining how conclusions were reached

## Versioning Model

Use version numbers to describe research maturity, not just file changes.

Suggested examples:

- `v1.0` - first public evidence-backed dossier
- `v1.1` - chronology improvements
- `v1.2` - new primary sources
- `v1.3` - DNA or identity-status updates
- `v1.4` - medical review updates
- `v2.0` - expanded intelligence assessment or major analytical revision

## Release Requirements

Before tagging a release:

- Every published factual claim must trace to one or more source IDs.
- Every analytical conclusion must trace to supporting and contradictory evidence.
- Unresolved evidence must remain visibly unresolved.
- Figure rights must be cleared or the figure must be excluded.
- Generated CSVs and LaTeX tables must validate.
- The changelog must state what changed and why.

## Principle

The project should behave like an open scientific investigation: transparent, reproducible, corrigible and versioned. A future researcher should be able to inspect the same evidence, follow the same workflow and understand why confidence rose, fell, or stayed unresolved.
