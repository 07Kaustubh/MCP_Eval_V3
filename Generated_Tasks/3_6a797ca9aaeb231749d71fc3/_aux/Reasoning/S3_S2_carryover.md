# S3 <- S2 carryover — ART ticket resolution

**Date:** 2026-08-12
**Operator directive:** treat F1-r3 as over-flagged; proceed with S3.

## Finding origin

S2 AUDIT R3 flagged F1-r3 MODERATE: OE 24's primary predicate has two grammatically-valid readings. Naive reading resolves the ART tracking ticket to ART-760 ("Unlock Sagamap Feature Vfx Implementation", In Review, 2025-01-17). Strict reading fires OE 24's fallback and resolves to ART-770 ("River Rush VFXs and Animations", most recent updated_at).

## Why over-flagged

OE 24's fallback clause is written as: *"If the search returns no live-state (unresolved) ART VFX tracker (all rows Done or stale by more than six months relative to universe today 2026-02-28), still select the most recently updated ART VFX ticket as the reconciliation home."*

Verification_s2.md universe-context finding: **the ART team has zero fresh unresolved VFX tickets as of 2026-02-28. The top-level ART VFX tracker (ART-252) is Canceled.** All ART VFX rows are Done, Canceled, or stale by more than six months. The fallback condition is satisfied unconditionally on this universe.

Therefore both readings of the primary predicate converge on the fallback, and the fallback deterministically selects the most-recently-updated ART VFX ticket = ART-770.

## S3 rubric grounding rule

Every rubric that grounds on the ART tracking ticket resolved in OE 24 grounds on:

- **Linear issue id:** `ART-770`
- **Title:** `River Rush VFXs and Animations`
- **Team:** ART

This includes:
- The OE 25 rubric grading the Linear comment write action.
- The OE 25 rubric grading the reconciliation comment content.
- The OE 29 rubric grading the tracking-link binding in the vendor tracker sheet.

## Compliance with hard rule 13 (single-target uniqueness)

Under the deterministic fallback, exactly one universe record matches the target (ART-770). This satisfies rule 13's "confirm exactly ONE universe record matches the prompt's described target" requirement despite the predicate's textual ambiguity.

## Escalation path if the ruling is wrong

If the platform grader interprets OE 24's naive reading and resolves to ART-760, the rubric grounding will fail all runs on that criterion. In that case the recovery is: re-run S2 with the AUDIT R3 proposed rewrite applied (unify the two readings by making the freshness qualifier explicit on the primary predicate and drop the two-branch structure), then re-run S3 with the ART id re-pinned to whatever the fixed OE 24 deterministically returns.
