-- Note:
    -- Filesystem schema: stores documents as files, not database tables.
    -- This SQL query covers database-backed services only.
    -- ⚠️ AVOID crafting prompts that depend on the Filesystem MCP server — this tool has known issues.
    --    Do NOT design tasks where the agent must read/write files via filesystem_read_file or filesystem_write_file.

SELECT 'contacts.contacts' AS source, to_jsonb(t) AS row_data FROM contacts.contacts t
UNION ALL
SELECT 'crm.crm_companies', to_jsonb(t) FROM crm.crm_companies t
UNION ALL
SELECT 'crm.crm_contacts', to_jsonb(t) FROM crm.crm_contacts t
UNION ALL
SELECT 'crm.crm_deals', to_jsonb(t) FROM crm.crm_deals t
UNION ALL
SELECT 'crm.crm_engagements', to_jsonb(t) FROM crm.crm_engagements t
UNION ALL
SELECT 'crm.crm_leads', to_jsonb(t) FROM crm.crm_leads t
UNION ALL
SELECT 'email.emails', to_jsonb(t) FROM email.emails t
UNION ALL
SELECT 'email.jmap_emails', to_jsonb(t) FROM email.jmap_emails t
UNION ALL
SELECT 'email.mailboxes', to_jsonb(t) FROM email.mailboxes t
UNION ALL
SELECT 'email.threads', to_jsonb(t) FROM email.threads t
UNION ALL
SELECT 'mortgage_los.activity_log_entries', to_jsonb(t) FROM mortgage_los.activity_log_entries t
UNION ALL
SELECT 'mortgage_los.borrowers', to_jsonb(t) FROM mortgage_los.borrowers t
UNION ALL
SELECT 'mortgage_los.conditions', to_jsonb(t) FROM mortgage_los.conditions t
UNION ALL
SELECT 'mortgage_los.document_checklist_items', to_jsonb(t) FROM mortgage_los.document_checklist_items t
UNION ALL
SELECT 'mortgage_los.lenders', to_jsonb(t) FROM mortgage_los.lenders t
UNION ALL
SELECT 'mortgage_los.loans', to_jsonb(t) FROM mortgage_los.loans t
UNION ALL
SELECT 'mortgage_los.milestones', to_jsonb(t) FROM mortgage_los.milestones t
UNION ALL
SELECT 'mortgage_los.staff', to_jsonb(t) FROM mortgage_los.staff t
UNION ALL
SELECT 'mortgage_los.vendors', to_jsonb(t) FROM mortgage_los.vendors t
UNION ALL
SELECT 'public._changelog', to_jsonb(t) FROM public._changelog t
UNION ALL
SELECT 'quickbooks.accounts', to_jsonb(t) FROM quickbooks.accounts t
UNION ALL
SELECT 'quickbooks.bills', to_jsonb(t) FROM quickbooks.bills t
UNION ALL
SELECT 'quickbooks.customers', to_jsonb(t) FROM quickbooks.customers t
UNION ALL
SELECT 'quickbooks.invoices', to_jsonb(t) FROM quickbooks.invoices t
UNION ALL
SELECT 'quickbooks.items', to_jsonb(t) FROM quickbooks.items t
UNION ALL
SELECT 'quickbooks.vendors', to_jsonb(t) FROM quickbooks.vendors t
UNION ALL
SELECT 'slack.slack_channels', to_jsonb(t) FROM slack.slack_channels t
UNION ALL
SELECT 'slack.slack_drafts', to_jsonb(t) FROM slack.slack_drafts t
UNION ALL
SELECT 'slack.slack_emojis', to_jsonb(t) FROM slack.slack_emojis t
UNION ALL
SELECT 'slack.slack_files', to_jsonb(t) FROM slack.slack_files t
UNION ALL
SELECT 'slack.slack_messages', to_jsonb(t) FROM slack.slack_messages t
UNION ALL
SELECT 'slack.slack_scheduled_messages', to_jsonb(t) FROM slack.slack_scheduled_messages t
UNION ALL
SELECT 'slack.slack_users', to_jsonb(t) FROM slack.slack_users t
UNION ALL
SELECT 'stripe.balance_transactions', to_jsonb(t) FROM stripe.balance_transactions t
UNION ALL
SELECT 'stripe.charges', to_jsonb(t) FROM stripe.charges t
UNION ALL
SELECT 'stripe.connected_accounts', to_jsonb(t) FROM stripe.connected_accounts t
UNION ALL
SELECT 'stripe.coupons', to_jsonb(t) FROM stripe.coupons t
UNION ALL
SELECT 'stripe.credit_notes', to_jsonb(t) FROM stripe.credit_notes t
UNION ALL
SELECT 'stripe.customers', to_jsonb(t) FROM stripe.customers t
UNION ALL
SELECT 'stripe.disputes', to_jsonb(t) FROM stripe.disputes t
UNION ALL
SELECT 'stripe.events', to_jsonb(t) FROM stripe.events t
UNION ALL
SELECT 'stripe.fc_account_owners', to_jsonb(t) FROM stripe.fc_account_owners t
UNION ALL
SELECT 'stripe.fc_accounts', to_jsonb(t) FROM stripe.fc_accounts t
UNION ALL
SELECT 'stripe.fc_sessions', to_jsonb(t) FROM stripe.fc_sessions t
UNION ALL
SELECT 'stripe.fc_transactions', to_jsonb(t) FROM stripe.fc_transactions t
UNION ALL
SELECT 'stripe.invoice_items', to_jsonb(t) FROM stripe.invoice_items t
UNION ALL
SELECT 'stripe.invoices', to_jsonb(t) FROM stripe.invoices t
UNION ALL
SELECT 'stripe.payment_intents', to_jsonb(t) FROM stripe.payment_intents t
UNION ALL
SELECT 'stripe.payment_methods', to_jsonb(t) FROM stripe.payment_methods t
UNION ALL
SELECT 'stripe.payouts', to_jsonb(t) FROM stripe.payouts t
UNION ALL
SELECT 'stripe.prices', to_jsonb(t) FROM stripe.prices t
UNION ALL
SELECT 'stripe.products', to_jsonb(t) FROM stripe.products t
UNION ALL
SELECT 'stripe.refunds', to_jsonb(t) FROM stripe.refunds t
UNION ALL
SELECT 'stripe.subscription_items', to_jsonb(t) FROM stripe.subscription_items t
UNION ALL
SELECT 'stripe.subscriptions', to_jsonb(t) FROM stripe.subscriptions t
UNION ALL
SELECT 'stripe.transfers', to_jsonb(t) FROM stripe.transfers t
UNION ALL
SELECT 'stripe.treasury_financial_accounts', to_jsonb(t) FROM stripe.treasury_financial_accounts t
UNION ALL
SELECT 'stripe.treasury_outbound_payments', to_jsonb(t) FROM stripe.treasury_outbound_payments t;
