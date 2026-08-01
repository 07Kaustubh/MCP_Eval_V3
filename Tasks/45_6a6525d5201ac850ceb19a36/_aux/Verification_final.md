# Verification — PIPELINE FINAL (Task 45, StarPM V4, Mesa Vista 4C QC Hold)

Universe: **starpm** (V4) · today 2026-07-01 America/Chicago · window 2026-05-01..2026-07-01.
Density scheme: StarPM per-model (design 40+, floor 15). NOT the V3-family 50/40 scheme.

## Data sources consulted
- All 3 artifacts (5_Prompt, 6_Oracle_Events, 7_Rubrics — 19 outcome / 0 process) read together.
- _aux/Universe_Split/ :: gcalendar/airtable/quickbooks/slack greped directly to ground every tight identifier (council Lens 1).
- _aux/Fact_Ledger.json :: amounts 387.00 / 1340.00, dates 2026-06-15 / 06-30 / 07-01 / 07-15, recIDs, OPS issue keys, @starpm.com emails all present.
- _aux/Hardness_Plan.md :: 5 engaged levers (L2 symmetric + L1/L10 Opus-sel + L31 Gemini-sel + L7 + L9) traced end-to-end; THIN-density acceptance carried forward.
- _aux/Validator_Reports/ :: submission_gate + injection + prompt/oe/rubrics.
- Tasks/_meta/Learnings.md :: banked StarPM dual-model 0/6 recipe (item 11), L31 negative-directive Gemini stump (L31), L15/L16 implicit-belief framing, item 12 exact-ID accept-set warning, L33 grading-noise margin.
- Docs_starpm/7_QC_Spec_Doc1.json + 8_QC_Spec_Doc2.md :: QC sub-dim scoring (via council).
- Evals_starpm/0_Injection_Quality_Eval.md + 5_Submission_Gate_Eval.md (F2 line ~146) :: enforced by the two V4 deterministic gates; F2 definition read directly.
- Reference/Sessions/FINAL.md + Reference/Council_Protocol.md (B3 density SSOT).

## All eval specs verified (StarPM 6-eval set)
- Evals_starpm/1_Prompt_Eval.md :: prompt phase re-applied at integration (implicit framing, no leakage, date alignment).
- Evals_starpm/2_OE_Eval.md :: OE phase re-applied (tool-param bindings, lifecycle, unordered-coverage).
- Evals_starpm/3_Rubrics_Eval.md :: rubric phase re-applied (atomicity, exact values, outcome>process, Bucket-risk).
- Evals_starpm/4_Verifier_Fails_Eval.md :: Lens 6 bucket simulation (~5% Bucket-1 risk, all designed fails = Bucket 3).
- Evals_starpm/0_Injection_Quality_Eval.md :: deterministic PASS (0 fails); base-universe task (inject.sql = template header, 4_Changelog.json = []).
- Evals_starpm/5_Submission_Gate_Eval.md :: deterministic PASS after Path B gate fix (see below).

## QC spec coverage (Docs_starpm/7 + 8)
- Prompt sub-dims :: scored via council Lens 1/2/4 (implicit, coherent, date-aligned, no pre-solving/tool-leak — validator prompt PASS).
- Universe sub-dims :: feasibility + cross-service coherence (Lens 1/5; injection PASS).
- OE sub-dims :: solvability + tool-parameter correctness (Lens 5; validator oe PASS).
- Rubric sub-dims :: category balance 19/0 (Outcome>Process binary PASS), atomicity, groundedness, all-failing (deferred to S4).
- Trajectory sub-dims :: T1 density projected per-model (THIN, MAJOR carry-forward, mandatory S4 gate); T2/T3 deferred to S4 (trajectories are empty pre-upload stubs).

## Verification statements
- [x] Validator (validate.py --phase all) exit 0 across all 3 artifacts (prompt 0F / oe 0F / rubrics 0F/8W).
- [x] V4 injection gate PASS (0F; 4 council semantic notes: P4/P5/P6/P8, all satisfied per council).
- [x] V4 submission_gate PASS (0F/4 notes) AFTER Path B gate fix; regression clean.
- [x] 6 FINAL lenses returned PASS (Truthfulness / Rubric Binding / Cross-Artifact Holism / Red-team / Narrative-State+Action-Prescription / Verifier-Fails Pre-Upload). Report: _aux/Council_Reports/FINAL_council.md VERDICT: PASS.
- [x] Zero answer leakage — correct DECISION (hold / not-ready) + discriminators (which row is truth, bills unpaid, 7/15 future) never stated verbatim; "wrapped" framed as Carlos's belief (L15/L16).
- [x] Every Hardness lever triggers end-to-end (L2->R1/R2/R3; L1/L10->R1ev/R2; L31->R2/R15; L7->R1/R4/R9/R11/R14; L9->R8/R19). No lever regressed.
- [x] Dual-model (V4): both Opus and Gemini runs expected downstream (8a/8b + Agent_Responses/{Opus,Gemini}/ — currently empty pre-upload stubs).

## Submission-gate false positive + Path B gate fix (rule 18: finding -> standing gate)
- FAIL was: [Eval5 P2 MISMATCH] rubrics #8 and #19 reference 2026-07-15 (after today) as "future-dated expectation".
- Council (FINAL_council.md) confirmed FALSE POSITIVE: Evals_starpm/5 P2 (~L146) defines the F2 defect as future-AS-PAST ("rubric expects analysis of events not yet happened"); #8/#19 require the agent to STATE the event "has not yet occurred" = future-as-FUTURE = spec-correct. 2026-07-15 is a real status=confirmed gcalendar event (event_id 360b2149b7d0c10fa65224c281cdb53f); it is lever L9's sole carrier, so weakening the rubrics was NOT an option (would regress a lever).
- Path A (add "calendar" to evidence to trip rubric_is_cal_create) REJECTED as gate-gaming (rules 18-20; mislabels the NOTE).
- Path B IMPLEMENTED: made the F2 net negation-aware in Validators/v4_gates.py — added _FUTURE_ACK_RE; when a post-window future date co-occurs with future-acknowledging language ("not yet occurred", "still pending", "not yet done", "yet to occur", "upcoming"), emit a COUNCIL NOTE instead of a FAIL. Aligns the code with its own spec line (Evals_starpm/5 P2 ~L146) and closes the false-positive class for all future tasks.
- Safety: python3 Validators/check_regression.py -> PASS (anchors 62/62, reports 21/21 identical, verdicts 7/7 unchanged). test_regression_anchors.py -> 62/62. 0/21 frozen hashes moved (as council predicted; no snapshot carried the future-date+negation construction). Rubrics 5/6/7 shipped UNCHANGED. v4_gates.py change is additive; not committed (no commit without explicit request).

## Discrepancies surfaced (carry-forward, non-blocking)
- [MAJOR / accepted carry-forward] Per-model density THIN (competent projection Opus ~40-43 / Gemini ~38-41; empirical StarPM anchor 33-38). Accepted at S1 AUDIT with per-task justification; clears the 15 fail-floor. MANDATORY S4 gate: if real-run per-model avg < 40 -> PIPELINE REDO (AGENTS.md rule 11 / Hardness mitigation 2). 6 distinct writes preserved in OE10-15 + rubrics to hold the floor.
- [MINOR] R13 AND-bundles deep-clean + interior-repaint unpaid in one email criterion (7_Rubrics.json). Acceptable: per-bill amounts atomically graded on the issue (R5/R6) + final response (R16/R17); prompt names both scopes jointly. Optional split, LOW risk. Left unchanged (ship 5/6/7 as-is per council).
- [MINOR] OE1 references search_records param as `table` vs `tableId`; write path OE10 correct (tableId). Non-blocking (OE prose, not a rubric binding).
- [MINOR] OE11 literal team "Operations"; R4 binds to the grounded key OPS (230 OPS-* issues), so the rubric is safe regardless of the OE string.

## VERDICT: PASS — cleared for platform upload (dual-model Opus + Gemini, 6 runs each). Hold the mandatory S4 per-model density gate.


---

## POST-COUNCIL UPDATE — R13 atomic split applied (supersedes the line-50 MINOR note + all "19 rubrics" counts above)

Per the operator directive to evaluate the external AI-helper findings and incorporate valid ones, the AI-helper atomicity finding on criterion **b452971c** (the email "deep-clean AND interior-repaint bills unpaid" AND-bundle) was judged VALID: it converges with this council's own [MINOR] R13 flag and AGENTS.md rules 13 (atomic rubrics for multi-item write actions) + 14 (never merge to save a slot).

- **Split applied:** R13 -> two atomic outcome rubrics (deep-clean bill unpaid / interior-repaint bill unpaid), amount-free to match the original email-rubric design (per-bill amounts stay atomically graded on the tracking issue R5/R6 and the final response, now R17/R18).
- **Count is now 20 outcome / 0 process** (was 19). Under the 60 cap. Outcome>Process binary PASS unchanged.
- **Rubric renumbering:** the final-response 7/15 QC-reinspection rubric is now **#20** (was #19); submission_gate NOTEs #8 and #20.
- **Bucket-1 risk:** R13 was the sole ~5% Lens-6 Bucket-1-risk rubric; splitting drops it to ~0%.
- **No lever/entity/density change**; both bills still graded on the email. No FINAL re-council needed (the split was council-endorsed as "optionally split, LOW risk"; Path B was council-designed).
- **Re-verified GREEN:** validate.py --phase rubrics PASS (0 fails, 8 pre-existing benign amount-groundedness warns, unchanged by the split) · submission_gate PASS (0 fails) · check_regression PASS (62/62 · 21/21 · 7/7).

**Shipped deliverable: 7_Rubrics.json = 20 atomic outcome rubrics.** FINAL verdict stands: PASS — cleared for platform upload.