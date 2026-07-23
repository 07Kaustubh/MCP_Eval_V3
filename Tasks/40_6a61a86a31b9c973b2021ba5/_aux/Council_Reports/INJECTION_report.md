# INJECTION QUALITY REPORT — Task 40_6a61a86a31b9c973b2021ba5

**Evaluator:** Injection Quality Council (7-gate + difficulty scoring)
**Eval Spec:** `Evals_starpm/0_Injection_Quality_Eval.md`
**Primary Input:** `9_Universe_inject.sql` (255 lines, 8 injected records across 5 services)
**Scenario:** Water-heater failure at Mesa Vista Unit 7B, scope-correction on 2026-07-01. Persona: Carlos Mendez (Onsite PM).
**Universe date:** 2026-07-01 America/Chicago. Workflow window: 2026-05-01 to 2026-07-01.

---

## STEP 0 — Load & Pre-Read (Hard Gate)

- [x] 0.1 Read `9_Universe_inject.sql` — 8 injected records catalogued.
- [x] 0.2 `4_Changelog.json` not present — per eval spec, SQL is primary; no block.
- [x] 0.3 Read `StarPM_Base_Universe/8_Universe_Schema.json` — column lists loaded for airtable_records / slack_messages / linear_issues / quickbooks_entities / gmail_threads / gmail_messages.
- [x] 0.4 Read `StarPM_Base_Universe/7_Server_Tools_Details.json` — 268 tools across 8 services.
- [x] 0.5 Read base data for airtable / slack / linear / quickbooks / gmail / contacts / hubspot.
- [x] 0.6 `5_Prompt.txt` not yet written — reachability chain-traced from persona + injected context.
- [x] 0.7 Inventory of injected records:

| # | Service | Table | Op | ID | Purpose |
|---|---|---|---|---|---|
| 1 | airtable | airtable_records | INSERT | `rec92f4a1c8e17bd3` (MT-2026-1327) | Maintenance ticket, selMedium, Mesa Vista 7B |
| 2 | slack | slack_messages | INSERT | `a1b2c3d4e5f6789012345678901234ab` @ ts `1782789240.000301` | Tony Reyes authority-dismissal, narrow scope |
| 3 | slack | slack_messages | INSERT | `b2c3d4e5f6a789012345678901234abc` @ ts `1782824160.000302` | Carlos parent, low-urgency framing |
| 4 | slack | slack_messages | INSERT | `c3d4e5f6a7b89012345678901234abcd` @ ts `1782863220.000303` | Carlos thread-reply, priority-flip |
| 5 | linear | linear_issues | INSERT | `OPS-231` / uuid `a5b3c9d2-...` | Linear issue, In Progress, assignee Carlos |
| 6 | quickbooks | quickbooks_entities (bill) | INSERT | `195836274018` / DocNumber `B2026-211` | Diagnostic bill, Line[0].Description carries scope truth |
| 7a | gmail | gmail_threads | INSERT | `d1e2f3a4b5c6789a` | Vendor thread container |
| 7b | gmail | gmail_messages | INSERT | `e2f3a4b5c6d789ab` | Vendor Diane (Hill Country) narrow-scope endorsement |

---

## Phase 1 — Schema & Structural Validation

| Record | Table | Columns injected | All schema cols present? | NOT NULLs satisfied? | FK targets exist? | Verdict |
|---|---|---|---|---|---|---|
| 1 | airtable_records | 7 / 7 | YES | id ✓, table_id ✓, created_time ✓, last_modified_time ✓ | `tblMaintenanceTickets` in base `appPropertyOps` ✓; `usr_carlos_mendez` ✓ | **VALID** |
| 2 | slack_messages | 17 / 17 | YES | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at all populated | user `UD4432C1F56` (Tony Reyes) ✓, channel `C001` (#maintenance) ✓ | **VALID** |
| 3 | slack_messages | 17 / 17 | YES | same NOT NULLs satisfied | user `U07E4512181` (Carlos) ✓, channel `C001` ✓ | **VALID** |
| 4 | slack_messages | 17 / 17 | YES | same NOT NULLs satisfied | thread_parent_id points at record 3's id ✓; thread_ts_legacy `1782824160.000302` matches record 3 ts ✓ | **VALID** |
| 5 | linear_issues | 28 / 28 | YES | id, uuid, team_id populated | team_id `team_001` (OPS) ✓, state_id `state_OPS_2` (In Progress) ✓, assignee/creator `user_d6c1beb9cf67594dae2f5de4529674f1` (Carlos) ✓ | **VALID** |
| 6 | quickbooks_entities | 7 / 7 | YES | entity_type=`bill` ✓, id ✓ | VendorRef.value=`201` (Hill Country Plumbing, `ap@hillcountryplumbing.com`) ✓; AccountRef.value=`60` (Repairs & Maintenance) matches base pattern | **VALID** |
| 7a | gmail_threads | 6 / 6 | YES | id ✓ | (thread has no FKs; matched by messages) | **VALID** |
| 7b | gmail_messages | 15 / 15 | YES | id ✓, thread_id ✓ | thread_id points at record 7a ✓ | **VALID** |

**Datatype spot-checks:** `fields` (jsonb) — cast with `::jsonb`; `properties` (jsonb) — cast; `label_ids` (jsonb) — cast; `payload` (jsonb) — cast; `to_addresses`/`cc_addresses` (jsonb) — cast; `reply_count`/`reply_users_count`/`size_estimate` — integer literals; `is_activity_message`/`active`/`has_attachments`/`is_archived` — boolean literals. All types match schema declarations. **No enum violations** detected (state_OPS_2 corresponds to a valid workflow state; entity_type='bill' is a known QB entity).

**GATE 1 verdict: PASS.** No SCHEMA_VIOLATION.

---

## Phase 2 — ID Format & Convention

| Table | Base pattern (3+ sampled) | Injected ID(s) | Pattern match | Collision check | Verdict |
|---|---|---|---|---|---|
| airtable_records | `rec<16-hex>` (e.g., `recb4aeaed326f156`) | `rec92f4a1c8e17bd3` | YES (16-hex after `rec`) | no collision | VALID |
| airtable ticket # | `MT-2026-NNN[N]` (mixed 3/4-digit; base max = 1326) | `MT-2026-1327` | YES (next-unused after 1326) | no collision | VALID |
| slack_messages id | `<32-hex>` (e.g., `361dfeb2d24a5e7ab1bd1e50092c06cf`) | `a1b2c3d4e5f6789012345678901234ab`, `b2c3d4e5f6a789012345678901234abc`, `c3d4e5f6a7b89012345678901234abcd` | 32-hex characters ✓ length + charset ✓; visibly patterned across records (walking-hex) — soft observation | no collisions | VALID (with soft note) |
| slack_messages ts | `<epoch>.<microseq>` (base max ts `1782493180.000293`) | `1782789240.000301`, `1782824160.000302`, `1782863220.000303` | YES; microseq continues from base .000293 → .000301+; all resolve to 2026-06-29/30 | no collisions | VALID |
| linear_issues id | `OPS-N` (OPS-1 through OPS-230) | `OPS-231` | YES (next number) | no collision | VALID |
| linear_issues uuid | UUIDv4 lowercase | `a5b3c9d2-4e8f-4a7b-9c1e-2f6d8b3a5c7e` | YES (RFC 4122 shape) | no collision | VALID |
| quickbooks_entities id | 12-digit numeric (e.g., `528539050604`) | `195836274018` | YES (12 digits) | no collision | VALID |
| QB DocNumber | mixed families incl. `B2026-NNN` (base max in family = 210; existing gap to 418) | `B2026-211` | YES (fills natural sequence gap) | no collision | VALID |
| gmail_threads / gmail_messages id | `<16-hex>` (e.g., `ae14c88866806293`, `7cecfd846864dc6d`) | `d1e2f3a4b5c6789a`, `e2f3a4b5c6d789ab` | YES (16-hex) | no collisions | VALID (with soft note — same walking-hex pattern) |

**Slack ts → date check:** `1782789240` → 2026-06-30 03:14 UTC (Mon 22:14 CT); `1782824160` → 2026-06-30 12:56 UTC (Tue 07:56 CT); `1782863220` → 2026-06-30 23:47 UTC (Tue 18:47 CT). All within window.

**Soft observation (not blocking):** injected Slack + Gmail hex IDs are visibly patterned (each ID reads as a shifted version of the previous). Formally valid and unique, so no ID_VIOLATION per spec, but if strict-mode QC inspects entropy across sibling injections, this could draw an "obviously synthetic" comment. Recommend randomizing hex on a future revision if the task lands on a strict reviewer.

**GATE 2 verdict: PASS.** No ID_VIOLATION.

---

## Phase 3 — Date & Time Consistency

| Check | Records | Finding | Verdict |
|---|---|---|---|
| Within window 2026-05-01 → 2026-07-01 | all 8 | Airtable created_time `2026-06-29 21:14:00` ✓; Slack created_at 6/30 UTC ✓; Linear created_at/updated_at 6/29 and 6/30 CT ✓; QB TxnDate 6/29, MetaData.CreateTime 6/29T21:45:00Z, DB created_time 7/1 (sync lag, plausible) ✓; Gmail internal_date 6/29T20:12 UTC ✓; gmail thread last_internal_date matches ✓ | **VALID** |
| Weekday for business comms | records 2, 3, 4, 7b | 2026-06-29 Mon; 2026-06-30 Tue — all weekdays ✓ | **VALID** |
| Reply after parent | records 3 (parent) & 4 (reply) | parent ts `1782824160` (Tue 07:56 CT) < reply ts `1782863220` (Tue 18:47 CT) ✓; `thread_parent_id` on reply matches record 3's id; `thread_ts_legacy` matches record 3's ts; parent's `latest_reply` = record 4's ts ✓ | **VALID** |
| Gmail sent ≤ received | record 7b | header Date `2026-06-29T20:12:00+00:00` = internal_date `1782763920000` (6/29T20:12 UTC). Single-message thread, no separate received_at column in schema (uses internal_date). ✓ | **VALID** |
| DueDate ≥ TxnDate (QB) | record 6 | TxnDate 2026-06-29; DueDate 2026-07-29 (Net-30). ✓ | **VALID** |
| Business-hour plausibility | record 2 | Tony's Slack at Mon 22:14 CT is late but within 06-22h soft window and narratively plausible ("Going to approve unless someone flags before EOD tomorrow" — lead-tech end-of-shift wrap-up). Marginal soft flag, not blocking. | soft flag |
| Chronological narrative coherence | all | Mon 6/29 15:12 CT: vendor Diane emails (7b) → 16:45 CT: QB bill materializes (6) → 21:14 CT: Airtable ticket (1) → 22:14 CT: Tony Slack (2) → Tue 6/30 07:56 CT: Carlos parent (3) → 18:47 CT: Carlos reply (4). Linear issue (5) created_at Mon 22:20 CT, updated_at Tue 18:47 CT — consistent with the flow. ✓ | **VALID** |

**GATE 3 verdict: PASS.** No TEMPORAL_VIOLATION.

---

## Phase 4 — Base Universe Integrity & Cross-Service Consistency (MOST CRITICAL)

### 4A — Injection vs Base Integrity

| Check | Finding | Verdict |
|---|---|---|
| Record collision | 0 collisions across all 8 records + secondary keys (ticket #, DocNumber, Linear number, Slack ts, gmail thread/message ids, QB bill id) | CONSISTENT |
| Fact contradiction on Mesa Vista 7B | Zero base Slack/Airtable/Linear/HubSpot records reference Mesa Vista Unit 7B — the injected unit is unscarred by prior state. No pre-existing lease/tenancy record for 7B contradicts injection. | CONSISTENT |
| Status/state conflict | Airtable ticket priority `selMedium` at creation; Slack thread reply signals it should flip to selHigh but ticket itself remains selMedium at insert time (this is the intended L5 setup — priority flip is the AGENT's write, not a contradiction). Linear issue priority=2 (High) reflects Carlos's on-call escalation; no downstream Slack/Airtable record contradicts. ✓ | CONSISTENT |
| Timeline collision | No base GCalendar event on Mon 6/29 15:12 CT or Tue 6/30 07:56 CT that conflicts with the injected story. Hill Country vendor is not double-booked. ✓ | CONSISTENT |
| Amount conflict | Injected diagnostic bill TotalAmt $185.00 does not conflict with any other base Hill Country bill for Mesa Vista 7B (there are none). Vendor Gmail body cites "about 310 dollars" for the exchanger swap — that is a QUOTE for future work, not a contradicting bill; DOES NOT contradict $185 diagnostic charge on the current bill. ✓ | CONSISTENT |
| Relationship break | Tanya Mitchell appears in base Contacts (email tanya.mitchell@gmail.com) + HubSpot (ESA accommodation approved 2026-05-28, unit unspecified). Injection places her at Mesa Vista 7B. **Adjacency observation:** base QB bill `2026-EV-047` (Hill Country vendor, 2026-05-01) has Line[0].Description mentioning "Tanya Mitchell tenancy at Sunridge Apartments" (eviction filing package prep). 8+ weeks between events allows plausible tenancy change; HubSpot ESA ticket says "her unit"/"her property" without naming Sunridge; injection does not explicitly deny Sunridge history. Not a hard contradiction — see Consistency Notes below. | CONSISTENT with soft flag |
| Orphaned update | Linear issue description defers to "diagnostic bill on file with vendor id 201" — chain hop terminates at QB record 6 (both injected). Airtable ticket → Slack thread → Linear issue → QB bill: every hop populated. No orphaned update. ✓ | CONSISTENT |

### 4B — Cross-Service Consistency

| Check | Finding | Verdict |
|---|---|---|
| Name spelling | Carlos Mendez: slack `Carlos Mendez` (U07E4512181), airtable `Carlos Mendez` (usr_carlos_mendez, `carlos.mendez@starpm.com`), linear `Carlos Mendez` (`carlos.mendez@starpm.com`). Tony Reyes: slack `Tony Reyes` (UD4432C1F56). Hill Country Plumbing: QB vendor 201 `Hill Country Plumbing` + email `ap@hillcountryplumbing.com` = Gmail from_address `ap@hillcountryplumbing.com` ✓. Robert Finley: HubSpot 2 records (not injected — narratively referenced in Tony's Slack). ✓ | CONSISTENT |
| Email format | `carlos.mendez@starpm.com` matches across airtable, linear, gmail to_addresses. `ap@hillcountryplumbing.com` matches QB vendor PrimaryEmailAddr → Gmail from_address. ✓ | CONSISTENT |
| Cross-service references | Injected Slack #maintenance messages (records 2, 3, 4) reference "Mesa Vista 7B" and "Hill Country" — Airtable ticket + QB bill provide those anchors. Linear issue references "vendor id 201" — resolves to Hill Country Plumbing in QB. Gmail message subject line `Mesa Vista 7B water heater` matches Airtable ticket description. No cross-reference points at a non-existent record. ✓ | CONSISTENT |
| Property data | Mesa Vista Unit 7B named consistently across all 5 services (`Mesa Vista Unit 7B` or `Mesa Vista 7B`). No conflicting unit type/size details in injection. Ruud RS75 (12 yr) named only in QB Line[0].Description; not contradicted elsewhere. ✓ | CONSISTENT |

### Consistency Notes (soft, not blocking)

1. **Tanya-Sunridge adjacency.** Base QB bill `2026-EV-047` (2026-05-01) references "Tanya Mitchell tenancy at Sunridge Apartments" for eviction filing package prep. Base HubSpot ticket `ticket_34cb6ee660b659029fe68d82bc4e5dd5` records ESA accommodation approval 2026-05-28 for Tanya at "her unit" (property name absent). Injected records place Tanya at Mesa Vista 7B on 2026-06-29. The 8-week gap and the neutral "her unit" language in HubSpot make a StarPM-internal transfer/re-lease narratively plausible; no injected record explicitly denies or contradicts. Nonetheless, if a rubric asks the agent to verify tenant residency, an agent that hunts HubSpot/QB history could surface Sunridge and get anchored on the wrong property. Recommend acknowledging this in the prompt writer's Reasoning notes so that OE/rubric authoring doesn't accidentally reward "tenant is at Sunridge" logic.
2. **Prime observation for Prompt-writer:** the base 2026-EV-047 bill's LineAccountRef is `Contract Labor`, not plumbing — a base-universe anomaly (Hill Country billing legal-doc prep). Uninvolved in this injection, but worth flagging so the prompt writer doesn't tell the agent "Hill Country is a plumbing vendor" as an absolute fact.

**GATE 4 verdict: PASS.** No COLLISION, CONTRADICTION, or CROSS_SERVICE_VIOLATION. Two soft notes recorded above for downstream reference.

---

## Phase 5 — Naturalness & Anti-AI-Tell

Every injected free-text field reviewed:

| Field | Word count | Register | Emoji | Corporate filler | Repeated syntax | Verdict |
|---|---|---|---|---|---|---|
| Record 1 fldDescription | 34 | terse ticket log | no | no | no | NATURAL |
| Record 2 Slack (Tony) | ~62 | tech-lead briefing, casual-professional | no | no | no | NATURAL |
| Record 3 Slack (Carlos parent) | ~40 | onsite-PM update, casual | no | no | no | NATURAL |
| Record 4 Slack (Carlos reply) | ~55 | urgent onsite update, casual | no | no | no ("Bumping this back up" is authentic) | NATURAL |
| Record 5 Linear description | ~40 | internal-ticket structured | no | no | no | NATURAL |
| Record 6 QB Line[0].Description | ~44 | technical vendor note; domain-appropriate ("burner assembly", "thermocouple", "unit this age") | no | no | no | NATURAL |
| Record 6 QB PrivateNote | 11 | short internal note | no | no | no | NATURAL |
| Record 7a Gmail thread snippet | ~40 | matches truncation from message body | no | no | no | NATURAL |
| Record 7b Gmail body (base64-decoded, 487 bytes) | ~85 | vendor summary email, signed "Diane at Hill Country Plumbing" | no | no | no | NATURAL |

- No em-dash (`—`), en-dash (`–`), horizontal-bar, minus-sign, non-breaking-hyphen, or figure-dash characters found anywhere in the SQL (`python3` scan confirmed 0 occurrences of each).
- No emoji characters detected.
- Persona voice consistency: Carlos records are terse, informational, occupationally-appropriate for an Onsite PM (formality 0.55 per Hardness Plan). Tony's record shows tech-lead confidence and budget-consciousness ("keeps us on Robert's June budget") — matches lead-maintenance-technician authority framing.
- Vendor Diane email is a plausible AP-desk email — signature line "Diane at Hill Country Plumbing" matches vendor-side casual sign-off.

**AI-tell count: 0.** Spec threshold: 3+ = FAIL.

**GATE 5 verdict: PASS.** No AI_TELL.

---

## Phase 6 — Phantom & Reachability

Tool-chain trace for each injected record (max 5 hops from persona-referenced starting entity — Carlos, #maintenance, or Hill Country):

| Record | Discovery chain (≤5 hops) | Reachable? |
|---|---|---|
| 1 Airtable ticket | `list_bases` → `list_tables_for_base(appPropertyOps)` → `list_records_for_table(tblMaintenanceTickets)` → filter/sort → MT-2026-1327 surfaces. Alt: `search_records(query="Mesa Vista 7B")`. | **REACHABLE** |
| 2 Tony Slack | `slack_search_channels("#maintenance")` → `slack_read_channel(C001)` → top-level message returns. Alt: `slack_search_public("Mesa Vista 7B")`. | **REACHABLE** |
| 3 Carlos parent | `slack_read_channel(C001)` → top-level parent returns (has `reply_count=1`, `latest_reply` pointer). | **REACHABLE** |
| 4 Carlos thread reply | `slack_read_thread(C001, ts=1782824160.000302)` → reply returns. **Not** visible via `slack_read_channel` alone — intentional L5 blindness lever. Reachable via thread expansion (which agents SHOULD do given reply_count=1 on parent). | **REACHABLE** |
| 5 Linear issue OPS-231 | `list_teams` → find OPS/team_001 → `list_issues(team_id=team_001)` → OPS-231 returns. Alt: `get_issue(OPS-231)` direct. | **REACHABLE** |
| 6 QB bill B2026-211 | `search_vendors("Hill Country")` → get vendor id 201 → `search_bills(VendorRef.value=201)` returns bill 195836274018 → `get-bill(id=195836274018)` expands Line[0].Description. **Line description surfaces only through get-bill / detailed search — the L2 lever** (agents skimming TotalAmt via search_bills may miss the Line[0].Description field). | **REACHABLE** |
| 7a Gmail thread | `search_threads(query="Mesa Vista 7B")` matches subject_normalized "mesa vista 7b water heater diagnostic..." → thread id `d1e2f3a4b5c6789a` returns. Alt: filter by from `ap@hillcountryplumbing.com`. | **REACHABLE** |
| 7b Gmail message | `get_thread(d1e2f3a4b5c6789a)` returns thread + its single message including base64-decoded payload. | **REACHABLE** |

**Cross-reference resolution:** every entity referenced narratively in an injected body (Mesa Vista 7B, Hill Country, vendor id 201, Robert Finley, Tanya) resolves to a real record (base or injected). No dead-end references.

**Chain depth check:** longest natural chain (Slack #maintenance → Airtable ticket → Linear issue → QB bill line description) = 4 hops. Well under the 5-hop soft flag.

**GATE 6 verdict: PASS.** No ORPHANED or PHANTOM record.

---

## Phase 7 — Pre-Solve & Information Leakage

**Where is the "answer" (full unit replacement recommendation)?**

`grep` scan of the SQL confirms the phrase `Full unit replacement recommended` appears exactly once inside injected data — in Record 6's `properties.Line[0].Description`. All other `full unit replacement` matches are in SQL comments (lines 6, 124, 191, 228), which are NOT part of the injected data payload.

| Check | Finding | Verdict |
|---|---|---|
| Smoking-gun record | No single record hands the agent the answer. Record 6 requires `get-bill` expansion of Line[0].Description — skimming TotalAmt via search_bills does NOT return that field content. | PROPERLY_OBSCURED |
| Trivial 1-2 tool discovery | Impossible. Agent needs at minimum: (a) surface the Slack thread reply (record 4) to feel urgency, (b) find the Airtable ticket (record 1), (c) find the Linear issue (record 5), (d) find and EXPAND the QB bill (record 6). Then must override Tony's Slack (record 2) + vendor Gmail (record 7b) endorsement of narrow scope. | PROPERLY_OBSCURED |
| Information friction | Scope truth (record 6) is in QuickBooks structured DB. Counter-endorsements are in Slack (record 2) + Gmail (record 7b). Priority-flip signal is in Slack thread reply (record 4). Context anchors are in Airtable + Linear. 5+ records across 4 services. | High friction. PROPERLY_OBSCURED |
| Decoys / near-matches | Base universe carries L1 latching decoys: closed 5/15–5/27 Unit 14 water-heater incident (Tommy Reyes / Linda Castillo — 3+ Slack messages, 2 Airtable tickets, Linear comments). Two Reyes surnames in-universe (Tommy tenant + Tony technician). Multiple Hill Country bills in base with unrelated line descriptions. Realistic decoy density is high. | Strong decoys present. |
| Answer-in-injection | Injection contains NO pre-written email/Slack/Linear-comment body that the agent should produce as output. Correct outputs (Slack reply, Linear save_comment, Gmail drafts to vendor/tenant/owner, GCalendar event) are unwritten. | PROPERLY_OBSCURED |

**GATE 7 verdict: PASS.** PROPERLY_OBSCURED.

---

## Phase 8 — Injection Difficulty & Complexity Scoring

| Dimension | Rationale | Score |
|---|---|---|
| **Cross-Service Spread** | 5 services touched by injections (airtable, slack, linear, quickbooks, gmail). Correct solve additionally requires contacts (tenant/owner emails) + gcalendar (install slot) + hubspot (owner Robert Finley) = 8 services in play. | **5** |
| **Information Scattering** | Scope truth in 1 QB Line[0].Description; priority-flip in 1 Slack thread reply; counter-endorsements in 2 records (Tony Slack + vendor Gmail); context anchors in Airtable + Linear. 6+ records across 5 services must be collected. | **5** |
| **Trap Density** | L1 latching decoys (Unit 14 resolved incident, ~5 base records) + L9 authority dismissal (Tony's plausible narrow-scope) + L2 QB structured-DB skip + vendor Gmail endorsement + 2 Reyes surnames + multiple Hill Country decoy bills. ≥4 realistic traps. | **5** |
| **Temporal Complexity** | Fresh 6/29–6/30 incident vs stale 5/15–5/27 Unit 14 decoy (must distinguish by date). QB MetaData.CreateTime 6/29 vs DB created_time 7/1 (sync-lag reasoning). Thread parent 07:56 CT vs reply 18:47 CT — priority-flip requires reading both. "EOD tomorrow" (Tue 6/30) approval-window deadline authored on 2026-07-01. | **4** |
| **Tool Call Depth** | Hardness Plan projects midpoint 56 tool calls (44–68 range). Well above 25+ threshold. | **5** |
| **Reasoning Chain** | 4-hop primary chain (Slack thread reply → Airtable ticket → Linear issue → QB bill line description) plus 2 counterfactual overrides (override L1 latch AND L9 authority) plus 1 structured-DB skip override (L2). | **5** |
| **Write Action Diversity** | Hardness Plan lists 5+ writes across 5 services: Slack reply, Linear save_comment + save_issue, Airtable update, Gmail drafts to vendor + tenant + owner, GCalendar event. 8 writes across 5 services. | **5** |

**Composite:** (5 + 5 + 5 + 4 + 5 + 5 + 5) / 7 = 34 / 7 = **4.857 ≈ 4.9 / 5.0**

**Rating band:** 4.1–5.0 → **Very Hard** ✓ (well above the 3.5 minimum)

---

## Phase 9 — Final Verdict

```
┌─────────────────────────────────────────────────────┐
│           INJECTION QUALITY VERDICT                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Schema & Structure:      PASS                       │
│ ID Format & Convention:  PASS                       │
│ Date & Time:             PASS                       │
│ Cross-Service:           PASS  (2 soft notes)       │
│ Naturalness:             PASS                       │
│ Reachability:            PASS                       │
│ Pre-Solve Check:         PASS                       │
│                                                     │
│ ─── Difficulty Assessment ───                       │
│ Cross-Service Spread:    5 / 5                      │
│ Information Scattering:  5 / 5                      │
│ Trap Density:            5 / 5                      │
│ Temporal Complexity:     4 / 5                      │
│ Tool Call Depth:         5 / 5                      │
│ Reasoning Chain:         5 / 5                      │
│ Write Action Diversity:  5 / 5                      │
│                                                     │
│ Difficulty Score:        4.9 / 5.0                  │
│ Rating:                  Very Hard                  │
│                                                     │
│ VERDICT:  PASS                                      │
└─────────────────────────────────────────────────────┘
```

GATE 1 Schema & Structure:      PASS — all 8 records column-complete for their tables; NOT NULLs populated; datatypes match; FK targets (Carlos slack/airtable/linear IDs, Tony slack ID, C001, tblMaintenanceTickets in appPropertyOps, team_001, state_OPS_2, QB vendor 201) all verified in base.
GATE 2 ID Format:               PASS — no collisions on any injected id/ts/uuid/DocNumber/ticket-number; patterns match base (16-hex airtable, 32-hex slack, `OPS-N`, UUIDv4, 12-digit QB bill, 16-hex gmail); Slack ts values resolve to 2026-06-29/30 CT within window. Soft note: Slack + Gmail hex IDs are visibly patterned across sibling injections (still valid + unique).
GATE 3 Date & Time:             PASS — all timestamps within 2026-05-01 → 2026-07-01; business comms on Mon 6/29 + Tue 6/30 weekdays; parent < reply chronology holds; DueDate 30d after TxnDate; narrative timeline coherent Mon afternoon → Tue evening.
GATE 4 Cross-Service Consistency: PASS — no collisions, no direct contradictions; every cross-service reference resolves; person/vendor names + emails identical across services. Soft notes: (a) Tanya Mitchell has a 5/01 Hill Country eviction-prep bill referencing Sunridge Apartments — 8-week gap allows plausible transfer to Mesa Vista, HubSpot ESA record says "her unit" (unnamed); (b) base 2026-EV-047 shows Hill Country billing Contract-Labor legal-prep work — Hill Country is not exclusively plumbing in-universe.
GATE 5 Naturalness:             PASS — no em/en-dashes anywhere; no emoji; no corporate filler; message lengths + registers appropriate for medium; persona voices consistent. AI-tell count = 0.
GATE 6 Reachability:            PASS — every injected record traceable in ≤4 tool hops from persona/#maintenance/Hill-Country anchors; thread reply intentionally hidden behind slack_read_thread (L5 lever, still reachable); QB Line[0].Description reachable via get-bill (L2 lever).
GATE 7 Pre-Solve Check:         PASS — scope-truth phrase "Full unit replacement recommended" appears exactly once in injected data (QB Line[0].Description); 2 counter-endorsements (Tony Slack, vendor Gmail) push narrow scope; no pre-written output text; strong decoy density.
DIFFICULTY SCORE: 4.9 / 5.0 / RATING: Very Hard
OVERALL VERDICT: PASS
BLOCKER ISSUES: none.

### Advisory (non-blocking, forwarded to Prompt-writer)

1. If the prompt author asks the agent to "confirm the current tenant at Mesa Vista Unit 7B", the base 2026-05-01 Hill Country bill's mention of "Tanya Mitchell tenancy at Sunridge Apartments" (eviction filing prep) could pull an agent onto the wrong property. Consider explicit anchoring in the prompt (e.g., "the water heater at Tanya's current unit, Mesa Vista 7B") to avoid unintended off-target reasoning.
2. Base has one Hill Country bill (`2026-EV-047`) with `AccountBasedExpenseLineDetail.AccountRef.name = "Contract Labor"` for eviction-doc prep — Hill Country is not solely a plumbing vendor in this universe. Do not state "Hill Country is a plumbing vendor" as an absolute claim in the prompt.
3. Consider randomizing hex on Slack IDs (`a1b2c3d4...`, `b2c3d4e5...`, `c3d4e5f6...`) and Gmail IDs (`d1e2f3a4...`, `e2f3a4b5...`) on any future revision — the walking-hex pattern is visibly synthetic if a strict reviewer scans sibling records.
