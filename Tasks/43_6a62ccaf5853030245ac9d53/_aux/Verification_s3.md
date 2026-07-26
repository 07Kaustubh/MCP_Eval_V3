# Verification — PIPELINE S3 (Rubrics) — Tasks/43_6a62ccaf5853030245ac9d53

v16 cross-source verification. Universe: **starpm** (V4 framework). Deliverable: `7_Rubrics.json`, **25 rubrics, 25 outcome / 0 process**, flat four-field schema.

## Sources consulted

**Per-task data** — `_aux/Universe_Split/`, `_aux/Fact_Ledger.json`, `_aux/Universe_Index/`, `3_UniverseDataForThisTask.json` (via the S0 split), `5_Prompt.txt`, `6_Oracle_Events.txt`, `_aux/Hardness_Plan.md`, `_aux/Verification_s2.md`, `_aux/Verification_audit_oe.md`.
**Eval spec** — `Evals_starpm/3_Rubrics_Eval.md` (read in full, both pages; every hard gate executed — enumerated under "Eval spec sub-dims" below).
**QC spec** — `Docs_starpm/7_QC_Spec_Doc1.json` (Rubric dimension, all 5 sub-dims read verbatim) + `Docs_starpm/8_QC_Spec_Doc2.md` (appendix severity taxonomy).
**Framework + reference** — `Docs_starpm/2_Rubrics_V3_Guidelines.md`, `Docs_starpm/12_Always_Failing_Rubrics.md`, `Reference/Rubric_Format.md`, `Reference/Strict_Convention_Inventory.json`, all four `QC_Tasks/V4_Tasks/QC_Passed/*/7_Rubrics.json`, `StarPM_Base_Universe/7_Server_Tools_Details.json`.

Per-task detail, re-verified from source rather than from any upstream summary:

- `_aux/Universe_Split/` :: ground-truth values each rubric tests, re-read from raw `row_data` JSON strings rather than from any upstream summary. Records re-verified: invoice `445653930748` (DocNumber 2026-534, lines 387.00 / 1140.00 / 95.00, TotalAmt 1622.00, CustomerRef Linda Castillo `proj-4ae920b7c9e8`, sync_token 0); bills `195089456477` (2026-SC-4C, Sunshine Cleaning, 387.00, acct 62), `696089964235` (PD-2026-09, Permian Make-Ready Crew, 1340.00, acct 63), `546359391323` (2026-519, Permian, 85.00, acct 64 Owner Reserve (Trust)), `991582431419` (2026-481-566, Alamo HVAC Services, 85.00, acct 61 Supplies); `tblMakeReady` rows `recc8534b3fd13954` (selReady, last mod 2026-05-29 14:26:59) and `recbd087a4abd605b` (selProg, last mod 2026-05-22 21:14:34); `tblMaintenanceTickets` `reca424761ae15355` + `rec12969a3fdb0852`; contacts Linda Castillo / Pete Donovan / John Castillo / Tony Reyes / Tommy Reyes / Jaime Salinas / Brooke Phillips / Carmen Delgado; QuickBooks customers `proj-4ae920b7c9e8` / `proj-f6f9edfeae5c` / `proj-e576b03e2b4c`; gmail `5101c5a41dffa90a` (base64 body decoded — **no dollar figures at all**); the six 4C Slack messages in C004; the ten-bill $1,340 cluster (exactly 10); decoy invoices 2547 ($385) and 2026-AP-0184 ($1,340), both billed to the same Linda Castillo.
- `_aux/Fact_Ledger.json` :: 403 amounts / 206 emails indexed. Confirmed present: `$1,622`, `$1,340`, `$1,140`, `$387`, `$95`, `$85`, `$200`, `$190`, `$385`. Confirmed **absent**: `$1,812` and `$10`. Both absences are intentional and load-bearing — see "Derived values" below.
- `_aux/Verification_s2.md` + `_aux/Verification_audit_oe.md` :: prior-phase verification reviewed for OE-rubric consistency. No open discrepancy carried into S3.
- `_aux/Hardness_Plan.md` :: lever selection L2 / L10 / L6 / L11 (+ L1 reserve) and the per-model density projection.

## Eval spec sub-dims (`Evals_starpm/3_Rubrics_Eval.md`) verified

- **Overall Rubric Quality** :: PASS (5). Threshold math on 25: Major 0 (0.00%), Major+Moderate 0 (0.00%), all-severity 0-1 (≤4.0%). Pipeline absolute-count gates also clear (set < 30, so Major ≥ 3 / M+M ≥ 5 / any ≥ 8 all inapplicable at 0).
- **Rubric Category Balance** :: PASS (5). 25 outcome / 0 process; `#Outcome > #Process` satisfied, binary dim.
- **Process Rubrics** :: PASS (5). Zero process rubrics, affirmatively justified (below), so the "2+ invalid" FAIL threshold cannot be reached.
- **Agent Centric Phrasing** :: PASS (5). 25/25 titles are `The Agent` + finite verb + context; **zero possessive-form titles**; zero tool names in any criterion.
- **All-Failing Rubrics** :: 5 (rubric stage; verifier-run dependent, re-assess at S4).

## QC spec sub-dims (`Docs_starpm/7_QC_Spec_Doc1.json` — Rubric dimension) verified

All 5 Rubric sub-dims read verbatim and scored under the strictest interpretation (every NON-FAIL middle band collapsed). Appendix issue taxonomy from `Docs_starpm/8_QC_Spec_Doc2.md` re-applied. Hard gates from the eval executed: Blank Fields, Forward Coverage, Atomicity Split-Completely, Act-vs-Defer (T9 — n/a, no rubric derives from a `proposed_resolution`), Impossible Derivation (T10), Imported Constraint (T10), Write-as-Deliverable Preservation (T12), Prompt-vs-Rubric Action Alignment (Gap 6 — all four writes are assigned to the agent by the prompt, none to the user), Deliverable Destination Consistency, Final-Response Coverage (Gap 3), OE-to-Rubric Cross-Reference (Gap 4), Exclusion/Decoy Coverage, Under-Strict per-criterion-in-isolation, Pre-Submission All-Fail Prediction.

## Reference docs consulted

- `Reference/Rubric_Format.md` :: flat schema + handling-flexibility patterns + dilution-prevention absolute-count gates re-checked.
- `Reference/Strict_Convention_Inventory.json` :: allowed phrasings + evidence-field shapes. Treated as advisory rather than binding where Brookfield-derived, per the S3 runbook's note that the StarPM phrasing SSOT is the V4 passed corpus + `Docs_starpm/2_Rubrics_V3_Guidelines.md`.
- `Docs_starpm/2_Rubrics_V3_Guidelines.md`, `Docs_starpm/12_Always_Failing_Rubrics.md`, all four `QC_Tasks/V4_Tasks/QC_Passed/*/7_Rubrics.json`, `StarPM_Base_Universe/7_Server_Tools_Details.json`.

## Derived values — deliberate Fact_Ledger absences

`$1,812` (= 387 + 1,340 + 85) and `$10` (= 95 − 85) appear nowhere in the universe. This is the **L2 flagship lever functioning as designed**, not a grounding failure: the correct owner figure is stated on no readable surface, so it can only be produced by opening the AP bills and adding them. Council A independently confirmed `"1,812"` has **0** occurrences universe-wide and that the 17 bare-`1812` hits are all epoch/history-id fragments. Answer-leakage swept over a 2.46M-character fully-decoded surface (every base64 Gmail body included): `1,812` / `1812.00` / `1,897` / `1,727` / `1,810` all **0 hits**; minimum synthesis depth to reach the answer is **3 sources**.

## Validator warns — three artifact classes, none concealing a defect

33 warns, decomposing exactly: **25** X2 rubric-OE consistency + **6** Fact_Ledger amount + **2** Hardness_Plan atom.

1. **X2 (25)** — `MONEY_RE` at `validate.py:171` is `$`-anchored, and `6_Oracle_Events.txt` contains **zero** `$` characters (V4 OE convention writes amounts unprefixed). The check's OE amount-atom set is therefore empty and it warns on every rubric carrying an amount. **The suppressed check was discharged by hand**: all 25 rubric-title amounts trace to at least one OE step (verified programmatically against four format variants). AUDIT independently re-ran the manual X2 substitute: **0 gaps**.
2. **Fact_Ledger (6)** — the five `$1,812` occurrences plus one `$10`. Intentional per "Derived values" above.
3. **Hardness_Plan (2)** — the two `$190` occurrences. `$190` *is* in the Fact_Ledger (coincidentally, via invoice `618793969708`); it warns only because the Hardness Plan leaves the net implicit, stating the components (`$200` understated, `$10` overstated) without their sum. My initial accounting said two classes; AUDIT corrected it to three.

## Zero Process rubrics — affirmatively justified

The three-condition test was applied to the one candidate ("the Agent verifies the vendor bills before correcting the invoice"). It fails **condition 2**: the derived Outcome values (`$1,340`, `$85`, `$1,812`, `$190`) appear on no readable surface, so the Outcome cannot be satisfied without doing the underlying work and a Process rubric adds no signal. This is the exact inverse of the single passing Process precedent in `QC_Passed/Task3` R11, which survives *because* its balances were mirrorable from BlackLine's own reported fields. Confirmed by Council B (B2d) and AUDIT (LENS 5, zero disguised process rubrics).

## The "approximately" ruling

No `approximately` qualifier appears on any amount. Ruled deliberately rather than by omission, against `Docs_starpm/2_Rubrics_V3_Guidelines.md` Rule 4 and `Docs_starpm/12_Always_Failing_Rubrics.md` Example 3: Rule 4's discrete-quantity carve-out governs because every input is a whole-dollar `TotalAmt`, so there are no cents for an agent to round away and AF Example 3 (whose exemplars all carry cents) is inapplicable. Decisively, `approximately $1,812` would admit the **$1,810** decoy (0.110% away, inside any rounding band) and `approximately $190` would admit **$200** (5.26%) — destroying levers L6 and L11. Format-level tolerance is instead granted explicitly in rubric[0]'s evidence ("with or without trailing cents"). AUDIT ruled this "not an AF risk"; Council B verified the arithmetic.

## Verification statements

- [x] Validator (`validate.py --phase rubrics`) exit 0 — **PASS, 0 fails**, 33 warns (all three classes accounted for above). No Major issue tally above the 10% threshold: 0/25.
- [x] Council A **GO** (iteration 4) — zero ungrounded non-derived values, zero convention drift, zero SCOPE_DRIFT, zero SOLVABILITY_BREAK, zero OPEN_ASK_BUNDLED, 25/25 atomic.
- [x] Council B **GO** (iteration 4) — 0 Major / 0 Moderate / 0 Minor on 25; all five sub-dims 5; B3 density within band per model; B4 all levers preserved; B7 zero CONSISTENCY_GAP; B6 zero blocking PROPAGATE.
- [x] Outcome > Process (25 > 0). Outcome 1.1 for every OE write action (OE 24 → rubric[8]; OE 25 → rubric[14]; OE 26 → rubric[17]; OE 27 → rubric[22]). Outcome 2.1 for every prompt tell-me cue (6 user-facing asks → rubrics[0]-[7]).
- [x] Regression-anchor suite executed: **62/62 PASS**.
- [x] Similarity gate: max composite **27.4**, all < 40.
- [x] AUDIT verdict = **PASS (STRICT)** — see `_aux/Council_Reports/AUDIT_rubrics.md`. Reached after **3 REVISE rounds** (at the runbook cap): r1 five findings (1 Major), r2 three Moderates, r3 one Minor.

## Discrepancies surfaced

### Resolved during the phase

| # | Finding | Gate | Resolution |
|---|---|---|---|
| 1 | rubric[8] evidence required a sync token; catalog marks `SyncToken` **optional** — evidence stricter than criterion | Council B r1 (Moderate) | clause deleted |
| 2 | rubric[14] admitted the stale In Progress row; an agent updating only `recbd087a4abd605b` passed three criteria | Council B r1 (Minor) | Selection-Logic Ready-status discriminator added to rubrics[14]-[16] |
| 3 | Three titles attributed `$1,140` / `$190` / `$1,622` to "the summary she received", but OE 7 establishes the belief email carries **no** dollar figures | Council B r1 (note) | re-attributed to "originally billed" |
| 4 | **Channel closed set excluded `#maintenance`**, which the stale 4C row — a row OE 4 forces the agent to read — names as this unit's coordination channel | **AUDIT r1 (MAJOR)** | enumeration ultimately **dropped**; criterion now "a StarPM team channel" |
| 5 | Two negative guards; the second vacuously satisfiable and against the corpus rate of 1-in-83 | AUDIT r1 (Minor) | second guard deleted (26 → 25), folded into rubric[9] evidence as an entailment clause |
| 6 | 12 possessive titles; QC Spec Doc1 lists that form verbatim as its Agent-Centric **Non-Fail (3/4)** exemplar, so strictest reading caps at 4 | AUDIT r1 (Minor) | all 12 converted to `The Agent` + verb + context |
| 7 | **Regression from fix 6:** the possessive→active conversion turned rubric[9] from end-state to action phrasing, breaking a valid path — `update_invoice.properties` is unconstrained `object \| null` and `TotalAmt` is server-computed, so a line-array-only envelope writes a correct $1,812 invoice and would have failed | AUDIT r2 (Moderate) | reverted to end-state: "so that it totals $1,812" |
| 8 | **Regression from fix 5:** rubric[13] evidence conjunct re-graded whether the amendment landed, duplicating rubric[8] | AUDIT r2 (Moderate) | rewritten |
| 9 | Channel set still omitted `#general` (grounded per `AUDIT_prompt.md:66`) and `#budget-review` (three cues found by Council B) | AUDIT r2 (Moderate) + Council B r3 (Moderate) | enumeration dropped entirely |
| 10 | **Regression from fix 8:** the rewrite became an exhaustive `fails only if A or B` list plus a disclaimer, removing the vacuity gate — an analysis-only agent triggered neither condition and passed | AUDIT r3 (Minor) | replaced with AUDIT's prescribed **precondition** text, verbatim |

### Adjudicated disputes

- **Density.** Council B put Opus at ~42; AUDIT initially at ~37 blended, reasoning that a stumped run skips the AP-bill leg. **AUDIT conceded** on repo evidence: Task 39 logged Opus **43.5 at 0/6**, and Task 41 logged Opus **48.0 at 0/6 on the identical L2 vendor-linked-AP-bill flagship** with both models never opening the bill; the minimum across all recorded 0%-pass sets is **41.5**. A stumped agent keeps searching rather than skipping. **Record: Opus ~42 (range 32-48), PASS but knife-edge; Gemini ~32, THIN.** AUDIT's **round-1 F3** governance finding (that nothing authorises an Opus THIN) is consequently **withdrawn as a defect** — with Opus empirically at PASS, the Hardness Plan's Gemini-scoped acceptance is correct as written; it is retained only as a prudential watch-item because the low end of the range (32) is THIN and the midpoint is knife-edge. (Numbering note: AUDIT's round-3 text called this "Round 2's F3"; AUDIT corrected itself at closure — round 2's F3 was the separate `#general` omission on rubric[22], which was **fixed** by dropping the enumeration, not withdrawn.)
- **Council A's request** to move the no-fourth-line guard into rubric[9]'s title was **declined**, and the decline was upheld by AUDIT and then withdrawn by Council A on its own evidence: `TotalAmt == sum(Line.Amount)` holds across **385/385** QuickBooks records with zero counterexamples, so a four-line invoice declaring $1,812 is unrepresentable and the guard is a genuine entailment. The proposed edit would have added an independently-failable second claim; the composition alternative would have duplicated rubrics[10]-[12].

### Carried forward — not S3 blockers

- **S4 re-open triggers, per model:** Gemini **< 24**, Opus **< 32** (reconciled from Council B's Opus < 40 and AUDIT's < 30 conditions). Remedy if tripped is a grounded fifth write or an added OE cross-service read — **not** rubric padding, which the Hardness Plan forbids and both gates rejected.
- **Lever L1 (latching) is now live and graded** via rubrics[14]-[16], but `_aux/Hardness_Plan.md` still labels it "reserve". L1 is spent as a margin-deepener. A stale-row latch fails rubrics[14], [15] and [16] together — a genuine Bucket 3 model failure, **not** a bundled-rubric artifact; do not misread it at the All-Failing review.
- **Delivered service breadth is 5, not the 6** the Hardness Plan projects — nothing in the rubric set forces Linear or HubSpot.
- **Pre-upload dry-run** of the four writes whose evidence requires "returned a success response" (rubrics[8], [14], [17], [22]), per `Hardness_Patterns_Log.md:233`.
- **OE-prose nit for FINAL only, do NOT re-run S2:** OE 26/27 attribute dollar figures to the summary email, which OE 7 itself correctly records as carrying none. Values and directions are exact; the rubrics are now strictly more accurate than the OE prose, and the rubric set documents the departure.
- The owner email grades four of OE 26's five body elements (defensible under the prompt's "short note"; both omitted facts have strict companions elsewhere). `2026-519` appears in no title — self-containment holds via a unique amount + scope + vendor triple.

### Instrumentation gaps surfaced (tooling, not deliverable defects)

Recorded because each represents a check the pipeline believes it performs but does not, and each was compensated for by hand this phase:

1. **Fact_Ledger indexes no QuickBooks vendor or customer names.** "Sunshine Cleaning", "Alamo HVAC Services", "Permian Make-Ready Crew" and "Linda Castillo" were therefore **ungated by any automated check** — all four hand-verified against `quickbooks.quickbooks_entities.json` in every round. Same class as the S2-phase finding that `verify_universe_atoms` cannot reach 12-digit QB entity ids.
2. **`validate.py` X2 rubric-OE consistency is `$`-anchored** (`MONEY_RE`, line 171) and the V4 OE convention writes amounts unprefixed, so the check silently self-disables on every StarPM task. Discharged by hand each round: 25 amounts, 0 gaps, every round.
3. **`validate.py`'s Slack service-metadata check is bypassed rather than satisfied** by rubric[22] (regex miss, disclosed by AUDIT); the substantive judgement was made against Eval Phase 2.7 #1 and 2.10 instead.
4. **Cross-document density-threshold inconsistency** — 40 vs 50 vs 15 appear across four files. The StarPM per-model scheme (≥40 PASS / 15-39 THIN / <15 INSUFFICIENT) is the governing one and was applied; the V3-family 50/40 wording in `Reference/Sessions/S3.md` exit criteria and `Reference/Sessions/AUDIT.md` is a live trap for a future operator on a StarPM task.

### Pipeline-improvement item (generalises beyond this task)

Three REVISE rounds produced **three fix-induced side-effects, none visible in a fix summary** — each was caught only by re-auditing the file from scratch. Both AUDIT (N15) and Council B independently converged on the same remedy, recommended for the S3 checklist:

1. A `gate_on_write` assertion for every negative or `keeps`-phrased criterion, plus a criterion/evidence polarity check — exhaustive `fails only if …` lists silently make a criterion vacuously true.
2. When a fix changes wording, re-run every open note whose discharge depended on that wording, plus the alt-paths it made safe. Council B traced both of its own misses to this exact pattern: identify a hazard, discharge it on a property of the current text, fail to re-test when that property moves.

## Verdict

**PASS** — S3 exit criteria met for `7_Rubrics.json` (25 rubrics, 25 outcome / 0 process).

| Exit criterion | Status |
|---|---|
| All rubrics agent-centric, outcome > process, no tool names in titles | **PASS** — 25/25 `The Agent` + finite verb, 25 > 0, zero tool names |
| Validator returns PASS for the rubrics phase | **PASS** — 0 fails; 33 warns all accounted for as three instrumentation classes |
| Council A returns GO with every concrete value grounded | **GO** (iteration 4) |
| Council B returns GO with every QC rubric sub-dim at 5 and zero adversarial hits | **GO** (iteration 4) — 0 Major / 0 Moderate / 0 Minor on 25 |
| Council B-B3 density within band | **PASS (Opus ~42)** · **THIN (Gemini ~32)**, THIN accepted under the Hardness Plan's documented `## THIN density acceptance`; StarPM bands, never the V3-family 50/40 scheme |
| Council B-B4 every Hardness lever covered by an Outcome rubric requiring traversal | **PASS** — 5/5 traced, including L1 promoted from reserve to live |
| Strict veteran AUDIT returns `PASS (STRICT)` | **PASS (STRICT)** — reached after 3 REVISE rounds, at the runbook cap |
| Coverage matrix in place | **PASS** — `_aux/Reasoning/Rubric_Coverage_Matrix.md` |

No `REBUILD` recommendation. No `PROPAGATE TO S1` or `PROPAGATE TO S2` finding — the single OE-prose nit is cosmetic, carries exact values, and is explicitly marked FINAL-only.

Next trigger: **`PIPELINE FINAL — Tasks/43_6a62ccaf5853030245ac9d53`** in a fresh chat.
