# S1 Prompt Design — Task 43_6a62ccaf5853030245ac9d53

**Persona:** Carlos Mendez (Onsite Property Manager, p_009) · **Business Function:** Property Operations (StarPM BF1)
**Spine:** Mesa Vista 4C make-ready owner cost pass-through reconciliation (owner Linda Castillo).

## Levers engineered into the prompt
- **L2 — Structured-DB skip (SYMMETRIC flagship).** Framing: "every dollar on her bill has to line up with what we actually paid out on that unit... Go back to what each vendor charged us for the 4C work and set it against the line items I sent her." Forces the agent into the QuickBooks AP bills rather than trusting the visible AR draft + Carlos's "complete" email. Empirically robust even though the source is named (sibling StarPM task named QuickBooks and still stumped 0/12).
- **L10 — Reversal / supersession.** Framing: the summary Carlos sent "is the record she keeps"; instruction to "correct the invoice she is holding" (not create a new one) establishes the stale AR draft as the thing the AP-bill truth supersedes.
- **L6 — Near-miss entity (OPUS-asymmetric).** Surfaced by per-line reconciliation over the 10-bill $1,340 cluster (only one bill is the 4C repaint), the $1,140-vs-$1,340 and $95-vs-$85 near-misses, twin $85 charges, and the Linda-vs-Pete owner decoy (prompt firmly anchors Linda, never mentions Pete).
- **L11 — Net-vs-gross + universe-grounded gotcha (GEMINI-leaning).** Framing: "Only outside vendor work belongs on her side. Anything that was our own time on the unit, an internal walk or a condition check we handled in house, stays off her bill entirely." Preserves the $1,897 (include internal Alamo $85) and $1,727 (drop closet $85) decoys as traps while locking UGT to $1,812.

## Expected stump targets
- **[HIGH — BOTH models]** Report $1,622 (trust AR + belief email) instead of derived $1,812 — flagship L2 + L10. Prior StarPM structured-skip stumps hit 0/12 twice.
- **[MED-HIGH — OPUS]** Grab the wrong $1,340 bill from the 10-bill cluster, or anchor on AR's first-seen $1,140, or bill Pete Donovan — L6 near-miss + first-framing.
- **[MED — GEMINI-leaning]** Mis-scope billable lines → $1,727 (drop closet) or $1,897 (include internal inspection) — L11 (may be masked by L2).
- **[LOW-MED — BOTH]** Duplicate write: create a new invoice instead of correcting 2026-534 (prompt explicitly guards: "I do not want a second bill created next to the one she already has").

## Council verdicts
- **Validator (--phase prompt):** PASS — 0 fails, 1 WARN (bolt-on heuristic false positive), 4 notes; 364 words, 0 dashes, 3 services detected.
- **Council A (Grounding):** GO — zero ungrounded claims; all entities verified against Universe_Split (parsed row_data); business function match true; end-to-end solvability confirmed.
- **Council B (Adversarial QC):** GO — all 12 Prompt sub-dims 5/5 (no NON-FAIL bands invoked); B2 every adversarial path is a trapped model error, not a valid reading; B4 levers 4/4 preserved; B6 no upstream propagation.
- **Density (StarPM per-model):** Opus midpoint ~43 = PASS (≥40); Gemini midpoint ~34 = THIN (15-39), pre-accepted per Hardness_Plan "## THIN density acceptance". Neither model INSUFFICIENT. 4 real writes across 5 services.

## Similarity
- Max composite **27.4** (< 40 PASS, < 35). Top match: `QC_Tasks/V3_Tasks/Task14` (27.4, different Brookfield universe). Sibling **Task 42** (Carlos owner-pass-through, Ridgeview/Finley) raw-lex 30.4 but composite only **11.0** after contextual weighting — deliberate divergence: Task 43 corrects an EXISTING already-sent owner invoice (backward-looking) + updates Airtable make-ready, vs Task 42 sets up a NEW vendor payment before money leaves (forward-looking) + Linear/calendar. Avoided the shared Carlos verbal tics ("close the loop", "tie out", "Go into the books", "bring it back to me first", "rather catch it now", "set a reminder on my calendar").

## AUDIT verdict
- **PASS (STRICT).** Lens 1: 14/14 sub-dims 5/5 with per-atom evidence table (no empty cells). Lens 2: zero answer-leakage (prompt contains no dollar figures; only digit is "4C"). Lens 3: 4/4 levers surfaced with cited prompt sentences (OE/rubric legs PENDING for S2/S3). Lens 4: Opus ~43 PASS / Gemini ~34 THIN. Lens 8: 62/62 regression anchors. New finding: Airtable tblMakeReady lacks a cost field / "Closed" status (feasibility still 5 via fldNotes2). Four carry-forward watch-items logged for S2/S3.

## Final S1 verdict
**SHIP.** 5_Prompt.txt clears every gate (validator PASS, both councils GO, similarity 27.4, AUDIT PASS (STRICT)). Word count 364 (≤ 500), no em-dashes, no tool names, no internal IDs, no pre-solving, correct total $1,812 absent. Ready for platform linter / S2 (Oracle Events).
