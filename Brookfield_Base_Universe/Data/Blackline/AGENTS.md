# BlackLine (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/blackline.*.json`. Do not use these files for per-task work.

## Service role

Close + reconciliation workflow. BlackLine holds the workflow metadata around Excel workbooks (the actual reconciliation worksheet is an attachment). ~6,800 entries in the base universe.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `blackline_reconciliations.json` | `id` (`BL-...`), `entity_id`, `account_number`, `period_id`, `state`, `preparer`, `reviewer`, `certifier`, `gl_balance`, `supporting_balance`, `variance` |
| `blackline_exceptions.json` | `id` (`exc_...`), `type` (NOT `exception_type`), `state`, `urgency`, `approver`, `entity_id`, `assigned_to`, `escalated`, `root_cause`, `sla_due_at`, `related_reconciliation_id`, `financial_impact`, `systemic_issue_flag` |
| `blackline_review_notes.json` | `id`, `recon_id`, `author`, `body`, `created_at` |
| `blackline_close_tasks.json` | `id`, `period_id`, `bd_day`, `status` |
| `blackline_evidence.json` | `id`, `recon_id`, `kind`, `attachment_path` |
| `blackline_audit_trail.json` | append-only event log |
| `blackline_archived_reconciliations.json` | post-archival roll-forward |

## State machines

- **Reconciliation:** `open → in_progress → submitted → approved → certified → archived` (side state: `overdue`)
- **Exception:** `logged → investigating → awaiting_approval → closed`

## Exception types (6 only)

`duplicate_entry_detected`, `unrecorded_invoice`, `timing_difference_over_sla`, `fx_revaluation_drift`, `subledger_feed_drop`, `missing_accrual_variance`

## Variance materiality bands

- under $10 — immaterial
- $10–$1,000 — should be addressed (often rolled to subsequent month JE)
- over $1,000 — urgent

## MCP tool notes

- `blackline_get_exception`, `blackline_list_exceptions` (filter by `state`, `entity_id`, `related_period_id`)
- `blackline_get_reconciliation`, `blackline_list_reconciliations`
- Lifecycle write tools: `blackline_submit_reconciliation`, `blackline_approve_reconciliation`, `blackline_certify_reconciliation`
