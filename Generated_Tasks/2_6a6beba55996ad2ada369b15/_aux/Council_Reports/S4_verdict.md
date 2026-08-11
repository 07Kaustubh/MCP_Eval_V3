# Verifier Fails — S4 verdict

Task `2_6a6beba55996ad2ada369b15` · universe **harmonygames** · model under test **Claude Opus 4.8** (single-model).

**Pass 2.** Export pinned at entry and re-verified at exit: `8_Verifier_Fails.txt` `ad0260ca6682ad47…` 55,564 B, per-run [17, 19, 21, 20, 19, 22]; `7_Rubrics.json` `bf26e5373d7fbab6…` 13,703 B.

This export supersedes the one pass 1 reasoned about. `phase_ready.py` flagged the drift on entry, naming the movement `[16, 20, 22, 18, 16, 17]` to `[17, 19, 21, 20, 19, 22]`. Every count, cell and bucket call below was re-derived from the export in hand; nothing was reconciled against pass 1 by hand. The pass-1 reports are archived unaltered at `_aux/Council_Reports/_superseded/pass1_2026-08-07/`.

**What moved and why.** The trajectories did not change. `trajectory-runs/trajectory-run-{1..6}.json` are byte-identical to the set pass 1 walked, and `parse_trajectories.py` re-derives the same 63 / 58 / 60 / 69 / 60 / 59 tool-call totals. Two different things account for the whole delta:

1. **The pass-1 rubric fixes landed.** Four criteria had their target figures re-anchored from the source cents to the whole dollars the warehouse actually serves, and two had an exclusion clause added. That is a deliberate change to what is being graded.
2. **Regrading noise on the rest.** Criteria the fixes never touched still moved: criterion 7's single PASS moved from run 3 to run 6, criterion 25 went 1/6 to 2/6, criterion 27 went 1/6 to 0/6. Byte-identical trajectories, different cells. This is the AGENTS.md rule 15 corollary in the open, and it is why no single-cell number in this report is treated as a stable quantity. Gate margins are the durable claim.

Tool-call numbers throughout count the Nth `tool_use` block in that run's trajectory, in order. Pass 1 used a different numbering and the two are not comparable.

---

## Trajectory T3 — Error Rate

Erroneous runs: **0/6**. Verdict: **PASS** (< 3).

All six parse and reach a verifier-evaluable end state. Runs 3, 4 and 6 each issued a `GROUP BY game` against a table whose column is `game_id`, took a DuckDB binder error, and recovered on the next call. Recoverable mid-walk errors, not failed runs.

## Trajectory T2 — Agent Failure Rate

Runs passing all rubrics: **0/6**. pass@1: **0.0%**. Verdict: **PASS** (≤ 40%).

**Corrected pass@1 is also 0.0%.** There are no Bucket 1 criteria in this export to exclude, so the raw and corrected numbers coincide for the first time on this task. Upholding the one judge-error appeal moves run 5 from 19/28 to 20/28 and still leaves it failing eight criteria, so pass@1 is unchanged under every reading. The best run in the export is run 6 at 22/28.

For contrast: pass 1's corrected pass@1 was 16.7%, computed by excluding six defective criteria from a set where run 3's only failures were those six. That inflation is gone. The task now fails every run on criteria that are all sound.

## Trajectory T1 — Density

Avg total tool calls **61.5**, avg MCP tool calls **49.3**, per-run totals 63 / 58 / 60 / 69 / 60 / 59. Verdict: **PASS** against the 40+ HarmonyGames target and the 15 QC floor. Realisation over the plan's 47.0 projected midpoint is about 1.31, consistent with the HarmonyGames pattern of density running over projection.

---

## Run matrix

P = pass, F = fail. Keyed by criterion title, not by export position, because the export orders criteria differently per run.

| # | R1 | R2 | R3 | R4 | R5 | R6 | Fails | Criterion (abbreviated) |
|---|---|---|---|---|---|---|---|---|
| 1 | P | P | P | P | P | P | 0 | creates a standalone written page or document |
| 2 | P | P | P | P | P | P | 0 | measurement window 2026-01-05 to 2026-02-09 |
| 3 | P | P | P | P | P | P | 0 | 0.00 lifetime revenue |
| 4 | P | P | P | P | P | P | 0 | acquisition spend ~7,476 across 01-05 to 02-28 |
| 5 | F | F | P | F | F | F | 5 | peak DAU 801 across both platforms |
| 6 | F | F | F | F | P | P | 4 | ~8,447 over the 19 days from 02-10, written account |
| 7 | F | F | F | F | F | P | 5 | Leonard Hayes controls the ad accounts |
| 8 | P | P | P | P | P | P | 0 | net proceeds 10,800 |
| 9 | P | P | P | P | P | P | 0 | cash on hand 2,500 |
| 10 | F | F | F | F | F | F | **6** | outside provider's wind-down price ~15,000 / 13,000-15,000 |
| 11 | F | F | F | F | F | F | **6** | provider's price alone exceeds the 10,800 net |
| 12 | F | P | P | P | F | F | 3 | written account concludes funds fall short |
| 13 | P | P | P | P | P | P | 0 | posts a message in #winddown |
| 14 | P | P | P | P | P | P | 0 | message addresses Leonard and Arthur |
| 15 | P | P | P | P | P | P | 0 | message points to the written account |
| 16 | F | P | P | P | F | F | 3 | message states funds fall short |
| 17 | F | F | F | F | F | P | 5 | ~8,447 in the #winddown message |
| 18 | P | P | P | P | P | P | 0 | files a tracking item |
| 19 | P | P | P | P | P | P | 0 | tracking item subject is the still-running spend |
| 20 | F | F | F | F | P | P | 4 | ~8,447 in the tracking item |
| 21 | F | F | P | F | F | P | 4 | tracking item names Leonard Hayes as owner |
| 22 | P | P | P | P | P | P | 0 | two or three lead figures in the final response |
| 23 | P | P | P | P | P | P | 0 | lead figures drawn from the records |
| 24 | F | P | P | P | F | F | 3 | final response reports funds fall short |
| 25 | P | F | F | P | P | P | 2 | funds available at 13,300 |
| 26 | P | P | P | P | P | P | 0 | continuing paid UA is the uncovered cost |
| 27 | P | P | P | P | P | P | 0 | licensing form rather than outright sale |
| 28 | P | P | P | P | P | P | 0 | Process: account created before the channel post |

**Reconciliation.** Column sums are 17, 19, 21, 20, 19, 22 of 28, matching the export's own per-run headers and the pin exactly. Failing criteria: **12**. All-failing (0/6): **2** — criteria 10 and 11. No cell is unevaluated.

---

## Step 1b — passing-cell audit

`check_criterion_dependencies.py` exits 0. It inferred 13 dependency edges (criteria 2 through 11 and 26 on criterion 1's "written account"; 16 and 17 on criterion 13's "#winddown message") and found no cell where a dependent passed in a run whose antecedent failed. Criteria 1 and 13 pass 6/6, so that class cannot arise here.

The manual audit found **one structurally impossible PASS the checker cannot see**, because it is an artifact-scope leak rather than a dependency edge.

**Criterion 7, run 6.** The grader passed it citing "runs the Meta/FB ad account — set up the Combo Fighter FB app". That string is in run 6's `linear_create_issue` at tool call 58, in the description of DES-2438. It is not in run 6's `gdocs_create_document` at tool call 56, which is the written account this criterion grades. That 7,104-character body names Leonard three times, none of them against the ad accounts: in its header, as joint owner of "GitHub, Deel, Gusto, Intuit, Linear", and as owner of Carta. Its paid-UA section attaches no owner at all.

Criterion 7 therefore fails 5/6 in the export and 6/6 on the trajectories. It is classified on the export's five failing cells, per rule 15. Full citation in `S4_judge_errors.md` finding 2; a cell-neutral surface-binding hardening and a pre-drafted AF justification are in `S4_fixes.md` section B, so it is ready if a later export grades that cell correctly and the criterion becomes all-failing.

The class generalises: criteria 7 and 21 grade the same fact on two different surfaces, and so do 12, 16 and 24. Any such family is exposed to this, and the dependency checker will never see it because the antecedent passes.

---

## Classifications

| Bucket | Count | Criteria | File |
|---|---|---|---|
| 1 — Rubric Invalid | **0** | none | `S4_fixes.md` |
| 2 — Judge Error | **1 criterion, 2 cells** | 17 (run 5, wrong FAIL, appeal) · 7 (run 6, wrong PASS, audit finding only) | `S4_judge_errors.md` |
| 3 — Legitimate Fail | **12** | 5, 6, 7, 10, 11, 12, 16, 17, 20, 21, 24, 25 | `S4_AF_justifications.md` for the two all-failing |

### Bucket 3 detail — what the model genuinely got wrong

- **Criteria 10 and 11, the outside provider's price and the comparison it feeds (6/6 each).** Re-verified after the verdict was first drafted, by an eight-test falsification pass recorded in `_aux/Verification_s4.md`. Both are legitimate model failures: the channel was listed to three runs and its bodies served to three, the private-channel history tool demonstrably works for this persona and reaches the 2026-02-11 window, no call was denied anywhere in the six runs, and `C07C2866011` appears in zero tool inputs across the whole corpus.** Every run had "Sunset" returned to it in a tool result from the wind-down channel, and two runs put the name in their own deliverables. None asked what it charges. The price is grounded twice inside the persona's reach, in `#executives` at ts `1770850852.708789` ("the cost of Sunset is about ~$15K") and in the Feb 11 wind-down meeting notes in Robert's own mailbox ("an estimated cost of $13,000 to $15,000"). **No run called `slack_conversations_history` on C07C2866011 once**, on any pass. Run 3 came within one call: its tool call 44 `gmail_search_messages` returned the meeting-notes thread id as its first result, and the run never fetched it. The runs wrote the February legal line of 13,000 from the burn table instead, which is a booked accounting cost rather than a forward price, and the pass-1 exclusion clause now correctly refuses it.
- **Criterion 5, peak DAU 801 (5/6).** The table is one row per date per platform, so the figure needs a sum-then-max. Runs 1, 2, 4 and 5 ran a bare `MAX(dau)` and got the per-platform 426. Runs 1, 2 and 5 then reported 784, the combined figure for the wrong day. Run 6 ran the correct query at tool call 33, received `["2026-02-07", "801"]`, and wrote "Peak ~800". Run 4 never computed it and eyeballed "~800" off a 72-row dump. Run 3 ran the windowed query and passed. The Overly Specific case for the two "~800" cells is argued in full and rejected in `S4_fixes.md` section A.
- **Criterion 7 (5/6 graded, 6/6 in substance) and criterion 21 (4/6), Leonard Hayes as ad-account owner.** The grounding is in `#executives` in January and no run retrieved it. Runs 1, 2 and 5 named Arthur Blake, who appears in those threads only as an integration helper asking to be added as a user. The decoy owner worked as designed. Runs 3 and 6 named Leonard in the tracking item, by inference from the Meta app rather than from the record.
- **Criteria 6, 17 and 20, the continuing spend scoped studio-wide (4/6, 5/6, 4/6).** The prompt asks what is "still taking money from us". Runs 1 through 4 answered for Combo Fighter alone and reported 2,441; runs 5 and 6 widened to all three titles and reported 8,447. A single-title default beat a studio-wide question on two thirds of the runs. This is the discrimination the pass-1 re-anchoring was meant to preserve, and it survived intact.
- **Criteria 12, 16 and 24, the coverage conclusion (3/6 each, perfectly correlated).** Runs 2, 3 and 4 commit to a shortfall somewhere ("marginal, not comfortable… There is no buffer"; "Real net position is roughly negative $6-7K"; "does NOT fund the tax/payroll/chargeback reserves counsel flagged"). Runs 1, 5 and 6 write conditional break-even instead ("closes roughly cash-neutral if and only if"; "break-even exit, not a distribution"; "covers an orderly shutdown ONLY IF"). The failing runs are substantively wrong rather than merely cautious: each nets Unity and Singular to zero on an insolvency waiver the record shows as requested and unanswered, which is the only route to cash-neutral. OE 22 is explicit that neither can be read down to nothing. The same six-run split reproduced across three criteria on two independent gradings of byte-identical trajectories, which is strong evidence the criteria discriminate.
- **Criterion 25, funds available 13,300 (2/6).** Runs 2 and 3 each state 10,800 and 2,500 and neither adds them. The multi-link chain doing its job.

---

## All-Failing Rubrics sub-dim

Bucket 1 ratio = **0 / 12 failing criteria = 0.0%**, below the 25% threshold.

**Score: 5/5 (PASS).** Every failure in this export is a legitimate model failure or, in one cell, a judge misreading. No criterion is invalid.

Restricted to criteria that failed every run the ratio is also **0/2 = 0%**. Pass 1's sharper reading was 4/4 = 100% on the same restriction, which is the finding that drove the six fixes. Both all-failing criteria here were argued for removal under rule 21 before a word of justification was written, and both survive on a defence that names a reachable grounding surface, a run that came within one tool call of it, and the specific reasoning gap.

---

## Hardness calibration

Stump hypothesis hit rate: **0 of 2 [HIGH], 1 of 2 [MED] partial** — and the [MED] partial has now decayed to zero on this export.

| # | Predicted | Outcome on this export |
|---|---|---|
| 1 | [HIGH] Net-vs-gross latch: agent reports 22,500 instead of the 10,800 net | **Over-predicted.** Criterion 8 passes 6/6. Every run derived 22,500 minus 11,700 unprompted. The single-hop reduction was not a lever. |
| 2 | [HIGH] Snowflake `FINANCE` never queried | **Over-predicted.** Criterion 9 passes 6/6. Every run reached `FINANCE.EXPENSES.CASH_BALANCE` and read 2,500. The structured-source skip never fired. |
| 3 | [MED] Deal-structure supersession, sale vs licence | **Over-predicted.** Criterion 27 now passes 6/6, having failed 1/6 on the previous grading of the same trajectories. Not a lever at all. |
| 4 | [MED] Vendor disposition at an intermediate state | Not gradeable; no criterion carries it. |

**Four of four selected stumps produced nothing. All the difficulty came from four levers the plan never named**, and this export sharpens the ranking pass 1 gave them:

1. **Unpriced-service discovery.** The one figure that exists only in unstructured records, in a channel nobody opens and a mail thread nobody fetches, while its name is handed to every run for free. Cost 6 of 6 twice over, on criteria 10 and 11. **The strongest lever in the task, and it is the only all-failing one.** The shape is worth naming: put the fact behind one extra retrieval hop, seed the entity's *name* in the cheap surface, and let a same-band decoy sit on the path everyone already walks.
2. **Aggregate-shape trap.** Per-platform rows requiring sum-then-max; a bare `MAX(dau)` returns 426. Cost 5 of 6.
3. **Scope widening.** "Still taking money from us" answered for one title instead of three. Cost 4 of 6 on the written account, 5 of 6 on the channel post, 4 of 6 on the tracker.
4. **Decoy owner plus hedged conclusion.** Arthur Blake reads as the operations owner; Leonard is the account holder and the grounding is in the same unopened January channel. Cost 5 of 6. And three runs would not commit to a shortfall, netting two open vendor balances to zero to avoid it. Cost 3 of 6 on each of three surfaces.

The plan scored itself 5/5 on two [HIGH] hypotheses that both whiffed. The task is genuinely hard, at 0.0% pass@1 with no defective criteria left in the set, but for reasons the plan did not name. The arithmetic levers it selected were all solved on the first attempt; the retrieval and judgement levers it never considered are the whole of the difficulty.

Recorded to `Tasks/_meta/Stump_Hypotheses.md` and `Tasks/_meta/Hardness_Patterns_Log.md`.

---

## Action items

1. **Submit the two AF justifications** in `S4_AF_justifications.md`, for the outside provider's price and for the comparison against the net proceeds. Voice gate clean.
2. **Appeal one judge-error cell:** criterion 17, run 5. The Slack message posted at tool call 58 carries "$8,447 since the 9th" with the per-title split; the grader called it absent. Citation in `S4_judge_errors.md` finding 1.
3. **No Bucket 1 fixes.** No rubric edit is required by this export.
4. **Two optional hardenings, operator's call, both cell-neutral.** Criterion 5's evidence field gains the near-miss FAIL list every other exact-value criterion already has; criterion 7's evidence field states the surface it grades so the run-6 cross-artifact credit cannot recur. Wordings and paired OE notes in `S4_fixes.md` sections A and B. Applying either requires re-running `check_oe_rubric_sync.py`, `check_rubric_antipatterns.py` and `validate.py` on both phases.
5. **Do not re-run the platform verifier to chase cells.** Two gradings of these trajectories have now moved roughly a tenth of the decision cells in both directions with no change to any gate. Every gate passes with margin and the rubric set carries no defect. A third grading buys noise.

## Pin history

| Stage | `7_Rubrics.json` | `8_Verifier_Fails.txt` |
|---|---|---|
| Pass 1 classification | `69713012b52f17d6…` 11,941 B | `d28c7c4ac71a9abd…` 53,558 B, per-run [16, 20, 22, 18, 16, 17] |
| Pass 1 after fixes applied | `bf26e5373d7fbab6…` 13,703 B | `d28c7c4ac71a9abd…` 53,558 B, unchanged |
| **Pass 2, this report** | `bf26e5373d7fbab6…` 13,703 B, unchanged | `ad0260ca6682ad47…` 55,564 B, per-run [17, 19, 21, 20, 19, 22] |

The rubric file has not moved since the pass-1 fixes landed, so this pass graded exactly the rubric set that was shipped. The export moved once, at the boundary between the passes, which is the re-grade this pass was invoked to read. `check_export_freshness.py` was re-run bare immediately before this report was declared complete and exits 0.
