# S1 Prompt Design — Task 45 (StarPM V4)

## Deliverable
5_Prompt.txt (271 words). Jaime Salinas (QC Inspector) runs a QC pass on the Mesa Vista 4C make-ready turn from its mid-June move-out and records a sign-off OR kick-back decision. Correct answer: HOLD/kick-back.

## Levers engineered into the prompt
- L2 structured-DB skip (SYMMETRIC, primary) — "before anyone lists it I need the real state of that turn" + "whether both are genuinely closed and signed off or still open" forces querying the make-ready record; every easier signal (Carlos's chatter, the two maintenance tickets, the prior selReady turn) says done.
- L1 latching (OPUS-SEL) — "Carlos has Mesa Vista 4C down as wrapped ... Brooke is ready to put it on the market on his word."
- L10 supersession (OPUS-SEL, partial) — the "done" tickets + prior selReady turn bait the trust-the-latest heuristic; rule-13 disambiguation (mid-June move-out / end-of-June target) correctly subordinates L10 to F7 single-target uniqueness.
- L31 explicit negative directive (GEMINI-SEL) — "if it is not, say so plainly and hold it ... does not go to listing until every outstanding scope is closed and signed off ... Brooke needs to hear it from us before she markets it." Grounded (explicitly asked-for), avoiding the Task-39 "phrase never asked" defect; strengthened by the F2 reword (guaranteed make-ready hold-write target).
- L7 multi-write (density) — 4-5 writes: make-ready QC determination / Linear ticket / Slack C004 post / Gmail draft to Carlos / Brooke notification.
- L9 future-event (density + breadth) — "a re-inspection on the calendar for the middle of this month, and it factors into whether I can call this one done." F9-clean (no "only open item" over-claim).

## Expected stump targets
- SYMMETRIC (both models): latch on Carlos's "wrapped" report + the "complete" maintenance ticket + the prior selReady turn -> sign off. Missed: current selProg turn recbd087, deep-clean + interior-repaint still open, 6/30 target past-due, two bills unpaid, 7/15 re-inspection pending -> HOLD.
- OPUS-SEL: pick the wrong make-ready row (prior selReady, created later) or treat the maintenance ticket as authoritative.
- GEMINI-SEL: describe 4C's state but omit the explicit do-not-market hold directive.

## Council + AUDIT verdicts
- Council A (grounding): GO (delta GO after the "my calendar" -> "on the calendar" grounding fix). Zero ungrounded claims; single-target uniqueness holds.
- Council B (adversarial QC): GO — all 12 prompt sub-dims 5; competent-trajectory density Opus ~43 / Gemini ~41; all levers fire; UGT single end-state HOLD.
- AUDIT (strict veteran, StarPM density bar 40+): REVISE round 1 (F2 fldTurnStatus-no-HOLD-enum + F-DENSITY THIN) -> fixes applied -> PASS (STRICT). All 12 sub-dims 5/5, zero blocker, every lever traces to a prompt sentence.

## Similarity gate (step 7 log)
- Max composite 30.8 < 40 -> PASS, no pivot. Top match: Tasks/44_6a62ccba8cad60844b8364b9/5_Prompt.txt (composite 30.8, raw_lex 30.8, same StarPM universe / multiplier 1.0). Sub-40 after contextual weighting -> genuinely distinct given the StarPM QC make-ready scenario + Jaime QC-inspector persona + BF3 (QC & Field Services).

## Density disposition
THIN per-model, accepted with documented per-task justification (Hardness_Plan "## THIN density acceptance"): clears the StarPM 15 QC-spec floor with wide margin; competent midpoint 41-43 meets the 40 design target; the minimizing floor (~21) and the L33 empirical (33-38) are THIN, and no prompt-side lever reaches 40 without bolt-on. Prompt-side floor-raisers applied at S1: F2 reword (guarantees the make-ready write) + F1/F4 keyword softening ("still open"). Mandatory downstream mitigations: S2/S3 preserve 5-6 distinct writes; hard S4 REDO gate on any sub-40 per-model average.

## Carry-forwards to S2/S3/S4
Recorded in _aux/Hardness_Plan.md ("## THIN density acceptance" + "## Record census correction") and _aux/Verification_s1.md (8-item "Discrepancies surfaced" list): preserve 5-6 writes; S4 REDO gate; S3 QC-status rubric binds to recbd087 (checks "not advanced to Ready" + "hold determination recorded", never a nonexistent enum, not satisfiable by either ticket or the prior turn); census = 4 records; cross-calendar discovery for the 7/15 event; repaint vendor = Permian (not Pete Donovan); Brooke-notify accepts any channel; bill-chronology noise (ground "not closed" on selProg + unpaid balances).
