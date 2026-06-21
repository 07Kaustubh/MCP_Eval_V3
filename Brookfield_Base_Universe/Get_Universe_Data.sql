-- Note:
    -- This script is used to get the universe complete data for the Brookfield Base Universe.

SELECT 'airtable.bases' AS source, to_jsonb(t) AS row_data FROM airtable.bases t
UNION ALL
SELECT 'airtable.records', to_jsonb(t) FROM airtable.records t
UNION ALL
SELECT 'airtable.tables', to_jsonb(t) FROM airtable.tables t
UNION ALL
SELECT 'blackline.blackline_archived_reconciliations', to_jsonb(t) FROM blackline.blackline_archived_reconciliations t
UNION ALL
SELECT 'blackline.blackline_audit_trail', to_jsonb(t) FROM blackline.blackline_audit_trail t
UNION ALL
SELECT 'blackline.blackline_close_tasks', to_jsonb(t) FROM blackline.blackline_close_tasks t
UNION ALL
SELECT 'blackline.blackline_evidence', to_jsonb(t) FROM blackline.blackline_evidence t
UNION ALL
SELECT 'blackline.blackline_exceptions', to_jsonb(t) FROM blackline.blackline_exceptions t
UNION ALL
SELECT 'blackline.blackline_reconciliations', to_jsonb(t) FROM blackline.blackline_reconciliations t
UNION ALL
SELECT 'blackline.blackline_review_notes', to_jsonb(t) FROM blackline.blackline_review_notes t
UNION ALL
SELECT 'blackline.blackline_sox_controls', to_jsonb(t) FROM blackline.blackline_sox_controls t
UNION ALL
SELECT 'calendar.events', to_jsonb(t) FROM calendar.events t
UNION ALL
SELECT 'contacts.contacts', to_jsonb(t) FROM contacts.contacts t
UNION ALL
SELECT 'email.emails', to_jsonb(t) FROM email.emails t
UNION ALL
SELECT 'email.jmap_emails', to_jsonb(t) FROM email.jmap_emails t
UNION ALL
SELECT 'email.mailboxes', to_jsonb(t) FROM email.mailboxes t
UNION ALL
SELECT 'email.threads', to_jsonb(t) FROM email.threads t
UNION ALL
SELECT 'linear.linear_comments', to_jsonb(t) FROM linear.linear_comments t
UNION ALL
SELECT 'linear.linear_issues', to_jsonb(t) FROM linear.linear_issues t
UNION ALL
SELECT 'linear.linear_projects', to_jsonb(t) FROM linear.linear_projects t
UNION ALL
SELECT 'linear.linear_team_memberships', to_jsonb(t) FROM linear.linear_team_memberships t
UNION ALL
SELECT 'linear.linear_teams', to_jsonb(t) FROM linear.linear_teams t
UNION ALL
SELECT 'linear.linear_users', to_jsonb(t) FROM linear.linear_users t
UNION ALL
SELECT 'messaging.conversations', to_jsonb(t) FROM messaging.conversations t
UNION ALL
SELECT 'messaging.messages', to_jsonb(t) FROM messaging.messages t
UNION ALL
SELECT 'oracle_gl.ogl_accounts', to_jsonb(t) FROM oracle_gl.ogl_accounts t
UNION ALL
SELECT 'oracle_gl.ogl_fiscal_periods', to_jsonb(t) FROM oracle_gl.ogl_fiscal_periods t
UNION ALL
SELECT 'oracle_gl.ogl_journal_entries', to_jsonb(t) FROM oracle_gl.ogl_journal_entries t
UNION ALL
SELECT 'oracle_gl.ogl_subledger_feed_runs', to_jsonb(t) FROM oracle_gl.ogl_subledger_feed_runs t
UNION ALL
SELECT 'oracle_gl.ogl_subledger_feeds', to_jsonb(t) FROM oracle_gl.ogl_subledger_feeds t
UNION ALL
SELECT 'oracle_gl.ogl_transactions', to_jsonb(t) FROM oracle_gl.ogl_transactions t
UNION ALL
SELECT 'public._changelog', to_jsonb(t) FROM public._changelog t
UNION ALL
SELECT 'records_vault.rv_access_grants', to_jsonb(t) FROM records_vault.rv_access_grants t
UNION ALL
SELECT 'records_vault.rv_chain_of_custody', to_jsonb(t) FROM records_vault.rv_chain_of_custody t
UNION ALL
SELECT 'records_vault.rv_classifications', to_jsonb(t) FROM records_vault.rv_classifications t
UNION ALL
SELECT 'records_vault.rv_document_versions', to_jsonb(t) FROM records_vault.rv_document_versions t
UNION ALL
SELECT 'records_vault.rv_documents', to_jsonb(t) FROM records_vault.rv_documents t
UNION ALL
SELECT 'records_vault.rv_legal_holds', to_jsonb(t) FROM records_vault.rv_legal_holds t
UNION ALL
SELECT 'records_vault.rv_retention_policies', to_jsonb(t) FROM records_vault.rv_retention_policies t
UNION ALL
SELECT 'reminder.reminders', to_jsonb(t) FROM reminder.reminders t
UNION ALL
SELECT 'sap_subledger.ap_invoices', to_jsonb(t) FROM sap_subledger.ap_invoices t
UNION ALL
SELECT 'sap_subledger.depreciation_schedule', to_jsonb(t) FROM sap_subledger.depreciation_schedule t
UNION ALL
SELECT 'sap_subledger.fixed_assets', to_jsonb(t) FROM sap_subledger.fixed_assets t
UNION ALL
SELECT 'sap_subledger.lease_schedules', to_jsonb(t) FROM sap_subledger.lease_schedules t
UNION ALL
SELECT 'sap_subledger.prepaid_periods', to_jsonb(t) FROM sap_subledger.prepaid_periods t
UNION ALL
SELECT 'sap_subledger.prepaid_schedules', to_jsonb(t) FROM sap_subledger.prepaid_schedules t
UNION ALL
SELECT 'sap_subledger.subledger_transactions', to_jsonb(t) FROM sap_subledger.subledger_transactions t
UNION ALL
SELECT 'slack.slack_channels', to_jsonb(t) FROM slack.slack_channels t
UNION ALL
SELECT 'slack.slack_messages', to_jsonb(t) FROM slack.slack_messages t
UNION ALL
SELECT 'slack.slack_users', to_jsonb(t) FROM slack.slack_users t;
