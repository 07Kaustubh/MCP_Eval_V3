# Council B — Adversarial QC + Density + Hardness Preservation

**Deliverable:** `Tasks/44_6a62ccba8cad60844b8364b9/5_Prompt.txt`
**Phase:** prompt (S1) · **Universe:** starpm (V4) · **Universe today:** 2026-07-01 (America/Chicago)
**Persona:** Jaime Salinas · Quality Control Inspector · `p_007` · `jaime.salinas@starpm.com`
**Business function:** 3 · Quality Control & Field Services
**Density scheme:** StarPM v4, applied PER MODEL — midpoint ≥ 40 PASS · 15–39 THIN · < 15 INSUFFICIENT. The V3-family 50/40 bands are NOT applied.

**VERDICT: GO** — zero Major issues, zero blocking B6 propagation flags, all 14 applicable sub-dims at 5, density PASS on both models, 5/5 levers preserved, L31 beat present, no escape-valve clause.

---

## Evidence base

All findings below are re-derived from `_aux/Universe_Split/` directly, not inherited from the Hardness Plan's claims. Record counts confirmed against `_aux/Universe_Index/service_inventory.md`: 230 Linear issues, 48 Linear comments, 5 workflow states, 580 Slack messages (104 in C001), 565 GCalendar events, 484 Gmail messages, 170 Airtable records, 625 QuickBooks entities, 61 contacts.

Key structural facts independently verified:

| Fact | Source | Verified |
|---|---|---|
| `proj_003` = "Preventive Maintenance Push", state `backlog` | `linear.linear_projects.json` | yes |
| Workflow states: `state_OPS_0..4` = Backlog / Todo / In Progress / In Review / Done | `linear.linear_workflow_states.json` | yes |
| Jaime owns exactly 3 issues: OPS-87 **Todo**, OPS-96 **Todo**, OPS-98 **In Progress** | `linear.linear_issues.json` (`assignee_id` → Jaime Salinas) | yes |
| OPS-40 and OPS-91 are genuinely **Done** (`completed_at` 2026-05-18, 2026-05-28) | `linear.linear_issues.json` | yes |
| Push kickoff, Brooke, 2026-05-07 C001: "the Preventive Maintenance Push is officially moving into active execution, kicking off the portfolio-wide HVAC, plumbing, and electrical audit" | `slack.slack_messages.json` | yes |
| End-of-June target: Brooke 2026-06-19 C001 "Goal is to close everything out before end of June" + OPS-186 "closed out before the end of June" | slack + linear | yes |
| C001 = `#maintenance`; 104 messages, **56 thread replies under 37 distinct parents** | `slack.slack_channels.json`, `slack.slack_messages.json` | yes |
| Airtable `tblMaintenanceTickets` description: *"System of record for maintenance work orders; Linear is secondary."* | `airtable.airtable_tables.json` | yes |
| `jaime.salinas@starpm.com` exists as a GCalendar calendar id | `gcalendar.gcalendar_calendars.json` | yes |
| 27 future confirmed events (9 unique), **none** touching the push / HVAC clusters / Jaime | `gcalendar.gcalendar_events.json` | yes |
| No CB universe edits (`4_Changelog.json` = `[]`, inject SQL is template-only) | task dir | yes |

---

## [B1] QC sub-dimension scoring

Scored against `Docs_starpm/7_QC_Spec_Doc1.json` with the `Evals_starpm/1_Prompt_Eval.md` hard gates applied literally. Line format per Council_Protocol "Sub-dimension scoring scheme map".

### Hard gates executed first

**HARD GATE — UGT end-state divergence.** Candidate final universe states enumerated under every reasonable reading (full analysis in B2). All readings converge on one end-state: N new Linear follow-up items for the still-open push work, a note on each of Jaime's three QC records, one Airtable maintenance ticket for field items needing a tech back onsite, one GCalendar re-inspection slot on Jaime's calendar, one Slack post to C001, one Gmail draft to Brooke carrying the **negative** branch. **No divergence.**

**HARD GATE — UGT precision guardrail (T11).** Three-part test run before considering any UGT fail. (1) Concrete writes enumerated under both the "Airtable ticket log" and the "Linear-only" readings, and under both the "narrative-only" and "mutating" readings — see B2. (2) Variation acceptance is an S3 concern; noted forward. (3) Deliverable content is identical under every surviving reading. Guardrail confirms **no material divergence** → UGT is not failed.

**HARD GATE — Convergence investigation.** No agent runs exist at S1. Not applicable; recorded rather than skipped.

**HARD GATE — Dimensional feasibility (T10).** The prompt requests two per-X breakdowns: *"where every piece of it stands as of today, cluster by cluster"* and *"draft an email to Brooke, cluster by cluster"*. Dimension = cluster. Verified the universe carries it: South / North / East are named in OPS-16, OPS-17, OPS-18 scope descriptions and in Elias's C001 posts; West is established independently by OPS-35 ("Preventive Maintenance Push - West Cluster Properties"), OPS-91 ("West Cluster") and OPS-186 ("the West Cluster work still underway"). The dimension is carried as consistent literal text in issue titles and descriptions rather than a dedicated enum column, but it is queryable, unambiguous, and exhaustive over four values. **Feasible** — this is not the absent-jurisdiction-field pattern the gate exists to catch.

**HARD GATE — Phantom tight-identifier grep.** Every tight identifier extracted and grepped against `_aux/Universe_Split/`. The prompt carries no numeric IDs, no channel names, no dollar amounts and no absolute dates, which collapses the phantom surface almost to zero.

| Tight identifier in prompt | Grep target | Hit |
|---|---|---|
| "Preventive Maintenance Push" | `linear.linear_projects.json` `proj_003`; also OPS-35 / OPS-40 / OPS-51 descriptions, Slack 2026-05-07, 2 calendar check-ins | **40 hits** in `Universe_complete_data.json` |
| "Brooke" | `contacts.contacts.json` → Brooke Phillips, Apartment Property Supervisor, `brooke.phillips@starpm.com`. **Exactly one Brooke in 61 contacts** — no first-name collision, no escalation to Major | 2152 hits |
| "HVAC" | Slack C001, OPS-16/17/18/43/87/91/96, Airtable tickets | 256 hits |
| "plumbing" | Slack 2026-05-07 kickoff; OPS-97 "Plumbing inspection complete" | 244 hits |
| "electrical" | Slack 2026-05-07 kickoff; OPS-186 "Electrical panel inspections complete" | 18 hits |
| "maintenance ticket log" | `airtable.airtable_tables.json` `tblMaintenanceTickets` "Maintenance Tickets" | 16 hits on "maintenance ticket" |
| "the channel the push has been running in" | C001 `#maintenance` (kickoff, wrap, field note, filter post, 6/19 updates all in C001) | resolved |
| "my calendar" | `gcalendar.gcalendar_calendars.json` id `jaime.salinas@starpm.com` | resolved |
| "end of June" / "yesterday" | Brooke 2026-06-19 C001 + OPS-186; yesterday = 2026-06-30 | resolved |
| "early May" | Slack 2026-05-07 Brooke kickoff | resolved |
| "late May" | OPS-87 created 2026-05-24; OPS-96 / OPS-98 created 2026-05-25 | resolved |
| "around the same time" (crew wrap) | Elias C001 `1779308446.000005` / `1779308447.000006`, 2026-05-20 | resolved |

**Zero phantoms. Zero near-match traps.**

**HARD GATE — Write-action divergence.** Enumerated in B2. No reading flips a write action, and there is no write-vs-no-write or act-vs-defer fork. **Pass.**

**HARD GATE — Delegation clarity.** Regex scan for `I'll [verb]` / `I will` / `I am going to` / `I need to [verb]` across the prompt body: **zero hits**. Every first-person construction is either a state report ("I logged", "I have been", "my read is") or a preference statement ("I need to know", "I do not want"), none of which claims a self-action that competes with an imperative directed at the agent. **Pass.**

**HARD GATE — Minimum complexity.** Estimated tool calls 50 (mid-case, B3) against a >15 threshold; 7 of 8 services exercised against a 2+ threshold; 6 write actions across 5 services against a "multiple meaningful writes" threshold; the answer is provably not in one place (the load-bearing contradiction requires joining Linear `state_id`, Linear prose, Slack top-level posts, Slack thread replies, and Calendar agendas). **Pass on all four rows.**

**HARD GATE — 2.8 date alignment against 2026-07-01.** Every relative phrase resolved and data-checked:

| Phrase | Resolves to | Universe data in window | Answer changes if date shifts? | Verdict |
|---|---|---|---|---|
| "End of June was the target" | 2026-06-30 | Brooke 2026-06-19 C001; OPS-186 2026-06-17 | anchored to a named target, not to today | OK |
| "That came and went yesterday" | 2026-06-30 | the deadline date itself | yes — anchored by fixed today 2026-07-01 | OK |
| "as of today" | 2026-07-01 | 3 Jaime-owned issues live, ~30 push-adjacent issues non-Done | yes — anchored | OK |
| "Brooke started this in early May" | 2026-05-07 | Slack kickoff 2026-05-07 | no | OK |
| "in late May" | 2026-05-24 / 2026-05-25 | OPS-87, OPS-96, OPS-98 | no | OK |
| "around the same time" | 2026-05-20 | Elias wrap `1779308446/47` | no | OK |

Universe-level alignment: 27 future confirmed calendar rows are legitimately forward-facing (per the QC spec's explicit carve-out), the latest push artifact is OPS-186 dated 2026-06-17, and nothing in the push chain post-dates today. No stale references, no ambiguous windows, no contradictions. **Pass.**

### Sub-dimension scores

```
SUB-DIM Unique Ground Truth -> SCORE 5/5 (1/3/5 scheme, no middle band since 06/09) -> end-state divergence gate enumerated four readings; all converge on one final universe state, and the universe determinately fires the negative branch of the closing conditional
SUB-DIM Feasibility -> SCORE 5/5 (1/3/5 scheme) -> every ask maps to a real tool (save_issue, save_comment, create_records_for_table, create_event, create_draft, slack_send_message) and every required fact is materialized; T10 dimensional gate passes on the cluster dimension
SUB-DIM Explicit Tool Mention -> SCORE 5/5 (1/5 binary) -> zero service names, zero tool function names, zero parameter names, zero internal IDs (OPS-*, C00*, tbl*, rec*) in the prompt body
SUB-DIM Prompt Clarity and Specificity -> SCORE 5/5 (1/3/5 scheme) -> write-action divergence gate and delegation-clarity gate both clean; no reading flips a write action, and there are zero "I'll [verb]" statements
SUB-DIM Contrived / Unnatural Prompts -> SCORE 5/5 (1/3/5 scheme) -> no command list, no numbered steps, no exact-timestamp or format constraints; difficulty is entirely from scattered information and prose-versus-state conflict
SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5 scheme) -> phantom tight-identifier grep returns zero misses across 12 identifiers; zero major and zero minor factual errors; every authority claim is soft-verbed and literally true of what was logged
SUB-DIM Tool use and Cross-service requirement -> SCORE 5/5 (1/5 binary) -> 7 of 8 services exercised, and the load-bearing conclusion cannot be reached inside any single service
SUB-DIM Investigation -> SCORE 5/5 (1/5 binary) -> not pre-solved; the prompt asserts the opposite of the ground truth and every write depends on an investigation the prompt does not shortcut
SUB-DIM Coherence -> SCORE 5/5 (1/5 binary) -> remove-sentence test run on all six paragraphs; the validator's bolt-on WARN on the opening sentence is a false positive because removing it strands "Before I put my name to this closing out" with no antecedent
SUB-DIM Persona -> SCORE 5/5 (1/3/5 scheme) -> a QC inspector deciding whether to sign off or kick back is the literal centre of Jaime's brief; voice matches (313 words, short declaratives, observation-first, zero emoji)
SUB-DIM Business Function -> SCORE 5/5 (3/5 scheme, no FAIL band) -> primary scenario is a QC sign-off reconciliation plus a field re-inspection, squarely inside "3 - Quality Control & Field Services"
SUB-DIM Alignment with Today's Date -> SCORE 5/5 (1/3/5 scheme) -> all six relative phrases resolve cleanly against 2026-07-01 with confirmed universe data in every resolved window
SUB-DIM Universe Feasibility (Data Exists) -> SCORE 5/5 (1/5 binary) -> every fact required by the trajectory is materialized in _aux/Universe_Split/ and reachable through the StarPM tool catalog
SUB-DIM Universe Cross-service Coherence -> SCORE 5/5 (1/5 binary) -> 4_Changelog.json is empty and the inject SQL is template-only, so there are no CB edits capable of creating a contradiction
```

**All 14 applicable sub-dims at 5.** No sub-dim requires a below-5 justification.

---

## [B2] Adversarial alt-path / second-reading attack

Read five times under the five role lenses. Four targeted attacks per the brief, plus two of my own.

### (a) "our maintenance ticket log" — could a reasonable agent write this to Linear instead of Airtable?

**Attack.** The Council Protocol's own StarPM service map says "maintenance tickets / issues → linear (secondary to airtable)". Linear is the store the agent has already been reading for twenty-plus calls by the time it reaches this sentence. An agent with momentum could file the field items as Linear issues and never open Airtable, producing a final universe state with no Airtable row.

**Resolution — attack fails, on three independent grounds.**

1. **The prompt is internally self-disambiguating.** It establishes "tracking item" as its term for the Linear write two sentences earlier — *"Anything still open gets its own tracking item raised, with the person who owns that work named on it."* It then explicitly contrasts: *"Anything flagged in the field that still needs a tech back onsite belongs in our maintenance ticket log **rather than sitting as a tracking item**."* The prompt does not merely name a destination; it names a destination *and excludes the competing one by the label it just defined*. A Linear-only execution contradicts the sentence's own subordinate clause.
2. **The universe supplies an explicit system-of-record statement.** `airtable.airtable_tables.json` → `tblMaintenanceTickets`, name "Maintenance Tickets", description *"Ongoing maintenance requests and issue tracking. System of record for maintenance work orders; Linear is secondary."* Any agent that opens the Airtable base reads the disambiguation directly.
3. **Precision guardrail.** Even granting the attack, it produces an *incomplete execution*, not a second valid reading — the agent has ignored an explicit exclusion clause. That is a rubric failure, which is the intended behaviour, not a UGT divergence.

**Ruling: NOT a divergence.** Carried forward: S2 must pin `appPropertyOps` / `tblMaintenanceTickets`, and S3 must grade the Airtable ticket on content (unique by construction), never on a record id.

### (b) "get our tracking to match" — could an agent reasonably read this as narrative-only?

**Attack.** "Get our tracking to match" is abstract. An agent could satisfy it by *describing* the mismatch in the Slack post and the Gmail draft rather than mutating any record — a write-vs-no-write fork, which the Clarity hard gate treats as an automatic FAIL.

**Resolution — attack fails.**

1. The clause sits inside an unbroken chain of write imperatives, and the two sentences immediately after it are both explicit mutations: *"Anything still open gets its own tracking item raised, with the person who owns that work named on it. My own spot-check records are part of that, with a short note left on each one saying where it landed and why."* A narrative-only reading requires discarding both.
2. The reporting work is **separately and explicitly allocated elsewhere** — *"post where this stands in the channel the push has been running in"* and *"draft an email to Brooke"*. Because the prompt already has dedicated narrative deliverables, "get our tracking to match" cannot be absorbed into them without leaving the sentence with no function. The narrative-only reading is not merely weaker; it is *redundant*, which is what kills it.
3. "Match" takes a direct object relationship between two things — the tracking and what is actually finished. Making them match is a mutation predicate, not a reporting predicate.

**Ruling: NOT a write-vs-no-write divergence.**

**Residual, recorded.** The *scope* of the corrective mutation is bounded but not sealed. The prompt licenses two determinate channels — new tracking items for open work, and a note on each of Jaime's own spot-check records — and never authorises editing issues owned by others (OPS-43, OPS-97, OPS-35 are Elias's / Carlos's / Brooke's). A thorough agent might additionally flip states on those. Under the precision guardrail this is an *additive, non-contradictory* write: the six enumerated deliverables are identical under both readings. Not a UGT fail. Carried to S3: no rubric may require or penalise third-party state edits.

### (c) "put a slot on my calendar to go back out and re-inspect whatever ends up in that follow-up" — is the event's subject determinate?

**Referent chain traced.** "that follow-up" ← "Anything flagged in the field that still needs a tech back onsite belongs in our maintenance ticket log". The event's subject is therefore *the re-inspection of the field-flagged items routed into the maintenance ticket log*. That is a single, determinate subject.

**Determinate:** the subject; the calendar (`my calendar` → `jaime.salinas@starpm.com`, confirmed present in `gcalendar.gcalendar_calendars.json`); the actor (Jaime); the fact that it is one slot, not a series.

**Under-determined:** date, start time, duration, attendees. The prompt supplies no date.

**Ruling: subject determinate, timing free.** A free timestamp on a single event with a fixed owner and a fixed subject is a wording-level variation under the T11 precision guardrail — the deliverable set is identical regardless of which day the agent picks. **NOT a UGT fail.** Carried to S3 as MODERATE-3 below: grade on calendar owner + re-inspection subject + a start date on or after 2026-07-01, never on an exact timestamp.

**Constraint-3 cross-check:** the new event must coexist with the 2026-07-15 *Make-Ready QC Inspection - Mesa Vista 4C* (attendees Carlos / Brooke / Wesley — notably **not** Jaime) and the 2026-07-23 *Q3 Make-Ready Planning & Budget Review*. The prompt makes no claim about Jaime's calendar being otherwise clear, so nothing is contradicted.

### (d) Does the final conditional create two valid end-states? — answered by checking the universe

The sentence: *"If my QC side is a pass, say pass. If it is not, say straight out that my earlier sign-off does not hold and this should not be treated as closeable yet, with the reasons."*

**This is the single most important question in the review, and it is answerable from data.** I checked whether the universe leaves the branch open. It does not — the positive branch is **unreachable** on four independent, separately-sourced grounds:

1. **Structured state.** Jaime is the assignee on exactly three issues in the 230-issue corpus: OPS-87 `state_OPS_1` (Todo), OPS-96 `state_OPS_1` (Todo), OPS-98 `state_OPS_2` (In Progress). **Not one is in `state_OPS_4` (Done).** Her own prose says otherwise — OPS-87's description ends "I've commented the results directly on each cluster's issue and moved both from In Review to Done", and OPS-98's 2026-05-25T09:00 comment says "Everything cleared QC, so I've moved both cluster issues to Done."
2. **The filter run was never finished.** OPS-96's comment (2026-05-30T05:31) claims *"Ran a spot-check across all units this morning - filters look good across the board."* But John Smith posted in C001 on 2026-05-23: *"the supply closet is almost out of 20x25 filters so we'll need a restock before I can finish the run"*, and the sole reply on that parent (Brooke, `1779569323.000012`) asks Elias for a stock count before a bulk order. No restock and no completion follows. An "all units" filter QC pass is not supportable.
3. **Her own field note was never dispositioned.** Jaime, C001, 2026-05-23: *"north Cluster walk-throughs done. Two units need HVAC looked at right away, flagged on the Linear issue with coil, plumbing, and panel notes."* One day later OPS-87 says "everything came back clean across the board", and OPS-98's comment says "No issues to flag on either side". No follow-up issue for those two units exists anywhere in the 230-issue corpus.
4. **Coverage gap.** Her three QC issues cover South, North and portfolio filters. West is a separate scope (OPS-35, In Progress, Lisa Smith onsite lead) and OPS-186 dated 2026-06-17 states *"the West Cluster work still underway"*. She never walked West.

**Ruling: the universe is determinate. Only the negative branch fires. One end-state.**

The conditional is a persona-voice framing device whose resolution is fixed by the data — structurally identical to "tell me whether X reconciles", where the conditional describes the *shape of the report* and the universe fixes the *answer*. It is not a fork. **UGT PASS.**

### (e) Own attack — "My own spot-check records": which records?

"My own spot-check records ... a short note left on each one." Jaime is the assignee on exactly three issues (OPS-87, OPS-96, OPS-98). But OPS-99, OPS-108 and OPS-51 all *narrate* Jaime's spot-checks in the third person while being assigned to Elias Navarro and Brooke Phillips ("Jaime pulled a spot-check across the East cluster units..."). A thorough agent could comment on five records instead of three.

**Ruling: MINOR, not a divergence.** "My own" is a strong possessive and the near-duplicates are written *about* Jaime in the third person, which reads as someone else's record. The dominant reading is the three she owns. The variant reading is a superset that adds comments without removing or changing any. Carried to S3 as MODERATE-2 with an explicit accept-band.

### (f) Own attack — what state should Jaime's own records be moved to?

If "get our tracking to match" is applied to her own records, what is the target state? This looks like it could be indeterminate — but it resolves cleanly. Her records' *state* already shows them open (Todo / Todo / In Progress); what is wrong is the *prose*. And the prompt asks for exactly the corrective that fits: *"with a short note left on each one saying where it landed and why."* The note is the determinate write; no state flip is required or implied.

Note the elegant consequence: an agent that latches on the prose ("I moved both to Done") without checking `state_id` will believe the tracker says Done and try to *reopen* the issues — a backward write that does not match. That is Lever 2 firing exactly as designed. It is a difficulty feature with a unique correct end-state, not an ambiguity defect.

### B2 conclusion

**No adversarial divergence found.** No second reading produces a different write-action set, a different recipient, or a different final universe state.

---

## [B3] Tool-call density projection

Independent trajectory sketch for THIS prompt as written, not inherited from the Hardness Plan.

| Phase | Calls (mid-case) | Composition |
|---|---:|---|
| Orient | 7 | channel list/search → C001; `slack_read_channel` ×2 (104 msgs, paginated); `slack_search_public`; `contacts_search_contacts` "Brooke"; `list_teams`; `list_projects` → proj_003 |
| Lever 2 — structured state | 9 | `list_issues` ×3 (project filter + pagination); **`list_issue_statuses` ×1** (decode `state_OPS_*`); `get_issue` ×5 on OPS-87 / 96 / 98 / 43 / 56 |
| Lever 9 + Lever 1 — authority + wrap | 7 | `list_comments` ×3 on Jaime's records; `get_issue` ×3 on OPS-35 / OPS-186 / OPS-97; `get_issue` ×1 sanity-check on OPS-40 or OPS-91 |
| Lever 5 + Lever 8 — replies + chain | 7 | `slack_read_thread` ×4 (of 37 parents); `slack_search_public` ×2 ("filters"/"restock", "West cluster"); `list_issues` ×1 second pass to locate the issue carrying the two-unit flag |
| Cross-service triangulation | 9 | `list_calendars`; `list_events` ×2 (check-in agendas); `list_bases`; `list_tables_for_base`; `get_table_schema`; `search_records` on existing tickets; `search_threads` ×1 (Gmail sweep); QuickBooks noise ×1 |
| Write actions (5 services, 6 writes) | 11 | `save_issue` ×4 (follow-up items: West coverage gap, filter run, South no-access, two North units); `save_comment` ×3 (OPS-87 / 96 / 98); `create_records_for_table` ×1; `create_event` ×1; `create_draft` ×1; `slack_send_message` ×1 |
| **TOTAL (mid-case)** | **50** | |

**Range.** Lean floor ≈ 31 (single-page channel read, no thread opens, one unfiltered `list_issues`, three follow-up items, minimal Airtable walk). Thorough ceiling ≈ 68 (per-issue `get_issue` across 12+ candidates, 6 thread opens, 6 follow-up items).

**Per-model projection (StarPM v4 bands):**

| Model | Midpoint | Band | Basis |
|---|---:|---|---|
| **Opus 4.8** | **54** | **PASS** | Opus enumerates issues individually and opens threads; the 6-write / 5-service surface is fixed cost |
| **Gemini** | **46** | **PASS** | Gemini compresses list calls and opens fewer threads; StarPM calibration (Task 41: 47 / 45 / 37 / 38 / 33 / 40) applied as a downward adjustment |
| **Combined** | **50** | **PASS** | |

**Against the Hardness Plan's 55.5.** My independent projection is 50 — about 10% below the Plan's midpoint, and within the same band. The gap comes from the buffer row: the Plan allots 7.5 to cross-service triangulation where I allot 9 but trim its Lever-1 row from 6.5 to a shared allocation, and I do not credit the Plan's optimistic assumption of `get_issue` iteration across the full push set. **No density regression** — the deliverable as written still clears the gate on both models with margin, and even the lean floor of 31 stays inside the THIN band rather than falling to INSUFFICIENT.

**Honest downside.** Individual Gemini runs on prior StarPM tasks dipped as low as 33. The gate reads the per-model *average*, and 46 clears 40 with room, but a single-run dip into THIN territory is plausible and should not be treated as a surprise at S4.

**Service breadth (v11 G1).** StarPM service list per `Validators/universes.py`: airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack.

| Service | Calls | Share |
|---|---:|---:|
| linear | 24 | 47% |
| slack | 11 | 22% |
| airtable | 6 | 12% |
| gcalendar | 4 | 8% |
| gmail | 3 | 6% |
| contacts | 2 | 4% |
| quickbooks | 2 | 4% |
| hubspot | 0 | 0% |

**Breadth gate: PASS.** 7 of 8 services exercised. **5 services carry ≥ 5%** against a threshold of 4. Dominant service **linear at 47%**, under the 60% single-service ceiling — density is not manufactured by stacking one service. HubSpot at zero is correct: it is the leasing/deal funnel and has no linkage to the maintenance push; padding it would be artificial.

**Deviation recorded.** The Hardness Plan projects linear at 34% and instructs the prompt writer to keep "Linear under 35% of the total". My projection puts it at 47%. The gate still passes comfortably, so this is a NOTE, not a finding — but the Plan's 34% figure was optimistic given that the prompt's core question resolves in a Linear column and three of the six writes are Linear writes.

---

## [B4] Hardness preservation

Expected 5 selected levers + the L31 beat. Each checked against the prompt **as written**, not against the Plan's intent.

### Lever 2 — Structured-DB skip on Linear `state_id` — **PRESERVED**

Trigger sentence: *"Before I put my name to this closing out, I need to know where every piece of it stands as of today, cluster by cluster"* and *"Work out what is actually finished and what is not."*

The agent must reach a per-cluster completion determination. Every conversational surface it will naturally read asserts completion — Elias's wrap, OPS-87/96/98 descriptions and comments, OPS-56's "South cluster is fully wrapped", OPS-99/OPS-108's "QC passed". The contradiction lives only in `state_id`, and decoding `state_OPS_1` / `state_OPS_2` requires a second call to `list_issue_statuses`. **The prompt never uses the words status, state, tracker field, Done, In Progress, or Backlog, and never suggests the tracker itself might be wrong.** Trigger fully intact.

### Lever 9 — Authority dismissal, persona-self variant — **PRESERVED (mild dilution, not a regression)**

Trigger sentence: *"I logged both cluster spot-checks as passing in late May and my read is that my part of it is finished."*

The wrong framing is authored by the person the agent works for, in her professional voice, and is corroborated by her own competently-worded issue prose (OPS-98: "airflow was solid throughout, coils came back clean, and refrigerant levels looked correct on every unit I pulled"). An agent acting on Jaime's behalf defers to her logged judgement.

**Dilution assessed:** the closing conditional raises the abstract possibility she is wrong. But Lever 9's mechanism is deference to domain-correct professional judgement, and the conditional supplies **no evidence** to overcome that deference — the evidence sits behind Lever 2, Lever 5 and Lever 8. An agent that does not do the structured work will take the positive branch. Not a regression.

### Lever 1 — Latching on the loudest wrap — **PRESERVED (strengthened)**

Trigger sentence: *"The crew called the HVAC run wrapped around the same time."*

This actively points the agent at Elias's C001 wrap (`1779308446.000005`: "all three clusters are done. Every unit serviced"; `1779308447.000006`: "Summer HVAC push is a wrap. All three clusters done, 34 units total serviced") **and endorses it in the persona's own voice**. It also seeds the three-cluster frame that Stump Hypothesis 4 depends on — an agent anchored on "all three clusters" reads three-of-three as portfolio coverage and never notices that OPS-35 / OPS-91 / OPS-186 establish a fourth. Trigger not merely intact but reinforced.

### Lever 8 — Multi-link chain off Jaime's own field note — **PRESERVED**

Trigger sentence: *"Anything flagged in the field that still needs a tech back onsite belongs in our maintenance ticket log rather than sitting as a tracking item."*

"Flagged in the field" is precisely the class Jaime's 2026-05-23 C001 note belongs to. Chain: (A) read C001 → find *"Two units need HVAC looked at right away, flagged on the Linear issue with coil, plumbing, and panel notes"*; (B) determine **which** of ~32 push-adjacent issues carries those notes; (C) determine whether the flag was ever dispositioned — it was not; no follow-up issue exists in the 230-issue corpus.

Critically, the prompt gives the chain a **write consequence** (the Airtable ticket plus the calendar re-inspection), which is what makes hop C rubric-able rather than merely observable. Trigger intact and better-anchored than the Plan required.

### Lever 5 — Thread-reply blindness — **PRESERVED**

Structure re-verified in-universe: C001 carries 104 messages, **56 of which are thread replies under 37 distinct parents**. The two load-bearing replies:

- `1779308444.000003` and `1779308445.000004` (Elias → Carlos, South no-access reschedule) under parent `1779308442.000001` — `thread_parent_id` = `8ce45073c71f56ae89c859c0f3f6fc09`, confirmed.
- `1779569323.000012` (Brooke → Elias, filter stock count before bulk order) under parent `1779567943.000011` — `thread_parent_id` = `7b8f161126065f47bf66e3e0326ef2ea`, confirmed.

The prompt's *"cluster by cluster"*, *"Anything still open"* and *"Anything flagged in the field that still needs a tech back onsite"* all force the agent toward the South no-access unit and the filter-run block, and both resolve only inside replies. A channel read returns parents; the agent must elect to open each thread. Trigger intact.

### L31 Gemini-selective retraction beat — **PRESENT and forcing**

Quote: *"I do not want Brooke's email written so it can be read either way. If my QC side is a pass, say pass. If it is not, say straight out that my earlier sign-off does not hold and this should not be treated as closeable yet, with the reasons."*

This is an explicit negative-directive requirement **plus** an explicit anti-hedging instruction. L31's documented Gemini failure mode is precisely hedged positive framing that names the blocker without issuing the prohibition — and "written so it can be read either way" forecloses exactly that. Present and correctly shaped.

**NOTE recorded (MODERATE-4).** The prompt supplies the retraction *wording* verbatim. This does not neutralise the beat, for two reasons: (i) L31's Task 39 evidence shows Gemini failing 6/6 even where the required phrasing existed in the rubric — the failure is behavioural, not lexical; (ii) more decisively, the retraction clause is **gated behind the Lever 2 determination** — a run that concludes "pass" (the predicted majority behaviour per Stump Hypothesis 1) never reaches the clause at all. Pre-registered for S4 rather than fixed at S1.

### COUNTER-CHECK — does the prompt contain an escape-valve clause neutralising Lever 2? (Hardness_Plan constraint 9)

**Required output: the closest sentence, quoted, with a ruling.**

**Closest sentence:** *"Work out what is actually finished and what is not, and get our tracking to match."*

**Ruling: NOT an escape valve. Constraint 9 HONOURED.**

Reasoning, against L29's actual shape. The L29 exemplar is *"If anything in what you pull together changes the read on this before I take it to Daniel, say so plainly. I would rather hear it from you before the package moves than from Andrea after."* — an open-ended, deliverable-unbound invitation to hunt for and surface contradictions, which primes the agent to interrogate every surface it touches. Three properties define it: it is conditional on discovery, it is unbound to any specific deliverable, and it signals the persona's own uncertainty.

The candidate sentence has **none** of those properties. It is unconditional, it is bound to a specific write ("get our tracking to match"), and it signals no uncertainty. It is the reconciliation ask itself — the irreducible core of the task, without which there is no task at all. Crucially, it points the agent at **field-completion state**, which is exactly where the *false* prose lives (Slack posts, issue descriptions, issue comments). It does not point at, name, or hint at the Linear workflow-state column that Lever 2 turns on. An agent following this sentence literally walks straight into the trap.

Two runner-up sentences also cleared:

- *"I need our records saying the same thing"* — a statement of the deliverable standard, not an invitation to hunt. Names no surface, contains no "check whether", no hedge.
- The closing conditional — bound to the **output shape of the Gmail draft**, not to any data surface. Constraint 9's own escape clause reads "If persona realism needs a hedge, point it at a non-load-bearing surface"; pointing it at a deliverable's tone rather than at a data surface is the safest placement available, and it is the pre-authorised L31 beat.

**The L29 shape is absent from the prompt entirely.** No sentence anywhere invites contradiction-surfacing.

### Lever preservation summary

| Lever | Status |
|---|---|
| Lever 2 — structured-DB skip (`state_id`) | **PRESERVED** |
| Lever 9 — authority dismissal, persona-self | **PRESERVED** |
| Lever 1 — latching on the loudest wrap | **PRESERVED (strengthened)** |
| Lever 8 — multi-link chain off the field note | **PRESERVED** |
| Lever 5 — thread-reply blindness | **PRESERVED** |
| L31 retraction beat (Gemini-selective) | **PRESENT and forcing** |
| Escape-valve counter-check (constraint 9) | **CLEAN** |

**Expected 5, preserved 5, missing 0. Zero HARDNESS_REGRESSION flags.**

---

## Hardness_Plan pre-registered S1 constraints — 1 through 10

| # | Constraint | Ruling | Evidence quote |
|---|---|---|---|
| 1 | F7 AMBIGUOUS_TARGET — prefer writes unique by construction | **HONOURED** | Every projected write is unique by construction: *"gets its own tracking item raised"* (new issue), *"belongs in our maintenance ticket log"* (new Airtable row), *"put a slot on my calendar"* (new event), *"draft an email to Brooke"* (named recipient), *"post ... in the channel the push has been running in"* (one channel). The one non-unique write is scoped by "each one" — *"My own spot-check records are part of that, with a short note left on **each one**"* — so no single-id pin is required. |
| 2 | F8 NON_ATOMIC_ENUM — decompose per item | **HONOURED** (rubric-phase constraint; prompt does not force bundling) | *"Anything still open gets its own tracking item raised"* mandates one item per open thing — precisely the atomic shape S3 needs. No completeness predicate is imposed at prompt level. |
| 3 | F9 UNRECONCILED_FUTURE_EVT — no claim that Jaime's queue is clear or the budget is settled | **HONOURED** | Re-verified: 27 future confirmed events, 9 unique, **none** touching the push / HVAC clusters / Jaime. The prompt's only forward-looking clause is *"put a slot on my calendar to go back out and re-inspect whatever ends up in that follow-up"* — a new event, asserting nothing about existing ones. Zero claims about queue clarity or maintenance budget. |
| 4 | Gmail is a deliverable, never a source | **HONOURED** | Gmail appears exactly once, as a write: *"draft an email to Brooke, cluster by cluster, with what is open, who is holding it, and what has to happen before this can close."* Correctly worded as **draft** (StarPM Gmail exposes `create_draft` with no send tool). No prompt ask requires reading an email body; the evidence chain is Linear + Slack + Airtable + Calendar. |
| 5 | Channel-lock-in — name the destination descriptively | **HONOURED** | *"post where this stands in **the channel the push has been running in**"* — descriptive, no name, no id. The trap is live: the push runs in C001 `#maintenance` (kickoff, wrap, field note, filter post, 6/19 updates all verified in C001) while Jaime's habitual channel per her brief is C004 `#make-ready`. |
| 6 | Do not build on OPS-91 | **HONOURED** | The prompt makes **no West-cluster assertion at all**. Its West-related content is entirely derivable from the general asks *"cluster by cluster"* and *"Work out what is actually finished and what is not."* Nothing anchors on OPS-91's inverted state/prose pair. |
| 7 | Do not build on an absence | **HONOURED** | Every ask is a positive determination — *"I need to know where every piece of it stands"*, *"Work out what is actually finished and what is not"* — and every write is a positive artifact. The absences (no restock bill, no follow-up issue for the two North units, no reply on OPS-56's access-notice ask) are reached *through* positive evidence (John's "before I can finish the run", Jaime's own field note) and function as corroboration, never as the answer. |
| **7a** | **HIGHEST RISK — never claim "nothing on the push is closed"** | **HONOURED** | Exact sentence: *"That came and went yesterday and **it is still sitting open**."* Referent of "it" is the Push as an initiative, and the claim is true: `proj_003` state = `backlog`; ~30 push-adjacent issues sit in non-Done states; Brooke's 2026-06-19 post and OPS-186 both frame it as not closed out. The prompt does **not** say nothing is closed, does **not** enumerate issue states, and asserts **nothing** about OPS-40 or OPS-91 — both of which I confirmed are genuinely `Done` (`completed_at` 2026-05-18 and 2026-05-28). The Task 39 overclaim pattern is **not** repeated. This is the constraint I checked hardest; it is clean. |
| **8** | **HIGHEST RISK — soft verbs on the authority anchor** | **HONOURED** | *"I logged both cluster spot-checks as passing in late May and **my read is** that my part of it is finished."* Two soft constructions: "I logged … as passing" is literally true of OPS-87 (title "South and North cluster HVAC QC spot-checks - both passed", created 2026-05-24) and OPS-98 (2026-05-25); "my read is" is an explicit opinion marker, not a completed-action assertion. The forbidden hard form ("my QC side **is** finished") is absent. Additionally *"The crew **called** the HVAC run wrapped"* is reported speech attributing the claim to the crew rather than asserting it. Every authority anchor in the prompt is soft, which is why Truthfulness holds at 5. |
| **9** | **HIGHEST RISK — no escape-valve clause** | **HONOURED** | Closest sentence quoted and ruled in the B4 counter-check above: *"Work out what is actually finished and what is not, and get our tracking to match."* Unconditional, deliverable-bound, signals no uncertainty, names no surface, and points at field-completion state rather than at the Linear `state_id` column. The L29 shape ("if anything changes the read, say so plainly") is absent from the prompt entirely. |
| 10 | Similarity pivot under 40% | **HONOURED** | `_aux/Similarity_Report.json` max composite = **27.2** (vs `QC_Tasks/V3_Tasks/Task12_6a29448b7e4c641c30eb3890`), band `below_40` → INVALIDATE. Under the ceiling with 13 points of margin. |

**10 of 10 HONOURED. Zero VIOLATED.**

---

## [B6] Upstream propagation

**No blocking `PROPAGATE TO` flags raised.**

Two data-hygiene findings have root causes upstream of S1. I am explicitly **not** classifying either as a B6 propagation flag, and I state the reasoning so it can be overruled:

**H1 — `_aux/Fact_Ledger.json` `lifecycle.today` is `null`.** The ledger builder did not populate the lifecycle date for this StarPM task (`{"today": null, "closed_periods": [], "open_periods": [], ...}`).

**H2 — `Validators/validate.py:464` falls back to a hardcoded Brookfield date.** `today_from_ledger = ledger_for_date.get("lifecycle", {}).get("today") or "2026-06-12"`. With H1 in play, the prompt validator therefore emits *"resolve against universe today `2026-06-12`"* — wrong for this universe. Note that `Validators/universes.py` **already carries the correct value** for starpm (`"today": "2026-07-01"`, `"today_tz": "America/Chicago"`), so the fallback is bypassing an authority that exists.

**Why these are not B6 flags.** The protocol's B6 trigger is an issue whose root cause makes the *deliverable under review* wrong and therefore requires re-running an upstream phase. Neither does. The prompt's dates are correct against 2026-07-01 and were verified independently against `_aux/Universe_Index/today_horizon.json` and `Evals_starpm/1`. Re-running S0 would not change one word of the prompt. Classifying these as blocking would stop a clean deliverable over a diagnostic-surface defect.

**Why they still must be fixed.** The validator's own note calls Fact_Ledger *"the single date-alignment source for prompt + OE + rubrics."* If S2 or S3 date-anchors to it, they will receive `null` and see `2026-06-12` asserted — a live path to embedding a wrong date in an OE or rubric.

**Fixes:**
1. Backfill `_aux/Fact_Ledger.json` → `lifecycle.today = "2026-07-01"` (one field; no phase re-run).
2. Change `Validators/validate.py:464` to read `get_universe_constants(detect_universe(task_dir))["today"]` instead of the hardcoded `"2026-06-12"`.
3. **Binding instruction to S2 and S3:** date-anchor to `_aux/Universe_Index/today_horizon.json` (`2026-07-01`), not to Fact_Ledger, until fix 1 lands.

---

## Issues

### Major

**None.**

### Moderate

**MODERATE-1 — `linear.save_issue` `assignee` parameter is typed `"null"` in the tool catalog.**
*Location:* `StarPM_Base_Universe/7_Server_Tools_Details.json` → `save_issue.parameters.assignee` = `{"required": "optional", "type": "null"}`. I swept the entire catalog: this is the **only** parameter across ~250 tools carrying that type, so it is unlikely to be a formatting artifact.
*Impact:* if the sandbox honours the signature, an agent cannot set a structured assignee, which touches the prompt's *"with the person who owns that work named on it."*
*Why Feasibility still scores 5:* the prompt says **"named on it"**, not "assigned to it". That is satisfiable by writing the owner's name into the issue title or description, which every agent can do. The ask has an escape by construction.
*Fix (S2 + S3, no prompt change):* the OE must write the owner's name into the follow-up issue's description text and must not depend on the `assignee` field. No rubric may test `assignee_id`; phrase as *"The Agent names <person> as the owner on the follow-up item for <work>."*

**MODERATE-2 — "My own spot-check records" admits a 3-record and a 5-record reading.**
*Location:* prompt para 3, *"My own spot-check records are part of that, with a short note left on each one saying where it landed and why."*
*Detail:* Jaime is assignee on exactly OPS-87, OPS-96, OPS-98. OPS-99, OPS-108 and OPS-51 narrate her spot-checks in the third person while assigned to Elias Navarro / Brooke Phillips.
*Why not a Clarity fail:* "my own" is a strong possessive and the near-duplicates read as someone else's record; the variant is a superset that adds writes without changing or removing any, so all deliverables are identical under the guardrail.
*Fix (S3, no prompt change):* require a note on each of OPS-87 / OPS-96 / OPS-98 as three atomic rubrics (per constraint 2 / F8), and record an explicit accept-band that additional comments on OPS-99 / OPS-108 / OPS-51 are **not** penalised. Encode the accept-band in the OE so the judge sees it.

**MODERATE-3 — the calendar write has a free timestamp.**
*Location:* prompt para 4, *"put a slot on my calendar to go back out and re-inspect whatever ends up in that follow-up."*
*Detail:* owner, calendar and subject are determinate; date, time, duration and attendees are not, and the prompt supplies no date.
*Fix (S3, no prompt change):* grade the event on three things only — it is created on Jaime's calendar (`jaime.salinas@starpm.com`), its subject is a re-inspection of the field-flagged follow-up items, and its start date is on or after 2026-07-01. Never test an exact timestamp. Do not author any rubric asserting the slot is conflict-free, since 2026-07-15 Mesa Vista 4C and 2026-07-23 Q3 Planning both sit in the window.

**MODERATE-4 — the L31 beat's retraction wording is supplied by the prompt.**
*Location:* prompt para 6, *"say straight out that my earlier sign-off does not hold and this should not be treated as closeable yet."*
*Detail:* handing Gemini the exact phrasing could inflate its apparent pass rate on the retraction criterion.
*Why no prompt change:* (i) L31's Task 39 evidence shows Gemini failing 6/6 even with the phrasing present in the rubric — the failure is behavioural, not lexical; (ii) the clause is **gated behind** the Lever 2 determination, so a run that concludes "pass" never reaches it. Removing the wording would weaken the anti-hedging instruction that makes the beat forcing in the first place.
*Fix (pre-registration for S4, per StarPM item 20):* if a Gemini run issues the retraction, score it as prompt-supplied wording rather than L31 surviving, and re-attribute that run's difficulty to Lever 2. Write this into the S4 calibration now, not retrospectively.

### Minor / Notes

- **N1 — validator bolt-on WARN is a false positive.** The WARN fires on *"End of June was the target to have the Preventive Maintenance Push closed out. That came and went yesterday and it is still sitting open."* Remove-sentence test: deleting it strands *"Before I put my name to this closing out"* with no antecedent and removes the entire reason the request is happening today. It is the situational premise. The heuristic misfires because subsequent paragraphs carry the entity by pronoun ("this", "it") rather than by repeating the name. Record in `Tasks/_meta/Linter_Justifications.md`; no change.
- **N2 — Fact_Ledger / validator date wiring.** See B6 H1 + H2 with fixes.
- **N3 — projected Linear share is 47%, not the Plan's 34%.** Breadth gate still passes (5 services ≥ 5% against a threshold of 4; dominant 47% against a 60% ceiling). The Plan's "keep Linear under 35%" instruction was optimistic given that the core question resolves in a Linear column and 3 of 6 writes are Linear writes. No action.
- **N4 — base-universe duplicate rows.** GCalendar events repeat 3–6× per logical event, and OPS-99 / OPS-108 and OPS-51 / OPS-71 are identical-title pairs in opposing states. These are base-universe noise (Lever 6 flavour), not CB edits — `4_Changelog.json` is empty. Per the QC spec's coherence note, well-supported data beats low-support contradiction, so this does not count as a contradiction. Universe Cross-service Coherence holds at 5.
- **N5 — Airtable `tblMaintenanceTickets` has only 4 fields** (Ticket Number, Description, Priority, Completion Date): no owner, no unit, no status. The prompt correctly attaches the owner requirement to the *tracking item* (Linear) rather than to the ticket. S2 must not write an owner field on the Airtable row.

---

## Role-lens roll-up

| Lens | Finding |
|---|---|
| **Architect** | Structure fits V4 cleanly. Six short paragraphs, one situation, escalating from premise → investigation → writes → communication → tone directive. No bolt-on. Abstractions correct: "tracking item" and "maintenance ticket log" are established as distinct terms before being contrasted. |
| **Implementer** | Runs. All six writes map to real tools. Recipient resolvable (one Brooke in 61 contacts). Channel resolvable (C001). Calendar resolvable (`jaime.salinas@starpm.com`). One catalog wrinkle surfaced — `save_issue.assignee` typed `"null"` (MODERATE-1) — with a working escape via "named on it". |
| **Red-team** | Six attacks mounted (four assigned, two self-generated). All six fail. The conditional in para 6 is the only structure that could fork the end-state, and the universe closes it on four independent grounds. |
| **Ground-truth** | Every claim re-derived from `_aux/Universe_Split/`, not from the Hardness Plan. 12 tight identifiers grepped, zero phantoms. Constraint 7a's overclaim risk checked against OPS-40 and OPS-91 directly and found clean. |
| **Integration** | Prompt ↔ Hardness_Plan consistent: 10/10 constraints honoured, 5/5 levers preserved, density in-band, breadth in-band. Four Moderate findings all resolve downstream at S2/S3 without re-running S1. |

---

## Verdict

**GO.**

- B1 — all 14 applicable sub-dims at 5; every hard gate in `Evals_starpm/1` executed literally and passed.
- B2 — no adversarial divergence; the closing conditional is universe-determinate on the negative branch.
- B3 — projected midpoint 50 combined (Opus 54, Gemini 46); **PASS** on both models under StarPM v4 bands; breadth PASS at 7 services exercised, 5 at ≥ 5%, dominant 47%.
- B4 — 5/5 levers preserved, L31 beat present and forcing, escape-valve counter-check clean.
- B6 — no blocking propagation flags; two data-hygiene fixes recorded with reasoning for the non-blocking classification.
- Constraints — 10/10 honoured, including all three highest-risk ones (7a, 8, 9).

Four Moderate issues are recorded. **None requires a prompt edit**; all four are downstream instructions binding on S2 and S3.

```json
{
  "phase": "prompt",
  "council": "B",
  "task_dir": "Tasks/44_6a62ccba8cad60844b8364b9",
  "verdict": "GO",
  "perspectives": {
    "B1": {
      "status": "PASS",
      "findings": []
    },
    "B2": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MINOR",
          "location": "prompt:para3",
          "issue": "'My own spot-check records' admits a 3-record (Jaime-assigned OPS-87/96/98) and a 5-record reading (adding Elias-assigned OPS-99/108 which narrate her spot-checks)",
          "fix": "S3 writes three atomic note rubrics on OPS-87/96/98 and records an explicit accept-band that extra comments on OPS-99/108/51 are not penalised",
          "propagate_to": null
        },
        {
          "severity": "MODERATE",
          "location": "prompt:para4",
          "issue": "Calendar write fixes owner, calendar and subject but leaves date/time entirely free",
          "fix": "S3 grades on Jaime's calendar + re-inspection subject + start date on or after 2026-07-01; never an exact timestamp; no conflict-free assertion",
          "propagate_to": null
        }
      ]
    },
    "B3": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "_aux/Hardness_Plan.md:Service Breadth",
          "issue": "Plan projects linear at 34% and instructs 'Linear under 35%'; independent projection puts it at 47%",
          "fix": "None required - breadth gate still passes (5 services >=5%, dominant under the 60% ceiling); record the corrected figure at S4",
          "propagate_to": null
        }
      ]
    },
    "B4": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MODERATE",
          "location": "prompt:para6",
          "issue": "L31 retraction beat supplies the exact negative-directive wording, which could inflate Gemini's apparent pass rate on the retraction criterion",
          "fix": "No prompt change - the clause is gated behind the Lever 2 determination. Pre-register for S4: if Gemini issues the retraction, score as prompt-supplied wording and re-attribute to Lever 2",
          "propagate_to": null
        }
      ]
    },
    "B6": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "_aux/Fact_Ledger.json:lifecycle.today",
          "issue": "lifecycle.today is null, so Validators/validate.py:464 falls back to hardcoded '2026-06-12' and misreports the universe date for this StarPM task",
          "fix": "Backfill lifecycle.today = '2026-07-01'; change validate.py:464 to read get_universe_constants(...)['today']; until then S2/S3 must date-anchor to _aux/Universe_Index/today_horizon.json. Not classified as a blocking B6 flag because the deliverable's dates are correct and no phase re-run would change the prompt",
          "propagate_to": null
        }
      ]
    },
    "Implementer": {
      "status": "NOTE",
      "findings": [
        {
          "severity": "MODERATE",
          "location": "StarPM_Base_Universe/7_Server_Tools_Details.json:save_issue.assignee",
          "issue": "save_issue.assignee is typed 'null' - the only parameter in the ~250-tool catalog with that type - so a structured assignee may not be settable",
          "fix": "Prompt says 'named on it', not 'assigned to it', so the ask has an escape. S2 writes the owner name into the issue description; no S3 rubric may test assignee_id",
          "propagate_to": null
        }
      ]
    }
  },
  "scores": {
    "unique_ground_truth": {
      "score": 5,
      "scheme": "1/3/5",
      "reason": "end-state divergence gate enumerated four readings; all converge on one final universe state and the universe determinately fires the negative branch of the closing conditional"
    },
    "feasibility": {
      "score": 5,
      "scheme": "1/3/5",
      "reason": "every ask maps to a real StarPM tool and every required fact is materialized; T10 dimensional gate passes on the cluster dimension across South/North/East/West"
    },
    "explicit_tool_mention": {
      "score": 5,
      "scheme": "1/5",
      "reason": "zero service names, tool function names, parameter names or internal IDs in the prompt body"
    },
    "prompt_clarity_and_specificity": {
      "score": 5,
      "scheme": "1/3/5",
      "reason": "write-action divergence and delegation-clarity hard gates both clean; zero 'I'll [verb]' statements"
    },
    "contrived_unnatural": {
      "score": 5,
      "scheme": "1/3/5",
      "reason": "no command list, no numbered steps, no exact-timestamp or format constraints; difficulty is scattered information plus prose-versus-state conflict"
    },
    "truthfulness": {
      "score": 5,
      "scheme": "1/3/5",
      "reason": "phantom tight-identifier grep clean across 12 identifiers; zero major and zero minor errors; every authority claim soft-verbed and literally true of what was logged"
    },
    "tool_use_cross_service": {
      "score": 5,
      "scheme": "1/5",
      "reason": "7 of 8 services exercised and the load-bearing conclusion is unreachable inside any single service"
    },
    "investigation": {
      "score": 5,
      "scheme": "1/5",
      "reason": "not pre-solved; the prompt asserts the opposite of the ground truth and every write depends on an investigation it does not shortcut"
    },
    "coherence": {
      "score": 5,
      "scheme": "1/5",
      "reason": "remove-sentence test run on all six paragraphs; the validator bolt-on WARN is a false positive since removing the opener strands 'Before I put my name to this closing out'"
    },
    "persona": {
      "score": 5,
      "scheme": "1/3/5",
      "reason": "a QC inspector deciding whether to sign off or kick back is the literal centre of Jaime's brief; voice matches at 313 words, short declaratives, zero emoji"
    },
    "business_function": {
      "score": 5,
      "scheme": "3/5",
      "reason": "QC sign-off reconciliation plus field re-inspection sits squarely inside '3 - Quality Control & Field Services'"
    },
    "alignment_with_todays_date": {
      "score": 5,
      "scheme": "1/3/5",
      "reason": "all six relative phrases resolve cleanly against 2026-07-01 with confirmed universe data in every resolved window"
    },
    "universe_data_exists": {
      "score": 5,
      "scheme": "1/5",
      "reason": "every fact required by the trajectory is materialized in _aux/Universe_Split/ and reachable through the StarPM tool catalog"
    },
    "universe_cross_service_coherence": {
      "score": 5,
      "scheme": "1/5",
      "reason": "4_Changelog.json is empty and the inject SQL is template-only, so there are no CB edits capable of creating a contradiction"
    }
  },
  "density_projection": {
    "midpoint": 50,
    "band": "PASS",
    "breadth_services": 7,
    "breadth_band": "PASS",
    "per_model": {
      "opus": {
        "midpoint": 54,
        "band": "PASS"
      },
      "gemini": {
        "midpoint": 46,
        "band": "PASS"
      }
    },
    "range_low": 31,
    "range_high": 68,
    "dominant_service": "linear",
    "dominant_share_pct": 47,
    "services_at_or_above_5pct": 5,
    "hardness_plan_midpoint": 55.5,
    "scheme": "starpm_v4_per_model"
  },
  "lever_preservation": {
    "expected": 5,
    "preserved": 5,
    "missing": [],
    "levers": {
      "lever_2_structured_db_skip": "PRESERVED",
      "lever_9_authority_dismissal_persona_self": "PRESERVED",
      "lever_1_latching_loudest_wrap": "PRESERVED_STRENGTHENED",
      "lever_8_multi_link_chain": "PRESERVED",
      "lever_5_thread_reply_blindness": "PRESERVED"
    },
    "l31_retraction_beat": "PRESENT_AND_FORCING",
    "escape_valve_counter_check": "CLEAN",
    "constraints_honoured": 10,
    "constraints_violated": 0
  },
  "bucket_1_risk_pct": null,
  "iteration": 1,
  "timestamp": "2026-07-26T00:00:00-05:00"
}
```
