# Verification — PIPELINE AUDIT `--phase all` (on-demand, strictest interpretation)

Task: `39_6a602c8886ebb06f12354d77` · Universe: **starpm (V4)** · Universe today: **2026-07-01 America/Chicago**
Audit date: 2026-07-23 · Mode: on-demand full-strict re-audit (prompt + OE + rubrics)
Report: `_aux/Council_Reports/AUDIT_all.md` (242 lines). Siblings `AUDIT_prompt/oe/rubrics.md` preserved untouched.

## Strictest interpretation re-applied
- Every "should" in the QC spec / evals read as "must".
- Every NON-FAIL middle band collapsed to REVISE.
- **Density = V4 per-model scheme (NOT the V3 50/40 default):** design target avg 40+ tool calls, absolute floor 15, applied to Opus and Gemini SEPARATELY (>=40 PASS, 15-39 THIN, <15 INSUFFICIENT). pass@1 <=40% = difficulty PASS.
- Every soft convention in the format cards treated as binding; every validator WARN/NOTE listed.

## Data sources consulted (re-verified from source — NOT trusting prior phase outputs)
- `_aux/Universe_Split/airtable.airtable_records.json` (170 rows) :: all 5 OE/rubric record ids re-grounded via fixed-string on the stringified `row_data` field — receb057b02f20052 (selReady / fldTargetReady 2026-05-01 / "cleared for leasing"), recf7aecc318b2252 (selProg, James in-house), rec651427ec0d84dd5a (selProg, 6/25 fridge, critical path), recac236210094352 (MT-2026-1271, fldCompletionDate blank = OPEN), recb403fe04c2f97683 (MT-2026-1325 = Rio Bend 214 dishwasher, 2026-06-25 — genuine different-unit decoy).
- `_aux/Universe_Split/slack.slack_messages.json` :: C001 (#maintenance) 2026-06-22 James "disposal seized / full replacement / waiting on parts approval from John / still open"; C004 (#make-ready) May "carpet done / punch-list done / officially cleared and ready" stale chatter.
- `_aux/Universe_Split/linear.linear_issues.json` + `linear.linear_comments.json` :: OPS-227 (garbage disposal, team_001, assigned James Bennett); exactly ONE comment 2026-06-22 (seized / full replacement / routed for parts approval), no reply → approval never came.
- `_aux/Universe_Split/linear.linear_teams.json` :: team_001 charter names Airtable Maintenance Tickets the system of record, Linear secondary.
- `_aux/Universe_Split/contacts.contacts.json` :: john.smith@starpm.com = Lead Maintenance Technician.
- `_aux/Fact_Ledger.json` :: atom surface cross-checked (note: `lifecycle.today` is null — see Discrepancy 3).
- `_aux/Universe_Index/today_horizon.json` :: universe_today 2026-07-01 America/Chicago.
- Empirical trajectories: `Agent_Responses/{Opus,Gemini}/*` counted first-hand; `_aux/Trajectory_Stats.json` (recorded, corrupt for Gemini — see Discrepancy 1); `_aux/Council_Reports/S4_verdict.md` + `S4_bucket3.md`; `8a_/8b_` verifier fails.
- Tool catalog `StarPM_Base_Universe/7_Server_Tools_Details.json` :: param traps confirmed against OEs — slack_send_message `message` (not payload); create_draft `body`, draft-only (no send); save_comment `issueId`+`body`; save_issue/list_issues `team` (not teamId); search_records `table` vs list_records_for_table `tableId`.

## Eval spec verified for this phase (universe-correct set: starpm → `Evals_starpm/`)
- `Evals_starpm/1_Prompt_Eval.md`, `2_OE_Eval.md`, `3_Rubrics_Eval.md` :: strictest reading applied across all three artifacts.
- V4 extras: `validate.py --phase injection` (Evals_starpm/0) = PASS 0/0; `validate.py --phase submission_gate` (Evals_starpm/5, defect families F1-F6) = PASS 0/0. No phantom-tool / F1-F6 hits in OEs or rubrics.

## QC spec re-verified (universe-correct doc set: starpm → `Docs_starpm/`)
- `Docs_starpm/7_QC_Spec_Doc1.json` :: all 5 dims / 24 sub-dims rescored under strict interpretation → **24/24 = 5/5**. The stale "Jun 12 US/Eastern" string inside the JSON is superseded by `Docs_starpm/6_Prompt_Relative_Time_Updates.md` + evals (authoritative today 2026-07-01) — no scoring impact.
- `Docs_starpm/8_QC_Spec_Doc2.md` :: appendix issue taxonomy re-applied; no hits.
- Caveat honored: `Docs_starpm/13_QC_Companion.md` is Brookfield-contaminated — NOT used as StarPM SSOT.

## All 9 lenses status
- Lens 1 strict QC scoring :: **PASS** — 24/24 sub-dims 5/5; per-atom evidence table produced for every Truthfulness/Accuracy 5/5 (no empty evidence cells).
- Lens 2 answer-leakage sweep :: **PASS** — regex sweep 0 hits; the 6/22 C001 partial-signal (3/4 conclusion elements) hard-excluded (no sole-blocker element; must be trusted over 3+ louder "ready" signals; buried under decoy; 0/6 empirical).
- Lens 3 hardness end-to-end :: **PASS** — 5 levers each trace prompt sentence → OE step → rubric criterion → Fact_Ledger atom; no HARDNESS_REGRESSION.
- Lens 4 strict density :: **Opus PASS (43.5) / Gemini THIN-of-40-target (33.0)** — both ≫ 15 floor; pass@1 0/6 both = difficulty PASS; net SHIPPABLE, NOT a deliverable REVISE.
- Lens 5 adversarial review :: **PASS** — implicit-prompt framing preserved across all 3 artifacts; R2-R4 record-pin (receb057b02f20052) is the unique selReady row (not over-fit); C004/john.smith are prompt-sourced (not lock-in); zero process rubrics; no tool-name/em-dash/at-least-N/approximate-near-id leaks; Gmail draft-only honored; near-dup PDF decoy + Unit-14 ambiguity not load-bearing here.
- Lens 6 :: **RETIRED (v18)** — folded into Lens 1 per-atom evidence table.
- Lens 7 anti-rationalization :: **PASS** — 4 candidates (R6 AND-bundle, R14 OR-branch, density lean-floor, receb057 record-pin) promoted then hard-excluded with cited exclusions; no un-scrutinized "it's fine because" lines remain.
- Lens 8 regression-anchor + tooling integrity :: **62/62 PASS** + one **LOW** tooling-integrity finding (parse_trajectories.py Gemini-schema blindspot — surfaced, not silent).
- Lens 9 :: **RETIRED (v18)** — folded into Lens 1 + Lens 5.

## Verification statements
- [x] Validator re-run during audit — `validate.py --phase all` PASS (prompt 0/0, oe 0/0, rubrics 0/0) + `--phase injection` PASS + `--phase submission_gate` PASS. Exit 0.
- [x] Regression-anchor suite executed — `test_regression_anchors.py` → **62/62 PASS**.
- [x] Anti-rationalization output check passed — every candidate finding either promoted to a listed discrepancy or hard-excluded with a cited exclusion; no rationalized-away lines.
- [x] Verdict recorded with explicit per-issue trail (AUDIT_all.md "Final verdict — per-issue trail").
- [x] Similarity re-run — `calc_similarity.py` max composite 26.7 (vs QC Task13); clear of the 40 ceiling.
- [x] Justification hygiene — `check_justification.py` on Linter_Justifications.md → 0 hits.

## Discrepancies surfaced (all NON-deliverable, none ship-gating)
1. **[REVISE — pipeline tooling]** `Validators/parse_trajectories.py:130-149` `count_tool_calls()` skips any event without a `message` wrapper (L138-140), so Gemini's flat top-level `{"type":"tool_use",...}` events all count 0. Confirmed first-hand. Fix: add a top-level `type=="tool_use"` branch + broaden the MCP prefix (`mcp__` and `mcp_mcp`) + read `tool_name`, then regenerate `Trajectory_Stats.json`. Shared regression-pinned tooling → out of this task's deliverable scope; NOT ship-gating (true numbers clear floor + difficulty). Already noted in `S4_verdict.md`.
2. **[LOW — hygiene]** `_aux/Trajectory_Stats.json` corrupt for Gemini (records `tool_calls_total: 0` ×6, `by_model.gemini.avg_tool_calls_total: 0`). Consequence of #1. Regenerate after the parser fix. Shipped `verdict: "OK"` remains correct on true numbers.
3. **[LOW — hygiene]** Validator stale-date fallback: `Fact_Ledger.json` `lifecycle.today` is null → validator resolves `today` against the stale 2026-06-12 constant. Authoritative today is 2026-07-01 (today_horizon + evals + Docs_starpm/6), under which the task is fully date-coherent (all events past). Fix: seed `Fact_Ledger.lifecycle.today = 2026-07-01` (rebuild `build_fact_ledger.py`).
4. **[NOTE — optional refinement]** R6 ("not ready AND should not be marketed/shown") — Gemini's sole 6/6 all-fail. Held VALID: clauses semantically fused (the stale C004 message it corrects said "start scheduling showings"), Opus meets both 6/6 → Bucket-3 model gap (Learnings L31), not a rubric defect. Optional split R6a/R6b for cleaner per-clause attribution; a nice-to-have, not a correctness fix.

## Verdict
**PASS (STRICT)** on the deliverables (`5_Prompt.txt` / `6_Oracle_Events.txt` / `7_Rubrics.json`) — zero BLOCKER, zero Lens-1 sub-dim < 5, every lever traces end-to-end, density clears floor + difficulty on both models on true numbers. One independent **REVISE-the-tooling** (parser bug) that does not change the ship decision. **Task is SHIPPABLE on true numbers.**
