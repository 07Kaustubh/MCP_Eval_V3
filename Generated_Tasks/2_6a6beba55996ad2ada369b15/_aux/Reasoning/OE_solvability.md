# OE Solvability — S2 (`2_6a6beba55996ad2ada369b15`)

Universe **harmonygames** (framework `hg`) · persona **Robert** · business function **Executive** · universe today **2026-02-28** · model under test **Claude Opus 4.7** · deliverable `6_Oracle_Events.txt`, 23 steps.

## The spine in one paragraph

Robert owned Combo Fighter's design, and the shutdown letter names Combo Fighter's data as the reason the company is closing. He wants the actual record written down before the accounts go dark. Querying it yields an unusually clean result: the title earned **0.00** across its entire life against **7,483.42** of paid acquisition, while its engagement numbers were genuinely good. Pulling that thread exposes the second finding, which nobody has looked for: the performance tables stop on 2026-02-09 but the spend table does not, and paid acquisition has kept charging every day since, **8,452.64** across all three titles, **346.00** of it dated today. That figure is roughly 78 percent of the **10,800** net the data deal actually produces. The third question, whether the deal funds an orderly shutdown, then answers itself starkly: **13,300** of available funds against roughly **41,000** of named vendor obligations before SVB, so the persona's standing belief is wrong by a wide margin rather than narrowly.

## Forward map: every prompt sentence to at least one OE step

| Prompt paragraph | Ask | OE steps |
|---|---|---|
| 1 | Context: Leonard's angel calls, Robert's ownership of the design, "somebody should write down what the data actually said" | OE 1, OE 2 (orientation and the shutdown decision), carried into OE 20 |
| 2 | "Go back to the real numbers for the whole life of that game, from its first day with players to the last day there is anything to look at" | OE 3, OE 4 (2026-01-05 to 2026-02-09, 36 dates), OE 9 (the two ranges differ by table) |
| 2 | "work out how it genuinely performed" | OE 4 (DAU peak 801, 845 new users, 55,101 sessions, D1 44.0 / D7 22.1 / D30 11.0), OE 5 (0.00 revenue), OE 6 (zero IAP corroboration) |
| 2 | "and what we paid to put players in front of it" | OE 8 (7,483.42 across six channels, 1,341 installs) |
| 2 | "Some of that will read better than I expect and some worse, so don't smooth it out" | OE 4 explicitly requires the strong retention figures be reported unsoftened; OE 5 requires the zero |
| 3 | "find out whether anything is still quietly running on our side" | OE 9, OE 10 |
| 3 | "We decided to stop on the ninth" | OE 2 (ts 1770664094.831769) |
| 3 | "that list got put together fast and nobody has been back over it properly" | OE 13 (the consolidated action list does not contain paid UA) |
| 3 | "Whatever is still taking money from us needs naming with a figure against it" | OE 10 (8,452.64), OE 11 (still live today at 346.00) |
| 3 | "and an owner" | OE 12 (Leonard Hayes, by ad-account control) |
| 4 | "I know roughly what we are getting for the data" | OE 14 (22,500 gross, 11,700 charge, 10,800 derived), OE 15 (restructured to a licence, cash unchanged) |
| 4 | "and I know who we still owe" | OE 16 (Singular 18,750; Unity roughly 21,000; Helpshift 1,200; SVB named and unquantified) |
| 4 | "I know roughly what we are getting" (what is NOT coming in) | OE 16a (the 24,275 R&D credit, superseded to a non-cash carried-forward credit) |
| 4 | "whether that genuinely covers shutting down in an orderly way" (the cost of doing so) | OE 16b (Sunset wind down service, about 15,000) |
| 4 | "whether that genuinely covers shutting down in an orderly way. Tell me where that actually leaves us and be precise about it" | OE 17 (cash 2,500), OE 18 (the reconciliation and the verdict) |
| 5 | "Write it up as one honest account ... somewhere it will outlast our accounts going dark" | OE 20 |
| 5 | "Then post it to him and Arthur in the wind down channel" | OE 19 (resolve both), OE 21 |
| 5 | "and file a tracking item for whatever is still costing us" | OE 22 |
| 6 | "Then tell me the two or three figures you would lead with" | OE 23 |

## Reverse map: no OE step exceeds a prompt ask

Every one of the 23 steps traces to a row above. The three steps that are not literal prompt sentences are OE 3 (warehouse enumeration, a precondition for OE 4 to OE 8 and OE 17), OE 7 (the versioned-mart decoy, a precondition for not misreading OE 5 and OE 8 as absent data), and OE 9 (the range comparison, the causal bridge from paragraph 2 to paragraph 3). Each is a discovery precondition rather than an added requirement, and none carries a rubric of its own.

## OE-to-rubric preview for S3

| OE | Becomes |
|---|---|
| OE 1 to OE 19, including OE 16a and OE 16b | Pure discovery. No criterion. The downstream Outcome criteria prove the reads happened. **OE 16a in particular must NOT become a criterion** (see directive 11). |
| OE 20 | **Outcome 1.1** durable account created · **Outcome 1.2** one criterion per content element in its decompose directive (10 elements listed) |
| OE 21 | **Outcome 1.1** post made to the wind down channel · **Outcome 1.2** per content element (4 listed) |
| OE 22 | **Outcome 1.1** tracking item created · **Outcome 1.2** per content element (4 listed) |
| OE 23 | **Outcome 2.1** the lead figures given in the final response (2 elements listed) |
| Ordering clause | **Process**, one criterion, durable account before the channel post. Required by AGENTS.md rule 23; both councils independently directed it. Phrase so any valid path passes. |

That is roughly 23 criteria before decomposition judgement (OE 20's element list grew to 11 with the wind down service cost), well inside the 60 ceiling, which leaves budget for the ordering Process rubric that rule 23 requires and for the per-figure binding S1 carried forward.

## Directives S3 must carry (consolidated from S1 carry-forward and both councils)

1. Bind the tracking-item criterion to the still-running paid acquisition and the figure **8,452.64**, not to a kept-vendor list. Role-bind it, since the competing reachable readings are 2,444.08 (Combo Fighter only) and 8,922.12 (inclusive of 02-09).
2. Bind revenue to the unversioned `REVENUE_DAILY`. A criterion satisfiable from `REVENUE_DAILY_V2` would pass a run that concluded there is no Combo Fighter data at all.
3. Role-bind **22,500**. It collides exactly with `CASH_BALANCE.monthly_net_burn = 22500`, so grading it as a bare token mis-grades.
4. **Corrected after AUDIT F1.** Singular (18,750), Unity (roughly 21,000 across nine months) and Helpshift (1,200) ARE quantified, at ts `1770765511.243329` in #executives. Only SVB is unquantified. A criterion may therefore grade the coverage verdict against the named stack, but must NOT demand a closed total, because SVB remains open and Unity's figure is stated as an unlabelled rate. Do not carry the superseded Helpshift 1,500, and do not accept the 300 or 12K figures, which sit outside Robert's read scope.
5. Grade the durable account **relative to Slack**, not as a guarantee of permanence, and do not pin a surface. The records settle only the bottom of the ordering: Slack drops to the free tier with no history.
6. Keep the durable-account criteria and the Slack-post criteria unnested, so no single agent act satisfies both (AGENTS.md rule 17).
7. No criterion may date a communications write to 2026-02-28. Weekend-comms, enforced at `--phase submission_gate`.
8. One Process rubric for the ordering constraint (rule 23), path-agnostic, inside the 40 percent Process cap.
9. Keep the `MONTHLY_BURN` 20,000 against `CASH_BALANCE` 22,500 gap non-load-bearing. It is an unexplained cross-table disagreement and the binary Universe / Cross-service Coherence sub-dim penalises one that causes an agent failure.
11. **Do not create a negative criterion for the R&D credit.** OE 16a excludes the 24,275 from available funds, but a criterion phrased as the agent NOT including it is a negatively framed criterion, and HG QC dimension 23 makes that an outright FAIL unless the prompt mandates a prohibition. This prompt mandates none. Grade the coverage verdict affirmatively on the figures that ARE available (10,800 plus 2,500); an account that wrongly adds the credit fails that criterion on its arithmetic without any criterion ever naming the credit.
12. **The sharpest single criterion available is the net-vs-gross one.** The wind down service costs about 15,000, which sits below the 22,500 gross offer and above the 10,800 net. Leonard's own line, "the cost of Sunset is about ~$15K, the data will likely cover our costs", is true against the gross and false against the net. A criterion binding the account to the net rather than the gross discriminates the primary stump directly.
13. Do not build a criterion on the January campaign-pause thread. Slack records campaigns paused on 2026-01-11 while `AD_SPEND_DAILY` shows uninterrupted spend, and nothing in the prompt requires that be reconciled.

## Density

Re-derived for the shipped combined spine, not inherited from the Hardness Plan, whose 47.0 midpoint and 8-service table were computed for the superseded wind-down-only spine.

| Band | Value |
|---|---|
| Projected total | 37 to 50, midpoint about 43 |
| Necessary-call subtotal | about 26 to 30 |
| Distinct services on the necessary path | 5 (slack, snowflake, confluence or gdocs, linear or trello, contacts) |

Against the HarmonyGames scheme, midpoint 43 clears the 40 authoring target, the necessary subtotal clears the prompt gate of more than 15, and both clear the trajectory floor of 15 average with wide margin. The V3-family 50/40 bands do not apply here and were explicitly excluded from both council briefs and the AUDIT brief.

## AUDIT

**Round 1: `VERDICT: REVISE`** on one MAJOR finding, applied in place.

**F1 (MAJOR, confirmed independently before acting).** OE 16 and OE 18 asserted that the Unity and Singular obligations are quantified nowhere and that the universe contains no liabilities total. Both claims were false. `slack.2026-02.json` ts `1770765511.243329`, channel `C07C2866011` (#executives), Leonard Hayes: "We have to pay to Singular ($18750), Unity (~2.348*9 months), and Helpshift ($150*8 months)". Robert authored 130 February messages in #executives, so it is inside his persona read scope, and OE 12 already reads that channel. **Root cause: both councils swept only #winddown.** No deterministic gate covers a cross-channel false-absence claim, which is precisely the residue AUDIT exists to catch. Spine impact: the coverage verdict was mis-weighted, treating the 8,452.64 ad leak as the dominant variable when the vendor stack is roughly five times larger. Fixed in OE 16, OE 18 and OE 20's decompose directive.

**F2 (MINOR).** OE 7 attributed "Excludes Combo Fighter prototype monetization" to `calc_metadata`; that sentence is the `REVENUE_DAILY_V2` table comment, while `excludes_prototype: true` is the calc_metadata field. Locations were conflated. Fixed.

**F3 (MINOR).** OE 2 characterised ts `1770664094.831769` as opening with the "After reviewing..." sentence; the message is a pasted email draft whose own first line is the salutation. Fixed.

AUDIT confirmed everything else held: all 33-table Snowflake figures and all 13 cited Slack timestamps re-derived EXACT, deterministic floor green (89/89 anchors), density midpoint 42 to 43 against the HG 40 target, all five levers exercised, coverage sound both directions. It agreed the 8,452.64 versus 2,444.08 scope question is advisory rather than a Unique Ground Truth block.

**Round 2: `VERDICT: REVISE`** on one MINOR. OE 16's "SVB is the only named obligation that no reachable record quantifies" was strictly false: ts `1770836625.652859` in #executives is an unquantified fundraising-advisor settlement. Fixed by scoping the absolute to vendor obligations and naming the settlement as corroboration that carries no criterion. AUDIT independently rebuilt Robert's reachable channel set and swept all 20 channels including the high-volume DMs, found no further omitted figure, and confirmed the REBUILD signal correctly did not fire.

**Round 3: `VERDICT: PASS (STRICT)`.** The narrowed absolute verifies true over the closed vendor set, the new clause is existential rather than exhaustive so it cannot fail the same way, it seeds no rubric carrier and poses no HG dimension 23 negative-criterion risk, and OE 18 and OE 20 are unaffected. Density 43 midpoint across 5 services, all five levers trace, coverage holds both directions.

## Council outcome

Council A **GO** (round 3). Council B **GO** (round 3), having explicitly withdrawn both its round-2 central finding and its `PROPAGATE TO S1/HARDNESS`, on the record rather than on argument.

## What the three rounds cost, and what closed the loop

Three REVISE rounds were consumed against a cap of 3. Every one turned on the same defect class: a claim that some figure is stated nowhere, tested against too small a set of channels. Round 1 councils both returned GO on a MAJOR instance of it. The class only closed when the sweep was given an explicit denominator, the persona-authorship map, which surfaced that no earlier round had opened the DMs Robert is a party to (792, 438 and 131 messages). No deterministic gate covers a cross-channel false-absence claim; `Validators/check_rubric_antipatterns.py` and the `--phase oe` validator both pass a file containing one. Per AGENTS.md rule 18 this is the shape of finding that should become a standing gate rather than prose, and it is recorded in `_aux/Verification_s2.md` discrepancy 9 for that purpose.
