# SAP Subledger (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/sap_subledger.*.json`. Do not use these files for per-task work.

## Service role

Transaction-level detail supporting GL. AP invoices, fixed assets, prepaid amortization, lease schedules. ~4,060 entries in the base universe. **Being decommissioned by Oct 2026 cutover into Oracle GL** per the SAP→Oracle migration plan.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `ap_invoices.json` | `id` (`apinv_<hex>`), `vendor_id` (`VEN-NNN[-suffix]`), `vendor_invoice_number`, `amount`, `currency`, `entity_id`, `due_date`, `status`, `approver`, `approved_at`, `paid_at`, `voided_at`, `void_reason`, `lines` (list with `account_number`, `cost_center`, `description`), `posting_date`, `invoice_date` |
| `fixed_assets.json` | `asset_id`, `entity_id`, `description`, `acquisition_cost`, `acquisition_date`, `useful_life_months`, `salvage_value`, `status` |
| `depreciation_schedule.json` | `asset_id`, `period_id`, `depreciation_amount`, `accumulated_depreciation` |
| `lease_schedules.json` | `lease_id`, `entity_id`, `lessor`, `commencement_date`, `term_months`, `monthly_payment`, `discount_rate` (ASC 842 leases) |
| `prepaid_schedules.json` | `schedule_id`, `entity_id`, `description`, `total_amount`, `amortization_months` |
| `prepaid_periods.json` | `schedule_id`, `period_id`, `amortization_amount` |
| `subledger_transactions.json` | `transaction_id`, `entity_id`, `gl_account_number`, `module` (AP / AR / etc.), `amount`, `posting_date`, `vendor_id`, `document_ref` |

## AP invoice status flow

`pending_approval → approved → paid` (or `voided`). 117 unique vendors in the base universe.

## Approval ladder

| Tier | Authority |
|---|---|
| Any amount, AP coding | AP clerks |
| ≤ $10,000 | AP managers |
| ≤ $50,000 | Controllers |
| > $50,000 | Managing Partner by entity (Steven Perry — Brookfield/Acme; Matthew Li — Northstar; Andrea Phil — de-minimis) |

## Discovery patterns

- A credit memo posted to AP via `subledger_transactions.json` (e.g., a vendor `subledger_transactions` row with negative amount against the same vendor) can reduce the net economic outflow of an AP invoice (Task 11 CloudNova pattern). Agents that read only `ap_invoices.json` and skip subledger transactions miss this.
- Aged invoices (90+ days since `invoice_date` still in `pending_approval`) are a recurring AP escalation hardness lever.

## MCP tool notes

- Read: `sap_subledger_list_ap_invoices` (filter by `entity_id`, `vendor_id`, `status`, `posting_date_from/to`), `sap_subledger_get_ap_invoice`, `sap_subledger_list_subledger_transactions` (filter by `gl_account_number`, `module`, `posting_date`), `sap_subledger_list_fixed_assets`, `sap_subledger_get_depreciation_schedule`, `sap_subledger_list_lease_schedules`, `sap_subledger_list_prepaid_schedules`
- Write: `sap_subledger_approve_ap_invoice`, `sap_subledger_void_ap_invoice` (requires `void_reason`)
