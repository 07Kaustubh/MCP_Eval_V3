# Oracle Events Format Card

## What an OE is

A numbered-prose list of the steps a correct agent would take. Free-form text, NOT structured JSON. OEs prove the task is solvable and drive rubric writing. They describe tool-use steps, not what the final response should say.

## Structure

```
OE1: <one or two sentences describing the step>
OE2: <next step>
OE3: ...
```

Each step covers:

- **What action / discovery happens** (search, retrieve, post, send, update).
- **What tool would be used** — exact tool name from `Brookfield_Base_Universe/8_Server_Tools_Details.json` (the one stable file).
- **What parameters matter** — keys + concrete expected values from the per-task universe split.
- **What the agent should conclude** from the step's output, when relevant (e.g., "exclude the $42,500 from the aggregate because the entry is reversed").

## Hard rules

| Rule | Detail |
|---|---|
| **No em-dash / en-dash** | The validator blocks both. Use periods, commas, parentheses. |
| **Real tool names only** | Every `verb_noun_subject` token must exist in `8_Server_Tools_Details.json`. The validator greps. |
| **Real parameter names** | The agent harness will reject unknown params. Critical traps: |
| | - `email_send_email`, `email_reply_to_email`, `messaging_send_message` use `content` (NOT `body`) |
| | - `slack_conversations_add_message` uses `payload` (NOT `text`) |
| **Real expected values** | Every JE id, exception id, vendor id, dollar amount, email address must be from this task's `_aux/Universe_Split/`. |
| **Numbered, sequential** | `OE1`, `OE2`, ..., one per logical step. Sub-steps OK if they share a single tool call. |
| **Discovery + action** | The OE list ends with the write actions. Read / lookup steps come first. |

## How OEs map to rubrics

| OE step type | Rubric type |
|---|---|
| Write action (send email, post message, upload doc, update issue) | **Outcome 1.1** — one rubric per write |
| Write action with specific content requirements (recipient + body fields) | **Outcome 1.2** — added when content needs verification |
| Key fact the user asked to be told directly | **Outcome 2.1** — one per fact |
| Read / lookup step | Usually no rubric. The downstream Outcome rubrics prove the read happened. |
| Ordering constraint (A must happen before B, no Outcome can verify it) | **Process** rubric, only if the three-condition test passes |

## Tool name traps to watch

- `oracle_gl_*` tools: posting uses `oracle_gl_create_journal_entry` then `oracle_gl_submit_journal_entry` then `oracle_gl_approve_journal_entry` then `oracle_gl_post_journal_entry`. 300-second minimum between transitions. Closed-period posting needs `late_post_authorization_id`.
- `sap_subledger_*` AP tools: `sap_subledger_list_ap_invoices`, `sap_subledger_get_ap_invoice`, `sap_subledger_approve_ap_invoice`, `sap_subledger_void_ap_invoice`.
- `blackline_*` reconciliation lifecycle: `submit / approve / certify / archive`.
- `records_vault_upload_document` requires `kind`, `retention_policy_code`, `classification`, `content_b64`. Valid retention codes: `AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, `INDEFINITE`. **Do not use** `SOX_7Y` or `SEC_PERMANENT`.
- `linear_create_comment` uses `issueId` + `body`.
- `airtable_create_record` / `airtable_update_records` take `base_id`, `table_id`, `fields`.

## Discovery-step phrasing

Good OE discovery phrasing names the search query the agent should pass, in the agent's own voice:

> OE 2: Search emails using email_search_emails with query "GraniteRack" or "VEN-012-753165" or "SOW-2024" (or similar) to reconstruct the escalation trail.

For Slack:

> OE 7: Search Slack messages using slack_conversations_search_messages with search_query "FairLedger" or "headcount" or "contractor conversions" (or similar) in #monthly-close-coordination (C005).

For structured-DB searches that the agent typically skips, be explicit about the table and the field shape:

> OE 11: Call blackline_get_exception with exception_id "exc_cb0a9a94a3084c" to confirm state "awaiting_approval", assigned_to harry.marks@brookfieldcpas.com, approver james.randall@brookfieldcpas.com, sla_due_at "2026-06-04T18:00:09-04:00" (now past).

## Final paragraph (optional)

When the task has a write-heavy finale, the last OE can summarize the final user-facing message: what facts must land in the partner email / Records Vault memo / Slack post. This becomes the source for the Outcome 1.2 content rubrics.

## What OEs are NOT

- Not a script for the final response. They describe tool calls, not what to write to the user.
- Not a list of every possible tool call. They are the minimum set of steps that produce a correct trajectory.
- Not a place to add rubric reasoning. Rubrics get their own justifications.
- **Not a source of truth (ML-confirmed July 2026).** OEs are the CB's interpretation of the prompt's critical path. They may be inaccurate or misaligned with the prompt or universe. Universe data (`_aux/Universe_Split/` + `Fact_Ledger.json`) is the SSOT for all verifiable values. If an OE step names a value (amount, ID, email, date) that contradicts what is in the universe, the universe is correct — fix the OE, never fix the universe to match a wrong OE.
- **Not a substitute for prompt clarity.** The prompt must be unambiguous and solvable on its own. An agent that never reads the OEs must still be able to complete the task correctly from the prompt alone. OEs cannot resolve ambiguities the prompt fails to resolve.
- **Not used to justify rubric values.** When deriving rubric criterion values, go to the universe directly. The OE tells you WHAT action to cover; the universe tells you WHAT VALUE to embed. Never copy a value from an OE step without first verifying it in `_aux/Universe_Split/` or `Fact_Ledger.json`.

## Machine-checkable conventions

`Reference/OE_Convention_Inventory.json` is auto-extracted from the 4 V3 reference OE files. It captures tool-usage frequencies, parameter-naming patterns, opening-phrase patterns, and parameter traps. Council A's convention sweep on OE phase reads this inventory and flags drift.

If new V3 reference tasks are added, regenerate the inventory by re-extracting from the new sources.
