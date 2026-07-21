-- Note:
    -- This script is used to get the universe complete data for the StarPM Base Universe.

SELECT 'public._changelog' AS source, to_jsonb(t) AS row_data FROM public._changelog t
UNION ALL
SELECT 'airtable.airtable_bases', to_jsonb(t) FROM airtable.airtable_bases t
UNION ALL
SELECT 'airtable.airtable_comments', to_jsonb(t) FROM airtable.airtable_comments t
UNION ALL
SELECT 'airtable.airtable_dashboard_elements', to_jsonb(t) FROM airtable.airtable_dashboard_elements t
UNION ALL
SELECT 'airtable.airtable_fields', to_jsonb(t) FROM airtable.airtable_fields t
UNION ALL
SELECT 'airtable.airtable_interfaces', to_jsonb(t) FROM airtable.airtable_interfaces t
UNION ALL
SELECT 'airtable.airtable_pages', to_jsonb(t) FROM airtable.airtable_pages t
UNION ALL
SELECT 'airtable.airtable_records', to_jsonb(t) FROM airtable.airtable_records t
UNION ALL
SELECT 'airtable.airtable_tables', to_jsonb(t) FROM airtable.airtable_tables t
UNION ALL
SELECT 'airtable.airtable_user_groups', to_jsonb(t) FROM airtable.airtable_user_groups t
UNION ALL
SELECT 'airtable.airtable_users', to_jsonb(t) FROM airtable.airtable_users t
UNION ALL
SELECT 'airtable.airtable_views', to_jsonb(t) FROM airtable.airtable_views t
UNION ALL
SELECT 'airtable.airtable_workspaces', to_jsonb(t) FROM airtable.airtable_workspaces t
UNION ALL
SELECT 'contacts.contacts', to_jsonb(t) FROM contacts.contacts t
UNION ALL
SELECT 'gcalendar.gcalendar_calendars', to_jsonb(t) FROM gcalendar.gcalendar_calendars t
UNION ALL
SELECT 'gcalendar.gcalendar_events', to_jsonb(t) FROM gcalendar.gcalendar_events t
UNION ALL
SELECT 'gmail.gmail_drafts', to_jsonb(t) FROM gmail.gmail_drafts t
UNION ALL
SELECT 'gmail.gmail_labels', to_jsonb(t) FROM gmail.gmail_labels t
UNION ALL
SELECT 'gmail.gmail_messages', to_jsonb(t) FROM gmail.gmail_messages t
UNION ALL
SELECT 'gmail.gmail_threads', to_jsonb(t) FROM gmail.gmail_threads t
UNION ALL
SELECT 'hubspot.hubspot_associations', to_jsonb(t) FROM hubspot.hubspot_associations t
UNION ALL
SELECT 'hubspot.hubspot_campaign_asset_metrics', to_jsonb(t) FROM hubspot.hubspot_campaign_asset_metrics t
UNION ALL
SELECT 'hubspot.hubspot_campaign_attribution', to_jsonb(t) FROM hubspot.hubspot_campaign_attribution t
UNION ALL
SELECT 'hubspot.hubspot_campaigns', to_jsonb(t) FROM hubspot.hubspot_campaigns t
UNION ALL
SELECT 'hubspot.hubspot_job_titles', to_jsonb(t) FROM hubspot.hubspot_job_titles t
UNION ALL
SELECT 'hubspot.hubspot_objects', to_jsonb(t) FROM hubspot.hubspot_objects t
UNION ALL
SELECT 'hubspot.hubspot_owners', to_jsonb(t) FROM hubspot.hubspot_owners t
UNION ALL
SELECT 'hubspot.hubspot_properties', to_jsonb(t) FROM hubspot.hubspot_properties t
UNION ALL
SELECT 'hubspot.hubspot_seats', to_jsonb(t) FROM hubspot.hubspot_seats t
UNION ALL
SELECT 'hubspot.hubspot_teams', to_jsonb(t) FROM hubspot.hubspot_teams t
UNION ALL
SELECT 'linear.linear_attachments', to_jsonb(t) FROM linear.linear_attachments t
UNION ALL
SELECT 'linear.linear_comments', to_jsonb(t) FROM linear.linear_comments t
UNION ALL
SELECT 'linear.linear_cycles', to_jsonb(t) FROM linear.linear_cycles t
UNION ALL
SELECT 'linear.linear_diff_threads', to_jsonb(t) FROM linear.linear_diff_threads t
UNION ALL
SELECT 'linear.linear_diffs', to_jsonb(t) FROM linear.linear_diffs t
UNION ALL
SELECT 'linear.linear_documents', to_jsonb(t) FROM linear.linear_documents t
UNION ALL
SELECT 'linear.linear_initiative_status_updates', to_jsonb(t) FROM linear.linear_initiative_status_updates t
UNION ALL
SELECT 'linear.linear_initiatives', to_jsonb(t) FROM linear.linear_initiatives t
UNION ALL
SELECT 'linear.linear_issue_labels', to_jsonb(t) FROM linear.linear_issue_labels t
UNION ALL
SELECT 'linear.linear_issue_relations', to_jsonb(t) FROM linear.linear_issue_relations t
UNION ALL
SELECT 'linear.linear_issues', to_jsonb(t) FROM linear.linear_issues t
UNION ALL
SELECT 'linear.linear_project_labels', to_jsonb(t) FROM linear.linear_project_labels t
UNION ALL
SELECT 'linear.linear_project_milestones', to_jsonb(t) FROM linear.linear_project_milestones t
UNION ALL
SELECT 'linear.linear_project_status_updates', to_jsonb(t) FROM linear.linear_project_status_updates t
UNION ALL
SELECT 'linear.linear_projects', to_jsonb(t) FROM linear.linear_projects t
UNION ALL
SELECT 'linear.linear_team_memberships', to_jsonb(t) FROM linear.linear_team_memberships t
UNION ALL
SELECT 'linear.linear_teams', to_jsonb(t) FROM linear.linear_teams t
UNION ALL
SELECT 'linear.linear_users', to_jsonb(t) FROM linear.linear_users t
UNION ALL
SELECT 'linear.linear_workflow_states', to_jsonb(t) FROM linear.linear_workflow_states t
UNION ALL
SELECT 'quickbooks.quickbooks_company_info', to_jsonb(t) FROM quickbooks.quickbooks_company_info t
UNION ALL
SELECT 'quickbooks.quickbooks_entities', to_jsonb(t) FROM quickbooks.quickbooks_entities t
UNION ALL
SELECT 'slack.slack_canvas_sections', to_jsonb(t) FROM slack.slack_canvas_sections t
UNION ALL
SELECT 'slack.slack_canvases', to_jsonb(t) FROM slack.slack_canvases t
UNION ALL
SELECT 'slack.slack_channels', to_jsonb(t) FROM slack.slack_channels t
UNION ALL
SELECT 'slack.slack_drafts', to_jsonb(t) FROM slack.slack_drafts t
UNION ALL
SELECT 'slack.slack_files', to_jsonb(t) FROM slack.slack_files t
UNION ALL
SELECT 'slack.slack_messages', to_jsonb(t) FROM slack.slack_messages t
UNION ALL
SELECT 'slack.slack_reactions', to_jsonb(t) FROM slack.slack_reactions t
UNION ALL
SELECT 'slack.slack_scheduled_messages', to_jsonb(t) FROM slack.slack_scheduled_messages t
UNION ALL
SELECT 'slack.slack_users', to_jsonb(t) FROM slack.slack_users t;
