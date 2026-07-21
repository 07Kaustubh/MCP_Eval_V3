# SUBMISSION GATE EVALUATOR — MCP Advanced V4 (StarPM)

> **Purpose:** Catch every defect pattern historically flagged by production auditors before submission. **Hard-gate eval** — any single submission-gate defect is a blocker. Zero tolerance.

---

## The 6 Defect Families

| # | Family | What it catches |
|---|---|---|
| F1 | **Impossible-with-Tools** | Rubrics demanding actions/data the toolset cannot provide |
| F2 | **Persona & Date Mismatch** | Persona attribution errors, system date contradictions, phantom references |
| F3 | **Process Rubric Violations** | Rubrics that credit tool-calling motions instead of measuring outcomes |
| F4 | **Rubric Defects (Broken / Over-Strict)** | Target data missing in universe, or valid alternative paths penalized |
| F5 | **Illegal Tool-Output Dependencies** | Rubrics whose grading requires inspecting tool return values (not visible in transcript) |
| F6 | **QC-Pattern Compliance** | Atomicity, missing criteria, overly broad, destination mismatch, blank fields, exclusion gaps, delegation ambiguity, OE contradictions, strict feasibility/date checks, complexity |

---

## STEP 0 — Mandatory TODO List (Hard Gate)

**Create and track this COMPLETE checklist. Every item is mandatory. Mark each as you go.**

```
- [ ] Phase 0: Load & Pre-Read
  - [ ] 0.1: Read 5_Prompt.txt — extract persona, scenario, all asks, all entity references
  - [ ] 0.2: Read 2_Persona.txt and 1_Business_Function.txt — extract role, authority, department
  - [ ] 0.3: Read 6_Oracle_Events.txt — extract every tool call, parameter, expected value
  - [ ] 0.4: Read 7_Rubrics.json — catalog every rubric: ID, category, criterion, evidence, expected values
  - [ ] 0.5: Read StarPM_Base_Universe/7_Server_Tools_Details.json — build tool inventory
  - [ ] 0.6: Read 3_UniverseDataForThisTask.json (if populated) + StarPM_Base_Universe/Data/ (always) + 4_Changelog.json (if exists) — build complete universe state
  - [ ] 0.7: Read StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md — extract persona role boundaries

- [ ] Phase 1: F1 — Impossible-with-Tools
  - [ ] 1.1: For EACH rubric, verify every referenced tool exists in 7_Server_Tools_Details.json
  - [ ] 1.2: For EACH rubric, verify every referenced parameter exists in that tool's parameter list
  - [ ] 1.3: Verify CRUD coverage — if rubric expects update/delete, does that tool type exist?
  - [ ] 1.4: For EACH search/filter rubric, verify the tool supports the required filter attribute
  - [ ] 1.5: For EACH entity referenced, verify it's discoverable via at least one tool (≤5 call chain)
  - [ ] 1.6: Check aggregation/pagination — any rubric requiring data from >50 unfilterable records or >10 pages?
  - [ ] 1.7: Check for PDF/attachment content referenced without a reader tool
  - [ ] 1.8: Check amount derivation — any rubric amounts from partial/truncated data?
  - [ ] 1.9: Record verdict per rubric: FEASIBLE / IMPOSSIBLE / UNREACHABLE

- [ ] Phase 2: F2 — Persona & Date Mismatch
  - [ ] 2.1: Verify prompt reads as if written by the assigned persona (role, authority, access)
  - [ ] 2.2: Verify persona has authority for ALL rubric-required actions (no role overreach)
  - [ ] 2.3: Check Slack/email attribution — messages match the assigned persona in universe data?
  - [ ] 2.4: Extract effective scenario date; verify ALL rubric events fall within reachable timeline
  - [ ] 2.5: Check for future-data-as-past — rubric expects analysis of events not yet happened?
  - [ ] 2.6: Scan prompt for EVERY entity reference; search universe data — does each exist?
  - [ ] 2.7: Check staff data consistency (is_active vs prompt claims about employment)
  - [ ] 2.8: For EACH email recipient in rubrics, verify they exist in Contacts/Slack AND are active
  - [ ] 2.9: Record verdict: CONSISTENT / MISMATCH / PHANTOM

- [ ] Phase 3: F3 — Process Rubric Violations
  - [ ] 3.1: Identify ALL rubrics categorized as "Process" — list them
  - [ ] 3.2: For EACH, apply three-condition test: (a) tests sequencing? (b) ordering in prompt? (c) not already covered by Outcome?
  - [ ] 3.3: For ALL rubrics: does criterion name a specific tool as success condition? (TOOL_GATE)
  - [ ] 3.4: Does criterion pin specific query params when alternatives work? (QUERY_GATE)
  - [ ] 3.5: Check for always-pass or always-fail gates (tool returns nothing or everything trivially)
  - [ ] 3.6: Check for write-actions categorized as Process (must be Outcome 1.1)
  - [ ] 3.7: Count: Process >40% of total? 3+ items crediting same tool/service?
  - [ ] 3.8: Record verdict: LEGITIMATE_PROCESS / TOOL_GATE / QUERY_GATE / ALWAYS_PASS / ALWAYS_FAIL / WRITE_IN_PROCESS

- [ ] Phase 4: F4 — Rubric Defects (Broken / Over-Strict)
  - [ ] 4.1: Extract EVERY expected value from EVERY rubric ($ amounts, names, IDs, dates, emails, counts)
  - [ ] 4.2: GREP each against universe data — does it exist? For calculations, verify components + math
  - [ ] 4.3: For EACH email address, verify it exists in Contacts/Slack AND maps to the right person
  - [ ] 4.4: For EACH rubric pinning a specific approach: would a valid alternative path be wrongly penalized?
  - [ ] 4.5: Check: equivalent-tool over-spec, email format over-spec, query param over-spec, structured ID lock-in
  - [ ] 4.6: Check role/segregation overreach — persona required to act beyond their authority?
  - [ ] 4.7: For QB/HubSpot creates, verify reference fields (item_ref, company_id) are discoverable
  - [ ] 4.8: Verify rubric facts match CURRENT universe data (not stale from previous snapshot)
  - [ ] 4.9: Record verdict: SOUND / BROKEN / OVER_STRICT

- [ ] Phase 5: F5 — Illegal Tool-Output Dependencies
  - [ ] 5.1: For EACH criterion: can a judge verify it from tool CALL ARGUMENTS alone?
  - [ ] 5.2: Flag: "tool returned success" checks, values only in tool responses, aggregation across responses
  - [ ] 5.3: Distinguish: content in write-action args (email body, message text) IS verifiable ✓
  - [ ] 5.4: Flag: rubric pass/fail based on tool success vs timeout (infrastructure dependency)
  - [ ] 5.5: Record verdict: SELF_CONTAINED / VERIFIABLE_FROM_ARGS / NEEDS_TOOL_OUTPUT

- [ ] Phase 6: F6 — QC-Pattern Compliance (derived from 158-task QC audit)
  - [ ] 6.1: Atomicity — does ANY criterion bundle multiple independently-verifiable items? (FAIL if >1)
  - [ ] 6.2: Forward Coverage — does every explicit prompt deliverable map to at least one Outcome rubric?
  - [ ] 6.3: Under-Strict — for each criterion in isolation: could a wrong answer still pass? (FAIL if plausible)
  - [ ] 6.4: Destination Consistency — do all rubrics target the prompt-specified output destination? (not "final response" when prompt says email/Slack)
  - [ ] 6.5: Blank Fields — does every rubric have non-blank Category, Criterion, Justification, Evidence?
  - [ ] 6.6: Exclusion Coverage — if prompt has filter criteria + universe has decoys, is incorrect inclusion penalized?
  - [ ] 6.7: Delegation Clarity — does prompt mix "I'll [verb]" with agent imperatives? (FAIL = Action Decision Ambiguity)
  - [ ] 6.8: UGT Convergence — if all 6 runs converge, apply deeper scrutiny before failing UGT
  - [ ] 6.9: OE Authority — do OEs contradict prompt or universe data? (OEs are NOT ground truth)
  - [ ] 6.10: Feasibility — can EVERY explicit prompt ask be fulfilled? (no "minor secondary" escape)
  - [ ] 6.11: Date Alignment — is universe data temporally sound with July 1, 2026? (no "still-solvable" escape)

- [ ] Phase 7: Final Verdict
  - [ ] 7.1: Fill in per-rubric findings table + task-level checks table
  - [ ] 7.2: Count failures per family (F1-F6) → produce verdict (PASS only if zero failures across ALL families)
```

---

## Input Files

| File | Purpose |
|---|---|
| `5_Prompt.txt` | Prompt — persona, scenario, asks |
| `6_Oracle_Events.txt` | Expected agent steps — tool calls, parameters |
| `7_Rubrics.json` | All rubric items — primary target of this eval |
| `3_UniverseDataForThisTask.json` | Task-specific universe snapshot (may be empty if CB did not export). **Always also read `StarPM_Base_Universe/Data/` + `4_Changelog.json` as the reliable fallback.** |
| `StarPM_Base_Universe/Data/Files/` | Read-only reference PDFs (contracts, invoices, reports). Read the relevant PDFs if the prompt, rubrics, or OEs reference a specific document. |
| `StarPM_Base_Universe/7_Server_Tools_Details.json` | All MCP tools with parameters and descriptions |
| `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` | Persona role boundaries |
| `Agent_Responses/{Model}/Run{N}_Trajectory.json` | Agent trajectories per model (if available) |

---

## Phase 1: F1 — Impossible-with-Tools

**For EVERY rubric, verify tool existence, parameter existence, CRUD coverage, filter support, and data discoverability.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Phantom tool | Tool in rubric doesn't exist in `7_Server_Tools_Details.json` | Rubric expects `quickbooks_update_bill` — only `create-bill` exists | **IMPOSSIBLE** |
| Phantom parameter | Parameter doesn't exist for that tool | Rubric expects `status` filter on search tool — no such parameter | **IMPOSSIBLE** |
| Missing CRUD | Rubric expects update/delete but only create exists | Prompt says "update the memo on the bill" but no update tool available | **IMPOSSIBLE** |
| Missing filter | Rubric requires searching by attribute the tool doesn't support | No `assigned_to` filter on search tool; rubric requires "tickets assigned to X" | **IMPOSSIBLE** |
| Undiscoverable entity | Entity exists in data but no tool can surface it | `tenant Maria Lopez / unit 8D at Las Palmas` never appears in ANY tool output | **UNREACHABLE** |
| Pagination wall | >50 unfilterable records or >10 pages needed | 1730 records with no status filter — agent can't find specific failed items | **UNREACHABLE** |
| Unreadable content | Rubric references file/attachment content without reader tool | Rubric expects values from PDF but tools only return filenames | **IMPOSSIBLE** |
| Truncated amount | Rubric amount derived from partial/first-page data | Rubric says "total of all invoices" but only first page of 500+ is accessible | **UNREACHABLE** |

---

## Phase 2: F2 — Persona & Date Mismatch

**Verify persona alignment, date consistency, and entity existence.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Persona role mismatch | Prompt actions exceed persona's role/authority | Coordinator doing executive-level strategic planning | **MISMATCH** |
| Wrong attribution | Slack/email messages attributed to wrong persona | Slack posts authored as `user_elena` when persona is Lisa Smith | **MISMATCH** |
| Role overreach | Rubric requires persona to approve/certify beyond their authority | Maintenance tech required to approve a vendor invoice (supervisor's job) | **MISMATCH** |
| Date contradiction | System date vs scenario date inconsistency | `current_date` is Jan 2026 but scenario references March-April events | **MISMATCH** |
| Future-as-past | Rubric expects analysis of events not yet happened per effective date | Prompt pins April 28 but system date varies per rollout (Oct, Sep) | **MISMATCH** |
| Phantom entity | Prompt references email/message/person that doesn't exist in universe | "Grace sent me a meeting notice" — no such email exists | **PHANTOM** |
| Staff inconsistency | `is_active` status contradicts prompt claims | `is_active=true` with `termination_date=null` but prompt says "last day April 4th" | **PHANTOM** |
| Inactive recipient | Rubric sends to someone not in Contacts/Slack or deactivated | Email to person who doesn't exist in contacts or has been deactivated | **PHANTOM** |

---

## Phase 3: F3 — Process Rubric Violations

**For EVERY Process rubric, apply the three-condition test. For ALL rubrics, check for tool/query gates.**

A Process rubric is legitimate ONLY if ALL three hold:
1. Tests **sequencing/ordering** (A before B)
2. Ordering is **explicitly stated in the prompt**
3. **No Outcome rubric** already covers the same ground

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Tool-selection gate | Criterion names a specific tool as the success condition | "Must use `search_bills`" — but `list_records_for_table` returns same data | **TOOL_GATE** |
| Query-construction gate | Criterion pins specific query parameters when alternatives return same data | "Must pass `query='overdue rent'`" — empty query `{}` returns same results | **QUERY_GATE** |
| Always-pass | Tool call always succeeds trivially in this universe | "Must use HubSpot tool" — in empty environment, calling it always passes | **ALWAYS_PASS** |
| Always-fail | Tool returns zero results; rubric always fails | "Must use `linear_list_comments`" — Linear has zero comments in this universe | **ALWAYS_FAIL** |
| Write-in-Process | Write action (send/create/update/post) categorized as Process | `send_email` or `create_issue` pass just for calling the tool, ignoring content | **WRITE_IN_PROCESS** |
| Inflated credit | 3+ rubric items credit calling the same tool/service; or Process >40% of total | 4 process items for CRM/QB/Airtable/Linear in empty env → 0.4-0.7 credit floor | Flag imbalance |

---

## Phase 4: F4 — Rubric Defects (Broken / Over-Strict)

**For EVERY rubric expected value, verify existence. For every pinned approach, check alt-path preservation.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Missing target | Dollar amount, entity, ID, email in rubric doesn't exist in universe | `INV-2026-0047 at $3,200` — no such invoice in QuickBooks | **BROKEN** |
| Bad calculation | Component data missing or math is wrong | Rubric says "total is $42,600" but source records sum to $38,200 | **BROKEN** |
| Empty service | Entire service/table has zero records | ~46 of 50 outcome items reference facts absent from empty environment | **BROKEN** |
| Stale data | Rubric facts don't match current universe snapshot | Rubric says "status: open" but current data shows "status: closed" | **BROKEN** |
| Equivalent tool ignored | Rubric demands Tool A when Tool B returns identical data | `get_crm_objects` returns embedded data that `search_bills` also returns — rubric demands specific endpoint | **OVER_STRICT** |
| Email format locked | Rubric pins one email format when aliases are valid | Rubric requires `robert.calloway@starpm.com` but `r.calloway@` is equally valid | **OVER_STRICT** |
| Query param locked | Rubric demands specific query when default returns same data | Rubric requires `query='overdue rent'` but empty query `{}` returns same results | **OVER_STRICT** |
| ID format locked | Rubric pins structured ID when tool also accepts name | Rubric pins `channel_id: C007` but tool also accepts channel name `#budget-review` | **OVER_STRICT** |
| Role overreach | Rubric requires persona to act beyond their role authority | Maintenance tech required to close/certify an item reserved for supervisor | **OVER_STRICT** |
| Undiscoverable ref | QB/HubSpot create requires reference field no tool can discover | `item_ref` value required but no search/list tool can find it | **BROKEN** |

---

## Phase 5: F5 — Illegal Tool-Output Dependencies

**For EVERY criterion, determine if a judge can verify it from tool call arguments alone.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Success-check | Criterion checks "tool returned success" | "Email sent via `send_email`, tool returned success" — requires inspecting response | **NEEDS_TOOL_OUTPUT** |
| Response-only value | Expected value only appears in tool response, not call args | "Agent identifies $3,200 from QuickBooks data" — $3,200 comes from tool response | **NEEDS_TOOL_OUTPUT** |
| Cross-response aggregation | Criterion requires summing/calculating across multiple tool responses | "Agent correctly sums total outstanding to $X" — sum requires seeing all responses | **NEEDS_TOOL_OUTPUT** |
| Infrastructure dependency | Pass/fail based on tool success vs timeout | "QuickBooks write reflecting real liabilities returned success" — response not visible | **NEEDS_TOOL_OUTPUT** |
| Write-arg content | Content in write args (email body, message text) | "Email includes the specific dollar amounts ($9,200 vs $8,450)" — body IS in call args | VERIFIABLE ✓ |
| Self-contained value | Criterion embeds the expected value directly | "Agent updates status to 'In Progress' for ticket MT-2026-0047" — value embedded | SELF_CONTAINED ✓ |

---

## Phase 6: F6 — QC-Pattern Compliance

> **What this catches:** The 11 most common QC failure patterns from 158 audited tasks (30 fails). These are defects that escaped the F1-F5 production audit checks but were caught by QC. This family closes that gap.

| # | Check | What to look for | Verdict if found |
|---|---|---|---|
| 6.1 | **Atomicity** | Criterion bundles 2+ independently-verifiable items (ML confirmed: "split completely") | **NOT_ATOMIC** |
| 6.2 | **Forward Coverage** | Explicit prompt deliverable has ZERO Outcome rubric coverage | **MISSING_CRITERIA** |
| 6.3 | **Under-Strict** | In isolation: could a factually wrong answer still pass THIS criterion? (never argue sibling covers it) | **OVERLY_BROAD** |
| 6.4 | **Destination Consistency** | Prompt says "email to X" but rubric checks "final response" — wrong artifact | **WRONG_DESTINATION** |
| 6.5 | **Blank Fields** | Any rubric has blank Category, Criterion, Justification, or Evidence | **BLANK_FIELD** |
| 6.6 | **Exclusion Coverage** | Filter criteria + decoy records exist, but no rubric penalizes incorrect inclusion | **MISSING_EXCLUSION** |
| 6.7 | **Delegation Clarity** | Prompt mixes "I'll [verb]" with agent imperatives — ambiguous who acts | **DELEGATION_AMBIGUITY** |
| 6.8 | **UGT Convergence** | All 6 runs converge but UGT is being failed — apply deeper scrutiny (convergence is circumstantial, not dispositive, but demands justification) | Investigation signal |
| 6.9 | **OE Authority** | OE contradicts prompt or universe data — OEs are CB internal docs, NOT ground truth | **OE_CONTRADICTION** |
| 6.10 | **Feasibility (strict)** | ANY explicit prompt ask cannot be fulfilled with available tools + data — no "minor secondary" escape | **INFEASIBLE** |
| 6.11 | **Date Alignment (strict)** | Universe data misaligned with July 1, 2026 AND creates stale references or ambiguity — no "still-solvable" escape | **DATE_MISALIGNED** |

---

## Phase 7: Final Verdict

**Per-rubric aggregate table:**

| Rubric # | Criterion | F1 | F2 | F3 | F4 | F5 | F6 | Overall |
|---|---|---|---|---|---|---|---|---|
| 1 | ... | FEASIBLE | CONSISTENT | N/A | SOUND | SELF_CONTAINED | PASS | **PASS** |
| 2 | ... | IMPOSSIBLE | — | — | BROKEN | — | NOT_ATOMIC | **FAIL** |

**Task-level summary:**

| Check | Result | Count |
|---|---|---|
| F1: Any IMPOSSIBLE / UNREACHABLE rubrics? | PASS/FAIL | |
| F2: Any PHANTOM entities or MISMATCH? | PASS/FAIL | |
| F3: Any TOOL_GATE / QUERY_GATE / ALWAYS_PASS / ALWAYS_FAIL? | PASS/FAIL | |
| F4: Any BROKEN / OVER_STRICT? | PASS/FAIL | |
| F5: Any NEEDS_TOOL_OUTPUT? | PASS/FAIL | |
| F6: Any NOT_ATOMIC criteria? | PASS/FAIL | |
| F6: Any MISSING_CRITERIA (forward coverage)? | PASS/FAIL | |
| F6: Any OVERLY_BROAD criteria? | PASS/FAIL | |
| F6: Any WRONG_DESTINATION rubrics? | PASS/FAIL | |
| F6: Any BLANK_FIELD rubrics? | PASS/FAIL | |
| F6: Any MISSING_EXCLUSION coverage? | PASS/FAIL | |
| F6: Any DELEGATION_AMBIGUITY in prompt? | PASS/FAIL | |
| F6: Any INFEASIBLE prompt asks (strict)? | PASS/FAIL | |
| F6: Any DATE_MISALIGNED issues (strict)? | PASS/FAIL | |
| F6: Any OE_CONTRADICTION? | PASS/FAIL | |
| Process > 40%? | PASS/FAIL | |

```
┌─────────────────────────────────────────────┐
│           SUBMISSION GATE VERDICT           │
├─────────────────────────────────────────────┤
│ Total rubrics evaluated:  ___               │
│ F1 (Impossible-with-Tools):   ___           │
│ F2 (Persona & Date):         ___            │
│ F3 (Process Violations):     ___            │
│ F4 (Broken / Over-Strict):   ___            │
│ F5 (Tool-Output Deps):       ___            │
│ F6 (QC-Pattern Compliance):  ___            │
│ TOTAL FAILURES:              ___            │
│                                             │
│ VERDICT:  PASS / FAIL                       │
│ PASS = zero failures across ALL 6 families. │
│ Any single defect = FAIL.                   │
└─────────────────────────────────────────────┘
```

---

## Quick Reference: 32 Canonical Submission Gate Patterns

| # | Pattern | Family | Auto-flag |
|---|---|---|---|
| 1 | Rubric expects `update_X` tool but only `create_X` exists | F1 | IMPOSSIBLE |
| 2 | Entity ID appears in zero tool outputs | F1 | IMPOSSIBLE |
| 3 | Tool lacks filter for attribute rubric searches by | F1 | IMPOSSIBLE |
| 4 | 500+ records with no usable filter to narrow | F1 | UNREACHABLE |
| 5 | Prompt references email/message/meeting that doesn't exist | F2 | PHANTOM |
| 6 | System date contradicts prompt scenario timeframe | F2 | MISMATCH |
| 7 | Persona attributed wrong in Slack/email vs assigned | F2 | MISMATCH |
| 8 | `is_active=true` but prompt says person has left | F2 | MISMATCH |
| 9 | "Must use `specific_tool`" when equivalent returns same data | F3 | TOOL_GATE |
| 10 | Tool call always passes in empty environment | F3 | ALWAYS_PASS |
| 11 | Tool returns zero results; rubric always fails | F3 | ALWAYS_FAIL |
| 12 | Write action categorized as Process | F3 | WRITE_IN_PROCESS |
| 13 | Specific query params required when default returns same data | F3/F4 | QUERY_GATE |
| 14 | Dollar amount / entity / ID doesn't exist in universe | F4 | BROKEN |
| 15 | Email address doesn't exist in contacts | F4 | BROKEN |
| 16 | Rubric demands one tool when another returns equivalent data | F4 | OVER_STRICT |
| 17 | Rubric pins ID format when tool also accepts name | F4 | OVER_STRICT |
| 18 | Persona required to act beyond role authority | F4 | OVER_STRICT |
| 19 | Criterion checks "tool returned success" | F5 | NEEDS_TOOL_OUTPUT |
| 20 | Expected value only in tool response, not call args | F5 | NEEDS_TOOL_OUTPUT |
| 21 | Aggregation/calculation across multiple tool responses | F5 | NEEDS_TOOL_OUTPUT |
| 22 | Criterion bundles 2+ independently-verifiable items (must split) | F6 | NOT_ATOMIC |
| 23 | Explicit prompt deliverable has zero Outcome rubric coverage | F6 | MISSING_CRITERIA |
| 24 | Wrong answer could plausibly pass this criterion (per-criterion only) | F6 | OVERLY_BROAD |
| 25 | Rubric checks "final response" but prompt specifies email/Slack/record | F6 | WRONG_DESTINATION |
| 26 | Rubric has blank Category, Criterion, Justification, or Evidence | F6 | BLANK_FIELD |
| 27 | Filter criteria + decoy records exist but no exclusion rubric | F6 | MISSING_EXCLUSION |
| 28 | Prompt mixes "I'll [verb]" with agent imperatives | F6 | DELEGATION_AMBIGUITY |
| 29 | OE contradicts prompt or universe data (OEs are NOT ground truth) | F6 | OE_CONTRADICTION |
| 30 | Explicit prompt ask can't be fulfilled — no "minor secondary" escape | F6 | INFEASIBLE |
| 31 | Universe data misaligned with July 1, 2026 — no "still-solvable" escape | F6 | DATE_MISALIGNED |
| 32 | Task solvable in <15 tool calls / single-service / investigate+one email | F6 | TOO_EASY |

---

## Key Rules

1. **One failure = task FAIL.** No "minor" CAI defect exists — every pattern above was a real production escape.
2. **Do not rationalize away a match.** audit data shows these patterns are wrong >90% of the time.
3. **Process rubrics get triple scrutiny.** 61% of flagged Process rubrics needed fixing. Default: wrong until proven right.
4. **Check evidence/justification fields too.** Tool names in evidence must exist. Expected values must match universe data.
