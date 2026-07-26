# Verification — HARDNESS — Tasks/39_6a602c8886ebb06f12354d77

## Sources consulted

Categories consulted for this phase. **Per-task data**: `_aux/Universe_Split/`, `_aux/Fact_Ledger.json`, `_aux/Universe_Index/`. **Eval spec**: `Evals_starpm/` trajectory Tool Call Count dim. **QC spec**: `Docs_starpm/7_QC_Spec_Doc1.json` trajectory T1. Detail per category follows in this section and the two spec sub-dim sections below.
- `_aux/Universe_Split/` :: grep-verified the load-bearing rows in `airtable.airtable_records.json` (receb057b02f20052, recf7aecc318b2252, rec651427ec0d84dd5a, recac236210094352=MT-2026-1271 OPEN, recb403fe04c2f97683=Rio Bend 214), `linear.linear_comments.json` (comment_16a0a0c53f... OPS-227 disposal flip), `linear.linear_teams.json` (team_001 Airtable-is-SoR), `slack.slack_messages.json` (8D "done" latching). Counted the 204B decoy swarm (61) vs 8D (6).
- `_aux/Fact_Ledger.json` :: atom surface confirmed feasible for the levers — amounts 403, dates 192, emails 206, ids (airtable_record 170, linear_issue 230, linear_comment 48, invoice 504). entities 0 / fiscal_periods 0 (expected-zero StarPM; confirms no GL/account-number trap).
- `_aux/Universe_Index/` :: graph_report + service_inventory + entities_personas + key_facts + today_horizon consulted by the deep-reasoning sub-agent for table volumes and persona roster (John Smith / Tony Reyes / Elias Navarro Leads; James Bennett p_006 junior).
- `_aux/S0_Setup_Report.md` :: read for universe/persona/injection status (discrepancy found, see below).
- `9_Universe_inject.sql` + `4_Changelog.json` :: read in full — inject is a comment-only stub, changelog is `[]`.
- `Agent_Responses/` :: `parse_trajectories.py` → 0/12 evaluable (all empty scaffolds); confirms this is a fresh forward HARDNESS, not a retrospective.

## Reference docs consulted
- `Reference/Hardness_Playbook.md` :: all 11 levers considered; selected L10 / L2 / L1 / L4 / L3 (5). L11 net-vs-gross considered and rejected (finance-flavored, unnatural for a junior tech; no GL in StarPM). L5 thread-reply marked partial (no confirmed 8D-critical reply resolution in base data).
- `Tasks/_meta/Learnings.md` :: cited L25 (stale-artifact anchor → L10), L10 (structured-DB skip → L2, Airtable as the StarPM analog), L13 (first-framing → L1), L26 (decoy overlap → L4), L12 (reply invisibility → L3), plus L9 (authority dismissal) reserved for the optional injection, and L6/L15 (implicit prompt, no verbatim answer) as prompt-design constraints. Explicitly avoided L4-near-miss-alone and L5-action-incompleteness-alone (do not fail the models).

## Eval spec sub-dims relevant to this phase
- Trajectory dim Tool Call Count :: **framework-scoped to StarPM V4** — floor 15, design target 40+ per model (NOT the V3-family 50+ midpoint). Projected per-model midpoint **48.5** → PASS.

## QC spec sub-dims relevant to this phase
- Trajectory T1 Tool Call Count :: projected per-model midpoint **48.5**, band **PASS** (StarPM V4: >= 40 PASS, 15-39 THIN, < 15 INSUFFICIENT).

## Verification statements
- [x] At least 3 levers selected (5 selected); each cites a Learnings.md entry (L25, L10, L13, L26, L12).
- [x] Density midpoint projection classified against the **StarPM V4** bands (framework-correct substitution for the template's V3-family `{PASS >= 50, THIN 40-49, INSUFFICIENT < 40}`): result **PASS (>= 40)** at 48.5/model.
- [x] Service breadth table populated (v11 G1): 6 distinct services >= 5%, 4 write surfaces → PASS.
- [x] Every yes/partial lever's cited row independently grep-verified in `_aux/Universe_Split/` (delegation output not taken on trust).

## Discrepancies surfaced
1. **S0 injection claim inaccurate.** `_aux/S0_Setup_Report.md` states `9_Universe_inject.sql` has "executable statements (73 lines)" and that `validate.py --phase injection` returned PASS. The current file is comment-only (73 lines all `--`, ends at "PASTE YOUR SQL STATEMENTS BELOW", zero SQL); `4_Changelog.json` is `[]`. A comment-only header SKIPS the injection gate. Downstream phases must treat this task as having **no separately-documented injection**; the Las Palmas 8D scenario is baked into `3_UniverseDataForThisTask.json` instead. Not a HARDNESS blocker (base data suffices), but flagged for S0-report accuracy.
2. **S0 verification doc malformed.** `phase_ready.py --phase hardness` reported `_aux/Verification_s0.md` is missing its Sources-consulted and Verdict sections. The 3 upstream artifacts (Universe_Split, Universe_Index, Fact_Ledger) are all present and usable, so HARDNESS proceeded, but the S0 verification doc is non-conforming and should be repaired.
3. **Tool catalog not fully read.** The sub-agent could not finish reading `StarPM_Base_Universe/7_Server_Tools_Details.json` (harness abort). Write-tool signatures used in the plan come from the StarPM registry constants, not the catalog file. S1 MUST re-confirm exact signatures (Slack `message`, Gmail draft-only `body` + no send tool, Linear `team`/`save_comment(issueId, body)`, Airtable camelCase `baseId`/`tableId`/`records[]`) against that file before drafting write steps.

## Verdict
**PASS.** 5/5 levers, per-model density 48.5 (StarPM V4 >= 40 PASS), breadth PASS. Proceed to S1 on base data. No STOP gate fired.
