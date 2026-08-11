# Verification: PIPELINE S4 · Task 2 (`2_6a6beba55996ad2ada369b15`) · pass 2

Universe **harmonygames**. Model **Claude Opus 4.8**, single-model. Pass-1 verification archived unaltered at `_aux/Council_Reports/_superseded/pass1_2026-08-07/Verification_s4.md`.

## Data sources consulted

- `7_Rubrics.json` :: the 28-criterion set being classified. `bf26e5373d7fbab6…`, 13,703 B, unchanged since the pass-1 fixes landed.
- `8_Verifier_Fails.txt` :: verifier output. `ad0260ca6682ad47…`, 55,564 B, per-run [17, 19, 21, 20, 19, 22]. **Drifted from the pass-1 pin and re-pinned before any classification.**
- `trajectory-runs/trajectory-run-{1..6}.json` :: walked per failing criterion. Byte-identical to the set pass 1 walked; `parse_trajectories.py` re-derives the same per-run tool-call totals.
- `HarmonyGames_Base_Universe/Services_Data/` :: ground truth re-confirmed first-hand this pass, not carried forward from pass 1. `4_Changelog.json` is `[]` and `9_Universe_inject.sql` touches no marketing, finance, slack or gmail surface used here, so base equals graded for every figure checked.
- `_aux/Fact_Ledger.json`, `_aux/Universe_Split/`, `_aux/Hardness_Plan.md`, `_aux/Trajectory_Stats.json`.

## Ground truth re-verified in this pass

| Fact | Source, checked directly | Result |
|---|---|---|
| Wind-down provider price, Slack | `slack/messages/C07C2866011/2026-02.json` ts `1770850852.708789` | Present: "the cost of Sunset is about ~$15K - the data will likely cover our costs without us liquifying the laptops/assets". Sunset is established as the provider four messages earlier ("work with Sunset or sherwood… They charge a percent of the wind down"). |
| Wind-down provider price, mail | `gmail/threads/EMPLOYEE_0016_EMAIL_1856871678357556733.json` | Present: "including managing legal, tax, and operational work, with an estimated cost of $13,000 to $15,000". `user_email` is `robert@harmonygames.co`, the persona's own mailbox; subject is `Notes: "Harmony Games Wind Down" Feb 11, 2026`. The string wraps across a line, which is why a naive grep for the full phrase misses it. |
| Ad-account owner | OE 12 grounding in `#executives` January 2026 | Present: the campaign start/stop and "I think I set up both Unity and and ironsource properly now" messages. Arthur Blake appears only as an integration helper. |
| Peak combined DAU | Returned live by the tool | `snowflake_execute_query` returns the literal `"801"` for `2026-02-07` to any query grouping by date before taking the max. Run 3 tool call 50 and run 6 tool call 33 both received it. |
| Burn-table collision | `FINANCE.EXPENSES.MONTHLY_BURN` | February `legal = 13000` still lands in the same numeric band and is still what every run reported. The pass-1 exclusion clause correctly refuses it on all six cells. |

## Retrieval reachability, established rather than assumed

The AF justifications rest on the claim that the provider's price was reachable. That claim was tested rather than inherited:

- **Provider name reached every run.** "Sunset" or "Sherwood" appears in a tool result in all six runs (run 1 call 8, run 2 call 14, run 3 call 22, run 4 call 14, run 5 call 8, run 6 call 14). Runs 3 and 5 wrote the name into their own deliverables.
- **The price reached none.** The string "Sunset is about" appears in zero tool results across all six runs.
- **The channel was never opened.** No run called `slack_conversations_history` or `slack_read_channel` on C07C2866011 on any pass. Every run read C0ADGSZKR3R only, apart from run 6 which also read C04UEQVDVB7. The channel is served rather than blocked: keyword searches returned its message bodies to runs 3, 5 and 6.
- **The mail thread surfaced once and was not opened.** Run 3 tool call 44, `gmail_search_messages` with `query: 'SVB OR Sunset OR "wind down" OR dissolution OR Singular OR Unity'`, returned `robert@harmonygames.co/1856871678357556733` as its first result. The search returns bare ids with no subject or snippet. Runs 1, 2 and 5 each made exactly one `gmail_get_thread` call, all three on the same unrelated thread; runs 3, 4 and 6 made none.

## Deep check on the all-failing pair (criteria 10 and 11)

The two AF justifications rest entirely on the claim that the provider's price was reachable and the agents did not go and get it. That claim was attacked directly rather than restated. Eight tests, run against the trajectories and the universe.

| # | Test | Result |
|---|---|---|
| 1 | Did C07C2866011 ever appear in a tool **result**? | **Yes, in all six runs.** `slack_channels_list` returned it to runs 1, 2 and 5. `slack_search_public_and_private` returned it to runs 1, 3, 4, 5 and 6, with message bodies attached in runs 3, 5 and 6. |
| 2 | Did C07C2866011 ever appear in a tool **input**? | **No. Zero occurrences across all six runs.** Not a denial. The read was never attempted. |
| 3 | Did the price text ever reach an agent? | **No.** Zero hits for "cost of Sunset", "$15K", "13,000 to" in any tool result. Every "$13,000" hit in any result is a write-call echoing the agent's own document body back at it (runs 2, 3, 6). |
| 4 | Does `slack_conversations_history` work on a **private** channel for this persona? | **Yes.** Run 6 tool call 48 read C04UEQVDVB7, which is private, and received 30 messages running to 2026-02-11. C07C2866011 is private with an identical members array per OE 16. |
| 5 | Does the read path reach the Feb-11 window at all? | **Yes.** Run 1 tool call 43 paged C0ADGSZKR3R with a 2026-02-12 cursor and received 60 messages spanning 2026-02-09 to 2026-02-12. |
| 6 | Any permission denial, ACL error or tool failure that could explain the miss? | **None.** No structured error, no `not_in_channel`, no `access_denied` in any run. Every literal "403" in the corpus is a substring inside a table id or a file timestamp, checked individually. |
| 7 | Is there another surface carrying the price that the criterion unfairly ignores? | **No.** Exactly two files in the entire universe contain it: `slack/messages/C07C2866011/2026-02.json` and `gmail/threads/EMPLOYEE_0016_EMAIL_1856871678357556733.json`. Confluence, Drive, Docs, Linear, Trello, contacts and Snowflake carry zero. |
| 8 | Did any run search for a term that names the provider? | **No.** Twenty-three distinct Slack search queries were issued across the six runs. Not one contains "Sunset", "Sherwood", "advisor", "legal", "dissolution", "provider" or "cost". Runs 3 and 5 wrote the provider's name into their own deliverables without ever searching for it. |

**The one claim that could not be closed, stated plainly.** The highest-dated C07C2866011 message ever returned to any run is **2026-02-09**. The price message is 2026-02-11. Nothing in these trajectories therefore demonstrates that a *search* for "Sunset" would have surfaced it; the only Feb-12 search hit in the corpus is from C0ADGSZKR3R, not from the executives channel. I could not test the search index directly.

This does not rescue either criterion, because the two retrieval paths that do not depend on the search index were both available and neither was attempted: a `slack_conversations_history` call on a channel three runs had listed by name, and a `gmail_get_thread` on an id run 3's own search had already handed it. Both are calls every run made against other targets in the same session. But the limit is recorded so no later pass claims more than the evidence carries, and the AF justification is worded to rest on the two calls that were not made rather than on a search that was not run.

**Criterion 11, checked independently.** No deliverable in any of the six runs contains a comparison between any wind-down service cost and the 10,800 net, in any wording. The criterion is 100% coupled to criterion 10: with no provider price retrieved, the comparison cannot exist. It survives rule 21 because it grades an inference rather than restating the fact, and every run already held the 10,800 side, so a run reaching the price still had a step left to take. The residual risk is honest and named: this pair contributes two all-failing criteria for one missed retrieval, and if a reviewer pushes back on the all-failing count, criterion 11 is the one to concede, not criterion 10.

**Verdict of the deep check: both criteria are legitimate model failures.** The environment served the channel, the tools reached the window, the persona had the access, no call was denied, and two independent one-call paths to the figure were left untaken while the provider's own name sat in two runs' finished write-ups.

## Eval spec verified

- `Evals_harmonygames/4_Verifier_Fails_Eval.md` :: five-verdict taxonomy re-applied per criterion. The **Tool Precision Mismatch** hard gate, which carried four criteria out of Bucket 3 in pass 1, was re-tested against criterion 5 and **does not reach it**: the tool serves the exact value 801 and two runs received it. Precision mismatch is about what the environment can expose, not about how the agent chose to round.
- Phase 3.3 cross-run comparison applied to criteria 12, 16 and 24 and to criterion 5. In both families the grader graded like text alike, so neither is judge inconsistency.
- `Docs_harmonygames/9_Common_Error.md` all-failing removal rule and `11_Taxonomy.md` severity ladder read before any classification.
- `AGENTS.md` rule 15 (pin first, never reconcile drift by hand), rule 16 (3-cell / both-model Bucket 1b threshold), rule 17 (audit the passing cells), rule 21 (removal before justification) all applied and each cited at the point it bound a decision.
- 5-point pre-write checklist applied to criteria 10 and 11 before either AF justification was drafted; the table is in `S4_fixes.md` section C.

## QC spec sub-dims verified

- **All-Failing Rubrics sub-dim.** Bucket 1 ratio 0/12 = 0.0%, below 25%. Score **5/5 (PASS)**.
- **Trajectory T1, tool-call floor.** Avg 61.5 total, 49.3 MCP. PASS against the 40+ target and the 15 floor.
- **Trajectory T2, pass@1 ≤ 40%.** 0/6 = 0.0%. PASS. Corrected value identical, since Bucket 1 is empty.
- **Trajectory T3, error runs ≤ 2.** 0/6. PASS.

## Verification statements

- [x] Export pinned before any classification, and re-verified bare at exit. The entry pin recorded the drift from pass 1 explicitly; no pass-1 count was carried forward.
- [x] Trajectory walk recorded for EVERY one of the 12 failing criteria across all 6 runs, not just for the Bucket 2 cell.
- [x] Every bucket entry carries a trajectory citation naming the run, the tool call and the parameter values.
- [x] T2 and T3 hard gates evaluated and recorded in `S4_verdict.md`.
- [x] Passing cells audited beyond `check_criterion_dependencies.py`. One structurally impossible PASS found, criterion 7 run 6, granted on a quote that exists only in the tracking item and not in the written account it grades.
- [x] Bucket 1 ratio computed from the export in hand; All-Failing Rubrics sub-dim scored.
- [x] Removal argued first for both all-failing criteria, at its strongest, before any justification prose.
- [x] 5-point checklist confirmed YES on all five for both AF justifications.
- [x] `check_justification.py` exit 0 on the AF batch.
- [x] `check_export_freshness.py` bare, `check_criterion_dependencies.py`, `check_oe_rubric_sync.py`, `check_rubric_antipatterns.py` all exit 0 at exit.
- [x] No rubric edit made during this pass, so no re-run of the sync and anti-pattern gates was triggered by an edit. They were run at entry and again at exit regardless.

## Discrepancies surfaced

1. **The export drifted between passes and pass 1's reports describe superseded bytes.** Handled as rule 15 requires: re-derived from scratch, pass-1 reports archived rather than edited. Recorded here because `phase_ready.py` and `close_task.py` would both have said READY without it.
2. **Regrading noise on byte-identical trajectories.** Criterion 7's single PASS moved from run 3 to run 6, criterion 25 went 1/6 to 2/6, criterion 27 went 1/6 to 0/6, none of them touched by the pass-1 fixes. Roughly a tenth of the decision cells moved, in both directions, with no gate affected. No single-cell number in this pass is treated as a stable quantity.
3. **Criterion 7 run 6 is a cross-artifact false PASS.** The criterion fails 5/6 as graded and 6/6 in substance. Classified on the graded cells per rule 15, flagged as the most likely next all-failing criterion, with its AF justification pre-drafted in `S4_fixes.md` section B.
4. **Criterion 5 carries a live over-specificity tension on two cells.** Runs 4 and 6 wrote "~800" for 801, and run 6 had the exact value in hand. Argued in full and resolved against changing the criterion, on three grounds: the environment serves the value, the grader was consistent, and loosening would credit run 4, which never performed the aggregation the criterion exists to test. Recorded so it is not silently re-decided.
5. **Criteria 10 and 11 cannot fail independently.** Two all-failing cells trace to one missed retrieval. The pair survives because the second criterion grades an inference rather than a restatement, but the coupling is named in the verdict rather than hidden inside the count.
6. **All four Hardness Plan stumps produced nothing, and the [MED] partial hit from pass 1 has now decayed to zero** (criterion 27 passes 6/6 on this grading). The task's real difficulty comes from four levers the plan never named. Appended to the calibration logs.
