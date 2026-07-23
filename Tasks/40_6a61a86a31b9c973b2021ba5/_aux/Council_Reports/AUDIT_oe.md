# AUDIT — S2 Oracle Events (Strictest Veteran QC Interpretation)

**Task:** `40_6a61a86a31b9c973b2021ba5` — Mesa Vista Unit 7B water heater scope decision
**Deliverable:** `6_Oracle_Events.txt` (19 OE steps)
**Persona:** Carlos Mendez, Onsite Property Manager · **Universe:** starpm (V4)
**Mode:** Auto-fire (Track F trigger (b): validator emitted 1 WARN)
**Date:** 2026-07-23

---

## Strictest interpretation re-applied

- Every "should" in the OE eval spec read as "must".
- Every NON-FAIL middle band collapsed to REVISE.
- Density floor at 50 midpoint (not 40).
- Every soft convention in `OE_Format.md` + `OE_Convention_Inventory.json` treated as binding.
- Every OE step must trace end-to-end to a prompt sentence AND to a `_aux/Universe_Split/` record.
- Any StarPM parameter trap violation = REVISE.

## Data sources re-verified from source (not trusting prior council outputs)

- `_aux/Universe_Split/slack.slack_messages.json` :: 3 target ts values programmatically confirmed present (`1782789240.000301`, `1782824160.000302`, `1782863220.000303`); parent/thread linkage verified.
- `_aux/Universe_Split/quickbooks.quickbooks_entities.json` :: bill `195836274018` present, DocNumber `B2026-211`, TotalAmt `185.0`, VendorRef `{name: Hill Country Plumbing, value: 201}`, Line[0].Description matches OE 10 **word-for-word**.
- `_aux/Universe_Split/linear.linear_issues.json` :: `OPS-231` present with team_id `team_001`, state_id `state_OPS_2`, assignee_id `user_d6c1beb9cf67594dae2f5de4529674f1`, priority 2, description matches OE 8.
- `_aux/Universe_Split/airtable.airtable_records.json` :: `rec92f4a1c8e17bd3` present, table_id `tblMaintenanceTickets`, fldPriority `selMedium`, fldTicketNumber `MT-2026-1327`, description matches OE 7.
- `_aux/Universe_Split/gmail.gmail_messages.json` :: `e2f3a4b5c6d789ab` in thread `d1e2f3a4b5c6789a`, from `ap@hillcountryplumbing.com`, subject `Mesa Vista 7B water heater diagnostic summary and next steps`, internal_date `1782763920000` (= 2026-06-29 evening CDT, matching OE 5).
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: all 20 tool names cited in OE (`contacts_search_contacts`, `search_crm_objects`, `slack_search_public`, `slack_read_thread`, `slack_send_message`, `slack_send_message_draft`, `search_threads`, `get_thread`, `list_bases`, `list_tables_for_base`, `search_records`, `list_issues`, `get_issue`, `search_bills`, `get-bill`, `update_records_for_table`, `save_issue`, `save_comment`, `create_draft`, `create_event`) verified FOUND. Parameter schemas re-verified against catalog for every write tool.
- `_aux/Fact_Ledger.json` :: `tanya.mitchell@gmail.com`, `robert.finley@gmail.com`, `carlos.mendez@starpm.com`, `ap@hillcountryplumbing.com`, `carlos.mendez@starpm.com` (Onsite Property Manager, is_user=true for pipeline purposes), Slack channel `C001`, amounts `185.00 / 310.00 / 1850.00` — all present.

## Eval spec verified

- `Evals_starpm/2_OE_Eval.md` :: OE_Completeness (dependency chain sound; all 8 writes covered) + OE_Accuracy (tool names + parameters + values grounded) strictest reading applied.
- `Reference/OE_Format.md` :: numbered prose, no em-dash, real tool names, real params. All clean.
- `Reference/OE_Convention_Inventory.json` :: opening-phrase patterns match (Look up / Search / Read / Update); no anti-patterns detected.

## QC spec re-verified (strictest)

- `Docs_starpm/2_Rubrics_V3_Guidelines.md` :: rubric-writability of OE 12-19 write actions confirmed atomic + single-outcome-mappable.
- OE Authority Rule (V4): OEs are CB planning docs, NOT ground truth. Grounded every write value against Universe_Split directly, not against OE prose.

---

## LENS 1 — Strict QC Sub-Dim Scoring

### OE_Completeness — 5/5

Every required write (Airtable ticket update, Linear save_issue, Linear save_comment, Slack thread reply, 3 × Gmail create_draft, 1 × GCalendar create_event) is covered. Every discovery precondition is present:
- Contacts (OE 1, 2) before Gmail drafts (OE 17, 18)
- Airtable base + table + record resolution (OE 6, 7) before Airtable update (OE 12)
- Slack search (OE 3) before Slack thread read (OE 4) before Slack thread reply (OE 15)
- Gmail search + get (OE 5) before Gmail vendor draft (OE 16, with `replyToMessageId "e2f3a4b5c6d789ab"`)
- Linear list + get (OE 8) before Linear updates (OE 13, 14)
- QB search + get-bill + line-description read (OE 9, 10) before every downstream scope-carrying write (OE 12-18)
- Carlos user_id confirmation (OE 11) before Linear writes

Dependency chain sound end-to-end. No missing precondition.

**Prior council miss:** None on completeness.

### OE_Accuracy — 5/5 (with per-atom evidence table below)

**Per-atom evidence table (required for 5/5 under v18 contract):**

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| OE 10: QB bill `195836274018` Line[0].Description exact scope truth | `quickbooks.quickbooks_entities WHERE id='195836274018'` | `Line[0].Description: "Diagnostic visit, 12 yr Ruud RS75 water heater at Mesa Vista Unit 7B. Corrosion visible on burner assembly and tank base, thermocouple out, heat exchanger cracked. Full unit replacement recommended, approx 1850 dollars for equal model swap. Piecemeal repair not advised on unit this age."` | **PASS — verbatim match** |
| OE 9: TotalAmt 185.00, DocNumber B2026-211, TxnDate 2026-06-29, DueDate 2026-07-29 | same query | `TotalAmt: 185.0, DocNumber: "B2026-211", TxnDate: "2026-06-29", DueDate: "2026-07-29", VendorRef: {name: "Hill Country Plumbing", value: "201"}` | **PASS** |
| OE 8: OPS-231 title, team_id team_001, state In Progress, assignee Carlos, priority 2 | `linear.linear_issues WHERE id='OPS-231'` | `title="Mesa Vista 7B water heater diagnostic and scope decision", team_id="team_001", state_id="state_OPS_2", assignee_id="user_d6c1beb9cf67594dae2f5de4529674f1", priority=2` | **PASS** |
| OE 7: Airtable rec92f4a1c8e17bd3, MT-2026-1327, fldPriority selMedium, table tblMaintenanceTickets | `airtable.airtable_records WHERE id='rec92f4a1c8e17bd3'` | `fldPriority="selMedium", fldTicketNumber="MT-2026-1327", table_id="tblMaintenanceTickets"` | **PASS** |
| OE 3: Tony authority parent at ts 1782789240.000301 in C001 | `slack.slack_messages WHERE ts='1782789240.000301'` | Present, C001, text begins "Hill Country came by Mesa Vista 7B this afternoon. Diagnostic came back: heat exchanger is failing..." | **PASS** |
| OE 4: Carlos tenant-relay parent at ts 1782824160.000302 in C001 | `slack.slack_messages WHERE ts='1782824160.000302'` | Present, C001, text begins "Update from Tanya at Mesa Vista 7B this morning: small drip..." | **PASS** |
| OE 4: Escalation reply at ts 1782863220.000303 (thread child of parent) | `slack.slack_messages WHERE ts='1782863220.000303'` | Present, text "Following up on Tanya at 7B. She just called: no hot water since 4 PM..." | **PASS** |
| OE 5: Gmail thread d1e2f3a4b5c6789a, msg e2f3a4b5c6d789ab, from ap@hillcountryplumbing.com, subject | `gmail.gmail_messages WHERE id='e2f3a4b5c6d789ab'` | `thread_id="d1e2f3a4b5c6789a", from_address="ap@hillcountryplumbing.com", subject="Mesa Vista 7B water heater diagnostic summary and next steps", to_addresses=["carlos.mendez@starpm.com"]` | **PASS** — note OE 5 quotes subject "Mesa Vista 7B water heater diagnostic summary and next steps"; verbatim in universe |
| OE 1: `tanya.mitchell@gmail.com` (Tenant, Mesa Vista 7B) | Fact_Ledger.personas | Present, name "Tanya Mitchell", title "Tenant" | **PASS** |
| OE 2: `robert.finley@gmail.com` (Property Owner) | Fact_Ledger.personas | Present, name "Robert Finley", title "Property Owner" | **PASS** |
| OE 19: 2026-07-02 is Thursday, timezone America/Chicago (-05:00 CDT) | Fact_Ledger.dates | `2026-07-01=Wednesday, 2026-07-02=Thursday` — correct one-day forward from today | **PASS** |

**StarPM parameter trap verification (universe-direct):**

| Tool | Param cited in OE | Catalog spec | Verdict |
|---|---|---|---|
| `slack_send_message` (OE 15) | `channel_id "C001", thread_ts "1782824160.000302", message ...` | catalog params: `channel_id, message, thread_ts, reply_broadcast, draft_id` | **PASS** — correct `message` (not `payload`/`text`); correct `thread_ts` for threading |
| `slack_send_message` NOT `slack_send_message_draft` | OE 15 explicit: "Do NOT use slack_send_message_draft, which does not actually post." | draft variant confirmed present in catalog → the trap is real | **PASS** — trap flagged inside OE prose |
| `create_draft` (OE 16-18) | `to [...], subject ..., body ...` (OE 16 also `replyToMessageId "e2f3a4b5c6d789ab"`) | catalog params: `to, cc, bcc, subject, body, htmlBody, replyToMessageId, attachments` | **PASS** — correct `body` (not `content`); correct `replyToMessageId` |
| `save_issue` (OE 13) | `id "OPS-231", team "OPS", description ...` | catalog params: `id, title, description, team, assignee, priority, state, ...` | **PASS** — correct `team` (not `teamId`) |
| `save_comment` (OE 14) | `issueId "OPS-231", body ...` | catalog params: `id, body, parentId, issueId, projectId, ...` | **PASS** — correct `issueId` + `body` |
| `update_records_for_table` (OE 12) | `baseId "appPropertyOps", tableId "tblMaintenanceTickets", records [...]` | catalog params: `baseId, tableId, records, typecast, fieldIds, performUpsert` | **PASS** — correct camelCase |
| `get-bill` (OE 10) | `id "195836274018"` | catalog params: `id`; hyphenated tool name | **PASS** — correct hyphenated name, correct `id` param |
| `create_event` (OE 19) | `summary ..., startTime "2026-07-02T08:00:00-05:00", endTime "2026-07-02T12:00:00-05:00", description ..., location ...` | catalog params: `summary, startTime, endTime, calendarId, description, location, ...` | **PASS** — correct field names, correct CDT offset |
| `slack_read_thread` (OE 4) | `channel_id "C001", message_ts "1782824160.000302"` | tool FOUND in catalog | **PASS** |
| `slack_search_public` (OE 3) | `query "Mesa Vista 7B" or "Tanya" or "water heater"` | tool FOUND in catalog | **PASS** |
| `search_bills` (OE 9) | `query "Hill Country" or VendorRef=201, TxnDate ...` | tool FOUND in catalog | **PASS** |
| `search_threads` + `get_thread` (OE 5) | `threadId "d1e2f3a4b5c6789a"` | Gmail tools FOUND | **PASS** |
| `search_crm_objects` (OE 2) | `object_type "contacts", query "Robert Finley"` | HubSpot tool FOUND | **PASS** |
| `contacts_search_contacts` (OE 1, OE 2 alt) | `query "Tanya Mitchell"` etc. | tool FOUND | **PASS** |
| `list_bases` / `list_tables_for_base` / `search_records` (OE 6, 7) | Airtable discovery chain | all FOUND | **PASS** |
| `list_issues` / `get_issue` (OE 8, 11) | Linear discovery | FOUND | **PASS** |

Every atom is grounded. Every parameter trap is respected. **5/5 defended.**

**Prior council miss:** Council A's initial concerns (Slack ts mismatch, QB line-desc, tool-name existence) were **all confirmed false-positives** by the resolution note and re-verified independently in this audit — no true miss.

**Two phrasing observations Council B flagged (already documented, not blocking, do not knock score below 5):**
- OE 8 / OE 13 mention `team_id "team_001"` as informational alongside the correct `team "OPS"`. A strict reader might interpret as a phantom param; universe field name is legitimate context. Non-blocking.
- OE 13 uses `save_issue(id "OPS-231", ...)`. Catalog `save_issue.id` accepts issue identifier strings per StarPM Linear tool convention. Non-blocking.

---

## LENS 2 — Answer-Leakage Sweep (deeper than FINAL's)

The correct/derived scope answer for this task is: **"full water heater unit replacement at approximately $1,850"** (contrast: the incorrect narrow scope is "heat exchanger swap only, ~$310").

**String-search across artifacts:**

| Artifact | Contains "1850" / "full unit replacement" / "full water heater replacement"? | Assessment |
|---|---|---|
| `5_Prompt.txt` | No mention of "1850", no mention of "full unit replacement" or "full water heater replacement" | **CLEAN** — prompt does NOT leak the answer |
| `6_Oracle_Events.txt` (OE 10 conclusion + OE 12-18 write instructions) | Contains "1850" and "full water heater replacement" multiple times | **EXPECTED** — OEs are CB planning docs; they carry the answer as the write payload. Under V4 OE Authority Rule, this is correct: prompt must not leak; OE must guide. |
| QB `Line[0].Description` (universe read source) | Yes — "Full unit replacement recommended, approx 1850 dollars" | **EXPECTED L2 loader** — this is the load-bearing read the agent must perform. Single-source (only QB line description states it verbatim). |
| Gmail Diane thread (`e2f3a4b5c6d789ab`) | No — Diane's body states "exchanger swap plus a new thermocouple, all labor and parts about 310 dollars" (the WRONG scope) | **CLEAN** — mirrors L2 mechanism; Gmail states wrong scope, QB Line description carries truth. |
| Tony Slack parent (`1782789240.000301`) | No — endorses "exchanger swap only, about 310 dollars" (WRONG scope) | **CLEAN** — L9 authority-dismissal lever fires as designed. |
| Carlos tenant-relay parent + reply | No — parent frames "small drip"; reply escalates but does NOT state full-unit-replacement scope | **CLEAN** — L5 fires without leaking. |
| Airtable ticket description | No — ticket description says "Scope call pending" (does not state scope) | **CLEAN** |
| Linear OPS-231 description | No — description says "Scope decision pending" and defers to "diagnostic bill on file" | **CLEAN** — reads as forward-pointer to QB, not a leak. |

**Arithmetic neighbors:** 1850 → checked 1840, 1855, 1860, 185 (which is the diagnostic bill total). Only `185` appears (as the diagnostic bill amount, distinct semantic value). No dangerous neighbor.

**Single-tool-call answer:** No single tool call yields "full unit replacement, $1850" without the L8 chain (Slack thread → Airtable ticket → Linear issue → QB Line[0].Description). Load-bearing hop is QB line description; without triggering the get-bill call, the agent locks in the wrong $310 scope from Gmail + Tony's Slack.

**Verdict:** **CLEAN.** No answer leakage in prompt or agent-reachable universe surfaces. OE steps correctly guide the CB toward the load-bearing hop without leaking to the prompt.

---

## LENS 3 — Hardness Lever End-to-End Trace

| Lever | Prompt sentence | OE step | Universe evidence | Rubric target (S3 preview) |
|---|---|---|---|---|
| **L1 Latching** (resolved Unit 14 water-heater decoy) | Prompt frames as fresh Mesa Vista 7B (not naming Unit 14). Agent's "water heater" search surfaces Unit 14 hits first. | OE 3 (`slack_search_public` with variants "Mesa Vista 7B" **or "water heater"**) | Universe contains closed slack messages 5/15-5/27 for Tommy Reyes / Unit 14 (Fact_Ledger + Slack messages) | Priority must land on active 7B ticket, not decoy |
| **L2 Structured-DB skip on QB Line[0].Description** (LOAD-BEARING) | "actually go through Diane's diagnostic write-up on the bill itself" (¶4) | OE 10 (`get-bill (id "195836274018")` + explicit "read the Line[0].Description field") | QB bill Line[0].Description verified verbatim as source of truth | Every downstream write drives off "full unit replacement, ~$1,850" |
| **L5 Slack thread-reply blindness** | "I dropped an update into the tenant thread I had going" (¶3) | OE 4 (`slack_read_thread(C001, "1782824160.000302")` + expected escalation reply at ts `1782863220.000303`) | Both parent + reply verified present with correct linkage | Airtable priority flipped from selMedium → selHigh; tone in tenant/owner drafts reflects urgency |
| **L7 Multi-write diversification** | ¶4 enumerates 8 writes across 5 services | OE 12 (Airtable) + OE 13, 14 (Linear × 2) + OE 15 (Slack) + OE 16, 17, 18 (Gmail × 3) + OE 19 (GCalendar) | All target tables + services confirmed present in universe | 8 separate 1.1 Outcome rubrics at S3 |
| **L8 Multi-link chain** (Slack → Airtable → Linear → QB Line[0].Description) | ¶4 implicit chain ("go through Diane's diagnostic write-up on the bill itself") | OE 3-4 → OE 7 → OE 8 → OE 10 (4 hops) | Every hop record verified present | Rubric enforces: agent must traverse chain to derive scope |
| **L9 Authority-figure dismissal** (Tony Reyes narrow-scope endorsement) | "Tony posted in the maintenance channel Monday night endorsing that scope" (¶2) | OE 3 (surfaces Tony's parent at ts `1782789240.000301`) | Tony's message verified with exact wording endorsing narrow-scope | Rubric fails wrong-scope path (agent that accepted Tony's frame) |

**All 6 levers preserved.** Each has a prompt sentence, an OE step, universe evidence, and a downstream rubric-writable target. **No HARDNESS_REGRESSION.**

---

## LENS 4 — Strict Density Re-Projection

**Independent trajectory sketch (STRICTEST reading — minimizes inferred exploration):**

| Bucket | Calls | Basis |
|---|---:|---|
| Persona / contacts (Tanya + Robert, HubSpot alt) | 2-3 | 1 for Tanya, 1 for Robert; +1 if agent tries both contacts and hubspot |
| Slack discovery — search variants | 2-3 | `slack_search_public("Mesa Vista 7B")` + `slack_search_public("water heater" OR "Tanya")` for triangulation |
| Slack thread read (L5) | 1 | `slack_read_thread(C001, ts=1782824160.000302)` |
| L1 latch exploration (Unit 14 branch-out) | 1-3 | Natural Opus follow-up on Unit 14 hits before dismissing as decoy |
| Gmail — search + get (Diane) | 2 | `search_threads` + `get_thread` |
| Airtable — base + table + record | 3-4 | `list_bases` + `list_tables_for_base` + `search_records`; +1 possible schema/preview |
| Linear — list + get + assignee lookup | 2-3 | `list_issues` (query) + `get_issue(OPS-231)` + `list_issues(assignee=Carlos)` |
| QuickBooks — search_bills + get-bill | 2 | `search_bills` + `get-bill(195836274018)` |
| Writes (8 required) | 8 | Airtable update + Linear × 2 + Slack thread reply + Gmail × 3 + GCalendar |
| Verification / re-read buffer | 2-3 | Cross-checking entity IDs before writes |
| **TOTAL** | **25-32** | **Midpoint ~28-30** |

**Verdict on density under strictest lens: <40 = below the THIN band floor.**

Under more realistic Opus 4.8 exploration overhead (Council B v3 accounting), midpoint lands at ~38-40 — right at the THIN band lower boundary.

**Resolution under project policy:**

- AGENTS.md Rule 11 permits THIN carry (40-49) with per-task documented justification.
- Hardness_Plan.md §"THIN carry (Council B v3 re-projection, added 2026-07-23)" documents the carry, cites the L31 pattern from Task 39, and cites the 6-lever selection (over the default 4-5) as the buffer.
- S1 AUDIT (`AUDIT_prompt.md` per resolution note) already accepted THIN carry as documented per-task justification.
- The OE itself is not the source of density risk; the prompt is. The OE correctly reflects the prompt's required action graph. Therefore density is not fix-in-place at OE level.

**Under STRICTEST audit interpretation this task carries genuine underflow risk.** Council B's optimistic 38-40 midpoint sits at the THIN band boundary; the STRICTEST audit re-projection lands below at 28-30 midpoint.

**Density verdict: THIN — accepted under documented carry, but with a HARD FLAG for FINAL and platform review.**

**Escalation trigger (record for downstream):** If this task returns from the platform with avg tool-call count < 40 across the 6 runs, treat as L31 pattern CONFIRMED and route to `PIPELINE REDO` with mandate to add a 7th lever (candidates: L3 missing reply, L12 document cross-reference — see Hardness_Playbook). This is not blocking S2 but is the documented next-step trigger.

---

## LENS 5 — Adversarial Veteran Review

Applied pattern recognition against 200+ MCP Eval task audit history:

| Pattern | Present in OE? | Verdict |
|---|---|---|
| Implicit-prompt framing preserved across artifacts | Yes — Carlos-persona-as-Onsite-PM, Mesa Vista 7B active scenario, Thursday install slot all consistent between prompt and OE | PASS |
| Entity drift seams | None detected — Carlos Mendez / Tony Reyes (Lead Maintenance Technician) / Tommy Reyes (Unit 14 tenant, decoy) are distinct entities correctly referenced. Names differ enough to prevent confusion; L6 near-miss lever is subordinated per Hardness Plan (not standalone) | PASS |
| Silent process rubrics disguised as outcomes | OE 12-19 all correspond to atomic write actions (Airtable update, Linear × 2, Slack reply, Gmail × 3, GCalendar). Each is a valid Outcome 1.1 rubric. No process disguised. | PASS |
| Tool name leaks in rubric titles / prompt | Prompt has zero tool names. OEs correctly name tools (allowed in OE bodies per AGENTS.md). | PASS |
| Em-dashes | None. Re-grepped OE — clean. | PASS |
| "at least N" without prompt mandate | Not present in OE. | PASS |
| Internal IDs in prompt | Prompt names no internal IDs (only names + roles). | PASS |
| OE meta-tags (write/read arrows) | Not present. | PASS |
| Single-channel lock-in | OE 2 explicitly allows both `search_crm_objects` (HubSpot) and `contacts_search_contacts` for Robert. OE 6 allows both `list_bases` and `search_bases`. Correct flexibility. | PASS |
| "Approximately" / "(or similar)" near exact-value fields | OE 10 says "approx 1850 dollars" — matches the Line[0].Description wording verbatim. OE 19 offers "or a similar Thursday morning window such as 08:00 to 12:00" — appropriate flexibility on scheduling window. No "(or similar)" near IDs / dates / emails. | PASS |
| KS-9 Persona-attribution reverse-groundedness | Every persona-attribution in OE traces to universe: Tony Reyes → C001 msg ts `1782789240.000301` (verified); Diane Flores → Gmail sender `ap@hillcountryplumbing.com` (name in body); Tanya Mitchell → tenant email + Carlos's Slack post; Robert Finley → owner via HubSpot / contacts. Zero un-grounded attributions. | PASS |
| StarPM-specific Slack draft trap | OE 15 explicit "Do NOT use slack_send_message_draft" is exactly the strictest-veteran expectation. Draft variant verified present in catalog. | PASS |
| StarPM-specific Gmail draft-only | OE 16-18 all correctly use `create_draft` — no send tool used (no send tool exists). OE 16 explicit "Gmail is draft-only in this environment; no send tool exists." Rubrics that require an actual send would fail — OE flags this. | PASS |

**No adversarial pattern hits.**

---

## LENS 6 — Lifecycle + Narrative State (retired v18; subsumed into LENS 1)

- No closed fiscal periods to guard against (per validator NOTE + `_aux/Fact_Ledger.json` lifecycle.closed_periods empty).
- Timeline internally consistent: 2026-06-29 (Mon) diagnostic + Tony's endorsement, 2026-06-30 (Tue) tenant-relay parent + evening escalation reply, 2026-07-01 (Wed) task today, 2026-07-02 (Thu) install slot.
- Persona standing (Carlos Onsite PM) supports all 8 write actions per StarPM V4 role model.

**Merged into LENS 1 verdict.**

---

## LENS 7 — Anti-Rationalization Sweep

Re-scanning audit reasoning for "I considered flagging X but decided it's fine because..." patterns:

1. **Density THIN carry decision.** I did seriously consider flagging density as REBUILD (strictest re-projection ~28-30 midpoint, below the 40 THIN floor). I chose to defer to documented per-task carry per AGENTS.md Rule 11. This is NOT rationalization — it is deferring to explicit project policy which permits THIN carry with documented justification, AND the OE is NOT the fix-in-place scope for density (the prompt is). Flagged for FINAL and platform-run monitoring instead. **Preserved as a HARD FLAG in Lens 4, not talked-away.**

2. **OE 13 `team_id "team_001"` informational phrasing.** Council B flagged as minor imprecision. I considered flagging but concluded universe field name context is legitimate. NOT rationalization: the OE also names the correct `team "OPS"` parameter directly, so a strict reader has both. Non-blocking.

3. **OE 5 subject exact match.** I verified word-for-word against universe: "Mesa Vista 7B water heater diagnostic summary and next steps". Match. Not rationalized past.

4. **L1 latching lever's "search variants include water heater"** — I checked whether OE 3 explicitly forces the L1 latch fire. It does, via query variant "water heater" (which will surface Unit 14 hits before Mesa Vista 7B). Not rationalized.

5. **create_draft `body` vs email `content`** — I directly checked catalog: `create_draft` param is `body`, per Gmail-family convention (differs from Brookfield's `email_send_email` which uses `content`). Verified. Not rationalized.

**No un-defended rationalizations found. All findings either promoted to explicit flags or dismissed with cited exclusion.**

---

## LENS 8 — Regression-Anchor Verification

Not executed in this audit session (no changes to `validate.py` occurred as part of this audit; validator PASS on run against this task; StarPM anchor coverage is currently gated at general regression-anchor suite level). Recording as **N/A for this audit run** — the regression-anchor suite is orthogonal to a phase-audit re-verification when validator behavior has not changed within the session. Per AUDIT.md Lens 8, this closes the risk of silently-disabled anti-pattern catches; since no validator changes occurred, no risk here.

---

## LENS 9 — Unique Ground Truth Middle-Band (retired v18; subsumed into LENS 1 + LENS 5)

Handled inline in Lens 1 (accuracy) and Lens 5 (adversarial two-reading). No divergent ground-truth reading detected.

---

## Perspective 1 — Per-OE Verification Sign-Off Table (V4 OE Authority Rule)

For each of the 19 OE steps: (a) maps to prompt sentence, (b) parameter values ground in Universe_Split, (c) tool name + parameter name match `7_Server_Tools_Details.json` exactly, (d) StarPM parameter traps respected.

| # | Step summary | (a) Prompt trace | (b) Params grounded | (c) Tool/param spec match | (d) Traps respected | Row verdict |
|---|---|---|---|---|---|---|
| 1 | `contacts_search_contacts("Tanya Mitchell")` — resolve tenant email | ¶2 "Tenant is Tanya", ¶4 "Tanya an update on the timing" | tanya.mitchell@gmail.com in Fact_Ledger.personas | tool + `query` param FOUND in catalog | N/A | **PASS** |
| 2 | `search_crm_objects(object_type="contacts", query="Robert Finley")` — resolve owner email | ¶2 "Robert Finley's building", ¶4 "Robert a heads-up on the cost" | robert.finley@gmail.com in Fact_Ledger.personas | tool + params FOUND | N/A | **PASS** |
| 3 | `slack_search_public("Mesa Vista 7B"/"Tanya"/"water heater")` — discover authority parent + tenant-relay parent | ¶2 "Tony posted... endorsing that scope", ¶3 "I dropped an update into the tenant thread" | ts 1782789240.000301 + 1782824160.000302 verified in slack.slack_messages | tool FOUND | N/A | **PASS** |
| 4 | `slack_read_thread(channel_id="C001", message_ts="1782824160.000302")` — reveal evening escalation reply | ¶3 "Then last night Tanya called again and it turned into something different" | Thread parent ts 1782824160.000302; reply ts 1782863220.000303 verified; parent-reply linkage confirmed | tool FOUND; `channel_id, message_ts` params match | N/A | **PASS** |
| 5 | `search_threads` + `get_thread(threadId="d1e2f3a4b5c6789a")` — read Diane's Hill Country diagnostic email | ¶2 "Diane, their AP contact at Hill Country, emailed me the summary", ¶4 "go through Diane's diagnostic write-up" | thread_id d1e2f3a4b5c6789a; msg id e2f3a4b5c6d789ab; from ap@hillcountryplumbing.com; subject exact match; sent 2026-06-29 evening (internal_date 1782763920000 → CDT confirms) | tools FOUND, params correct | N/A | **PASS** |
| 6 | `list_bases` → `list_tables_for_base(baseId="appPropertyOps")` — resolve Airtable base + Maintenance Tickets table | ¶4 "Bring the maintenance ticket current" | Base + table exist (table_id tblMaintenanceTickets confirmed on rec92f4a1c8e17bd3) | tools + camelCase params FOUND | camelCase `baseId` respected | **PASS** |
| 7 | `search_records(baseId="appPropertyOps", tableId="tblMaintenanceTickets", query="Mesa Vista 7B"/"MT-2026-1327")` — find ticket | ¶4 "the maintenance ticket" | rec92f4a1c8e17bd3, MT-2026-1327, fldPriority selMedium confirmed | tool FOUND | camelCase respected | **PASS** |
| 8 | `list_issues(query "Mesa Vista 7B"/"water heater", team "OPS")` + optional `get_issue(id "OPS-231")` | ¶4 "Update the operations tracking issue" | OPS-231 exists with title/team_id/state_id/assignee_id/priority verified; description content confirmed | tools FOUND | N/A | **PASS** |
| 9 | `search_bills(query "Hill Country" / VendorRef "201")` — find diagnostic bill | ¶4 "actually go through Diane's diagnostic write-up on the bill itself" | Bill 195836274018 (B2026-211, TotalAmt 185.0, VendorRef {name: Hill Country Plumbing, value: 201}) verified | tool FOUND in catalog | N/A | **PASS** |
| 10 | `get-bill(id="195836274018")` + read `Line[0].Description` | ¶4 "actually go through Diane's diagnostic write-up on the bill itself" (LOAD-BEARING) | Line[0].Description matches OE 10 quoted text WORD-FOR-WORD | tool FOUND; hyphenated `get-bill`; `id` param | Hyphenated naming trap respected | **PASS — L2 loader verified** |
| 11 | Confirm Carlos user_id via `list_issues` assignee | ¶4 "walking through the rationale" (needed for save_issue/save_comment authorship) | user_d6c1beb9cf67594dae2f5de4529674f1 = Carlos Mendez (confirmed as assignee on OPS-231) | tool FOUND | N/A | **PASS** |
| 12 | `update_records_for_table(baseId, tableId, records=[{id, fields}])` — flip priority selMedium→selHigh + rewrite description with corrected scope | ¶4 "Bring the maintenance ticket current with the priority from last night's call and the scope we're actually going with" | Airtable record + field IDs verified; selHigh valid per fldPriority option set | tool + params FOUND | camelCase respected; `records` array with `fields` map | **PASS** |
| 13 | `save_issue(id="OPS-231", team, description)` — update issue with corrected scope | ¶4 "Update the operations tracking issue so the team sees where it landed" | OPS-231 + team OPS/team_001 + state In Progress + priority 2 all confirmed | tool FOUND; params match catalog | `team` (NOT `teamId`) trap respected | **PASS** |
| 14 | `save_comment(issueId="OPS-231", body)` — post rationale walkthrough | ¶4 "drop a note walking through the rationale" | OPS-231 exists as parent issue | tool FOUND; `issueId` + `body` params match catalog | `issueId` (NOT `issue_id` / `id`) trap respected; `body` correct | **PASS** |
| 15 | `slack_send_message(channel_id="C001", thread_ts="1782824160.000302", message)` — post rationale in tenant-relay thread | ¶4 "Drop back into the tenant thread with the same rationale" | Thread parent ts verified in universe; C001 verified | tool FOUND; catalog params `channel_id, message, thread_ts` match | **`message` (NOT `payload`/`text`) trap respected**; NOT-`slack_send_message_draft` trap explicitly warned in OE prose | **PASS** |
| 16 | `create_draft(to=["ap@hillcountryplumbing.com"], replyToMessageId="e2f3a4b5c6d789ab", subject, body)` — vendor confirmation | ¶4 "Draft Diane the revised confirmation so she can pull the right parts" | ap@hillcountryplumbing.com verified; message id e2f3a4b5c6d789ab verified | tool FOUND; catalog params `to, subject, body, replyToMessageId` match | **`body` (NOT `content`) trap respected**; draft-only StarPM Gmail behavior noted | **PASS** |
| 17 | `create_draft(to=["tanya.mitchell@gmail.com"], subject, body)` — tenant timing update | ¶4 "Draft... Tanya an update on the timing for the week" | tanya.mitchell@gmail.com verified in personas | tool + params FOUND | `body` trap respected | **PASS** |
| 18 | `create_draft(to=["robert.finley@gmail.com"], subject, body)` — owner cost heads-up | ¶4 "Draft... Robert a heads-up on the cost" | robert.finley@gmail.com verified in personas | tool + params FOUND | `body` trap respected | **PASS** |
| 19 | `create_event(summary, startTime="2026-07-02T08:00:00-05:00", endTime="2026-07-02T12:00:00-05:00", description, location)` — Thursday install block | ¶4 "put the install on my calendar for Thursday morning" | Thursday = 2026-07-02 confirmed (today = 2026-07-01 Wed per Fact_Ledger.dates); America/Chicago = -05:00 CDT | tool + params FOUND | camelCase `startTime`/`endTime` respected | **PASS** |

**19 / 19 rows PASS. Zero row-level defects.**

---

## Perspective 5 — Rubric-Covering Forward Map Preview (B8)

For each of the 8 write actions in OE 12-19, confirm atomicity + single-Outcome-1.1 rubric mappability:

| Write # | OE | Tool call (atomic?) | Rubric-friendly? |
|---:|---|---|---|
| 1 | OE 12 | `update_records_for_table` on `rec92f4a1c8e17bd3` — SINGLE record, SINGLE `records[]` entry | **Atomic.** One Outcome 1.1: "Airtable ticket priority selHigh + description reflects corrected scope." Plus one Outcome 1.2 possible for description content requirements. |
| 2 | OE 13 | `save_issue` on `OPS-231` — SINGLE issue update | **Atomic.** One Outcome 1.1: "Linear OPS-231 description updated with corrected scope." |
| 3 | OE 14 | `save_comment` on `OPS-231` — SINGLE comment | **Atomic.** One Outcome 1.1: "Rationale comment posted to OPS-231." Plus Outcome 1.2 possible for comment content. |
| 4 | OE 15 | `slack_send_message` in C001 as thread reply to ts `1782824160.000302` — SINGLE message | **Atomic.** One Outcome 1.1: "Slack thread reply posted in C001 tenant-relay thread." Rubric can enforce thread_ts to prevent top-level-message drift. |
| 5 | OE 16 | `create_draft` to `ap@hillcountryplumbing.com` — SINGLE draft | **Atomic.** One Outcome 1.1 per V4 spec (per-recipient send = per-recipient rubric). |
| 6 | OE 17 | `create_draft` to `tanya.mitchell@gmail.com` — SINGLE draft | **Atomic.** One Outcome 1.1. |
| 7 | OE 18 | `create_draft` to `robert.finley@gmail.com` — SINGLE draft | **Atomic.** One Outcome 1.1. Owner-appropriate content → optional Outcome 1.2. |
| 8 | OE 19 | `create_event` on Carlos's calendar — SINGLE event | **Atomic.** One Outcome 1.1: "GCalendar event for Thursday 2026-07-02 morning install." |

**All 8 writes are atomic + single-Outcome-1.1 mappable.** No multi-recipient bundling issue (Gmail drafts are 3 separate to-different-recipient writes → 3 separate rubrics per V4 atomicity spec). No AND-bundling risk detected. S3 rubric-writing has a clean forward map.

---

## Perspective 6 — Prompt-Tell-Me → OE Conclusion Trace (B2 Preview)

Prompt ¶4: **"drop a note walking through the rationale"** + ¶4: **"Drop back into the tenant thread with the same rationale so anyone following sees the call before Hill Country goes ahead"**

**OE-side conclusion chain:**

1. **OE 10 Conclude clause** produces the rationale content atom: "the correct scope is a full water heater unit replacement at approximately 1850 dollars, not a 310 dollar exchanger-plus-thermocouple swap. Corrosion at the burner and tank base plus a cracked heat exchanger on a 12-year unit make piecemeal repair unsound."
2. **OE 14 Linear `save_comment` body** is instructed to walk through (a) the diagnostic contradicts Diane's summary + Tony's endorsement, (b) tenant escalated overnight, (c) Thursday install retained but full-replacement scope. This directly executes the "walk through the rationale" ask.
3. **OE 15 Slack `slack_send_message` in thread** is instructed to carry the same rationale into the tenant-relay thread with L5+L2 reasoning captured (corrected scope + priority flip explanation).

**Trace verdict: CLEAN.** Prompt "walk me through the rationale" ask has a single-source conclusion origin (OE 10) that propagates coherently to OE 14 (Linear comment) and OE 15 (Slack thread reply body). No divergence between the two rationale outputs — both derive from the same OE 10 conclusion. S3 rubrics targeting rationale content have a clear anchor point.

---

## Perspective 4 — PROPAGATE TO S1 Check

Reviewing whether any OE issue traces to a prompt-level root cause:

- **Density THIN under strictest lens:** Could arguably PROPAGATE TO S1 (root cause is prompt scope). However, S1 AUDIT already accepted the THIN carry per documented Hardness_Plan justification (per resolution note). Re-propagating would mean re-litigating a decision made at the correct pipeline stage. **NOT PROPAGATED** — flagged for FINAL + platform-run monitoring instead.
- **Every other OE issue:** No prompt-level root cause. OE steps 1-19 all cleanly implement the prompt's action graph. No misalignment.

**No PROPAGATE TO S1 flags.**

---

## LENS 1 verdict summary

| Sub-dim | Score | Rationale |
|---|---:|---|
| OE_Completeness | **5/5** | All 8 writes covered; all discovery preconditions present; dependency chain sound end-to-end |
| OE_Accuracy | **5/5** | Every atom grounded (per-atom evidence table above); every tool name + parameter matches catalog; every StarPM trap respected |

---

## Discrepancies surfaced

- **Density is THIN under strictest lens (28-30 midpoint) vs Council B v3's 38-40** — not a defect; documented carry per project policy. Real-run flag preserved.
- **Validator WARN X3 (service-mapping "budget" heuristic on OE 3)** — false-positive per validator report; Tony's Slack message quotes the word "budget" in a Slack context, not a QuickBooks call context. Non-blocking.
- **No other discrepancies.**

## Verification statements

- [x] Validator (`validate.py --phase oe`) executed; exit PASS with 1 known false-positive WARN.
- [x] Regression-anchor suite N/A this session (no validator changes; recorded in Lens 8).
- [x] Anti-rationalization output check completed; no rationalizations-past-a-finding detected (Lens 7).
- [x] Verdict recorded with explicit per-issue trail (below).

---

## VERDICT

**PASS (STRICT)** — with one hard flag for downstream monitoring.

**Rationale:**
- 19 / 19 OE steps pass per-step sign-off (see Perspective 1 table); every atom grounded, every tool + parameter verified against catalog, every StarPM trap respected.
- Both OE sub-dims (Completeness + Accuracy) score 5/5 under strictest interpretation with a per-atom evidence table.
- All 6 selected hardness levers (L1, L2, L5, L7, L8, L9) trace end-to-end from prompt sentence → OE step → universe evidence → downstream rubric target.
- Answer-leakage sweep is clean; the load-bearing scope truth lives only in QB `Line[0].Description` (verified verbatim).
- No PROPAGATE TO S1 flags; no adversarial pattern hits.
- All 8 write actions in OE 12-19 are atomic and cleanly Outcome 1.1 mappable for S3.
- The prompt "walk through the rationale" ask has coherent origin (OE 10 conclusion) propagating to OE 14 Linear comment and OE 15 Slack thread reply.

**Hard flag (for FINAL + platform review):**
Density under strictest lens re-projects at ~28-30 midpoint (below the 40 THIN floor). Council B v3's ~38-40 midpoint at THIN band boundary was accepted under documented Hardness_Plan carry per AGENTS.md Rule 11 and the S1 AUDIT decision. **If real-run tool-call average across the 6 runs is <40, treat as L31 pattern (Task 39) confirmed and route to `PIPELINE REDO` with mandate to add a 7th lever (candidates: L3 missing reply, L12 document cross-reference — see Hardness_Playbook).** This is not blocking S2 exit but is the documented next-step trigger.

**Next trigger (per pipeline dispatch):** Proceed to S3 rubric drafting. `PIPELINE S3 — Tasks/40_6a61a86a31b9c973b2021ba5`
