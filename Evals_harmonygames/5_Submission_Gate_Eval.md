# SUBMISSION GATE EVALUATOR — Original Conference (HarmonyGames)

> **Purpose:** Catch every defect pattern historically flagged by production auditors before submission. Hard-gate defects prevent submission. Moderate **Vague Exemplar Language** findings use the Overall Rubric Quality thresholds rather than auto-failing individually.

Each stored rubric object in `7_Rubrics.json` has exactly `title`, `category`, `justification`, and `evidence`. `title` contains the complete conceptual criterion text; there is no stored `criterion` key. `category` must be exactly `Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, or `Process`.

**Persona ACL is active and implemented.** `Docs/15_Persona_ACL.md` is authoritative for access semantics, and `HarmonyGames_Base_Universe/Persona_ACL_Roster.json` is authoritative for exact taxonomy persona records. Apply Persona ACL only to reads in Gmail, Slack, GCal, and Contacts; do not infer write denial or ACL for other services.

**Persona artifact hard gate:** `2_Persona.txt` must contain Persona Key,
Persona Email, Name, Role, and Department values that all exactly match one
entry in `HarmonyGames_Base_Universe/Persona_ACL_Roster.json`. A missing field,
mixed entry, inferred email, or value mismatch prevents submission.

---

## The 6 Defect Families

| # | Family | What it catches |
|---|---|---|
| F1 | **Impossible-with-Tools** | Rubrics demanding actions/data the toolset cannot provide |
| F2 | **Persona & Date Mismatch** | Persona attribution errors, system date contradictions, phantom references |
| F3 | **Process Rubric Violations** | Rubrics that credit tool-calling motions instead of measuring outcomes |
| F4 | **Rubric Defects (Broken / Over-Strict)** | Target data missing in universe, required precision unavailable through tools, hidden derivations, or valid alternative paths penalized |
| F5 | **Illegal Tool-Output Dependencies** | Rubrics whose grading requires inspecting tool return values (not visible in transcript) |
| F6 | **QC-Pattern Compliance** | Atomicity, requirement-level coverage, affirmative criterion wording, overly broad, prompt-specificity ceiling, duplicate rubrics, vague exemplar language, destination mismatch, blank fields, exclusion gaps, delegation ambiguity, OE contradictions, strict feasibility/date checks, complexity |

---

## STEP 0 — Mandatory TODO List (Hard Gate)

**Create and track this COMPLETE checklist. Every item is mandatory. Mark each as you go.**

```
- [ ] Phase 0: Load & Pre-Read
  - [ ] 0.1: Read 5_Prompt.txt — extract persona, scenario, all asks, all entity references
  - [ ] 0.2: Read 2_Persona.txt and 1_Business_Function.txt — require Persona Key, Persona Email, Name, Role, and Department to match one roster entry exactly; extract role, authority, and department
  - [ ] 0.3: Read 6_Oracle_Events.txt — extract every tool call, parameter, expected value
  - [ ] 0.4: Read 7_Rubrics.json — catalog every rubric: ID, `title`, `category`, `justification`, `evidence`, expected values
  - [ ] 0.5: Read every HarmonyGames_Base_Universe/Tool_Access/*.json catalog (all 13 services) — build the authoritative tool, parameter, and capability inventory
  - [ ] 0.6: Read 3_UniverseDataForThisTask.json (if populated) + HarmonyGames_Base_Universe/Services_Data/ (always) + 4_Changelog.json (if exists) — build complete universe state
  - [ ] 0.7: Read HarmonyGames_Base_Universe/2_Persona_Briefs.md — extract persona role boundaries
  - [ ] 0.8: If any run uses 500–1,000 tool calls, read Docs/14_Long_Horizon_Task_Guidelines.md and QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/ (the pass baseline), then run the long-horizon legitimacy checks
  - [ ] 0.9: If rubrics use record-level spot checks, determine whether the large audit-table exception applies; do not impose a minimum spot-check count
  - [ ] 0.10: Read Docs/15_Persona_ACL.md + HarmonyGames_Base_Universe/Persona_ACL_Roster.json; after the five-field hard gate passes, bind the required taxonomy persona and verify Agent Runner/Run Verifier parity

- [ ] Phase 1: F1 — Impossible-with-Tools
  - [ ] 1.1: For EACH rubric, verify every referenced tool exists exactly in HarmonyGames_Base_Universe/Tool_Access/*.json
  - [ ] 1.2: For EACH rubric, verify every referenced parameter exists in that tool's parameter list
  - [ ] 1.3: Verify CRUD coverage — if rubric expects update/delete, does that tool type exist?
  - [ ] 1.4: For EACH search/filter rubric, verify the tool supports the required filter attribute
  - [ ] 1.5: For EACH entity referenced, verify it's discoverable via at least one tool (≤5 call chain)
  - [ ] 1.6: Check aggregation/pagination — can the complete source-defined cohort be enumerated and retrieved without truncation? Do not fail solely because the task has >50 records or >10 pages
  - [ ] 1.7: Check for PDF/attachment content referenced without a reader tool
  - [ ] 1.8: Check amount derivation — any rubric amounts from partial/truncated data?
  - [ ] 1.9: Check numeric observability — compare canonical raw values/inputs with tool-visible values/precision; inaccessible precision is UNREACHABLE
  - [ ] 1.10: Check Persona ACL feasibility for every required Gmail, Slack, GCal, or Contacts read: mailbox ownership; Slack membership/public visibility; calendar ownership/share/invite; Contacts visibility; intentional denial outcome or authorized unscoped alternate
  - [ ] 1.11: Record verdict per rubric: FEASIBLE / IMPOSSIBLE / UNREACHABLE

- [ ] Phase 2: F2 — Persona & Date Mismatch
  - [ ] 2.1: Verify prompt reads as if written by the assigned persona (role, authority, access)
  - [ ] 2.2: Verify persona has authority for ALL rubric-required actions (no role overreach)
  - [ ] 2.3: Check Slack/email attribution — messages match the assigned persona in universe data?
  - [ ] 2.4: Extract effective scenario date; verify ALL rubric events fall within reachable timeline
  - [ ] 2.5: Check for future-data-as-past — rubric expects analysis of events not yet happened?
  - [ ] 2.6: Scan prompt for EVERY entity reference; search universe data — does each exist?
  - [ ] 2.7: Check staff data consistency (is_active vs prompt claims about employment)
  - [ ] 2.8: For EACH email recipient in rubrics, verify they exist in Contacts/Slack AND are active
  - [ ] 2.9: HARD GATE — verify 2_Persona.txt Persona Key, Persona Email, Name, Role, and Department all exactly match one taxonomy roster entry; AMV dropdown override is prohibited
  - [ ] 2.10: Verify Universe Explorer author god-mode is kept separate and Agent Runner + Run Verifiers use the same required persona
  - [ ] 2.11: Record verdict: CONSISTENT / MISMATCH / PHANTOM

- [ ] Phase 3: F3 — Process Rubric Violations
  - [ ] 3.1: Identify ALL rubrics categorized as "Process" — list them
  - [ ] 3.2: For EACH, apply the canonical three-condition test: required by every valid path, not capturable by a stricter Outcome, and describes verification rather than an execution trace
  - [ ] 3.3: For ALL rubrics: does criterion name a specific tool as success condition? (TOOL_GATE)
  - [ ] 3.4: Does criterion pin specific query params when alternatives work? (QUERY_GATE)
  - [ ] 3.5: Check for always-pass or always-fail gates (tool returns nothing or everything trivially)
  - [ ] 3.6: Check for write-actions categorized as Process (must be Outcome 1.1)
  - [ ] 3.7: Count: Process >40% of total? 3+ items crediting same tool/service?
  - [ ] 3.8: Only identify a missing Process criterion when the prompt has a sequential or causal dependency that Outcome criteria cannot verify; record it as NON_FAIL_MISSING_PROCESS
  - [ ] 3.9: Reject any tool-call, OE, Process, or complexity credit for set_acting_user environment configuration
  - [ ] 3.10: Record verdict: LEGITIMATE_PROCESS / TOOL_GATE / QUERY_GATE / ALWAYS_PASS / ALWAYS_FAIL / WRITE_IN_PROCESS / NON_FAIL_MISSING_PROCESS

- [ ] Phase 4: F4 — Rubric Defects (Broken / Over-Strict)
  - [ ] 4.1: Extract EVERY expected value from EVERY rubric ($ amounts, names, IDs, dates, emails, counts)
  - [ ] 4.2: GREP each against universe data — does it exist? For calculations, verify components + math
  - [ ] 4.3: Verify quantitative values through the cataloged tool path — raw existence alone is insufficient; record rounding, truncation, omitted inputs, and prompt-authorized derivations
  - [ ] 4.4: For EACH email address, verify it exists in Contacts/Slack AND maps to the right person
  - [ ] 4.5: For EACH rubric pinning a specific approach: would a valid alternative path be wrongly penalized?
  - [ ] 4.6: Check: equivalent-tool over-spec, email format over-spec, query param over-spec, structured ID lock-in
  - [ ] 4.7: Check role/segregation overreach — persona required to act beyond their authority?
  - [ ] 4.8: For service creates, verify reference fields (project_id, assignee_id) are discoverable
  - [ ] 4.9: Verify rubric facts match CURRENT universe data (not stale from previous snapshot)
  - [ ] 4.10: Reject rubrics/prompt reasoning that assumes write-side ACL denial or persona ACL on GDrive/GitHub/Snowflake/GDocs/GSheets/GSlides/Trello/Linear/Confluence
  - [ ] 4.11: Record verdict: SOUND / BROKEN / OVER_STRICT

- [ ] Phase 5: F5 — Illegal Tool-Output Dependencies
  - [ ] 5.1: For EACH criterion: can a judge verify it from the final response and/or write-call arguments, without making hidden tool-return success or response content the acceptance condition?
  - [ ] 5.2: Flag: "tool returned success" checks, values only in tool responses, aggregation across responses
  - [ ] 5.3: Distinguish: content in write-action args (for example, Slack message text) IS verifiable ✓
  - [ ] 5.4: Flag: rubric pass/fail based on tool success vs timeout (infrastructure dependency)
  - [ ] 5.5: Verify any direct evidence check uses the same assigned persona and never inaccessible cross-persona hidden state
  - [ ] 5.6: Record verdict: SELF_CONTAINED / VERIFIABLE_FROM_ARGS / NEEDS_TOOL_OUTPUT

- [ ] Phase 6: F6 — QC-Pattern Compliance (derived from 158-task QC audit)
  - [ ] 6.1: Atomicity — does ANY criterion bundle multiple independently-verifiable items, including quantifier-based bundling such as "at least N"? (FAIL if >1; the large audit-table exception permits atomic spot checks, not bundled mappings)
  - [ ] 6.2: Requirement-Level Forward Coverage — decompose the prompt and any validly incorporated environment source; does every authorized action, requested fact/conclusion, content item, recipient, destination, condition, qualifier, timing/order constraint, format requirement, and exclusion map to at least one rubric? For an eligible large audit table, repeated cells may be covered through overall total/reconciliation checks plus representative spot checks, with no minimum spot-check count or one-rubric-per-row requirement.
  - [ ] 6.3: Under-Strict — for each criterion in isolation: could a wrong answer still pass? (FAIL if plausible)
  - [ ] 6.4: Destination Consistency — do all rubrics target the prompt-specified output destination? (not "final response" when prompt says email/Slack)
  - [ ] 6.5: Blank Fields — does every rubric have non-blank `title`, `category`, `justification`, and `evidence`?
  - [ ] 6.6: Exclusion Coverage — if prompt has filter criteria + universe has decoys, is incorrect inclusion penalized?
  - [ ] 6.7: Delegation Clarity — does prompt mix "I'll [verb]" with agent imperatives? (FAIL = Action Decision Ambiguity)
  - [ ] 6.8: UGT Convergence — if all 6 runs converge, apply deeper scrutiny before failing UGT
  - [ ] 6.9: OE Authority — does an OE contradiction propagate into prompt feasibility, rubric correctness, or required action coverage? (OE-only inaccuracies remain non-failing)
  - [ ] 6.10: Feasibility — can EVERY explicit prompt ask be fulfilled? (no "minor secondary" escape)
  - [ ] 6.11: Date Alignment — is universe data temporally sound with February 28, 2026? (no "still-solvable" escape)
  - [ ] 6.12: Prompt Specificity Ceiling — does any rubric field add or narrow a requirement beyond the prompt and any validly incorporated environment source?
  - [ ] 6.13: Duplicate Rubrics — compare every pair; do any exact copies or semantic paraphrases test the same requirement on the same artifact?
  - [ ] 6.14: Vague Exemplar Language — scan every rubric field for `such as`, `e.g.`, and `for example`; count one Moderate issue per affected rubric
  - [ ] 6.15: Explicit Acceptance — does every flexible rubric define a complete accepted set or objective semantic acceptance rule?
  - [ ] 6.16: Affirmative Criterion Wording — does the conceptual criterion in every `title` express a positive Agent action, classification, scope boundary, or preserved state? Run a case-insensitive lexical pre-scan of `title` for `does not`, `do not`, `makes no`, `has no`, standalone `no`/`not`, `never`, `without`, `avoid`, `refrain`, and `fail to`; review every hit. FAIL for prohibition-only or absence-only syntax.
  - [ ] 6.17: Numeric Visibility — does any prompt or rubric require precision/calculation unavailable through the Agent's cataloged tool-visible environment, or does an OE numeric mismatch propagate into scoring? (OE-only inaccuracies remain non-failing)
  - [ ] 6.18: Affirmative ACL-Denial Outcome — intentional denial criteria require the Agent to identify/report/escalate the denial or surface an authorized alternative; "does not access" alone is invalid
  - [ ] 6.19: ACL Complexity Hygiene — blocked/denied/repeated calls and set_acting_user environment configuration do not count toward complexity

- [ ] Phase 7: Final Verdict
  - [ ] 7.1: Fill in per-rubric findings table + task-level checks table
  - [ ] 7.2: Count hard failures per family and apply Overall Rubric Quality thresholds to Moderate findings
```

---

## Input Files

| File | Purpose |
|---|---|
| `5_Prompt.txt` | Prompt — persona, scenario, asks |
| `2_Persona.txt` | Required persona artifact — all five fields must exactly match one roster entry |
| `6_Oracle_Events.txt` | Expected agent steps — tool calls, parameters |
| `7_Rubrics.json` | All stored rubric objects (`title`, `category`, `justification`, `evidence`) — primary target of this eval |
| `3_UniverseDataForThisTask.json` | Task-specific universe snapshot (may be empty if CB did not export). Combine it with the current full/sharded base checkout in `HarmonyGames_Base_Universe/Services_Data/`, `4_Changelog.json`, `9_Universe_inject.sql` when present, and live service reads. |
| `HarmonyGames_Base_Universe/Tool_Access/*.json` | **Authoritative MCP catalogs** — read all 13 JSON files for exact services, tools, parameters, and capabilities |
| `HarmonyGames_Base_Universe/2_Persona_Briefs.md` | Persona role boundaries |
| `Agent_Responses/trajectory-run-{N}.json` | Canonical agent trajectories (if available); when a canonical file is absent, accept legacy `Agent_Responses/Run{N}_Trajectory.json` |
| `Docs/14_Long_Horizon_Task_Guidelines.md` | Conditional rules for tasks with a 500–1,000-call run |
| `Docs/15_Persona_ACL.md` | Active scoped-read semantics, exact identity requirements, expected-denial handling, and author/runner/verifier separation |
| `HarmonyGames_Base_Universe/Persona_ACL_Roster.json` | Exact taxonomy Persona Key, Persona Email, Name, Role, and Department values |
| `QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/` | Canonical long-horizon pass baseline (592 calls) |

**Available services (exactly 13):** Gmail, GDrive, GitHub, Snowflake, Slack, GCal, GDocs, GSheets, GSlides, Trello, Linear, Contacts, and Confluence. Gmail can search/read, read attachments, mutate message/thread labels, archive threads, trash/untrash/delete messages or threads, and create/delete labels, but cannot send/reply/compose/draft. Snowflake is query/read-only.

**ACL boundary:** Persona-scoped reads apply only to Gmail, Slack, GCal, and Contacts. GDrive, GitHub, Snowflake, GDocs, GSheets, GSlides, Trello, Linear, and Confluence are the policy's unscoped public-service group: shared across task personas, not public outside the HarmonyGames evaluation environment. Do not invent persona ACL within that group. Writes are outside ACL scope and tasks must not assume write denial.

`HarmonyGames_Base_Universe/Services_Data/` is the current full base checkout, not a sampled subset: it contains the consolidated export, service-level JSON, sharded payloads, and repository trees.

---

## Phase 1: F1 — Impossible-with-Tools

**For EVERY rubric, verify tool existence, parameter existence, CRUD coverage, filter support, and data discoverability.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Phantom tool | Tool in rubric doesn't exist in `HarmonyGames_Base_Universe/Tool_Access/*.json` | Rubric expects deletion of a Linear issue, but the catalog exposes issue create/update/read operations and no issue-delete operation | **IMPOSSIBLE** |
| Phantom parameter | Parameter doesn't exist for that tool | Rubric expects `status` filter on search tool — no such parameter | **IMPOSSIBLE** |
| Missing CRUD | Rubric expects update/delete but only create/read exists | Prompt requires updating a Linear user, but the catalog has `linear_create_user`, `linear_get_user`, and `linear_list_users` with no user-update tool | **IMPOSSIBLE** |
| Missing filter | Rubric requires a parameter the named tool doesn't support | Rubric requires an `assignee` filter on `linear_get_issue`, whose only parameter is `id`; a valid OE must instead use a tool whose documented parameters fit the task | **IMPOSSIBLE** |
| Undiscoverable entity | Entity exists in data but no tool can surface it | `engineer Julia Lawson / Domino Delights project` never appears in ANY tool output | **UNREACHABLE** |
| Pagination wall | The source-defined cohort cannot be exhaustively enumerated because results truncate or no usable pagination path exists | A listing truncates an unknown cohort and exposes no next-page cursor or complete alternate listing | **UNREACHABLE** |
| Unreadable content | Rubric references file/attachment content without reader tool | Rubric expects values from PDF but tools only return filenames | **IMPOSSIBLE** |
| Truncated amount | Rubric amount derived from partial/first-page data | Rubric says "total of all invoices" but only first page of 500+ is accessible | **UNREACHABLE** |
| Precision loss | Raw universe contains a decimal, but the cataloged query path renders a whole-unit value and exposes no prompt-authorized recovery path | Raw `$10.52` is rendered as `$11`, while the rubric requires `$10.52` | **UNREACHABLE** |
| Cross-persona scoped-service read | Successful completion requires a Gmail/Slack/GCal/Contacts record outside the assigned persona's implemented visibility, with no intentional-denial outcome or authorized alternate | Another persona's private mailbox is the only source of a required answer | **UNREACHABLE** |
| Author-visibility substitution | Universe Explorer god-mode visibility is used to claim Agent Runner feasibility | Author can inspect a private Slack channel that the assigned runner persona cannot read | **UNREACHABLE** |

### Long-Horizon Legitimacy Check

For any task with a 500–1,000-call run:

1. Confirm the cohort is defined by an authoritative source and can be exhaustively enumerated.
2. Confirm each repeated call answers a distinct required question for a distinct record or evidence surface.
3. Check whether one available bulk call provides the same complete evidence. If it does, requiring individual calls is artificial.
4. Reject repeated reads, split queries, tiny checkpoints, unnecessary writes, or unrelated asks added only to increase volume.
5. Evaluate the deliverable and coverage—not the call count. No rubric may reward reaching a target number of calls.
6. If representative record-level rubrics are used for a large audit table, verify exhaustive Oracle Events/execution, overall total/reconciliation controls, and grounded atomic spot checks. There is no required minimum number of spot-check criteria.

ACL-blocked calls, repeated denied attempts, redundant retries, and `set_acting_user` environment configuration are not necessary Agent calls and cannot establish long-horizon legitimacy or minimum complexity.

A large cohort is not unreachable merely because it exceeds an ordinary-task record or page heuristic. It is unreachable only when available tools cannot establish or retrieve complete coverage.

An eligible large audit table does not need one rubric per repeated record-field cell. This exception never permits a bundled many-record mapping, an arbitrary “at least N of M” threshold, or sampling distinct write actions and non-repetitive requirements.

**Pass baseline:** `QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/` clears all six checks above — a source-defined cohort of 116 pull requests enumerated from two repository listings, five separately exposed GitHub evidence surfaces per record, no bulk substitute for any of them, 592 declared calls of which 580 are record-level, and 79 outcome-first rubrics that reconcile totals without rewarding volume. When a long-horizon task under review falls short, name which of the six checks it fails relative to that baseline.

---

## Phase 2: F2 — Persona & Date Mismatch

**Verify persona alignment, date consistency, and entity existence.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Persona role mismatch | Prompt actions exceed persona's role/authority | Coordinator doing executive-level strategic planning | **MISMATCH** |
| Wrong attribution | Slack/email messages attributed to wrong persona | Slack posts authored as `user_elena` when persona is Lisa Smith | **MISMATCH** |
| Role overreach | Rubric requires persona to approve/certify beyond their authority | Engineer required to approve a budget report (lead's job) | **MISMATCH** |
| Date contradiction | System date vs scenario date inconsistency | `current_date` is Jan 2026 but scenario references March-April events | **MISMATCH** |
| Future-as-past | Rubric expects analysis of events not yet happened per effective date | Prompt pins April 28 but system date varies per rollout (Oct, Sep) | **MISMATCH** |
| Phantom entity | Prompt references email/message/person that doesn't exist in universe | "Grace sent me a meeting notice" — no such email exists | **PHANTOM** |
| Staff inconsistency | `is_active` status contradicts prompt claims | `is_active=true` with `termination_date=null` but prompt says "last day April 4th" | **PHANTOM** |
| Inactive recipient | Rubric targets someone not in Contacts/Slack or deactivated | Slack message to a person who doesn't exist in contacts or has been deactivated | **PHANTOM** |
| Roster mismatch | Assigned persona does not exactly match one of the roster's 17 taxonomy persona records | Prompt names one persona while runner configuration binds another email | **MISMATCH** |
| Persona artifact mismatch | `2_Persona.txt` has a missing field or its Persona Key, Persona Email, Name, Role, and Department do not all match one roster entry exactly | Name and email come from different entries, or Role differs from the roster | **MISMATCH** |
| AMV override | AMV dropdown value is used to replace the assigned taxonomy persona | Run identity follows a UI dropdown instead of the roster-backed assignment | **MISMATCH** |
| Runner/verifier mismatch | Agent Runner and Run Verifiers use different persona identities | Verifier can see evidence that the Agent could not, or vice versa | **MISMATCH** |

---

## Phase 3: F3 — Process Rubric Violations

**For EVERY Process rubric, apply the three-condition test. For ALL rubrics, check for tool/query gates.**

A Process rubric is legitimate ONLY if ALL three hold:
1. The behavior is **required by every valid solution path**.
2. A stricter **Outcome rubric cannot capture it**.
3. It describes a **verification or behavioral property**, not a specific execution trace.

Explicit sequencing or ordering is a common valid Process case, but it is not the only possible case. When a Process rubric tests ordering, that ordering must be required by the prompt or a validly incorporated environment source.

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Tool-selection gate | `title` names a specific tool as the success condition | "The Agent must use `linear_get_issue`" — but verified environment evidence shows `linear_list_issues` returns the same required data | **TOOL_GATE** |
| Query-construction gate | `title` pins specific query parameters when alternatives return the same data | "The Agent must pass `query='overdue'` to `linear_list_issues`" even though a verified broader call returns the same required records | **QUERY_GATE** |
| Always-pass | Tool call always succeeds trivially in this universe | "Must use Trello tool" — in empty environment, calling it always passes | **ALWAYS_PASS** |
| Always-fail | Tool returns zero results; rubric always fails | "Must use `linear_list_comments`" — Linear has zero comments in this universe | **ALWAYS_FAIL** |
| Write-in-Process | Write action (create/update/post) categorized as Process | `slack_send_message` or `linear_create_issue` passes just for calling the tool, ignoring content | **WRITE_IN_PROCESS** |
| Inflated credit | 3+ rubric items credit calling the same tool/service; or Process >40% of total | 4 process items for Trello/GSheets/Confluence/Linear in empty env → 0.4-0.7 credit floor | Flag imbalance |
| Environment-config credit | Rubric/OE/complexity count rewards `set_acting_user` | Persona binding is counted as Agent verification or a tool call | **TOOL_GATE** |

---

## Phase 4: F4 — Rubric Defects (Broken / Over-Strict)

**For EVERY rubric expected value, verify existence. For every pinned approach, check alt-path preservation.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Missing target | Dollar amount, entity, ID, email in rubric doesn't exist in universe | `LIN-2026-0047` — no such issue in Linear | **BROKEN** |
| Bad calculation | Component data missing or math is wrong | Rubric says "total is $42,600" but source records sum to $38,200 | **BROKEN** |
| Tool-visible precision mismatch | Rubric embeds a canonical raw value that the Agent's cataloged tool path rounds, truncates, coerces, or omits | Rubric requires `$10.52`; the environment exposes `$11` | **BROKEN** |
| Hidden numeric derivation | Rubric requires a calculation absent from the prompt or incorporated source | Prompt asks for one-decimal display; rubric requires recomputing `91 / 853 = 10.7%` instead of accepting the exposed `11.0%` | **OVER_STRICT** |
| Empty service | Entire service/table has zero records | ~46 of 50 outcome items reference facts absent from empty environment | **BROKEN** |
| Stale data | Rubric facts don't match current universe snapshot | Rubric says "status: open" but current data shows "status: closed" | **BROKEN** |
| Equivalent tool ignored | Rubric demands Tool A when Tool B returns identical required data | Rubric demands `linear_get_issue` although verified environment evidence shows `linear_list_issues` returns the same required fields | **OVER_STRICT** |
| Target format locked | Rubric pins one internal identifier form without prompt or catalog support | Rubric requires an internal ID even though the prompt names only the record and a verified valid path targets it without that lock-in | **OVER_STRICT** |
| Query param locked | Rubric demands a specific query when a verified broader call returns the same data | Rubric requires `query='overdue'` on `linear_list_issues` despite direct environment evidence that another supported call returns the same required records | **OVER_STRICT** |
| ID format locked | Rubric pins a structured ID that the prompt did not require | Rubric pins an internal channel ID even though direct environment evidence establishes another valid supported form | **OVER_STRICT** |
| Role overreach | Rubric requires persona to act beyond their role authority | Engineer required to close/certify an item reserved for lead | **OVER_STRICT** |
| Undiscoverable ref | Service create requires a reference value no available tool can discover | A required reference cannot be obtained from any cataloged search/list/read path | **BROKEN** |
| Write-denial assumption | Rubric rejects or excuses a write because a related read service is persona-scoped | Treating ACL as if it blocked a Slack/GCal/Gmail/Contacts write | **BROKEN** |
| Invented unscoped-service ACL | Rubric requires persona visibility rules for Drive-family or another unscoped service | Treating GDrive/GDocs/GSheets/GSlides as persona-scoped under this ACL | **OVER_STRICT** |

---

## Phase 5: F5 — Illegal Tool-Output Dependencies

**For EVERY criterion, determine whether the judge can verify it from the final response and/or write-call arguments. Tool results may be inspected by evaluators to diagnose feasibility, environment behavior, or numeric rendering, but hidden return success or response content cannot define rubric acceptance.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Success-check | `title` checks "tool returned success" | "The Agent posts the Slack update via `slack_send_message`, and the tool returns success" — requires inspecting response | **NEEDS_TOOL_OUTPUT** |
| Response-only value | Expected value only appears in tool response, not call args | "The Agent identifies $3,200 from spreadsheet data" — $3,200 comes from tool response | **NEEDS_TOOL_OUTPUT** |
| Cross-response aggregation | `title` requires summing/calculating across multiple tool responses | "The Agent reports total outstanding as $X" — the sum requires seeing all responses | **NEEDS_TOOL_OUTPUT** |
| Infrastructure dependency | Pass/fail based on tool success vs timeout | "The Agent updates the Linear ticket, and the tool returns success" — response not visible | **NEEDS_TOOL_OUTPUT** |
| Cross-persona hidden evidence | Acceptance requires private evidence unavailable to the assigned persona or uses a differently bound verifier persona | Judge relies on another persona's mailbox/channel/calendar/contact state | **NEEDS_TOOL_OUTPUT** |
| Write-arg content | Content in write args (message text, document body) | "The Agent's Slack update includes the specific dollar amounts ($9,200 vs $8,450)" — text IS in call args | VERIFIABLE ✓ |
| Self-contained value | `title` embeds the expected value directly | "The Agent updates ticket MT-2026-0047 to 'In Progress'" — value embedded | SELF_CONTAINED ✓ |

---

## Phase 6: F6 — QC-Pattern Compliance

> **What this catches:** The core QC failure patterns from audited tasks plus the final rubric-authoring rules. These are defects that escaped the F1-F5 production audit checks but were caught by QC or final review. This family closes that gap.

| # | Check | What to look for | Verdict if found |
|---|---|---|---|
| 6.1 | **Atomicity** | The conceptual criterion in `title` bundles 2+ independently-verifiable items, including quantifier-based bundling such as "at least N" (ML confirmed: "split completely"). A qualifying large audit table may use atomic spot checks, but may not bundle many record values. | **NOT_ATOMIC** |
| 6.2 | **Requirement-Level Forward Coverage** | Any atomic requirement authorized by the prompt or a validly incorporated environment source has zero rubric coverage. Requirements include actions, requested facts/conclusions, content items, recipients, destinations, conditions, qualifiers, timing/order constraints, formats, and exclusions. For an eligible large audit table, overall total/reconciliation checks plus representative grounded atomic spot checks cover repeated cells; cells not selected for spot checks are not missing criteria, and no minimum spot-check count applies. | **MISSING_CRITERIA** |
| 6.3 | **Under-Strict** | In isolation: could a factually wrong answer still pass THIS criterion? (never argue sibling covers it). Do not call an eligible atomic register spot check under-strict merely because it intentionally grades one selected cell. | **OVERLY_BROAD** |
| 6.4 | **Destination Consistency** | Prompt says "post to Slack channel X" but rubric checks "final response" — wrong artifact | **WRONG_DESTINATION** |
| 6.5 | **Blank Fields** | Any rubric has blank `title`, `category`, `justification`, or `evidence` | **BLANK_FIELD** |
| 6.6 | **Exclusion Coverage** | Filter criteria + decoy records exist, but no rubric penalizes incorrect inclusion | **MISSING_EXCLUSION** |
| 6.7 | **Delegation Clarity** | Prompt mixes "I'll [verb]" with agent imperatives — ambiguous who acts | **DELEGATION_AMBIGUITY** |
| 6.8 | **UGT Convergence** | All 6 runs converge but UGT is being failed — apply deeper scrutiny (convergence is circumstantial, not dispositive, but demands justification) | Investigation signal |
| 6.9 | **OE Authority** | An OE contradicts prompt/universe truth and the contradiction propagates into prompt feasibility, rubric correctness, or required action coverage. OEs are CB internal docs, NOT ground truth; an OE-only inaccuracy remains non-failing under `Evals/2_OE_Eval.md`. | **OE_CONTRADICTION** |
| 6.10 | **Feasibility (strict)** | ANY explicit prompt ask cannot be fulfilled with available tools + data — no "minor secondary" escape | **INFEASIBLE** |
| 6.11 | **Date Alignment (strict)** | Universe data misaligned with February 28, 2026 AND creates stale references or ambiguity — no "still-solvable" escape | **DATE_MISALIGNED** |
| 6.12 | **Prompt Specificity Ceiling** | A criterion, justification, or evidence field adds a method, format, value constraint, threshold, qualifier, content item, destination, timing/order rule, or exclusion not required by the prompt or a validly incorporated environment source. A source is validly incorporated only when the prompt clearly directs the Agent to follow it, it is uniquely discoverable, it exists in the live task environment, and it is supported by the base universe or task changelog/injection. A grounded value is allowed only when it directly answers an authorized requirement and all valid answers remain accepted. | **OVER_SPECIFIED** |
| 6.13 | **Duplicate Rubrics** | Two rubrics have the same pass/fail signal for the same requirement on the same artifact, including semantic paraphrases and differently labeled copies. | **DUPLICATE_RUBRIC** |
| 6.14 | **Vague Exemplar Language (Moderate)** | A rubric contains `such as`, `e.g.`, or `for example`. Count once per affected rubric, regardless of occurrences or fields. | **VAGUE_EXEMPLAR** |
| 6.15 | **Explicit Acceptance** | A flexible rubric gives illustrations or a vague catch-all instead of a complete accepted set or an objective semantic acceptance rule. | **UNDEFINED_ACCEPTANCE** |
| 6.16 | **Affirmative Criterion Wording** | Run a case-insensitive lexical pre-scan of every `title` for `does not`, `do not`, `makes no`, `has no`, standalone `no`/`not`, `never`, `without`, `avoid`, `refrain`, and `fail to`, then review every hit. A conceptual criterion in `title` defines passing through prohibition-only or absence-only syntax when the hit supplies the acceptance condition. Rewrite exclusions as affirmative Agent classifications, scope boundaries, or preserved states. Negative factual states (`unimplemented`, `unconfirmed`, `unresolved`) and exact immutable entity titles containing negation tokens remain valid. Legacy reference examples do not override this repository-level rule. | **NEGATIVE_CRITERION_WORDING** |
| 6.17 | **Numeric Visibility** | A prompt or rubric requires a value, precision, rounding result, or derivation that exists only in raw backing data or depends on an unstated calculation, while cataloged tools expose a rounded/truncated value or omit required inputs. The same finding applies when an OE mismatch propagates into prompt/rubric scoring; an OE-only inaccuracy remains non-failing under `Evals/2_OE_Eval.md`. Display-format instructions do not silently authorize recomputation. | **NUMERIC_VISIBILITY_MISMATCH** |
| 6.18 | **Affirmative ACL-Denial Outcome** | An intentional scoped-read denial is graded only as inactivity (`does not access`) instead of an affirmative Agent action such as identifying/reporting/escalating the denial or finding an authorized alternate. | **NEGATIVE_CRITERION_WORDING / MISSING_CRITERIA** |
| 6.19 | **ACL Complexity Hygiene** | Complexity includes blocked/denied/repeated calls or `set_acting_user` environment configuration. | **TOO_EASY / INFLATED_COMPLEXITY** |

**Mandatory final-rule procedures:**

1. **Coverage matrix:** Quote the prompt and any validly incorporated source, split every authorized requirement into one independently verifiable row, and record at least one covering rubric ID. Topic similarity is not coverage. Coverage must target the requested artifact.
2. **Specificity comparison:** For every obligation in `title`, `justification`, and `evidence`, quote the prompt or validly incorporated source language that authorizes it. Retrieve that source from the live environment and verify it against the base universe or changelog/injection. A rubric may embed a universe-grounded answer to an authorized question; it may not turn a true but unrequested or incidental detail into a requirement.
3. **Pairwise duplicate scan:** Compare every rubric pair. If both pass and fail on the same behavior for the same requirement and artifact, remove one or rewrite it to grade a distinct requirement. Outcome 1.1 action-success and Outcome 1.2 action-content checks are distinct. The same fact in two different prompt-required artifacts is also distinct.
4. **Wording scan:** Search `title`, `category`, `justification`, and `evidence` case-insensitively for all three vague-exemplar phrases. Count one Moderate issue per affected rubric and apply the Overall Rubric Quality thresholds.
5. **Acceptance-definition check:** Flexible wording must identify the facts or meaning a valid paraphrase preserves, or list the complete accepted values. Illustrations and vague catch-alls do not define acceptance.
6. **Affirmative-criterion scan:** Run the mandatory case-insensitive lexical pre-scan for `does not`, `do not`, `makes no`, `has no`, standalone `no`/`not`, `never`, `without`, `avoid`, `refrain`, and `fail to`; review every hit for prohibition-only or absence-only acceptance syntax. Preserve every required exclusion by rewriting it as a positive classification, exact scope, unchanged state, or constrained activity criterion.
7. **Numeric-observability matrix:** For every quantitative prompt ask and rubric expected value, record canonical raw value/inputs, cataloged tool path, actual tool-visible value/precision, and prompt-authorized derivation. Raw universe existence alone never proves scoreability.
8. **Persona ACL matrix:** Require the exact five-field roster entry, resolve
   its Persona Email for the assigned taxonomy persona, verify runner/verifier
   parity, and map every Gmail, Slack, GCal, or Contacts read to scoped
   visibility, intentional affirmative denial handling, or an authorized
   unscoped alternate. Keep Universe Explorer author god-mode separate.

---

## Phase 7: Final Verdict

**Per-rubric aggregate table:**

| Rubric # | `title` (conceptual criterion) | F1 | F2 | F3 | F4 | F5 | F6 | Overall |
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
| F6: Any scoring-impacting OE_CONTRADICTION? | PASS/FAIL | |
| F6: Any OVER_SPECIFIED rubric fields? | PASS/FAIL | |
| F6: Any DUPLICATE_RUBRIC pairs? | PASS/FAIL | |
| F6: VAGUE_EXEMPLAR Moderate findings | Apply Overall Rubric Quality thresholds | |
| F6: Any UNDEFINED_ACCEPTANCE? | PASS/FAIL | |
| F6: Any NEGATIVE_CRITERION_WORDING? | PASS/FAIL | |
| F6: Any NUMERIC_VISIBILITY_MISMATCH? | PASS/FAIL | |
| F6: Any persona roster/runner/verifier mismatch or scoped-feasibility gap? | PASS/FAIL | |
| F6: Any negative-only ACL-denial criterion? | PASS/FAIL | |
| F6: Any inflated ACL/config complexity? | PASS/FAIL | |
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
│ PASS = zero hard failures across all families│
│ and Moderate-error thresholds are not exceeded.│
└─────────────────────────────────────────────┘
```

---

## Quick Reference: 38 Canonical Submission Gate Patterns

| # | Pattern | Family | Auto-flag |
|---|---|---|---|
| 1 | Rubric expects a Linear user-update tool, but only create/list/get user tools exist | F1 | IMPOSSIBLE |
| 2 | Entity ID appears in zero tool outputs | F1 | IMPOSSIBLE |
| 3 | Tool lacks filter for attribute rubric searches by | F1 | IMPOSSIBLE |
| 4 | Source-defined cohort truncates with no usable pagination or complete retrieval path | F1 | UNREACHABLE |
| 5 | Prompt references email/message/meeting that doesn't exist | F2 | PHANTOM |
| 6 | System date contradicts prompt scenario timeframe | F2 | MISMATCH |
| 7 | Persona attributed wrong in Slack/email vs assigned | F2 | MISMATCH |
| 8 | `is_active=true` but prompt says person has left | F2 | MISMATCH |
| 9 | "Must use `linear_get_issue`" when a verified `linear_list_issues` path returns the same required data | F3 | TOOL_GATE |
| 10 | Tool call always passes in empty environment | F3 | ALWAYS_PASS |
| 11 | Tool returns zero results; rubric always fails | F3 | ALWAYS_FAIL |
| 12 | Write action categorized as Process | F3 | WRITE_IN_PROCESS |
| 13 | Specific query parameters required although a verified supported alternative call returns the same data | F3/F4 | QUERY_GATE |
| 14 | Dollar amount / entity / ID doesn't exist in universe | F4 | BROKEN |
| 15 | Email address doesn't exist in contacts | F4 | BROKEN |
| 16 | Rubric demands one tool when another returns equivalent data | F4 | OVER_STRICT |
| 17 | Rubric pins an ID format absent from the prompt when another form is directly proven valid | F4 | OVER_STRICT |
| 18 | Persona required to act beyond role authority | F4 | OVER_STRICT |
| 19 | `title` checks "tool returned success" | F5 | NEEDS_TOOL_OUTPUT |
| 20 | Expected value only in tool response, not call args | F5 | NEEDS_TOOL_OUTPUT |
| 21 | Aggregation/calculation across multiple tool responses | F5 | NEEDS_TOOL_OUTPUT |
| 22 | `title` bundles 2+ independently-verifiable items, including "at least N" quantifier bundles (must split) | F6 | NOT_ATOMIC |
| 23 | Prompt-required write action has no Outcome 1.1 rubric verifying the action | F6 | MISSING_CRITERIA |
| 24 | Wrong answer could plausibly pass this criterion (per-criterion only) | F6 | OVERLY_BROAD |
| 25 | Rubric checks "final response" but prompt specifies Slack/document/record | F6 | WRONG_DESTINATION |
| 26 | Rubric has blank `title`, `category`, `justification`, or `evidence` | F6 | BLANK_FIELD |
| 27 | Filter criteria + decoy records exist but no exclusion rubric | F6 | MISSING_EXCLUSION |
| 28 | Prompt mixes "I'll [verb]" with agent imperatives | F6 | DELEGATION_AMBIGUITY |
| 29 | OE contradiction propagates into prompt feasibility, rubric correctness, or required action coverage; OE-only inaccuracies remain non-failing | F6 | OE_CONTRADICTION |
| 30 | Explicit prompt ask can't be fulfilled — no "minor secondary" escape | F6 | INFEASIBLE |
| 31 | Universe data misaligned with February 28, 2026 — no "still-solvable" escape | F6 | DATE_MISALIGNED |
| 32 | Task solvable in <15 tool calls / single-service / investigate+one Slack post | F6 | TOO_EASY |
| 33 | Any atomic requirement authorized by the prompt or a validly incorporated source has no covering rubric; an eligible large audit table may use overall total/reconciliation checks plus representative spot checks without a per-row or minimum spot-check requirement | F6 | MISSING_CRITERIA |
| 34 | Rubric field imposes a requirement narrower than the prompt | F6 | OVER_SPECIFIED |
| 35 | Two rubrics test the same requirement on the same artifact with the same pass/fail signal | F6 | DUPLICATE_RUBRIC |
| 36 | A rubric uses `such as`, `e.g.`, or `for example` (Moderate, once per rubric), or fails to define the accepted answer set/rule | F6 | VAGUE_EXEMPLAR / UNDEFINED_ACCEPTANCE |
| 37 | A `title` defines passing through prohibition-only or absence-only wording instead of an affirmative Agent action, classification, scope boundary, or preserved state | F6 | NEGATIVE_CRITERION_WORDING |
| 38 | Canonical raw value has greater precision than every cataloged tool-visible path, or the rubric requires an unstated calculation to recover it | F1/F4/F6 | UNREACHABLE / BROKEN / NUMERIC_VISIBILITY_MISMATCH |

---

## Key Rules

1. **One hard failure = task FAIL.** Vague Exemplar Language is Moderate and follows the Overall Rubric Quality thresholds rather than auto-failing individually.
2. **Do not rationalize away a match.** audit data shows these patterns are wrong >90% of the time.
3. **Process rubrics get triple scrutiny.** 61% of flagged Process rubrics needed fixing. Default: wrong until proven right.
4. **Check evidence/justification fields too.** Tool names in evidence must exist. Expected values must match universe data.
5. **Every authorized requirement needs coverage.** This includes explicit prompt requirements and task-relevant requirements from a validly incorporated environment source. Deliverable-level coverage is insufficient when a recipient, content item, condition, timing rule, format, or exclusion is left ungraded.
6. **The prompt plus validly incorporated sources form the specificity ceiling.** The source must exist live, be uniquely discoverable, and be supported by the base universe or changelog/injection. Universe-grounded answers may resolve authorized findings; they may not create extra obligations.
7. **Zero duplicates; tally vague exemplars correctly.** Remove exact or semantic duplicate rubrics. Count each rubric containing `such as`, `e.g.`, or `for example` as one Moderate issue and rewrite it with a complete accepted set or objective rule.
8. **Use affirmative acceptance wording while preserving exclusions.** A prohibition-only or absence-only conceptual criterion in `title` is a hard F6 failure. Rewrite it as an observable positive Agent state without dropping the decoy, exclusion, or prohibited-action signal.
9. **Verify numeric observability, not raw existence alone.** Every exact or precision-sensitive value must survive a cataloged tool path or a prompt-authorized derivation from tool-visible inputs. Repeated rounding across same-snapshot runs is an environment signal.
10. **Enforce Persona ACL at the correct boundary.** Require an exact roster-backed taxonomy persona, Agent Runner/Run Verifier parity, and assigned-persona feasibility for Gmail/Slack/GCal/Contacts reads. Keep author god-mode separate; never infer write denial or ACL on the other nine services.
11. **Do not reward environment setup.** `set_acting_user`, blocked calls, denial retries, and repeated calls are not Agent complexity, OEs, or Process behavior.
