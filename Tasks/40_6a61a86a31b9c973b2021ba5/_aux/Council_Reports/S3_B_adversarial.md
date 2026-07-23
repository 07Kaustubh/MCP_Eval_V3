# Council B — Adversarial QC (S3 Rubrics phase)

**Task:** `Tasks/40_6a61a86a31b9c973b2021ba5` (StarPM V4 — Mesa Vista 7B water heater scope correction, Carlos Mendez persona, 2026-07-01)
**Artifact under review:** `7_Rubrics.json` (16 outcome rubrics, 0 process)
**Council B version:** v3 (adversarial QC, strict interpretation)
**Reviewer stance:** heaviest single sub-agent call in pipeline; scoring under the strictest reasonable reading of `Docs/7_QC_Spec_Doc1.json`, `Docs_starpm/2_Rubrics_V3_Guidelines.md`, `Evals_starpm/3_Rubrics_Eval.md`, `Reference/Rubric_Format.md`, and `Docs_starpm/12_Always_Failing_Rubrics.md`.

---

## Rubric inventory (for reference)

| # | Sub | Write action | Content anchor |
|---:|:---:|---|---|
| 1  | 1.1 | Airtable update rec92f4a1c8e17bd3 | (write existence)                                       |
| 2  | 1.2 | Airtable → fldPriority | `selHigh`                                                          |
| 3  | 1.2 | Airtable → fldDescription | (a) escalation, (b) $1,850 full-replacement, (c) Thursday retained |
| 4  | 1.1 | Linear OPS-231 update | (write existence)                                                   |
| 5  | 1.2 | Linear OPS-231 description | full-replacement ≈$1,850 + Thursday retained                    |
| 6  | 1.1 | Linear OPS-231 save_comment | (write existence)                                             |
| 7  | 1.2 | Linear OPS-231 comment body | (a) diagnostic/full-replacement, (b) escalation, (c) Thursday |
| 8  | 1.1 | Slack post in C001 thread 1782824160.000302 | send (not draft)                              |
| 9  | 1.2 | Slack message body | (a) corrected scope, (b) High priority, (c) Thursday retained          |
| 10 | 1.1 | Gmail draft → ap@hillcountryplumbing.com | (write existence)                              |
| 11 | 1.2 | Gmail Diane body | full unit replacement Ruud RS75 ≈$1,850 + Thursday morning              |
| 12 | 1.1 | Gmail draft → tanya.mitchell@gmail.com | (write existence)                                |
| 13 | 1.2 | Gmail Tanya body | full-replacement framing + Thursday + no internal $ figures             |
| 14 | 1.1 | Gmail draft → robert.finley@gmail.com | (write existence)                                 |
| 15 | 1.2 | Gmail Robert body | ≈$310 → ≈$1,850 + diagnostic reason + Thursday                         |
| 16 | 1.1 | Calendar event on Carlos's calendar Thursday 2026-07-02 AM at Mesa Vista 7B | (bundled write) |

**Category balance:** 16 outcome / 0 process = 100% outcome (matches V3 reference tasks 11–14). 8 write actions × (1.1 + 1.2) = 16 rubrics; calendar collapses into a single 1.1 with light content constraints.

---

## B1 — QC sub-dim scoring (`Docs/7_QC_Spec_Doc1.json`)

Every applicable sub-dim scored under STRICTEST reading. Scale is 1/3/5.

| Sub-dim | Score | Justification |
|---|:---:|---|
| **Overall Rubric Quality** (severity gates + absolute counts) | **5** | 0 Major, 0 Moderate, 0 Minor across all 16 rubrics. Absolute-count gates (Major ≥ 3 = FAIL; Major+Moderate ≥ 5 = FAIL; total ≥ 8 = FAIL) all clear at zero. Severity swap (July 2026): no Overly Specific violations (all agent-generated content uses `(or similar phrasing)`), no Under Specific (all exact-match slots on structured fields — IDs, ticket numbers, emails, thread_ts, dollar figures — are exact). |
| **Rubric Category Balance** (outcome > process) | **5** | 16/16 outcome = 100%. Matches V3 refs (Task11-14 all 100% outcome). |
| **Process Rubrics** (present only when 3-condition test passes) | **5** | Zero present. Three-condition test would fail here anyway — every behavior the CB might have tempted to make Process is already provable via a tighter Outcome (scope value in body, priority value in field, etc.). |
| **Agent-Centric Phrasing** | **5** | All 16 titles start with `The Agent` (7 titles) or `The Agent's` (9 titles). No passive voice. Verbs correctly split: 1.1 uses `updates / adds / posts / drafts / creates`; 1.2 uses `sets / revises / includes / covers`. |
| **Atomicity** | **5** | Each write action has its own 1.1 (existence) plus its own 1.2 (content) — no bundled writes. The three "(a),(b),(c)" bundles (rubrics 3, 7, 9) are single-artifact narrative-content bundles per Rubric_Format.md "Bundle ONLY when a single write action contains multiple interconnected parts of the exact same request." Multi-recipient rule N/A (all sends single-recipient). |
| **Self-Containment** | **5** | Every expected value is embedded verbatim in the title itself: `rec92f4a1c8e17bd3`, `MT-2026-1327`, `selHigh`, `OPS-231`, `C001`, `1782824160.000302`, `ap@hillcountryplumbing.com`, `tanya.mitchell@gmail.com`, `robert.finley@gmail.com`, `2026-07-02`, `Mesa Vista Unit 7B`, `$1,850`, `$310`, `Ruud RS75`. Judge does not need the universe. |
| **Completeness** | **5** | 8 prompt-implied write actions × 1.1+1.2 = 16 rubrics. All 8 write actions from OE 12-19 covered end-to-end (see B7 and B10). |
| **Flexibility** | **5** | `(or similar phrasing)` correctly applied to agent-generated free text (rubrics 3, 5, 7, 9, 11, 13, 15). `approximately` correctly applied to the $1,850 and $310 dollar figures. Exact-match strictly reserved for IDs, emails, dates, thread_ts, and the categorical `selHigh` choice. Calendar rubric 16 accepts "a similar Thursday morning window" — flexible around the exact 08:00-12:00 anchor. |
| **Accuracy** (values grounded in `_aux/Universe_Split/`) | **5** | Per S2 Verification_s2.md: rec92f4a1c8e17bd3, MT-2026-1327, OPS-231, thread_ts 1782824160.000302 with reply at 1782863220.000303, QB bill 195836274018 with Line[0].Description carrying the "Full unit replacement recommended, approx 1850 dollars", Diane's msg id e2f3a4b5c6d789ab, all three email addresses, and 2026-07-02 Thursday all verified. `verify_universe_atoms.py` passed with 0 fails / 0 warns. |

**B1 overall: PASS (5/5 on every applicable Rubric sub-dim).**

---

## B2 — Adversarial alt-path attempts

Attempted 5 alt-paths that a reasonable agent might take. Every attempt fails on a genuine intent gap, not on an over-specified rubric.

| Alt-path attempt | Rubric hit | Rubric legitimate? |
|---|---|---|
| Agent uses `slack_send_message_draft` instead of `slack_send_message` in the C001 thread. | 8 fails. | **YES.** Prompt says "so anyone following sees the call before Hill Country goes ahead" — that requires an actual post. Draft-tool substitution is a StarPM parameter trap explicitly documented in `AGENTS.md` (StarPM section) and in `Reference/Rubric_Format.md` under tool-capability mismatch. The rubric encodes a functional requirement ("must actually post"), not a method lock-in — the send tool is the only realistic path to satisfy "anyone following sees the call." Rubric 8's phrasing "send-message action rather than the draft action" does NOT name the tool identifier (`slack_send_message_draft`) — it names the functional distinction. Not a tool-name-in-title violation. |
| Agent phrases Diane's draft body differently but still requests full replacement + Ruud RS75 + ≈$1,850 + Thursday. | 11 passes. | **YES.** Rubric 11 title says "(or similar phrasing)" — the load-bearing checks are the full-unit-replacement request, the ≈$1,850 figure, and the Thursday morning slot. Any body carrying those three passes. |
| Agent's Tanya draft mentions the internal ≈$310 figure while explaining the change. | 13 fails. | **YES.** Prompt frames tenant-facing communication as "an update on the timing for the week" — internal cost figures are inappropriate for tenant. OE 17 explicitly makes this constraint. Rubric is testing tenant-communication hygiene, not agent phrasing. |
| Agent's Robert draft says "cost increased significantly" without naming ≈$310 → ≈$1,850. | 15 fails on content check. | **YES.** Prompt says "Robert a heads-up on the cost" — the cost change from ≈$310 to ≈$1,850 is the entire point of the owner heads-up. Vague language fails the owner's need to know the delta. Rubric uses `(or similar phrasing)` for prose but the two dollar figures are the load-bearing content. |
| Agent creates the calendar block for Thursday afternoon (13:00-17:00) instead of morning. | 16 fails. | **YES.** Prompt says "put the install on my calendar for Thursday morning so I'm blocked out to be onsite when the crew shows up" — install is Thursday morning per Diane's Gmail (OE 5) and the retained scope. Afternoon block does not fulfill the intent. Rubric evidence says "e.g., 08:00 to 12:00 -05:00 or a similar Thursday morning window" — appropriately flexible on the exact window. |
| Agent updates Linear description with corrected scope BUT phrases it as "full water heater unit swap" rather than "full water heater unit replacement". | 5 passes. | **YES.** Rubric 5 accepts "approximately $1,850 (or the exact $1,850)" as the load-bearing content, and title says "(or similar phrasing)" — synonymous scope-verb phrasing passes. |

**B2 overall: no over-specification defects. Every rubric alt-path failure maps to a genuine intent gap.** GO.

---

## B3 — Tool-call density projection

Re-projected midpoint for a real Opus 4.8 run under strictest per-service accounting:

| Component | Range | Midpoint |
|---|---|---:|
| Base discovery (contacts × 3, Airtable base+table+search, Slack channel list, Linear list) | 6-9 | 7.5 |
| L1 Latching decoy reads (agent lands on closed Unit 14 records first) | 3-5 | 4.0 |
| L2 QB `list_entities` → `get-bill` on Hill Country diagnostic to read Line[0].Description | 3-5 | 4.0 |
| L5 Slack `search_public` → `read_thread` to surface the evening reply | 2-4 | 3.0 |
| L7 Multi-write (8 writes across 5 services) | 8-10 | 9.0 |
| L8 Multi-link chain reads (bill number lookup, thread linkage, Linear description) | 4-6 | 5.0 |
| L9 Authority read (Tony's authority parent visible from base Slack search) | 1-2 | 1.5 |
| Cross-service triangulation buffer | 3-6 | 4.5 |
| **TOTAL** | **30-47** | **~38.5** |

**Verdict: THIN (band 40-49 by generous reading; ~38 midpoint by strict reading).**

Prior verification (`_aux/Verification_s2.md`) documented a THIN carry accepted at S1 and re-affirmed at S2 (Council B-B3 v3 re-projected 38-40, AUDIT re-projected 28-30). The rubric set at S3 neither NARROWS scope (all 8 write actions retained) nor EXPANDS scope (no new writes added beyond OE) — inherits the S1+S2 THIN carry documented in `_aux/Hardness_Plan.md` and per AGENTS.md Rule 11.

**HARD FLAG (carried forward):** monitor real-run average across 6 runs at platform verification. If average lands below the 40 absolute floor, route to `PIPELINE REDO`.

**B3 verdict: THIN (accepted under documented carry). Not a Council B block by itself; adds to the density flag list at FINAL.**

---

## B4 — Hardness lever coverage matrix

Every selected lever from `_aux/Hardness_Plan.md` must be traversed by at least one Outcome rubric to pass.

| Lever | Mechanism | Rubric(s) that force traversal | Verdict |
|---|---|---|:---:|
| **L1 Latching** — resolved Tommy Reyes / Unit 14 water-heater incident (closed 5/16) is more findable than active Mesa Vista 7B | Rubric 1 (Airtable update rec92f4a1c8e17bd3, ticket MT-2026-1327). Agent that latches on Unit 14 records MT-2026-1211 / MT-2026-1256 fails rubric 1 because those records are for a different unit and are already closed. | PASS |
| **L2 QB structured-DB skip** — scope truth sits ONLY in `Line[0].Description` on QB bill 195836274018, not in TotalAmt or vendor Gmail | Rubrics 3, 5, 7, 11, 15 all require the $1,850 full-replacement scope; the only universe surface stating "full unit replacement recommended, approx 1850 dollars" is the QB line description. Agent that reads Gmail + Slack + skips QB line description lands ≈$310 exchanger scope and fails all five. | PASS |
| **L5 Thread-reply blindness** — Carlos's tenant-relay parent (1782824160.000302) frames low urgency; evening reply (1782863220.000303) flips priority | Rubric 2 (selHigh, not selMedium) is directly load-bearing. Rubric 3(a) requires the "overnight escalation with the tenant without hot water and an active leak" in fldDescription. Rubric 7(b) requires the escalation in the Linear comment. Rubric 9(b) requires the "escalation to High priority" in the Slack thread message. Four rubrics enforce reading the reply. | PASS |
| **L7 Multi-write diversification** — 8 writes across 5 services | Airtable (rubric 1), Linear-issue (rubric 4), Linear-comment (rubric 6), Slack (rubric 8), Gmail × 3 (rubrics 10, 12, 14), GCalendar (rubric 16). 5 distinct services, 8 write rubrics. | PASS |
| **L8 Multi-link chain** — Slack thread → Airtable ticket → Linear issue → QB bill line description | End-to-end scope-value propagation enforced: rubric 3 (Airtable description carries $1,850) → rubric 5 (Linear description carries $1,850) → rubric 7 (Linear comment cites diagnostic) → rubric 9 (Slack thread reply covers scope) → rubrics 11, 15 (Gmail bodies carry $1,850). Agent that breaks any hop of the chain fails one or more rubrics. | PASS |
| **L9 Authority dismissal** — Tony Reyes (Lead Maintenance) posted "exchanger swap only, tank sound, keeps us on Robert's June budget" in C001 authority parent 1782789240.000301 | Rubrics 5, 7, 11, 15 all require the $1,850 full-replacement scope. Agent that accepts Tony's authority framing lands ≈$310 and fails all four. Rubric 15 is the sharpest — it requires the *cost delta narrative* $310 → $1,850 in the owner draft, which explicitly overrides Tony's frame. | PASS |

**B4 overall: 6/6 levers each covered by ≥1 outcome rubric.** GO.

---

## B5 — Reverse-coverage (rubric → prompt sentence)

Every rubric must map to at least one sentence in `5_Prompt.txt`. Flag any rubric that goes beyond the prompt.

| Rubric | Prompt sentence |
|---:|---|
| 1  | L9 "Bring the maintenance ticket current with the priority from last night's call and the scope we're actually going with." |
| 2  | L5 "The ticket went in Monday night at medium priority off Tanya's early read on the drip. Then last night Tanya called again and it turned into something different." + L9 "the priority from last night's call" |
| 3  | L9 "the priority from last night's call and the scope we're actually going with" + L7 "whatever the diagnostic actually points to is the scope I want to move on" |
| 4  | L9 "Update the operations tracking issue so the team sees where it landed" |
| 5  | L9 "so the team sees where it landed" + L7 "whatever the diagnostic actually points to is the scope" |
| 6  | L9 "drop a note walking through the rationale" |
| 7  | L9 "walking through the rationale" + L7 (diagnostic narrative) + L5 (tenant escalation narrative) |
| 8  | L9 "Drop back into the tenant thread with the same rationale so anyone following sees the call before Hill Country goes ahead" |
| 9  | L9 same-thread rationale requirement |
| 10 | L9 "Draft Diane the revised confirmation so she can pull the right parts" |
| 11 | L9 same + L11 "Parts need pulling today so Hill Country's ready for Thursday morning" |
| 12 | L9 "Tanya an update on the timing for the week" |
| 13 | L9 "an update on the timing for the week" (tenant-appropriate framing implied by tenant recipient) |
| 14 | L9 "Robert a heads-up on the cost" |
| 15 | L9 "heads-up on the cost" (implies delta from prior expectation, which prompt establishes at L3 as "right around 310 dollars") |
| 16 | L9 "put the install on my calendar for Thursday morning so I'm blocked out to be onsite when the crew shows up" |

**B5 overall: all 16 rubrics reverse-covered. Zero rubrics go beyond the prompt.** GO.

---

## B6 — Adversarial atomicity + entity-swap check

### Atomicity

| Rubric | "Fails for two unrelated reasons?" |
|---:|---|
| 1, 4, 6, 10, 12, 14 | No — pure 1.1 existence rubrics on a single write. |
| 2 | No — single categorical field value (`selHigh`). |
| 3, 7, 9 | Bundled (a)(b)(c) narrative rubrics. Per Rubric_Format.md, bundling is permitted "when a single write action contains multiple interconnected parts of the exact same request." All three describe a single coordinated narrative on a single artifact (ticket description / Linear comment / Slack message). The three narrative elements are causally linked (escalation drove the priority flip, scope correction drove the dollar figure, Thursday retention is the conclusion) — this matches V3 reference-task Task 11 rubric 6 and Task 14 rubric 3. Not a defect. |
| 5, 11, 13, 15 | Two-element bundles (scope + timing, cost delta + reason, etc.) on a single artifact — same permitted-bundle rationale. |
| 8 | No — single functional requirement (post to specific thread using send-not-draft). The "send-message action rather than the draft action" clarifier is functional disambiguation, not a second failure axis. |
| 16 | Slightly compound (date + morning + location + purpose) but describes a single calendar event with mandatory bundled parameters. V3 refs (Task 12 rubric 12) do the same for calendar events. |

**No atomicity defects flagged.**

### Entity-swap

For every rubric that names a specific person alongside a workstream, checked whether a DIFFERENT person in the universe could plausibly be attributed to the same workstream and confuse the judge.

| Named person | Rubric(s) | Confusable? |
|---|---|---|
| **Tanya Mitchell** (tenant, tanya.mitchell@gmail.com) | 12, 13 | No other Tanya in universe (Fact_Ledger confirms single `tanya` alias). |
| **Robert Finley** (owner, robert.finley@gmail.com) | 14, 15 | No other Robert in universe (Fact_Ledger confirms single `robert` alias). |
| **Diane** at Hill Country (ap@hillcountryplumbing.com) | 10, 11 | Note: Fact_Ledger surfaces TWO Dianes — Diane Flores at Lone Star Maintenance Supply (`diane.flores@lonestarmaintenancesupply.com`) and Diane at Hill Country (`ap@hillcountryplumbing.com`, unnamed in contacts but confirmed as the diagnostic-email sender in OE 5). Rubrics 10 and 11 target the address `ap@hillcountryplumbing.com` — the Hill Country AP address, not the Lone Star address. This is exact-match on the email so the confusion cannot pass the rubric. NOT a defect. |
| **Carlos Mendez** (agent's own persona, carlos.mendez@starpm.com) | 16 (calendar owner) | Only one Carlos in universe. |
| **Tony Reyes** (authority-dismissal author) | not named in any rubric title | Correctly kept out of rubric-titles — Tony is the authority to *override*, not the target of any write. |
| **Tommy Reyes** (closed Unit 14 tenant, decoy) | not named in any rubric title | Correctly kept out. Rubric 1's exact record id `rec92f4a1c8e17bd3` cannot resolve to Tommy's MT-2026-1211 or MT-2026-1256. Latching decoy fails at the ID check. |

**Explicit Tommy-vs-Tony check:** Tommy = tenant (closed Unit 14); Tony = staff Lead Maintenance Tech (authority). Rubrics correctly attribute to different persons (Robert = owner, Tanya = tenant) and never name Tommy or Tony. The two-Reyes latch-and-dismiss pattern is preserved as a hardness lever without leaking into the rubric surface where entity confusion could false-fail an agent.

**B6 overall: no atomicity or entity-swap defects.** GO.

---

## B7 — Cross-artifact consistency (prompt ↔ OE ↔ rubric)

### Prompt-implied write actions walked forward

| # | Prompt phrase | OE step | Rubric(s) |
|---|---|---|---|
| a | "Bring the maintenance ticket current" | OE 12 | 1, 2, 3 |
| b | "Update the operations tracking issue" | OE 13 | 4, 5 |
| c | "drop a note walking through the rationale" | OE 14 | 6, 7 |
| d | "Drop back into the tenant thread" | OE 15 | 8, 9 |
| e | "Draft Diane the revised confirmation" | OE 16 | 10, 11 |
| f | "Tanya an update on the timing for the week" | OE 17 | 12, 13 |
| g | "Robert a heads-up on the cost" | OE 18 | 14, 15 |
| h | "put the install on my calendar for Thursday morning" | OE 19 | 16 |

All 8 prompt asks map cleanly to 1 OE write step and ≥1 rubric.

### OE steps walked forward (no over-coverage)

OE 1-11 (11 steps): all read/discovery steps; no rubrics required per outcome-testing convention.
OE 12-19 (8 write steps): all covered by ≥1 outcome rubric (see B10 below).

Zero orphan rubrics (rubrics without an OE step). Zero orphan OE writes (OE write steps without rubric coverage).

**B7 verdict:** PASS.

---

## B10 — OE 12-19 → rubric map

| OE | Write action | 1.1 rubric | 1.2 rubric |
|---:|---|---:|---:|
| 12 | Airtable `update_records_for_table` on rec92f4a1c8e17bd3 | 1 | 2 + 3 (bundled priority + description) |
| 13 | Linear `save_issue` on OPS-231 | 4 | 5 |
| 14 | Linear `save_comment` on OPS-231 | 6 | 7 |
| 15 | Slack `slack_send_message` in C001 thread | 8 | 9 |
| 16 | Gmail `create_draft` to Diane | 10 | 11 |
| 17 | Gmail `create_draft` to Tanya | 12 | 13 |
| 18 | Gmail `create_draft` to Robert | 14 | 15 |
| 19 | GCalendar `create_event` on Carlos's calendar | 16 | (bundled into 16) |

Every OE write step 12-19 has ≥1 Outcome 1.1 rubric. All content-carrying OE writes also have ≥1 Outcome 1.2 rubric.

**B10 verdict:** PASS.

---

## B11 — Prompt tell-me → rubric map

Prompt scanned for explicit "tell me / report / identify / flag / list / conclude" cues that would demand a 2.1 rubric on the final response.

| Prompt sentence | Tell-me cue? | 2.1 needed? |
|---|:---:|:---:|
| "I want a fresh look before I sign off." | Ambient wish, not an explicit report-to-me. | No |
| "check whether the detail she has captured lines up with the summary she and Tony are talking off of" | Instrumental — the check itself drives the scope decision, which is embedded in the writes (Airtable description, Linear description, Gmail bodies). | No |
| "Whatever the diagnostic actually points to is the scope I want to move on." | Directive to embed scope in downstream writes, not a report request. | No |
| "Once you've landed the scope, get everything else caught up." | Directive to write, not to report. | No |
| All other L9 asks | Directive writes only. | No |

**Zero explicit tell-me cues in the prompt.** All content requirements (scope narrative, cost delta, escalation reasoning) are correctly embedded in the writes themselves — rubrics 3, 5, 7, 9, 11, 13, 15 carry the content assertions on the artifacts.

The absence of any 2.1 rubric is CORRECT, not a coverage gap.

**B11 verdict:** PASS.

---

## Overall verdict: **GO**

Every Council B check clears at the strictest reading:

- **B1** 5/5 on every applicable Rubric QC sub-dim (Overall Rubric Quality, Category Balance, Process, Agent-Centric, Atomicity, Self-Containment, Completeness, Flexibility, Accuracy).
- **B2** No over-specification defects. Five alt-path attempts all map to genuine intent gaps, not rubric artifacts.
- **B3** Density THIN (~38 strict, ~40-45 generous) — inherits S1+S2 documented carry per AGENTS.md Rule 11 and Hardness_Plan.md. HARD FLAG carried forward to FINAL / platform monitoring.
- **B4** All 6 hardness levers (L1, L2, L5, L7, L8, L9) each covered by ≥1 outcome rubric that forces traversal.
- **B5** All 16 rubrics reverse-covered by ≥1 prompt sentence. Zero rubrics go beyond the prompt.
- **B6** No atomicity defects. Bundled rubrics (3, 7, 9) follow the permitted V3 single-artifact narrative-bundle pattern. Entity-swap check clean (Tommy vs Tony correctly kept out of rubric titles; Diane exact-email match dodges the Diane Flores confusable).
- **B7** Prompt ↔ OE ↔ rubric consistency clean. 8 prompt asks → 8 OE writes → 16 rubrics. No orphans in either direction.
- **B10** Every OE write step 12-19 has ≥1 Outcome 1.1 rubric plus (where applicable) a 1.2 content rubric.
- **B11** Zero explicit tell-me cues in prompt; zero 2.1 rubrics is correct.

### Severity breakdown

| Severity | Count | Rubrics |
|---|:---:|---|
| Major    | 0 | — |
| Moderate | 0 | — |
| Minor    | 0 | — |
| **Total defects** | **0** | — |

### Flags carried forward to FINAL

1. **Density THIN carry** (from S1 + S2 + S3 all inherited). Watch platform 6-run average — if it lands < 40 tool calls, route to `PIPELINE REDO`.
2. **Slack send-vs-draft trap in rubric 8.** This is intentional enforcement per OE 15 and StarPM parameter-trap documentation. FINAL should confirm no answer-leakage exists on this trap and that the AUDIT reads the "send-message action rather than the draft action" clause as functional, not tool-name-in-title.
3. **Two Dianes in universe** (Diane Flores at Lone Star vs the unnamed Diane at Hill Country AP). Rubrics 10 and 11 route via the exact email `ap@hillcountryplumbing.com`, which resolves the ambiguity. FINAL should confirm no rubric or artifact accidentally names "Diane Flores" where Hill Country is meant.

### Fix list

None. No rubric requires revision.

### Recommendation

**Proceed to strict veteran AUDIT (auto-fire per Rule 12).** If AUDIT clears at PASS (STRICT), advance to FINAL. Do not upload to platform before FINAL clears.
