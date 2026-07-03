# Verification — HARDNESS (Task 36)

## Sources consulted
- **Per-task data**: `_aux/Universe_Split/*` (25 JSON files, 1705 rows); `_aux/Fact_Ledger.json` (216 emails, 64 amounts, 155 dates, 132 personas, 9 slack channels); `_aux/Universe_Index/graph_report.md` (Julian in top-30 by mentions); `_aux/Universe_Index/service_inventory.md` (7 active services — airtable / contacts / crm / email / linear / quickbooks / slack); grepped for Terraform/Vantage, BrightLoop/Simone/Marcus Webb, NorthWind/Emilia Cruz, StormCloud/Jae-won, AWS spike, UrbanNest/Carmen Reyes, PHMSA hazmat.
- **Persona and business function**: `Tasks/36_6a44224ed5d3b47d6d727cf5/PersonaBrief.txt`, `2_Persona.txt`, `1_Business_Function.txt`, `_aux/S0_Setup_Report.md`.
- **Universe constants**: `AGENTS.md` (MoveOps timezone / landmines / V2.1 framework note), `_aux/Universe.txt` (auto-detected `moveops`).
- **Reference docs**: `Reference/Hardness_Playbook.md` (11-lever catalog with per-lever cost ranges + tiered density gate 50+/40-49/<40); `Reference/Sessions/HARDNESS.md` (phase runbook + procedure); `Tasks/_meta/Learnings.md` (L1-L30 empirical evidence).
- **Eval spec**: `Evals_moveops/1_Prompt_Eval.md`, `Evals_moveops/2_OE_Eval.md`, `Evals_moveops/3_Rubrics_Eval.md`, `Evals_moveops/4_Verifier_Fails_Eval.md` — HARDNESS produces the plan; sub-dims are checked at downstream phases.
- **QC spec**: `Docs_moveops/1_Prompt_V3_Guidelines.md`, `Docs_moveops/2_Rubrics_V3_Guidelines.md`, `Docs_moveops/3_Oracle_Events_V3_Guidelines.md` — HARDNESS Brief feeds S1 (which will apply QC prompt guidelines).

## Data sources consulted
- `_aux/Universe_Split/` :: sampled airtable.records, crm.crm_engagements, email.emails, quickbooks.invoices, slack.slack_messages for lever-scanning grounding.
- `_aux/Fact_Ledger.json` :: verified atom availability (emails / amounts / personas count non-zero) supports the L25 + L9 + L26 + L2 combination.
- `_aux/Universe_Index/graph_report.md` :: confirmed Julian in top-30 by mentions (24 emails + 19 Slack + 3 Linear comments); no JEs / no BlackLine / no reconciliations (MoveOps is operational).

## Reference docs consulted
- `Reference/Hardness_Playbook.md` :: applied 11-lever framework; MoveOps-adapted L2 to Airtable / QB / CRM engagement per HARDNESS runbook translation guidance; applied tiered density gate.
- `Tasks/_meta/Learnings.md` :: cited L2, L6, L8, L9, L14, L15, L16, L24, L25, L26, L29 in lever rationale; explicitly avoided L1, L4-alone, L5-alone, L7 per Learnings guidance.

## Eval spec sub-dims relevant to this phase
- **Trajectory dim Tool Call Count** (floor ≥ 15; pipeline targets 50+ midpoint) :: projected midpoint = 50 (range 41–59). PASS at design target.

## QC spec sub-dims relevant to this phase
- **Trajectory T1 Tool Call Count** :: projected midpoint 50, PASS band. Conservative baseline 41 also clears THIN floor of 40. **Note:** midpoint sits AT the 50 boundary — S1 must be sized to include ALL sketched writes to hit this reliably; skipping the internal status email + calendar hold could drop to ~45 (THIN).

## Verification statements
- [x] At least 3 levers selected — 4 primary levers (L25, L9, L26, L2 MoveOps-adapted) + emergent L8 anatomy; each cites a Learnings entry (L25 = highest-yield novel stump; L9 = ~100% fail most-effective single mechanism; L26 = 80%+ failure on canonical thread_ts; L2 = MoveOps-adapted structured-DB skip; L8 = ~40% pass target failure).
- [x] Density midpoint projection = **50** (range 41–59) — PASS at design target ≥ 50; conservative baseline (41) also clears the THIN 40 floor.
- [x] Service breadth table populated — 7 distinct services with ≥ 5% (email 24%, slack 20%, airtable 14%, crm 10%, linear 8%, contacts 8%, quickbooks 8%); dominant service well under 60%. PASS on breadth gate.
- [x] Must-not lever anti-patterns respected — L1 (confirm-already-done), L4-alone (near-miss entity), L5-alone (action-incompleteness), L6 (correction email stating answer), L7 (binary is-it-posted) all avoided.
- [x] MoveOps landmines surfaced (Marcus Webb 3-way identity across brightloopanalytics.com / ironcladsec.com / gmail.com; Simone 2-way identity BrightLoop vs StormCloud; Airtable-vs-CRM SSOT; PHMSA hazmat) but not relied on as standalone levers.
- [x] L29 escape-valve guardrail respected — brief instructs S1 NOT to include invitations to surface contradictions (would neutralize L2).
- [x] Timezone-sensitive lever explicitly NOT picked (today_horizon.json discrepancy with AGENTS.md is documented in S0 report; hardness plan does not depend on time-of-day resolution).

## Discrepancies surfaced
- **Density midpoint sits AT the 50 PASS boundary** — S1 must include ALL sketched write actions (email × 2, Slack post, Airtable update × 2, CRM engagement update, Linear comment, calendar hold, internal status email) to hit the design target reliably. If S1 phase reduces the write-action mix (e.g., drops Linear comment or internal status email), the projection can drop to ~45 (THIN band). Flag for S1 phase.
- **Persona-attribution landmine is present but secondary** — 3× Marcus Webb + 2× Simone Richter identities. Auto-memory `persona_attribution_landmine.md` and `review_audit_must_deep_query_universe.md` apply. S3 grounding + AUDIT + FINAL must grep both candidate addresses before latching.
- **S0 timezone label discrepancy inherited** — `today_horizon.json` says `America/New_York`, `AGENTS.md` says `US/Pacific` for MoveOps. HARDNESS did not resolve this. No lever depends on timezone precision, so non-blocking; S1 must still respect the date `2026-04-26` as universe today.

## Verdict
**PASS.** 4/5 levers grounded, density midpoint 50 (PASS at design target), service breadth 7 distinct services (PASS). Proceed to S1 with the Hardness Brief.
