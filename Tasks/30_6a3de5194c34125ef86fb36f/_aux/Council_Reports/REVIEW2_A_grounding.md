# Council A — Grounding + Convention (REVIEW2)

**Task:** `Tasks/30_6a3de5194c34125ef86fb36f/`
**Materialization under review:** `_aux/Scratch_Corrected/{5_Prompt.txt, 6_Oracle_Events.txt, 7_Rubrics.json, 2_Persona.txt, 1_Business_Function.txt}`
**Auditor stance:** Read-only. Strict-veteran lens.
**Prior phase verdicts:** AUDIT_prompt.md / AUDIT_oe.md / AUDIT_rubrics.md = **PASS (STRICT)** on each.

---

## A1 — Grounding sweep

Every concrete claim in the prompt, OEs, and rubrics was traced back to a per-task universe row in `_aux/Universe_Split/`. Enumerated below.

### A1.1 — Personas (5/5 confirmed)

| Claim | Universe location | Status |
|---|---|---|
| Marina Soko / marina.soko@brookfieldcpas.com / Compliance Officer | `slack.slack_users.json` → `persona_005`; persona alignment in `2_Persona.txt` matches | GROUNDED |
| Matthew Li / matthew.li@brookfieldcpas.com | `slack.slack_users.json` → `persona_023` (real_name "Matthew Li", is_admin=true) | GROUNDED |
| Steven Perry / steven.perry@brookfieldcpas.com | `slack.slack_users.json` → `persona_024` (real_name "Steven Perry", is_admin=true) | GROUNDED |
| Anita Knowles / anita.knowles@brookfieldcpas.com | `slack.slack_users.json` → `npc_018` (real_name "Anita Knowles") | GROUNDED |
| Farah Dlamini / farah.dlamini@brookfieldcpas.com | `slack.slack_users.json` → `npc_026` (real_name "Farah Dlamini") | GROUNDED |

Cross-validated against `email.emails.json` clearance chain (email IDs `email_scen_041_audit_compliance_0008/0009/0010`): Marina → Anita supervisory clearance request → Steven partner sign-off, CC Farah + Matthew. All addresses match.

### A1.2 — Journal entry (DR/CR/amount/date)

| Claim | Universe location | Status |
|---|---|---|
| JE-acme_cloud-FP-2026-04-0052 / `je_b2c2b939a1244823` | `oracle_gl.ogl_journal_entries.json` (entry_number + id match) | GROUNDED |
| DR 101000 Cash - Operating $57,077.69 | line_number=1, debit=57077.69, account_number=101000 | GROUNDED |
| CR 110000 AR - Trade $57,077.69 | line_number=2, credit=57077.69, account_number=110000 | GROUNDED |
| posting_date 2026-04-22 | posted_at "2026-04-22T13:42:57-04:00", status=posted | GROUNDED |
| entity_id `acme_cloud`, source_module AR | matches | GROUNDED |
| period_id `acme_cloud_FP-2026-04` | matches; period itself confirmed in `oracle_gl.ogl_fiscal_periods.json` (status=closed, locked 2026-05-05) | GROUNDED |

### A1.3 — Reminder

| Claim | Universe location | Status |
|---|---|---|
| reminder_id `reminder_scen_041_audit_compliance_0000` | `reminder.reminders.json` (exact id match) | GROUNDED |
| Title "Review AML threshold alert for JE-acme_cloud-FP-2026-04-0052" | matches | GROUNDED |
| Overdue vs. universe today 2026-06-12 | due_datetime 2026-05-02T01:00:00+00:00 → ≥41 days overdue | GROUNDED |
| Description references Marina, account 101000, period acme_cloud_FP-2026-04, Anita supervisory gate | matches | GROUNDED |

Note: OE03 says "due 2026-05-02" — the underlying due_datetime is 2026-05-02 UTC (= 2026-05-01 21:00 EDT). Either rendering is acceptable; the "overdue" claim holds in all timezones because universe today is 2026-06-12.

### A1.4 — Slack channel + thread

| Claim | Universe location | Status |
|---|---|---|
| C008 = `#compliance-and-registrations` | `slack.slack_channels.json` (id=C008, name=compliance-and-registrations, is_archived=false, members include persona_005, persona_023, persona_024, npc_018, npc_026) | GROUNDED |
| thread_ts `1776969000.000000` | `slack.slack_messages.json` (ts=1776969000.000000, channel_id=C008, user_id=persona_005, text opens AML case thread for JE-acme_cloud-FP-2026-04-0052, thread_parent_id=null → root of the case thread) | GROUNDED |
| Existing case-thread replies (Farah analyst findings, Marina case-thread closure) | Two child messages with thread_ts_legacy=1776969000.000000 confirmed | GROUNDED |

### A1.5 — Period id

`acme_cloud_FP-2026-04` confirmed in `oracle_gl.ogl_fiscal_periods.json` (fiscal_year=2026, fiscal_quarter=2, status=closed). GROUNDED.

### A1.6 — Retention + classification enums

| Claim | Universe location | Status |
|---|---|---|
| `AICPA_SQMS_7Y` retention code | `records_vault.rv_retention_policies.json` (entity_id=brookfield, retention_years=7, regulatory_basis "AICPA SQMS 1") | GROUNDED |
| `restricted` classification | `records_vault.rv_classifications.json` (requires_elevated_role=true) | GROUNDED |

Both match the AGENTS.md allowed enums (retention: AICPA_SQMS_7Y / IRS_TAX_7Y / FIRM_INTERNAL / INDEFINITE; classification: internal / restricted / public).

### A1.7 — Absence of disposition memo (documentation gap)

Searched `records_vault.rv_documents.json` for any document whose title or related_resource_id ties to JE-acme_cloud-FP-2026-04-0052 / je_b2c2b939a1244823 / "wire-monitoring" / "disposition" / "CDD clearance":

- `doc_38a8236a0c4546e2` — "Acme Cloud FY2026 AML Risk Assessment Memo" (annual risk assessment, not a per-JE disposition)
- `doc_fb028c9124e146c5` — "Acme Cloud FY2026 Beneficial Owner Refresh" (BO refresh, not a disposition)
- No document with kind=memo references this JE or the wire-monitoring clearance.

OE05's framing — "Existing AML-related documents found (BO refresh, risk assessment) but no disposition memo specific to this wire-monitoring clearance" — is **GROUNDED** as a real gap.

### A1.8 — CDD clearance trail referenced in OE02

Triangulated against `email.emails.json`:

- `email_scen_041_audit_compliance_0008` (2026-04-28) — Marina → Anita with package + recommends CLEAR
- `email_scen_041_audit_compliance_0009` (2026-04-29) — Anita supervisory sign-off → loops Steven
- `email_scen_041_audit_compliance_0010` (2026-04-30) — Steven partner clearance, no SAR

Slack analyst posting (Farah's findings, ts 1777318800.000000) confirmed in `slack.slack_messages.json`. Full four-stage clearance chain (analyst → coordinator → supervisor → partner) is grounded.

### A1.9 — Tool enumeration

All 10 tool names called in OE01–OE08 verified against `Brookfield_Base_Universe/8_Server_Tools_Details.json`:

`oracle_gl_list_journal_entries`, `oracle_gl_get_journal_entry`, `email_search_emails`, `slack_conversations_search_messages`, `reminder_get_all_reminders`, `reminder_delete_reminder`, `records_vault_list_documents`, `records_vault_upload_document`, `slack_conversations_add_message`, `email_send_email` — **ALL PRESENT**.

### A1 verdict

**A1: GO.** Zero ungrounded claims across prompt, OEs, and rubrics.

---

## A2 — Convention sweep

Compared against `Reference/Prompt_Format.md`, `Reference/OE_Format.md`, `Reference/Rubric_Format.md`, `Reference/Strict_Convention_Inventory.json`, `Reference/OE_Convention_Inventory.json`, and the V3 reference tasks (Task11–Task14).

### A2.1 — Prompt

| Check | Result |
|---|---|
| Word count ≤ 500 | 209 words. PASS. |
| Em-dashes | 0. PASS. |
| "At least N" without mandate | None. PASS. |
| Tool names in prompt | None (refers to "ledger entry", "reminders", "#compliance-and-registrations", "Records Vault" — concepts, not function names). PASS. |
| First-person persona voice | "I'm doing a sweep of our open compliance monitoring items…" — first person, Compliance Officer voice. PASS. |
| Multi-service spread | GL + email + Slack + reminders + Records Vault. PASS. |
| Internal IDs in user-facing text | None. The JE id, reminder id, and thread ts are absent from the prompt; the agent must discover them via tool calls. PASS. |

### A2.2 — Oracle events

| Check | Result |
|---|---|
| Action-first opening verbs | OE01 Get / OE02 Search / OE03 List / OE04 Delete / OE05 List / OE06 Upload / OE07 Post / OE08 Send. All action-first per V3 reference task convention. PASS. |
| Validator whitelist gap | Validator WARN flagged 0/8 against its narrow recognized-verb list. **Informational only** — verbs match the V3 reference family (e.g., Task11/Task12 OEs use "List", "Get", "Search", "Send", "Post"). Recommend widening the validator whitelist in a separate housekeeping PR; not a blocker for this task. |
| Numbered-prose format | OE01–OE08 with Tool / Parameters / Target Data fields populated. PASS. |
| Parameter trap-list — Slack `payload` (not `text`) | OE07 uses `payload`. PASS. |
| Parameter trap-list — email `content` (not `body`) | OE08 uses `content` per AGENTS.md trap-list; the email_send_email parameter naming convention is honored. PASS. |
| No fictitious tool names | All 10 verified against `8_Server_Tools_Details.json`. PASS. |
| OE-to-rubric coverage | Each of the 24 rubrics traces to ≥1 OE (cross-check matches AUDIT_oe.md row 1). PASS. |
| Step density | 8 OEs covering 10+ atomic calls (OE01 chains list→get; OE05+OE06 chains list→upload; OE03+OE04 chains list→delete; OE02 chains email_search + slack_conversations_search). Step-count vs. density floor satisfied per AUDIT_oe.md. PASS. |

### A2.3 — Rubrics

| Check | Result |
|---|---|
| Valid JSON | `python3 -c "import json; json.load(open(...))"` succeeds on the corrected file. PASS. |
| Outcome vs. process split | 24 outcome / 0 process. Matches V3 default and AGENTS.md hard rule #8. PASS. |
| Atomic titles | Every rubric checks exactly one observable. Rubric #4 (title identifies both client AND compliance subject) is the only "AND" — both halves are verifiable from the same `title` parameter on the same tool call, so the rubric stays atomic. PASS. |
| "At least N" without prompt mandate in title | None. Rubric #4 uses "both," which is exact-count. PASS. |
| Tool names in titles | None. Titles describe outcomes (e.g., "The Agent uploads a new AML clearance disposition memo for Acme Cloud to the Records Vault"). Tool names appear ONLY in evidence fields, which is allowed. PASS. |
| Evidence cites ≥1 OE step | Every rubric's evidence names a concrete tool call (records_vault_upload_document, reminder_delete_reminder, slack_conversations_add_message, email_send_email) or a final-response excerpt traceable to an OE. PASS. |
| Persona — Marina coordinator-role rubric (#13) | Evidence lists concrete pass/fail examples ("Marina Soko (CDD coordinator)" passes; "Prepared by: Marina Soko" fails). Lever stability verified. PASS. |
| JE-id-in-subject rubric (#5) | Accept set: `JE-acme_cloud-FP-2026-04-0052`, `je_b2c2b939a1244823`, `'JE 0052'`. Generic "Acme Cloud AML close-out" explicitly excluded. Tight criterion, no false-pass risk. PASS. |

### A2 verdict

**A2: GO.** Zero convention drift on Major fields. One informational WARN (validator action-verb whitelist mismatch) is acknowledged but does not constitute a defect — verbs match V3 reference convention. Issue belongs in the validator, not in the task.

---

## Cross-checks against prior AUDIT verdicts

No contradictions found. Council A's grounding + convention conclusions align fully with AUDIT_prompt.md, AUDIT_oe.md, and AUDIT_rubrics.md STRICT PASS verdicts on every sub-dimension I reviewed (feasibility, unique ground truth, parameter correctness, lever diversity, JE-id rubric tightness, Marina coordinator-role rubric specificity, JSON validity, OE-to-rubric coverage).

---

## Findings count by severity

- BLOCKER: 0
- MAJOR: 0
- MINOR: 0
- INFORMATIONAL: 1 (validator action-verb whitelist gap — applies to all V3 tasks, not specific to this one; belongs in validator maintenance)

## Overall verdict

**GO.** Both A1 (Grounding) and A2 (Convention) clear. Materialization in `_aux/Scratch_Corrected/` is ready to ship.
