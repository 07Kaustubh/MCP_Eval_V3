# PIPELINE FINAL — Reads log (Task 40_6a614767cd5b60ad96902fb4, StarPM V4)

v11 E2 compliance gate — every QC spec doc / Reference card / Eval spec / validator read for this phase, one line each.

## Runbook + artifacts
- Reference/Sessions/FINAL.md :: FINAL runbook — 6-lens holistic council + (V4) two extra deterministic gates (injection Evals_starpm/0, submission_gate Evals_starpm/5) run BEFORE the council; both must PASS or BLOCKER.
- Tasks/.../5_Prompt.txt :: persona = property manager (Lisa Smith); 5 asks — (1) update Unit 14 make-ready record true-to-state, (2) post account status in #make-ready, (3) draft (do NOT send) email to Brooke end-to-end, (4) set Google Calendar reminder early next week, (5) update the open ticket. Implicit framing: user BELIEVES account cleared + filing squared away; reality is the opposite (trap).
- Tasks/.../6_Oracle_Events.txt :: 19 OEs — disambiguate Sunset Ridge Unit 14 (recc83c05d889b354 / reca8230a8fd9ff51) vs Rio Bend Unit 14 (rec94e86a3007dd5e); hold turn at selSched; account breached-plan + active eviction; bill QR-2026-0441 Balance 2132.00; invoice 7214 zero-balance-but-delinquent conflict; EVF-2026-014 owner-approved but in JP coordination; ESA reasonable-accommodation on record; OPS-32 mirror ticket.
- Tasks/.../7_Rubrics.json :: 16 rubrics, all category=outcome, 0 process.

## Validator + gate results
- Validators/phase_ready.py --phase final :: OK — 7 upstream artifacts present, eval hashes 18/18, Todos_final present.
- Validators/validate.py --phase all :: PASS (prompt 0F/0W, oe 0F/0W, rubrics 0F/4W).
- Validators/validate.py --phase injection :: PASS (0F; 4 notes — difficulty >=3.5 is a COUNCIL judgment to feed the Final Council).
- Validators/validate.py --phase submission_gate :: **FAIL (5 fails)** — F4 rubric #10 $2,132.00 "absent"; F2 rubric #14 dates 2026-07-06/07 "future-dated". BOTH diagnosed as validator false-positives (see below).
- Validators/v4_gates.py :: submission_gate impl. MONEY_RE=`\$[\d,]+(?:\.\d{2})?` (raw substring, no normalization); F2 date check unconditionally rejects any title/evidence ISO date > WINDOW_END (2026-07-01). WINDOW_START=2026-05-01.

## Spec / mandate docs
- Evals_starpm/5_Submission_Gate_Eval.md :: 6 defect families. F4 = "Dollar amount/entity/ID doesn't exist in universe" (BROKEN); F2 = future-as-past = "rubric expects analysis of events not yet happened". Neither mandate covers a grounded amount stored as a bare float, nor an agent-CREATED calendar reminder.
- Validators/regression_baseline/V4_ENFORCEMENT_AUDIT.md :: L39 F2 mandate = "future-dated EXPECTATIONS vs universe today"; L44 F4 mandate = "expected amount ABSENT from SSOT"; L57 strict date-alignment (F6.11) is primarily COUNCIL. → both deterministic checks are firing WIDER than their documented mandate.
- Validators/check_regression.py :: SNAPSHOT_TASKS = 7 (3 brookfield, 2 keystone, 2 moveops), PHASES=[prompt,oe,rubrics]. No starpm, no submission_gate/injection frozen → a v4_gates fix cannot alter frozen report hashes. Will still run check_regression + 62 anchors after any edit.

## Pending (for the council / after gate passes)
- Docs_starpm/7_QC_Spec_Doc1.json + Docs_starpm/8_QC_Spec_Doc2.md :: QC scoring — to be supplied to the Final Council sub-agent.
- _aux/Hardness_Plan.md, _aux/Fact_Ledger.json, _aux/Universe_Index/, Tasks/_meta/Learnings.md :: council inputs.
- _aux/Validator_Reports/injection.md COUNCIL notes :: feed to Final Council (difficulty >= 3.5 judgment).

## Blocker status
submission_gate FAIL is a hard BLOCKER (FINAL.md V4 gate). Oracle consulted (bg_6a7734aa) on the exact validator-precision fix (F4 money normalization + F2 calendar-create exemption) + regression safety BEFORE any edit. Implementation blocked until Oracle returns.
