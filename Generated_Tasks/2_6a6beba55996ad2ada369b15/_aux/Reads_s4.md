# Reads — PIPELINE S4 (2_6a6beba55996ad2ada369b15)

Universe: **harmonygames** (`_aux/Universe.txt`). Model under test: Claude Opus 4.7 (single-model, no dual-model split).

## Runbook and project rules
- `Reference/Sessions/S4.md` :: phase order — pin exports FIRST, passing-cell audit at step 1b, trajectory walk mandatory for EVERY failing rubric before classification, Bucket 1 ratio scoring, STOP gate at the end.
- `AGENTS.md` rule 15 :: pin platform-pasted inputs by content hash before reasoning; re-verify before declaring complete. Pinned at entry, re-checked at exit.
- `AGENTS.md` rule 16 :: a title that reliably induces the same judge misreading on 3+ cells is a rubric defect (Bucket 1b), not a judge error. Applied to criterion 10.
- `AGENTS.md` rule 17 :: fail-driven walk is blind to a criterion that passes for the wrong reason; audit the passing cells. `check_criterion_dependencies.py` exit 0, but the manual passing-cell audit found criterion 10's single PASS resting on the wrong figure.
- `AGENTS.md` rule 21 :: for a criterion failing all completed runs the default is removal, not justification. Applied to all four all-failing criteria; none survived as legitimate, so zero AF justifications were written.
- `AGENTS.md` rule 2 :: HarmonyGames source of truth is `HarmonyGames_Base_Universe/Services_Data/` overlaid by `4_Changelog.json`, not the 940-byte per-task descriptor. `4_Changelog.json` is `[]` and `9_Universe_inject.sql` touches no marketing table, so base = graded for every figure checked here.

## Eval specs
- `Evals_harmonygames/4_Verifier_Fails_Eval.md` :: five verdicts for this universe — Rubric Invalid, **Tool Precision Mismatch**, Judge Error, Legitimate Fail, Excluded. The "Tool Precision Mismatch" HARD GATE (lines 250-266) is the controlling rule for criteria 4, 6, 17 and 20: *"Tool systematically exposes only a rounded/truncated value while the criterion requires inaccessible precision -> Tool Precision Mismatch; the criterion is invalid for that environment."* Its "mixed finding" clause (line 265) covers runs 1-4 on criteria 6/17/20, where the scope miss is genuine but the exact-value criterion is still invalid.
- `Evals_harmonygames/4_Verifier_Fails_Eval.md` Phase 3.3 :: cross-run comparison — if the failing run did the same thing a passing run did, the fail is judge inconsistency. Applied to criterion 10 (runs 1/3/6 wrote materially what run 2 wrote).
- `Docs_harmonygames/9_Common_Error.md:29` :: All-failing rubric handling scores 4/12 when "the all-fail criterion was itself defective". All four all-failing criteria here are defective, which is why they are fixed rather than justified.

## Universe ground truth re-confirmed for this pass
- `HarmonyGames_Base_Universe/Services_Data/snowflake/snowflake.tables.json` :: `ANALYTICS.MARKETING.AD_SPEND_DAILY`, 4,643 rows. combo_fighter = 330 rows, 2026-01-05 to 2026-02-28, `spend_usd` sums to exactly **7,483.42**; within-engagement-window subtotal **5,039.34**. All-titles 2026-02-10 to 2026-02-28 = 280 rows summing to exactly **8,452.64** (domino_delights 5,569.66, combo_fighter 2,444.08, zombie_match_3d 438.90). Every OE 8 / OE 10 figure verified to the cent.
- Same file :: `ANALYTICS.GAME_EVENTS.DAILY_ACTIVE_USERS`, combo_fighter 72 rows over 36 dates. Combined ios+android peak = **801 on 2026-02-07**, then 784 (02-08), 783 (02-09), 768, 765. OE 4 verified.
- Same file :: `FINANCE.EXPENSES.MONTHLY_BURN` 2026-02-01 rows carry `legal = 13000`. This is the collision behind the criterion 10 defect and is **not** the priced managed wind-down.
- `HarmonyGames_Base_Universe/Services_Data/slack/messages/C07C2866011/2026-02.json` :: ts `1770850852.708789`, "the cost of Sunset is about ~$15K - the data will likely cover our costs without us liquifying the laptops/assets". OE 19 grounding confirmed present and inside the persona's read scope.
- `HarmonyGames_Base_Universe/Services_Data/gmail/threads/EMPLOYEE_0016_EMAIL_1856871678357556733.json` :: subject `Notes: "Harmony Games Wind Down" Feb 11, 2026`, body carries "an estimated cost of $13,000 to $15,000". Second grounded reading confirmed.
- `HarmonyGames_Base_Universe/Services_Data/slack/messages/C07C2866011/2026-01.json` :: OE 12 ad-account ownership grounding confirmed present ("keep our cpi low", "pause the campaigns", "ironsource properly", "turn it off today"). No run retrieved any of it.

## Task artifacts
- `5_Prompt.txt` :: four asks — full-life performance record, what is still taking money with a figure and an owner, whether proceeds cover an orderly shutdown, then write / post / file / report.
- `6_Oracle_Events.txt` :: 28 OEs. OE 24 / 25 / 26 / 27 enumerate the graded elements per deliverable; OE 28 maps every decoy to the figure it would corrupt.
- `7_Rubrics.json` :: 28 criteria, 27 Outcome + 1 Process.
- `8_Verifier_Fails.txt` :: 6 runs, per-run 16/20/22/18/16/17 of 28.
- `_aux/Hardness_Plan.md` :: 5 selected levers, 4 stump hypotheses, density midpoint 47.0. Risk register item 2 names the `MONTHLY_BURN` legal 13,000 row but only as a burn-reconciliation risk, not as a collision with the wind-down service cost band.
- `_aux/Trajectory_Stats.json` :: measured avg 61.5 total / 49.3 MCP tool calls, pass@1 0.0.

---

# Pass 2 — 2026-08-07 (re-grade of the fixed rubric set)

Same universe, same model, same six trajectories. `8_Verifier_Fails.txt` moved to `ad0260ca6682ad47…` 55,564 B, per-run [17, 19, 21, 20, 19, 22]. Everything below was re-read or re-verified in this pass rather than carried forward from pass 1.

## Runbook and project rules, re-read at the point each one bound a decision
- `Reference/Sessions/S4.md` :: pin first, passing-cell audit at 1b, trajectory walk before every classification, Bucket 1 ratio scoring, STOP gate.
- `AGENTS.md` rule 15 :: the drift warning fired on entry. Re-derived from scratch; archived pass-1 reports rather than editing them. Its corollary on grading noise is what governs the reading of the cells that moved without a rubric change.
- `AGENTS.md` rule 16 :: tested against criterion 5's two "~800" cells. Two cells, one model, grader internally consistent, so below the reclassification threshold. Left in Bucket 3.
- `AGENTS.md` rule 17 :: `check_criterion_dependencies.py` exits 0, and the manual audit still found criterion 7 run 6 passing on a quote from the wrong artifact. The checker cannot see an artifact-scope leak because the antecedent passes.
- `AGENTS.md` rule 21 :: removal argued at its strongest for criteria 10 and 11 before any prose. Both survive; both carry AF justifications, which is the first AF batch this task has produced.
- `AGENTS.md` rule 2 :: `4_Changelog.json` is `[]`, `9_Universe_inject.sql` touches no surface used here, so `HarmonyGames_Base_Universe/Services_Data/` is the graded ground truth for every figure re-checked.

## Eval specs
- `Evals_harmonygames/4_Verifier_Fails_Eval.md` :: the Tool Precision Mismatch hard gate was the controlling rule in pass 1 and was re-tested against criterion 5 in this pass. It does not reach it. The tool returns the literal `"801"`, and two runs received it, so the criterion asks for a value the environment serves.
- Same file, Phase 3.3 cross-run comparison :: applied to criteria 12/16/24 and to criterion 5. In both families like text was graded alike, so neither is judge inconsistency.
- `Docs_harmonygames/9_Common_Error.md` and `11_Taxonomy.md` :: read before assigning any severity or writing any justification.
- `Reference/Linter_Playbook.md` :: AF justification voice, two to five sentences, first person, concrete record, no em-dashes.

## Universe ground truth re-confirmed first-hand
- `slack/messages/C07C2866011/2026-02.json` ts `1770850852.708789` :: "the cost of Sunset is about ~$15K…". Sunset established as the wind-down firm four messages earlier at ts `1770839105.706739`.
- `gmail/threads/EMPLOYEE_0016_EMAIL_1856871678357556733.json` :: "an estimated cost of $13,000 to $15,000", `user_email` `robert@harmonygames.co`. The phrase wraps across a line, so a grep for the whole string misses it. Recorded so a later pass does not conclude the grounding is absent.
- `FINANCE.EXPENSES.MONTHLY_BURN` February `legal = 13000` :: still the collision, now correctly excluded on all six cells.
- OE 12 grounding for the ad-account owner, in `#executives` January 2026 :: present and reachable, retrieved by nobody.

## Trajectory reads
- All six `trajectory-runs/trajectory-run-N.json` walked in full. Tool-call numbering in this pass counts the Nth `tool_use` block in order; pass 1 numbered differently and the two are not comparable.
- Retrieval reachability tested rather than assumed: which runs saw the provider's name, which opened `#executives`, which called `gmail_get_thread` and on what. Results in `_aux/Verification_s4.md`.
