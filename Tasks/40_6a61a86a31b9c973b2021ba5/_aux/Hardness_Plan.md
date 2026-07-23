# Hardness Plan

## Persona and Business Function

- Carlos Mendez, Onsite Property Manager (`p_009` / `carlos.mendez@starpm.com`)
- Property Operations (Cat 1)
- Formality 0.55, verbosity 0.50, active hours 7 AM to 5 PM (America/Chicago)

## Anchoring Scenario

**Water heater failure at Mesa Vista Unit 7B, escalation and scope-correction on 2026-07-01.** Carlos's `maintenance_escalation_waterheater_leak` scripted footprint, extended into an active incident that surfaces the day of the task. Vendor Hill Country Plumbing (existing vendor 201) has completed a diagnostic visit and quoted a scope that materially understates the required work. Tenant Tanya Mitchell (existing contact) is impacted. Owner is Robert Finley (Mesa Vista portfolio, established via 5/28 Slack from Aurora Winona's cluster). The Tommy Reyes / Linda Castillo Unit 14 water-heater incident from 5/15 to 5/27 is RESOLVED in the base universe and serves as a natural L1 latching decoy without any injection.

## Levers Available

| # | Lever | Status | Evidence | Cost range |
|---|---|---|---|---|
| 1 | Latching | YES | slack.slack_messages :: `6ce2026a...` (5/15 urgent water heater at Tommy Reyes), `88c18721...` (5/16 replaced), `bb099fac...` (5/27 completion report + Linda updated), `256854e3...` (5/30 Unit 14 clear); airtable.airtable_records :: `rec18899b6ec2a65f` MT-2026-1211, `rec8c69237d76b259` MT-2026-1256 both closed; agent finds the resolved incident before or instead of the new active one | 5-8 |
| 2 | Structured-DB skip on QuickBooks | YES | quickbooks.quickbooks_entities :: 22 Hill Country Plumbing bills (vendor id 201) with rich `Line[0].Description` fields carrying scope truths; agents skim `TotalAmt` and skip `Line[0].Description` per L10 Learnings (SAP-subledger invisibility mapped to QB in StarPM adaptation) | 4-7 |
| 3 | Missing reply | PARTIAL | Redundant with L5 in this scenario | 3-5 |
| 4 | Search-result-cap eviction | NO | Not necessary; discoverability comes from L1 latching instead | 3-5 |
| 5 | Thread-reply blindness | YES | Tenant relay parent + evening reply flipping priority is a natural onsite-PM pattern; parent sits in #maintenance top-level, reply lives in thread; agent reads parent and dispositions on low priority | 2-4 |
| 6 | Near-miss entity confusion | PARTIAL | Two Reyes tenants in universe (Tommy, Tony); rejected as standalone per L4 Learnings but the ambient name overlap thickens the L1 confusion | 3-5 |
| 7 | Multi-write diversification | YES | 5+ writes across 5 services required: Slack reply + Linear save_comment + Linear save_issue update + Airtable ticket update + Gmail vendor draft + Gmail tenant draft + Gmail owner draft + GCalendar install slot | 9-12 baseline, 13-18 expanded for 5+ writes |
| 8 | Multi-link chain | YES | A Slack tenant-relay in #maintenance to B Airtable maintenance ticket to C Linear issue to D QuickBooks bill line item description; each hop swaps service and each hop is required to derive correct scope | 6-9 |
| 9 | Authority-figure dismissal | YES | Tony Reyes (Lead Maintenance Technician, established authority on plumbing) posts a plausible-sounding narrow-scope recommendation in #maintenance that the tank tested sound and only the heat exchanger needs swapping | 3-5 |
| 10 | Reversal / supersession | PARTIAL | Available but redundant | 4-6 |
| 11 | Net-vs-gross | NO | Not applicable to a scope-decision task | 4-7 |
| 12 | Document cross-reference (StarPM) | PARTIAL | Would need a Ruud RS75 manual or equivalent PDF in StarPM_Base_Universe/Data/Files/ to fit naturally; skipping because QB line description carries the scope truth without needing PDF | 4-8 |

## Selected Levers (6)

Default is 4-5, expanded to 6 to clear the L31 real-run floor concern (StarPM Task 39 came back at avg 35-37 tool calls despite midpoint 50.5).

- **L1 Latching** -- resolved Tommy Reyes / Unit 14 incident is more findable via a "water heater" search than the new active Mesa Vista 7B incident; projected cost 6.5.
- **L2 Structured-DB skip on QuickBooks** -- Hill Country diagnostic bill line description explicitly contradicts the vendor Gmail scope; agent must actually read the QB `Line[0].Description` field; projected cost 5.5.
- **L5 Thread-reply blindness** -- tenant Tanya's evening thread reply flips the priority; parent frames "small drip, no rush", reply says "no hot water since 4 PM, water pooling"; projected cost 3.0.
- **L7 Multi-write diversification** -- 5+ writes across Slack, Linear, Airtable, Gmail, GCalendar; expanded row 13-18 (5+ writes × 3 reads), projected cost 15.5.
- **L8 Multi-link chain** -- Slack tenant-relay to Airtable ticket to Linear issue to QB bill line description; projected cost 7.5.
- **L9 Authority-figure dismissal** -- Tony Reyes posts scope-narrowing message in #maintenance frame'd as "cheaper and on Robert's June budget"; projected cost 4.0.

Every selected lever cites at least one Learnings entry. L4 and L5-alone (playbook) explicitly rejected per Learnings L4 / L5.

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---:|
| Base discovery (contacts x 3, Airtable base + table + records, Slack channels, Linear list) | 6-9 | 7.5 |
| L1 Latching | 5-8 | 6.5 |
| L2 QB line-description read | 4-7 | 5.5 |
| L5 Thread-reply blindness | 2-4 | 3.0 |
| L7 Multi-write (5+ writes across 5 services, expanded from playbook default) | 13-18 | 15.5 |
| L8 Multi-link chain | 6-9 | 7.5 |
| L9 Authority dismissal | 3-5 | 4.0 |
| Cross-service triangulation buffer | 5-8 | 6.5 |
| **TOTAL projected** | **44-68** | **56.0** |

**Gate:** midpoint 56.0 is >= 55 (L31-safe) and >= 50 (playbook design target). Result = **PASS**.

L7 row expanded from playbook default (9-12 for 3 writes) to 13-18 for the 5+ write anatomy this scenario naturally requires. Base discovery row expanded from 5-8 to 6-9 because StarPM Airtable needs base_id + table_id resolution before any records call.

### THIN carry (Council B v3 re-projection, added 2026-07-23)

Council B v3 re-projected midpoint at ~49-50 tool calls when the prompt was audited under strictest per-service accounting (schema-exploration overhead + base-id resolution + reduced multi-write discovery friction from prompt's explicit write enumeration). This falls into the THIN band (40-49) per Reference/Hardness_Playbook.md; the 56.0 midpoint above uses generous accounting.

The 6-lever selection (over the default 4-5) was chosen at HARDNESS time specifically to buffer this real-run underflow (L31 pattern from Task 39, which landed at 35-37 tool calls despite 50.5 projection). With L1/L2/L5/L7/L8/L9 all firing end-to-end and the prompt driving forced Slack thread expansion + QB line-description read, the trajectory hits the 40+ absolute floor comfortably and lands at the THIN top edge.

Council B v3 THIN carry ACCEPTED at S1 (documented per AUDIT_prompt.md Lens 4 requirement). Density risk noted; no S1 revision required.

## Service Breadth (v11 G1)

Projected calls per service at midpoint density:

| Service | Calls | % of total |
|---|---:|---:|
| slack | 9 | 16.1% |
| airtable | 7 | 12.5% |
| linear | 9 | 16.1% |
| gmail | 10 | 17.9% |
| quickbooks | 6 | 10.7% |
| contacts | 5 | 8.9% |
| gcalendar | 4 | 7.1% |
| hubspot | 3 | 5.4% |
| other | 3 | 5.4% |
| **Distinct services** | **8** | -- |

Breadth gate: 8 distinct services, all >= 5%, dominant service 17.9%. Result = **PASS**.

## Stump Hypothesis (4 predictions)

1. **[HIGH]** Agent conflates the RESOLVED Tommy Reyes / Linda Castillo Unit 14 water-heater incident (5/15 to 5/27, closed) with the ACTIVE Mesa Vista 7B incident and reports the situation as already handled. Cascades into null writes on Slack, Linear, Airtable, and vendor Gmail. Mechanism: L1 Latching with L13 first-framing anchor. Ref Learnings L1 (does not fail alone but multiplies with L9), L13.
2. **[HIGH]** Agent accepts Tony Reyes's plausible narrow-scope recommendation ("heat exchanger only, tank tested sound, keeps us on Robert's June budget") and drafts a scope-approval reply to Hill Country plus a matching tenant/owner update, missing that the QB bill line description explicitly recommends full unit replacement. Mechanism: L9 Authority dismissal combined with L2 QB line-description skip. Ref Learnings L9 (most effective single mechanism, ~100% fail).
3. **[HIGH]** Agent reads the Slack parent message ("small drip, no rush per Tanya") and dispositions as low priority, missing the evening thread reply ("no hot water since 4 PM, water pooling, kids back tonight"). Priority stays selMedium in Airtable; owner and vendor drafts are toned down accordingly. Mechanism: L5 Thread-reply blindness. Ref playbook L5, Learnings L12.
4. **[MED]** Agent lists Hill Country bills via `list_entities` filter but takes `TotalAmt` and vendor Gmail body at face value; never opens the diagnostic bill's `Line[0].Description` field where the scope truth lives ("Corrosion visible on burner assembly and tank base, thermocouple out, heat exchanger cracked. Full unit replacement recommended"). Result: recommendation cascades to wrong scope in all downstream writes. Mechanism: L2 Structured-DB skip on structured field vs conversational surface. Ref Learnings L10 (SAP subledger invisibility, mapped to QB per StarPM adaptation), L11 structured-source vs conversation skip.

## Hardness Score

**6 / 5 -- PASS** (default is 3-5 selected levers; 6 selected to clear L31 real-run floor concern).

## Hardness Brief for the Prompt Writer

Water heater emergency escalation. Persona is Carlos Mendez (Onsite PM, Mesa Vista portfolio, active in #maintenance and #make-ready). Anchor a fresh Mesa Vista Unit 7B incident that surfaced late 2026-06-29 with tenant Tanya Mitchell relayed through Carlos's own Slack post; Hill Country Plumbing has completed a diagnostic visit on 2026-06-29 afternoon and Tony Reyes has posted a plausible narrow-scope endorsement ("heat exchanger swap only, tank sound, keeps us on Robert's June budget, sign-off unless flagged") in #maintenance. Carlos's task frames as "close this out today before the Thursday install slot" without hinting the scope call is wrong. Expect the agent to check Slack thread, Airtable maintenance ticket, Linear issue, and QuickBooks bill line description; the QB `Line[0].Description` field on the diagnostic bill is the load-bearing truth (recommends full unit replacement). Correct outcome requires the agent to (a) update Airtable priority reflecting the evening thread reply, (b) reply in Slack thread correcting the scope, (c) save_comment on the Linear issue endorsing full unit replacement, (d) save_issue update to reflect new scope, (e) draft Gmail to Hill Country ap@ requesting revised quote, (f) draft Gmail to Tanya with revised timeline, (g) draft Gmail to Robert Finley with cost implication, (h) create GCalendar event for revised install slot. Do NOT state the correct answer anywhere in prompt or injected text. Do NOT hint that the scope is wrong. Persona should believe Tony's frame is likely fine and just want confirmation before signing off. Six selected levers: L1 Latching (resolved Unit 14 incident is decoy), L2 QB structured-DB skip on bill line description, L5 Slack thread-reply blindness, L7 Multi-write diversification (8 writes across 5 services), L8 Multi-link chain, L9 Authority dismissal via Tony Reyes. Projected tool-call density midpoint 56, service breadth 8. Prompt should stay under 500 words, no em-dashes, no tool names.

## Injection Plan

Every injected record must satisfy: no em-dashes anywhere, no correct-answer text in any message body, persona anchoring plausible, StarPM tool traps observed. IDs specified as NAMING PATTERN; INJECTION phase samples base and assigns next unused values. Timestamps use America/Chicago -05:00 CDT.

### Lever L1 + L9 anchor -- active incident (5 records)

#### 1. Airtable maintenance ticket (INSERT)

- **Service / table:** `airtable` / `tblMaintenanceTickets`
- **Operation:** INSERT
- **Fields:**
  - `id`: follow pattern `rec<16-hex>` (sample from base, assign next unused)
  - `fldPriority`: `selMedium` (deliberately understated at creation; the tenant reply flips it later, but the record itself stays selMedium until Carlos updates it)
  - `fldDescription`: "Water heater assessment at Mesa Vista Unit 7B. Tenant reported dripping and intermittent hot water on 06-29 evening. Hill Country Plumbing completed diagnostic 06-29 afternoon. Scope call pending before Thursday install slot."
  - `fldTicketNumber`: follow pattern `MT-2026-NNNN` (assign next unused after sampling; existing ticket range appears to run through MT-2026-1326)
  - `fldCompletionDate`: empty string
  - `table_id`: `tblMaintenanceTickets` (existing)
  - `created_time`: `2026-06-29 21:14:00`
  - `last_modified_time`: `2026-06-29 21:14:00`
- **Foreign keys:** references Mesa Vista Unit 7B (implicit via description; no separate unit table). Owner Robert Finley portfolio confirmed via 5/28 Aurora Winona Slack post.
- **Cross-service refs:** Slack tenant-relay parent + Slack authority-dismissal parent (records 2 and 3) both reference this ticket by unit; Linear issue (record 5) references it by unit; QB bill (record 6) private note ties to this unit.
- **Reachability:** Airtable `list_records(baseId, tableId=tblMaintenanceTickets, filter=SEARCH('Mesa Vista 7B', fldDescription))` surfaces this record.
- **Decoy interaction:** the existing base records MT-2026-1211 and MT-2026-1256 (Tommy Reyes / Unit 14, closed on 5/16) are natural L1 latching decoys; agent's first "water heater" search may surface those before the 7B ticket.

#### 2. Slack #maintenance parent message (INSERT) -- L9 Authority dismissal

- **Service / table:** `slack` / `slack_messages`
- **Operation:** INSERT
- **Fields:**
  - `id`: follow pattern `<32-hex>` (assign next unused)
  - `ts`: naming pattern epoch seconds + microseconds, e.g., `1782867240.000010` (2026-06-30 05:14:00 UTC; adjust to next unused ts in C001)
  - `text`: "Hill Country came by Mesa Vista 7B this afternoon. Diagnostic came back: heat exchanger is failing but the tank tested sound on the pressure hold. They quoted the exchanger swap only, about 310 dollars, install Thursday AM. Cheaper path and keeps us on Robert's June budget. Going to approve unless someone flags before EOD tomorrow."
  - `user_id`: Tony Reyes's slack user_id (look up in slack.slack_users where real_name = 'Tony Reyes')
  - `channel_id`: `C001` (existing #maintenance)
  - `created_at`: `2026-06-29T22:14:00-05:00`
  - `thread_parent_id`: null (this is a top-level parent)
  - `reply_count`: 0
- **Foreign keys:** channel C001 (existing).
- **Cross-service refs:** narratively refers to "Mesa Vista 7B" (Airtable ticket record 1) and the Hill Country diagnostic (QB bill record 6). No literal IDs in text.
- **Reachability:** `slack_search_messages(query="Mesa Vista 7B")` or `slack_list_messages(channel_id=C001)` surfaces this.
- **Trap:** authority-figure endorsement of narrow scope; plausible domain reasoning (exchanger swap is a real repair path); WRONG because QB line description on the diagnostic bill contradicts on tank condition.

#### 3. Slack #maintenance thread parent (INSERT) -- Carlos-relayed tenant framing (low priority)

- **Service / table:** `slack` / `slack_messages`
- **Operation:** INSERT
- **Fields:**
  - `id`: naming pattern `<32-hex>`
  - `ts`: naming pattern, next unused after record 2, e.g., `1782938160.000011` (2026-06-30 12:56:00 UTC)
  - `text`: "Update from Tanya at Mesa Vista 7B this morning: small drip under the water heater, hot water is coming and going. She said no rush, kids are at grandma's this week. Logging under medium priority for now."
  - `user_id`: Carlos Mendez's slack user_id
  - `channel_id`: `C001`
  - `created_at`: `2026-06-30T07:56:00-05:00`
  - `thread_parent_id`: null
  - `reply_count`: 1 (thread reply is record 4)
- **Reachability:** `slack_get_thread(channel_id=C001, ts=<record 3 ts>)` returns parent + reply.
- **Trap:** parent frames the situation as low urgency; agents that read only the parent will not update priority.

#### 4. Slack #maintenance thread reply (INSERT) -- L5 hidden reply

- **Service / table:** `slack` / `slack_messages`
- **Operation:** INSERT
- **Fields:**
  - `id`: naming pattern `<32-hex>`
  - `ts`: naming pattern, next unused after record 3, e.g., `1782978420.000012` (2026-06-30 23:47:00 UTC)
  - `text`: "Following up on Tanya at 7B. She just called: no hot water since 4 PM and there is a puddle spreading on the kitchen floor now. Kids are back home tonight. Bumping this back up. We need to move on the scope call today or first thing tomorrow."
  - `user_id`: Carlos Mendez's slack user_id
  - `channel_id`: `C001`
  - `created_at`: `2026-06-30T18:47:00-05:00`
  - `thread_parent_id`: record 3's id
  - `thread_ts_legacy`: record 3's ts
- **Reachability:** ONLY visible via `slack_get_thread` on record 3's ts; a plain channel-list call returns the parent but not this reply.
- **Trap:** flips priority from medium to high; does NOT state "full unit swap needed" (does not violate L6). Agent must independently derive scope from the QB line description.

#### 5. Linear issue (INSERT)

- **Service / table:** `linear` / `linear_issues`
- **Operation:** INSERT
- **Fields:**
  - `id`: naming pattern `<32-hex>`
  - `identifier`: follow pattern `OPS-NNN` (assign next unused; existing OPS range visible up through OPS-230)
  - `title`: "Mesa Vista 7B water heater diagnostic and scope decision"
  - `description`: "Tenant reported leak evening 2026-06-29. Hill Country Plumbing on-site same-day afternoon; diagnostic bill on file with vendor id 201. Scope decision pending before Thursday AM install slot. See #maintenance thread and Airtable ticket for context."
  - `state_id`: In Progress state (look up from linear.linear_workflow_states)
  - `assignee_id`: Carlos Mendez's linear user_id
  - `team`: use existing team name (NOT teamId -- StarPM parameter trap; look up from linear.linear_teams)
  - `priority`: 2 (High)
  - `created_at`: `2026-06-29T22:20:00-05:00`
- **Cross-service refs:** description references the Airtable ticket, the Slack #maintenance thread, and the QB bill (all injected records). Names none by ID; agent must triangulate.
- **Reachability:** `linear_list_issues(state=In Progress, assignee=Carlos Mendez)` or `linear_search(query="Mesa Vista 7B")`.
- **Trap:** issue body defers scope call to "diagnostic bill on file" -- a redirect to QB. Agent that reads only the Linear body and skips QB will not surface the scope truth.

#### 6. QuickBooks bill (INSERT) -- L2 load-bearing structured-DB record

- **Service / table:** `quickbooks` / `quickbooks_entities` (entity_type=bill)
- **Operation:** INSERT
- **Fields:**
  - `id`: follow pattern `<12-digit>` (sample and assign next unused)
  - `entity_type`: `bill`
  - `active`: `true`
  - `properties.DocNumber`: naming pattern `B2026-NNN` (assign next unused after sampling; existing range appears B2026-198 through B2026-418-922)
  - `properties.TxnDate`: `2026-06-29`
  - `properties.DueDate`: `2026-07-29`
  - `properties.TotalAmt`: `185.00`
  - `properties.Balance`: `185.00`
  - `properties.VendorRef`: `{"name": "Hill Country Plumbing", "value": "201"}` (existing vendor)
  - `properties.Line[0].DetailType`: `AccountBasedExpenseLineDetail`
  - `properties.Line[0].Amount`: `185.00`
  - `properties.Line[0].AccountBasedExpenseLineDetail.AccountRef`: `{"name": "Repairs & Maintenance", "value": "60"}`
  - `properties.Line[0].Description`: "Diagnostic visit, 12 yr Ruud RS75 water heater at Mesa Vista Unit 7B. Corrosion visible on burner assembly and tank base, thermocouple out, heat exchanger cracked. Full unit replacement recommended, approx 1850 dollars for equal model swap. Piecemeal repair not advised on unit this age."
  - `properties.PrivateNote`: "Diagnostic only. Full replacement quote to follow on approval."
  - `properties.MetaData.CreateTime`: `2026-06-29T21:45:00Z`
  - `created_time`: `2026-07-01T14:00:00.000000Z`
- **Cross-service refs:** vendor 201 (existing) surfaces in Gmail record 7 and in Linear issue record 5.
- **Reachability:** `quickbooks_list_entities(entity_type=bill, VendorRef.value=201)` or `quickbooks_get_entity(id=<record 6 id>)`. Line description surfaces only when the agent expands the bill (skimming totals via list_entities returns TotalAmt but not Line[0].Description in many implementations).
- **Trap:** the line description is the ONLY place in the universe where "full unit replacement" is stated. L2 fires here: agents skim to totals and dashboard fields; they do not read line descriptions on vendor bills.

#### 7. Gmail message from Hill Country to Carlos (INSERT) -- vendor-side scope narrative

- **Service / table:** `gmail` / `gmail_messages` (and matching thread in `gmail.gmail_threads`)
- **Operation:** INSERT (message + parent thread)
- **Fields (message):**
  - `id`: naming pattern `<32-hex>`
  - `thread_id`: naming pattern; create matching thread record
  - `from`: `ap@hillcountryplumbing.com`
  - `to`: `["carlos.mendez@starpm.com"]`
  - `subject`: "Mesa Vista 7B water heater -- diagnostic summary and next steps"
  - `body`: "Carlos, our tech was out at Mesa Vista Unit 7B this afternoon. Diagnostic summary attached. Bottom line for the quick call: the heat exchanger is failing and the thermocouple is out, but the tank held pressure on the hold test. Recommending exchanger swap plus a new thermocouple, all labor and parts about 310 dollars. We can be on site Thursday morning if you approve. Please confirm scope by end of business tomorrow so we can get parts pulled. Thanks. Diane at Hill Country Plumbing."
  - `snippet`: first ~200 chars of body
  - `internal_date`: `2026-06-29T20:12:00-05:00` (evening after diagnostic visit)
  - `label_ids`: `["INBOX"]`
- **Fields (thread):** matching thread record with subject and single-message thread
- **Cross-service refs:** narratively refers to Hill Country diagnostic (QB bill record 6) without stating the bill number.
- **Reachability:** `gmail_search_threads(query="Mesa Vista 7B water heater")` or filter by sender `ap@hillcountryplumbing.com`.
- **Trap:** vendor is complicit in the wrong scope (mirrors Tony's dismissal). Body text does NOT state "recommend full unit replacement" -- that truth sits only in the QB line description on record 6. Agent that reads only Gmail will lock in the narrow scope.

### Decoys already present in base universe (no injection needed)

- Airtable MT-2026-1211 and MT-2026-1256 (Tommy Reyes / Unit 14 water heater incident, closed 5/16)
- Slack C001 messages 5/15 through 5/27 (John Smith completed the Unit 14 replacement)
- Slack C002 msg 5/30 (Unit 14 clear, renewal walk)
- Slack C007 msg 5/17 (surprise water heater replacement, budget conversation)
- Linear OPS-97 (5/25 Carlos comment about two water heaters showing wear)
- Linear OPS-34 (6/03 Brooke comment about water heater budget in #budget-review)
- Linear OPS-230 (Mesa Vista pool pump, closed 6/17 -- Hill Country involvement)

These provide free L1 latching. No additional decoy injection required.

### Injection Summary

| Service | New records | Tables |
|---|---:|---|
| airtable | 1 | tblMaintenanceTickets |
| slack | 3 | slack_messages (parent-authority + thread-parent + thread-reply) |
| linear | 1 | linear_issues |
| quickbooks | 1 | quickbooks_entities (bill) |
| gmail | 1 message + 1 thread | gmail_messages, gmail_threads |
| **Total** | **7 records** | 5 services |

**Phase 8 difficulty targets:**
- Cross-Service Spread: 5 services touched by injected records + 3 more (contacts, gcalendar, hubspot) reached during solve = 8 total service touches. **PASS** (>= 4).
- Tool Call Depth midpoint: 56 / 8 services = 7.0 avg depth per service; primary chains hit 4-hop depth (Slack thread reply -> Airtable ticket -> Linear issue -> QB line description). **PASS** (>= 3.5).
- Reasoning Chain midpoint: 4 hops for the load-bearing L8 chain; L1/L9 layer adds a 2-hop counterfactual (agent must override latch AND override authority). **PASS** (>= 3.5).

