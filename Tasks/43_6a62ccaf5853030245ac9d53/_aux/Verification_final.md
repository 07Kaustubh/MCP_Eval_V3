# Verification — PIPELINE FINAL · Task 43_6a62ccaf5853030245ac9d53

**Universe:** StarPM V4 (dual-model: 6 Opus 4.8 + 6 Gemini) · **Persona:** Carlos Mendez, Onsite Property Manager (`carlos.mendez@starpm.com`, `p_009`) · **Today in-universe:** 2026-07-01 America/Chicago.
**Downstream state:** `8a`/`8b_Verifier_Fails`, `9_QC_Feedback`, `10`/`11` PT-dispute files are 0 bytes and `Agent_Responses/{Opus,Gemini}/` are unpopulated. Task not yet run, so density is a **projection**, not a measurement. Expected at this phase.

## Sources consulted
Categories covered below: **Per-task data** (`_aux/Universe_Split/`, `_aux/Fact_Ledger.json`, `_aux/Feasible_Surface.json`), **Eval spec** (`Evals_starpm/0-5`, next section), **QC spec** (`Docs_starpm/7_QC_Spec_Doc1.json` + `8_QC_Spec_Doc2.md`, section below).

- All 3 artifacts (`5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json`) read together, not in isolation.
- `_aux/Universe_Split/` :: cross-verified the end-to-end dependency chain (Airtable make-ready rows -> QB AP bills -> AR invoice 2026-534 -> owner email -> Slack C004).
- `_aux/Fact_Ledger.json` :: 403 amounts / 206 emails indexed; every atom in the artifacts traced to the ledger or to a `Universe_Split` row.
- `_aux/Hardness_Plan.md` :: lever preservation traced through the artifact set; FINAL carry-forward appended.
- `_aux/Verification_s1.md` / `Verification_s2.md` / `Verification_s3.md` :: prior phase verifications cross-referenced.
- `_aux/Feasible_Surface.json` :: confirms `fldTurnStatus` enum is exactly {selSched, selProg, selReady} — no "Closed" option, which is what forces OE 25 / rubrics 16-17 into `fldNotes2`.
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: exact per-tool parameter lists for the Lens 5 binding check.

## All eval specs verified (StarPM routing — no cross-universe spec loaded)
- `Evals_starpm/1_Prompt_Eval.md` :: prompt eval re-applied at the integration layer. The one validator WARN (bolt-on candidate) adjudicated a FALSE POSITIVE by remove-sentence test: deleting the sentence leaves "Then email Linda..." with no antecedent action and "where it landed" with no referent.
- `Evals_starpm/2_OE_Eval.md` :: OE eval re-applied. 28 steps, inside the `OE_Convention_Inventory.json` distribution. Coverage treated as unordered; lifecycle ordering not applicable (no closed fiscal periods in `Fact_Ledger.lifecycle.closed_periods`).
- `Evals_starpm/3_Rubrics_Eval.md` :: rubrics eval re-applied. 25 Outcome / 0 Process. 0/25 Major, 0/25 Moderate+.
- `Evals_starpm/4_Verifier_Fails_Eval.md` :: Lens 6 simulated bucket classification for all 25 rubrics. 4/25 = 16.0% Bucket_1_Risk (<= 20%); all four hardened in place.
- `Evals_starpm/0_Injection_Quality_Eval.md` :: presence-gated. `4_Changelog.json` == `[]` and `9_Universe_inject.sql` is a comment-only template header, so this is a **no-injection task**. Gate PASS, 0 fails.
- `Evals_starpm/5_Submission_Gate_Eval.md` :: F1-F6 defect families. **Initially 4 FAILs (F5 NEEDS_TOOL_OUTPUT)**; fixed in place, re-run PASS 0 fails.

## QC spec full coverage check (`Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md`)
- All Prompt sub-dims :: scored. Implicit framing preserved; no pre-solving; no tool names; 364 words (under the 500 cap).
- All Universe sub-dims :: scored. No base-universe edits, no injection.
- All OE sub-dims :: scored. Every tool named exists; every parameter binding is on the exact named tool.
- All Rubric sub-dims :: scored. Atomicity, self-containment, Outcome/Process split, exact-value mandate.
- Trajectory sub-dims :: T1 only at this phase; T2/T3 deferred to S4 (task not yet run).

## Verification statements
- [x] Validator `validate.py --phase all` exit 0 across all 3 artifacts (prompt PASS / oe PASS / rubrics PASS).
- [x] V4 gate `validate.py --phase injection` PASS (0 fails).
- [x] V4 gate `validate.py --phase submission_gate` PASS (0 fails) — after fixing 4 F5 NEEDS_TOOL_OUTPUT defects.
- [x] 6 FINAL lenses returned PASS (Truthfulness / Rubric Binding / Cross-Artifact Holism / Red-team / Narrative-State + Action-Prescription / Verifier-Fails-Spec Pre-Upload).
- [x] Zero answer leakage. `$1,812` and the `$190` net delta appear nowhere as money in `5_Prompt.txt` or in any agent-readable universe surface. All 17 raw `1812` hits in the universe are `history_id` / `internal_date` / Slack-ts / Airtable-microsecond substrings. `Fact_Ledger.amounts[]` holds 1622 / 1140 / 95 / 387 / 1340 / 85 but NOT 1812.00, confirming derive-only.
- [x] Every tight identifier in all 3 artifacts resolves to a real `Universe_Split` row. Zero phantoms.
- [x] Every Hardness lever still triggers end-to-end (L2 / L10 / L6 / L11 mapped to a prompt sentence + OE step + rubric each), with the MAJOR-1 yield caveat recorded.
- [x] Every OE tool-parameter binding verified on the EXACT named tool.
- [x] Outcome (25) > Process (0). No tool names in rubric titles. No em-dashes. No cross-universe tokens.

## Ground truth re-derived from source (not taken from upstream phases)
| Component | Bill id | DocNumber | Vendor | Amount | Invoice line |
|---|---|---|---|---:|---|
| Post-move-out deep clean | `195089456477` | 2026-SC-4C | Sunshine Cleaning | 387.00 | line 1 = 387.00 (ties) |
| Interior repaint | `696089964235` | PD-2026-09 | Permian Make-Ready Crew | 1340.00 | line 2 = 1140.00 (**-200 understated**) |
| Closet trim touch-up | `546359391323` | 2026-519 | Permian Make-Ready Crew | 85.00 | line 3 = 95.00 (**+10 overstated**) |
| Condition walk (**excluded**) | `991582431419` | 2026-481-566 | Alamo HVAC Services | 85.00 | absent from the invoice |

Correct owner pass-through **387 + 1340 + 85 = 1812.00** against invoice `445653930748` (Doc 2026-534, Linda Castillo `proj-4ae920b7c9e8`, TotalAmt/Balance 1622.00, `sync_token` `"0"`). Net **190.00** understated. Decoys recompute exactly: 1897 (adds the internal walk), 1727 (drops the closet trim), 1810 (substitutes the 385.00 Rio Bend deep clean on invoice 2547).

## Density projection (per-model — StarPM gate 40 design target / 15 fail floor, NOT the Brookfield 50/40 scheme)
| Model | Band | Midpoint | Band verdict |
|---|---|---:|---|
| Opus 4.8 | 38-53 | ~45 | **PASS (>= 40)** |
| Gemini | 30-43 | ~36 | **THIN (15-39)**, well clear of the 15 floor |

Gemini THIN is **accepted, not waived**: `_aux/Hardness_Plan.md` carries the per-task justification, and the promised mitigation was delivered and verified here — **4 writes across 4 services** (OE 24 `update_invoice`, OE 25 `update_records_for_table`, OE 26 `create_draft`, OE 27 `slack_send_message`). Service breadth 5-6 distinct, each >= 5%, quickbooks ~42% (< 60%).
**S4 watch-item:** carry a per-model density spread, not one midpoint. If the first Gemini run lands < 30, the OE needs another grounded write before any re-upload.

## Discrepancies surfaced
1. **[FIXED — was a deterministic FAIL]** `submission_gate` F5 NEEDS_TOOL_OUTPUT on rubrics 9 / 15 / 18 / 23 (1-indexed): evidence ended "and confirm the tool returned a success response". Rewritten to grade from call arguments only. Gate re-run 0 fails.
2. **[FIXED — Lens 6, 4 rubrics]** Bucket_1_Risk hardening on `rubric[4]`, `rubric[19]`, `rubric[21]`, `rubric[24]`. See the council report addendum for the per-rubric change.
3. **[FIXED — Lens 2 / MAJOR-2]** `rubric[7]` evidence now discloses the summary-email corroboration for keeping the $85 closet trim owner-billable. Ground truth remains unique: the prompt's own exclusion is narrowed to "an internal walk or a condition check", and `"Internal labor charge for"` appears on exactly 2 records universe-wide (both $85 bills), so that phrase discriminates nothing.
4. **[CARRIED FORWARD — MAJOR-1, no artifact change]** L2 flagship yield is optimistic; `5_Prompt.txt` sentence 3 points at the AP side (Learnings L29 pattern). Not fixed by design — removing the reconciliation ask would cost Feasibility/Clarity. Expected sweep re-attributed to L6/L11 in `_aux/Hardness_Plan.md`.
5. **[NO ACTION — validator false positives]** Prompt "bolt-on candidate" WARN fails the remove-sentence test. The 26 rubric X2 amount-consistency WARNs are an extractor artifact (the matcher requires a `$` prefix; the OEs write bare figures such as `1340.00`); all amounts hand-verified present in the OE text. The `$1,812` / `$10` / `$190` "not in Fact_Ledger" WARNs are the intended derive-only signature, not defects.

6. **[ADJUDICATED then PARTIALLY REVERSED — platform QC atomicity challenge, two passes, 2026-07-25]** First pass flagged 4 criteria; `rubric[0]` was retitled (recipient ambiguity) and a genuine stack the check missed was fixed at `rubric[13]`. Second pass narrowed to `rubric[2]` and `rubric[19]` with a stronger argument, and **it was correct**: `8_QC_Spec_Doc2.md` scopes acceptable bundling to "the same source / the same relocation record" and states plainly that "components from separate tool outputs should NOT be grouped". $1,340 (`get-bill`) and $1,140 (`read_invoice`) are two records from two calls. `rubric[2]`, `rubric[3]` and `rubric[19]` were tightened to one source-value each, with the invoice-side figure and derived delta demoted to `evidence` as marked grounding. Not split into three (that would create a free-pass rubric on the mandatory invoice read). `rubric[3]` was fixed although the second pass dropped it, since it is the identical shape. `rubric[10]`/`rubric[11]` deliberately unchanged: write-state criteria whose "from" value is universe pre-state the Agent never asserts. Bucket_1_Risk falls 4/25 (16.0%) -> 3/25 (12.0%). All 5 gates re-run PASS. Full adjudication in `_aux/Council_Reports/FINAL_council.md` ADDENDUM 2 + ADDENDUM 3.

7. **[THIRD PASS — reasoning rejected, remedy applied]** `rubric[24]` (platform #25) flagged as bundling supersession + the `$1,622` amount. The stated reasoning misread the evidence field, whose disjunction already made naming the amount optional. The parenthetical in the criterion was nonetheless a real residual (the same criterion-stricter-than-evidence defect Lens 6 logged against this rubric originally, now hit by a second independent pass), so it was removed and the amount demoted to marked grounding. Bucket_1_Risk 3/25 (12.0%) -> 2/25 (8.0%). `rubric[10]`/`rubric[11]` confirmed atomic and unchanged: their second dollar figure is universe pre-state the Agent never asserts, so it cannot contribute an independent failure. See ADDENDUM 4.

8. **[FOURTH PASS — 1 stale, 1 invalid]** Atomicity re-flag on `rubric[24]` quoted the pre-ADDENDUM-4 title and is stale; no action beyond platform sync. Overlap finding claiming `rubric[9]` (invoice totals $1,812) is redundant with `rubric[10]`/`rubric[11]`/`rubric[12]` is **invalid**: a four-line amendment that adds the 85 condition walk passes all three line criteria while totalling 1,897 and failing `rubric[9]`, and 1,897 is a designed decoy. Converse also fails (1,350 + 75 + 387 = 1,812). `rubric[9]` justification hardened with both counter-examples; title deliberately unchanged to avoid tripping the atomicity check. See ADDENDUM 5.

## Verdict
`_aux/Council_Reports/FINAL_council.md` :: **VERDICT: PASS** — 0 BLOCKER, 2 MAJOR (both dispositioned), Bucket_1_Risk 16.0%. Cleared for platform upload. Verification is dual-model: BOTH Opus and Gemini runs are expected downstream (`8a`/`8b` + `Agent_Responses/{Opus,Gemini}/`).
