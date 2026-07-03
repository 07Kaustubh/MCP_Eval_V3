# Reads — PIPELINE FINAL — Task 35_6a4421ec8169e23828bb442d

## Deliverables (this session, holistic read)
- `Tasks/35_6a4421ec8169e23828bb442d/5_Prompt.txt` :: Robert Calloway Owner voice, ransomware pay-vs-restore + borrower-notice decision; 397 words; new sentence "Anything feeding the same borrower notice counts, even from a separate workstream" verified as F1 fix.
- `Tasks/35_6a4421ec8169e23828bb442d/6_Oracle_Events.txt` :: 27 OEs (1-17 discovery, 18-21 writes to Sloane/D_grace_robert_denise/CRM NOTE/filesystem, 22-27 verification); all tool params match KeyStone `6_Server_Tools_Details.json`.
- `Tasks/35_6a4421ec8169e23828bb442d/7_Rubrics.json` :: 35 outcome, 0 process; flat schema; agent-centric; validator PASS 0/0/5.

## Upstream artifacts
- `_aux/Hardness_Plan.md` :: scenario_14b3ffde anchor, 5 selected levers (§L8 §L9 §L10 §L25 §L26), density midpoint 52.
- `_aux/Fact_Ledger.json` :: 552KB per-task atom surface (personas, emails, amounts, dates, IDs, accounts).
- `_aux/Universe_Split/*` :: contacts, slack channels/users/messages, emails, CRM engagements, mortgage_los loans — deep-queried by prior AUDIT for atom verification.
- `_aux/Verification_s1.md / _s2.md / _s3.md` :: prior PASS verdicts with 6 PROPAGATE flags all honored.
- `_aux/Council_Reports/AUDIT_prompt_v2.md` :: iter-2 PASS (STRICT); F1 (L25 restore) resolved, F2 (D_grace_robert_denise channel) downstream-fixed at S2.
- `_aux/Council_Reports/AUDIT_oe.md` :: PASS (STRICT); all 11 checks clean; 7 propagate flags to S3.
- `_aux/Council_Reports/AUDIT_rubrics.md` :: PASS (STRICT); 48/48 regression anchors; 2 NOTE-level counter-locked observations.
- `_aux/Validator_Reports/prompt.md / oe.md / rubrics.md` :: all PASS.

## Reference docs
- `AGENTS.md` :: 12 hard rules re-read (Opus 4.8 UUT, per-task universe SSOT, 500-word cap, no em-dashes, no "at least N", outcome > process, ≥40 density with 50+ design target, 5/5 QC bar).
- `Reference/Sessions/FINAL.md` :: this runbook; 6 lenses; hard-rule table.
- `Reference/Council_Protocol.md` :: council instructions.
- `Reference/Prompt_Format.md` / `OE_Format.md` / `Rubric_Format.md` :: format cards.
- `Reference/Hardness_Playbook.md` :: 11-lever catalog.
- `Reference/Strict_Convention_Inventory.json` + `OE_Convention_Inventory.json` :: allowed phrasings.

## QC + Eval specs
- `Docs_keystone/7_QC_Spec_Doc1.json` + `Docs_keystone/8_QC_Spec_Doc2.md` :: 21 sub-dim scoring.
- `Docs_keystone/2_Rubrics_V3_Guidelines.md` :: outcome-first, three-condition test, atomicity, Common Mistakes 1-12.
- `Docs_keystone/12_Always_Failing_Rubrics.md` :: AF patterns.
- `Evals_keystone/1_Prompt_Eval.md` :: Prompt phase eval (12 sub-dims).
- `Evals_keystone/2_Oracle_Events_Eval.md` :: OE phase eval (2 sub-dims).
- `Evals_keystone/3_Rubrics_Eval.md` :: Rubric phase eval (5 sub-dims).
- `Evals_keystone/4_Verifier_Fails_Eval.md` :: Bucket 1/2/3 taxonomy for Lens 6 pre-upload simulation.
- `Mortgage_Base_Universe/6_Server_Tools_Details.json` :: KeyStone tool catalog (email content, Slack payload, crm body per-tool traps).

## Cross-task learnings
- `Tasks/_meta/Learnings.md` :: L4 (near-miss entity), L6 (correct-answer-in-artifact rule), L8 (multi-service reduction), L9 (authority dismissal), L10 (structured-DB skip), L15 (implicit prompts), L24 (soft verbs), L25 (existing-output anchor / CROSS_SCENARIO_RECONCILE), L26 (decoy parent thread), L28 (filesystem tool-variant).
