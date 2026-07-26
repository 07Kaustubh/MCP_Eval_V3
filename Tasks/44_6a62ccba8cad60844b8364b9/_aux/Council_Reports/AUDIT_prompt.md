# PIPELINE AUDIT — Veteran QC Second-Opinion · `--phase prompt`

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** `starpm` (V4, dual-model) · **Universe today:** 2026-07-01 (America/Chicago)
**Deliverable:** `Tasks/44_6a62ccba8cad60844b8364b9/5_Prompt.txt` (313 words, 14 sentences, 6 paragraphs)
**Persona:** Jaime Salinas · Quality Control Inspector · `p_007` · `jaime.salinas@starpm.com` · BF 3 Quality Control & Field Services
**Prior verdicts re-examined:** Council A GO, Council B GO. **This audit does not inherit either.**

**Density scheme applied:** StarPM V4, **per model** — midpoint >= 40 PASS · 15-39 THIN · < 15 INSUFFICIENT (AGENTS.md hard rule 11; AUDIT.md framework-scoping note). The V3-family 50/40 bands are **not** applied.

**VERDICT: PASS (STRICT)** — 0 BLOCKER · 0 sub-dim < 5 · 5/5 levers trace with cited evidence · density PASS on both models (Opus 47, Gemini 41, combined 44). **15 findings recorded**, of which 3 MODERATE and 3 MINOR bind downstream on S2/S3. **No edit to `5_Prompt.txt` is required.**

---

## Pre-declared inputs and known defect

| Item | Status |
|---|---|
| `validate.py --phase prompt` | PASS · 0 fails · **1 WARN** · **6 NOTES** — each treated as a hard issue below |
| `verify_universe_atoms.py` | PASS · 0 fails · 0 warns · **0 atoms checked** — vacuity assessed at A-10 |
| `calc_similarity.py` | max composite **27.2** (top match `QC_Tasks/V3_Tasks/Task12_6a29448b7e4c641c30eb3890`), corpus 44, band `below_40` → INVALIDATE. Under the 40 ceiling and under the 35 AUDIT-trigger band. Verified from `_aux/Similarity_Report.json`. |
| **LENS 8 regression-anchor suite** | **62 passed, 0 failed out of 62** (already run this pass; recorded verbatim, not re-run) |
| **KNOWN DEFECT (pre-declared, not re-derived)** | `_aux/Fact_Ledger.json` `lifecycle.today = null` → `Validators/validate.py:464` prints the hardcoded Brookfield fallback `2026-06-12` in NOTES 4 and 5. **That fallback is wrong for this universe.** `_aux/Universe_Index/today_horizon.json` `{"universe_today": "2026-07-01", "universe_timezone": "America/Chicago"}` is authoritative and every check below resolves against it. Recorded as **surfaced discrepancy A-11**, not a prompt defect. |
| OE / Rubrics | `6_Oracle_Events.txt` and `7_Rubrics.json` are unfilled templates. LENS 3 OE and rubric columns are **N/A at S1**; what S2/S3 must carry is stated per lever. |

**Every validator WARN and NOTE, adjudicated:**

| # | Kind | Text | Strict adjudication |
|---|---|---|---|
| W1 | WARN | bolt-on candidate on sentence 1 | **FALSE POSITIVE** — independently re-derived below (not inherited). No edit. |
| N1 | NOTE | universe: starpm | Correct. `_aux/Universe.txt` = `starpm`. |
| N2 | NOTE | word count 313 | Under the 500 hard cap. PASS. |
| N3 | NOTE | 313 over 300, "could still be tightened" | Advisory. Removal test run on all 14 sentences: only S5 survives grammatically, and S5 plants Lever 1. Nothing is cuttable without losing a write ask or a coreference anchor. **No action.** |
| N4 | NOTE | relative date `yesterday` vs universe today `2026-06-12` | **Anchor is wrong** (pre-declared defect). Against the authoritative 2026-07-01, `yesterday` = **2026-06-30** = end of June. In-window data confirmed: OPS-186 (2026-06-17) and Brooke C001 `1781899601.000096` / `1781902061.000097` (2026-06-19) both state the end-of-June target. **Prompt correct.** |
| N5 | NOTE | relative date `today` vs universe today `2026-06-12` | Same. `today` = **2026-07-01**. In-window data: 3 Jaime-owned issues live, ~21 push-adjacent issues in non-Done states. **Prompt correct.** |
| N6 | NOTE | distinct services referenced: 2 | **Inverted-signal regex artifact.** My own sweep of the prompt for service/tool tokens returns zero hits except lowercase "calendar" in "my calendar" (natural noun, not a service name). The prompt names **zero** services — which is exactly why Explicit Tool Mention scores 5. The five write surfaces are all descriptive ("tracking item", "our maintenance ticket log", "my calendar", "the channel", "an email"). **No defect.** |

---

## LENS 1 — Strict QC scoring

Scored against `Docs_starpm/7_QC_Spec_Doc1.json` with every "should" in `Evals_starpm/1_Prompt_Eval.md` read as "must" and every soft convention in `Reference/Prompt_Format.md` read as binding.

### 1.1 PER-ATOM EVIDENCE TABLE (mandatory for Truthfulness)

Every factual claim in the prompt. Every row personally retrieved from `_aux/Universe_Split/` by `json.loads` on `row_data` during this audit. **No row inherited from either council's table.**

| # | Atom asserted | Universe query | Row excerpt (retrieved) | Verdict |
|---|---|---|---|---|
| 1 | "Preventive Maintenance Push" is a real initiative | `linear.linear_projects` WHERE `name LIKE '%Preventive Maintenance%'` | `proj_003` · name `"Preventive Maintenance Push"` · state `"backlog"` | **PASS** (tight identifier, exact string) |
| 2 | "End of June was the target to have [it] closed out" | `linear.linear_issues` WHERE `id='OPS-186'` → `description`; `slack.slack_messages` ts `1781899601.000096`, `1781902061.000097` | OPS-186: *"The goal is to have every open issue resolved and closed out before the end of June."* (created 2026-06-17T19:50:45-05:00) · Brooke C001 2026-06-19: *"Goal is to close everything out before end of June."* | **PASS** |
| 3 | "That came and went yesterday" → 2026-06-30 | `_aux/Universe_Index/today_horizon.json` | `{"universe_today":"2026-07-01","universe_timezone":"America/Chicago"}` → yesterday = 2026-06-30 = end of June | **PASS** |
| 4 | "it is still sitting open" (the Push, as initiative) | `linear.linear_projects.proj_003.state`; `linear.linear_issues` state sweep across the push set | `proj_003.state="backlog"` · OPS-186 Todo · OPS-35 In Progress · OPS-43 In Progress · OPS-56 In Progress · OPS-97 Todo · OPS-87 Todo · OPS-96 Todo · OPS-98 In Progress · OPS-108 Backlog · OPS-44 Backlog · OPS-17 In Progress | **PASS** |
| 4a | **Constraint 7a counter-check** — does the prompt overclaim "nothing is closed"? | `linear.linear_issues` WHERE `id IN ('OPS-40','OPS-91')` | OPS-40 `state_OPS_4` Done `completed_at=2026-05-18T11:54:26.202206-05:00`; OPS-91 `state_OPS_4` Done `completed_at=2026-05-28T21:37:11.901732-05:00` — **both genuinely Done.** Prompt says only *"it is still sitting open"* about the **initiative**, never that nothing on it is closed, and enumerates zero issue states. | **PASS — Task 39 overclaim NOT repeated** |
| 5 | "Brooke started this in early May" | `slack.slack_messages` ts `1778171944.000091`; `linear.linear_issues.OPS-40.description` | Brooke Phillips, `created_at 2026-05-07T16:39:04+00:00`, C001: *"the Preventive Maintenance Push is officially moving into active execution"* · OPS-40 desc: *"as part of the portfolio-wide push Brooke kicked off this week"* | **PASS** |
| 6 | "HVAC, plumbing and electrical across the whole portfolio" | same Slack row | verbatim: *"kicking off the portfolio-wide HVAC, plumbing, and electrical audit before summer heat hits"* | **PASS (verbatim match)** |
| 7 | "I have been the QC eye on it" | `linear.linear_issues` WHERE `assignee_id='user_d3186a640f425ae0b69423f09aa4d7ec'`; kickoff mentions; `linear.linear_comments.OPS-108` | Jaime assignee on exactly OPS-87 / OPS-96 / OPS-98 · kickoff @-mentions `@Jaime Salinas` · OPS-108 comment: *"Moving this to In Review for Jaime to look over"* · OPS-99 desc: *"Jaime pulled a spot-check across the East cluster units"* | **PASS** |
| 8 | "I logged both cluster spot-checks as passing in late May" | `linear.linear_issues` OPS-87, OPS-98 titles + `created_at`; `linear.linear_comments` OPS-98 | OPS-87 title *"South and North cluster HVAC QC spot-checks - both passed"*, created `2026-05-24T15:45:34-05:00` · OPS-98 title *"QC spot-checks complete - South and North clusters closed"*, created `2026-05-25T08:55:00-05:00` · OPS-98 comment 2026-05-25T09:00 (author = Jaime Salinas): *"Everything cleared QC, so I've moved both cluster issues to Done."* | **PASS** — asserts only what she **logged**; literally true of the prose |
| 9 | "my read is that my part of it is finished" | `linear.linear_issues` state + `completed_at` on Jaime's three | OPS-87 `state_OPS_1` **Todo** `completed_at=null` · OPS-96 `state_OPS_1` **Todo** `completed_at=null` · OPS-98 `state_OPS_2` **In Progress** `completed_at=null` | **PASS AS BELIEF.** Soft-verbed ("my read is") per constraint 8 / Learnings L24. False as fact — which is Lever 9 — true as a statement of her reading. Not a Truthfulness defect. |
| 10 | "The crew called the HVAC run wrapped around the same time" | `slack.slack_messages` ts `1779308446.000005`, `1779308447.000006`; `contacts.contacts` Elias | Elias Navarro (Lead Maintenance Technician), C001 `created_at 2026-05-20T20:20:46+00:00`: *"Alright, all three clusters are done. Every unit serviced"* and T20:20:47: *"Summer HVAC push is a wrap. All three clusters done, 34 units total serviced."* Gap to her 5/24-5/25 logs = 4-5 days, inside the soft qualifier "around" | **PASS** (reported speech, literally true) |
| 11 | "our maintenance ticket log" exists | `airtable.airtable_tables` | `tblMaintenanceTickets` · name `"Maintenance Tickets"` · desc *"Ongoing maintenance requests and issue tracking. System of record for maintenance work orders; Linear is secondary."* · 50 records in `airtable.airtable_records` | **PASS** |
| 12 | "tracking item" ≠ ticket (the contrast the prompt draws) | `linear.linear_teams.team_001.description` | *"Maintenance work orders are tracked in the Airtable Maintenance Tickets table, which is the system of record. Linear is secondary for maintenance items and is used for broader operations and project tracking."* | **PASS** — the contrast is universe-grounded from both sides |
| 13 | "my calendar" exists and is hers | `gcalendar.gcalendar_calendars` | `id="jaime.salinas@starpm.com"` · `primary=true` · `access_role="owner"` · `time_zone="America/Chicago"` | **PASS** |
| 14 | "the channel the push has been running in" resolves uniquely | `slack.slack_messages` GROUP BY `channel_id` on push keywords | **C001 `#maintenance` = 16** push-keyword messages (kickoff, Elias wrap ×2, Jaime field note, John filter post, Brooke filter reply, Lisa 5/27, Carlos 5/31, Brooke 6/3, Brooke 6/19 ×2 …). C007 = 3 (one incidental budget mention of the push budget). C003 = 4 (unrelated). Only 2 messages anywhere name "Preventive Maintenance Push": C001 kickoff and one C007 budget aside. | **PASS — unambiguous** |
| 15 | "Brooke" is emailable and unique | `contacts.contacts` | `brooke.phillips@starpm.com` · job `"Apartment Property Supervisor"` · **exactly 1 of 61 contacts** matches "Brooke" → no first-name collision, so no Minor→Major escalation under the 06/10 rule | **PASS** |
| 16 | "the person who owns that work" is knowable | ownership sweep across `linear.linear_issues` + `linear.linear_comments` + `slack.slack_messages` | Owners exist for every open item, but are **multi-valued** (see A-1). The prompt asserts nothing about who owns what, so this is not a Truthfulness defect. | **PASS (prompt-side); flagged as S3 hazard A-1** |
| 17 | Gmail is a write surface only | `gmail.gmail_messages` push sweep (484 rows); `7_Server_Tools_Details.json` gmail writes | Zero push-related Gmail messages. Gmail write set = `create_draft`, `create_label`, `update_label`, `delete_label` — **no send tool exists**, so the prompt's "draft an email" is the only feasible phrasing and is correct | **PASS** |

**Zero major factual errors. Zero minor factual errors. Zero misleading statements. Truthfulness = 5.**

**What the prior councils missed on this table:** Council A's A3 row 3 asserts a proj_003 membership list that is **factually wrong** — OPS-35 and OPS-99/OPS-108 are `proj_002`, OPS-56 is `proj_002`, and OPS-97/OPS-98/OPS-186 are `proj_001`. Only OPS-17, OPS-43, OPS-44, OPS-87 and OPS-96 of its cited list are actually in `proj_003`. The **conclusion** ("still sitting open") survives — I re-derived it from `proj_003.state="backlog"` plus the per-issue state sweep — but the evidence was mis-cited. Recorded as **A-12**.

### 1.2 Sub-dimension scores

Format: `SUB-DIM -> SCORE -> ONE-LINE REASON -> WHAT THE PRIOR COUNCIL MISSED`.

```
SUB-DIM Unique Ground Truth -> 5/5 (1/3/5, no middle band since 06/09)
  REASON: Four readings enumerated; all converge on one end-state, and the universe closes the
          closing conditional on the negative branch on four independent grounds (state column,
          unfinished filter run, undispositioned field flag, West coverage gap).
  MISSED: Neither council traced Lever 8 hop B to a concrete record. I did (OPS-34, see A-8) and
          it confirms the negative branch is derivable, not merely asserted.

SUB-DIM Feasibility -> 5/5 (1/3/5)
  REASON: All six writes map to real StarPM tools (save_issue, save_comment,
          create_records_for_table, create_event, create_draft, slack_send_message); T10
          dimensional gate passes on the cluster dimension (South/North/East/West all carried as
          literal text in issue titles/descriptions); no conflicting instruction.
  MISSED: Council B flagged `save_issue.assignee` typed `"null"` as MODERATE-1. I confirmed it
          from the catalog and confirmed it is harmless: the prompt says "named on it", not
          "assigned to it", and save_issue's own description lists assignee as a settable field.
          Neither council checked the OTHER catalog constraint that matters: `list_issue_statuses`
          has `team` as a REQUIRED parameter, so decoding state_OPS_* costs a `list_teams` call
          first. That is +1 to the Lever 2 discovery cost, not a defect.

SUB-DIM Explicit Tool Mention -> 5/5 (1/5 binary)
  REASON: Independent regex sweep of the prompt body: 0 tool function names, 0 MCP server names,
          0 parameter names, 0 internal IDs (OPS-\d+, C\d{3}, rec[a-f0-9]{6,}, tbl\w+, proj_\d+,
          state_OPS), 0 ISO dates, 0 dollar amounts, 0 non-ASCII characters.
  MISSED: nothing.

SUB-DIM Prompt Clarity and Specificity -> 5/5 (1/3/5)
  REASON: Write-action-divergence gate and delegation-clarity gate both clean (0 "I'll [verb]" /
          "I will" / "I am going to" hits). Three residuals exist (record-set boundary, owner
          attribution, routing partition) but each is bounded by a discriminator the prompt itself
          supplies, and none produces a write-vs-no-write or act-vs-defer fork.
  MISSED: BOTH councils examined the "my own spot-check records" ambiguity only in the SUPERSET
          direction (3 -> 5, adding OPS-99/OPS-108). Neither examined the SUBSET direction
          (3 -> 2), which is the dangerous one because it DROPS a deliverable. See A-4.
          Neither council examined owner-attribution determinacy (A-1) or the Linear-vs-Airtable
          routing partition item by item (A-2). All three are logged, none reaches the FAIL band.

SUB-DIM Contrived / Unnatural Prompts -> 5/5 (1/3/5)
  REASON: No command list, no numbered steps, no "First... Then...", no exact-timestamp demand, no
          format constraint, no behaviour no real employee would exhibit. Difficulty is entirely
          scattered information plus prose-versus-state conflict.
  MISSED: nothing.

SUB-DIM Truthfulness -> 5/5 (1/3/5)
  REASON: 17-atom evidence table above, every row personally retrieved. Zero major, zero minor.
  MISSED: Council A mis-cited project membership on its "still sitting open" row (A-12). The claim
          holds on re-derivation; the citation did not.

SUB-DIM Tool use and Cross-service requirement -> 5/5 (1/5 binary)
  REASON: The load-bearing conclusion is unreachable inside any single service - it requires
          joining Linear state_id, Linear prose (descriptions + comments), Slack top-level posts,
          Slack thread replies and Calendar agendas. 7 of 8 services exercised.
  MISSED: nothing.

SUB-DIM Investigation -> 5/5 (1/5 binary)
  REASON: Not pre-solved. The prompt asserts the OPPOSITE of the ground truth ("my read is that my
          part of it is finished") and names no root cause, no count, no open item, no culprit.
  MISSED: nothing.

SUB-DIM Coherence -> 5/5 (1/5 binary)
  REASON: Validator WARN independently re-adjudicated - see 1.3 below. Not inherited.
  MISSED: nothing; both councils reached the same answer, and my independent derivation confirms
          it with a fact neither stated (see 1.3).

SUB-DIM Persona -> 5/5 (1/3/5)
  REASON: "Either signs off on marketing-ready status or kicks work back" is the literal centre of
          Jaime's brief (StarPM_Base_Universe/2_..PERSONA BRIEFS.md:183); the prompt's climax is
          exactly that decision. Voice matches: 313 words, short declaratives, observation-first,
          zero emoji, formality ~0.55. She is an authoring persona (7 actions / 7 scenarios), not
          an NPC.
  MISSED: nothing.

SUB-DIM Business Function -> 5/5 (3/5 scheme, no FAIL band)
  REASON: assigned=3, prompt_primary=3. Category 3 is Jaime's HOME function and
          3_StarPM_TASK CATEGORIES.md:62 states "tasks are always authored from a persona's home
          Business Function, not from participant appearances". Maps to subcategory 3.2 (Property
          Inspections & Compliance - "cross-property scope") with the 3.1 signature move as the
          climax. Category 3's own Primary-systems row lists Airtable, Slack, Google Calendar,
          Linear and Gmail - the exact five write surfaces the prompt uses.
  MISSED: nothing.

SUB-DIM Alignment with Today's Date -> 5/5 (1/3/5)
  REASON: All six relative phrases resolve cleanly against 2026-07-01 with confirmed data in every
          resolved window (table in the validator-NOTE section above). Universe-level: 27 calendar
          rows / 9 unique confirmed events sit on or after 2026-07-01 and are legitimately
          forward-facing per the QC spec's explicit carve-out; nothing in the push chain post-dates
          today (latest push artifact = OPS-186, 2026-06-17).
  MISSED: nothing. NOTE that the validator's own date anchor is wrong (2026-06-12) - pre-declared
          defect A-11, not a prompt defect.

SUB-DIM Universe Feasibility (Data Exists) -> 5/5 (1/5 binary)
  REASON: Every trajectory link materialised and re-verified this pass, including the two that
          neither council pinned: Lever 8 hop B (OPS-34 comment, unique coil+plumbing+panel match)
          and the C001 thread structure (56 replies under 37 parents, re-counted).
  MISSED: The Hardness Plan's "15 distinct parents" is wrong - actual is 37 (A-13). Council B had
          this right; the Plan does not.

SUB-DIM Universe Cross-service Coherence -> 5/5 (1/5 binary)
  REASON: `4_Changelog.json` = [] and `9_Universe_inject.sql` is template-only, so there are zero
          CB edits capable of creating a contradiction. Base-universe noise (duplicate calendar
          rows, OPS-99/OPS-108 and OPS-51/OPS-71 identical-title pairs, OPS-34's title/comment
          mismatch, the dangling "#make-ready" cross-reference at A-9) is pre-existing, is not a CB
          edit, and falls under the QC spec's "well-supported data beats low-support contradiction"
          note.
  MISSED: Neither council surfaced the OPS-34 "#make-ready" dangling reference (A-9). It does not
          move the score but it binds S3.
```

**14 of 14 applicable sub-dims at 5. Zero sub-dims below 5. LENS 1: PASS.**

### 1.3 Independent re-adjudication of the bolt-on WARN (not inherited)

Validator text: *"bolt-on candidate: sentence `End of June was the target to have the Preventive Maintenance Push closed out.` shares no named entities with the rest of the prompt."*

I ran the **actual** remove-sentence test rather than the entity-overlap heuristic, and I established one fact neither council stated explicitly: **the string "Preventive Maintenance Push" appears exactly ONCE in the entire prompt — in sentence 1.** Every later reference is a lowercase coreference: "That" and "it" (S2), "this" (S3), "it" (S4, S6), "this closing out" (S6), "this" (S7), "the push" (S11), "this can close" (S9), "closeable" (S14).

Delete S1 and the prompt opens: *"That came and went yesterday and it is still sitting open."* — "That" has no antecedent, "it" has no antecedent, and **the initiative is never named anywhere in the remaining 13 sentences**. An agent could not identify what to investigate. The remainder does **not** make perfect sense, so the Coherence FAIL band ("removing a sentence doesn't change the rest") does not trigger.

**Independent verdict: NOT a bolt-on. FALSE POSITIVE. No edit to S1.** The heuristic misfires because its entity extractor matches capitalised multi-word spans only and cannot see an anaphora chain. Record in `Tasks/_meta/Linter_Justifications.md` so it is not re-litigated at S2/S3/FINAL.

Sentence 5 (*"The crew called the HVAC run wrapped around the same time."*) is the only sentence that survives a strict grammatical removal. It is inside the Context movement, introduces no new ask, describes the same situation, and is the sole prompt-side anchor for Lever 1. **NOTE only, keep as written.**

---

## LENS 2 — Answer-leakage sweep

**Derived answer under audit:** *Jaime's QC sign-off does not hold and the Preventive Maintenance Push is not closeable yet, because none of her three QC issues (OPS-87, OPS-96, OPS-98) is in a completed workflow state while every prose surface says otherwise, and because multiple field items remain open.*

Method: string-search over `_aux/Universe_Split/Universe_complete_data.json` (4.4 MB, all 8 services, every artifact an agent could read) for the aggregate conclusion and for near-neighbour phrasings. **70 + 33 = 103 patterns tested.**

| Pattern family | Patterns | Hits |
|---|---|---|
| Direct retraction ("sign-off does not hold", "signoff does not hold", "retract", "walk back", "rescind", "withdraw my sign", "my earlier sign", "prior sign-off", "previous sign-off") | 9 | **0** |
| Closeability ("not closeable", "not closeable yet", "should not be treated as closeable", "cannot be closed", "can't close", "should not be closed", "not ready to close", "push cannot close") | 8 | **0** |
| Prematurity ("premature", "premature sign", "signed off too early", "signed off prematurely", "qc was premature", "reopen the qc") | 6 | **0** |
| State contradiction ("state column", "state_id says", "workflow state says", "status field is wrong", "statuses are wrong", "tracker is wrong", "tracker does not match", "never moved to done", "still shows todo", "still shows as todo", "still in todo", "incorrectly marked", "marked done in error", "wrong status", "inaccurate status") | 15 | **0** |
| Negation of completion ("not actually done", "not really done", "wasn't actually", "was not actually", "isn't actually", "is not actually", "never completed", "incomplete qc") | 8 | **0** |
| QC verdict ("qc side is not a pass", "qc did not pass", "qc does not pass", "kick back", "kicked back", "qc gap") | 6 | **0** |
| Coverage / per-item ("none of her", "none of jaime", "three qc issues", "west cluster was never", "never walked west", "did not cover west", "filters were not", "filter run was never", "spot-check never", "jaime never", "jaime did not", "jaime's qc") | 12 | **0** |
| Record mirroring ("ops-87", "ops-96", "ops-98" outside their own rows) | 3 | **0 external** — all 12 occurrences are the issues' own `linear_issues` / `linear_comments` rows or their `git_branch_name` slugs |
| Near-miss vocabulary ("discrepan" ×51, "mismatch" ×6, "out of sync" ×2, "doesn't match" ×2, "does not match" ×1, "don't match" ×1, "failed qc" ×3, "coverage gap" ×1) | 8 | **0 relevant** — every hit contextually inspected. "failed qc" ×3 = Las Vistas 3C make-ready rework (Gmail thread `9f0bd31ccf588236` + Slack C004 `1781620200.000000`), a different program. "coverage gap" ×1 = OPS-121 "after-hours maintenance coverage gap". "discrepan" ×51: only 2 are HVAC-adjacent and both are billing (April HVAC invoice variance; Delgado HVAC credit memo CM-2026-088). Zero touch the push's QC state. |

**No artifact anywhere in the universe states the aggregate conclusion, or any component of it, in prose.** The conclusion must be assembled by joining Linear `state_id` (structured), Linear descriptions and comments (prose), Slack top-level posts, Slack thread replies, and Calendar agendas.

**LENS 2: CLEAN — zero BLOCKER.** Satisfies Learnings L6 (HARD) and AUDIT's answer-leakage bar.

---

## LENS 3 — Hardness end-to-end trace

OE and rubric columns are **N/A at S1** (`6_Oracle_Events.txt` and `7_Rubrics.json` are unfilled templates). For each lever I give the exact prompt sentence, the atoms the agent must touch, and what S2/S3 must carry. "Probably triggered" is not accepted anywhere below.

### Lever 2 — Structured-DB skip on Linear `state_id` (symmetric backbone, cost 5.5)

- **Prompt sentence (S6):** *"Before I put my name to this closing out, I need to know where every piece of it stands as of today, cluster by cluster, and I need our records saying the same thing."*
- **Prompt sentence (S7):** *"Work out what is actually finished and what is not, and get our tracking to match."*
- **Atoms the agent must touch** (all confirmed present, all in `Fact_Ledger.ids.linear_issue`): `linear.linear_issues` `state_id` on **OPS-87 = `state_OPS_1`**, **OPS-96 = `state_OPS_1`**, **OPS-98 = `state_OPS_2`**, OPS-97 = `state_OPS_1`, OPS-108 = `state_OPS_0`, OPS-44 = `state_OPS_0`; all three of Jaime's carry `completed_at = null`. Decoding requires `linear.linear_workflow_states` (5 rows: `state_OPS_0` Backlog / `_1` Todo / `_2` In Progress / `_3` In Review / `_4` Done), reachable only via `list_issue_statuses`, whose `team` parameter is **required** — so a `list_teams` call is a hard prerequisite.
- **Contradicting prose the agent meets first:** OPS-87 desc *"everything came back clean across the board. I've commented the results directly on each cluster's issue and moved both from In Review to Done."*; OPS-98 desc + comments 2026-05-25T09:00 / T14:00 *"Everything cleared QC, so I've moved both cluster issues to Done."*; OPS-96 desc + comment 2026-05-30T05:31 *"Moving this to In Review."*
- **Trigger integrity verified:** the prompt contains the words status / state / tracker field / Done / In Progress / Backlog **zero times** (regex-confirmed), and never suggests the tracker itself might be wrong.
- **S2 must carry:** `list_teams` → `list_issue_statuses` → `list_issues`/`get_issue` on OPS-87/96/98, with the decoded state names as expected values. **S3 must carry:** the determination graded on content ("her QC issues are not in a completed state"), never on a record id.
- **TRACES. PASS.**

### Lever 9 — Authority dismissal, persona-self variant (cost 4.0)

- **Prompt sentence (S4):** *"I logged both cluster spot-checks as passing in late May and my read is that my part of it is finished."*
- **Atoms:** OPS-98 comments (author_id `user_d3186a640f425ae0b69423f09aa4d7ec` = Jaime, verified) — *"airflow was solid throughout, coils came back clean, and refrigerant levels looked correct on every unit I pulled. Everything cleared QC…"* — competent, domain-correct QC vocabulary in the persona's own voice; OPS-87 description; OPS-96 comment.
- **Constraint 8 verified honoured:** two soft constructions. *"I logged … as passing"* is literally true of OPS-87 (title ends "both passed") and OPS-98. *"my read is"* is an explicit opinion marker. The forbidden hard form ("my QC side **is** finished") is absent. *"The crew **called** the HVAC run wrapped"* is likewise reported speech.
- **S2/S3 must carry:** the override must be graded as the agent's own determination, never as compliance with a prompt hint.
- **TRACES. PASS.**

### Lever 1 — Latching on the loudest wrap (cost 6.5)

- **Prompt sentence (S5):** *"The crew called the HVAC run wrapped around the same time."*
- **Atoms:** Slack C001 ts `1779308446.000005` (2026-05-20, Elias Navarro, *"all three clusters are done. Every unit serviced"*) and near-duplicate ts `1779308447.000006` (*"All three clusters done, 34 units total serviced"*).
- **Contradicted by, all verified present:** OPS-186 (2026-06-17) *"Two clusters are now substantially complete, with the West Cluster work still underway"*; Lisa Smith ts `1779884437.000093` (2026-05-27) *"Trying to nail down a window to get HVAC knocked out across my properties this week"*; Brooke ts `1781899601.000096` / `1781902061.000097` (2026-06-19) *"two clusters are pretty much wrapped up, one still in progress"*.
- **Set-definition trap verified:** Elias's scope issues OPS-16 / OPS-17 / OPS-18 name **three** clusters; OPS-35 ("Preventive Maintenance Push - West Cluster Properties"), OPS-91 ("West Cluster") and OPS-186 establish a **fourth**. Stump Hypothesis 4 is materialised.
- **TRACES. PASS.**

### Lever 8 — Multi-link chain off Jaime's own field note (cost 7.5)

- **Prompt sentence (S10):** *"Anything flagged in the field that still needs a tech back onsite belongs in our maintenance ticket log rather than sitting as a tracking item, and put a slot on my calendar to go back out and re-inspect whatever ends up in that follow-up."*
- **Hop A** — Slack C001 ts `1779562423.000092` (2026-05-23T18:53:43, Jaime Salinas): *"north Cluster walk-throughs done. Two units need HVAC looked at right away, flagged on the Linear issue with coil, plumbing, and panel notes."*
- **Hop B — RESOLVED THIS AUDIT (neither council identified it).** The carrying record is **`OPS-34`, comment `comment_4f3f967af50554ee8a7f1b0db1529bad`, `author_id = user_d3186a640f425ae0b69423f09aa4d7ec` (Jaime), `created_at 2026-05-21T09:00:00-05:00`**: *"Wrapped up the first pass on the North Cluster units this morning. Condenser coils are showing moderate fouling across the board… Plumbing fixtures have the usual wear… Electrical panels looked okay overall… two units need HVAC attention before anything else moves forward on them."* I swept all 48 Linear comments: this is the **unique** record containing coil + plumbing + panel together. Hop B is therefore determinate and solvable.
- **Hop C** — disposition. One day later OPS-87 (2026-05-24) says *"everything came back clean across the board"* and OPS-98's comment says *"No issues to flag on either side"*. I swept all 230 issues for a post-2026-05-23 North-cluster follow-up: **none exists** (only OPS-81, OPS-87 and OPS-98, none of which is a follow-up for those two units).
- **Critical S2/S3 binding (A-8):** OPS-34's **title is "Exterior signage update - brand-compliant vendor selected"** and its state is **Done** — the title gives zero signal and the issue carries 18 topically unrelated comments. Locating OPS-34 by title is effectively impossible; it is reachable only by enumerating comments. **No OE step or rubric may require the agent to name OPS-34.** The graded fact is the **disposition** (the flag was never actioned), which is fully derivable from hop A plus the absence of a follow-up.
- **TRACES. PASS**, with binding A-8.

### Lever 5 — Thread-reply blindness (cost 3.0)

- **Prompt sentences (S6 / S8 / S10):** *"where every piece of it stands … cluster by cluster"* · *"Anything still open gets its own tracking item raised"* · *"Anything flagged in the field that still needs a tech back onsite."*
- **Structure re-counted this audit:** C001 carries **104 messages, 56 of them thread replies under 37 distinct parents** (48 top-level; 37 messages with `reply_count > 0`). A channel read returns parents; the agent must elect to open each thread.
- **Atoms, both verified by `thread_parent_id`:** South no-access reschedule — ts `1779308444.000003` and `1779308445.000004`, both `thread_parent_id = 8ce45073c71f56ae89c859c0f3f6fc09` (= parent ts `1779308442.000001`). Filter-stock block — ts `1779569323.000012`, `thread_parent_id = 7b8f161126065f47bf66e3e0326ef2ea` (= parent ts `1779567943.000011`, John Smith: *"we'll need a restock before I can finish the run"*).
- **A-13:** the Hardness Plan states "15 distinct parents"; the true figure is **37**. The error is in the favourable direction (a larger parent set raises the miss rate), so Lever 5 is stronger than planned, not weaker.
- **TRACES. PASS.**

**5 of 5 selected levers trace end-to-end with cited evidence. Zero HARDNESS_REGRESSION.** The L31 retraction beat is not one of the 5 selected levers; it is assessed separately at LENS 5 / finding A-3.

---

## LENS 4 — Strict density projection

Sketched under the reading that **minimises inferred exploration** — i.e. only what the prompt's asks force, with no credit for a thorough agent's optional cross-checks.

### Bottom-up strict floor

| Component | Opus | Gemini | Basis (strict minimum) |
|---|---:|---:|---|
| Orient | 5 | 4 | channel list → C001; `slack_read_channel` (104 msgs, paginated); `list_teams` (hard prerequisite for `list_issue_statuses`); `list_projects` |
| Lever 2 — structured state | 7 | 5 | `list_issues` ×2-3 (proj filter + pagination); `list_issue_statuses` ×1; `get_issue` ×3 on OPS-87/96/98 |
| Prose walk | 4 | 3 | `list_comments` on her three records + ≥1 push issue |
| "cluster by cluster" over 4 clusters | 5 | 3 | `get_issue` on South/North/East/West anchors (OPS-43/56, OPS-40/44, OPS-99/108, OPS-35/91/186) |
| Levers 5 + 8 | 4 | 3 | `slack_read_thread` ×2-3 of 37 parents; `slack_search_public` ×1-2 |
| Write-supporting reads | 7 | 6 | `list_calendars`; `list_events`; `list_bases`; `list_tables_for_base`; `get_table_schema`; `search_records` (existing tickets); `contacts_search_contacts` |
| Writes (6 asks, 5 services) | 11 | 10 | `save_issue` ×3-4; `save_comment` ×3; `create_records_for_table` ×1; `create_event` ×1; `slack_send_message` ×1; `create_draft` ×1 |
| **Bottom-up strict floor** | **43** | **34** | |

### Empirically-calibrated strict midpoint (the banded figure)

Bottom-up minimal sketches systematically under-count real trajectories (pagination, retries, redundant list calls). The StarPM empirical anchors are Task 40 (avg 40.0) and Task 41 Gemini (47 / 45 / 37 / 38 / 33 / 40, avg 40.0 — counts confirmed unchanged at re-grade per Learnings item 8). **This task's write surface is strictly larger than either** (6 write asks across 5 services vs. their smaller sets), and the fixed write-plus-supporting-read cost of ~17-18 calls cannot be compressed by any reading.

| Model | Strict midpoint | Range | **Band** |
|---|---:|---|---|
| **Opus 4.8** | **47** | 38-58 | **PASS** (>= 40) |
| **Gemini** | **41** | 33-50 | **PASS** (>= 40) — **at the band edge** |
| **Combined** | **44** | 35-54 | **PASS** |

### Service breadth under the strict projection (Opus 47 profile)

| Service | Calls | Share |
|---|---:|---:|
| linear | 25 | **53%** |
| slack | 9 | 19% |
| airtable | 5 | 11% |
| gcalendar | 3 | 6% |
| gmail | 2 | 4% |
| contacts | 2 | 4% |
| quickbooks | 1 | 2% |
| hubspot | 0 | 0% |

**Breadth: PASS but tight** — 7 services exercised, **exactly 4 at >= 5%** against a threshold of 4; dominant service **53%**, under the 60% ceiling with 7 points of headroom.

**LENS 4: PASS on both models.** Recorded as **A-7**: this is a material downgrade from Council B's 50 combined / Opus 54 / Gemini 46 with "room", and a large downgrade from the Hardness Plan's 55.5 and its "linear at 34% / keep Linear under 35%" instruction. Under the strictest reading Gemini has roughly **one call of margin**, not room, and breadth sits **exactly at** the threshold rather than two services above it. Band is still PASS, so this is not a REVISE trigger — but S2 must not add Linear-only OE steps without a compensating cross-service step.

---

## LENS 5 — Adversarial veteran review

| Pattern (200+ task recognition) | Result |
|---|---|
| **Implicit-framing preservation (L15 / L16)** | **CLEAN.** The prompt frames the task as **execution** ("Before I put my name to this closing out"), and the persona **believes the wrong thing** ("my read is that my part of it is finished"). No sentence asks the agent to investigate whether she is wrong. S2/S3 must preserve this: no OE step or rubric may presuppose a "flag the discrepancy" instruction the prompt never gave — the discrepancy must be graded as the agent's own derivation. |
| **Entity-drift seams** | **CLEAN.** "Brooke" → exactly 1 of 61 contacts (`brooke.phillips@starpm.com`, Apartment Property Supervisor). "The crew" → Elias Navarro, Lead Maintenance Technician per `contacts.contacts`, and the wrap posts are his. "the channel the push has been running in" → C001 uniquely (16 push messages vs C007's 1 incidental). "my calendar" → `jaime.salinas@starpm.com` primary/owner. No seam. |
| **Tool-name leaks / MCP-server names** | **CLEAN.** Regex-verified zero. |
| **Em-dash / en-dash** | **CLEAN.** 0 × U+2014, 0 × U+2013, zero non-ASCII characters in the file. |
| **"at least N" without prompt mandate** | **CLEAN.** Zero occurrences. |
| **Internal IDs** | **CLEAN.** Zero `OPS-\d+`, `C\d{3}`, `rec[a-f0-9]{6,}`, `tbl\w+`, `proj_\d+`, `state_OPS`, `MT-2026-`. |
| **"approximately" / "roughly" near IDs, dates, amounts** | **CLEAN.** Zero occurrences. The only soft quantifier is "around the same time", which is attached to a *duration*, not to an ID/date/amount, and is grounded (4-5 days). |
| **"(or similar)" near exact values** | **CLEAN.** Zero occurrences. |
| **Single-channel lock-in where the prompt named only a goal** | **CLEAN and correctly built.** The Slack destination is named descriptively ("the channel the push has been running in"), honouring constraint 5. The lock-in trap is live and deliberate: the push runs in C001 `#maintenance` while Jaime's habitual channel per her brief is C004 `#make-ready` (she has 6 messages in C004 and 1 in C001). S2 must pin C001 in the OE; S3 must accept the equivalent descriptive path. |
| **Delegation ambiguity ("I'll [verb]")** | **CLEAN.** Zero hits for `I'll`, `I will`, `I am going to`, `I'm going to`. Every first-person construction is a state report ("I logged", "I have been") or a preference ("I need to know", "I do not want"). |
| **Command-list / numbered steps** | **CLEAN.** Prose, no ordinals, no "First… Then…". |

### The assigned question: does the final paragraph make the L31 differentiator a lexical gift?

**Sentence under audit:** *"If it is not, say straight out that my earlier sign-off does not hold and this should not be treated as closeable yet, with the reasons."*

**Finding: PARTLY YES, and Council B's primary defence is invalid.** Recorded as **A-3 (MODERATE)**.

Council B's MODERATE-4 offered two reasons the beat survives:

- **Reason (i) — "L31's Task 39 evidence shows Gemini failing 6/6 even where the required phrasing existed in the rubric, so the failure is behavioural not lexical." This argument does not hold.** The rubric is visible to the **judge**, never to the **agent**. Phrasing present in a rubric is not phrasing supplied to the model. Here the phrasing is in the **prompt**, which the agent reads. Task 39 is therefore not an apposite precedent, and it cannot be used to conclude that supplying the wording is harmless. Under LENS 7 I promote this rather than accept it.
- **Reason (ii) — "the clause is gated behind the Lever 2 determination, so a run that concludes 'pass' never reaches it." This argument does hold.** I verified the gate: the universe closes the conditional on the negative branch only for an agent that has already done the structured work, and Stump Hypothesis 1 predicts most runs will not.

**The correct characterisation is that reason (ii) rescues the prompt but destroys the lever's independence.** With the wording supplied, the retraction criterion no longer measures L31 (will Gemini spontaneously issue a negative directive?). It measures Lever 2 a second time (did Gemini get far enough to trigger the conditional?). That is precisely the **displaced-lever** pattern documented in Learnings item 9 (Task 41: L11 never observable because it sat one hop past L2's discovery gate) and reconfirmed from the other direction by item 20.

**Why no prompt edit is recommended.** Removing the wording would also remove the anti-hedging instruction (*"I do not want Brooke's email written so it can be read either way"* + *"say straight out"*) that makes the beat forcing at all; a vaguer directive would weaken both the beat and Clarity. The recoverable value is downstream, so the fix is binding rather than editorial:

1. **S3:** author the retraction criterion so it grades the **substantive prohibition** ("the agent states the earlier QC pass does not hold AND that the push should not be treated as closeable yet"), not lexical echo of the prompt's phrasing, and split it into two atomic criteria (retraction of the pass; prohibition on closing) so a Gemini run that echoes one half and hedges the other is graded correctly.
2. **S4 (pre-registration, per StarPM item 20 — write it now, not retrospectively):** if a Gemini run issues the retraction, score it as **prompt-supplied wording** and re-attribute that run's difficulty to Lever 2; do **not** log L31 as surviving. If Gemini fails the retraction criterion, verify from the trajectory whether it reached the negative determination at all before crediting L31.
3. **The dual-model mix must not be assumed to have three independent legs.** As written it has two measurable legs (symmetric Lever 2; Opus-selective Levers 9 + 1) plus a conditional third. Neither council stated this.

### Anti-patterns from `Reference/Prompt_Format.md` and the validator's cliché list

Checked and absent: "go through everything and surface every", "loop in", "CC our CEO", "before it blows up", over-signalled service lists, generic urgency framing.

**LENS 5: PASS with A-3 recorded.**

---

## Defect families F7 / F8 / F9 (AGENTS.md hard rule 13, `Evals_starpm/5`)

### F7 AMBIGUOUS_TARGET — does any write ask pin a target more than one universe record satisfies?

| Write ask | Target | Uniqueness |
|---|---|---|
| *"Anything still open gets its own tracking item raised, with the person who owns that work named on it"* | new Linear issue | **Unique by construction** (create) |
| *"My own spot-check records … a short note left on each one"* | Jaime-assigned spot-check issues | **Set write over an explicitly exhaustive set** ("each one"), not a single-target pin. `assignee_id = user_d3186a640f425ae0b69423f09aa4d7ec` → exactly **OPS-87, OPS-96, OPS-98** (all three carry "spot-check" in the title). Jaime's only other created issues are OPS-224/225/226 (Las Vistas 3C make-ready punch items — not spot-checks, not the push). **F7 does not fire**, but see A-4. |
| *"belongs in our maintenance ticket log"* | new Airtable row in `tblMaintenanceTickets` | **Unique by construction** (create). Verified: of the 50 existing tickets, **zero** reference the push, the clusters, condensate drains, the no-access unit, the filter run or Carlos's flagged water heaters. The 4 water-heater tickets that exist are decoys on unrelated properties (Tommy Reyes's unit, Pinecrest 12). See A-6. |
| *"put a slot on my calendar"* | new event on `jaime.salinas@starpm.com` | **Unique by construction** (create) |
| *"post … in the channel the push has been running in"* | C001 `#maintenance` | **Unique** — 16 push messages vs C007's 1 incidental budget aside |
| *"draft an email to Brooke"* | `brooke.phillips@starpm.com` | **Unique** — 1 of 61 contacts |

**F7: CLEAN.** Every write is unique by construction or scoped to an exhaustive set.

### F8 NON_ATOMIC_ENUM — does the prompt force a non-atomic enumeration downstream?

**No.** *"Anything still open gets its **own** tracking item raised"* mandates one item per open thing — the atomic shape S3 needs. No completeness predicate is imposed at prompt level ("all six", "every one of the"). *"a short note left on **each one**"* likewise decomposes.

**Binding on S3 (constraint 2):** three atomic per-issue criteria (OPS-87, OPS-96, OPS-98), each graded on note content; never one bundled "comments on her spot-check issues" criterion. Per Learnings item 5, split any criterion whose two facts come from different records — this task's open items are sourced across Linear state, Linear comments, Slack parents, Slack replies and Calendar agendas, so the risk is live.

### F9 UNRECONCILED_FUTURE_EVT — swept independently this audit

I re-read all **565** rows of `gcalendar.gcalendar_events.json` and filtered on `start_dt >= 2026-07-01`:

**27 rows / 9 unique confirmed events.** In full: JP Court Eviction Filing Appointment (07-01), Las Vistas 9D Unit-Turn Make-Ready Kickoff (07-02), Lease Renewal - Tommy Reyes (07-06), Vendor Walk-Through A Plus Carpet Las Palmas 8D (07-07), Mesa Vista HOA Management Review (07-08), Move-In Walkthrough Sunridge (07-09), Vendor Walk-Through Ridgeview Roof Follow-Up (07-13), **Make-Ready QC Inspection - Mesa Vista 4C (07-15)**, **Q3 Make-Ready Planning & Budget Review (07-23)**.

- **Zero** mention the Preventive Maintenance Push, HVAC, the clusters, or Jaime (case-insensitive JSON sweep on `jaime` / `preventive` / `hvac`: **0 hits**).
- **Jaime is not an attendee on any of the nine.** The 07-15 Mesa Vista 4C QC inspection is on Carlos Mendez's calendar with attendees Carlos / Brooke / Wesley Tran.
- The prompt makes **no** claim that Jaime's QC queue is otherwise clear and **no** claim that the maintenance-budget question is settled, so constraint 3's two watch items are not contradicted.
- The prompt's only forward-looking clause creates a **new** event and asserts nothing about existing ones.

**F9: CLEAN. Nothing in the prompt is contradicted by any confirmed event dated on or after 2026-07-01.**

---

## Hardness_Plan pre-registered S1 constraints — all 10 re-verified independently

| # | Constraint | Ruling | Evidence I retrieved |
|---|---|---|---|
| 1 | F7 — prefer writes unique by construction | **HONOURED** | Table above; 5 of 6 writes are creates, the sixth is an exhaustive set write |
| 2 | F8 — decompose per item | **HONOURED** at prompt level | "its **own** tracking item"; "**each one**" |
| 3 | F9 — no claim that Jaime's queue is clear / budget settled | **HONOURED** | 27 future rows read; 9 unique; zero touch the push or Jaime; prompt makes neither claim |
| 4 | Gmail is a deliverable, never a source | **HONOURED** | Gmail appears once, as *"draft an email to Brooke"*. 484 Gmail rows swept: zero push-related. Gmail exposes `create_draft` and **no send tool**, so "draft" is the only feasible verb |
| 5 | Channel-lock-in — descriptive naming | **HONOURED** | *"the channel the push has been running in"* — no name, no id. Trap live: push in C001, Jaime's habit is C004 (6 of her 7 Slack messages) |
| 6 | Do not build on OPS-91 | **HONOURED** | The prompt makes **zero** West-cluster assertions. OPS-91's inverted pair (state `state_OPS_4` Done, `completed_at 2026-05-28`, description *"Moving this issue to In Progress"*) is untouched by any prompt claim |
| 7 | Do not build on an absence | **HONOURED** | Every ask is a positive determination and every write a positive artifact. The absences (no restock bill, no follow-up issue for the two North units, no reply on OPS-56's access ask) are reached **through** positive evidence (John's *"before I can finish the run"*; Jaime's own field note) and function as corroboration |
| **7a** | **HIGHEST RISK — never claim "nothing on the push is closed"** | **HONOURED** | Exact prompt text: *"That came and went yesterday and **it is still sitting open**."* Referent = the **initiative**. Verified true: `proj_003.state="backlog"`, ~21 push-adjacent issues in non-Done states. Verified **not** overclaimed: OPS-40 `completed_at 2026-05-18`, OPS-91 `completed_at 2026-05-28` are genuinely Done, and the prompt asserts nothing about either and enumerates zero issue states. **This is the constraint I checked hardest. It is clean.** |
| **8** | **HIGHEST RISK — soft verbs on the authority anchor** | **HONOURED** | *"I **logged** both cluster spot-checks **as passing**"* (true of the prose in OPS-87/OPS-98) + *"**my read is** that my part of it is finished"* (explicit opinion marker) + *"The crew **called** the HVAC run wrapped"* (reported speech). The hard form ("my QC side **is** finished") is absent. This is exactly why Truthfulness holds at 5 |
| **9** | **HIGHEST RISK — no escape-valve clause on the load-bearing surface** | **HONOURED** | Closest sentence: *"Work out what is actually finished and what is not, and get our tracking to match."* Against the L29 exemplar's three defining properties — conditional on discovery, unbound to a deliverable, signals the persona's uncertainty — this sentence has **none**: it is unconditional, bound to a named write, and signals no uncertainty. It names no system, no field, no status, and no contradiction. Crucially it points at **field-completion state**, which is exactly where the **false** prose lives (Slack posts, issue descriptions, issue comments); an agent following it literally walks into the trap. Positively confirmed absent from the whole prompt: "check whether", "look for", "see if anything contradicts", "flag any discrepancies", "verify the states", and any reference to Linear, issues, statuses or workflow states |
| 10 | Similarity pivot under 40% | **HONOURED** | `_aux/Similarity_Report.json`: max composite **27.2**, corpus 44, band `below_40` → INVALIDATE. 13 points of margin |

**10 of 10 HONOURED. Zero VIOLATED.**

---

## LENS 7 — Anti-Rationalization scan (explicit)

I re-scanned my own reasoning for every "I considered flagging X but decided it's fine because…" line. **Six were found. All six are promoted to logged findings below. None was silently cleared.** For each I state whether the clearing reasoning cites a hard exclusion.

| # | The thing I considered flagging | The rationalization I caught myself making | Disposition |
|---|---|---|---|
| R1 | "get our tracking to match" could mean flip the state on OPS-87/96/98, or leave them and only add notes — a different `save_issue` call | *"…but the deliverable set is identical either way"* | **PROMOTED → A-5 (MINOR).** Hard exclusion cited: the T11 precision guardrail (identical deliverables + a structured field variation where every reading leaves the record in a non-Done state, so the open/closed end-state is invariant) plus the prompt's own instantiation for her records being explicitly *"a short note left on each one"*. Sub-dim stays 5; binding fix recorded. |
| R2 | "my own spot-check records" could be read as the two cluster records named in S4, dropping OPS-96 | *"…but the plain sense of an unrestricted possessive plural is the full set"* | **PROMOTED → A-4 (MINOR).** Hard exclusion cited: S9's noun phrase carries **no** restrictor and no definite back-reference to S4; S4 is narrative, five sentences and one paragraph away, and does not even cleanly exclude OPS-96 (whose comment also logs a pass). The 2-record reading requires importing a restrictor that is not grammatically present. Sub-dim stays 5; binding fix recorded. |
| R3 | The Linear-vs-Airtable routing boundary is judgement-laden for the filter run, the water heaters and the South no-access unit | *"…but the prompt supplies the test, so applying it is investigation not ambiguity"* | **PROMOTED → A-2 (MODERATE).** Hard exclusion cited: the prompt states the discriminator explicitly (*"still needs a tech back onsite"*) and each channel has at least one **unambiguous** member under every reading (two North HVAC units → Airtable; West QC coverage gap → Linear), so no reading empties either channel. Sub-dim stays 5, but the S3 false-fail hazard is real and the fix is mandatory. |
| R4 | Council B's Lever-8 hop B was asserted without ever naming the record | *"…but the councils clearly did the work"* | **REJECTED as rationalization. PROMOTED → A-8 (NOTE) and resolved by me.** Neither council named the target. I identified it (OPS-34, `comment_4f3f967af50554ee8a7f1b0db1529bad`, Jaime, 2026-05-21T09:00, unique coil+plumbing+panel match) and found the consequence they missed: OPS-34's title is about exterior signage and its state is Done, so it must never be a graded identification. |
| R5 | Council B's L31 defence reason (i) | *"…a prior council adjudicated this, and a QC-passed task does the same"* | **REJECTED as rationalization — this is the exact "a QC-passed task does the same" shape AUDIT.md names. PROMOTED → A-3 (MODERATE).** Reason (i) confuses rubric visibility with prompt visibility and is invalid on its own terms. |
| R6 | `verify_universe_atoms` "0 atoms checked" | *"…the prompt legitimately has no structured atoms, so 0 is correct"* | **PROMOTED → A-10 (NOTE).** Hard exclusion cited: the extractors target account claims, no-response claims, money, ISO dates, emails and IDs; `Reference/Prompt_Format.md` **forbids** internal IDs in prompts, so 0 is the structurally correct output and not a regression. But the consequence is not excused: the programmatic Truthfulness floor contributed **zero** evidence, so the 5/5 rests entirely on the 17-row manual table in LENS 1 — which is exactly the v18 contract, discharged. |

**Anti-rationalization scan result: 6 candidates found, 6 promoted to findings, 0 silently cleared. Two of the six (R4, R5) were rationalizations built on deference to the prior councils and are rejected outright.** No promoted finding forces a sub-dim below 5, so the scan does not convert the verdict to REVISE.

---

## Findings

Format: `[SEVERITY] issue -- file:location -- exact fix`.

### MODERATE (bind on S2 / S3; no prompt edit)

**[MODERATE] A-1 — "the person who owns that work" is multi-valued for every open item; a rubric pinning one name will false-fail correct agents.**
`5_Prompt.txt:5` (*"Anything still open gets its own tracking item raised, with the person who owns that work named on it."*)
I resolved ownership for each open item from source and **every one admits two or more defensible owners**: unfinished filter run → **John Smith** (*"before I can finish the run"*, C001 `1779567943.000011`) or **Elias Navarro** (Brooke's reply `1779569323.000012` assigns him the stock count); South no-access unit → **Carlos Mendez** (Elias's thread replies `1779308444/45`, OPS-56 comment) or **Elias Navarro** (OPS-43 assignee); two North HVAC units → **Elias**, **Tony Reyes**, **Brooke** (OPS-44 assignee) or **Jaime** herself; West coverage gap → **Lisa Smith** (OPS-35 desc *"Lisa is the onsite lead"*, OPS-91 assignee) or **Brooke Phillips** (OPS-35 assignee); water heaters → **Carlos Mendez** (flagged them) or **Brooke Phillips** (*"I'll flag those for Brooke to get vendor quotes"*, plus her 6/03 budget-priority post).
**Neither council examined owner determinacy.** This is the Task 41 R6 / Learnings item 12 false-fail shape and the `Evals_starpm/5` F4 family.
**FIX (S3, mandatory):** owner criteria must either (a) grade that the follow-up item **names an owner** without pinning who, or (b) carry an explicit accept-set of every defensible owner per item, e.g. *"The Agent names John Smith or Elias Navarro as the owner on the follow-up item for the unfinished filter run."* Never a single-name pin. **(S2):** the OE must record the accept-set per item so the judge sees it.

**[MODERATE] A-2 — the Linear-vs-Airtable routing partition has boundary items two competent agents will route differently.**
`5_Prompt.txt:5,7` (*"Anything still open gets its own tracking item raised"* vs *"Anything flagged in the field that still needs a tech back onsite belongs in our maintenance ticket log rather than sitting as a tracking item"*)
Unambiguous members exist on both sides — the two North units needing HVAC "right away" are clearly tech-onsite (Airtable); Jaime's own West-cluster QC coverage gap clearly is not (Linear). But three items sit on the boundary: the **unfinished filter run** (a tech must return, but the blocker is a 20x25 restock/procurement), the **flagged water heaters** (onsite replacement, but the blocker is vendor quotes and budget), and the **South no-access unit** (a tech must return, but the action is access coordination with Carlos). Elias's wrap also flags **two condensate-drain units** for follow-up (`1779308446.000005`, `1779308447.000006`), a fourth boundary candidate.
**Neither council examined the partition item by item.** Clarity holds at 5 because the prompt states the discriminator and neither channel is empty under any reading — but the S3 hazard is severe.
**FIX (S2):** the OE must pin **one unambiguous item on each side** (two North units → Airtable ticket; West coverage gap → Linear item) and must state that boundary items may be routed either way. **(S3):** no criterion may require a boundary item in a specific channel; grade the Airtable ticket on content ("field items needing a tech back onsite") accepting any defensible member, and do not penalise an agent that files a boundary item in both.

**[MODERATE] A-3 — the L31 retraction beat's wording is supplied by the prompt, and Council B's primary defence of it is invalid.**
`5_Prompt.txt:11` (*"say straight out that my earlier sign-off does not hold and this should not be treated as closeable yet"*)
Full analysis at LENS 5. Council B's reason (i) — "Task 39 shows Gemini failing 6/6 even with the phrasing present in the rubric" — confuses **rubric** visibility (judge-only) with **prompt** visibility (agent-facing) and does not support the conclusion. Reason (ii) (the clause is gated behind Lever 2) is valid but converts the beat from an independent Gemini-selective differentiator into a **displaced lever** behind Lever 2's discovery gate — the Learnings item 9 / item 20 pattern. The dual-model mix therefore has two measurable legs, not three.
**FIX (S3):** author the retraction as **two atomic criteria** graded on substance, not lexical echo — (a) the agent states her earlier QC pass does not hold, (b) the agent states the push should not be treated as closeable yet. **(S4, pre-register now per StarPM item 20):** if a Gemini run issues the retraction, score it as prompt-supplied wording, re-attribute to Lever 2, and do not log L31 as surviving; if it fails, verify from the trajectory whether it reached the negative determination at all. No prompt edit — removing the wording would strip the anti-hedging instruction that makes the beat forcing.

### MINOR (bind on S2 / S3; no prompt edit)

**[MINOR] A-4 — "my own spot-check records" admits a subset reading (2 of 3) that drops OPS-96, the load-bearing filter record.**
`5_Prompt.txt:5`
S4 says *"I logged both **cluster** spot-checks as passing"*; S9 says *"My own spot-check records … a short note left on **each one**"*. An agent could import S4's "cluster" restrictor and comment only on OPS-87 and OPS-98, dropping **OPS-96** — the record whose *"spot-check across **all units** … filters look good across the board"* is falsified by John Smith's unfinished filter run, i.e. the sharpest contradiction in the set. **Both councils examined only the superset direction (3 → 5, adding Elias-assigned OPS-99/OPS-108); neither examined the subset direction, which is the dangerous one because it drops a deliverable rather than adding one.**
**FIX (S3):** three atomic per-issue criteria (OPS-87, OPS-96, OPS-98), each graded on note content, so a 2-of-3 agent fails exactly one; plus an explicit accept-band that extra comments on OPS-99 / OPS-108 / OPS-51 are **not** penalised. **(S2):** the OE must pin all three by `assignee_id`. **A prompt-side enumeration fix is explicitly NOT recommended** — naming the filter check in S4 would point the agent at OPS-96 and risk a constraint-9 escape valve on a load-bearing surface.

**[MINOR] A-5 — "get our tracking to match" leaves the state-flip question open on Jaime's own three records.**
`5_Prompt.txt:5`
Reading A: leave OPS-87/96/98 in Todo/Todo/In Progress (already the correct open state) and add notes. Reading B: additionally flip a state within the open range (e.g. OPS-96 Todo → In Progress). No reading moves them to Done, so the open/closed end-state is invariant and the deliverable set is identical; but Reading B is an extra `save_issue` call.
**FIX (S2):** the OE scopes state correction to Jaime's three and states that no state flip is required (the state is already correct; the **prose** is what is wrong). **(S3):** no criterion may require a state flip on OPS-87/96/98, and none may penalise one. Also, per Council A's M2, do not require or penalise state edits on third-party issues (OPS-43 Elias, OPS-97 Carlos, OPS-35 Brooke, OPS-91 Lisa).

**[MINOR] A-6 — Airtable water-heater decoys could induce an update-instead-of-create.**
`5_Prompt.txt:7`
`tblMaintenanceTickets` carries 4 water-heater tickets, all on unrelated properties (Tommy Reyes's unit ×2, Pinecrest 12 ×2 including MT-2026-1317). An agent routing Carlos's flagged water heaters could treat an existing decoy as coverage. The push's actual field items (two North units, South no-access, condensate drains, filter run) have **no** existing ticket, so the create is unique by construction.
**FIX (S3):** grade the Airtable write on **content** (a new ticket describing push field items needing a tech onsite), never on a record id; do not fail an agent that also updates an existing ticket. **(S2):** the OE must pin `appPropertyOps` / `tblMaintenanceTickets` and must **not** write an owner or status field — the table has only Ticket Number, Description, Priority (Low/Medium/High) and Completion Date.

### NOTE (record only)

**[NOTE] A-7 — strict density is materially below both prior projections; Gemini sits at the band edge and breadth sits exactly at threshold.**
`_aux/Hardness_Plan.md:Tool-Call Density Projection` + `_aux/Council_Reports/S1_B_adversarial.md:[B3]`
Strict per-model: **Opus 47, Gemini 41, combined 44** (Plan 55.5; Council B 54 / 46 / 50). Bottom-up strict floor is Opus 43 / Gemini 34. Breadth: 7 services exercised, **exactly 4 at >= 5%** (threshold 4), dominant `linear` at **53%** (Plan claims 34% and instructs "under 35%"; Council B found 47%; ceiling 60%). **Band is PASS on both models — no REVISE.**
**FIX:** none required. **(S2):** do not add Linear-only OE steps without a compensating cross-service step; ensure the OE explicitly exercises `gcalendar list_events` and an Airtable existing-ticket sweep so those services stay above 5%. **(S4):** expect Gemini runs in the 33-45 band and do not treat a single sub-40 run as a surprise.

**[NOTE] A-8 — Lever 8 hop B target identified for the first time: OPS-34, an unrelated-titled Done issue. Must never be a graded identification.**
`linear.linear_comments:comment_4f3f967af50554ee8a7f1b0db1529bad`
The record carrying Jaime's *"coil, plumbing, and panel notes"* is **OPS-34**, whose title is *"Exterior signage update - brand-compliant vendor selected"*, whose state is **Done**, and which carries 18 topically unrelated comments. It is the **unique** coil+plumbing+panel match across all 48 comments and is authored by Jaime herself. Neither council named it.
**FIX (S2/S3):** no OE step or rubric may require the agent to name OPS-34. The graded fact is the **disposition** — that the two flagged North units were never actioned — derivable from Jaime's C001 note `1779562423.000092` plus the verified absence of any follow-up issue in the 230-issue corpus.

**[NOTE] A-9 — dangling cross-reference inside the Lever 8 chain.**
`linear.linear_comments` OPS-34, 2026-05-21T09:00
The comment says *"I also dropped a summary in **#make-ready**"*, but I swept all 144 C004 `#make-ready` messages and **zero** mention "north". Jaime's actual field note is in C001 `#maintenance` (2026-05-23). Base-universe noise, not a CB edit (`4_Changelog.json` = `[]`), and well-supported data beats the low-support reference per the QC spec's coherence note.
**FIX (S3):** no rubric may require the agent to find a `#make-ready` summary of the North cluster — it does not exist.

**[NOTE] A-10 — `verify_universe_atoms.py` returned a structurally correct but evidentially vacuous pass.**
`_aux/Council_Reports/verify_universe_atoms.md`
0 atoms checked, empty per-atom evidence table. The extractors target account claims, no-response claims, money, ISO dates, emails, JE/EXC/RECON/vendor/invoice IDs, `OPS-\d+`, `C\d{3}`, `rec…`, and the prompt carries none of these **by design** (`Reference/Prompt_Format.md` forbids internal IDs). So 0 is correct, not a regression. **But the consequence is real:** the programmatic Truthfulness floor contributed zero evidence to this deliverable, so Truthfulness 5/5 rests entirely on the 17-row manual evidence table in LENS 1. Under the v18 rule (empty evidence → forced score <= 3), that table is what discharges the requirement. **No action; recorded so a future gate does not read the clean atom-verifier exit as independent Truthfulness corroboration.**

**[NOTE] A-11 — `Fact_Ledger.lifecycle.today` is null (pre-declared known defect); must be fixed BEFORE S2.**
`_aux/Fact_Ledger.json:lifecycle.today` + `Validators/validate.py:464`
`lifecycle.today = null` → `validate.py` falls back to the hardcoded Brookfield `"2026-06-12"` and prints it in NOTES 4 and 5 as *"the single date-alignment source for prompt + OE + rubrics"*. **Wrong for this universe.** `Validators/universes.py` already carries `starpm.today = "2026-07-01"`, so the fallback is bypassing an authority that exists. The prompt's dates are correct against 2026-07-01 and were verified independently.
**FIX:** (1) backfill `_aux/Fact_Ledger.json` `lifecycle.today = "2026-07-01"`; (2) change `validate.py:464` to `get_universe_constants(detect_universe(task_dir))["today"]`; (3) **binding until (1) lands:** S2 and S3 must date-anchor to `_aux/Universe_Index/today_horizon.json`, never to Fact_Ledger. Because `6_Oracle_Events.txt` is still an empty template, fix (1) should land **before S2 starts**, not after.

**[NOTE] A-12 — Council A mis-cited project membership on its load-bearing "still sitting open" row.**
`_aux/Council_Reports/S1_A_grounding.md:113`
A3 row 3 lists OPS-35, OPS-56, OPS-97, OPS-98, OPS-99, OPS-108 and OPS-186 among "60 `proj_003` issues". They are not: OPS-35/56/99/108 are `proj_002`, and OPS-97/98/186 are `proj_001`. Of that cited list only OPS-17, OPS-43, OPS-44, OPS-87 and OPS-96 are actually in `proj_003` — which itself contains 60 issues, most of them unrelated mass-email-campaign items. **The conclusion survives** (I re-derived "still sitting open" from `proj_003.state="backlog"` plus a direct per-issue state sweep), but the citation did not. No deliverable impact; recorded so the mis-citation is not propagated into an OE or rubric.

**[NOTE] A-13 — Hardness_Plan understates the C001 thread-parent count.**
`_aux/Hardness_Plan.md:42` says *"C001 carries 104 messages with 15 distinct parents"*. Re-counted: **104 messages, 56 thread replies under 37 distinct parents, 48 top-level, 37 messages with `reply_count > 0`.** Council B had this right. The error is in the favourable direction — a 37-parent set raises the Lever 5 miss rate above the L12 baseline. No action.

**[NOTE] A-14 — Hardness_Plan arithmetic nit.**
`_aux/Hardness_Plan.md:25` says Lisa's 5/27 ask came *"five days after Elias declared all clusters done"*. Elias's wrap is 2026-05-20; the gap is **7 days**. Plan-side only, no deliverable impact.

**[NOTE] A-15 — Hardness_Plan service-breadth table is materially optimistic.**
`_aux/Hardness_Plan.md:98-108` projects `linear` at 34% with 6 services at >= 5% and instructs the prompt writer to keep "Linear under 35%". Strict re-derivation: **53%, 4 services at >= 5%.** The instruction was unachievable given that the core question resolves in a Linear column and 3 of the 6 write asks are Linear writes. Gate still passes. No action beyond A-7's S2 binding.

---

## Verification statements

- [x] Validator (`validate.py --phase prompt`) result consumed: PASS, 0 fails, 1 WARN, 6 NOTES. **Every WARN and NOTE listed and adjudicated individually above** (not re-run — result pre-supplied).
- [x] **Regression-anchor suite executed this pass: 62 passed, 0 failed out of 62.** Recorded verbatim; not re-run.
- [x] Atom-verifier result consumed (PASS, 0 atoms) and its vacuity assessed at A-10; the required per-atom evidence table was produced manually in LENS 1 with 17 rows, every row retrieved this audit.
- [x] Similarity consumed: max composite 27.2, corpus 44, band `below_40`. Under the 40 ceiling and under the 35 AUDIT band.
- [x] **Anti-rationalization output check performed and reported in full (LENS 7): 6 candidates found, 6 promoted, 0 silently cleared, 2 rejected as deference-to-prior-council.**
- [x] Verdict recorded with an explicit per-issue trail (15 findings).
- [x] Universe re-derived from source, not from prior phase outputs: `linear.linear_issues` (230), `linear.linear_comments` (48), `linear.linear_workflow_states` (5), `linear.linear_projects` (3), `linear.linear_users`, `slack.slack_messages` (C001: 104), `slack.slack_channels` (8), `slack.slack_users`, `gcalendar.gcalendar_events` (565), `gcalendar.gcalendar_calendars`, `airtable.airtable_tables`, `airtable.airtable_fields`, `airtable.airtable_records` (50 in `tblMaintenanceTickets`), `contacts.contacts` (61), `gmail.gmail_messages` (484), `Universe_complete_data.json` (4.4 MB, 103 leakage patterns).
- [x] Tool catalog verified universe-correctly: `StarPM_Base_Universe/7_Server_Tools_Details.json` (linear 42 tools, slack 19, airtable 22, gcalendar 9, gmail 13, contacts 8, quickbooks 141, hubspot 14).
- [x] Eval + QC specs verified universe-correctly: `Evals_starpm/1_Prompt_Eval.md`, `Evals_starpm/5_Submission_Gate_Eval.md`, `Docs_starpm/7_QC_Spec_Doc1.json`, `Docs_starpm/8_QC_Spec_Doc2.md`. `Docs_starpm/13_QC_Companion.md` correctly **not** consulted (Brookfield-contaminated per `Validators/regression_baseline/ROUTING_DECISIONS.md`).

## All lenses status

| Lens | Verdict |
|---|---|
| LENS 1 — strict QC scoring (14 sub-dims + 17-row atom table) | **PASS** — 14/14 at 5, zero below 5 |
| LENS 2 — answer-leakage sweep (103 patterns) | **PASS** — zero hits, zero BLOCKER |
| LENS 3 — hardness end-to-end trace | **PASS** — 5/5 levers trace with cited evidence; OE/rubric columns N/A at S1 |
| LENS 4 — strict density projection | **PASS** — Opus 47, Gemini 41, combined 44 (StarPM V4 bands, per model) |
| LENS 5 — adversarial veteran review | **PASS** with A-3 recorded |
| LENS 6 — lifecycle + narrative state | **RETIRED in v18** — merged into LENS 1, not executed |
| LENS 7 — anti-rationalization | **PASS** — 6 candidates found, 6 promoted, 0 silently cleared |
| LENS 8 — regression-anchor verification | **62/62 PASS** |
| LENS 9 — unique ground truth middle band | **RETIRED in v18** — merged into LENS 1 UGT + LENS 5, not executed |
| F7 / F8 / F9 (AGENTS.md rule 13, Evals_starpm/5) | **CLEAN / CLEAN / CLEAN** |
| Hardness_Plan constraints 1-10 (incl. 7a, 8, 9) | **10/10 HONOURED** |

## Discrepancies surfaced

1. **`_aux/Fact_Ledger.json` `lifecycle.today = null`** → `validate.py:464` hardcoded Brookfield fallback `2026-06-12`, wrong for this universe. Authoritative date is **2026-07-01** per `_aux/Universe_Index/today_horizon.json`. Pre-declared; recorded as A-11 with a three-part fix that must land before S2.
2. **`Validators/validate.py:464`** bypasses `Validators/universes.py`, which already carries the correct `starpm.today`.
3. **Council A** mis-cited `proj_003` membership on its "still sitting open" row (A-12) — conclusion correct, citation wrong.
4. **Council B's** L31 defence reason (i) is invalid (rubric vs prompt visibility) — A-3.
5. **Hardness_Plan** carries three factual errors: C001 thread parents 15 vs actual 37 (A-13); "five days" vs actual 7 (A-14); service breadth linear 34% / 6 services vs strict 53% / 4 services (A-15).
6. **`StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md`** Universe-constants row names "Linear (maintenance tickets)" as a system of record, contradicting `linear_teams.team_001.description` and `airtable_tables.tblMaintenanceTickets.description`, which both name Airtable. Live universe data wins; agents only read live data. (Council A M3 — confirmed independently.)
7. **`StarPM_Base_Universe/7_Server_Tools_Details.json`** `save_issue.assignee` is typed `"null"` — the only parameter in the catalog with that type. Harmless here because the prompt says "named on it", not "assigned to it". (Council B MODERATE-1 — confirmed independently.)
8. **Base-universe noise, none CB-authored** (`4_Changelog.json` = `[]`): OPS-34's title/comment topical mismatch and its dangling `#make-ready` reference (A-9); duplicate GCalendar rows (3-6× per logical event); identical-title pairs OPS-99/OPS-108 and OPS-51/OPS-71 in opposing states; OPS-91's inverted state/prose pair.

---

## Verdict

**PASS (STRICT).**

Zero BLOCKER. Zero LENS-1 sub-dims below 5 (14 of 14 at 5, with a 17-row per-atom evidence table personally retrieved this pass). All 5 selected levers trace end-to-end with cited evidence, including Lever 8's hop B which I resolved to a concrete record neither council named. Density clears the StarPM V4 PASS band on both models under the strictest reading (Opus 47, Gemini 41, combined 44). Answer-leakage sweep clean across 103 patterns. F7 / F8 / F9 clean. All 10 pre-registered constraints honoured, including all three highest-risk ones (7a, 8, 9).

Fifteen findings are recorded. **None requires an edit to `5_Prompt.txt`.** Three MODERATE and three MINOR are binding downstream instructions for S2 and S3 — A-1 (owner accept-sets), A-2 (routing-partition accept-band), A-3 (retraction graded on substance + S4 pre-registration), A-4 (three atomic per-issue note criteria), A-5 (no required or penalised state flip), A-6 (Airtable graded on content) — plus the mandatory pre-S2 date fix at A-11.

```json
{
  "phase": "audit_prompt",
  "council": "AUDIT",
  "task_dir": "Tasks/44_6a62ccba8cad60844b8364b9",
  "verdict": "PASS_STRICT",
  "perspectives": {
    "Lens1": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MODERATE",
          "location": "5_Prompt.txt:5",
          "issue": "'the person who owns that work' is multi-valued for every open item (filter run John/Elias; South no-access Carlos/Elias; two North units Elias/Tony/Brooke/Jaime; West Lisa/Brooke; water heaters Carlos/Brooke) - neither council examined owner determinacy",
          "fix": "S3 owner criteria must grade 'names an owner' or carry an explicit per-item accept-set; never a single-name pin. S2 records the accept-set in the OE.",
          "propagate_to": "S3"
        },
        {
          "severity": "MINOR",
          "location": "5_Prompt.txt:5",
          "issue": "'my own spot-check records' admits a subset reading (2 of 3) that drops OPS-96, the load-bearing filter record; both councils examined only the superset direction (3->5)",
          "fix": "S3 writes three atomic per-issue criteria on OPS-87/OPS-96/OPS-98 graded on note content, plus an accept-band for extra comments on OPS-99/OPS-108/OPS-51. S2 pins all three by assignee_id. Do NOT enumerate them in the prompt - naming the filter check would point at OPS-96 and risk a constraint-9 escape valve.",
          "propagate_to": "S3"
        },
        {
          "severity": "MINOR",
          "location": "5_Prompt.txt:5",
          "issue": "'get our tracking to match' leaves the state-flip question open on OPS-87/96/98; no reading moves them to Done so the open/closed end-state is invariant, but Reading B adds a save_issue call",
          "fix": "S2 states the state is already correct and the prose is what is wrong; S3 must neither require nor penalise a state flip on her three, nor on third-party issues OPS-43/OPS-97/OPS-35/OPS-91.",
          "propagate_to": "S3"
        },
        {
          "severity": "NOTE",
          "location": "_aux/Council_Reports/verify_universe_atoms.md",
          "issue": "atom verifier returned 0 atoms checked with an empty evidence table - structurally correct (prompt carries no IDs/amounts/ISO dates by design) but evidentially vacuous",
          "fix": "No action. Truthfulness 5/5 rests entirely on the 17-row manual evidence table in LENS 1, which discharges the v18 contract. Recorded so no future gate reads the clean atom-verifier exit as independent Truthfulness corroboration.",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "_aux/Council_Reports/S1_A_grounding.md:113",
          "issue": "Council A's A3 row 3 lists OPS-35/56/97/98/99/108/186 as proj_003 issues; they are proj_002 or proj_001. Conclusion ('still sitting open') survives on re-derivation from proj_003.state='backlog' plus a per-issue state sweep; the citation does not",
          "fix": "No deliverable impact. Recorded so the mis-citation is not propagated into an OE or rubric.",
          "propagate_to": null
        }
      ]
    },
    "Lens2": { "status": "PASS", "findings": [] },
    "Lens3": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "linear.linear_comments:comment_4f3f967af50554ee8a7f1b0db1529bad",
          "issue": "Lever 8 hop B resolves to OPS-34 (title 'Exterior signage update - brand-compliant vendor selected', state Done, 18 unrelated comments) - the unique coil+plumbing+panel match across all 48 comments, authored by Jaime 2026-05-21T09:00. Neither council named the record",
          "fix": "No OE step or rubric may require the agent to name OPS-34. Grade the disposition (the two flagged North units were never actioned), derivable from Slack 1779562423.000092 plus the verified absence of any follow-up issue in the 230-issue corpus.",
          "propagate_to": "S3"
        },
        {
          "severity": "NOTE",
          "location": "linear.linear_comments:OPS-34 2026-05-21T09:00",
          "issue": "comment says 'I also dropped a summary in #make-ready' but zero of the 144 C004 messages mention 'north'; Jaime's actual field note is in C001. Base-universe dangling reference, not a CB edit",
          "fix": "No rubric may require the agent to find a #make-ready summary of the North cluster - it does not exist.",
          "propagate_to": "S3"
        },
        {
          "severity": "NOTE",
          "location": "_aux/Hardness_Plan.md:42",
          "issue": "Plan states C001 has 15 distinct thread parents; re-counted actual is 37 parents / 56 replies / 48 top-level. Error is in the favourable direction (raises Lever 5 miss rate)",
          "fix": "None. Correct the figure at S4 calibration.",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "_aux/Hardness_Plan.md:25",
          "issue": "Plan says Lisa's 5/27 ask came 'five days after Elias declared all clusters done'; Elias posted 2026-05-20, so the gap is 7 days",
          "fix": "Plan-side arithmetic nit; no deliverable impact.",
          "propagate_to": null
        }
      ]
    },
    "Lens4": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "_aux/Hardness_Plan.md:74-110 and _aux/Council_Reports/S1_B_adversarial.md:[B3]",
          "issue": "Strict projection is Opus 47 / Gemini 41 / combined 44 against Plan 55.5 and Council B 54/46/50; breadth is exactly 4 services at >=5% (threshold 4) with linear at 53% against the Plan's claimed 34% and Council B's 47%. Gemini has roughly one call of margin, not 'room'",
          "fix": "Band is PASS on both models - no revision. S2 must not add Linear-only OE steps without a compensating cross-service step, and should explicitly exercise gcalendar list_events plus an Airtable existing-ticket sweep. S4 should expect Gemini runs in the 33-45 band.",
          "propagate_to": "S2"
        }
      ]
    },
    "Lens5": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MODERATE",
          "location": "5_Prompt.txt:11",
          "issue": "The prompt supplies the L31 retraction wording verbatim. Council B's primary defence (Task 39 Gemini failed 6/6 with the phrasing present in the rubric) is invalid - rubrics are judge-visible, not agent-visible. The surviving defence (the clause is gated behind Lever 2) is valid but converts the beat into a displaced lever behind Lever 2's discovery gate (Learnings item 9 / item 20), so the dual-model mix has two measurable legs, not three",
          "fix": "No prompt edit - removing the wording would strip the anti-hedging instruction that makes the beat forcing. S3: two atomic criteria graded on substance not lexical echo (a) earlier QC pass does not hold, (b) push should not be treated as closeable yet. S4 pre-registration per StarPM item 20: if a Gemini run issues the retraction, score as prompt-supplied wording and re-attribute to Lever 2; if it fails, verify from the trajectory whether it reached the negative determination at all.",
          "propagate_to": "S3"
        },
        {
          "severity": "MODERATE",
          "location": "5_Prompt.txt:5,7",
          "issue": "The Linear-vs-Airtable routing partition has boundary items (unfinished filter run, flagged water heaters, South no-access unit, two condensate-drain units) that competent agents will route differently; neither council examined the partition item by item",
          "fix": "S2 pins one unambiguous item per side (two North HVAC units -> Airtable; West QC coverage gap -> Linear) and states boundary items may go either way. S3 must not require a boundary item in a specific channel and must not penalise dual filing.",
          "propagate_to": "S2"
        },
        {
          "severity": "MINOR",
          "location": "5_Prompt.txt:7",
          "issue": "tblMaintenanceTickets carries 4 water-heater decoy tickets (Tommy Reyes's unit, Pinecrest 12) that could induce an update-instead-of-create; the push's actual field items have no existing ticket, so the create is unique by construction",
          "fix": "S3 grades the Airtable write on content, never a record id, and does not fail an agent that also updates. S2 pins appPropertyOps/tblMaintenanceTickets and writes no owner or status field (the table has only Ticket Number, Description, Priority, Completion Date).",
          "propagate_to": "S3"
        }
      ]
    },
    "Lens7": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "AUDIT_prompt.md:LENS 7",
          "issue": "Anti-rationalization scan found 6 'I considered flagging X but decided it's fine because...' lines: R1 state-flip, R2 spot-check subset, R3 routing partition, R4 unnamed Lever-8 hop B target, R5 deference to Council B's L31 defence, R6 vacuous atom pass",
          "fix": "All 6 promoted to logged findings (A-5, A-4, A-2, A-8, A-3, A-10). Zero silently cleared. R4 and R5 rejected outright as deference-to-prior-council rationalizations. No promoted finding forces a sub-dim below 5, so the scan does not convert the verdict to REVISE.",
          "propagate_to": null
        }
      ]
    },
    "Lens8": { "status": "PASS", "findings": [] },
    "validator_notes": {
      "status": "NOTE",
      "findings": [
        {
          "severity": "MINOR",
          "location": "5_Prompt.txt:1",
          "issue": "validate.py WARN 'bolt-on candidate' on sentence 1",
          "fix": "FALSE POSITIVE, independently re-derived. 'Preventive Maintenance Push' appears exactly ONCE in the prompt (sentence 1); removing it strands 'That'/'it' with no antecedent and leaves the initiative unnamed across the remaining 13 sentences. The heuristic matches capitalised multi-word spans and cannot see the lowercase coreference chain ('That','it','this','the push'). No edit. Record in Tasks/_meta/Linter_Justifications.md.",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "_aux/Validator_Reports/prompt.md",
          "issue": "NOTE 'distinct services referenced: 2' is an inverted-signal regex artifact; the prompt names zero services (regex-verified), which is precisely why Explicit Tool Mention scores 5",
          "fix": "No action. Recorded so no downstream gate reads it as a cross-service shortfall.",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "_aux/Validator_Reports/prompt.md",
          "issue": "NOTE 'word count 313 over 300' advisory; removal test run on all 14 sentences - only S5 survives grammatically and it plants Lever 1",
          "fix": "No action; nothing is cuttable without losing a write ask or a coreference anchor.",
          "propagate_to": null
        }
      ]
    },
    "infra": {
      "status": "NOTE",
      "findings": [
        {
          "severity": "NOTE",
          "location": "_aux/Fact_Ledger.json:lifecycle.today",
          "issue": "PRE-DECLARED KNOWN DEFECT: lifecycle.today is null so Validators/validate.py:464 falls back to the hardcoded Brookfield date 2026-06-12 and prints it as 'the single date-alignment source for prompt + OE + rubrics'. Wrong for starpm; authoritative date is 2026-07-01 per _aux/Universe_Index/today_horizon.json. Validators/universes.py already carries the correct value, so the fallback bypasses an existing authority",
          "fix": "(1) Backfill lifecycle.today = '2026-07-01'; (2) change validate.py:464 to get_universe_constants(detect_universe(task_dir))['today']; (3) until (1) lands, S2/S3 must date-anchor to _aux/Universe_Index/today_horizon.json. Fix (1) should land BEFORE S2 starts, since 6_Oracle_Events.txt is still an unfilled template. Prompt itself is correct against 2026-07-01 and is unaffected.",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "_aux/Hardness_Plan.md:94-112",
          "issue": "Plan's service-breadth table projects linear at 34% with 6 services at >=5% and instructs 'keep Linear under 35%'; strict re-derivation gives 53% with exactly 4 services at >=5%. The instruction was unachievable given the core question resolves in a Linear column and 3 of 6 writes are Linear writes",
          "fix": "Breadth gate still passes (4 at >=5% against a threshold of 4; dominant 53% under the 60% ceiling). Record the corrected figures at S4.",
          "propagate_to": null
        }
      ]
    }
  },
  "scores": {
    "unique_ground_truth": { "score": 5, "scheme": "1/3/5", "reason": "four readings enumerated, all converge on one end-state; universe closes the closing conditional on the negative branch on four independently-sourced grounds" },
    "feasibility": { "score": 5, "scheme": "1/3/5", "reason": "all six writes map to real StarPM tools; T10 cluster dimension carried across South/North/East/West; no conflicting instruction; save_issue.assignee 'null' typing is harmless because the prompt says 'named on it'" },
    "explicit_tool_mention": { "score": 5, "scheme": "1/5", "reason": "regex-verified zero tool names, MCP-server names, parameter names, internal IDs, ISO dates, dollar amounts and non-ASCII characters" },
    "prompt_clarity_and_specificity": { "score": 5, "scheme": "1/3/5", "reason": "write-action-divergence and delegation-clarity hard gates clean (0 'I'll [verb]'); three residuals logged (A-1, A-2, A-4) each bounded by a discriminator the prompt itself supplies, none producing a write-vs-no-write or act-vs-defer fork" },
    "contrived_unnatural": { "score": 5, "scheme": "1/3/5", "reason": "no command list, numbered steps, exact-timestamp demand or format constraint; difficulty is scattered information plus prose-versus-state conflict" },
    "truthfulness": { "score": 5, "scheme": "1/3/5", "reason": "17-row per-atom evidence table, every row personally retrieved from _aux/Universe_Split/ this pass; zero major and zero minor factual errors; every authority claim soft-verbed per constraint 8; constraint-7a counter-check against OPS-40 and OPS-91 clean" },
    "tool_use_cross_service": { "score": 5, "scheme": "1/5", "reason": "the load-bearing conclusion requires joining Linear state_id, Linear prose, Slack top-level posts, Slack thread replies and Calendar agendas; 7 of 8 services exercised" },
    "investigation": { "score": 5, "scheme": "1/5", "reason": "not pre-solved; the prompt asserts the opposite of the ground truth and names no root cause, count, open item or culprit" },
    "coherence": { "score": 5, "scheme": "1/5", "reason": "independently re-derived: 'Preventive Maintenance Push' appears exactly once (sentence 1) and four downstream coreferences depend on it, so the removal test fails and the validator WARN is a false positive" },
    "persona": { "score": 5, "scheme": "1/3/5", "reason": "sign-off-or-kick-back is the literal centre of Jaime's brief; voice matches at 313 words, short declaratives, observation-first, zero emoji; she is an authoring persona, not an NPC" },
    "business_function": { "score": 5, "scheme": "3/5", "reason": "assigned=3, prompt_primary=3; Category 3 is her home function per 3_StarPM_TASK CATEGORIES.md:62, mapping to subcategory 3.2 with the 3.1 signature move as the climax; Category 3's own Primary-systems row lists all five write surfaces used" },
    "alignment_with_todays_date": { "score": 5, "scheme": "1/3/5", "reason": "all six relative phrases resolve cleanly against 2026-07-01 with confirmed data in every window; 27 future calendar rows are legitimately forward-facing per the spec carve-out; latest push artifact is OPS-186 2026-06-17" },
    "universe_data_exists": { "score": 5, "scheme": "1/5", "reason": "every trajectory link materialised and re-verified, including Lever 8 hop B (OPS-34 comment) and the C001 thread structure (56 replies / 37 parents), neither of which the prior councils pinned" },
    "universe_cross_service_coherence": { "score": 5, "scheme": "1/5", "reason": "4_Changelog.json is empty and the inject SQL is template-only, so zero CB edits exist; base-universe noise (OPS-34 title/comment mismatch, dangling #make-ready reference, duplicate calendar rows, identical-title pairs) falls under the QC spec's well-supported-beats-low-support note" }
  },
  "density_projection": {
    "midpoint": 44,
    "band": "PASS",
    "breadth_services": 7,
    "breadth_band": "PASS",
    "scheme": "starpm_v4_per_model",
    "per_model": {
      "opus": { "midpoint": 47, "range_low": 38, "range_high": 58, "band": "PASS" },
      "gemini": { "midpoint": 41, "range_low": 33, "range_high": 50, "band": "PASS" }
    },
    "bottom_up_strict_floor": { "opus": 43, "gemini": 34 },
    "dominant_service": "linear",
    "dominant_share_pct": 53,
    "services_at_or_above_5pct": 4,
    "hardness_plan_midpoint": 55.5,
    "council_b_midpoint": 50
  },
  "lever_preservation": {
    "expected": 5,
    "preserved": 5,
    "missing": [],
    "levers": {
      "lever_2_structured_db_skip": "TRACES",
      "lever_9_authority_dismissal_persona_self": "TRACES",
      "lever_1_latching_loudest_wrap": "TRACES",
      "lever_8_multi_link_chain": "TRACES",
      "lever_5_thread_reply_blindness": "TRACES"
    },
    "l31_retraction_beat": "PRESENT_BUT_DISPLACED_BEHIND_LEVER_2",
    "escape_valve_counter_check": "CLEAN",
    "constraints_honoured": 10,
    "constraints_violated": 0,
    "f7_ambiguous_target": "CLEAN",
    "f8_non_atomic_enum": "CLEAN",
    "f9_unreconciled_future_evt": "CLEAN"
  },
  "regression_anchors": { "passed": 62, "failed": 0, "total": 62 },
  "similarity": { "max_composite": 27.2, "corpus_size": 44, "band": "below_40" },
  "anti_rationalization_scan": { "candidates_found": 6, "promoted": 6, "silently_cleared": 0, "rejected_as_deference": 2 },
  "bucket_1_risk_pct": null,
  "iteration": 1,
  "timestamp": "2026-07-26T02:20:00-05:00"
}
```
