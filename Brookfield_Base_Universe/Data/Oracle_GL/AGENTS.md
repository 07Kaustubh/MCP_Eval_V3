# Oracle GL (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/oracle_gl.*.json`. Do not use these files for per-task work.

## Service role

Main accounting platform. Every journal entry, every fiscal-period state, every CoA account lives here. ~2,933 entries in the base universe.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `ogl_journal_entries.json` | `id` (`je_*`), `entry_number` (`JE-<entity>-FP-YYYY-MM-NNNN`), `entity_id`, `period_id`, `status`, `lines` (list), `total_debit`, `total_credit`, `posted_at`, `posted_by`, `prepared_by`, `submitted_at`, `approved_at`, `approved_by`, `rejected_at`, `rejected_by`, `reversed_at`, `reverses_entry_id`, `reversed_by_entry_id`, `late_post_authorization_id`, `is_standard_entry`, `business_justification`, `source_module` (AR, AP, GL, etc.) |
| `ogl_fiscal_periods.json` | `id` (`<entity>_FP-YYYY-MM`), `status` (`open`/`closed`/`future`), `entity_id`, `locked_at`, `locked_by`, `bd3_lock_at`, `bd5_close_at`, `period_label`, `fiscal_year`, `fiscal_quarter` |
| `ogl_accounts.json` | `id`, `entity_id`, `account_number`, `account_name`, `account_type` (asset/liability/equity/revenue/expense/contra), `is_active` |
| `ogl_subledger_feeds.json` | `feed_id`, `entity_id`, `source_module`, `schedule` |
| `ogl_subledger_feed_runs.json` | `run_id`, `feed_id`, `run_at`, `status` |
| `ogl_transactions.json` | Empty in base universe |

## JE lifecycle

`draft → submitted → approved → posted → (reversed)`. Minimum 300 seconds between state transitions. Posting into a closed period requires `late_post_authorization_id`.

A `reversed` JE has both `reverses_entry_id` (pointing to the original) and `reversed_by_entry_id` (on the original, pointing back).

## Account-number traps (per entity)

| Number | Brookfield | Northstar | Acme | Note |
|---|---|---|---|---|
| `101000` | Cash – Operating | Cash – Operating | Cash – Operating | consistent |
| `105000` | Cash – Client Trust | IOLTA Trust | Short-term Investments | **3 different concepts** |
| `120000` | not in CoA | Client Cost Advances | Deferred Commissions (ASC 340-40) | **2 different concepts** |
| `133000` | Prepaid CPE | Prepaid CLE | not in CoA | **2 different concepts** |
| `135000` | Prepaid Marketing | Prepaid Marketing | Prepaid Marketing & Advertising | v47 addition |
| `155000` | not in CoA | not in CoA | Capitalized Software | Acme only |
| `525000` | not in CoA | not in CoA | Sales Tax Expense | Acme only |
| `535000` | CPE | CLE | not in CoA | |

> **Always verify per-entity role before naming an account number in an OE or rubric.**

## Sales Tax accounting gap

There is no dedicated Sales Tax *Payable* account. The expense lands on `525000` (Acme only); the payable side lands on `225000` (otherwise Accrued Salaries & Bonuses). Confirm per entity before authoring sales-tax tasks.

## MCP tool notes

- Read: `oracle_gl_list_journal_entries` (filter by `period_id`, `entity_id`, `status`), `oracle_gl_get_journal_entry`, `oracle_gl_list_fiscal_periods`, `oracle_gl_get_fiscal_period`, `oracle_gl_list_accounts`
- Write lifecycle: `oracle_gl_create_journal_entry` → `oracle_gl_submit_journal_entry` → `oracle_gl_approve_journal_entry` → `oracle_gl_post_journal_entry`. 300-second minimum between transitions. Reversal: `oracle_gl_reverse_journal_entry`.
