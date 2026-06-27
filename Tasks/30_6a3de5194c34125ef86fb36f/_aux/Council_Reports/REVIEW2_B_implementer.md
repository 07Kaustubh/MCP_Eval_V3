LENS: Implementer

# REVIEW2 — Council B Lens 2 (B5 — tool-leak / phrasing scan + parameter validity)

**Target:** corrected materialization of Task 30 (SALVAGEABLE) — `_aux/Scratch_Corrected/{5_Prompt.txt, 6_Oracle_Events.txt, 7_Rubrics.json}`
**Posture:** read-only, will-this-actually-run-on-the-platform
**Iteration under review:** iteration 2 (post-removal of Row 3 ghost-tool `records_vault_update_document`)

---

## Section 1 — Tool name reality check

Every tool name referenced in `6_Oracle_Events.txt` and in `7_Rubrics.json` evidence strings was grep'd against `Brookfield_Base_Universe/8_Server_Tools_Details.json`. Results:

| Tool name | Line in 8_Server_Tools_Details.json | Verdict |
|---|---|---|
| `oracle_gl_list_journal_entries` | 2789 | REAL |
| `oracle_gl_get_journal_entry` | 2837 | REAL |
| `email_search_emails` | 1733 | REAL |
| `slack_conversations_search_messages` | 4548 | REAL |
| `reminder_get_all_reminders` | 3937 | REAL |
| `reminder_delete_reminder` | 3916 | REAL |
| `records_vault_list_documents` | 3277 | REAL |
| `records_vault_upload_document` | 3378 | REAL |
| `slack_conversations_add_message` | 4626 | REAL |
| `email_send_email` | 1593 | REAL |

**Ghost-tool re-check:** `grep records_vault_update_document` against the three corrected files returns ZERO hits. The Row 3 ghost tool from iteration 1 is fully purged. Confirms the prior AUDIT_oe.md note that the ghost reference was correctly removed.

**Verdict — Section 1:** PASS (10/10 real, 0 ghost tools).

---

## Section 2 — Parameter trap compliance

Per AGENTS.md trap list, with corrected-file evidence:

| Trap | Required | Actual in OE | Verdict |
|---|---|---|---|
| Slack: use `payload` not `text`/`body` | `payload` | OE07 specifies `payload summarising: ...` | PASS |
| Email: use `content` not `body` | `content` | OE08 specifies `content confirming the file is fully closed` | PASS |
| reminder_delete_reminder uses `reminder_id` | `reminder_id` | OE04 specifies `reminder_id="reminder_scen_041_audit_compliance_0000"` | PASS |
| records_vault_upload_document required params | `title`, `kind`, `retention_policy_code`, `classification`, `content_b64` | OE06 specifies title=, kind="memo", retention_policy_code="AICPA_SQMS_7Y", classification="restricted", content_b64 referencing… | PASS |
| email_send_email required params | `sender`, `recipients`, `cc`, `subject`, `content` | OE08 specifies sender=, recipients=[…], cc=[…], subject…, content… | PASS |
| slack_conversations_add_message required params | `channel_id`, `thread_ts`, `payload` | OE07 specifies channel_id="C008", thread_ts="1776969000.000000", payload… | PASS |

**Verdict — Section 2:** PASS (6/6 trap-compliant in OE file).

---

## Section 3 — ID format validity

Cross-checked every concrete ID against `_aux/Universe_Split/*.json`:

| ID | Location verified | Verdict |
|---|---|---|
| `reminder_scen_041_audit_compliance_0000` | reminder.reminders.json — 1 row matched, title `"Review AML threshold alert for JE-acme_cloud-FP-2026-04-0052"` | REAL |
| `C008` | slack.slack_channels.json — id `C008`, name `compliance-and-registrations` | REAL |
| `1776969000.000000` | slack.slack_messages.json — 3 hits including the parent message id `b3f16284b9e35ce69a027f40960a755a` posted in C008 by `persona_005` opening the AML case thread for JE-acme_cloud-FP-2026-04-0052. Format = epoch-seconds with microsecond decimal (matches Slack ts convention) | REAL |
| `acme_cloud_FP-2026-04` | oracle_gl.ogl_fiscal_periods.json — 1 row matched | REAL |
| `JE-acme_cloud-FP-2026-04-0052` | oracle_gl.ogl_journal_entries.json — entry_number matches je id `je_b2c2b939a1244823`, posted 2026-04-22, DR 101000 Cash $57,077.69 / CR 110000 AR $57,077.69, entity_id `acme_cloud`, period_id `acme_cloud_FP-2026-04` — every field in OE01 target_data verified verbatim | REAL |
| `je_b2c2b939a1244823` | same row above | REAL |
| `matthew.li@brookfieldcpas.com` | email.emails.json — 84 hits | RESOLVABLE |
| `steven.perry@brookfieldcpas.com` | email.emails.json — 94 hits | RESOLVABLE |
| `farah.dlamini@brookfieldcpas.com` | email.emails.json — 15 hits | RESOLVABLE |
| `marina.soko@brookfieldcpas.com` (sender) | email.emails.json — 212 hits | RESOLVABLE |
| `AICPA_SQMS_7Y` (retention) | records_vault.rv_retention_policies.json — row exists, `retention_years: 7`, `regulatory_basis: AICPA SQMS` | VALID ENUM |
| `restricted` (classification) | AGENTS.md valid enum: internal / restricted / public | VALID ENUM |

**Verdict — Section 3:** PASS (12/12 IDs resolve to real per-task atoms).

---

## Section 4 — Phrasing scan (across all three corrected files)

Run as `grep -nE '—|at least [0-9]|approximately|\(or similar\)|mortgage_los|stripe|keystonemortgage|April 28 2026'` over each file.

| File | Em-dash | "at least N" w/o mandate | "approximately" before exact | "(or similar)" near exact | Keystone/MoveOps tokens |
|---|---|---|---|---|---|
| 5_Prompt.txt | 0 | 0 | 0 | 0 | 0 |
| 6_Oracle_Events.txt | 0 | 0 | 0 | 0 | 0 |
| 7_Rubrics.json | 0 | 0 | 0 | 0 | 0 |

**Tool-name-in-rubric-title scan:** Iterated all 24 rubrics, grep titles for `oracle_gl_`, `email_send_email`, `email_search_emails`, `slack_conversations_`, `reminder_`, `records_vault_` — ZERO hits. Tool names appear ONLY in evidence strings, per Rule 7.

**Internal-ID-in-prompt scan:** grep `5_Prompt.txt` for `reminder_scen_`, `1776969000`, `JE-acme_cloud-FP`, `je_b2c2b939`, `C008`, `persona_00`, `thread_ts` — ZERO hits. Prompt never leaks internal IDs.

**Verdict — Section 4:** PASS (zero phrasing hits, zero tool-name-in-title, zero internal-ID leakage in prompt).

---

## Section 5 — JSON validity hard re-check

Command: `python3 -c "import json; data=json.load(open('Tasks/30_6a3de5194c34125ef86fb36f/_aux/Scratch_Corrected/7_Rubrics.json')); print(len(data))"`
Output: `24`

`7_Rubrics.json` parses cleanly with exactly 24 rubrics. The Row 1 Major fix (the originally-reported JSON syntax defect) is fully resolved. PASS.

---

## Section 6 — Concern requiring REVISE (contradicts prior AUDIT_rubrics STRICT PASS)

**Finding:** Rubric #21 evidence string says `"The body parameter of the email_send_email call references the Acme Cloud compliance file..."` — but `email_send_email` does NOT have a `body` parameter. Per AGENTS.md parameter-trap list and per OE08's correct usage, the email body is carried in the `content` parameter.

- Title (#21): `"The Agent addresses the Acme Cloud compliance close-out in the body of the email sent to the engagement partners..."` — natural-language "body of the email" is fine here.
- Evidence (#21): `"The body parameter of the email_send_email call..."` — references a non-existent API parameter. A strict verifier pattern-matching on tool-call argument names will look for an arg named `body` on the `email_send_email` call, fail to find one (the OE uses `content`), and silent-fail the rubric.

**Why this matters — strict implementer lens:** Every other rubric in `7_Rubrics.json` that names a parameter does so with the literal correct name:
- Rubric #4: `"The title parameter of the records_vault_upload_document call..."` (literal correct param)
- Rubric #5: `"The subject parameter of the email_send_email call..."` (literal correct param)
- Rubric #6: `"the parameter retention_policy_code set exactly to AICPA_SQMS_7Y"` (literal correct param)
- Rubric #7: `"the parameter classification set to restricted"` (literal correct param)
- Rubric #21: `"The body parameter of the email_send_email call..."` — INCONSISTENT, references non-existent `body` param

**Contradicts prior AUDIT_rubrics STRICT PASS verdict.** The prior `AUDIT_rubrics.md` accepted this rubric, but the strict implementer lens flags it as a parameter-trap inconsistency that may silent-fail on a literal-matching verifier. The fix is one targeted word change.

**Required fix:**

File: `Tasks/30_6a3de5194c34125ef86fb36f/_aux/Scratch_Corrected/7_Rubrics.json` — rubric #21 evidence

OLD:
```
"The body parameter of the email_send_email call references the Acme Cloud compliance file and conveys a close-out or confirmation message. An email body that is unrelated to the Acme Cloud compliance matter does not pass. Exact wording is not required; any body that clearly pertains to the compliance file close-out qualifies."
```

NEW:
```
"The content parameter of the email_send_email call references the Acme Cloud compliance file and conveys a close-out or confirmation message. An email content that is unrelated to the Acme Cloud compliance matter does not pass. Exact wording is not required; any content that clearly pertains to the compliance file close-out qualifies."
```

(Title remains unchanged — "body of the email" as natural English is fine; only the evidence parameter-name reference needs alignment with the actual `content` parameter.)

---

## Verdict

**REVISE** — one targeted fix on rubric #21 evidence wording. All other implementer checks PASS:
- 10/10 tool names real
- 0 ghost tool references (Row 3 cleanup confirmed)
- 6/6 parameter traps respected in OE
- 12/12 concrete IDs resolve against per-task universe atoms
- 0 phrasing hits across all three files
- 0 tool names in rubric titles
- 0 internal IDs leaked into prompt
- JSON parses cleanly with 24 rubrics

Once rubric #21 evidence wording is aligned with the actual `content` parameter name, the deliverable bundle will run cleanly on the platform.
