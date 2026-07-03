# Reads Log — HARDNESS

Every QC spec doc / Reference card / Eval spec read during this phase, one line each.

## Reference cards
- `Reference/Hardness_Playbook.md` :: 11-lever catalog with per-lever tool-call cost ranges + tiered density gate (>=50 PASS / 40-49 THIN / <40 STOP). Composition rules (4-5 levers default; 3+ writes across 3+ services).
- `Reference/Sessions/HARDNESS.md` :: This phase's runbook. Confirmed procedure, exit criteria, gate handling, and v16 cross-source verification format.

## Cross-task learnings
- `Tasks/_meta/Learnings.md` :: L1-L30 empirical failure-mode catalog. Confirmed target anatomy: L8 (multi-service reductions) + L9 (authority dismissal soft-verb per L24) + L10 (structured-DB skip) + L25 (existing-output anchor) + L26 (decoy parent thread) + L29 (avoid escape-valve on load-bearing surface). KeyStone universe has no SAP subledger — the L10 "structured-DB skip" needs a KeyStone-native surrogate (mortgage_los.conditions / mortgage_los.disclosures / mortgage_los.document_checklist_items).

## Universe registry
- `Validators/universes.py` (KeyStone section) :: Services are mortgage_los / stripe / filesystem / crm / quickbooks / email / slack / contacts. TRID timing + Marcus Webb departed-employee are the two hardcoded landmines. No account-number trap (loan-based, not GL-based).

## KeyStone framework docs
- `Docs_keystone/` :: To be consulted at S1/S2/S3 for QC sub-dim scoring. Not required for HARDNESS lever selection (Playbook + Learnings are the primary sources for this phase).

## Eval spec
- N/A for HARDNESS lever-scan phase — Eval sub-dims (Prompt / OE / Rubric / Verifier-Fails) engage at S1-S4. HARDNESS only constrains the trajectory dim `Tool Call Count` (>= 15 spec floor; pipeline targets 50+ midpoint).

## QC spec
- N/A for HARDNESS lever-scan phase — QC sub-dims engage at S1/S2/S3. The only QC touchpoint HARDNESS respects is Trajectory T1 Tool Call Count via the density projection gate.

## Per-task S0 artifacts
- `_aux/S0_Setup_Report.md` :: Executive persona = Robert Calloway; 7 open scenarios; universe today = 2026-04-28; ~31k records / 34 sources.
- `_aux/Universe_Index/service_inventory.md` :: emails 7287 / email.threads 2504 / slack 573 / mortgage_los.loans 644 / borrowers 638 / conditions 32 / document_checklist_items 8841 / disclosures? (not listed — confirm at scan) / crm.crm_engagements 472 / stripe.fc_transactions 3228 / quickbooks.bills 585.
- `_aux/Universe_Index/graph_report.md` :: Robert-adjacent people cluster (Grace / Denise / Priya / Marcus Webb / Amy Chen). Top volumes: Sofia Reyes (776), Rachel Kim (753), Darnell Price (716). No BlackLine / no JE-period counts (KeyStone schema, expected).
- `_aux/Universe_Index/key_facts.md` :: 7287 emails / 573 Slack messages. Slack top channels: C002 (334), C001 (55), C004 (28), C008 (24). D_grace_robert (21) and D_denise_grace (10) DMs are relevant to Robert's escalations.
- `_aux/Fact_Ledger.json` :: 1923 emails, 4446 amounts, 808 dates, 1306 personas. Rich enough for multi-surface lever anchoring.
- `_aux/Feasible_Surface.json` :: 21 tables with enums. Confirmed loan statuses (application/conditional_approval/processing/underwriting/clear_to_close/closed/denied/withdrawn) and condition statuses (outstanding/cleared).

## REDO context
- `_aux/REDO_reason.md` :: NOT PRESENT — fresh CB build.
- `_aux/Candidate_Originals/` :: NOT PRESENT — fresh CB build.
