# Verifier Fails — S4 verdict

Task `2_6a6beba55996ad2ada369b15` · universe **harmonygames** · model under test **Claude Opus 4.7** (single-model).
Pass 1. Export pinned at entry and re-verified at exit: `8_Verifier_Fails.txt` `d28c7c4ac71a9abd…` 53,558 B, per-run [16, 20, 22, 18, 16, 17]; `7_Rubrics.json` `69713012b52f17d6…` 11,941 B.

Inputs arrived mis-named and were normalised before anything was read: `8_Verifier_fails.txt` to `8_Verifier_Fails.txt`, and `trajectory-run-N (2).json` to `trajectory-run-N.json` for all six runs.

---

## Trajectory T3 — Error Rate

Erroneous runs: 0/6. Verdict: **PASS** (< 3).

All six trajectories parse and reach a verifier-evaluable end state. Three runs hit recoverable query errors mid-walk (runs 3, 4 and 6 each issued `GROUP BY game` against a table whose column is `game_id` and got a DuckDB binder error) and all three recovered on the next call.

## Trajectory T2 — Agent Failure Rate

Runs passing all rubrics: 0/6. pass@1: **0.0%**. Verdict: **PASS** (<= 40%).

**Corrected pass@1, excluding the six criteria classified Rubric Invalid: 1/6 = 16.7%.** Run 3's only failures were criteria 4, 6, 10, 11, 17 and 20, every one of them a defect, so run 3 becomes a clean sweep once they are fixed. Runs 1, 2, 4, 5 and 6 still fail on criteria 5, 7, 12, 16, 21, 24, 25 or 27 after the exclusion. The difficulty of this task does not depend on its defective criteria, and it clears the 40% gate with 23 points of margin on the corrected number.

## Trajectory T1 — Density

Avg total tool calls **61.5**, avg MCP tool calls **49.3**, per-run totals 63 / 58 / 60 / 69 / 60 / 59. Verdict: **PASS** against the 40+ HarmonyGames target and the 15 QC floor.

Realisation ran over projection: `Hardness_Plan.md` projected a 47.0 midpoint and the runs measured 61.5, a ratio of about 1.31. Consistent with the HarmonyGames pattern of density running over projection rather than under it.

---

## Run matrix

P = pass, F = fail. Keyed by criterion title, not by export position.

| # | R1 | R2 | R3 | R4 | R5 | R6 | Fails | Criterion (abbreviated) |
|---|---|---|---|---|---|---|---|---|
| 1 | P | P | P | P | P | P | 0 | creates a standalone written page or document |
| 2 | P | P | P | P | P | P | 0 | measurement window 2026-01-05 to 2026-02-09 |
| 3 | P | P | P | P | P | P | 0 | 0.00 lifetime revenue |
| 4 | F | F | F | F | F | F | **6** | acquisition spend 7,483.42 across 01-05 to 02-28 |
| 5 | F | F | P | F | F | F | 5 | peak DAU 801 across both platforms |
| 6 | F | F | F | F | F | F | **6** | 8,452.64 over the 19 days from 02-10, written account |
| 7 | F | F | P | F | F | F | 5 | Leonard Hayes controls the ad accounts |
| 8 | P | P | P | P | P | P | 0 | net proceeds 10,800 |
| 9 | P | P | P | P | P | P | 0 | cash on hand 2,500 |
| 10 | F | P | F | F | F | F | 5 | managed wind-down service cost ~15,000 / 13,000-15,000 |
| 11 | F | P | F | F | F | F | 5 | service cost alone exceeds net proceeds |
| 12 | F | P | P | P | F | F | 3 | written account concludes funds fall short |
| 13 | P | P | P | P | P | P | 0 | posts a message in #winddown |
| 14 | P | P | P | P | P | P | 0 | message addresses Leonard and Arthur |
| 15 | P | P | P | P | P | P | 0 | message points to the written account |
| 16 | F | P | P | P | F | F | 3 | message states funds fall short |
| 17 | F | F | F | F | F | F | **6** | 8,452.64 in the #winddown message |
| 18 | P | P | P | P | P | P | 0 | files a tracking item |
| 19 | P | P | P | P | P | P | 0 | tracking item subject is the still-running spend |
| 20 | F | F | F | F | F | F | **6** | 8,452.64 in the tracking item |
| 21 | F | F | P | F | F | P | 4 | tracking item names Leonard Hayes as owner |
| 22 | P | P | P | P | P | P | 0 | two or three lead figures in the final response |
| 23 | P | P | P | P | P | P | 0 | lead figures drawn from the records |
| 24 | F | P | P | P | F | F | 3 | final response reports funds fall short |
| 25 | P | F | P | P | P | P | 1 | funds available at 13,300 |
| 26 | P | P | P | P | P | P | 0 | continuing paid UA is the uncovered cost |
| 27 | P | P | P | F | P | P | 1 | licensing form rather than outright sale |
| 28 | P | P | P | P | P | P | 0 | Process: account created before the channel post |

Per-run totals reconcile to the export exactly: 16, 20, 22, 18, 16, 17 of 28. Failing criteria: **14**. All-failing (0/6): **4** — criteria 4, 6, 17, 20.

## Step 1b — passing-cell audit

`check_criterion_dependencies.py` exits 0. It inferred 13 dependency edges (criteria 2-11 and 26 on criterion 1's "written account"; 16 and 17 on criterion 13's "#winddown message") and found no cell where a dependent passed in a run whose antecedent failed. Criteria 1 and 13 passed 6/6, so the class cannot arise here.

The manual passing-cell audit the fail-driven walk would otherwise miss found one structurally wrong PASS that the checker cannot see, because it is a value collision rather than a dependency: **criterion 10, run 2**. That cell passed on the February `legal = 13000` row of `FINANCE.EXPENSES.MONTHLY_BURN`, not on the priced managed wind-down the criterion is about. Three other runs wrote the same figure from the same table and failed. Detail and fix in `S4_fixes.md` section B.

---

## Classifications

| Bucket | Count | Criteria | File |
|---|---|---|---|
| 1 — Rubric Invalid | **6** | 4, 6, 17, 20 (Tool Precision Mismatch) · 10, 11 (value collision / subject binding) | `S4_fixes.md` |
| 2 — Judge Error | **0** | none | `S4_judge_errors.md` |
| 3 — Legitimate Fail | **8** | 5, 7, 12, 16, 21, 24, 25, 27 | none all-failing, so no AF justifications |

### Bucket 1 detail

**Tool Precision Mismatch (criteria 4, 6, 17, 20 — all 6/6).** The hydrated warehouse stores `AD_SPEND_DAILY.spend_usd` as whole dollars, rounded half-up. `snowflake_execute_query` returns 7,476 where the universe holds 7,483.42, and 8,447 where it holds 8,452.64. Proven three ways: row-level (universe 53.57 returned as `"54"`, Run 1 call 50), aggregate-level (every figure any run reported equals the sum of half-up-rounded rows and never the exact sum), and by the `avg_session_minutes` control, whose exact column average is 12.674 and whose integer-rounded average is 12.736 while Run 6 call 39 returned **12.74**. This triggers the `Evals_harmonygames/4_Verifier_Fails_Eval.md` Tool Precision Mismatch hard gate: the criteria are invalid for this environment and cannot be scored as legitimate fails.

**Value collision (criteria 10, 11 — 5/6).** The accepted band "approximately 13,000 to 15,000" collides with the `FINANCE.EXPENSES.MONTHLY_BURN` February `legal = 13000` row, which every run queried. Four cells turned on wording rather than on the fact. The intended figure, the ~15,000 Sunset quote at `C07C2866011` ts `1770850852.708789` and the 13,000-15,000 range in the Feb 11 wind-down meeting notes, appears in **zero** of the six trajectories despite both surfaces being inside the persona's read scope. Difficulty is real; the acceptance band is not gradeable.

### Bucket 3 detail — what the model genuinely got wrong

- **Criterion 5, peak DAU 801 (5/6).** Requires summing ios and android per date before taking the max. Runs 2, 4 and 5 took `MAX(dau)` on raw rows and got the per-platform max 426. Run 1 hand-picked three dates for a combined query and omitted 2026-02-07, landing on 784. Run 3 ran the correct windowed query and passed. Run 6 ran the correct query too, got `["2026-02-07", "801"]` at call 81, and then wrote "Peak ~800" on the page.
- **Criterion 7 (5/6) and 21 (4/6), Leonard Hayes as ad-account owner.** The grounding sits in `C07C2866011` January 2026 ("keep our cpi low", "Can I pause the campaigns", "ok, campaigns are paused", "ironsource properly"). **No run retrieved any of it.** Runs 1, 4 and 5 named Arthur Blake, who appears in those threads only as an integration helper. Runs 3 and 6 named Leonard by inference from the Meta app setup rather than from the grounding. The decoy owner worked exactly as designed.
- **Criteria 12, 16 and 24, the coverage conclusion (3/6 each, perfectly correlated).** Runs 2, 3 and 4 each state an unconditional negative somewhere ("marginal, not comfortable", "Real net position is roughly negative $6-7K", "It does not fund the reserves counsel flagged"). Runs 1, 5 and 6 state only conditionals ("closes roughly cash-neutral if and only if", "covers everything only if", "ONLY IF"). The grader was internally consistent per run across all three surfaces, which is evidence the criterion discriminates rather than coin-flips.
- **Criterion 25, funds available 13,300 (1/6).** Run 2 stated 10,800 and 2,500 separately and never summed them. This is the multi-link chain doing its job.
- **Criterion 27, licensing rather than sale (1/6).** Run 4's page said "Data-licensing deal" but its final response said "the data sale". Correctly graded against the criterion's two-surface scope.

## All-Failing Rubrics sub-dim

Bucket 1 ratio = 6 / 14 failing criteria = **42.9%**, which falls in the 25-50% band.

**Score: 3/5 (NON-FAIL).** A meaningful fraction of the failures trace to rubric issues rather than to task difficulty. The four all-failing criteria are all Tool Precision Mismatch, and criteria 10 and 11 rest on an ungradeable acceptance band.

**Sharper reading, recorded because it is the one that matters for the fix.** Restricted to criteria that failed every run, the ratio is **4/4 = 100%**, which on the same table would score 1/5. Every criterion that failed all six runs is a defect, and none is desired difficulty. This is why zero AF justifications were written and why `AGENTS.md` rule 21 resolves to fix rather than justify for all four. The 3/5 above is the score the stated denominator produces; the 4/4 is the finding.

---

## Hardness calibration

Stump hypothesis hit rate: **0 of 2 [HIGH], 1 of 2 [MED] partial.**

| # | Predicted | Outcome |
|---|---|---|
| 1 | [HIGH] Net-vs-gross latch: agent reports 22,500 instead of the 10,800 net | **Over-predicted.** Criterion 8 passed 6/6. Every run derived 22,500 minus 11,700 without prompting. The single-hop reduction was not a lever at all. |
| 2 | [HIGH] Snowflake `FINANCE` never queried | **Over-predicted.** Criterion 9 passed 6/6. Every run reached `FINANCE.EXPENSES.CASH_BALANCE` and read 2,500. The structured-source skip did not fire once. |
| 3 | [MED] Deal-structure supersession, sale vs licence | **Partial hit.** Criterion 27 failed 1/6, and only in the final response while the written account was correct. |
| 4 | [MED] Vendor disposition at an intermediate state | Not gradeable; no criterion carries it. |

**Under-predicted, and this is where all the difficulty actually came from.** None of the four levers that produced the failures is named in `Hardness_Plan.md`:

1. **Aggregate-shape trap on peak DAU.** Per-platform rows require a sum-then-max; a naive `MAX(dau)` returns 426. Cost 5 of 6 runs. The strongest single lever in the task and it was discovered by the rubric writer, not the lever planner.
2. **Scope widening on the continuing spend.** The prompt asks what is "still taking money from us"; four of six runs answered for Combo Fighter alone (2,441) rather than across all three titles (8,447). A single-title default beat a studio-wide question.
3. **Decoy owner on the ad accounts.** Arthur Blake reads as the operations owner from the wind-down channel; Leonard Hayes is the actual account holder and the grounding for that sits in a January channel nobody paged into. Cost 5 of 6 on criterion 7.
4. **Hedged coverage conclusion.** Three runs would not commit to a shortfall and wrote conditional break-even instead. The arithmetic levers the plan selected were solved; the judgement call was not.

The plan's `Hardness Score: 5/5` was carried on two [HIGH] hypotheses that both whiffed. The task is genuinely hard, at a corrected 16.7% pass@1, but for reasons the plan did not name. Recorded to `Tasks/_meta/Stump_Hypotheses.md` and `Tasks/_meta/Hardness_Patterns_Log.md`.

The plan's risk register did name the `MONTHLY_BURN` February `legal = 13000` row, but only as a burn-reconciliation coherence risk. It did not notice that the same value collides with the wind-down service cost band a rubric would later accept. Near-miss registers need to be checked against the acceptance bands of the criteria that get written downstream, not only against the figures.

---

## Action items

1. ~~Apply the six Bucket 1 fixes and the paired Oracle Event edits.~~ **DONE 2026-08-07**, on operator instruction. Both files edited in step, pre-fix copies archived in `_aux/`. Two drafted clauses were reworded to clear `check_rubric_antipatterns.py` and `validate.py`; see `S4_fixes.md` STATUS block.
2. ~~Re-run the gates.~~ **DONE.** `check_oe_rubric_sync` OK · `check_rubric_antipatterns` OK · `check_criterion_dependencies` OK · `validate.py --phase rubrics` and `--phase oe` both 0 fails, 0 warns · `check_export_freshness` re-pinned and OK.
3. **Re-run the platform verifier.** Still open, and it is the only remaining step. Four criteria changed value and two changed their acceptance clause, so **every per-run count and matrix cell in this report describes the pre-fix rubric** and is superseded by the next export. Do not reconcile the new export against this one by hand.
4. **No AF justifications to submit.** All four all-failing criteria were defects and are fixed.
5. **No judge-error appeals to file.**
6. Expect criterion 10 to come back 6/6 failing under the rewrite, because run 2's PASS rested on the collision the fix now excludes. Its removal case is argued and rejected in `S4_fixes.md` section D; it stays.

## Pin history

| Stage | `7_Rubrics.json` | `8_Verifier_Fails.txt` |
|---|---|---|
| Classification (this report's matrix) | `69713012b52f17d6…` 11,941 B — archived at `_aux/S4_input_pin.classification.json` | `d28c7c4ac71a9abd…` 53,558 B |
| After fixes applied | `bf26e5373d7fbab6…` 13,703 B — current pin | `d28c7c4ac71a9abd…` 53,558 B, unchanged |

The verifier export never moved, so no per-run count in this report was invalidated. The rubric drift is the approved fix landing after the loop closed, not a mid-pass re-paste.
