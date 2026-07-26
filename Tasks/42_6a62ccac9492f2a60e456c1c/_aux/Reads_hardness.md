# Reads log — HARDNESS — Tasks/42_6a62ccac9492f2a60e456c1c (v11 E2 gate)

Every reference / spec / eval doc consulted this phase, one line each.

## Reference cards / runbooks
- Reference/Sessions/HARDNESS.md :: phase procedure — lever scan + density projection (per-model, StarPM) + stump hypothesis → Hardness_Plan.md; two hard gates (INSUFFICIENT_LEVERS <3, tiered density).
- Reference/Hardness_Playbook.md :: 11-lever catalog with per-lever tool-call costs; density projection formula; StarPM density bands 40 design / 15 floor per model.
- AGENTS.md :: hard rules — no-edit EXCEPT V4 injection is first-class (add via 9_Universe_inject.sql + 4_Changelog.json, base rows never modified); density framework-scoped (V4 = 40+ avg per model, floor 15, per model).

## Empirical learnings / calibration
- Tasks/_meta/Learnings.md :: L1-L31 + 2026-07-23/24 StarPM entries. Load-bearing: L31 Gemini negative-directive omission (Gemini-selective); item 3/9/10/11/12 = vendor-linked AP-bill arrears symmetric flagship (0/12 twice); L1 owner-latching + L10 reversal-record = Opus-selective; L2 structured-DB skip; net-vs-gross masked if stacked behind discovery lever.
- Tasks/_meta/Stump_Hypotheses.md :: StarPM entries Tasks 38/39/40/41 — banked dual-model 0/6 triad = 1 symmetric stump + 2 complementary asymmetric stumps; per-model density spread (Gemini uses fewer calls).
- Tasks/_meta/Hardness_Patterns_Log.md :: StarPM lever robustness ranking — vendor-linked-AP-bill arrears (symmetric) > negative-directive omission (Gemini) ~ owner-latching/reversal-record (Opus) > net-vs-gross (masked) > near-miss unit (weak). Verify registry landmines instantiated per-task.

## S0 infrastructure consulted
- _aux/Universe_Index/{service_inventory,key_facts,graph_report,entities_personas,today_horizon}.md :: table counts, top personas, QB/Airtable/HubSpot/Slack/Linear inventories, universe today 2026-07-01.
- _aux/Fact_Ledger.json :: atom counts for lever feasibility (amounts 403, emails 206, invoice ids 504, dates 192).
- _aux/S0_Setup_Report.md / Verification_s0.md :: universe=starpm, persona whitelisted, 59 records dated after today (forward-scheduled cal + AP due dates).

## Eval / QC spec docs
- Reference/Sessions/HARDNESS.md :: phase procedure + two hard gates (INSUFFICIENT_LEVERS <3, per-model density); StarPM 40/15 bands.
- Validators/phase_ready.py --phase hardness :: OK — 3 upstream artifacts + Verification_s0 valid.
- Validators/check_verification.py --phase hardness :: OK — Verification_hardness.md sections/categories/verdict valid (aligned to `## Sources consulted` + Per-task/Eval/QC + Verdict PASS after correcting the runbook-template header drift).
