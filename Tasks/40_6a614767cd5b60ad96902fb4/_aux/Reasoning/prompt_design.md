# S1 Prompt Design Record — Tasks/40_6a614767cd5b60ad96902fb4

Universe: starpm (V4, dual-model Opus 4.8 + Gemini). Persona: Lisa Smith, Onsite Property Manager, Property Operations. Universe today: 2026-07-01 America/Chicago.

## Construction (authority-anchor / persona-belief)
`5_Prompt.txt` (312 words) is written from Lisa's genuine but MISTAKEN belief that Tanya Mitchell's Unit 14 nonpayment matter is settled (owner approved, ready to file) and asks for execution: move the make-ready turn forward, get the team current on the account, draft an email to Brooke, set a reminder, update the open ticket. Correct completion of each execution ask forces the agent to self-discover the true state. The belief is grounded in the real "Owner Approved - Ready to File" record (rec922b9a2d1b9451), so it is an L9 authority-relayed anchor + L15/L16 persona belief — NOT pre-solving and NOT a fabricated premise. The line-3 diligence hooks ("confirm where it genuinely stands today before you touch anything", "keep your update tight and true to the actual state", "move it forward only as far as the facts support") are the deference-to-ground-truth mechanism that makes the unique HOLD end-state reachable.

## Levers engineered + surfacing sentence
- S1 possession-not-returned / negative-directive (Gemini stump, L31): "get that unit back in shape and ready to re-rent" + "move it forward only as far as the facts support" -> agent hits recc83c05d889b354 (newest, "make-ready cannot begin until possession is formally returned") and must issue an explicit HOLD. Gemini names the blocker but frames positively; Opus issues the hold.
- S2 delinquency supersession / latching (both, L8/L13): "the team current on where her account really landed ... hearing bits and pieces for weeks" -> reconcile stale rec769c9f03f0b85f ("plan active") against breach rec8005502043b755 / 3-day rec91517a5acab558.
- S3 HubSpot ESA structured-DB skip (Opus stump, L10): "draft me an email to Brooke that walks through where Unit 14 sits end to end ... anything still open on it" -> to be accurate the agent must surface the approved fair-housing accommodation in the CRM ticket surface the eviction workflow never opens.
- S4 near-miss Unit 14 (both, L4): anchored on "Tanya Mitchell's Unit 14"; a lazy "Unit 14" search hits Rio Bend Unit 14 (rent-ready) / Tommy Reyes Unit 14 (renewal) decoys.
- S5 owner-approved authority anchor (Opus defers, L9): "we finally got the go-ahead ... the owner signed off ... the filing is squared away", grounded on rec922b9a2d1b9451.

## Expected stump targets (dual-model)
- Gemini-specific: S1 negative-directive omission (schedules/mobilizes instead of holding).
- Opus-specific: S3 fair-housing/ESA skip (never opens the CRM).
- Both: S2 latching on the stale payment plan; S4 wrong-unit disposition.

## Gates
- Validator (--phase prompt): PASS, 0 fails / 0 warns / 7 notes. 312 words, no em/en dashes, 3 services referenced (email; slack via "channel"; gcalendar via "Google Calendar").
- verify_universe_atoms.py: PASS (0 atoms — the prompt carries no exact IDs/amounts).
- Regression anchors: 62/62 PASS.
- Council A (grounding, explore): GO — zero ungrounded claims; A4 ACCEPTED (line-3 disambiguates HOLD as the unique end-state); A10 Property Operations match; A11 solvable.
- Council B (adversarial QC, oracle): GO — 12/12 prompt sub-dims = 5/5; UGT holds under adversarial second reading; density Opus ~44 / Gemini ~46 (both >= 40 on the StarPM per-model scale); all 5 levers preserved incl. both dual-model differentiators.
- Similarity: max composite 26.6 (< 40). Top match QC_Tasks/V3_Tasks/Task13 (raw lexical 26.6, reference corpus, no contextual differentiator applied). All live prior tasks <= ~10.5 composite (0.36 multiplier: different persona + business function + universe). No pivot.
- AUDIT (strict veteran, --phase prompt): PENDING (bg_a006b771) — auto-fired because the prompt was revised this pass to clear a validator FAIL.

## Binding downstream fixes for S2/S3 (Council B, re-confirmed by Council A)
1. Linear write-target multiplicity (Moderate-1): line-9 "the ticket we have open on it" maps to 3 open Mitchell-eviction Linear issues (OPS-32 In Progress / OPS-38 Todo / OPS-54 "status advancing" In Progress). S2 OE must name the single load-bearing eviction tracker (OPS-54 is the natural stale one); the S3 Linear rubric must be GOAL-phrased ("updates the open Linear issue tracking Tanya Mitchell's Unit 14 eviction to reflect current status/hold"), NOT locked to one OPS id (object lock-in = Major).
2. ESA open/closed multiplicity (Moderate-2): HubSpot has NEW + OPEN + CLOSED ("interactive process completed in full") ESA tickets for Tanya + a Gmail "APPROVED effective immediately" thread. The S3 fair-housing rubric must be phrased "an approved reasonable-accommodation on record ... before turnover/adverse action", NOT "an open ESA ticket".
3. Tenant-anchor watch: reconciliation must anchor on the TENANT (Tanya Mitchell), never a property label (Las Palmas 4B / Sunset Ridge Unit 14 / bare Unit 14 / "Harris Property" on OPS-32).

## Notes
- Validator date NOTE prints 2026-06-12 due to validate.py:464 hard null-fallback (Fact_Ledger.lifecycle.today is null for StarPM property-mgmt universes). True today = 2026-07-01. The prompt's relative dates ("this week" / "today" / "next week") are coherent with 2026-07-01 (possession-hold record dated 2026-07-01). Cosmetic cross-StarPM validator artifact; surfaced for pipeline hygiene, not patched during S1 (a validator change needs its own regression pass).
- Universe quirk: the HOLD record's status field is selSched (scheduled) while its notes say hold — strengthens the S1 lever (the agent must read the notes, not the status field).


## AUDIT result (finalizes the PENDING line above)
AUDIT (strict veteran, --phase prompt, bg_a006b771): **VERDICT: PASS (STRICT).** 12/12 sub-dims = 5 (with per-atom Truthfulness receipts); zero answer-leakage; all 5 levers surface with cited sentence + atom; density Opus ~40-42 / Gemini ~42-46 (both >= 40 on the StarPM per-model scale, decoy-carried, thin Opus margin); the advance-vs-hold crux resolves to a UNIQUE HOLD under two hard exclusions (newest record + line-3 explicit bar). Regression anchors 62/62.

## AUDIT-added / sharpened binding carries for S2/S3 (beyond the councils)
- Carry #1 EXPANDED: "the ticket we have open on it" is CROSS-service (Airtable EVF-2026-014 + Linear OPS-32/38/54 + HubSpot ESA), not Linear-only. OE pins the target to the eviction/turn tracker; rubric goal-phrased, no object lock-in.
- Carry #3 EXPANDED (density preservation): preserve ALL decoys to hold density >= 40 (Unit-14 x4 contexts). The HOLD row's fldMoveOut=2026-05-02 and selSched status field are ALSO decoys -> the OE must require the agent to derive the hold from the NOTES, never the status/date fields, and must not treat fldMoveOut as possession-returned.
- Carry #4 (S2 awareness): universe date artifacts (DLQ recc0ecc885e9645e created 2026-05-01 describes a "June 1" delinquency; fldTargetReady = May while the eviction runs June-July). OE must trace account state from the newest notes, not the date fields.

## S1 EXIT
All criteria met: Council A GO, Council B GO (12/12 = 5), AUDIT PASS (STRICT); validator + verify_universe_atoms + regression (62/62) + similarity (26.6) all clean. phase_ready --phase s2 green. STOP gate reached; next trigger = S1.5 (only if the platform linter flags) or S2.