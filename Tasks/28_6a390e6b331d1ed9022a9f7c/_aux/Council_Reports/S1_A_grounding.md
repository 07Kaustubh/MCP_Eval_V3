# Council A — Grounding and Convention — S1 Prompt

**Task:** 28_6a390e6b331d1ed9022a9f7c
**Deliverable:** `5_Prompt.txt` (402 words per validator)
**Universe today:** 2026-06-12 (Friday)
**Council:** A (Grounding + Convention)

---

## A1 — Grounding Verification

Field-resolution note: per-task universe files store rows as JSON-encoded strings under `row_data`. Primary key for BL exceptions / reconciliations is `id`, not `exception_id` / `reconciliation_id`. All verifications below decoded `row_data` before lookup.

| # | Claim in prompt | Verified | Evidence (file : record index) |
|---|---|---|---|
| 1 | "$6,328.86 variance" | YES | `blackline.blackline_exceptions:INDEX 12` (id=`exc_a0f77f2a19104e`, financial_impact=6328.86, related_account_id=210000, entity_id=brookfield, related_period_id=brookfield_FP-2026-05). Also referenced in `messaging.messages:INDEX 940 / 973 / 974 / 977`. Overdetermined per Hardness caveat — accepted. |
| 2 | "May FX refresh on AP-external-vendors recon" | YES | `blackline.blackline_reconciliations:INDEX 627` (id=`BL-516B536953DA`, entity_id=brookfield, account_id=210000, period_id=brookfield_FP-2026-05, preparer=anaya.wallace). Recon `name` is null in row but ties match (entity + account + period). |
| 3 | "April close USD/GBP was 0.7191 and May close was 0.7838" | YES | `messaging.messages:INDEX 977` (id=`msg_6f4c8432a047`, conversation_id=conversation_scen_040_recon_currency_refresh_0001): "April close USD/GBP was 0.7191 and May close USD/GBP was 0.7838". |
| 4 | "Acme Research Ltd UK subscription line ... booked at the March invoice-date spot rate" | YES (framing) / NO underlying SAP record (expected, engineered lever) | `messaging.messages:INDEX 973 / 974 / 977` (Anaya's framing). `sap_subledger.ap_invoices` — zero results for `vendor_name LIKE "Acme Research"`, zero for `vendor_id="VEN-441207"`. Confirmed structured-DB skip per Hardness Plan Lever 2. |
| 5 | "workings already up in Vault under the title 'Brookfield May 2026 AP-external-vendors FX variance workings'" | NO (expected, engineered phantom doc) | `records_vault.rv_documents` — zero docs with that title; zero "Brookfield + FX + variance" titled docs. Confirmed phantom-doc lever per Hardness Plan Lever 9(b). |
| 6 | "bd3 lock and bd5 sign-off" passed (period not locked) | YES | `oracle_gl.ogl_fiscal_periods:INDEX 10` (id=`brookfield_FP-2026-05`): status=open, locked_at=null, bd3_lock_at=2026-06-03T14:22:13-04:00 (9 days passed), bd5_close_at=2026-06-05T14:44:59-04:00 (7 days passed). All consistent with "a week past the bd3 lock and the bd5 sign-off". |
| 7 | "Andrea's partner sign-off" — Andrea Phil partner-level | YES | `contacts.contacts:INDEX 7` (contact_id=`contact_eaac7885aa06`, email=andrea.phil@brookfieldcpas.com, job="Partner, Accounting Services", description="Partner over accounting services; final escalation point for big client issues, fees, and service delivery decisions"). Partner role confirmed. |
| 8 | "exception that's been sitting on this recon since the 25th" | YES | `blackline.blackline_exceptions:INDEX 12` identified_at=2026-05-25T12:54:31-04:00, related_reconciliation_id=BL-516B536953DA. Exact ties. |
| 9 | "Ryan" — disposition sitting with Ryan | YES | `blackline.blackline_exceptions:INDEX 12` approver=ryan.delgado@brookfieldcpas.com, state=awaiting_approval. Also `contacts.contacts:INDEX 19` (ryan.delgado). |
| 10 | "Daniel" — copy on email | YES | `contacts.contacts:INDEX 1` (daniel.jones@brookfieldcpas.com). |
| 11 | "Hannah opened the exception" | YES | `blackline.blackline_exceptions:INDEX 12` identified_by=hannah.grant@brookfieldcpas.com. Also `contacts.contacts:INDEX 3`. |
| 12 | "the close channel" | YES | `slack.slack_channels:INDEX 4` (id=C005, name=monthly-close-coordination). Colloquial reference is correct per Brookfield channel map. |
| 13 | "reminder on me from last Friday about chasing the bd3 sign-off backlog" | **PARTIAL MISMATCH — see Issue 1 below** | `reminder.reminders:INDEX 39` (reminder_id=`reminder_scen_011_orphan_exception_0000`, due_datetime=**2026-06-01** (Monday, 11 days ago — NOT last Friday 2026-06-05), title="Disposition BlackLine exception exc_06b89e3937b04a before BD3 lock", description names Anaya as assignee on account 240000 Deferred Revenue, variance $-172.62 — this is a **single-exception** disposition reminder, not a generic "BD3 sign-off backlog" chase). Closest fit; no other Anaya BD3 reminder exists. |

**A1 verdict:** 12 of 13 claims fully verified. 1 of 13 has a temporal + topical mismatch (Item 13). The 2 expected NOT FOUND results (Items 4 and 5) are engineered Hardness levers and are correct as designed.

---

## A2 — Convention Verification

| Rule | Check | Status |
|---|---|---|
| Word count ≤ 500 | 402 words (validator + local recount) | PASS |
| Zero em-dash (U+2014) | 0 occurrences | PASS |
| Zero en-dash (U+2013) | 0 occurrences | PASS |
| No tool / MCP-server names | "Vault" (colloquial, per Task 11 reference precedent), "the close channel" (colloquial Slack), "the GL" (colloquial ledger). No "Slack", "Oracle GL", "BlackLine", "Linear", "Airtable", "SAP", "Records Vault MCP", etc. | PASS |
| No internal IDs | No `BL-...`, `exc_...`, `FP-2026-XX`, `VEN-...`, `apinv_...`, `doc_...`, `issue_...`, `msg_...`, `conv_...` in prompt body. | PASS |
| No "at least N" | None present. | PASS |
| Voice register — trainee Anaya | Deferential markers: "I don't want to step on his sign-off", "ask him to confirm he's happy before I action anything that needs his name on it", "There's a reminder on me from last Friday about chasing the bd3 sign-off backlog that I let slip because I was on this". Concise, professional, owns the work. Matches PersonaBrief (Trainee Accountant). | PASS |
| Opening distinct from V3 references | Closest analog is Task 14 ("It's already the 12th and our own May books still aren't locked"). This prompt opens "My one recon item from Brookfield's May FX refresh is still sitting open and now it's blocking the period lock". Both reference a stuck May close, but Task 14 leads with calendar-date pressure while this leads with a single-owned recon item; framing is sufficiently distinct. | PASS |
| Three movements (Trigger / Context / Asks) | Trigger: recon item blocking period lock. Context: $6,328.86 variance, FX rate refresh, Acme Research line, support file in Vault (engineered claim), BD3/BD5 missed, Andrea's missing sign-off. Asks: stage JE referencing exception, recon notes update, exception note update (no-resolve), formal email to Ryan + CC list, close channel summary, fresh Vault memo, reminder push. | PASS |
| No pre-solving | The FX-catch-up framing is the engineered first-framing trap per Hardness Plan Lever 1 (latching). The agent must self-discover the classification conflict via the BL exception. This is allowed. | PASS |
| Mid-thought entry | Opens in medias res with "My one recon item". | PASS |
| Asymmetric knowledge | Persona names variance, rates, vendor (claimed), support file (claimed), Andrea's sign-off, Ryan's hold — agent must verify and discover the duplicate-classification conflict. | PASS |
| Anti-patterns (validator + format card) | No command list. No tool-name list. No artificial timestamp precision. No "before it blows up". No "loop in" / "CC our CEO" cliché. "Copy Daniel and Andrea" is natural CC phrasing. | PASS |

**A2 verdict:** Zero convention drift. PASS on every convention rule.

---

## Issues

### Issue 1 — Grounding: "reminder on me from last Friday about chasing the bd3 sign-off backlog" doesn't match the only fitting reminder

**Location:** Final paragraph of prompt: "And one last thing. There's a reminder on me from last Friday about chasing the bd3 sign-off backlog that I let slip because I was on this. Push it out to tomorrow so I actually get to it before close."

**What the data shows:** `reminder.reminders:INDEX 39` is the ONLY BD3-flavored reminder where Anaya Wallace is named as the assignee.
- due_datetime: **2026-06-01** (Monday) — universe today is 2026-06-12 (Friday), so "last Friday" would be **2026-06-05**. The reminder is 11 days overdue, not 7.
- title: "Disposition BlackLine exception exc_06b89e3937b04a before BD3 lock" — a **single-exception** disposition reminder on account 240000 (Deferred Revenue - Client Retainers), variance $-172.62. Not a generic "BD3 sign-off backlog" chase.

**Why this fails strict grounding:** Council A's bar is "zero ungrounded claims." "Last Friday" is a concrete temporal claim (resolves to 2026-06-05) and does not verify. The topic ("chasing the bd3 sign-off backlog") implies a multi-item backlog, while the only fitting reminder is about one specific exception. A reader inspecting the prompt against the reminders table sees the mismatch immediately.

**Why it's only PARTIAL (not catastrophic):** Reminder 39 is uniquely identifiable as Anaya's only BD3-tagged reminder. The agent will find it regardless of framing. The lever (reminder reset write action) still fires. But the prompt is technically describing a reminder that does not exist.

**Suggested fix (smallest change):** Either soften the temporal anchor or align the topic to the data.

Option A (soften the date):
> "And one last thing. There's an overdue reminder on me about clearing one of my BlackLine dispositions before this period's lock that I let slip because I was on this. Push it out to tomorrow so I actually get to it before close."

Option B (align topic, keep date loose):
> "And one last thing. There's a reminder on me from earlier this month about a BD3 disposition I owe on another exception that I let slip because I was on this. Push it out to tomorrow so I actually get to it before close."

Either restoration grounds the claim against `reminder.reminders:INDEX 39` cleanly while preserving the diversification write action.

---

## Verdict

**BLOCK** — 1 issue: Issue 1 (reminder claim "from last Friday about chasing the bd3 sign-off backlog" doesn't match `reminder.reminders:INDEX 39` on date or topic).

All other 12 concrete claims verify. All convention rules PASS. Apply Option A or Option B to Issue 1 and the prompt clears Council A.

**Engineered NOT-FOUND items (Items 4 phantom SAP invoice and 5 phantom Vault doc) are correct as designed per Hardness Plan Levers 2 and 9(b) — not blockers.**

---

## Re-review round 2

**Trigger:** S1 revise applied to address Issue 1 (BD3 reminder grounding). Revised final paragraph:

> "And one last thing. There's a reminder on me about dispositioning one of my open May exceptions before bd3 that I let slip because I was on this. Push it out to tomorrow so I actually get to it before close. Thanks."

### Targeted re-verification

| Check | Result |
|---|---|
| Phrase grounds against `reminder.reminders:INDEX 39` | YES |
| "one of my open May exceptions" → reminder is about a single exception (`exc_06b89e3937b04a`), period `brookfield_FP-2026-05` (May), state `investigating` (open). Anaya named as assignee in description. | YES |
| "before bd3" → reminder title is "Disposition BlackLine exception exc_06b89e3937b04a before BD3 lock"; exact wording match. | YES |
| Temporal anchor consistency | PASS — no specific date claim ("last Friday") in revised text; "I let slip because I was on this" naturally explains why BD3 (lock_at 2026-06-03, 9 days ago) has already passed without action. |
| "Backlog" plural-implication removed | YES — "one of my open May exceptions" correctly signals a single exception. |
| Reminder still uniquely identifiable | YES — only Anaya-owned BD3-tagged reminder; no ambiguity for the agent's reminder-reset write action. |

### Convention re-scan

| Rule | Round 2 result |
|---|---|
| Word count | 403 (≤ 500). +1 from round 1's 402; expected delta from revised sentence. PASS |
| Em-dash (U+2014) | 0. PASS |
| En-dash (U+2013) | 0. PASS |
| New tool / MCP names introduced | None. PASS |
| New internal IDs introduced | None. "bd3" is colloquial book-close vocabulary already cleared in round 1 ("bd3 lock and bd5 sign-off"). PASS |
| Opening change | None — opening unchanged from round 1, still distinct from Task 14's "It's already the 12th and our own May books still aren't locked". PASS |
| Voice register | Unchanged — trainee Anaya admitting a slip, deferring on the disposition. PASS |
| Anti-patterns | None introduced. PASS |

### Round 2 verdict

**GO** — Issue 1 cleanly resolved. Revised reminder claim grounds against `reminder.reminders:INDEX 39` (reminder_id `reminder_scen_011_orphan_exception_0000`) on topic, ownership, and BD3 framing. No convention drift introduced. All 13 of 13 concrete claims now verify (2 engineered NOT-FOUND items remain correct as designed per Hardness Plan Levers 2 and 9(b)).

Council A clears the prompt to proceed to Council B.

---

## Re-review round 3

**Trigger:** AUDIT_prompt.md REVISE verdict on THIN_DENSITY. Path A applied: paragraph 5 (Vault memo ask) extended to motivate L8 Hop D SAP query by asking the agent to "pull the underlying invoice line into it so anyone reviewing can retrace the figure end to end."

**Revised paragraph 5:**
> "I also need a fresh memo filed in Vault on the corrective itself, covering the entry's reasoning, the rate sources, and who reviewed, and pull the underlying invoice line into it so anyone reviewing can retrace the figure end to end. Tag it the way journal-entry support memos normally go."

### Delta verification

| # | Check | Result |
|---|---|---|
| 1 | Word count ≤ 500 | **421** by local `len(text.split())` (validator reports 419 — 2-word tokenization delta, likely from hyphen-compound handling; both well under 500). PASS |
| 2 | "the underlying invoice line" — new ungrounded claim? | **NO new claim.** Phrasing is intentionally underspecified (no vendor field, no internal ID, no `vendor_id`, no `invoice_number`). It is a natural follow-up to the existing "Acme Research Ltd UK subscription line" framing in paragraph 1, which Council A round 1 already verified as the engineered Lever 2 structured-DB skip. **SAP absence re-confirmed:** `sap_subledger.ap_invoices` (n=987) — 0 hits on `vendor_name LIKE "Acme Research"`, 0 hits on `vendor_id="VEN-441207"`, 0 hits on `entity_id="brookfield" + currency="GBP"`, 0 hits on `amount=6328.86`. Engineered design intact — agent who attempts the L8 Hop D SAP query returns ZERO results. PASS |
| 3 | Convention re-scan | Em-dash 0, en-dash 0. No new tool names introduced (Vault already cleared as colloquial). No new internal IDs. No pre-solving (request frames the work as "retrace the figure", not "verify against the SAP invoice number" or "confirm the rate calculation"). PASS |
| 4 | Voice register | Still trainee Anaya, deferential, audit-trail-conscious. The added clause "so anyone reviewing can retrace the figure end to end" is consistent with her in-prompt concern for the next reviewer ("the next person picking it up doesn't have to retrace" earlier in paragraph 3). Voice intact. PASS |
| 5 | New escape-valve clause? | **NO.** Added wording asks the agent to "pull the underlying invoice line into it so anyone reviewing can **retrace the figure end to end**." Diction is "retrace" (memo-completeness framing), not "verify" / "check" / "confirm" / "flag if anything looks off". The clause does NOT invite the agent to question Anaya's $6,328.86 / FX-catch-up framing — it asks for a trace artifact, not a correctness check. L29 escape-valve compliance preserved. PASS |

### Round 3 verdict

**GO** — Paragraph 5 delta cleanly motivates L8 Hop D without:
- Introducing any new ungrounded claim (the absence is the engineered signal per Lever 2),
- Violating any convention,
- Drifting from Anaya's trainee voice,
- Planting an escape valve that would let the agent step out of the first-framing trap.

The engineered NOT-FOUND signal is now strengthened by the ask: the agent who attempts the SAP query against the (claimed) "underlying invoice line" returns zero results and must reason from that absence, which is exactly the Hardness Plan's intended kill on Lever 8 Hop D + Lever 2.

All 13 of 13 concrete claims still ground. 2 engineered NOT-FOUND items (phantom Vault doc + phantom SAP invoice line) continue to fire as designed. Council A clears the round-3 revised prompt to proceed.
