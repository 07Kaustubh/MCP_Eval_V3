SELECT 'airtable.bases' AS source, to_jsonb(t) AS row_data FROM airtable.bases t
UNION ALL
SELECT 'airtable.tables', to_jsonb(t) FROM airtable.tables t
UNION ALL
SELECT 'airtable.records', to_jsonb(t) FROM airtable.records t
UNION ALL
SELECT 'calendar.events', to_jsonb(t) FROM calendar.events t
UNION ALL
SELECT 'contacts.contacts', to_jsonb(t) FROM contacts.contacts t
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
SELECT 'linear.linear_users', to_jsonb(t) FROM linear.linear_users t
UNION ALL
SELECT 'linear.linear_teams', to_jsonb(t) FROM linear.linear_teams t
UNION ALL
SELECT 'linear.linear_team_memberships', to_jsonb(t) FROM linear.linear_team_memberships t
UNION ALL
SELECT 'linear.linear_projects', to_jsonb(t) FROM linear.linear_projects t
UNION ALL
SELECT 'linear.linear_issues', to_jsonb(t) FROM linear.linear_issues t
UNION ALL
SELECT 'linear.linear_comments', to_jsonb(t) FROM linear.linear_comments t
UNION ALL
SELECT 'public._changelog', to_jsonb(t) FROM public._changelog t
UNION ALL
SELECT 'quickbooks.accounts', to_jsonb(t) FROM quickbooks.accounts t
UNION ALL
SELECT 'quickbooks.customers', to_jsonb(t) FROM quickbooks.customers t
UNION ALL
SELECT 'quickbooks.vendors', to_jsonb(t) FROM quickbooks.vendors t
UNION ALL
SELECT 'quickbooks.invoices', to_jsonb(t) FROM quickbooks.invoices t
UNION ALL
SELECT 'quickbooks.bills', to_jsonb(t) FROM quickbooks.bills t
UNION ALL
SELECT 'quickbooks.items', to_jsonb(t) FROM quickbooks.items t
UNION ALL
SELECT 'slack.slack_users', to_jsonb(t) FROM slack.slack_users t
UNION ALL
SELECT 'slack.slack_channels', to_jsonb(t) FROM slack.slack_channels t
UNION ALL
SELECT 'slack.slack_messages', to_jsonb(t) FROM slack.slack_messages t;