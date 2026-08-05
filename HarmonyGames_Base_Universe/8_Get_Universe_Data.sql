-- Note:
    -- This script is used to get the universe complete data for the Harmony Games Universe.
        -- It only extracts structured JSON data from database tables. It does NOT extract binary/non-JSON content such as PDFs, images, documents (.docx), spreadsheets (.xlsx), or other file attachments.
        -- Those are given in this eval's Services_Data folder already, so we don't need to extract them here.

    -- Coverage: all 106 Postgres tables in 7_Universe_Schema.json, spanning the 13 Postgres-backed services (confluence, contacts, gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, snowflake, trello) plus the internal public._changelog audit table. 
    -- Snowflake is now materialized in this Postgres universe DB: the 42 snowflake.* tables (catalog mirrors snowflake_*, warehouse marts wh_analytics__*/wh_finance__*/wh_live_ops__*, and information-schema mirrors wh_information_schema__*) are live-queried at eval time via the snowflake_* tools in 6_Server_Tools_Details.json, and are also extractable here as regular tables. They are included below. 
        -- Keep this in sync with 7_Universe_Schema.json: if a new table is added there, add a matching UNION ALL line below. 
        -- Regenerate the schema with 9_Get_Universe_Schema.sql

SELECT 'confluence.confluence_attachments' AS source, to_jsonb(t) AS row_data FROM confluence.confluence_attachments t
UNION ALL
SELECT 'confluence.confluence_comments', to_jsonb(t) FROM confluence.confluence_comments t
UNION ALL
SELECT 'confluence.confluence_labels', to_jsonb(t) FROM confluence.confluence_labels t
UNION ALL
SELECT 'confluence.confluence_page_versions', to_jsonb(t) FROM confluence.confluence_page_versions t
UNION ALL
SELECT 'confluence.confluence_pages', to_jsonb(t) FROM confluence.confluence_pages t
UNION ALL
SELECT 'confluence.confluence_spaces', to_jsonb(t) FROM confluence.confluence_spaces t
UNION ALL
SELECT 'confluence.confluence_users', to_jsonb(t) FROM confluence.confluence_users t
UNION ALL
SELECT 'contacts.contacts', to_jsonb(t) FROM contacts.contacts t
UNION ALL
SELECT 'gcal.gcal_calendars', to_jsonb(t) FROM gcal.gcal_calendars t
UNION ALL
SELECT 'gcal.gcal_events', to_jsonb(t) FROM gcal.gcal_events t
UNION ALL
SELECT 'gdocs.docs_documents', to_jsonb(t) FROM gdocs.docs_documents t
UNION ALL
SELECT 'gdrive.drive_files', to_jsonb(t) FROM gdrive.drive_files t
UNION ALL
SELECT 'gdrive.drive_sheets', to_jsonb(t) FROM gdrive.drive_sheets t
UNION ALL
SELECT 'gdrive.drive_users', to_jsonb(t) FROM gdrive.drive_users t
UNION ALL
SELECT 'github.github_branches', to_jsonb(t) FROM github.github_branches t
UNION ALL
SELECT 'github.github_commit_map', to_jsonb(t) FROM github.github_commit_map t
UNION ALL
SELECT 'github.github_commits', to_jsonb(t) FROM github.github_commits t
UNION ALL
SELECT 'github.github_issues', to_jsonb(t) FROM github.github_issues t
UNION ALL
SELECT 'github.github_labels', to_jsonb(t) FROM github.github_labels t
UNION ALL
SELECT 'github.github_pr_comments', to_jsonb(t) FROM github.github_pr_comments t
UNION ALL
SELECT 'github.github_pull_request_commits', to_jsonb(t) FROM github.github_pull_request_commits t
UNION ALL
SELECT 'github.github_pull_requests', to_jsonb(t) FROM github.github_pull_requests t
UNION ALL
SELECT 'github.github_releases', to_jsonb(t) FROM github.github_releases t
UNION ALL
SELECT 'github.github_repositories', to_jsonb(t) FROM github.github_repositories t
UNION ALL
SELECT 'github.github_review_comments', to_jsonb(t) FROM github.github_review_comments t
UNION ALL
SELECT 'github.github_reviews', to_jsonb(t) FROM github.github_reviews t
UNION ALL
SELECT 'github.github_tags', to_jsonb(t) FROM github.github_tags t
UNION ALL
SELECT 'github.github_timeline_events', to_jsonb(t) FROM github.github_timeline_events t
UNION ALL
SELECT 'github.github_users', to_jsonb(t) FROM github.github_users t
UNION ALL
SELECT 'gmail.gmail_attachments', to_jsonb(t) FROM gmail.gmail_attachments t
UNION ALL
SELECT 'gmail.gmail_labels', to_jsonb(t) FROM gmail.gmail_labels t
UNION ALL
SELECT 'gmail.gmail_messages', to_jsonb(t) FROM gmail.gmail_messages t
UNION ALL
SELECT 'gmail.gmail_threads', to_jsonb(t) FROM gmail.gmail_threads t
UNION ALL
SELECT 'gmail.gmail_users', to_jsonb(t) FROM gmail.gmail_users t
UNION ALL
SELECT 'gsheets.sheets_sheets', to_jsonb(t) FROM gsheets.sheets_sheets t
UNION ALL
SELECT 'gsheets.sheets_spreadsheets', to_jsonb(t) FROM gsheets.sheets_spreadsheets t
UNION ALL
SELECT 'gslides.slides_page_elements', to_jsonb(t) FROM gslides.slides_page_elements t
UNION ALL
SELECT 'gslides.slides_pages', to_jsonb(t) FROM gslides.slides_pages t
UNION ALL
SELECT 'gslides.slides_presentations', to_jsonb(t) FROM gslides.slides_presentations t
UNION ALL
SELECT 'linear.linear_attachments', to_jsonb(t) FROM linear.linear_attachments t
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
SELECT 'public._changelog', to_jsonb(t) FROM public._changelog t
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
SELECT 'snowflake.snowflake_columns', to_jsonb(t) FROM snowflake.snowflake_columns t
UNION ALL
SELECT 'snowflake.snowflake_databases', to_jsonb(t) FROM snowflake.snowflake_databases t
UNION ALL
SELECT 'snowflake.snowflake_query_history', to_jsonb(t) FROM snowflake.snowflake_query_history t
UNION ALL
SELECT 'snowflake.snowflake_schemas', to_jsonb(t) FROM snowflake.snowflake_schemas t
UNION ALL
SELECT 'snowflake.snowflake_tables', to_jsonb(t) FROM snowflake.snowflake_tables t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__daily_active_users', to_jsonb(t) FROM snowflake.wh_analytics__game_events__daily_active_users t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__daily_metrics_agg', to_jsonb(t) FROM snowflake.wh_analytics__game_events__daily_metrics_agg t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__dim_country', to_jsonb(t) FROM snowflake.wh_analytics__game_events__dim_country t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__dim_date', to_jsonb(t) FROM snowflake.wh_analytics__game_events__dim_date t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__dim_device', to_jsonb(t) FROM snowflake.wh_analytics__game_events__dim_device t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__dim_player', to_jsonb(t) FROM snowflake.wh_analytics__game_events__dim_player t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__level_performance', to_jsonb(t) FROM snowflake.wh_analytics__game_events__level_performance t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__player_daily_progress', to_jsonb(t) FROM snowflake.wh_analytics__game_events__player_daily_progress t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__session_level_events', to_jsonb(t) FROM snowflake.wh_analytics__game_events__session_level_events t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__session_summary', to_jsonb(t) FROM snowflake.wh_analytics__game_events__session_summary t
UNION ALL
SELECT 'snowflake.wh_analytics__game_events__user_cohort_retention', to_jsonb(t) FROM snowflake.wh_analytics__game_events__user_cohort_retention t
UNION ALL
SELECT 'snowflake.wh_analytics__marketing__ad_spend_daily', to_jsonb(t) FROM snowflake.wh_analytics__marketing__ad_spend_daily t
UNION ALL
SELECT 'snowflake.wh_analytics__marketing__app_store_reviews', to_jsonb(t) FROM snowflake.wh_analytics__marketing__app_store_reviews t
UNION ALL
SELECT 'snowflake.wh_analytics__marketing__install_events', to_jsonb(t) FROM snowflake.wh_analytics__marketing__install_events t
UNION ALL
SELECT 'snowflake.wh_analytics__marketing__singular_installs_raw', to_jsonb(t) FROM snowflake.wh_analytics__marketing__singular_installs_raw t
UNION ALL
SELECT 'snowflake.wh_analytics__marketing__ua_spend_unified_v2', to_jsonb(t) FROM snowflake.wh_analytics__marketing__ua_spend_unified_v2 t
UNION ALL
SELECT 'snowflake.wh_analytics__monetization__iap_transactions', to_jsonb(t) FROM snowflake.wh_analytics__monetization__iap_transactions t
UNION ALL
SELECT 'snowflake.wh_analytics__monetization__revenue_daily', to_jsonb(t) FROM snowflake.wh_analytics__monetization__revenue_daily t
UNION ALL
SELECT 'snowflake.wh_analytics__monetization__revenue_daily_v2', to_jsonb(t) FROM snowflake.wh_analytics__monetization__revenue_daily_v2 t
UNION ALL
SELECT 'snowflake.wh_analytics__monetization__virtual_currency_ledger', to_jsonb(t) FROM snowflake.wh_analytics__monetization__virtual_currency_ledger t
UNION ALL
SELECT 'snowflake.wh_analytics__raw_telemetry__ad_impression_events', to_jsonb(t) FROM snowflake.wh_analytics__raw_telemetry__ad_impression_events t
UNION ALL
SELECT 'snowflake.wh_analytics__raw_telemetry__client_error_events', to_jsonb(t) FROM snowflake.wh_analytics__raw_telemetry__client_error_events t
UNION ALL
SELECT 'snowflake.wh_analytics__raw_telemetry__design_events', to_jsonb(t) FROM snowflake.wh_analytics__raw_telemetry__design_events t
UNION ALL
SELECT 'snowflake.wh_analytics__raw_telemetry__progression_events', to_jsonb(t) FROM snowflake.wh_analytics__raw_telemetry__progression_events t
UNION ALL
SELECT 'snowflake.wh_analytics__raw_telemetry__raw_game_events', to_jsonb(t) FROM snowflake.wh_analytics__raw_telemetry__raw_game_events t
UNION ALL
SELECT 'snowflake.wh_analytics__raw_telemetry__resource_flow_events', to_jsonb(t) FROM snowflake.wh_analytics__raw_telemetry__resource_flow_events t
UNION ALL
SELECT 'snowflake.wh_analytics__raw_telemetry__stg_events_enriched', to_jsonb(t) FROM snowflake.wh_analytics__raw_telemetry__stg_events_enriched t
UNION ALL
SELECT 'snowflake.wh_analytics__raw_telemetry__stg_progression_events', to_jsonb(t) FROM snowflake.wh_analytics__raw_telemetry__stg_progression_events t
UNION ALL
SELECT 'snowflake.wh_finance__expenses__cash_balance', to_jsonb(t) FROM snowflake.wh_finance__expenses__cash_balance t
UNION ALL
SELECT 'snowflake.wh_finance__expenses__headcount', to_jsonb(t) FROM snowflake.wh_finance__expenses__headcount t
UNION ALL
SELECT 'snowflake.wh_finance__expenses__monthly_burn', to_jsonb(t) FROM snowflake.wh_finance__expenses__monthly_burn t
UNION ALL
SELECT 'snowflake.wh_information_schema__columns', to_jsonb(t) FROM snowflake.wh_information_schema__columns t
UNION ALL
SELECT 'snowflake.wh_information_schema__databases', to_jsonb(t) FROM snowflake.wh_information_schema__databases t
UNION ALL
SELECT 'snowflake.wh_information_schema__schemata', to_jsonb(t) FROM snowflake.wh_information_schema__schemata t
UNION ALL
SELECT 'snowflake.wh_information_schema__tables', to_jsonb(t) FROM snowflake.wh_information_schema__tables t
UNION ALL
SELECT 'snowflake.wh_live_ops__events__live_event_performance', to_jsonb(t) FROM snowflake.wh_live_ops__events__live_event_performance t
UNION ALL
SELECT 'snowflake.wh_live_ops__events__push_notification_stats', to_jsonb(t) FROM snowflake.wh_live_ops__events__push_notification_stats t
UNION ALL
SELECT 'trello.trello_actions', to_jsonb(t) FROM trello.trello_actions t
UNION ALL
SELECT 'trello.trello_attachments', to_jsonb(t) FROM trello.trello_attachments t
UNION ALL
SELECT 'trello.trello_boards', to_jsonb(t) FROM trello.trello_boards t
UNION ALL
SELECT 'trello.trello_cards', to_jsonb(t) FROM trello.trello_cards t
UNION ALL
SELECT 'trello.trello_check_items', to_jsonb(t) FROM trello.trello_check_items t
UNION ALL
SELECT 'trello.trello_checklists', to_jsonb(t) FROM trello.trello_checklists t
UNION ALL
SELECT 'trello.trello_labels', to_jsonb(t) FROM trello.trello_labels t
UNION ALL
SELECT 'trello.trello_lists', to_jsonb(t) FROM trello.trello_lists t
UNION ALL
SELECT 'trello.trello_members', to_jsonb(t) FROM trello.trello_members t
UNION ALL
SELECT 'trello.trello_organizations', to_jsonb(t) FROM trello.trello_organizations t;
