# Reads — PIPELINE FINAL · Task 43_6a62ccaf5853030245ac9d53

v11 E2 compliance gate. Every spec doc / reference card / eval spec consulted this phase, one line each.

## Runbook + project bootstrap
- `AGENTS.md` :: confirmed hard rules 1-12; rule 4 V4 injection exception; rule 11 density is framework-scoped (StarPM = 40+ design target per model, 15 fail floor, NOT the Brookfield 50/40 scheme); rule 8 Outcome must outnumber Process.
- `Reference/Sessions/FINAL.md` :: 6-lens roster, 13 binding hard-rule gates, V4 extra gates (injection + submission_gate must PASS before the council call), STOP-gate contract.
- `Reference/Council_Protocol.md` :: B3 density projection is the SSOT for the tiered density gate; council verdict vocabulary.

## Universe routing (StarPM — no cross-universe spec loading)
- `Tasks/43_.../_aux/Universe.txt` :: `starpm` -> route to `Docs_starpm/` + `Evals_starpm/`. Brookfield `Docs/` and KeyStone/MoveOps specs NOT loaded.
- `Docs_starpm/7_QC_Spec_Doc1.json` :: QC sub-dimension set + 1/3/5 scoring bands for Prompt (12), Universe (2), OE (2), Rubric (5), Trajectory.
- `Docs_starpm/8_QC_Spec_Doc2.md` :: companion scoring prose; fail-floor definitions.
- `Docs_starpm/1_Project_Instructions_Overall.md` :: hard gate "AVERAGE TOOL CALL COUNT OF ALL AGENT RUNS MUST BE 40+" — the StarPM density authority.
- `Docs_starpm/2_Rubrics_V3_Guidelines.md` + `3_Rubrics_V3_One_Pager.md` :: atomicity, Outcome/Process split, self-containment, exact-value mandate for IDs/dates/amounts.
- `Docs_starpm/12_Always_Failing_Rubrics.md` :: redundancy / manufactured-split anti-pattern.
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: per-tool exact parameter lists for Lens 5 binding checks (`slack_send_message`->message, `create_draft`->body, `update_records_for_table`->baseId/tableId/records, `search_records`->table vs `list_records_for_table`->tableId, `get-bill` hyphenated).

## Eval specs (all 4 + 2 V4-only, re-applied at the integration layer)
- `Evals_starpm/0_Injection_Quality_Eval.md` :: 7 hard gates; this task is no-injection (`4_Changelog.json` == `[]`, `9_Universe_inject.sql` comment-only) so the gate runs presence-gated and PASSes; difficulty >= 3.5 deferred to council.
- `Evals_starpm/1_Prompt_Eval.md` :: prompt sub-dims re-applied at integration layer (coherence / pre-solving / tool-mention / relative-date).
- `Evals_starpm/2_OE_Eval.md` :: OE coverage unordered, lifecycle ordered where preconditions apply.
- `Evals_starpm/3_Rubrics_Eval.md` :: severity taxonomy; channel-lock-in Major-by-default per pipeline deviation table.
- `Evals_starpm/4_Verifier_Fails_Eval.md` :: Bucket 1 / 2 / 3 taxonomy — the basis for Lens 6 pre-upload simulation.
- `Evals_starpm/5_Submission_Gate_Eval.md` :: defect families F1-F6; F5 NEEDS_TOOL_OUTPUT table rows 19-21 ("criterion checks 'tool returned success'") — the rule that fired 4 FAILs this phase and drove the rubric evidence fix.

## Prior-phase carry-forward
- `_aux/Hardness_Plan.md` :: 4 selected levers (L2 flagship / L10 / L6 / L11) + reserve L1; per-model density Opus 43.5 PASS, Gemini ~34 THIN with documented acceptance.
- `_aux/Verification_s1.md` / `Verification_s2.md` / `Verification_s3.md` :: prior phase verifications cross-referenced.
- `_aux/Fact_Ledger.json` :: 403 amounts / 206 emails indexed — atom SSOT for the identifier grep.
- `_aux/Feasible_Surface.json` :: 15 tables with enum maps — confirms `fldTurnStatus` has no "Closed" option.
- `Tasks/_meta/Learnings.md` :: empirical Opus 4.8 failure modes (L2/L4/L6/L10/L11/L13/L15/L16 references used by the Hardness Plan).
