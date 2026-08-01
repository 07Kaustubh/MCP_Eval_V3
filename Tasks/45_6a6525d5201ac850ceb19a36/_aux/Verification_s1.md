# S1 Cross-Source Verification — Task 45 (StarPM V4)

## Sources consulted
- Per-task data :: _aux/Universe_Split/ — Council A grounded every concrete prompt claim: Carlos Mendez (Onsite Property Manager), Brooke Phillips (Apartment Property Supervisor), Jaime Salinas (QC Inspector, p_007); the current make-ready turn recbd087a4abd605b (selProg, fldMoveOut 2026-06-15, fldTargetReady 2026-06-30, fldNotes2 deep-clean + interior-repaint incomplete); the two named scopes; the 2026-07-15 "Make-Ready QC Inspection - Mesa Vista 4C" (the only future 4C event, on Carlos/Wesley/Brooke calendars); unpaid QuickBooks bills (Sunshine Cleaning deep-clean $387 + Permian Make-Ready Crew interior-repaint $1,340, both overdue); Carlos's Slack C004 "4C is market-ready, good to list" chatter. Census: 4 records for Mesa Vista 4C (2 make-ready rows recbd087 selProg / recc8534 selReady prior turn + 2 maintenance tickets reca424 "complete" / rec12969 turn-open); the 2 make-ready rows are disambiguated by move-out date.
- Per-task data :: _aux/Fact_Ledger.json — atom surface; the prompt carries no hard IDs/amounts by design (zero leakage). verify_universe_atoms.py PASS (0 fails, 0 warns).
- Per-task data :: _aux/Hardness_Plan.md — levers L2/L1/L10/L31/L7/L9 preserved in prompt framing; disambiguation contract honored (target pinned by mid-June move-out + end-of-June target, never bare unit name); THIN density acceptance + census correction recorded at S1.
- Eval spec :: Evals_starpm/1_Prompt_Eval.md — 12 prompt sub-dims scored 5/5 by Council B and re-scored 5/5 by AUDIT (strictest interpretation).
- QC spec :: Docs_starpm/7_QC_Spec_Doc1.json — Prompt-dimension sub-dims 5/5 under strictest AUDIT reading; the four binary prompt sub-dims (Explicit Tool Mention, Tool Use & Cross-service, Investigation+Action, Coherence/Bolt-on) all PASS.

## Reference docs consulted
- Reference/Prompt_Format.md :: hard rules re-checked — 500-word cap (271), no em/en-dash (0), no tool-function names, no MCP-server names, no internal IDs, no pre-solving, first-person, one coherent situation (sentence-removal test), Trigger->Context->Asks, 3+ writes across 3+ services.
- Docs_starpm/9_Common_Error.md :: Part 1 prompt-writing errors — all 7 avoided.
- Docs_starpm/4_Prompt_Hard_Tips.md :: Opus failure modes engineered (skip-structured-DB = L2, latch-first-framing = L1, investigation-and-action).

## Verification statements
- [x] Validator (validate.py --phase prompt) exit 0 — 0 fails, 0 warns, 4 notes; 271 words; no em/en-dash.
- [x] Council A GO — zero ungrounded claims, zero convention drift (delta GO after the "my calendar" -> "on the calendar" fix).
- [x] Council B GO — every applicable Prompt sub-dim scored 5; competent-trajectory density Opus ~43 / Gemini ~41 per model; all Hardness levers triggered; UGT single end-state (HOLD). Delta GO.
- [x] Similarity gate composite 30.8 < 40 (top match Task 44, StarPM), Similarity_Report.json present.
- [x] Regression anchors 62/62 PASS; verify_universe_atoms.py PASS.
- [x] AUDIT verdict PASS (STRICT) — REVISE findings F2 + F-DENSITY resolved; all 12 prompt sub-dims 5/5; every lever traces to a prompt sentence; density THIN accepted with documented per-task justification + mandatory S4 gate.

## Discrepancies surfaced
- Council A BLOCK (round 1): prompt claimed the 7/15 re-inspection was "on my [Jaime's] calendar"; the universe event is on Carlos/Wesley/Brooke calendars, not Jaime's. FIXED -> "a re-inspection on the calendar" (delta GO). Downstream note: OE discovery must cross-calendar search (the event is not on the actor's default calendar).
- AUDIT REVISE (round 1): F2 (make-ready fldTurnStatus enum {Scheduled, In Progress, Ready} has no HOLD value, so "Set the QC status on the turn" risked a no-op on the hold path) + F-DENSITY (per-model density THIN under the strictest minimizing read ~21, and the L33 empirical 33-38, below the 40 design target). RESOLVED -> F2 reword "record your QC determination on that turn"; F1/F4 keyword softening "still tracking" -> "still open"; THIN accepted with per-task justification + 5-6-write mandate + hard S4 REDO gate (Hardness_Plan). AUDIT re-review -> PASS (STRICT).
- Carry-forwards to S2/S3/S4 (documented in _aux/Hardness_Plan.md): (1) preserve 5-6 DISTINCT writes, do not collapse to 3; (2) hard S4 gate — per-model average < 40 tool calls -> PIPELINE REDO (rule 11); (3) S3 QC-status rubric binds to recbd087, checks "did NOT advance to Ready" + "recorded the QC hold determination", never a nonexistent hold enum, not satisfiable by either "done" maintenance ticket or the prior selReady turn recc8534; (4) census = 4 records (2 make-ready + 2 tickets), not 3; (5) cross-calendar discovery for the 7/15 event; (6) repaint vendor = Permian Make-Ready Crew (not the calendar event's Pete Donovan); (7) Brooke-notify rubric accepts any channel (prompt names a goal, not a method); (8) bill TxnDate 2026-05-01 predates the 6/15 move-out — universe-internal noise; ground "not closed" on selProg + unpaid balances, not calendar dates.
- Pipeline wiring notes (non-blocking, flagged to operator): (a) the HARDNESS/S1/S2/S3 runbook verification-doc templates use the stale `Data sources consulted` section name while check_verification.py requires `Sources consulted` + `Verdict` sections — this doc uses the correct shape (matching the passing Verification_s0.md); (b) validate.py's relative-date NOTE prints the Brookfield default today 2026-06-12 for StarPM because Fact_Ledger.lifecycle.today is null (property-management universe has no fiscal periods) — cosmetic, gates nothing; the prompt's relative dates resolve correctly against the true StarPM today 2026-07-01.

## Verdict
- PASS — 5_Prompt.txt clears every S1 exit criterion: validator PASS, Council A GO, Council B GO (all sub-dims 5), similarity 30.8 < 40, AUDIT PASS (STRICT). Density accepted as THIN with documented per-task justification + mandatory S4 REDO gate. Ready for the platform linter (S1.5 if flagged) or S2.
