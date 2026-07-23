# Council A — Grounding and Convention
## OE Phase Evaluation
**Task:** 40_6a61a86a31b9c973b2021ba5 (Mesa Vista Unit 7B water heater scope decision)  
**Date:** 2026-07-23  
**Persona:** Carlos Mendez, Onsite Property Manager  
**Universe:** StarPM (Star Property Management, V4)  

---

## VERDICT: BLOCK

**Critical blocker (A1 Grounding):** Slack message timestamps specified in OE steps 3-4 must be coordinated with the INJECTION phase. The OE hardcodes timestamp values (1782789240.000301, 1782824160.000302, 1782863220.000303) that differ from the example pattern in Hardness_Plan.md. Agent tool calls using these exact ts values will FAIL if injected messages have different timestamps. Coordination required before proceeding to S2 validation.

**Critical loader (A11 End-to-End Solvability):** QB bill Line[0].Description field must contain the exact wording specified in OE 10. This is the L2 load-bearing lever for hardness (scope truth). Verify injection plan will produce this text verbatim.

**Tool name verification required (A2 Convention):** Tool names "slack_search_public" (OE 3) and "slack_read_thread" (OE 4) are not visible in partial 7_Server_Tools_Details.json catalog retrieved. Slack tools need verification against StarPM tool inventory.

---

## A1 — Grounding (Concrete Claims)

### CRITICAL ISSUE: Slack Message Timestamps

**Finding:** OE steps 3, 4, and 5 specify Slack message timestamps that must match exactly for agent tool calls to succeed.

| OE Step | Specified ts | Field | Context |
|---------|---|---|---|
| OE 3 | 1782789240.000301 | Tony Reyes authority parent in C001 | Authority dismissal L9 lever |
| OE 4 | 1782824160.000302 | Carlos tenant-relay parent in C001 | Thread-reply blindness L5 lever parent |
| OE 4 | 1782863220.000303 | Carlos escalation reply (thread child) | Thread-reply blindness L5 lever reply |

**Problem:** Hardness_Plan.md injection section (Record 2-4) specifies these as "naming pattern" values with examples like:
- Record 2 (Tony's parent): ts example `1782867240.000010` 
- Record 3 (Carlos tenant-relay): ts example `1782938160.000011`
- Record 4 (escalation reply): ts example `1782978420.000012`

These **DO NOT MATCH** the OE-specified values.

**Impact:** 
- OE 4 specifies `slack_read_thread(channel_id "C001", message_ts "1782824160.000302")`. If injected message has ts=1782938160.000011, this tool call fails with "message not found."
- Agent cannot execute OE 4-5 steps without the exact ts value.

**Required Fix:** Either:
1. INJECTION phase must produce messages with the EXACT ts values specified in OE (1782789240.000301, etc.), OR
2. OE steps 3-4 must be revised to use placeholder language ("Read the tenant-relay thread using slack_read_thread") without hardcoding ts values, deferring discovery of the actual ts to agent execution.

**A1 Grounding Verdict:** **BLOCKED** — Timestamp synchronization required.

---

### Verified Claims (Universe Alignment)

**From task context (HEAD statement):** The task expects these injected records:
- Airtable ticket: rec92f4a1c8e17bd3, ticket MT-2026-1327 ✓
- Linear issue: OPS-231 ✓
- QB bill: id 195836274018, DocNumber B2026-211, TotalAmt 185.00 ✓
- Gmail: from ap@hillcountryplumbing.com ✓
- Contacts: tanya.mitchell@gmail.com, robert.finley@gmail.com ✓

**OE claims verified against Fact_Ledger:**
- Tanya Mitchell email: tanya.mitchell@gmail.com ✓ (line 238)
- Robert Finley email: robert.finley@gmail.com ✓ (line 231)
- Carlos Mendez email: carlos.mendez@starpm.com ✓ (line 134)
- ap@hillcountryplumbing.com ✓ (line 117)
- Slack channel C001 ✓ (line 1460, slack_channel IDs list)
- Amount $185.00 ✓ (in Fact_Ledger amounts list, line 319)
- Amount ~$1850 (approx cost) ✓ (line 561, in amounts list)
- Amount $310 (quoted path) ✓ (line 360, in amounts list)

**Claims requiring Universe_Split verification:**
- Airtable record rec92f4a1c8e17bd3 exists in tblMaintenanceTickets
- Airtable fldPriority options include selLow/selMedium/selHigh
- Linear issue OPS-231 exists with team "OPS", state "In Progress", assignee Carlos Mendez
- Linear user_id user_d6c1beb9cf67594dae2f5de4529674f1 is Carlos Mendez
- QB bill 195836274018 exists with DocNumber B2026-211 and exact Line[0].Description wording (see L2 loader below)
- Gmail thread_id d1e2f3a4b5c6789a exists with message from ap@hillcountryplumbing.com sent 2026-06-29

**Status:** Cannot fully verify without access to Universe_Split files. Assumption: injected records will produce these exact values.

---

### CRITICAL LOADER: QB Bill Line Description (L2 Lever)

**OE 10 specifies exact content:**
```
"Diagnostic visit, 12 yr Ruud RS75 water heater at Mesa Vista Unit 7B. Corrosion visible on burner assembly 
and tank base, thermocouple out, heat exchanger cracked. Full unit replacement recommended, approx 1850 
dollars for equal model swap. Piecemeal repair not advised on unit this age."
```

**This wording is the load-bearing truth for the entire OE chain.** Every downstream write (OE 12-18) depends on this fact:
- Full unit replacement (not just heat exchanger swap)
- Approx $1850 cost (not $310)
- Piecemeal repair unsound on 12-year unit

**Hardness_Plan.md Injection (Record 6)** specifies the exact same text for `properties.Line[0].Description`. **Match verified ✓**

**Dependency:** If injected QB bill lacks this exact wording, OE 10 will surface a different scope, cascading wrong values into OE 12-18 writes. This is the intended L2 hardness lever (structured-DB skip trap).

**Verification required:** Before OE PASS, confirm injection produces QB bill with exact Line[0].Description text matching OE 10 word-for-word.

---

## A2 — Convention (Format & Tool Names)

### Format Compliance

| Rule | OE Compliance | Status |
|---|---|---|
| Numbered prose (OE 1 - OE 19) | ✓ All 19 steps numbered sequentially | PASS |
| Free-form text (not JSON) | ✓ Narrative prose throughout | PASS |
| No em-dashes / en-dashes | ✓ Scanned entire OE, none found | PASS |
| Opening phrase patterns | ✓ Matches OE_Convention_Inventory patterns: "Look up...", "Search...", "Read...", "Locate...", "Update..." | PASS |
| Tool names named in steps | ✓ All tools named explicitly | PASS |
| "Conclude:" clause usage | ✓ OE 4 uses "Conclude: the tenant situation has escalated..." for critical L5 reasoning | PASS |
| Real parameter names | ✓ StarPM parameter traps applied (see below) | PASS with verification needed |

### Tool Name Verification Required

| Tool Name | OE Step | StarPM Catalog Status | Issue |
|---|---|---|---|
| `contacts_search_contacts` | 1 | ✓ Visible in partial catalog (line 545) | VERIFIED |
| `search_crm_objects` | 2 | ✓ Visible in partial catalog (line 1131) | VERIFIED |
| `slack_search_public` | 3 | ❓ NOT visible in partial 7_Server_Tools_Details.json | **NEEDS VERIFICATION** |
| `slack_read_thread` | 4 | ❓ NOT visible in partial catalog | **NEEDS VERIFICATION** (may be `get_thread` for Slack) |
| `search_threads` | 5 | ✓ Visible in Gmail tools (line 881) | VERIFIED |
| `get_thread` | 5 | ✓ Visible in Gmail tools (line 903) | VERIFIED |
| `list_bases` | 6 | ✓ Visible in Airtable tools (line 31) | VERIFIED |
| `list_tables_for_base` | 6 | ✓ Visible in Airtable tools (line 55) | VERIFIED |
| `search_records` | 7 | ✓ Visible in Airtable tools (line 117) | VERIFIED |
| `list_issues` | 8 | ✓ Visible in Linear tools (line 1359) | VERIFIED |
| `get_issue` | 8 | ✓ Visible in Linear tools (line 1429) | VERIFIED |
| `search_bills` | 9 | ❓ NOT visible in partial QB catalog (lines 2430-3319) | **NEEDS VERIFICATION** |
| `get-bill` | 10 | ✓ Visible in QB tools (line 3020) | VERIFIED |
| `update_records_for_table` | 12 | ✓ Visible in Airtable tools (line 165) | VERIFIED |
| `save_issue` | 13 | ✓ Visible in Linear tools (line 1451) | VERIFIED |
| `save_comment` | 14 | ✓ Visible in Linear tools (line 1789) | VERIFIED |
| `slack_send_message` | 15 | ❓ NOT visible in partial catalog | **NEEDS VERIFICATION** (CRITICAL: ensure this is the send tool, not draft) |
| `create_draft` | 16-18 | ✓ Visible in Gmail tools (line 935) | VERIFIED |
| `create_event` | 19 | ✓ Visible in GCalendar tools (line 657) | VERIFIED |

**Action Required:** Verify Slack tools (slack_search_public, slack_read_thread, slack_send_message) and QB search tool (search_bills) exist in full 7_Server_Tools_Details.json catalog. If tool names differ, update OE.

### StarPM Parameter Trap Compliance

| Tool | Parameter | OE Usage | Correct? | Status |
|---|---|---|---|---|
| `slack_send_message` | message param | OE 15: `message covering...` | ✓ Uses "message", not "payload"/"text" | VERIFIED |
| `slack_send_message` | NOT draft | OE 15: "Do NOT use slack_send_message_draft" | ✓ Explicit warning present | VERIFIED |
| `create_draft` | body param | OE 16-18: `body covering...` | ✓ Uses "body" | VERIFIED |
| `save_issue` | team param | OE 13: `team "OPS"` | ✓ Uses "team", not "teamId" | VERIFIED |
| `save_comment` | issueId param | OE 14: `issueId "OPS-231"` | ✓ Correct parameter name | VERIFIED |
| `update_records_for_table` | camelCase | OE 12: `baseId`, `tableId`, `records` | ✓ All camelCase | VERIFIED |
| `get-bill` | hyphen | OE 10: `get-bill` | ✓ Uses hyphen, not underscore | VERIFIED |

**A2 Verdict:** CONDITIONAL PASS — Format and parameter traps correct, but 4 tool names require verification against full catalog.

---

## A3 — Narrative State Consistency

### Timeline Alignment

| Date | Event | OE Step | Consistency |
|---|---|---|---|
| 2026-06-29 | Hill Country diagnostic visit (Monday) | OE 5, 9 | ✓ Monday, matches prompt backstory |
| 2026-06-29 | Tony posts authority endorsement | OE 3 | ✓ "Monday night" per prompt context |
| 2026-06-30 | Carlos posts tenant-relay parent (Tuesday) | OE 4 | ✓ "Last night Tanya called" per prompt (implied 6-30) |
| 2026-06-30 | Tenant escalation reply (evening) | OE 4 | ✓ "no hot water since 4 PM" escalation timing |
| 2026-07-01 | Task today (Wednesday) | Task context | ✓ Fact_Ledger dates include 2026-07-01 |
| 2026-07-02 | Thursday install slot | OE 19 | ✓ "startTime 2026-07-02T08:00:00-05:00" |

**A3 Verdict:** PASS — Timeline internally consistent.

### Persona Standing

Carlos Mendez (Onsite Property Manager) can:
- Update Airtable maintenance tickets ✓ (operational responsibility)
- Update Linear operations issues ✓ (peer-level tracking)
- Draft vendor communications ✓ (vendor management authority)
- Draft tenant communications ✓ (property manager interface)
- Draft owner communications ✓ (escalation authority)
- Create calendar events for himself ✓ (scheduling own work)

**A6 Verdict:** PASS — All write actions within persona scope.

---

## A4 — Action-vs-Universe-Prescription

### OE Scope Decisions vs Universe Data

**Load-bearing prescription:** QB bill Line[0].Description (OE 10) recommends "Full unit replacement" at "approx 1850 dollars", NOT the narrow "heat exchanger swap only" at "$310" that Tony and Diane advocate.

**OE write cascade (OE 12-18) follows the QB prescription:**
- OE 12 Airtable update: "corrected scope" covering "full water heater replacement"
- OE 13 Linear update: "corrected scope is a full water heater unit replacement at approximately 1850 dollars"
- OE 14 Linear comment: "diagnostic recommends full unit replacement"
- OE 15 Slack reply: "diagnostic bill points to full unit replacement rather than the exchanger-only path"
- OE 16 vendor draft: "correct scope is a full water heater unit replacement rather than the exchanger and thermocouple swap"
- OE 18 owner draft: "initial 310 dollar exchanger-swap quote has moved to a full water heater unit replacement at approximately 1850 dollars"

**Alignment:** Every downstream write action is grounded in the L2 lever (QB line description truth). No divergence detected. ✓

**A4 Verdict:** PASS — All writes trace back to universe data (QB bill) as source of truth.

---

## A7 — Clarity & Specificity (Holistic)

### First-Time Reader Walk-Through

1. **OE 1-2 (Look up people):** Clear. Specify contacts to find email addresses for OE 17-18.
2. **OE 3-5 (Search for discovery):** Clear. Explicit "expected surface" and "expected discovery" language. Search queries named (e.g., "Mesa Vista 7B", "Hill Country diagnostic").
3. **OE 6-8 (Navigate to records):** Clear. Base → table → record resolution steps explicit.
4. **OE 9-11 (Find QB bill and confirm user):** Clear. Bill search and line-description read detailed.
5. **OE 12-19 (Write actions):** Clear. Every write specifies tool, key parameters, and field values.

### Ambiguity Scan

**Potential ambiguity: OE 6 "list_bases or search_bases"**
- Resolved: Both tools exist; either works. OE 6 allows agent flexibility. No blocker.

**Potential ambiguity: OE 12 "fldDescription revised to reflect the escalation"**
- Resolved: OE 12 specifies "revised description should... carry the corrected scope so the field team sees the right call." Sufficient guidance for agent to synthesize updated text.

**Potential ambiguity: OE 16-18 email body content**
- Resolved: OE 16-18 specify the CONTENT to include (scope, cost, reason) but allow agent to draft tenant-appropriate and owner-appropriate framing. Sufficient specificity.

**A7 Verdict:** PASS — No material clarity gaps. Agent can execute OE chain without ambiguity (pending tool name verification and timestamp coordination).

---

## A10 — Business Function Match

**Task:** Water heater emergency escalation at residential property (Mesa Vista Unit 7B)  
**Hardness_Plan designation:** Property Operations (Cat 1)  
**OE activities:**
- Maintenance ticket update (Property Operations)
- Vendor scope confirmation (Property Operations)
- Tenant communication (Property Operations)
- Owner cost notification (Property Operations)
- Calendar scheduling for onsite work (Property Operations)

**A10 Verdict:** PASS — Business function correctly assigned.

---

## A11 — End-to-End Solvability

### Critical Path Chain

```
OE 1-2 (Contacts)
  ↓
OE 3-5 (Slack + Gmail discovery)
  ↓
OE 6-11 (Airtable + Linear + QB discovery + Carlos user_id)
  ↓
OE 12 (Update Airtable with priority + corrected description)
  ↓
OE 13-14 (Update + comment on Linear)
  ↓
OE 15 (Post rationale to Slack thread)
  ↓
OE 16-18 (Draft 3 emails: vendor + tenant + owner)
  ↓
OE 19 (Create Thursday install calendar event)
```

### Per-Step Reachability

| Step | Tool Call | Reachability | Blocker? |
|---|---|---|---|
| 1 | contacts_search_contacts("Tanya Mitchell") | ✓ Tanya in Fact_Ledger emails + Persona briefs | NO |
| 2 | search_crm_objects("Robert Finley") | ✓ Robert in Fact_Ledger emails | NO |
| 3 | slack_search_public(query "Mesa Vista 7B") in C001 | ✓ C001 exists; Tony's parent expected ts TBD | **YES** (timestamp coordination) |
| 4 | slack_read_thread(C001, ts=1782824160.000302) | Depends on OE 3; exact ts required | **YES** (timestamp coordination) |
| 5 | search_threads(query "Hill Country diagnostic") | ✓ Diane's email from ap@hillcountryplumbing.com | NO |
| 6 | list_bases() or search_bases("Property Operations") | ✓ appPropertyOps expected to exist | NO |
| 7 | search_records(appPropertyOps, tblMaintenanceTickets, "Mesa Vista 7B") | ✓ rec92f4a1c8e17bd3 expected to exist | NO |
| 8 | list_issues(query "Mesa Vista 7B") | ✓ OPS-231 expected to exist | NO |
| 9 | search_bills(query "Hill Country") or filter VendorRef=201 | Requires working search tool | **NEEDS VERIFICATION** (tool name) |
| 10 | get-bill(id 195836274018) & read Line[0].Description | ✓ Bill expected to exist; description must match OE 10 word-for-word | **YES** (content verification) |
| 11 | list_issues(assignee=Carlos) to confirm user_id | ✓ Expected to resolve Carlos's Linear user_id | NO |
| 12-19 | Write actions (Airtable, Linear x2, Slack, Gmail x3, Calendar) | All depend on OE 1-11 discovery | Depends on 1-11 |

**Critical blockers for end-to-end solvability:**
1. **Timestamp coordination (OE 3-4):** Slack message ts must match injected values or tool calls fail.
2. **QB bill content verification (OE 10):** Line[0].Description must contain exact scope truth or cascade fails.
3. **QB search tool verification (OE 9):** Tool "search_bills" must exist in StarPM catalog.

**A11 Verdict:** CONDITIONAL PASS — Solvable pending resolution of timestamp coordination and content verification. Tool name verification does not block execution (agent can search via list_entities or other alternatives).

---

## Summary of Issues by Severity

### BLOCKER (A1)

**Issue:** Slack message timestamps in OE steps 3-4 must be coordinated with INJECTION phase.

**Fix Required:** One of:
- (Option A) INJECTION phase produces messages with exact ts values: 1782789240.000301, 1782824160.000302, 1782863220.000303
- (Option B) OE steps 3-4 revised to use placeholder language, deferring ts discovery to agent execution

**Citation:** A1 Grounding, "CRITICAL ISSUE: Slack Message Timestamps"

---

### CRITICAL LOADER (A11)

**Issue:** QB bill Line[0].Description wording must match OE 10 exactly. This is the L2 lever for hardness.

**Fix Required:** Verify injection will produce QB bill with exact text: "Diagnostic visit, 12 yr Ruud RS75 water heater at Mesa Vista Unit 7B. Corrosion visible on burner assembly and tank base, thermocouple out, heat exchanger cracked. Full unit replacement recommended, approx 1850 dollars for equal model swap. Piecemeal repair not advised on unit this age."

**Citation:** A11 End-to-End Solvability, "Per-Step Reachability"

---

### NEEDS VERIFICATION (A2)

**Issue:** Four tool names not visible in partial 7_Server_Tools_Details.json catalog:
1. `slack_search_public` (OE 3)
2. `slack_read_thread` (OE 4)
3. `slack_send_message` (OE 15)
4. `search_bills` (OE 9)

**Fix Required:** Verify these tools exist in full StarPM catalog. If tool names differ, update OE accordingly.

**Citation:** A2 Convention, "Tool Name Verification Required"

---

## Final Assessment

| Dimension | Status | Notes |
|---|---|---|
| **A1 Grounding** | BLOCKED | Slack timestamp coordination required |
| **A2 Convention** | CONDITIONAL PASS | 4 tool names require verification |
| **A3 State Consistency** | PASS | Timeline and persona alignment verified |
| **A4 Action-vs-Universe** | PASS | Writes trace to QB bill truth |
| **A6 Persona Scope** | PASS | Carlos can execute all writes |
| **A7 Clarity** | PASS | No material ambiguities |
| **A10 Business Function** | PASS | Property Operations correct |
| **A11 Solvability** | CONDITIONAL PASS | Depends on blockers above |

---

## Recommendation

**Do NOT pass OE to S2 validation.** Resolve the blocker (timestamp coordination) and load-bearing issue (QB content verification) first. Tool name verification can proceed in parallel and be resolved before or during S2 if alternative tools exist.

**Path forward:**
1. INJECTION phase confirms exact timestamp values and QB bill content
2. OE revised if timestamps differ, OR timestamp synchronization verified
3. QB bill Line[0].Description verified to match OE 10
4. Tool names verified in full catalog
5. Re-submit OE to Council A for PASS gate

