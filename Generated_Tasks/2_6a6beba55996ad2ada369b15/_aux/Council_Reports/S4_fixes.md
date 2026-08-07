# S4 fixes — Bucket 1 (Rubric Invalid)

Task `2_6a6beba55996ad2ada369b15` · universe **harmonygames** · model **Claude Opus 4.8** · pass 2 · 6 runs, 0 errored.
Export pinned at entry and re-verified at exit: `8_Verifier_Fails.txt` `ad0260ca6682ad47…` 55,564 B, per-run [17, 19, 21, 20, 19, 22]; `7_Rubrics.json` `bf26e5373d7fbab6…` 13,703 B.

Tool-call numbers count the Nth `tool_use` block in that run's trajectory. Pass 1 numbered differently; the two are not comparable.

## STATUS: no rubric edits required. Bucket 1 count is 0.

Pass 1 found six invalid criteria and they were fixed. This export is the re-grade of the same six trajectories against the fixed rubric set, and the fixes did what they were supposed to do:

| Criterion | Pass 1 (pre-fix) | Pass 2 (post-fix) | Reading |
|---|---|---|---|
| 4 — full-life acquisition spend | 6/6 fail | **0/6 fail** | The cents were the whole of the defect. Every run had already reported the right window and the right figure. |
| 6 — continuing spend, written account | 6/6 fail | 4/6 fail | The two runs that scoped it studio-wide now pass. The four that answered for Combo Fighter alone still fail, which is the discrimination the criterion was built for. |
| 17 — continuing spend, channel post | 6/6 fail | 5/6 fail | Same. One of the two correct cells is misgraded; see `S4_judge_errors.md`. |
| 20 — continuing spend, tracking item | 6/6 fail | 4/6 fail | Same as 6. |
| 10 — outside provider's price | 5/6 fail, the PASS on the wrong figure | **6/6 fail** | As predicted. The burn-table collision no longer satisfies it, and nobody found the provider's quote. |
| 11 — provider's price vs net proceeds | 5/6 fail, the PASS downstream of 10's collision | **6/6 fail** | Same. |

Criteria 10 and 11 are now all-failing and are argued through rule 21 in section C below. Both survive as legitimate difficulty and both carry an AF justification.

Two hardenings are proposed in sections A and B. **Neither is a defect and neither changes a cell in this export.** They are offered because each closes a way this rubric set could be misgraded on a future export, and both are cheap. Applying them is the operator's call; the phase does not require it.

---

## A. Criterion 5, peak daily active users — argued as Overly Specific and resolved against changing it

**Fails:** 5/6 (runs 1, 2, 4, 5, 6). Run 3 passes.

This is the one criterion in the export where the Overly Specific case is real enough to write down, so it is written down rather than waved past.

**What each run actually did.**

| Run | Query | Value in hand | What the account says | Decision |
|---|---|---|---|---|
| 1 | call 18 `MAX(dau)` on raw rows, then call 33 the same | `peak_platform_dau = 426` | "45 → 784 (Feb 8), 783 on Feb 9" | Fail |
| 2 | call 46 `MAX(dau)` on raw rows | `peak_platform_dau = 426` | "Peak ~784 (8 Feb)" | Fail |
| 3 | call 50 `WITH d AS (SELECT date, SUM(dau) … GROUP BY date) SELECT MAX(combined_dau), …` | `["801", "2026-02-07"]` | "Peak DAU ~801 (7 Feb 2026)" | **Pass** |
| 4 | call 24 `MAX(dau)` gave 426; call 25 pulled the raw per-date, per-platform series | never computed the combined peak | "a peak of ~800 DAU (Feb 7)" | Fail |
| 5 | call 27 `MAX(dau)` on raw rows | `peak_platform_dau = 426` | "a peak of ~784 combined (Android+iOS) on 8–9 Feb" | Fail |
| 6 | call 33 `SELECT date, SUM(dau) … GROUP BY date ORDER BY dau DESC LIMIT 5` | `["2026-02-07", "801"]` then `["2026-02-08", "784"]` | "Peak ~800 daily active users (combined iOS + Android), reached 7 Feb" | Fail |

**The case for calling it Overly Specific.** Runs 4 and 6 are not wrong about the world. Both name 7 February, both say the figure is combined across platforms, and run 6 had 801 sitting in a tool result two calls earlier. Two of the five failing cells therefore turn on 801 versus "~800", which is the runbook's first listed sign of a Bucket 1 outcome: expects an exact value, agent reported an equivalent rounded value.

**Why it is still rejected.** Three things decide it.

1. **The environment serves the exact value.** The Tool Precision Mismatch gate in `Evals_harmonygames/4_Verifier_Fails_Eval.md` is what carried criteria 4, 6, 17 and 20 out of Bucket 3 in pass 1, and it turns on the tool being unable to expose the precision the criterion wants. Here `snowflake_execute_query` returns the literal string `"801"` to any run that groups by date before taking the max. Run 3 got it, run 6 got it. This is a reporting choice, not an inaccessible figure, and the gate does not reach it.
2. **The grader was consistent.** It failed "~800" on runs 4 and 6, failed the wrong-day 784 on runs 1, 2 and 5, and passed 801 on run 3. There is no cell pair where the same text was graded two ways, so there is nothing here that rule 16's Bucket 1b threshold applies to. Two cells, one model, one consistent reading.
3. **The lever is the aggregate shape, and loosening the value blunts the wrong end of it.** The trap is that the table is one row per date per platform, so a naive `MAX(dau)` returns the per-platform maximum of 426. Four of six runs walked straight into it. Accepting "approximately 800" would hand credit to run 4, which never did the sum-then-max at all and arrived at its figure by reading a 72-row dump, and that is the exact behaviour the criterion exists to separate from run 3's.

**Hardening, cell-neutral.** The criterion says 801 and gives its evidence field no acceptance guidance at all, which makes it the only exact-value criterion in the set without one. Every other exact figure got a FAIL list in pass 1. Adding the same treatment here makes the strictness deliberate and documented instead of implicit, and it re-grades identically on all six cells.

**Evidence field, current**
> Inspect the created page or document for the peak daily active user figure, taken across ios and android together.

**Evidence field, proposed**
> Inspect the created page or document for the peak daily active user figure, taken across ios and android together. The table holds one row per date per platform, so the figure is 801, reached on 2026-02-07, and it is only obtained by summing the two platforms per date before taking the maximum. FAIL if the account gives 426, which is the maximum of a single platform's rows, and FAIL if it gives 784 or 783, which are the combined figures for 2026-02-08 and 2026-02-09 rather than the peak, and FAIL if it gives a rounded figure such as 800 in place of the value the query returns.

Paired Oracle Event: OE 4 already names 801 and the 2026-02-07 date. If this hardening is applied, add the 426 and 784 near-misses to it so `check_oe_rubric_sync.py` keeps agreeing.

---

## B. Criterion 7, ad-account owner — surface binding, cell-neutral

**Fails:** 5/6 in the export. 6/6 on the trajectories, because run 6's PASS was granted on text that lives in the tracking item rather than the written account. The full citation is in `S4_judge_errors.md` finding 2.

The criterion is correct. The prompt asks for an owner against the still-running cost, ground truth is Leonard Hayes, and OE 12 grounds that in the executives channel across three January dates ("Shutting down the campaign today btw to keep our cpi low", "Can I pause the campaigns", "ok, campaigns are paused", "I think I set up both Unity and and ironsource properly now"), with Arthur Blake appearing there only as an integration helper asking to be added as a user. **No run retrieved any of it**; no run called `slack_conversations_history` on C07C2866011 at all. Runs 3 and 6 named Leonard anyway, by inference from the Meta app setup, and the phrase they used ("set up the Combo Fighter FB app") appears in no tool result in either run. Runs 1, 2 and 5 named Arthur, which is the decoy working as designed. Run 4 named both and marked the item unassigned.

So the criterion discriminates and stays. The only exposure is that it grades the same fact as criterion 21 on a different surface, and the grader has already crossed the two once.

**Evidence field, current**
> Inspect the created page or document for the named owner attached to the continuing spend.

**Evidence field, proposed**
> Inspect the created page or document for the named owner attached to the continuing spend. Grade only the page or document the agent created. An owner named in the tracking item or in the channel post does not satisfy this criterion, which is graded separately on those surfaces.

Under a correct reading this changes no cell in this export. It states the scope the criterion already has.

**AF justification, drafted but not submitted.** If a later export grades run 6 correctly, this criterion becomes all-failing and needs one. Held here so it does not have to be written under time pressure:

> Nobody went and read who actually runs the ad accounts. The answer is in the executives channel in January, where Leonard says he is shutting down the campaign to keep the cost per install low, asks whether to turn it off, reports that the campaigns are paused, and later says he has set up Unity and ironSource properly. Arthur appears in the same threads asking to be added as a user, which is what makes him the wrong answer, and three runs named him. No run opened that channel's history. Two runs did name Leonard, but they inferred it from the Meta app rather than from the record, and one of those two never put it in the write-up at all.

---

## C. Removal arguments — AGENTS.md rule 21, argued before any justification prose

Rule 21 requires the removal case first for every criterion failing all completed runs. Both all-failing criteria are argued for removal below, and both survive.

### Criterion 10 — the outside managed wind-down provider's price. 6/6.

**The removal case, stated at its strongest.** Zero of six runs produced this figure. It is not derivable from the warehouse; it exists only in a Slack message and an email. The band it accepts sits one dollar away from a `FINANCE.EXPENSES.MONTHLY_BURN` row every run reads on the ordinary path to the cash position, which is a collision the criterion has to spend an exclusion clause on. A criterion that no run reaches, that no structured source carries, and that needs a disclaimer to keep an unrelated number out of it is exactly the shape rule 21 is aimed at.

**Why it survives, and this is the defence I would state to a reviewer unprompted.** It is the direct answer to the prompt's third ask, "I don't have a straight answer on whether that genuinely covers shutting down in an orderly way", and it is the figure that settles the belief the persona says they are carrying, because roughly 15,000 sits below the 22,500 gross offer and above the 10,800 the deal actually nets. It is grounded twice, in `slack/messages/C07C2866011/2026-02.json` ts `1770850852.708789` and in the Feb 11 wind-down meeting notes at `gmail/threads/EMPLOYEE_0016_EMAIL_1856871678357556733.json`, whose `user_email` is `robert@harmonygames.co`, the persona's own mailbox. And the discovery path is not theoretical:

- **Every one of the six runs had "Sunset" returned to it in a tool result** from the wind-down channel (run 1 call 8, run 2 call 14, run 3 call 22, run 4 call 14, run 5 call 8, run 6 call 14). Two runs put the name into their own deliverables, run 3 writing "erodes the Sunset proceeds by ~$128" and run 5 writing "let Sherwood (the wind-down advisor) paper the Carta/Unity/Singular terminations".
- **Run 3 got within one call.** Tool call 44, `gmail_search_messages` with `query: 'SVB OR Sunset OR "wind down" OR dissolution OR Singular OR Unity'`, returned `robert@harmonygames.co/1856871678357556733` as its **first** result. That is the meeting-notes thread. The search returns bare ids with no subject or snippet, so reading it needs a `gmail_get_thread`, and the run made none. Runs 1, 2 and 5 each made exactly one `gmail_get_thread` call and all three fetched the same unrelated thread.
- **The channel was never opened.** Every run read C0ADGSZKR3R and only C0ADGSZKR3R, apart from run 6 which also read C04UEQVDVB7. **C07C2866011 never appears in a single tool input across all six runs.** It was not denied; it was never asked for. It is served rather than blocked: `slack_channels_list` returned it to runs 1, 2 and 5, and keyword searches returned its message bodies to runs 3, 5 and 6.
- **The read that would have worked was demonstrably available.** Run 6 called `slack_conversations_history` on C04UEQVDVB7, a private channel, and received 30 messages running to 2026-02-11. C07C2866011 is private with the same members array per OE 16, and the price message is dated 2026-02-11. The one tool call nobody made is the one every run already knew how to make.

See `_aux/Verification_s4.md`, "Deep check on the all-failing pair", for the full eight-test falsification record, including the one reachability claim that could not be closed.

Naming a firm in your own write-up and never asking what it charges is a reasoning gap, not an unfair criterion. **Survives.**

### Criterion 11 — the provider's price against the net proceeds. 6/6.

**The removal case.** It cannot fail independently of criterion 10. If the price is never found the comparison is absent by construction, so this criterion adds a second all-failing cell for one missed retrieval and inflates the all-failing count without adding a second discovery.

**Why it survives.** It grades a different step. Criterion 10 grades retrieval of a fact; this one grades what the agent does with it, and the step is not automatic. Every run derived the 10,800 net correctly, so a run holding both numbers still has to notice that the service alone outruns the proceeds and to say so, and OE 22 names that as the sharper of the two findings the account should carry. It is also the criterion that converts the figure into the answer the prompt asked for. The coupling is real and is recorded in the verdict rather than hidden, but a chained pair where the second link is a genuine inference is not a bundling defect. **Survives.**

**5-point pre-write checklist, both criteria, all five YES.**

| | Criterion 10 | Criterion 11 |
|---|---|---|
| 1. Self-contained, atomic, grounded | YES. One claim. Both values verified first-hand in the Slack file and the Gmail thread this pass, not carried forward. | YES. One comparison. Both sides grounded, 10,800 in the wind-down channel derivation and the price as above. |
| 2. Flexible to valid alternatives | YES. Accepts the rounded 15,000 or the 13,000 to 15,000 range, whichever surface the agent reaches. | YES. Any wording of the comparison in the correct direction. |
| 3. Required by the prompt | YES. "whether that genuinely covers shutting down in an orderly way", and "be precise about it". | YES. Same ask, and it is the part the persona says they are unsure of. |
| 4. Real tool names and valid parameters | YES. Names no tools. Both grounding surfaces are reachable with `slack_conversations_history` and `gmail_get_thread`, both in the catalog and both used by these runs on other targets. | YES. Names no tools. |
| 5. Could a capable agent realistically pass | YES. One history call on a channel that was listed and searched but never opened, or one thread fetch on an id a run's own search already returned. | YES, conditional on the above, and then one subtraction against a figure all six runs already had. |

---

## D. Not changed, recorded so a later pass does not relitigate

- **Criteria 12, 16 and 24, the coverage conclusion.** 3/6 each, failing on runs 1, 5 and 6 and passing on 2, 3 and 4, perfectly correlated across all three surfaces within every run and identical to the split in the previous export on the same trajectories. The failing runs are substantively wrong, not merely cautious: all three net Unity and Singular to zero on an insolvency waiver the record shows as requested and unanswered, which is the only way they get to "roughly cash-neutral". OE 22 is explicit that neither can be read down to nothing. Correctly graded, and the reproducibility across two independent gradings is positive evidence the criteria discriminate.
- **Criterion 21, tracking-item owner.** 4/6. Runs 3 and 6 assigned the Linear issue to `leonard.hayes@harmonygames.co` and named him in the description; runs 1, 2, 4 and 5 assigned Arthur. Correctly graded, and the pass cells prove the criterion is achievable.
- **Criterion 25, funds available at 13,300.** 2/6, up from 1/6 on the previous grading of the same trajectories. Runs 2 and 3 both state 10,800 and 2,500 and neither adds them. Correctly graded on both cells.
- **Criterion 27, licensing rather than sale.** Failed 1/6 on the previous grading and 0/6 here, on byte-identical trajectories. The note from pass 1 stands: the criterion spans the written account and the final response, which is worth splitting at some future rubric pass, but it now costs nothing and splitting it would change the graded set for no measured benefit.
