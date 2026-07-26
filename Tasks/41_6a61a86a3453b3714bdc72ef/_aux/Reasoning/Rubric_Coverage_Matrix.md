# Rubric Coverage Matrix — Tasks/41_6a61a86a3453b3714bdc72ef

**AUDIT verdict:** `PASS (STRICT)` (`_aux/Council_Reports/AUDIT_rubrics.md`) · Council A GO · Council B GO · Validator PASS (0 fails) · Regression anchors 62/62.
**Rubric set:** 18 rubrics, all Outcome (0 Process). Sub-types: 2.1 ×5 (R1-R5), 1.1 ×4 (R6, R9, R12, R14), 1.2 ×9 (R7, R8, R10, R11, R13, R15, R16, R17, R18).

## Forward map — every prompt ask → OE step(s) → rubric(s)

| Prompt ask (sentence) | OE step(s) | Rubric(s) |
|---|---|---|
| "what Tanya genuinely owes us right now" (clean number, not double-counting a credit) | OE2-5 | R1 (net ≈$1,832) |
| "walk it back to the underlying charges so I know it is the clean number" | OE5 | R2 ($1,982 charges: 847 + 925 + 210) |
| back rent "mostly squared away" assumption / paid-invoice decoy is not "current" | OE3, OE5, OE18 | R1 (FAIL clause rejects $0 / $2,132 / catch-all) |
| "whether we have truly filed the petition yet or are still short of that" | OE8-13, OE18 | R3 (petition NOT filed, JP coordination) |
| "confirm we have the owner's authorization on file the way we should" | OE10-11, OE18 | R4 (owner auth on file, Linda Castillo, EVF-2026-014) |
| "whether we are clear to release her unit back for make-ready, or whether it has to hold" | OE7-8, OE18 | R5 (unit held; not release / not market) |
| "get our make-ready record for the unit updated to the real current state" | OE14 | R6 (updates Sunset Ridge Unit 14 record; not Rio Bend) + R7 (status not advanced) + R8 (note records possession-hold) |
| "Leave a short note on the eviction ticket so the trail is current" | OE15 | R9 (adds note to OPS-32) + R10 (petition not filed) + R11 (owner-approved) |
| "Drop the make-ready team a heads-up in our channel on where things landed" | OE16 | R12 (posts to #make-ready) + R13 (crew not mobilize / not market, possession not returned) |
| "draft me an email to the owner covering the balance, the eviction status, and whether we can touch the unit yet" | OE17 | R14 (drafts to linda.castillo@gmail.com) + R15 (balance ≈$1,832) + R16 (petition not filed) + R17 (owner-approved) + R18 (unit cannot be released/marketed) |
| "If anything I've assumed here turns out to be off, tell me plainly" | OE18 | covered by the factual corrections R1 / R3 / R5 (no separate rubric to avoid overlap) |

## Reverse map — every rubric ties back to a prompt ask (no surplus)

Every rubric R1-R18 appears in the forward map above with an explicit prompt sentence and OE. No rubric goes beyond the prompt; the split owner-approved/petition-not-filed pairs on the note (R10/R11) and email (R16/R17) are grounded in OE15/OE17, which both enumerate owner-approved AND petition-not-filed as distinct content.

## Decoy / exclusion coverage (HARD GATE)

| Decoy | Rubric(s) that penalize incorrect inclusion |
|---|---|
| Paid invoice 7214, Balance $0 ("current") | R1 FAIL clause; R15 FAIL clause |
| Stored bill Balance $2,132 (credit added, not subtracted) | R1 FAIL clause; R15 FAIL clause; R2 (credit subtracted) |
| $185 internal filing-prep bill 2026-EV-047 / ~$13,208.75 catch-all customer | R1 FAIL clause |
| Rio Bend Unit 14 (rec94e86a3007dd5e, selReady) | R5 FAIL clause; R6 FAIL clause |
| Owner mis-attribution (Harry Harris / John Castillo) | R4 FAIL clause; R14 FAIL clause |
| "Hearing set / at court / ruling" overstatement (Linear OPS-32) | R3 FAIL clause; R10 FAIL clause; R16 FAIL clause |

## Hardness-lever end-to-end trace (Council B-B4 / AUDIT Lens 3)

| Lever | Prompt sentence | OE | Rubric | Fact_Ledger / universe atom |
|---|---|---|---|---|
| L2 structured-DB skip (AP bill) | "what Tanya genuinely owes" | OE4-5 | R1, R2, R15 | bill QR-2026-0441 id 232176553533 (VendorRef, no CustomerRef) |
| L10 reversal / supersession | "where the eviction really stands today" | OE8-13 | R3, R7, R10, R16 | Airtable SoR recc83c05d889b354; EVF-2026-014 |
| L1 latching (Harris / hearing) | "last I tracked it we were about at the hearing stage" | OE12-13 | R3, R4, R11, R17 | Linear OPS-32; EVF-2026-014 Linda Castillo |
| L11 net-vs-gross / sign | "not double-counting any credit" | OE5 | R1, R2 | bill lines 847/925/210 vs 150 credit; stored 2132 |
| L31 negative-directive (Gemini) | "I don't want the crew mobilizing ... or us marketing something we can't deliver" | OE14/16/17 | R5, R8, R13, R18 | possession-not-returned note (recc83c05d889b354 fldNotes2) |

## Density (StarPM v4 per-model)
Projected midpoint Opus ~50 / Gemini ~43 — both clear the StarPM v4 PASS band (>=40). 8 distinct services, 7 at >=5%. Rubric set aligns with a 4-write, 8-service, >=40-call trajectory.
