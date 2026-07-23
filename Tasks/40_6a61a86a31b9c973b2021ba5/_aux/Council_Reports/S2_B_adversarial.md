# S2 Council B — Adversarial QC + Density + Hardness Preservation

**Deliverable:** `Tasks/40_6a61a86a31b9c973b2021ba5/6_Oracle_Events.txt`
**Phase:** oe · **Universe:** starpm · **Lens set:** Architect / Implementer / Red-team / Ground-truth / Integration

---

## B1 — QC Sub-Dimension Scoring

`SUB-DIM OE_Completeness -> SCORE 5/3-4-5 -> REASON All 8 required writes covered (Airtable update, Linear save_issue, Linear save_comment, Slack thread reply, 3 Gmail drafts, 1 GCalendar event); every discovery precondition present (contacts before drafts, base+table before Airtable update, list before get for Linear+QB, thread expansion before priority flip, QB line description before every downstream write); dependency chain sound end-to-end.`

`SUB-DIM OE_Accuracy -> SCORE 5/3-4-5 -> REASON All tool names verified against 7_Server_Tools_Details.json; parameter shapes correct (contacts_search_contacts query, hubspot search_crm_objects object_type+query, slack_search_public+slack_read_thread channel_id+message_ts, gmail search_threads+get_thread threadId, airtable list_bases→list_tables_for_base→search_records→update_records_for_table with baseId+tableId+records, linear list_issues/get_issue/save_issue/save_comment, quickbooks search_bills+get-bill, gcalendar create_event with summary+startTime+endTime); expected data values consistent with Hardness Plan injection spec (ticket MT-2026-1327, OPS-231, bill B2026-211/195836274018, Diane thread d1e2f3a4b5c6789a, tenant-relay ts 1782824160.000302); Thursday date correctly resolved to 2026-07-02 from universe today 2026-07-01 America/Chicago; StarPM parameter traps observed (Slack uses "message" not payload, Gmail uses "body" not content, Linear uses "team" not teamId, Gmail is draft-only, slack_send_message NOT slack_send_message_draft explicitly called out in OE 15).`

**Both sub-dims: 5/5 → PASS.**

Minor imprecisions noted (do not knock score below 5, but worth calling out for the CB):
- OE 8, OE 13 use informal `team_id "team_001"` phrasing next to the correct `team "OPS"`. This is descriptive of the universe field name, not the tool parameter — but a strict reader could interpret it as a phantom `team_id` param. Rewording as "team `OPS` (equivalently, team value `team_001`)" would eliminate ambiguity.
- OE 13 tells the agent to `save_issue(id "OPS-231", ...)`. Linear `save_issue.id` accepts the internal id, and passing an identifier string may work depending on server tolerance. If the platform strictly requires the internal issue uuid, the OE should note "use the id returned from get_issue in OE 8". Non-blocking; noted.

---

## B2 — Adversarial Alt-Path Divergences

| # | Divergence | OE coverage | Blocking? |
|---|---|---|---|
| 1 | Agent uses `slack_send_message_draft` in OE 15 instead of `slack_send_message` → tenant-thread post never actually appears | **Covered:** OE 15 explicitly states "Do NOT use slack_send_message_draft, which does not actually post." Rubric will fail the draft path per 5_Prompt requirement. | No |
| 2 | Agent skips OE 10 (`get-bill` line[0].Description) and rides Diane's Gmail summary + Tony's Slack endorsement → all 8 downstream writes lock in the 310-dollar exchanger-only scope | **This is the L2 lever firing correctly**, not an OE gap. The prompt requires the agent to "actually go through Diane's diagnostic write-up on the bill itself" — a rubric will fail the wrong-scope path. Not a divergence to fix in OE; it's the intended stumping vector. | No |
| 3 | Agent reads Carlos's tenant-relay parent (OE 3) but never expands the thread (OE 4) → misses the evening escalation → keeps priority selMedium and tones down owner+tenant drafts | **This is the L5 lever firing correctly.** OE 4 is present and explicit; rubric enforces the priority flip. Not a divergence to fix. | No |
| 4 | Agent posts to `#maintenance` as a top-level message instead of a thread reply on ts `1782824160.000302` | **Covered:** OE 15 explicitly says "Posting into the thread (not a new top-level message) is important..." | No |
| 5 | Agent latches on the resolved Unit 14 (Tommy Reyes / Linda Castillo) water-heater incident and reports the situation as already handled | **This is the L1 lever firing correctly.** OE 3 uses "water heater" as one search variant which will surface the decoys. Not a divergence to fix; it's the intended anchor. | No |
| 6 | Agent uses `contacts_search_contacts` for Robert Finley instead of HubSpot `search_crm_objects` | **Covered:** OE 2 explicitly names both paths as valid ("Alternatively contacts_search_contacts... resolves the same address"). | No |
| 7 | Agent conflates Tony Reyes (Lead Maintenance Technician, authority endorsement) with Tommy Reyes (Unit 14 resolved tenant) due to name overlap | Not an OE-fixable issue; it's incidental hardness thickening from name proximity. No rubric implication. | No |
| 8 | Agent uses OE 9's stated `bill id "195836274018"` directly in `get-bill` without running `search_bills` first (skips the search step) | Both paths satisfy OE 9+10 semantically. Not a divergence. | No |
| 9 | Agent creates the calendar block on wrong day (2026-07-01 today instead of 2026-07-02 Thursday) | OE 19 fixes date `2026-07-02T08:00:00-05:00`. Correct given today is 2026-07-01 Wednesday. Rubric will enforce Thursday. | No |

**No blocking adversarial divergences.** Coverage is tight — the OE explicitly calls out every trap-adjacent alternate path.

---

## B3 — Tool-Call Density Projection

Simulating a competent Opus 4.8 following the OE chain with realistic exploration overhead:

| Bucket | Tool calls | Notes |
|---|---:|---|
| Persona/context (contacts × 2, hubspot × 1) | 3-4 | Tanya, Robert via both contacts and hubspot |
| Slack discovery (list_channels + slack_search_public × 2-3 query variants + slack_read_thread × 2) | 5-7 | Mesa Vista 7B / water heater / Tanya variants + expand tenant-relay parent + read Tony's authority parent |
| L1 latch exploration (Unit 14 slack searches + read Tommy Reyes msgs + read closed timeline) | 4-6 | Natural Opus branch-out when "water heater" search returns Unit 14 hits |
| Gmail (search_threads × 1-2 + get_thread × 1) | 2-3 | Hill Country diagnostic thread + context searches |
| Airtable (list_bases + list_tables_for_base + get_table_schema + search_records) | 3-4 | Full base/table/schema resolution before update |
| Airtable L1 decoy (search MT-2026-1211/1256 Unit 14) | 1-2 | Natural side-search after latching |
| Linear (list_issues query + get_issue + list_issues assignee) | 2-3 | OPS-231 body read + Carlos user lookup |
| QuickBooks (search_bills / list_entities + get-bill) | 2-3 | Filter vendor 201, expand line detail |
| Writes (8) | 8 | Airtable update + Linear save_issue + Linear save_comment + Slack thread reply + Gmail × 3 + GCalendar create_event |
| Verification / retry buffer | 2-4 | Re-reads before writes, schema previews |
| **TOTAL** | **32-44** | |

**Midpoint: ~38-40. Spread: 32-44.**

**Verdict: THIN_DENSITY** (borderline INSUFFICIENT lower edge; midpoint at the 40 gate).

Per AGENTS.md Rule 11 and the tier gate above, THIN_DENSITY is acceptable **only if** `Hardness_Plan.md` documents per-task THIN carry justification. It does:
- `Hardness_Plan.md` §"THIN carry (Council B v3 re-projection, added 2026-07-23)" explicitly documents 49-50 midpoint under strictest per-service accounting and cites the 6-lever selection (over the default 4-5) as the buffer against L31 real-run underflow (Task 39 landed at 35-37 despite 50.5 projection).
- The Hardness Plan's own aggressive-accounting midpoint of 56 sits above my re-projection because it credits more per-service branching per L7 (5+ writes × 3 reads = 15.5 for the multi-write bucket alone).

**My re-projection (~38-40) is at the pessimistic edge and slightly below Council B v3's 49-50, but within a reasonable Opus-variance band and above the 32 absolute floor even in the worst case.** The task carries real Task 39 underflow risk on real platform runs, which is exactly the risk the documented THIN carry acknowledges. **ACCEPT under documented THIN carry.**

Flag for FINAL and platform-review: if this task comes back at <40 tool-call average across the 6 runs, treat as L31-pattern confirmed and route to PIPELINE REDO. Do not accept further THIN carries on this scenario shape without adding a lever.

---

## B4 — Hardness Lever Preservation

| Lever | Fires at OE | Evidence | Status |
|---|---|---|---|
| **L1 Latching** (resolved Unit 14 water-heater decoy) | OE 3 | Search query variants include "water heater" — will surface Unit 14 slack + Tommy Reyes msgs + closed tickets before Mesa Vista 7B hits. L1 latch is realized purely by the natural query variants; no additional OE step needed. | ✅ Preserved |
| **L2 Structured-DB skip on QB Line[0].Description** (LOAD-BEARING) | OE 10 | Explicit `get-bill (id "195836274018")` with instruction to read `Line[0].Description` field and conclude "full unit replacement" scope. This is the load-bearing hop of the L8 chain. | ✅ Preserved |
| **L5 Slack thread-reply blindness** | OE 4 | Explicit `slack_read_thread (channel_id "C001", message_ts "1782824160.000302")` with the expected reply at ts `1782863220.000303` from Carlos flipping priority from Medium to High. | ✅ Preserved |
| **L7 Multi-write diversification** (8 writes / 5 services) | OE 12-19 | 8 writes across Airtable + Linear × 2 + Slack + Gmail × 3 + GCalendar = 5 distinct services. | ✅ Preserved |
| **L8 Multi-link chain** (Slack → Airtable → Linear → QB Line[0].Description) | OE 3-4 → OE 7 → OE 8 → OE 10 | Slack tenant-relay thread expansion → Airtable ticket record `rec92f4a1c8e17bd3` → Linear issue OPS-231 whose body defers to "diagnostic bill on file with vendor id 201" → QB bill line description. 4-hop chain preserved end-to-end. | ✅ Preserved |
| **L9 Authority-figure dismissal** (Tony Reyes) | OE 3 | Search surfaces Tony's C001 parent at ts `1782789240.000301` with narrow-scope endorsement ("heat exchanger swap only, tank tested sound, keeps us on Robert's June budget, sign-off unless flagged"). | ✅ Preserved |

**All 6 selected levers fire.** No HARDNESS_REGRESSION.

Minor strengthening opportunity (non-blocking): OE 3 could add an explicit disposition instruction after L1 surfaces the Unit 14 decoy ("Note the resolved Unit 14 incident from 5/15-5/27 is a separate closed ticket and does not apply to the active Mesa Vista 7B situation") to help the AF-classifier during S4. Currently the OE lets the lever fire naturally without prescribing the discrimination — which is fine for stumping but slightly harder for verifier grading. Optional.

---

## B6 — Upstream Propagation

**No PROPAGATE TO S1 flags.**

The prompt (`5_Prompt.txt`) is:
- Unambiguous on the 8 required writes (each is named or clearly implied in ¶4 + ¶5).
- Clear on the thread-reply requirement ("drop back into the tenant thread I had going").
- Clear on the diagnostic-vs-summary comparison ("actually go through Diane's diagnostic write-up on the bill itself and check whether the detail she has captured lines up with the summary").
- Correctly leaves the answer un-leaked (never states the scope should be full unit replacement; frames Tony's narrow scope as "what he was going to sign off on unless flagged").
- Correctly identifies persona (Carlos), tenant (Tanya), owner (Robert), vendor (Diane at Hill Country), authority (Tony).
- Correctly frames urgency ("close this out today", "Thursday install slot", "Parts need pulling today").

The OE cleanly implements every ask. No prompt-level revision needed.

---

## B8 — OE Completeness Semantic (Dependency Chain Walk)

Walking the prompt's required action graph against the OE chain:

| Required agent step | OE covering it | Dependency ordering |
|---|---|---|
| Resolve Tanya's email for OE 17 | OE 1 | Before OE 17 ✓ |
| Resolve Robert's email for OE 18 | OE 2 | Before OE 18 ✓ |
| Surface Tony's narrow-scope endorsement (context for hardness) | OE 3 | Before OE 10-18 ✓ |
| Surface Carlos's tenant-relay parent | OE 3 | Before OE 4, OE 15 ✓ |
| Expand tenant-relay thread and surface evening escalation | OE 4 | Before OE 12 (priority flip) ✓ |
| Resolve Diane's message id for reply threading in OE 16 | OE 5 | Before OE 16 ✓ |
| Read Hill Country vendor summary (the wrong-scope narrative) | OE 5 | Before OE 10 (so agent can see the mismatch) ✓ |
| Resolve Airtable baseId + tableId for OE 12 | OE 6 | Before OE 12 ✓ |
| Identify the Mesa Vista 7B ticket for OE 12 | OE 7 | Before OE 12 ✓ |
| Identify Linear OPS-231 for OE 13, 14 | OE 8 | Before OE 13, 14 ✓ |
| Identify QB bill id for OE 10 | OE 9 | Before OE 10 ✓ |
| Read QB Line[0].Description (load-bearing scope truth) | OE 10 | Before all writes OE 12-18 (scope drives every message) ✓ |
| Resolve Carlos's Linear user id | OE 11 | Before OE 13 (assignee context) ✓ |
| **Write 1:** Update Airtable ticket priority + scope | OE 12 | ✓ |
| **Write 2:** Update Linear OPS-231 description | OE 13 | ✓ |
| **Write 3:** Post rationale comment to OPS-231 | OE 14 | ✓ |
| **Write 4:** Reply in Slack tenant-relay thread | OE 15 | ✓ (with explicit slack_send_message + thread_ts guidance) |
| **Write 5:** Draft revised confirmation to Diane | OE 16 | ✓ |
| **Write 6:** Draft timing update to Tanya | OE 17 | ✓ |
| **Write 7:** Draft cost heads-up to Robert | OE 18 | ✓ |
| **Write 8:** GCalendar Thursday install block | OE 19 | ✓ (correct date 2026-07-02, correct tz America/Chicago -05:00 CDT) |

**All 8 writes have OE coverage. All discovery preconditions present. Dependency chain sound.**

Discovery-before-write ordering is respected in every dependency: agents cannot successfully execute writes OE 12-18 without first surfacing the correct scope from OE 10. Contact lookups (OE 1, 2, 5) precede their consuming Gmail drafts. Airtable base/table resolution (OE 6) precedes the update (OE 12). Linear issue resolution (OE 8) precedes both Linear writes (OE 13, 14).

---

## B9 — OE Service Mapping (StarPM-inferred)

Inferred StarPM data-type → service mapping per AGENTS.md:

| Data type | Correct StarPM service | OE(s) targeting this data | Mapping correct? |
|---|---|---|---|
| Tenant maintenance ticket (SSOT) | airtable | OE 6, 7, 12 (Maintenance Tickets base) | ✅ |
| Ops tracking issue + rationale | linear | OE 8, 11, 13, 14 (OPS-231) | ✅ |
| Chat / tenant relay / vendor endorsement | slack | OE 3, 4, 15 (#maintenance C001) | ✅ |
| Vendor email (draft-only in StarPM) | gmail | OE 5, 16, 17, 18 | ✅ |
| Vendor bill / financial paperwork | quickbooks | OE 9, 10 (Hill Country bill B2026-211) | ✅ |
| Owner CRM lookup | hubspot | OE 2 (Robert Finley) | ✅ |
| Tenant contact lookup | contacts | OE 1 (Tanya) + OE 2 alt path | ✅ |
| Calendar event block | gcalendar | OE 19 (Thursday install) | ✅ |

**All 8 services map correctly.** No cross-service misrouting.

Verified StarPM parameter traps are observed:
- OE 15: `slack_send_message` (correct — not `slack_send_message_draft`), uses `message` param (not `payload`/`text`)
- OE 16-18: `create_draft` with `body` (not `content`)
- OE 13: `save_issue` with `team` (informal `team_id` alt-phrasing noted but not blocking)
- OE 14: `save_comment(issueId, body)` (correct)
- OE 12: `update_records_for_table` with `baseId`+`tableId`+`records[]` camelCase (correct)
- OE 19: `create_event(summary, startTime, endTime)` (correct)

---

## Final Verdict

**GO.**

- OE Completeness: 5/5
- OE Accuracy: 5/5 (with two minor phrasing notes that do not affect score)
- Adversarial divergences: none blocking (every alt-path is explicitly covered or is intentional lever firing)
- Density: **THIN_DENSITY** at midpoint ~38-40, spread 32-44 — **ACCEPTED under documented THIN carry** in `Hardness_Plan.md` §"THIN carry (Council B v3 re-projection, added 2026-07-23)". Flag for FINAL: monitor for L31 real-run underflow.
- Hardness levers: all 6 preserved (L1, L2, L5, L7, L8, L9)
- Upstream propagation: none
- OE Service Mapping: clean

**Next step:** Proceed to S2 AUDIT (strictest interpretation, 5-only bar, density gate 50+). AUDIT may re-open the THIN density discussion — the THIN carry is documented; the density is at the borderline; AUDIT verdict should stand or route to lever-add.
