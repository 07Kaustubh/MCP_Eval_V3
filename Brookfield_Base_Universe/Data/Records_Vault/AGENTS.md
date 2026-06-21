# Records Vault (stale-to-task pre-baked split)

> Per-task data lives in `Tasks/<TASK_DIR>/_aux/Universe_Split/records_vault.*.json`. Do not use these files for per-task work.

## Service role

Document repository. Workpapers, MAPs, engagement letters, AML files, control-test memos, tax-determination memos, consent letters. ~4,554 entries (2,007 documents + 2,356 versions + 184 access grants) in the base universe.

## Tables (inner shapes, parsed from `row_data`)

| File | Key fields |
|---|---|
| `rv_documents.json` | `id` (`doc_*`), `title`, `kind`, `classification` (`internal`/`restricted`/`public`), `retention_policy_code`, `entity_id`, `uploaded_by`, `uploaded_at`, `latest_version_id` |
| `rv_document_versions.json` | `id` (`v_*`), `document_id`, `version_number`, `uploaded_at`, `uploaded_by`, `file_path`, `content_b64`, `summary` |
| `rv_access_grants.json` | `id`, `document_id`, `granted_to`, `granted_by`, `role` |
| `rv_classifications.json` | enum: `public`, `internal`, `restricted` |
| `rv_retention_policies.json` | enum: `AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, `INDEFINITE` |
| `rv_chain_of_custody.json` | Empty in base universe |
| `rv_legal_holds.json` | Empty in base universe |

## Retention codes (hard list)

- `AICPA_SQMS_7Y` — default for tax workpapers, audit support, recon evidence
- `IRS_TAX_7Y` — tax-preparer records
- `FIRM_INTERNAL` — engagement letters, client master files (5y)
- `INDEFINITE` — partnership agreements, statutory records

> **Never write `SOX_7Y` or `SEC_PERMANENT`.** They do not exist in this universe.

## Classifications

- `internal` — default, ~98% of documents
- `restricted` — AML files, executive comp, audit folders, partner-only memos, client-consent letters
- `public` — defined in schema, **unused in the base universe**. Do not author prompts that produce `public` artifacts unless deliberately introducing the first one.

## Document kinds (common)

`memo`, `workpaper`, `engagement_letter`, `engagement_letter_addendum`, `engagement_change_order`, `tax_return`, `tax_determination_memo`, `management_accounts_package`, `annual_accounts_package`, `quarterly_reporting_package`, `client_consent_letter`, `audit_evidence`, `journal_entry_support`, `reconciliation_support`, `internal_strategy`, `internal_status_update`

## Parameter trap

- `records_vault_upload_document` requires `kind`, `retention_policy_code` (from the hard list above), `classification`, `content_b64`. Missing any one = tool failure.

## MCP tool notes

- Read: `records_vault_list_documents`, `records_vault_get_document`, `records_vault_search_documents`, `records_vault_list_versions`, `records_vault_get_version`
- Write: `records_vault_upload_document`, `records_vault_create_version`, `records_vault_grant_access`
