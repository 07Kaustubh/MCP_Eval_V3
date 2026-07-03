# AUDIT OE (STRICTEST) — Task 37 (on-demand, fresh chat)

**Universe:** keystone · **Trigger:** `PIPELINE AUDIT --phase all` (pre-upload sanity gate)
**Artifact:** `6_Oracle_Events.txt` (26 OEs — UNCHANGED from candidate submission)
**Baseline priors:** `AUDIT_oe_original.md`, `REVIEW_FINAL.md`, `FINAL_materialize.md` all PASS (STRICT). Independently re-derived here with landmine re-verification.

## Programmatic floor (inherited)
- `validate.py --phase oe` = **PASS** (0 fails · 1 warn [OE 10 CRM/loans false positive] · 3 notes)
- `verify_universe_atoms.py` = **PASS** (41/41 atoms grounded)
- `test_regression_anchors.py` = **48/48 PASS**

## LENS 1 — Strict QC scoring (Docs/7_QC_Spec_Doc1.json)

Per-atom evidence table (v18 mandate). Every OE atom claim traced to universe source.

| OE # | Key atom(s) | Universe source | Verified |
|---|---|---|---|
| 1 | Sofia Reyes login (email sofia.reyes@keystonemortgage.com) | `mortgage_los.staff` row `los_staff_afc9caafae9d` (verified: name="Sofia Reyes", role="processor", is_active=True) | ✅ |
| 2 | 26 active loans across 5 statuses (1 app / 10 proc / 5 UW / 8 CA / 2 CTC); assigned_to=Sofia's staff_id | `mortgage_los.loans` filtered on `assigned_processor=los_staff_afc9caafae9d AND status IN active` → 26 rows in exactly this status distribution | ✅ |
| 3 | Specific loan atoms (LN-2026-00184 processing $340k Carlos; LN-2026-00008 CA $276.4k Derek; LN-2026-00010 processing $519.2k Natasha; LN-2026-00613 CA $433k Priya; LN-2026-00623 CTC $467k Priya; all locks < 2026-04-28) | `mortgage_los.loans` records — verified individually via grep against split file. Every named loan number + status + amount + LO + rate_lock_expiration matches | ✅ |
| 4 | Aggregate `mortgage_los_get_compliance_alerts` returns all 26 lock-expired | Tool catalog `6_Server_Tools_Details.json` confirms this returns compliance alerts across the portfolio; universe seed = 26 expired locks | ✅ |
| 5 | LN-2026-00008 has 3 conditions (2 outstanding prior_to_docs + prior_to_closing; 1 cleared); amount $291,000 in condition text | `mortgage_los.conditions` filtered on `loan_id=<LN-2026-00008.id>` → 3 rows exactly (2 outstanding, 1 cleared, verbatim text matches) | ✅ |
| 6 | 8 loans w/ required docs totaling 26 items; specific counts per loan (LN-2026-00010=7, LN-2026-00623=5, LN-2026-00627=4, LN-2026-00625=3, LN-2026-00376=3, LN-2026-00008=2, LN-2026-00611=1, LN-2026-00196=1) | `mortgage_los.document_checklist_items status=required` grouped by loan → 8 loans, sum 26. Each per-loan count matches | ✅ |
| 7 | Veronica Hayes inactive (term 2025-09-30) on 4 loans; Brian Mitchell inactive (term 2025-04-15) on 1 loan; total 5 loans | `mortgage_los.staff` row `los_staff_06b484d01f94` (is_active=False, term 2025-09-30) + `los_staff_6d606f7506a7` (is_active=False, term 2025-04-15) — verified. Loans join count: 4 + 1 = 5 | ✅ |
| 8 | Email counts per loan (LN-2024-00123=11, LN-2024-00125=15, LN-2026-00008=4, LN-2026-00010=3, LN-2026-00632=2, LN-2026-00611=3, LN-2026-00613=1) | `email.emails` grep by loan number substring | ✅ |
| 9 | Slack msg counts per loan (LN-2026-00184=9, LN-2026-00613=6, LN-2026-00010=6, LN-2026-00627=6, LN-2024-00123=6, LN-2026-00632=4, LN-2026-00623=4, LN-2026-00625=4, LN-2026-00611=2) | `slack.slack_messages` grep by loan number substring | ✅ |
| 10 | CRM engagement counts (LN-2026-00008=3, LN-2026-00010=2) | `crm.crm_engagements` grep by loan number substring: LN-2026-00008=3 hits, LN-2026-00010=2 hits (verified) | ✅ |
| 11 | Slack channel C002 = #loan-processing | `slack.slack_channels` C002 confirmed in service_inventory | ✅ |
| 12 | 8 LO contact emails + 4 escalation contact emails (Carlos, Derek, Keisha, Amy, Marcus, Natasha, James, Priya; Camille, Grace, Elena, Denise) | `mortgage_los.staff` — every named email/name pair verified. Marcus Webb specifically confirmed `is_active=True, role=loan_officer, email=marcus.webb@keystonemortgage.com` (see LENS 5 landmine) | ✅ |
| 13-20 | Per-LO email content atoms (each LO's 2-4 loans; status/amount/lock/lender for each) | Each atom cross-checked against `mortgage_los.loans` filtered on that LO. 8 LOs × 2-4 loans each. All atoms match records verbatim | ✅ |
| 21 | Camille lock summary: 26 loans, all expired; most-recent expirations (LN-2026-00010 4d, LN-2026-00627 11d, LN-2026-00613 14d, LN-2026-00625 17d, LN-2026-00611 18d ago from 2026-04-28) | Date arithmetic against `rate_lock_expiration`: 2026-04-28 − 2026-04-24 = 4d ✅; − 2026-04-17 = 11d ✅; − 2026-04-14 = 14d ✅; − 2026-04-11 = 17d ✅; − 2026-04-10 = 18d ✅ | ✅ |
| 22 | Grace pipeline report: 5 status breakdown; 5 terminated-LO loans (Veronica × 4 loans named + Brian × 1 loan named); 26 outstanding docs across 8 loans | Verified via LENS 1 rows 2, 6, 7 | ✅ |
| 23 | Post to C002 payload param | Tool catalog: `conversations_add_message(channel_id, payload)` — `payload` is correct param (v18/v20 KeyStone note: NOT `text`) | ✅ |
| 24 | `mortgage_los_add_activity(loan_id, action, detail)` on problem loans | Tool catalog verified: parameters match | ✅ |
| 25 | `crm_create_engagement(engagement_type, body, contact_ids)` | Tool catalog verified: `crm_create_engagement(contact_ids, engagement_type, body)` — required params match | ✅ |
| 26 | Compliance concerns: LN-2026-00008 + LN-2026-00010 phishing scope, LN-2026-00613 TRID redisclosure, terminated-LO gap | Slack C004 (Denise ts=1775572140 verbatim names LN-2026-00522/00008/00010/00009); Slack C002 (LN-2026-00613 30yr→15yr, missing revised LE); LENS 1 row 7 | ✅ |

**Sub-dim scores (strictest 5/5-only bar):**

| Sub-dim | Score | Note |
|---|---|---|
| Coverage (all lever-load-bearing actions have OEs) | **5** | 26 OEs cover: login, pipeline discovery, per-loan detail, compliance-alerts aggregate, conditions per LN-00008, doc-checklist per loan, staff-status check, email/Slack/CRM investigation, contact resolution, 8 LO emails, 3 escalation emails, Slack post, activity notes, CRM engagements, compliance escalation |
| Groundedness (all atoms trace) | **5** | 41/41 verify_universe_atoms PASS; LENS 1 table above re-derives each |
| Lifecycle preconditions | **5** | OE 1 (login) → OE 2 (pipeline) → OE 3-6 (per-loan detail, requires loan_id from OE 2) → OE 7 (staff, requires assigned_lo from OE 2) → OE 12 (contact resolution before send-email fan-out) → OE 13-20 (per-LO email, requires resolved contact) → OE 21-22 (aggregate emails) → OE 23-25 (writes) → OE 26 (conditional compliance escalation). Correct dependency order |
| Tool-name specificity (MANDATORY in OEs) | **5** | Every OE names the exact MCP tool with `_service_action` form: `mortgage_los_login`, `mortgage_los_get_pipeline`, `mortgage_los_get_loan`, `mortgage_los_get_compliance_alerts`, `mortgage_los_get_conditions`, `mortgage_los_get_outstanding_documents`, `mortgage_los_list_staff`, `email_search_emails`, `slack_conversations_search_messages`, `crm_search_deals`, `crm_list_engagements`, `channels_list`, `contacts_search_contacts`, `email_send_email`, `slack_conversations_add_message`, `mortgage_los_add_activity`, `crm_create_engagement` |
| Parameter accuracy (KeyStone traps) | **5** | Email `content` (not `body`) — OE 13-22 use `content` correctly ✅ · Slack `payload` (not `text`) — OE 23 uses `payload` ✅ · CRM `crm_create_engagement` uses `engagement_type`/`body`/`contact_ids` — OE 25 correct ✅ · `mortgage_los_add_activity(loan_id, action, detail)` — OE 24 correct ✅ |

**LENS 1 verdict: PASS (STRICT) — every applicable sub-dim = 5/5.**

## LENS 2 — Answer-leakage sweep

The OE file is the SOLUTION BLUEPRINT and is expected to contain full atom detail; leakage sweep here targets whether the OE surfaces the answer via a single-shot aggregate that would make the discovery trivial in trajectory.

**Aggregate tool audit (the strictest concern per task charter):**

- OE 4 mentions `mortgage_los_get_compliance_alerts (no parameters)` as an "Additionally or alternatively" path.
- OE 6 mentions `mortgage_los_get_outstanding_documents(assigned_to)` as an assigned-to filter.

Under strictest lens: does availability collapse hardness? MEASURED answer (3 trajectory spot-checks):

| Run | compliance_alerts called? | get_pipeline aggregate? | Total tool calls | Difficulty |
|---|---|---|---|---|
| 1 | Yes (1×) | Yes (1×) | 89 | 28/30 PASS |
| 3 | No | Yes (1×) | 338 | 28/30 PASS |
| 5 | Yes (1×) | Yes (2×) | 226 | 28/30 PASS |

Aggregate calls appear (4/6 runs use compliance_alerts) but they do NOT collapse density (avg 216.8) or difficulty (33.3% pass@1). The aggregate tools return the *fact* that locks are expired but agents still need per-loan iteration for status/amount/LO/blocker/email/Slack synthesis for each rubric bundle. Hardness is preserved.

**LENS 2 verdict: PASS (STRICT). Aggregate tools are legitimate discovery shortcuts, not answer leakage.**

## LENS 3 — Hardness end-to-end trace (from REVIEW_hardness.md)

| # | Lever | OE anchor(s) |
|---|---|---|
| 1 | 26 active loans | OE 2 |
| 2 | All 26 locks expired | OE 3, OE 4 |
| 3 | 5 terminated-LO loans | OE 7 (names Veronica × 4 loans, Brian × 1 loan verbatim) |
| 4 | 26 outstanding docs across 8 loans | OE 6 (names all 8 loans + counts) |
| 5 | UWM/Keisha phishing scope | OE 8 (email search), OE 9 (Slack search — C004 relevant), OE 26 (explicit "phishing compromise scenario associated with LN-2026-00008 and LN-2026-00010") |
| 6 | LN-2026-00613 TRID redisclosure | OE 26 ("TRID redisclosure concern on LN-2026-00613 from the 30yr-to-15yr switch") |
| 7 | LN-2026-00623 CTC anomaly | OE 6 (5 required docs on LN-2026-00623), OE 20 (Priya email — CTC + 5 docs specific) |
| 8 | LN-2026-00010 max-docs | OE 6 (7 required docs on LN-2026-00010), OE 18 (Natasha email — 7 docs specific) |

All 8 levers have direct OE anchors. **PASS (STRICT).**

## LENS 4 — Density projection

Measured 216.8 avg. OE cardinality = 26 (18 discovery + 8 write actions). Per-OE expected tool calls: OE 2 (1) + OE 3 (up to 26) + OE 4 (1-2) + OE 5 (1) + OE 6 (1-8) + OE 7 (1) + OE 8-10 (multi-search) + OE 12 (12) + OE 13-22 (10 sends) + OE 23-26 (Slack + notes + engagement + escalation). Sum trivially exceeds 50+ design. Measured confirms 216.8. **PASS (STRICT).**

## LENS 5 — Adversarial veteran review

**Landmine #1 — Marcus Webb (departed-employee trap per AGENTS.md v20 KeyStone base scenario_7da8f37a).**
Direct query: `mortgage_los.staff` row `los_staff_a583f044387a` = `{name: "Marcus Webb", role: "loan_officer", is_active: True, termination_date: None, email: "marcus.webb@keystonemortgage.com"}`. **This per-task universe has swapped Marcus to ACTIVE.** OE 17 (Marcus email) is FINE — not writing to a departed employee. Rubrics [14] + [15] emailing Marcus are FINE. No blocker.

**Landmine #2 — CRM/loans linkage (OE 10 validator WARN).**
Prior audit dismissed as false positive. Re-verified: `crm.crm_deals.dealname` — 80/80 deals contain `LN-YYYY-NNNNN` pattern in dealname (verbatim examples: "VA - Vincent Foster (LN-2024-00005)"). OE 10's `crm_search_deals(dealname: loan numbers or borrower names)` is a valid, indexed query path. CRM engagements: LN-2026-00008 = 3 engagement hits, LN-2026-00010 = 2 engagement hits — matches OE 10's expected discovery verbatim. WARN confirmed **false positive**.

**Landmine #3 — Airtable vs CRM source-of-truth trap.** N/A (KeyStone; that's a MoveOps landmine).

**Landmine #4 — Account-number trap.** N/A (KeyStone loan-based universe, not GL-based).

Other adversarial checks:

| Anti-pattern | Present? | Note |
|---|---|---|
| Method-lock in OE (over-specifying communication channel) | ❌ | OE 21-22 use email because the deliverable is email; OE 23 uses Slack because prompt says "processing channel". Both prompt-inherent |
| Persona-scope violation | ❌ | Sofia = processor writing on her own pipeline; Elena/Denise = valid escalation contacts (staff row confirmed) |
| Tool-name typo / wrong service | ❌ | All 17+ MCP tools name-matched against `Mortgage_Base_Universe/6_Server_Tools_Details.json` |
| Em-dashes | ❌ | 0 |
| "At least N" in OE | Present in OE 3 ("at least the most recent and highest-priority ones"), OE 24 ("at minimum the most problematic files") | ✅ acceptable — OEs are internal artifacts (not rubric titles); "at least" is descriptive language for the audit trail, not a hard rubric floor |
| Entity drift | ❌ | 8 LOs + 4 escalation contacts all confirmed in staff |
| Wrong param name | ❌ | Email `content` correct; Slack `payload` correct; CRM `body`/`engagement_type`/`contact_ids` correct; `mortgage_los_add_activity(loan_id, action, detail)` correct |

**LENS 5 verdict: PASS (STRICT).**

## LENS 6 — RETIRED in v18 (merged into LENS 1 per-atom evidence table).

## LENS 7 — Anti-rationalization pass

1. **OE 4 aggregate `compliance_alerts` — could this be answer leakage?** Considered flagging as "hardness collapse" but MEASURED trajectory data shows 216.8 avg tool calls and 33.3% pass@1 — hardness is preserved. Aggregate tools return the *fact* of expiration but not the per-loan synthesis that rubrics demand. Not rationalization.

2. **OE 10 CRM/loans WARN — could linkage be broken?** Directly queried `crm.crm_deals` → 80/80 have LN- pattern in dealname; `crm.crm_engagements` → LN-2026-00008=3, LN-2026-00010=2. WARN is a false positive from the validator heuristic. Not rationalization.

3. **OE 17 emails Marcus Webb — is Marcus active in this universe?** Directly queried staff row → `is_active=True`. Per-task swap from base scenario. Not rationalization.

4. **OE 26 conditional compliance escalation — could this be a rubric-side rationalization?** OE 26 is an OE, not a rubric; it names 3 latent findings (phishing scope / TRID / terminated-LO gap) that surface via investigation. Universe evidence confirms all 3 (Slack C004 verbatim, Slack C002 verbatim, staff.is_active=False × loans join). Not rationalization.

**LENS 7 verdict: No suppressed findings.**

## LENS 8 — Regression anchor verification

`test_regression_anchors.py` → **48/48 PASS** (inherited).

## LENS 9 — RETIRED in v18.

## Final verdict

**OE: PASS (STRICT)**

One-line summary: All 26 OEs' atoms trace to real universe records (41/41 verify_universe_atoms PASS); Marcus Webb landmine confirmed inert (per-task swap to active); OE 10 CRM/loans WARN confirmed false positive by direct query (80/80 CRM deals have loan-number in dealname); aggregate tools do NOT collapse hardness (216.8 avg tool calls, 33.3% pass@1 measured); every parameter name matches KeyStone v20 tool-catalog conventions.
