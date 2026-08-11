# Reads — PIPELINE FINAL (v11 E2 compliance log)

Universe routed from `_aux/Universe.txt` = `harmonygames`. No other universe's spec was loaded.
**Round 2** — the artifacts were edited after round 1 closed, so every claim below was re-derived
rather than carried forward from `FINAL_council.md` round 1 (AGENTS.md rule 19: chains of internal
citation are not evidence about the artifact).

## QC spec / eval docs
- `Docs_harmonygames/7_QC_Spec_Doc1.json` :: 7 dims / 38 sub-dims, 18 BINARY; Rubric Category Balance is a flat Process <= 40% cap, no Outcome-majority rule.
- `Docs_harmonygames/8_QC_Spec_Doc2.md` :: severity taxonomy; Overly Broad = Moderate, Overly Specific = Minor (the reverse of StarPM). `:270` vague-exemplar scan, `:295`/`:302` negative-criteria method.
- `Evals_harmonygames/3_Rubrics_Eval.md` :: line 7 and the Phase 1.2 HARD GATE fix the `category` enum at `Outcome 1.1` / `Outcome 1.2` / `Outcome 2.1` / `Process`; Accuracy principle ("unobservable values = wrong scoring"); Requirement Provenance HARD GATE (OE-only requirement = Incorrect, Major); Atomicity Decomposition HARD GATE; Exclusion / Decoy Coverage HARD GATE; Gap 3 Final-Response Coverage.
- `Evals_harmonygames/1_Prompt_Eval.md`, `/2_OE_Eval.md` :: re-applied at the integration layer via `validate.py`.
- `Evals_harmonygames/4_Verifier_Fails_Eval.md` :: Lens 6 bucket simulation basis.
- `Evals_harmonygames/5_Submission_Gate_Eval.md` :: F-family defects; P2 weekend-comms anchor against rubric text.
- `Evals_harmonygames/0_Injection_Quality_Eval.md` :: floor 2.5; this task injects nothing (`4_Changelog.json` = `[]`).
- `Docs_harmonygames/14_Persona_ACL.md` :: `:17` ACL does not govern writes; `:129` "inaccessible content cannot be required ground truth"; `:134` an ACL denial may not be made necessary to a prompt, OE or rubric. This is the authority behind the removal of the 12K criterion.
- `Docs_harmonygames/12_Always_Failing_Rubrics.md` :: "use exact values for IDs, dates, counts"; "approximately only for genuinely calculated or rounded values"; "do not loosen exact source values". Applied to the 15,000 / 13,000-15,000 wind-down cost (rounded at source, so approximate is correct) and against widening the Singular criterion.
- `Reference/Sessions/FINAL.md` :: the six lenses and the binding hard-rule table.
- `Reference/Council_Protocol.md` (B3 density SSOT) :: the 50/40 bands are V3-family and do not apply; HG authoring target is 40+ calls and 3+ services, QC floor >= 15 average.
- `AGENTS.md` :: hard rules 2, 11, 13, 14 (60-cap and the OE-mirroring duty), 19, 21 (default to removal), 26, 28 (weak assertions), 32 (persona ACL is a feasibility gate).
- `QC_Tasks/V5_HG_Buckets/QC_Passed/Task1_6a625f3ea428e7b7d971e57f_HG/7_Rubrics.json` :: read to confirm the shipped HG evidence convention is a grading instruction, not a `Per OE#` back-reference. FINAL.md's `Per OE#` line is a Brookfield convention and does not govern here.

## Universe sources (HG contract: `base_export_plus_changelog`)
- `Validators/check_hydration.py` :: `[OK] harmonygames: payload hydrated and matches its manifest`. Run before any data claim.
- `snowflake/snowflake.tables.json` :: AD_SPEND_DAILY, DAILY_ACTIVE_USERS, REVENUE_DAILY, IAP_TRANSACTIONS, CASH_BALANCE, REVENUE_DAILY_V2, UA_SPEND_UNIFIED_V2 re-aggregated row by row. Every figure in the artifact set reproduced exactly.
- `slack/messages/{C0ADGSZKR3R,C07C2866011,C04UEQVDVB7,D04UC0UEN2V}/2026-02.json` :: all 21 cited timestamps opened and quoted against.
- `slack/slack.channels.json` + `slack.users.json` :: member arrays and author identities; D04UC0UEN2V members confirmed as U04SNNV580G / U04UP2L1RUY, excluding Robert's U04TWDMDT0V.
- `gmail/threads/EMPLOYEE_0016_EMAIL_*.json` :: all 16,249 of Robert's threads swept for 10,800 / 8,452 / 11,700 / 22,500 / 18,750 / 6,250 / 9,717 / 24,275 / 13,000 with word-boundary matching on subject and body.
- `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` :: all 22 tools named in the OE resolved; every parameter checked against that specific tool.
- `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json` :: Leonard Hayes and Arthur Blake email forms confirmed against the roster rather than constructed.
- `confluence/confluence.spaces.json`, `linear/linear.teams.json`, `trello/trello.lists.json` :: COMPANY, team_ENG and list 670015c2ecd45b634d5eec81 confirmed as real rows.
- `gcal/*.json`, `gslides/*.json` :: 3 bytes each, so the hard-rule-13 Calendar sweep is vacuously clear (deviation HG-U11 leaves F9 unavailable here).
