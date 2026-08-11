# Verification — PIPELINE HARDNESS — `2_6a6beba55996ad2ada369b15`

v16 cross-source verification. Universe **harmonygames**, persona **Robert** (Executive), universe today **2026-02-28**.

## Data sources consulted

- `_aux/Universe_Split/slack.2026-02.json` :: the active-window shard (3,081 messages, 2026-02-01 to 2026-02-13 19:58 UTC). Channel and author distributions computed; `#winddown` C0ADGSZKR3R read in full (212 messages); `#executives` C07C2866011 (459) and `#prototype` C09UHHN6PFZ (474) sampled at the tail. Eight cited timestamps re-read verbatim and confirmed present with the quoted text: `1770789534.434749`, `1770839322.836779`, `1770839688.408909`, `1770859981.856189`, `1770911000.728559`, `1770924424.711879`, `1770924465.624129`, `1770933601.686309`.
- `_aux/Universe_Split/slack.2026-01.json` :: prior-month shard (10,650 messages) used only to establish Robert's channel footprint and confirm `#winddown` did not exist before 02-09.
- `_aux/Universe_Split/slack.slack.channels.json` :: 985 channels; id-to-name resolution and `members[]` arrays. Confirmed Robert's `U04TWDMDT0V` membership in every channel the plan reads.
- `_aux/Universe_Split/snowflake.snowflake.tables.json` :: 33 tables enumerated. `FINANCE.EXPENSES.CASH_BALANCE`, `FINANCE.EXPENSES.MONTHLY_BURN` and `FINANCE.EXPENSES.HEADCOUNT` read in full including embedded rows.
- `_aux/Universe_Split/gsheets.gsheets.sheets_spreadsheets.json` :: 26 spreadsheets, ownership tallied.
- `_aux/Universe_Split/linear.linear.issues.json` (3,852) and `trello.trello.cards.json` (803) :: checked for activity in the 2026-01 / 2026-02 window. **Zero records in either.** Both remain valid write targets; neither can host a discovery lever.
- `_aux/Universe_Split/confluence.confluence.pages.json` :: 31 pages, titles enumerated.
- `_aux/Universe_Split/gdocs.gdocs.docs_documents.json` :: 67 documents, titles enumerated.
- `HarmonyGames_Base_Universe/Services_Data/gcal/` and `gslides/` :: `gcal.events.json`, `gcal.calendars.json` and `gslides.slides_presentations.json` are each 3 bytes (`[]`). Checked directly at the base export because the split contained no `gcal.*` or `gslides.*` files and the absence needed to be distinguished from a split defect.
- `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` :: 276 tools across 13 services. Write-capable tools enumerated per service; all 27 `gmail_*` tools listed individually.
- `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json` :: 17 personas. Robert's record read exactly.
- `_aux/Fact_Ledger.json` :: persona and alias surface. Confirmed `robert@harmonygames.co` -> `Robert`, `is_user` true, `contact_id 5f647df33ba6e92fbd56b05b`. Confirmed the irregular-email landmine in the alias map and the first-name collisions relevant to near-miss work (marcus, claire, thomas, brian, victor, megan all resolve to two identities).
- `_aux/Universe_Index/today_horizon.json` :: universe today 2026-02-28 America/Chicago; zero records dated after today.
- `_aux/Universe_Index/graph_report.md`, `key_facts.md`, `entities_personas.md`, `accounts_per_entity.md` :: consulted and found largely empty. The generator is Brookfield-shaped, so the JE-density, BlackLine, AP-vendor and Records-Vault sections have no HarmonyGames counterpart. Only the Slack-id mention ranking was usable. Lever evidence therefore comes from direct split reads.
- `_aux/Universe_Index/service_inventory.md` :: per-source record counts, used to scope the survey.
- `3_UniverseDataForThisTask.json`, `4_Changelog.json`, `9_Universe_inject.sql` :: read to establish injection posture. Descriptor, `[]`, and comment-only template respectively.

Source categories consulted in this phase:

- **Per-task data** :: `_aux/Universe_Split/` (slack 2026-01 and 2026-02 shards, slack.channels, snowflake.tables, gsheets, linear, trello, confluence, gdocs), `_aux/Fact_Ledger.json`, `_aux/Universe_Index/`, `3_UniverseDataForThisTask.json`, `4_Changelog.json`, `9_Universe_inject.sql`.
- **Eval spec** :: `Evals_harmonygames/` trajectory sub-dims for Tool Call Count, Agent Failure Rate and Error Rate, plus the Prompt sub-dims for Tool use and Cross-service requirement and for Feasibility with Tools. Applied as the density triple, the pass@1 <= 40% target, and the two binary prompt gates recorded below.
- **QC spec** :: `Docs_harmonygames/7_QC_Spec_Doc1.json` density and coherence sub-dims, and `Docs_harmonygames/14_Persona_ACL.md` as the authority for persona-scoped reads. Applied as the 40+ authoring target with a >=15 trajectory floor, the binary Universe Cross-service Coherence check, and the read-feasibility confirmations.

## Reference docs consulted

- `Reference/Hardness_Playbook.md` :: all 11 levers considered and scored in the plan's availability table. **Selected: L11 net-vs-gross, L2 structured-source skip, L8 multi-link chain, L10 reversal/supersession, L7 multi-write.** Marked partial and not selected: L3 missing reply, L4 search-cap eviction, L5 thread-reply blindness, L9 universe-grounded gotcha. Marked available but flavour-only: L1 latching (subsumed into L11's framing), L6 near-miss.
- `Reference/Sessions/HARDNESS.md` :: phase contract, the six required plan sections, the service-breadth table, and the framework-scoped density note.
- `Tasks/_meta/Learnings.md` :: read end to end. Entries cited as lever rationale in the plan: **L2** (single-hop reductions pass ~80%, the basis for promoting L8 and rejecting a bare subtraction), **L5** (writes drive density, not stumping), **L6** (answer must never appear verbatim), **L8** (stack across structurally different systems), **L10 and L11 of the Learnings numbering** (structured-source invisibility, structured-vs-conversation skip), **L12** (thread and supersession invisibility), **L13** (first-framing anchor), **L16** (persona believes the wrong number), **L18** (the figure is the rubric), **L19** (cascade rubrics), **L31** (considered and explicitly rejected as single-model-inapplicable), **L33 Rule 1 and Rule 4** (design for margin; carry levers on created artifacts), **L36** (difficulty is withheld inference — every selected lever carries a withhold clause).
- `AGENTS.md` :: HarmonyGames universe constants, the 13-service list, the landmine set, hard rules 2, 13, 32, 33 and 36, and deviation HG-U11.
- `Docs_harmonygames/14_Persona_ACL.md` :: the access matrix. Confirmed seven persona-scoped read services and the six-member unscoped public-service group, and that ACL does not govern writes.

## Eval spec sub-dims relevant to this phase

- Trajectory `Tool Call Count` :: HarmonyGames carries three normatively separate thresholds. Projected total midpoint **47.0** against the 40+ authoring target; **~28 necessary calls** against the >15 prompt-eval hard gate; both against the >=15 trajectory floor. `set_acting_user`, ACL-denied reads and inaccessible retries excluded from all three counts.
- Trajectory `Agent Failure Rate` :: pass@1 target <= 40%. The selected anatomy pairs a symmetric structured-source stump with a derived figure absent from the universe, which is the single-model recipe for that band.
- Prompt `Tool use and Cross-service requirement` (binary) :: 8 distinct services projected, dominant service ~30%.
- Prompt `Feasibility with Tools` (binary) :: the Gmail send-tool absence and persona ACL readability were both verified rather than assumed, because a violation here is a task defect rather than a model miss.

## QC spec sub-dims relevant to this phase

- Trajectory `Tool Call Count` :: projected midpoint 47.0. Band under the HarmonyGames scheme (>= 40 PASS · 15-39 THIN · < 15 INSUFFICIENT) is **PASS**.
- Universe `Cross-service Coherence` (binary) :: one contradiction surfaced and recorded rather than built upon, see the discrepancies below. It is only a failure if it causes an agent failure, so the plan instructs S2 not to make it load-bearing.
- Universe `Feasibility` (binary) :: zero injection required; every lever grounded in present data.

## Verification statements

- [x] At least 3 levers selected; each cites a Learnings entry. **Five selected**, each with a Learnings citation and an explicit withhold clause per L36.
- [x] Density midpoint projection stated with its band. **47.0 -> PASS.** Note the runbook template's `{PASS >= 50, THIN 40-49, INSUFFICIENT < 40}` triple is the **V3-family** scheme and does not apply here; the HarmonyGames scheme (>= 40 PASS · 15-39 THIN · < 15 INSUFFICIENT) was used, per the framework-scoped note in the runbook and playbook.
- [x] Service breadth table populated (v11 G1). Eight distinct services, seven at or above 5%, dominant service ~30%.
- [x] Every evidence pointer produced by the delegated scan was independently re-read against the split before adoption. Eight Slack timestamps confirmed verbatim; the Snowflake FINANCE tables confirmed to exist with embedded rows; the GSheets ownership claim confirmed.

## Discrepancies surfaced

1. **`MONTHLY_BURN` and `CASH_BALANCE` disagree for February 2026.** The `MONTHLY_BURN` category rows for `2026-02-01` sum to $20,000 (salaries 4,000 + contractor_fees 500 + aws_hosting 500 + legal 13,000 + tools_software 500 + other 1,500), while `CASH_BALANCE` for `2026-02-28` records `monthly_net_burn = 22500`. A $2,500 gap with no stated reconciliation. Recorded, not built upon; the plan instructs S2 to keep burn reconciliation off the load-bearing path.
2. **A numeric collision on `22500`.** The data cash offer in Slack and the February `monthly_net_burn` in Snowflake are the same number in two unrelated roles. Usable as a near-miss lever but a rubric hazard; the plan requires S3 to bind the figure to its role rather than grade the bare token.
3. **Robert's department differs between sources.** `4_Persona_ACL_Roster.json` records `department: Executive`; Snowflake `FINANCE.EXPENSES.HEADCOUNT` records `EMPLOYEE_0016` as `department: product`. The roster is authoritative for persona identity and matches the task's assigned business function. Noted so that no artifact cites the Snowflake value as Robert's function.
4. **The sub-agent's L11 confidence was overstated as specified.** It proposed a single subtraction at [HIGH]; Learnings L2 rates single-hop reductions at roughly 80% pass. Corrected in the plan by promoting L8 multi-link chain to a selected lever so the figure sits inside a three-service chain rather than standing alone.
5. **A `$12K` variant of the `$11,700` charge exists in DM `D04UC0UEN2V`**, a conversation Robert is not party to. Invisible under persona-scoped Slack reads, so it cannot poison the derivation, but S2 must not cite it as reachable and S3 must not accept `$10,500` as an alternate net.
6. **SVB debt is referenced three times and never quantified.** A full obligation reconciliation would be ungradeable; the plan anchors the chain on net proceeds plus cash on hand versus named open obligations instead.
7. **Fifteen-day staleness gap.** Last Slack message 2026-02-13 19:58 UTC against a universe today of 2026-02-28. `today_horizon.json` reports a last-event timestamp of 2026-02-22 sourced from a non-Slack service. S1 must frame the ask as "where did we land", not as fresh news.
8. **The S0 Universe_Index is structurally inapplicable to this universe.** `key_facts.md`, `entities_personas.md` and `accounts_per_entity.md` are empty and `graph_report.md` has only one populated section, because the generator emits Brookfield-shaped sections. Not a data gap and not blocking for this phase, but worth noting as a standing limitation for any HarmonyGames task.
9. **Channel-membership evidence was re-derived after a banked warning.** The delegated scan established Robert's read access from Slack `members[]` arrays. `Tasks/_meta/Hardness_Patterns_Log.md` (2026-08-06, Task 2 HG) records that HarmonyGames `members[]` arrays are unusable as membership evidence: the export tokenised 100 of 218 Slack users and never re-tokenised the arrays, so `#executives` reports `num_members: 3` while carrying tens of thousands of messages from tokenised employees. The conclusion is unchanged but the evidence has been replaced with **authorship counts**, which prove membership because a non-member cannot post. Robert authored 21 messages in `#winddown`, 132 in `#executives` and 136 in `#prototype` in the February shard, and 583 / 720 respectively in January.
10. **A prior S1 pass on this task used a different spine.** `Tasks/_meta/Hardness_Patterns_Log.md` carries an entry dated 2026-08-06 headed "Task 2 HG (Combo Fighter post-mortem, S1)" describing a Hardness Brief and prompt for this task index. No `5_Prompt.txt` and no prior `Hardness_Plan.md` exist in the task directory, and `Generated_Tasks/` is untracked by git so there is no history to recover. Surfaced to the operator as an open question rather than resolved unilaterally, because the spine choice materially changes every downstream artifact.

## Verdict

**PASS.** Five levers selected against a minimum of three, each citing a Learnings entry and carrying an explicit withhold clause. Density midpoint 47.0 against the HarmonyGames 40+ authoring target, with ~28 necessary calls against the >15 prompt-eval gate and a >=15 trajectory floor. Service breadth 8 distinct services, seven at or above 5%, dominant service ~30%. Zero injection required. Every evidence pointer produced by the delegated scan was independently re-read against the split before adoption, and one class of evidence (channel membership) was re-derived after a banked warning invalidated the method the scan used.

One item is referred to the operator rather than decided here: discrepancy 10, the prior S1 pass on a different spine.
