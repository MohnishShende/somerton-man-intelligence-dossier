# Verification Workflow

## Claim Lifecycle

1. Extract claim.
2. Assign claim ID.
3. Classify claim type.
4. Identify source needed for verification.
5. Check primary source where possible.
6. Record status and confidence.
7. Preserve conflicts.
8. Promote only supported claims into the manuscript.

## Status Values

- `unverified`: extracted but not checked.
- `source-located`: a likely source has been identified.
- `verified`: reliable evidence supports the claim.
- `partly-verified`: evidence supports only part of the claim.
- `disputed`: reliable sources conflict with the claim.
- `unsupported`: no adequate support found after reasonable search.
- `superseded`: replaced by a better-framed claim.
- `out-of-scope`: retained in the archive but not relevant to the dossier.

## Confidence Values

- High: multiple strong sources or one authoritative primary source.
- Medium: credible source support with limitations.
- Low: plausible but weakly supported.
- Unknown: not yet assessed.

## Evidence Priority

Official and contemporary records take precedence over later recollections. Conflicts should be documented rather than harmonized away.

## Publication Rule

No factual claim enters the manuscript as established fact unless its verification status is `verified` or its limitations are explicitly stated.

