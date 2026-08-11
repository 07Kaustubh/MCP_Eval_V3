# S4 fixes — Bucket 1 (Rubric Invalid)

Task `2_6a6beba55996ad2ada369b15` · universe **harmonygames** · 6 runs, 0 errored.
Export pinned at entry: `8_Verifier_Fails.txt` `d28c7c4ac71a9abd…` 53,558 B, per-run [16, 20, 22, 18, 16, 17]; `7_Rubrics.json` `69713012b52f17d6…` 11,941 B.

## STATUS: APPLIED 2026-08-07, on operator instruction

All six rubric edits and all paired Oracle Event edits in section C are now in `7_Rubrics.json` and `6_Oracle_Events.txt`. Pre-fix files are archived at `_aux/7_Rubrics.pre_s4fix.bak.json` and `_aux/6_Oracle_Events.pre_s4fix.bak.txt`; the pin that the classification was reasoned against is archived at `_aux/S4_input_pin.classification.json`.

**Pin movement, recorded deliberately.** Applying the fixes drifted `7_Rubrics.json` from `69713012b52f17d6…` (11,941 B) to `bf26e5373d7fbab6…` (13,703 B), and `check_export_freshness.py` correctly FAILed on it. This drift is the approved fix being applied *after* the classification loop closed, not a mid-pass re-paste, so it was re-pinned rather than treated as an invalidation. `8_Verifier_Fails.txt` is byte-identical throughout (`d28c7c4ac71a9abd…`, per-run [16, 20, 22, 18, 16, 17]), so no per-run count in these reports moved. **Every bucket call and matrix cell in `S4_verdict.md` describes the pre-fix rubric**, which is the correct reading of them; the next platform export supersedes them.

**Two deviations from the drafts below, both forced by gates and both kept.**

1. `check_rubric_antipatterns.py` rejects `FAIL only if` as a MODERATE finding: *"makes every unenumerated shape a PASS, including plain omission. Rewrite additively."* It is right, and it outranks the phrasing suggested in the S4 runbook's Bucket 1b fix pattern. Criteria 4 and 10 were rewritten to `FAIL if X, and FAIL if Y`.
2. `validate.py --phase rubrics` warned that criterion 6's evidence carried `2026-02-09`, a date absent from its title. The exclusion is now expressed as "the stop-decision day itself", which the title already bounds with "from 2026-02-10 onward".

An unrelated `validate.py --phase oe` warning was also self-inflicted and cleared: the word "warehouse" in OE 24's element list tripped the service-mapping check, since OE 24 is a Confluence/Docs/Drive write step. Reworded to "the whole-dollar figure a query returns".

Post-fix gate state: `check_oe_rubric_sync` OK · `check_rubric_antipatterns` OK · `check_criterion_dependencies` OK · `check_export_freshness` OK against the new pin · `validate.py --phase rubrics` **0 fails, 0 warns** · `validate.py --phase oe` **0 fails, 0 warns**.

---

Every edit below has a paired `6_Oracle_Events.txt` edit listed in section C — `check_oe_rubric_sync.py` will FAIL if the rubric moves and the OE does not.

---

## A. Tool Precision Mismatch — four criteria, all failing 6/6

### The mechanism, established before any classification

The hydrated HarmonyGames warehouse stores `ANALYTICS.MARKETING.AD_SPEND_DAILY.spend_usd` as a whole-dollar integer, rounded half-up from the source value. The cents in the universe file are not reachable through `snowflake_execute_query` by any query path. Three independent proofs:

1. **Row-level.** Universe row `2026-01-05 / combo_fighter / meta_facebook / US` carries `spend_usd = 53.57`. Run 1, tool call 50 (`SELECT * FROM ANALYTICS.MARKETING.AD_SPEND_DAILY WHERE game_id ILIKE '%combo%'`) returned that row as `"54"`. Same call: `29.44 -> "29"`, `27.76 -> "28"`, `25.91 -> "26"`, `17.02 -> "17"`, `14.72 -> "15"`.
2. **Aggregate-level.** Every aggregate any run retrieved equals the sum of half-up-rounded rows, never the exact sum. Predicted-vs-observed, all six matched:

   | Aggregate | Universe exact | Sum of rounded rows | Tool actually returned |
   |---|---|---|---|
   | combo_fighter, 2026-01-05 to 2026-02-28 | 7,483.42 | 7,476 | `"7476"` (Run 1 call 52; Run 5 call 45; Run 6 call 41) |
   | combo_fighter, through 2026-02-09 | 5,039.34 | 5,035 | `"5035"` (Run 6 call 129) |
   | all titles, 2026-02-10 to 2026-02-28 | 8,452.64 | 8,447 | `"8447"` (Run 5 call 134; Run 6 call 53) |
   | combo_fighter, 2026-02-10 to 2026-02-28 | 2,444.08 | 2,441 | `"2441"` (Run 5 call 134; Run 6 call 45) |

3. **Cross-column control.** `avg_session_minutes` discriminates the two paths: the exact column average is 12.674, the integer-rounded column average is 12.736. Run 6, tool call 39 (`ROUND(AVG(avg_session_minutes),2)`) returned **12.74**. The warehouse is serving integers for every `NUMBER` column, not only for spend.

**Two falsification attempts, both failed.**

- *Could the rounding be at serialization rather than at storage?* No. If the engine computed on exact values and rounded the answer, `SUM(spend_usd)` would return **7483**. It returns 7476, which is the sum of the rounded rows. Twelve aggregates were predicted from the storage-rounded model before being compared against the trajectories and all twelve matched (7476, 5035, 8447, 2441, 5574, 432, and the six channel splits). Across all six runs and every `snowflake_execute_query` call, **zero** stored-column values ever came back with a decimal.
- *Is there another surface carrying the exact figures?* No. `SINGULAR_INSTALLS_RAW` and `UA_SPEND_UNIFIED_V2` hold zero combo_fighter rows, matching OE 7. No Confluence page, Google Doc, Sheet, Drive file, Linear issue, Trello card or contact record contains either figure. A text search does hit `7483.42` and `8452.64` inside Slack and Gmail, but every one is a substring of an unrelated 2023-2025 message timestamp (`"ts": "1715188452.640269"`), not a stated amount. Recorded here so a later pass does not read those grep hits as a reachable source.

This is the `Evals_harmonygames/4_Verifier_Fails_Eval.md` **Tool Precision Mismatch** hard gate, lines 250-266: *"Tool systematically exposes only a rounded/truncated value while the criterion requires inaccessible precision -> Tool Precision Mismatch; the criterion is invalid for that environment."* No agent on any run, present or future, can state 7,483.42 or 8,452.64 from the tool surface. These four criteria cannot be Legitimate Fails and cannot carry AF justifications.

The mixed-finding clause at line 265 applies to criteria 6, 17 and 20 on runs 1-4: those runs also scoped the still-running spend to Combo Fighter alone (`"2441"`) instead of across the studio's titles. That scope miss is a genuine task miss and the rewrite below preserves it as a fail. Runs 5 and 6 scoped it correctly and were failed only on the inaccessible cents.

---

### Criterion 4 — written account, full-life acquisition spend

**Fails:** 6/6.

**Trajectory citation.** Run 5, tool call 45: `SELECT game_id, …, SUM(spend_usd) total_spend … GROUP BY game_id` returned `["combo_fighter", "2026-01-05", "2026-02-28", 330, "7476", "1341"]`. The agent wrote "Lifetime paid UA on Combo Fighter: $7,476 across six networks … 1,341 attributed installs" — the exact value the tool gave it, for the exact window the criterion asks about, with the row count and install count both matching the criterion's own source. Runs 1, 2 and 4 wrote the same 7,476. Runs 3 and 6 wrote the two components, 5,035 + 2,441.

**Before**
> The Agent's written account states Combo Fighter's total paid acquisition spend across 2026-01-05 to 2026-02-28 as 7,483.42.

**After**
> The Agent's written account states Combo Fighter's total paid acquisition spend across 2026-01-05 to 2026-02-28 as approximately 7,476.

**Evidence field, after**
> Inspect the created page or document for the total acquisition spend figure covering the full span of the acquisition record. The warehouse returns whole dollars, so 7,476 is the value the tool exposes and 7,483.42 is the underlying exact total; either is correct, as is a stated sum of the two components 5,035 and 2,441. FAIL only if the account gives no total covering 2026-01-05 to 2026-02-28, or gives the 5,035 within-engagement-window subtotal as the full-life figure.

**Why this is not a loosening.** The discriminating lever in this criterion was never the cents. It is the window: 7,476 spans the acquisition record to 2026-02-28 while 5,035 stops on 2026-02-09 with the engagement and revenue tables, and OE 8 is explicit that an account reporting 5,035 in place of the total "has scoped the acquisition record short." The rewrite keeps that discrimination and removes only the precision the environment does not serve.

---

### Criterion 6 — written account, still-running spend

**Fails:** 6/6.

**Trajectory citation.** Run 6, tool call 53: `SELECT SUM(CASE WHEN date>'2026-02-09' THEN spend_usd ELSE 0 END) …` returned `["8447", "1541", 19]` — the right scope, the right 19 days, and the tool's whole-dollar rendering of 8,452.64. The agent wrote "$8,447 over 19 days". Run 5 reached the same value at call 134 and wrote "Total spent AFTER the 9 Feb stop: $8,447 (1,541 installs)". Runs 1-4 never widened past Combo Fighter and wrote 2,441 (Run 1 call 60; Run 4's Confluence page, "$2,441 for Combo Fighter UA post-shutdown").

**Before**
> The Agent's written account states that 8,452.64 of paid acquisition spend has been charged across the studio's titles over the 19 days from 2026-02-10 onward.

**After**
> The Agent's written account states that approximately 8,447 of paid acquisition spend has been charged across the studio's titles over the 19 days from 2026-02-10 onward.

**Evidence field, after**
> Inspect the created page or document for the spend charged over the days following the stop decision. The warehouse returns whole dollars, so 8,447 is the value the tool exposes and 8,452.64 is the underlying exact total; either is correct. FAIL if the figure given covers Combo Fighter alone rather than all three titles (2,441 is the Combo Fighter subtotal and does not satisfy this criterion), if the window includes 2026-02-09 (8,916 on the tool, 8,922.12 exact), or if no figure is given for the days after the stop decision.

---

### Criterion 17 — #winddown message, still-running spend

**Fails:** 6/6. Same mechanism, same figure, restated in the Slack post.

**Trajectory citation.** Run 5's `slack_send_message` to C0ADGSZKR3R carried "$8,447 since the 9th"; Run 6's carried "$8,447 over 19 days". Runs 1-4 carried 2,441.

**Before**
> The Agent's #winddown message states the 8,452.64 of paid acquisition charged over the 19 days from 2026-02-10 onward.

**After**
> The Agent's #winddown message states the approximately 8,447 of paid acquisition charged over the 19 days from 2026-02-10 onward.

**Evidence field, after**
> Inspect the posted message for the continuing spend figure covering the days after the stop decision. Accept 8,447 or 8,452.64. FAIL if the message gives the Combo Fighter subtotal 2,441 in its place, or gives no continuing spend figure.

---

### Criterion 20 — tracking item, still-running spend

**Fails:** 6/6. Same mechanism, same figure, restated in the tracker.

**Trajectory citation.** Run 5's `linear_create_issue` description: "Total since the 9 Feb stop: **$8,447 / ~$445 per day, still running**". Run 6's Linear issue: "$8,447 / 1,541 installs over 19 days". Runs 1-4 carried 2,441 (Run 1: ENG-2438, "$2,441 spent Feb 10 -> Feb 28").

**Before**
> The Agent's tracking item carries the figure 8,452.64 for the paid acquisition charged over the 19 days from 2026-02-10 onward.

**After**
> The Agent's tracking item carries a figure of approximately 8,447 for the paid acquisition charged over the 19 days from 2026-02-10 onward.

**Evidence field, after**
> Inspect the created tracking item for the continuing spend figure covering the days after the stop decision. Accept 8,447 or 8,452.64. FAIL if the item carries the Combo Fighter subtotal 2,441 in its place, or carries no spend figure.

---

## B. Value collision on the wind-down service cost — two criteria

### Criterion 10 — the priced managed wind-down

**Fails:** 5/6. The single PASS is on the wrong figure.

`FINANCE.EXPENSES.MONTHLY_BURN` carries a `2026-02-01 / legal / 13000` row. Every run queried that table. The criterion accepts "approximately 13,000 to 15,000", so a February legal burn line of exactly 13,000 lands inside the accepted band without the agent ever discovering the outside wind-down provider. Four runs wrote materially the same sentence and the grader split on it:

| Run | What the account actually says | Source it came from | Decision |
|---|---|---|---|
| 1 | `\| Wind-down legal \| ~$13K \| Booked in Feb burn \|` | MONTHLY_BURN | **Fail** |
| 2 | "Legal / managed wind-down … ~$13,000 in February alone (plus ~$5,000 in January)" | MONTHLY_BURN | **Pass** |
| 3 | `\| Feb wind-down legal \| $13,000 \| Already paid from cash. \|` | MONTHLY_BURN | **Fail** |
| 6 | "Wind-down legal: ~$13,000 booked in February (largely already incurred)" | MONTHLY_BURN | **Fail** |
| 5 | "the SVB card payoff lands inside that ~$13K envelope" | SVB, not a wind-down price | Fail |
| 4 | no figure in the band | — | Fail |

Run 2 differs from runs 1, 3 and 6 only in having written the words "managed wind-down" next to the same burn-table number. That is four cells turning on phrasing rather than on the fact, which is over the `AGENTS.md` rule 16 / Bucket 1b threshold of three, and it matches `Evals_harmonygames/4_Verifier_Fails_Eval.md` Phase 3.3 cross-run comparison: the failing runs did what the passing run did.

**The intended fact was found by nobody, and it is not an access problem.** OE 19 grounds it twice and both surfaces are confirmed inside the persona's reach:

- `slack/messages/C07C2866011/2026-02.json` ts `1770850852.708789`, "the cost of Sunset is about ~$15K - the data will likely cover our costs without us liquifying the laptops/assets".
- Gmail thread id `robert@harmonygames.co/1856871678357556733`, subject `Notes: "Harmony Games Wind Down" Feb 11, 2026`, body "an estimated cost of $13,000 to $15,000". The thread id resolves to Robert's own mailbox.

Neither string appears in any of the six trajectories. **The channel is served, so this is retrieval behaviour and not an ACL denial:** Run 5 call 5 (`slack_channels_list`) returned `{"id": "C07C2866011", "name": "executives", "is_private": true}`, and searches returned message bodies from it (Run 3 call 114 surfaced Leonard's "$4K outstanding debt to Applovin" from C07C2866011; Run 5 call 19 surfaced his board-email draft). What never came back was any **February 2026** message from that channel, on any run. No run called `slack_conversations_history` on C07C2866011 even once; every run touched #executives only through keyword searches, several of which returned empty (Run 4 call 115 `"SVB balance owe"`, Run 5 call 107 `"data buyer license offer"`, Run 5 call 112, Run 6 call 116). The Gmail route was under-searched the same way: 24 gmail calls across the six runs and the meeting-notes thread was served to none of them.

So the underlying difficulty is real and should be preserved, and the Persona ACL hard gate does not fire. What must change is the acceptance band, which currently lets an unrelated burn line satisfy the criterion.

**The collision source is confirmed on every run.** All six queried `FINANCE.EXPENSES.MONTHLY_BURN` and all six received the February `legal = 13000` row (Run 1 calls 78 and 88, Run 2 call 78, Run 3 calls 89-100, Run 4 call 103, Run 5 call 71, Run 6 call 83). The number was in front of every agent; only the words around it varied.

**Before**
> The Agent's written account states the managed wind-down service cost as approximately 15,000, or as the range of approximately 13,000 to 15,000 that the records carry.

**After**
> The Agent's written account prices the outside managed wind-down provider at approximately 15,000, or at the 13,000 to 15,000 range the wind-down meeting notes carry.

**Evidence field, after**
> Inspect the created page or document for a cost attributed to the outside firm engaged to run the wind-down, accepting either the rounded figure or the range. FAIL if the account gives no figure for that provider, or if the only figure it offers in that band is the February legal line from the monthly burn table, which is a booked accounting cost rather than the provider's quote.

**Regrade of every cell under the rewrite.** Runs 1, 3, 4, 5 and 6 stay Fail — none names an outside provider's price. Run 2 flips Pass to Fail: its "~$13,000 in February alone (plus ~$5,000 in January)" is explicitly sourced to `MONTHLY_BURN` in its own sources list and carries a monthly framing the provider's quote does not have. The criterion becomes 6/6 failing under the rewrite, which is why the removal argument in section D is recorded for it.

---

### Criterion 11 — the comparison against net proceeds

**Fails:** 5/6, and the one PASS is downstream of criterion 10's collision.

**Trajectory citation.** Run 2's Google Doc draws the comparison as "The net data proceeds (~$10.8K) are roughly the size of ONE line item — the legal bill" — that is the 13,000 burn row set against 10,800, not the provider's quote set against 10,800. Runs 1, 3, 4, 5 and 6 never identified a provider price, so the comparison is simply absent from each (Run 4's page reaches the neighbouring point, "counsel's plan for pain was ~$50K", without pricing the provider).

**Before**
> The Agent's written account states that the managed wind-down service cost alone exceeds the net proceeds of the data agreement.

**After**
> The Agent's written account states that the outside managed wind-down provider's cost alone exceeds the 10,800 net proceeds of the data agreement.

**Evidence field, after**
> Inspect the created page or document for the comparison between the outside provider's wind-down price and the net proceeds. FAIL if the comparison is absent, if it points the other way, or if it rests on the February legal line from the monthly burn table rather than on the provider's quote.

The subject is bound by description ("the outside managed wind-down provider", "the February legal line from the monthly burn table") rather than by criterion number, so the binding survives renumbering.

---

## C. Paired Oracle Event edits — mandatory, same commit

`check_oe_rubric_sync.py` currently exits 0. It will FAIL if the rubric figures move and these do not.

| OE | Line | Change |
|---|---|---|
| OE 8 | 15 | `spend_usd summing to 7,483.42` -> `7,483.42 in the source, which the warehouse serves as 7,476`. Same for the within-window subtotal `5,039.34` -> add "5,035 on the tool". The six channel splits are also integer-served: meta_facebook 2,265.43 -> 2265, meta_instagram 1,355.97 -> **1351**, unity_ads 1,318.85 -> 1318, google_uac 1,070.33 -> 1068, ironsource 742.91 -> 742, applovin 729.93 -> **732**. Note instagram and applovin move by more than a dollar; an OE that pins them to the cent misdescribes what the agent sees. |
| OE 10 | 19 | `totalling 8,452.64` -> add "served as 8,447". Splits: domino_delights 5,569.66 -> 5574, combo_fighter 2,444.08 -> 2441, zombie_match_3d 438.90 -> 432. The wrong-window control `8,922.12` -> 8,916 on the tool. |
| OE 11 | 21 | `17 rows totalling 346.00 … combo_fighter is 160.88` -> tool serves 345 and 161. |
| OE 22 | 43 | Carries the literal figure: "The 8,452.64 of advertising spent since the stop decision does not close that gap on its own". Mirror it. The derived claim on the same line, "roughly 78 percent of the net proceeds", holds either way (8,447/10,800 = 78.2%, 8,452.64/10,800 = 78.3%), so only the literal needs to move. |
| OE 24 | 47 | `7,483.42 of acquisition spend` and `8,452.64 spent over the 19 days` -> mirror criteria 4 and 6. |
| OE 25 | 49 | `the still-running spend figure of 8,452.64` -> mirror criterion 17. |
| OE 26 | 51 | `description carrying the 8,452.64 figure` -> mirror criterion 20. |
| OE 27 | 53 | `the 8,452.64 that has continued to leave since the stop decision` -> mirror. |
| OE 28 | 55 | Carries `7,483.42` in the decoy mapping: "the two versioned marts in OE 7 are graded through the 0.00 revenue and the 7,483.42 acquisition spend in OE 24". Mirror it, or the decoy map points at a figure criterion 4 no longer names. |
| OE 19 | 37 | Add the disambiguation the rubric now carries: the ~15,000 Sunset quote and the 13,000-15,000 meeting-notes range are the priced managed wind-down; the `FINANCE.EXPENSES.MONTHLY_BURN` February `legal = 13000` row is a different fact that lands in the same band and does not satisfy the criterion. |

**Completeness check on this table.** Every occurrence of the four affected figures in `6_Oracle_Events.txt` is accounted for: line 15 (12 hits), 19 (5), 21 (2), 43 (1), 47 (2), 49 (1), 51 (2), 53 (2), 55 (1). In `7_Rubrics.json` they sit at lines 21, 33, 99 and 117, which are criteria 4, 6, 17 and 20.

## D. Removal arguments (AGENTS.md rule 21, argued before any rewrite)

Rule 21 requires the removal case first for every criterion failing all completed runs.

- **Criteria 4, 6, 17, 20.** Removal was considered and rejected. What they grade — the full-life acquisition window, and the still-running spend scoped across all three titles over the 19 days after the stop decision — is the prompt's second ask ("Whatever is still taking money from us needs naming with a figure against it") and it discriminates: four of six runs got the scope wrong. The defect is confined to the precision, so the defensible action is re-anchoring, not deletion. This defence is one I would state to a reviewer unprompted.
- **Criterion 10.** Under the rewrite it becomes 6/6 failing, so rule 21 applies to it as well. Removal was considered and rejected: the priced managed wind-down is the direct answer to the prompt's third ask ("whether that genuinely covers shutting down in an orderly way"), it is grounded twice on surfaces inside the persona's read scope, and it is the figure that settles the persona's stated belief, sitting below the 22,500 gross and above the 10,800 net. Nobody finding it is the intended difficulty, not evidence of an unfair criterion. It survives.
- **Criterion 11.** Same defence, and it is the comparison that converts the figure into the conclusion the prompt asks for.

## E. Not changed, recorded so the next pass does not relitigate

- **Criterion 27** (licensing rather than outright sale) failed only Run 4, whose Confluence page used "Data-licensing deal" correctly while its final response said "the data sale lets us close roughly cash-neutral". The criterion's evidence field scopes it to both surfaces, so the grading is correct. It is non-atomic in spanning two artifacts, which is worth a note at the next rubric pass, but it cost one cell and splitting it now would change the graded set for no measured benefit.
- **Criterion 25** (funds available at 13,300) failed only Run 2, which stated 10,800 and 2,500 separately and never summed them. Correctly graded; this is the L8 chain doing its job.
