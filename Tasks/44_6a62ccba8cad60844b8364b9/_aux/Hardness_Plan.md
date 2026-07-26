# Hardness Plan

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** `starpm` (Star Property Management, LLC) · **Framework:** V4 (dual-model: Opus 4.8 + Gemini)
**Universe today:** 2026-07-01 (America/Chicago) · **Density scheme:** StarPM v4 — >= 40 midpoint PASS · 15-39 THIN · < 15 INSUFFICIENT, applied PER MODEL. The V3-family 50/40 bands do NOT apply.
**Mode:** fresh CB build. Neither `_aux/REDO_reason.md` nor `_aux/Candidate_Originals/` exists, so there is no prior-attempt lever set to differ from.

## Persona and Business Function

- **Jaime Salinas** (Quality Control Inspector) · `p_007` · `jaime.salinas@starpm.com` · Mid seniority, Portfolio Operations.
- **Business function:** 3 · Quality Control & Field Services.
- Scripted footprint is thin by design (7 actions / 7 scenarios, leads none; 15th by artifact density at 48 mentions). Per the S0 graph-report note, levers are built on the **surface she signs off on**, not on a Jaime-led scenario. Her role is the impartial QC eye: she walks work after maintenance declares it complete, validates it, and either signs off or kicks it back. That makes "does her own sign-off actually hold" the natural, in-role centre of gravity.

## Selected scenario (the surface the levers sit on)

The **Preventive Maintenance Push** — the portfolio-wide HVAC / plumbing / electrical audit Brooke Phillips kicked off on 2026-05-07 and set to close out "before the end of June". Today is 2026-07-01, so the close-out target has passed. Jaime is the QC anchor on it: she logged cluster spot-check passes in late May and her own notes say she moved her QC issues to Done.

The record does not support that. Six independent, separately-sourced facts contradict the closed-and-clean reading, and no single artifact states the aggregate conclusion.

| # | What the record actually shows | Where it lives | Service |
|---|---|---|---|
| 1 | **Not one Preventive-Maintenance-Push QC issue sits in a completed state.** OPS-87 = Todo, OPS-96 = Todo, OPS-98 = In Progress — while their own descriptions and comments say "moved both from In Review to Done" / "Moving this to In Review". OPS-108 = Backlog and OPS-44 = Backlog against the same pattern. | `linear.linear_issues.json` `state_id` field + `linear.linear_comments.json` | linear |
| 2 | **Jaime's own field note contradicts her own sign-off, one day earlier.** 2026-05-23: "north Cluster walk-throughs done. Two units need HVAC looked at right away, flagged on the Linear issue with coil, plumbing, and panel notes." Her OPS-87 (5/24) and OPS-98 (5/25) then say "everything came back clean across the board" / "No issues to flag on either side". No follow-up issue for those two units exists. | Slack C001 ts `1779562423.000092`; OPS-87 / OPS-98 + comments | slack + linear |
| 3 | **Two South-cluster holdovers were never closed.** OPS-43 (In Progress) plus its two comments: a condensate drain that needed extended flush, and a **no-access unit awaiting a reschedule with Carlos**. The reschedule ask exists only in Elias's Slack **thread replies** and OPS-56's comments ("second round of access notices to those two remaining tenants"). | OPS-43 / OPS-56 comments; Slack C001 replies ts `1779308444.000003` and `1779308445.000004` under parent `1779308442.000001` | linear + slack |
| 4 | **The filter run was never finished.** John Smith 2026-05-23: "the supply closet is almost out of 20x25 filters so we'll need a restock **before I can finish the run**"; Brooke's thread reply asks Elias for a stock count before a bulk order. Jaime's OPS-96 comment (5/30) nonetheless claims "a spot-check across **all units** this morning - filters look good across the board". | Slack C001 parent ts `1779567943.000011` + reply `1779569323.000012`; OPS-96 comment | slack + linear |
| 5 | **Jaime's QC coverage never included the West cluster.** Her three QC issues cover South, North and portfolio filters; East was covered via OPS-99 / OPS-108. West exists as its own scope (OPS-35, Lisa Smith onsite lead) and OPS-186 dated 2026-06-17 states "the **West Cluster work still underway**". Lisa was still asking on 5/27 whether coil cleaner and filters were stocked so she could "get HVAC knocked out across my properties this week" — five days after Elias declared all clusters done and two days after Jaime's sign-off. | OPS-35 / OPS-91 / OPS-186; Slack C001 ts `1779884437.000093` | linear + slack |
| 6 | **Carlos's plumbing findings are still open.** 2026-05-31: two water heaters past serviceable life plus hose bibs across units; OPS-97 comment says "Moving this to In Progress" but OPS-97 state = **Todo**. Brooke escalated it to a budget priority on 6/03 and the 6/02 calendar check-in agenda names "the budget implications of the water heater replacements Carlos flagged". | Slack C001 ts `1780256425.000094`; OPS-97 + comment; gcalendar 2026-06-02T16:45 | slack + linear + gcalendar |

Corroborating the same direction: Brooke's 2026-06-19 posts (ts `1781899601.000096` and near-duplicate `1781902061.000097`) — "two clusters are pretty much wrapped up, **one still in progress**. Goal is to close everything out before end of June."

**Answer-leakage check:** no artifact anywhere in the universe states the aggregate conclusion. Grepped `Universe_complete_data.json` for `qc sign-off does not`, `sign-off doesn`, `not actually done`, `never moved to done`, `still shows todo`, `cannot be closed`, `push cannot close`, `reopen the qc`, `qc was premature`, `premature sign`, `signed off too early` — all zero hits. The conclusion must be derived by aggregation across Linear structured state, Linear comments, Slack top-level posts, Slack thread replies and Calendar agendas. Satisfies Learnings L6 (HARD) and AGENTS.md pipeline-implications item 2.

## Levers Available

Full 11-lever scan against this task's `_aux/Universe_Split/`. Evidence is cited by split file plus record id or Slack `ts`.

| # | Lever | Status | Evidence in this task's universe | Cost range |
|---|---|---|---|---|
| 1 | **Latching** | **yes** | The loudest, most confident framing in the channel is Elias's wrap, Slack C001 ts `1779308446.000005` ("all three clusters are done. Every unit serviced") and its near-duplicate `1779308447.000006` ("Summer HVAC push is a wrap. All three clusters done, 34 units total serviced"). Contradicted by OPS-186 (West still underway), Lisa's 5/27 ask ts `1779884437.000093`, and Brooke's 6/19 "one still in progress" ts `1781899601.000096`. Elias's own scope issues OPS-16 / OPS-17 / OPS-18 name only three clusters while OPS-35 / OPS-91 / OPS-186 establish a fourth. | 5-8 |
| 2 | **Structured-DB skip** | **yes (strongest)** | The load-bearing fact lives only in the Linear `state_id` column: OPS-87 `state_OPS_1` (Todo), OPS-96 `state_OPS_1` (Todo), OPS-98 `state_OPS_2` (In Progress), OPS-97 `state_OPS_1` (Todo), OPS-108 `state_OPS_0` (Backlog), OPS-44 `state_OPS_0` (Backlog). Every prose surface says the opposite. Requires `list_issue_statuses` to even decode the ids. No email or Slack message mirrors the state values. | 4-7 |
| 3 | **Missing reply** | partial | OPS-56 comment asks Carlos for a second round of access notices to two remaining tenants; no reply or closing comment exists on that ask anywhere in the 48-comment corpus. Usable but the "absence" shape brushes against L7, so it is used as corroboration only, never as a load-bearing rubric. | 3-5 |
| 4 | **Search-result-cap eviction** | partial | An Airtable `search_records` on "HVAC" returns 20+ `tblMaintenanceTickets` rows, all on unrelated properties (Building C 304, Palomar 312, Pinecrest 12, Riverside, Oakdale). A QuickBooks HVAC keyword sweep returns 134 entities, none push-linked. The push signal is buried under high-traffic keyword noise. Not selected on its own per Playbook guidance. | 3-5 |
| 5 | **Thread-reply blindness** | **yes** | Two load-bearing facts exist ONLY in Slack thread replies: the South no-access reschedule (`1779308444.000003`, `1779308445.000004` under parent `1779308442.000001`) and the filter-stock block resolution (`1779569323.000012` under parent `1779567943.000011`). C001 carries 104 messages with 15 distinct parents. | 2-4 |
| 6 | **Near-miss entity confusion** | **yes (flavor)** | Duplicate-titled Linear issues in opposing states: OPS-99 (In Progress) vs OPS-108 (Backlog), identical title "East cluster HVAC service complete - QC passed"; OPS-51 (In Review) vs OPS-71 (Backlog), identical title. Near-miss vendors "Lone Star Maintenance Supply" vs "Lone Star Electric". Inverted pair OPS-91 (state Done, prose says "Moving this issue to In Progress"). Per L4 this is flavor, not a difficulty lever — carried but not counted. | 3-5 |
| 7 | **Multi-write diversification** | **yes** | Five distinct write services reachable and in-role for a QC inspector: `slack_send_message`, `linear.save_issue` (new follow-up issue + status correction), `linear.save_comment`, `gmail.create_draft`, `airtable.create_records_for_table`, `gcalendar.create_event`. Accounted for in the Write-actions row of the projection rather than double-counted as a lever. | 9-12 |
| 8 | **Multi-link chain** | **yes** | A -> B -> C, three hops with a different search strategy at each: (A) Jaime's 5/23 Slack note that two North units need HVAC right away and are "flagged on the Linear issue with coil, plumbing, and panel notes" — findable in a normal channel read; (B) the agent must work out WHICH Linear issue carries those notes across 20 push-adjacent issues; (C) the disposition — no follow-up issue was ever opened and her own QC issues logged the day after say "no deficiencies, no rework flagged". | 6-9 |
| 9 | **Universe-grounded gotcha / authority dismissal** | **yes** | The authority whose sign-off must be overridden is **the persona herself**. Jaime's OPS-98 comments (2026-05-25T09:00 and T14:00) read as a competent, domain-correct QC pass: "airflow was solid throughout, coils came back clean, and refrigerant levels looked correct on every unit I pulled. Everything cleared QC, so I've moved both cluster issues to Done." An agent acting on Jaime's behalf defers to her logged professional judgement. Reinforced by the universe-grounded trap that "moved to Done" is prose, not state. | 3-5 |
| 10 | **Reversal / supersession** | partial | OPS-91 (West cluster, state Done) is superseded in substance by OPS-186 (2026-06-17, West still underway); OPS-99 is superseded by the later-created OPS-108 on the same title in a lower state. Real but ambiguous in direction, so it is carried as a WATCH rather than selected — see the constraints section. | 4-6 |
| 11 | **Net-vs-gross framing** | **no** | This universe surface has no aggregate figure to net down. Elias's "34 units total serviced" is the only count and there is no per-unit roster to reconcile it against. Correctly dropped rather than manufactured — Playbook: if a lever has no backing data, drop it. | 4-7 |

**Levers present:** 7 yes / 3 partial / 1 no.

## Selected Levers (5)

Chosen for independence — each fires through a different mechanism, in a different service, discoverable by a different search strategy. No two are variants of the same latch.

- **Lever 2 — Structured-DB skip (Linear `state_id`).** The symmetric backbone. Projected cost **5.5**. Rationale: the entire "is the QC actually closed" question resolves in one structured column that no conversational surface mirrors, and decoding it needs a second call to `list_issue_statuses`. Cites **Learnings L2** ("agents skip structured databases"; "the strongest traps put the load-bearing answer in a system the agent has no conversational reason to query" — L11), **StarPM item 3** ("place the authoritative number in the object type the agent is least likely to query"), and **StarPM item 11** (structured-store-skip is the symmetric stump across both models).
- **Lever 9 — Authority dismissal, persona-self variant.** Projected cost **4.0**. Rationale: the wrong framing is authored by the person the agent is working for, in her own professional voice, with domain-correct QC vocabulary. Cites **Learnings L9** (authority-figure dismissal, most effective single mechanism), **L16** (persona believes the wrong thing), and **StarPM item 11** (owner/authority latching is Opus-selective).
- **Lever 1 — Latching on the loudest wrap.** Projected cost **6.5**. Rationale: Elias's "all three clusters are done / 34 units serviced" is the first and most confident completion claim an agent meets in C001, and it is posted a month before three later artifacts contradict it. Cites **Learnings L13** (first-framing anchor; needs 3+ structured contradictions to override) and **L25** (an existing artifact that superficially matches the requested state dominates the agent's read).
- **Lever 8 — Multi-link chain off Jaime's own field note.** Projected cost **7.5**. Rationale: three hops, each in a different store, with the terminal step being a judgement not a lookup — did the flag she raised ever get dispositioned. Cites **Learnings L8** (three reductions across three services is the target anatomy) and **L14** (correct observation, wrong conclusion).
- **Lever 5 — Thread-reply blindness.** Projected cost **3.0**. Rationale: two facts live only in replies inside a 104-message channel; cheap to plant, empirically ~40% miss. Cites **Learnings L12** (thread replies missed ~40% of the time; stack with other levers, never alone).

**Lever 7 (multi-write diversification)** is engineered into the ask across five services and is scored in the Write-actions row of the projection rather than counted a sixth time here. Levers 3, 4, 6 and 10 are present and will appear as corroboration and noise in the trajectory, but no rubric will be built to depend on them.

### Dual-model difficulty mix (V4 requirement)

Following the banked recipe in **Learnings item 11** — one symmetric stump plus two complementary asymmetric stumps:

| Role | Lever | Expected behaviour |
|---|---|---|
| **Symmetric** (guarantees neither model sweeps) | Lever 2, Linear `state_id` skip | Both families read the prose "moved to Done" and never check the column. |
| **Opus-selective** | Lever 9 + Lever 1 (persona self sign-off, Elias's wrap anchor) | Opus defers to the logged professional judgement of the persona it is acting for and to the loudest completion claim. |
| **Gemini-selective** | The retraction beat (**Learnings L31**) | Closing this out honestly requires an explicit negative directive to Brooke: the earlier QC pass does not hold and the push should not be treated as closeable yet. L31 records that Gemini names the blocker but frames it positively and never issues the prohibition — near-100% Gemini stump, trivial for Opus. It arises naturally here from the QC inspector's own kick-back authority, so it is not a bolt-on. |

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (channel + user + contact resolution, Airtable base/table/schema walk, Linear team + status enumeration) | 6-9 | 7.5 |
| Lever 2 — structured-DB skip (`list_issues` filtered passes, `get_issue` across the push set, `list_issue_statuses`) | 4-7 | 5.5 |
| Lever 9 — authority/self sign-off (re-read Jaime's own descriptions + comments on OPS-87 / OPS-96 / OPS-98, corroborate against field record) | 3-5 | 4.0 |
| Lever 1 — latching (cross-check Elias's wrap against OPS-186, Lisa's 5/27 ask, Brooke's 6/19 posts) | 5-8 | 6.5 |
| Lever 8 — multi-link chain (Jaime's note -> locate the carrying issue across 20 candidates -> comment walk -> disposition check) | 6-9 | 7.5 |
| Lever 5 — thread-reply blindness (`slack_read_thread` on 3-4 parents in C001) | 2-4 | 3.0 |
| Write actions (5 services, ~1.5 supporting reads each: Slack post, Linear issue + status, Linear comment, Gmail draft, Airtable ticket, Calendar event) | 12-16 | 14.0 |
| Cross-service triangulation buffer (Calendar check-in agendas, Airtable decoy sweep, Gmail sweep, QuickBooks noise sweep) | 6-9 | 7.5 |
| **TOTAL projected** | **44-67** | **55.5** |

**Gate (StarPM v4 bands, per model):** midpoint **55.5 >= 40 = PASS**. The low end of the range (44) also clears 40, so the projection does not depend on optimistic assumptions.

Calibration against shipped StarPM tasks: Task 40 averaged 40.0 and Task 41 measured 47 / 45 / 37 / 38 / 33 / 40. Those two were QuickBooks-figure tasks whose discovery converged on a handful of entities. This surface is Linear-state-heavy across roughly 20 push-adjacent issues with per-issue comment walks, which is structurally more call-hungry, so a 55.5 projection landing in the mid-40s on real runs is the realistic expectation for both models. Applied per model: Opus PASS, Gemini PASS.

**Under-count risk, stated honestly:** a strong agent can retrieve state for many issues in a single `list_issues` page rather than iterating `get_issue`, which would compress the Lever 2 row toward its low end. The projection already uses 5.5 rather than the Playbook maximum for that row, and the total clears 40 even if that row collapses to 1.

## Service Breadth (v11 G1)

StarPM service list per `Validators/universes.py`: airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack.

| Service | Calls | % of total |
|---|---:|---:|
| linear | 19 | 34% |
| slack | 14 | 25% |
| airtable | 7 | 13% |
| gcalendar | 6 | 11% |
| gmail | 6 | 11% |
| contacts | 3 | 5% |
| quickbooks | 1 | 2% |
| hubspot | 0 | 0% |
| **Distinct services** | **7 exercised, 6 at >= 5%** | — |

**Breadth gate: PASS.** Six services carry >= 5% of projected calls, against a threshold of four. The dominant service (linear at 34%) is well under the 60% single-service ceiling, so this is not the false-positive pattern where density is manufactured by stacking one service. The chain genuinely forces cross-correlation: the claim lives in Linear prose, the contradiction lives in the Linear `state` column, the field evidence lives in Slack top-level posts, two load-bearing details live only in Slack thread replies, the corroborating agenda lives in Calendar, and the write surface spans five services.

HubSpot is the leasing/deal funnel and has no linkage to the maintenance push; it is correctly at zero rather than padded.

### QuickBooks exclusion (deliberate, documented)

QuickBooks is exercised only as a noise sweep and no lever depends on it. Three reasons:

1. **`VendorRef.name` is unreliable in this universe.** Bills attributed to "Alamo HVAC Services" carry line descriptions for landscaping, legal review, lease-renewal fees and Tanya Mitchell's rent arrears; "Lone Star Maintenance Supply" bills carry rent and deposit lines. Any rubric grounded on vendor attribution here would be false-fail-prone — the exact failure mode recorded in **Learnings item 19**.
2. **The only push-relevant QuickBooks fact would be an absence.** There is no bill or purchase order for the 20x25 filter restock or the Lone Star bulk order. Building on that would make the correct answer "it is not there", which **Learnings L7** forbids outright.
3. **Similarity pivot.** Tasks 41, 42 and 43 all resolved to a QuickBooks dollar figure. Keeping this task's answer non-monetary is the primary lever for staying under the 40% platform-similarity ceiling.

## Stump Hypothesis (4 predictions)

1. **[HIGH] Both models will report the QC side of the push as complete-and-clean, or will name open field items while still treating the tracker as closed, because they never read the Linear `state` column.** Mechanism: Lever 2 (structured-DB skip), reinforced by Lever 9 (the persona's own logged sign-off) and Lever 1 (Elias's wrap). Reasoning: every prose surface an agent naturally reads — issue descriptions, issue comments, Slack posts — asserts "moved to Done" or "Moving this to In Review", while `state_id` says Todo / In Progress / Backlog on all six relevant issues. **Learnings L2 / L11** plus **StarPM item 3** put this class of skip near 0% find rate, and **StarPM item 11** establishes structured-store-skip as the symmetric stump that keeps both model families from sweeping. Expect this to be the highest-discrimination rubric in the set.

2. **[HIGH] Gemini runs will name the open items but will not issue the retraction — they will not tell Brooke that the earlier QC pass does not hold and that the push should not be treated as closeable.** Mechanism: **Learnings L31** (explicit negative directive omission). Reasoning: L31 documents a rubric requiring "not ready, should not be marketed or shown" failing 6/6 Gemini and passing 6/6 Opus, with every Gemini post framing the state positively while naming the blocker. Walking back one's own prior sign-off is the same shape. Expect near-100% Gemini failure and near-0% Opus failure on the retraction criterion — a legitimate cross-model gap (Bucket 3), with the Opus passes serving as the achievability proof.

3. **[MED] Runs will miss the South-cluster no-access unit and the unfinished filter run, because both resolve only inside Slack thread replies.** Mechanism: Lever 5 (thread-reply blindness) stacked on Lever 8 (multi-link chain). Reasoning: **Learnings L12** puts thread-reply miss rate near 40%; C001 carries 104 messages across 15 parents, so a channel read returns the parents and an agent has to elect to open each thread. The filter-run gap is the sharper of the two because it directly falsifies Jaime's "all units" claim in OPS-96 — an agent that misses it has no basis to question that issue at all.

4. **[MED] Runs will overlook that Jaime's spot-check coverage never included the West cluster, and will treat "South, North, East all passed" as portfolio-wide coverage.** Mechanism: Lever 1 (latching) plus Lever 8 (the cluster-set is inconsistent across services). Reasoning: Elias's scope issues OPS-16 / OPS-17 / OPS-18 name three clusters, so an agent that anchors on the HVAC scope will read three-of-three as complete coverage and never notice that OPS-35, OPS-91 and OPS-186 establish a fourth that Jaime never walked. This is **Learnings L13** anchoring on a set definition rather than on a figure. Confidence held at MED rather than HIGH because a systematic agent that enumerates issues by project may stumble onto OPS-35 early.

**Pre-registered lever re-attribution** (per **StarPM item 20** — write the prediction now so S4 calibration is honest rather than retrofitted): if runs DO read the `state` column and still conclude the push is closeable, score that as Lever 9 firing (deference to the persona's sign-off), not Lever 2 failing. If runs surface the West-coverage gap but not the state contradiction, Lever 1 fired and Lever 2 did not. If a run reaches the open items via Slack alone and never opens Linear at all, that is Lever 2 firing at maximum strength and Lever 8's hop B should be re-scored as unobserved rather than passed.

## Hardness Score

**5/5 — PASS.**

- Levers: 5 selected, each citing a Learnings entry. Threshold is 3. **PASS.**
- Density: projected midpoint **55.5**, low end 44, against the StarPM v4 design target of 40 per model. **PASS** (not THIN, not INSUFFICIENT).
- Breadth: 6 services at >= 5%, dominant service 34%. **PASS.**

## Constraints carried forward to S1 / S2 / S3 (pre-registered, not deferred)

These are AGENTS.md hard rule 13 and `Evals_starpm/5` F7 / F8 / F9 applied at design time, because **Learnings items 13-16** record that Task 39 shipped a QC failure precisely by deferring these to human judgement downstream.

1. **F7 AMBIGUOUS_TARGET — the live risk on this task.** Jaime owns **three** QC issues on this push (OPS-87, OPS-96, OPS-98) plus two near-duplicates she is named in but does not own (OPS-99, OPS-108). No rubric may pin one issue id while the prompt names the target only by entity ("her cluster QC issue"). Two permitted routes: grade on **content** rather than record id (the fix that empirically worked in **StarPM items 5 and 7**), or scope the ask to writes that are **unique by construction** — a new Linear issue, a new Airtable ticket, a new Calendar event, a Gmail draft to a named recipient, a Slack post to the channel the push runs in. Prefer the second.
2. **F8 NON_ATOMIC_ENUM.** Six open items are available. Do NOT write one criterion enumerating three or more of them under a completeness predicate. Decompose per item, and split any criterion whose two facts come from different records — **StarPM item 5** records exactly this defect surviving S3, AUDIT and FINAL on Task 40, and **item 7** records the split fixing grading accuracy with pass@1 unchanged.
3. **F9 UNRECONCILED_FUTURE_EVT — swept and clean, with two named watch items.** All 565 calendar rows were read. There are 9 unique confirmed events dated on or after 2026-07-01 and **none touches the Preventive Maintenance Push, the HVAC clusters, or Jaime** (zero future events mention her). The push chain is therefore F9-clean. Two adjacent events must still not be contradicted: **2026-07-15 Make-Ready QC Inspection - Mesa Vista 4C** (a future QC inspection in Jaime's function, attendees Carlos / Brooke / Wesley) and **2026-07-23 Q3 Make-Ready Planning & Budget Review**. Consequence: no deliverable may claim Jaime's QC queue is otherwise clear, and no deliverable may claim the maintenance-budget question is fully settled.
4. **Gmail bodies are base64 and agents do not decode them** (**Learnings item 17**, 0 of 12 runs decoded on Task 43). The `snippet` field is the only plaintext and it truncates near 200 characters. No rubric may depend on a fact reachable only inside an email body. This task is naturally safe — the entire chain is Linear, Slack, Airtable and Calendar — but the Gmail **write** (draft to Brooke) must stay a deliverable, never a source.
5. **Channel-lock-in is Major by default** per the AGENTS.md deviations table. The push runs in Slack C001 while Jaime's habitual channel per her brief is C004. The prompt must name the destination descriptively ("where the push has been getting tracked"), never by tool or id, and the rubric must either accept the equivalent path or the OE must pin the channel explicitly.
6. **Do not build a rubric on OPS-91.** Its `state` is Done while its own description says "Moving this issue to In Progress" — an inverted pair. The defensible West-cluster claim is the one grounded in Jaime's own three issues (her spot-checks never covered West) plus OPS-186's later dated statement, not any assertion about whether West HVAC work is itself finished.
7. **Do not build a rubric on an absence.** No restock bill, no follow-up issue for the two North units, no reply on the OPS-56 access-notice ask — all true, all forbidden as load-bearing answers per **Learnings L7**. They are corroboration only.
7a. **Scope the state claim to Jaime's QC issues, never to the whole push.** Two push issues DO sit in Done: OPS-40 "Preventive Maintenance Push - North Cluster Properties" and OPS-91 "HVAC condenser cleaning and filter replacements - West Cluster". The verified, defensible claim is narrower: **none of Jaime's three QC issues (OPS-87 Todo, OPS-96 Todo, OPS-98 In Progress) is in a completed state**, and OPS-97, OPS-108 and OPS-44 show the same prose-versus-state pattern. A rubric or OE that says "nothing on the push is closed" is falsifiable from OPS-40 and OPS-91 and would be the Task 39 overclaim failure repeated. This is the single most important wording constraint on the phase.
8. **Soft verbs on the prompt-side authority anchor** (**Learnings L24**). Phrase Jaime's belief as what she logged and how she reads it ("I logged both cluster spot-checks as passing and my read is my QC side is done"), which is literally true of OPS-87 / OPS-96 / OPS-98, rather than as a hard completed-action assertion about the initiative. This preserves Lever 9 while keeping Truthfulness at 5.
9. **No escape-valve clause pointing at the load-bearing surface** (**Learnings L29**, reconfirmed from the other direction by **item 20**). A sentence inviting the agent to surface contradictions would neutralise Lever 2 on exactly the column the task turns on. If persona realism needs a hedge, point it at a non-load-bearing surface.
10. **Similarity pivot must hold.** Tasks 39 and 40 were single-unit make-ready closeouts; 41, 42 and 43 resolved to QuickBooks dollar figures. This task is portfolio-scope rather than unit-scope, its answer is a coverage-and-closure ledger rather than an amount, its primary store is Linear rather than QuickBooks, and its persona is the QC Inspector rather than a PM or supervisor. S1 must still run `calc_similarity.py` and confirm under 40%.

## Naive-agent simulation (rule 13, run at design time)

Reading the intended scenario with the oracle out of view: a competent agent lands in Slack C001, reads Elias's "all three clusters are done, 34 units serviced", reads Jaime's own OPS-98 comment saying everything cleared QC and both issues moved to Done, and concludes the QC side is complete. It then writes a clean sign-off to Brooke. Nothing in that path is unreasonable, which is the point — the derivation that overturns it requires electing to read a structured column that no conversational surface mentions. No alternate valid target competes for the write actions as long as the S1/S3 constraints above are honoured, because every projected write is unique by construction.

## Hardness Brief for the Prompt Writer

Write for **Jaime Salinas, Quality Control Inspector**, in her voice: short, factual, observation-first, verbosity 0.30, no emoji, formality 0.55. The ask is to close out **her QC side of the Preventive Maintenance Push** — the portfolio-wide HVAC, plumbing and electrical audit that was supposed to be wrapped by the end of June, which has now passed. She should believe her part is done and say so with soft verbs: she logged both cluster spot-checks as passing back in late May, her read is her QC work is finished, and she wants the record squared and the supervisor told so the initiative can close. **Give no hint that anything is wrong, and include no escape-valve sentence inviting the agent to look for contradictions** — that clause would neutralise the task's load-bearing lever. Frame it as execution, not investigation.

The five selected levers are **Lever 2 structured-DB skip** on the Linear workflow-state column (the symmetric backbone: every prose surface says the QC issues moved to Done, the column says Todo / In Progress / Backlog), **Lever 9 authority dismissal in its persona-self variant** (the wrong framing is Jaime's own competently-worded QC sign-off, which an agent working for her will defer to), **Lever 1 latching** on the loudest completion claim in the channel (the lead technician's "all three clusters are done, 34 units serviced", contradicted a month later by three separate artifacts), **Lever 8 multi-link chain** off Jaime's own field note that two units needed HVAC attention right away and were flagged on a Linear issue (locate which issue, then determine whether the flag was ever dispositioned — it was not), and **Lever 5 thread-reply blindness** (the South no-access reschedule and the filter-restock block that stopped the filter run both live only in Slack thread replies). Ask for writes across **five services** — a status post in the channel where the push has been tracked, a Linear follow-up for the open work plus a correction on her own QC record, a comment on that record, a draft to the supervisor, an Airtable ticket for the flagged units, and a calendar slot for the re-inspection — naming none of them by tool or id. Target **55 projected tool calls, 40+ measured average per model**, across six services with Linear under 35% of the total. Include a beat that requires Jaime to **explicitly walk back her earlier pass** — state plainly that the sign-off does not hold and the push should not be treated as closeable yet — which is the deliberate Gemini-selective differentiator. Honour every constraint in the section above verbatim: three of Jaime's issues are interchangeable candidates for "her QC issue", so prefer writes that are unique by construction; keep no fact load-bearing inside an email body; and assert nothing about her QC queue being otherwise clear, because a Mesa Vista 4C QC inspection sits on 2026-07-15.

---

## Corrections appended at S2 (2026-07-26) — body above left as authored

Three figures in the plan above were falsified against `_aux/Universe_Split/` during S2 grounding. The lever selection, the density band and the hardness score are unaffected; only these figures are wrong. Recorded here so S3 and FINAL do not re-propagate them. Full detail in `_aux/Verification_s2.md`.

| Location | As written | Verified | Source |
|---|---|---|---|
| line 42 (Lever 5) and line 128 (Stump Hypothesis 3) | "C001 carries 104 messages with 15 distinct parents" / "104 messages across 15 parents" | 104 messages, **37** distinct thread parents (48 top-level, 56 replies) | `slack.slack_messages.json`, parentage via `thread_parent_id` |
| line 41 (Lever 4) | "an Airtable `search_records` on 'HVAC' returns 20+ `tblMaintenanceTickets` rows, all on unrelated properties (Building C 304, Palomar 312, Pinecrest 12, Riverside, **Oakdale**)" | **18** of 50 rows carry the token HVAC. Distribution: Building C 9, Palomar 4, Pinecrest 12 / Elmwood / Riverside 1 each; four rows name no property. **"Oakdale" appears nowhere in `tblMaintenanceTickets`** | `airtable.airtable_records.json` |
| line 25 (evidence table row 5) | Lisa's 2026-05-27 ask was "five days after Elias declared all clusters done" | **seven** days (Elias 2026-05-20) | already recorded as S1 Council A N5 |
| lines 98-108 (Service Breadth table) and line 166 (Hardness Brief) | linear 19 calls / **34%** of total, brief targets "Linear under 35% of the total" | linear **~26.5 of ~54** calls, **~49%** at the Opus midpoint. Still under the 60% single-service ceiling with 5 services at >= 5%, so the breadth gate still PASSes; the concentration is intrinsic to a Linear-state-resolved answer rather than manufactured | FINAL council trajectory sketch (2026-07-26), corroborating the AUDIT_oe THIN_BREADTH acceptance note |

The error in the plan's direction of travel is favourable in two of three cases: 37 thread parents makes Lever 5 stronger than planned, not weaker, and 18 decoy rows is still ample noise for Lever 4.

---

## Corrections appended post-S4 / post-AUDIT (2026-07-26) — body above left as authored

Two pre-registered predictions in the plan above are falsified by the 12 live trajectories. Recorded here so a future build on this universe does not re-propagate them. Sources: `_aux/Council_Reports/S4_verdict.md` and `_aux/Council_Reports/AUDIT_all.md` finding A-4.

| Location | As written | Falsified by | Consequence |
|---|---|---|---|
| Lever 5 selection (line 60) + density row (line 83) + Lens 3 trace | **Lever 5 thread-reply blindness** selected as one of five levers, priced at 3.0 calls, "empirically ~40% miss" | `slack_read_channel(channel_id="C001", limit=100)` returns thread replies **inline as flat messages** on this server. Opus called `slack_read_thread` **0 times across all 6 runs**; Gemini called it 9 times across 4 runs. Both families had John Smith's 20x25 post and Brooke's stock-count reply in context either way. | **Lever 5 has no live discriminating mechanism on StarPM.** The facts it was planted to hide still carry criteria (8, 9, 12, 29, 35, 38, 39) and those criteria still fail, but as **reasoning** misses, not retrieval misses. Four live levers remain against a threshold of three, so the hardness score is unaffected. Do not budget calls for thread depth on this universe and do not select thread-reply blindness as an independent lever. |
| Stump Hypothesis 2 (line 126) + dual-model mix table (line 72) | **[HIGH]** Gemini names the open items but never issues the retraction; "near-100% Gemini failure" on the retraction criterion, cited as the deliberate Gemini-selective differentiator per Learnings L31 | Criteria 49 and 50 pass **12/12** — all six Opus runs and all six Gemini runs issue the retraction. | **The L31 retraction beat is not a Gemini stump on this task.** Root cause: the prompt's closing paragraph supplies both branches of the QC verdict in the persona's own words. That wording is *required* for a 5/5 Unique Ground Truth score — without it the ask is action-decision ambiguous — and it is also what makes the retraction reachable for Gemini. **Bankable lesson: L31's retraction stump and a 5/5 Unique Ground Truth score are in direct tension; when both are wanted, the retraction cannot be the differentiator.** Gemini's actual failure mode is *what* it names, not whether it retracts: the May 23 North pair, the tenant-access holdovers and the West coverage gap are absent, so the retraction attaches to the wrong open-item list. |

Neither correction moves a gate: pass@1 is 0/6 on both models and per-model density is 62.5 (Opus) and 79.8 (Gemini) against a 40 target.
