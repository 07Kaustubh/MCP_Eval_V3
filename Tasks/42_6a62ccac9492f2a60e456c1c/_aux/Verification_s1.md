# Cross-Source Verification — S1 (prompt)

## Data sources consulted
- _aux/Universe_Split/ :: grounded persona (Brooke Phillips p_000), owner Robert Finley (contact + QB customer proj-e59d4a436ed7), Pete Donovan (Exterior Painter contact / QB customer proj-f6f9edfeae5c, NOT a vendor), Ridgeview roof record (airtable rec8b679d92f30753), Owner Reserve (Trust) account 64, two Big Bend Restoration bills (528539050604 / 301715729067, vendor 203), owner AR pass-through invoice 109367557444, #owner-relations channel C006, Linear owner-report issue OPS-100, Slack "approved/good to go" posts (2026-05-28), Gmail owner approval 4bcbe384bedfd26f.
- _aux/Fact_Ledger.json :: prompt intentionally carries NO grounded atoms (no IDs, no dollar amounts) by answer-leak design; verify_universe_atoms.py PASS (0 atoms to ground).
- _aux/Hardness_Plan.md :: all 5 selected levers (L2 structured-DB skip flagship, L10 duplicate, L31 negative-directive/HOLD, L1 latching, L6 near-miss) preserved in the prompt framing; 4-write mandate + reminder engineered to hold Gemini density >= 40.

## Eval spec sub-dims (Evals_starpm/1_Prompt_Eval.md) verified
- 1.1 Unique Ground Truth :: PASS — queue-vs-hold resolves to a single "prepare-but-hold" end-state co-determined by the universe (unresolved duplicate + unconfirmed reserve).
- 1.2 Feasibility :: PASS — no conflicting/impossible ask; "get payment in order... ready the moment we are clear" is compatible with the hold.
- 1.3 Explicit Tool Mention :: PASS — no tool/function/MCP names; systems referenced naturally ("the books", "owner relations channel", "our tracker", "my calendar", "email Finley").
- 1.4 Prompt Clarity and Specificity :: PASS — one leading interpretation; no MAJOR second reading that flips the write-action set (Council A A7 + Council B B2 confirmed).
- 1.5 Contrived / Unnatural :: PASS — mid-thought first-person portfolio-supervisor voice; one coherent situation; no artificial precision.
- 1.6 Truthfulness :: PASS — every claim grounded; "Finley gave his approval" genuinely granted (Gmail 4bcbe384...); "Pete Donovan's crew is confirmed" is the persona's chatter-grounded belief (the intended latch), not a fabrication.
- 1.7 Tool use and Cross-service requirement :: PASS — true trajectory spans 7 services (QB, Gmail, Slack, Linear, GCalendar, Airtable, Contacts); validator literal-mention count of 2 clears the >=2 gate.
- 1.8 Investigation :: PASS — "figure out what the payable actually is", "if anything does not line up", "bring it back to me with what you found" force discovery before action.
- 1.9 Coherence :: PASS — every sentence advances the single Ridgeview roof CapEx close-out; no bolt-on (validator 0 warns after entity anchoring).
- 1.10 Persona :: PASS — matches Brooke's PersonaBrief (direct, organized, coaching; owns vendor-invoice approval + owner CapEx flow); signature scenario owner_capex_approval_roof.
- 1.11 Business Function :: PASS — squarely BF#2 Portfolio Coordination & Owner Relations.
- 1.12 Alignment with Today's Date :: PASS — "sitting since late May" (approval 2026-05-28, past), "into July"/"new quarter" (today 2026-07-01 = Q3 start) all coherent with the date SSOT.

## QC spec sub-dims (Docs_starpm/7_QC_Spec_Doc1.json — Prompt dimension) verified
- All 12 Prompt sub-dims scored 5/5 per the scheme map in Reference/Council_Protocol.md (Council B-B1 + AUDIT Lens 1). Universe Data-Exists + Cross-service Coherence also 5/5.

## Reference docs consulted
- Reference/Prompt_Format.md :: voice, anti-patterns, 500-word cap (prompt is 319), no-em-dash, no-tool-name rules re-checked and clean.
- Docs_starpm/4_Prompt_Hard_Tips.md :: structured-DB-skip + latch-first-framing exploited; go-broad / hint-without-giving-away applied; write diversification for density.
- Docs_starpm/6_Prompt_Relative_Time_Updates.md :: today = 2026-07-01 confirmed as date SSOT.

## Verification statements
- [x] Validator (validate.py --phase prompt) exit 0 — PASS, 0 fails, 0 warns, 4 notes.
- [x] Council A grounding + convention clean (zero ungrounded claims, zero convention drift, zero narrative-state contradictions).
- [x] Council B QC scoring shows every applicable sub-dim = 5 (no NON-FAIL band invoked).
- [x] Council B-B3 density Opus ~48 / Gemini ~40 (both >= 40 StarPM per-model PASS); B-B4 all 5 levers triggered.
- [x] Similarity gate (calc_similarity.py) composite 27.1 < 40.
- [x] AUDIT verdict = PASS (STRICT).
- [x] verify_universe_atoms.py PASS; test_regression_anchors.py 62/62 PASS.

## Discrepancies surfaced (if any)
- None blocking. Watch-item: Gemini density sits exactly at the 40 floor — confirm on the first S4 platform run. Two non-blocking S3 anchoring notes (OPS-100 vs OPS-10; duplicate-catch rubric should not hard-pin which doc survives).
