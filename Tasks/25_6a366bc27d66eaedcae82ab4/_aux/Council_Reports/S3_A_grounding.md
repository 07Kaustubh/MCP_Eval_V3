# Council A — Grounding — Rubrics
# Task: 25_6a366bc27d66eaedcae82ab4
# Date: 2026-06-22
# Status: GO

## Method
Extracted every concrete value (recon/exception/review-note/reminder/run/period/email/channel IDs, account numbers, dollar amounts, dates, integer counts, retention code, classification, channel name, persona emails) from the 20 rubric `title` fields in `7_Rubrics.json` and verified each verbatim via `grep -r --include="*.json"` against the per-source files in `_aux/Universe_Split/` (excluding `Universe_complete_data.json`).

## Grounded values table

| Value | Universe file | Record ID / line | Used in rubric(s) |
|---|---|---|---|
| BL-75810CD0FEE4 | blackline.blackline_reconciliations.json | id BL-75810CD0FEE4 (line 2671) | 4a022be0, 1af03630, 5248e45d, 0e88aacd, 702ef241, 2640ecb4, 576e29f5, 32b42ee4, 07a64324, 2e0b7395, 8ca25c9d |
| blackline_bdbbea5db590 | blackline.blackline_reconciliations.json | id blackline_bdbbea5db590 (line 2711) | 576e29f5 |
| exc_1ddfc978ce5a4d | blackline.blackline_exceptions.json | id exc_1ddfc978ce5a4d (line 39) | 07a64324, 1af03630, 8ca25c9d, 3952b3e7, 2e0b7395, 0e88aacd, 702ef241 |
| rn_564e65ce0d594f | blackline.blackline_review_notes.json | id rn_564e65ce0d594f (line 295, author edith.banda) | 2640ecb4 |
| reminder_scen_010_orphan_exception_0000 | reminder.reminders.json | reminder_id reminder_scen_010_orphan_exception_0000 (line 211) | 0e88aacd |
| run_e33ed2561f2c46 | oracle_gl.ogl_subledger_feed_runs.json | id run_e33ed2561f2c46, status success, rows_in 2083, rows_posted 2083, rows_rejected 0 (line 263) | ac93a531, 0e49d120, 10033d88 |
| brookfield_time_and_wip_feed | oracle_gl.ogl_subledger_feeds.json | id brookfield_time_and_wip_feed (line 23) | ac93a531, 0e49d120, 10033d88 |
| brookfield_FP-2026-05 | oracle_gl.ogl_fiscal_periods.json | id brookfield_FP-2026-05 (line 43) | 80d39aeb, ac93a531, 576e29f5, 32b42ee4, 0e49d120, 10033d88, 8ca25c9d |
| FP-2026-06 (bd3 anchor 2026-07-03) | oracle_gl.ogl_fiscal_periods.json | id brookfield_FP-2026-06, bd3_lock_at 2026-07-03T12:38:40-04:00 (line 47) | 1af03630, 3952b3e7, 702ef241 |
| 119000 | oracle_gl.ogl_accounts.json | number 119000, entity brookfield, Work in Process - Unbilled Services (line 27) | 80d39aeb, 576e29f5 |
| C005 / monthly-close-coordination | slack.slack_channels.json | id C005, name monthly-close-coordination (line 19) | a485a9e1, 2e0b7395 |
| thread_ts 1780248600.000000 | slack.slack_messages.json | id f936a11a46b05e0e9e16fdfac02bf8e4, ts 1780248600.000000, channel_id C005 (line 1871) | a485a9e1, 2e0b7395 |
| email_scen_059_wip_recognition_0000 | email.emails.json | email_id email_scen_059_wip_recognition_0000, sender andrea.phil, cc margaret.sullivan, recipient george.mcadam (line 5363) | 07c488a4, b4eaf6a4, 5248e45d, 0e49d120 |
| AICPA_SQMS_7Y | records_vault.rv_retention_policies.json | code AICPA_SQMS_7Y (line 3) | c2d08157 |
| restricted | records_vault.rv_classifications.json | code restricted (line 11) | c2d08157 |
| 2026-06-02 (Hannah accept-timing approval) | email.emails.json | email_id email_scen_010_orphan_exception_0009, sender hannah.grant, ts 2026-06-02T19:12:00 (line 5479) | 1af03630, 3952b3e7 |
| 2026-07-03 (FP-2026-06 bd3) | oracle_gl.ogl_fiscal_periods.json | brookfield_FP-2026-06.bd3_lock_at 2026-07-03 (line 47) | 702ef241 |
| $147,825 / 147825 | oracle_gl.ogl_journal_entries.json | je_53962aed96fe4b67 total_debit 147825 total_credit 147825 (line 9191); also email_scen_059 content | 80d39aeb, 2e0b7395, b4eaf6a4 |
| $4,390.62 / 4390.62 | blackline.blackline_reconciliations.json | BL-75810CD0FEE4 variance 4390.62 (line 2671); doppel 4390.62 (line 2711) | 5248e45d, 576e29f5, 32b42ee4 |
| 2083 (rows_in / rows_posted) | oracle_gl.ogl_subledger_feed_runs.json | run_e33ed2561f2c46 rows_in 2083, rows_posted 2083 (line 263) | ac93a531, 0e49d120, 10033d88 |
| george.mcadam@brookfieldcpas.com | contacts.contacts.json + email.emails.json + slack.slack_users.json | persona_001 | 80d39aeb, 07c488a4 |
| andrea.phil@brookfieldcpas.com | contacts.contacts.json + email.emails.json (sender of email_scen_059) | npc persona | 07c488a4, b4eaf6a4, 5248e45d, 0e49d120 |
| margaret.sullivan@brookfieldcpas.com | email.emails.json (cc on email_scen_059) | npc persona | 07c488a4 |
| anaya.wallace@brookfieldcpas.com | blackline.blackline_reconciliations.json (preparer on BL-75810CD0FEE4 + doppel) | npc persona | 576e29f5, 32b42ee4 |
| hannah.grant@brookfieldcpas.com | email.emails.json (sender of email_scen_010_orphan_exception_0009) | npc persona | 1af03630, 3952b3e7, 2e0b7395, 5248e45d, 702ef241 |
| daniel.jones@brookfieldcpas.com | contacts.contacts.json + slack.slack_users.json | npc persona | 80d39aeb, 2e0b7395, b4eaf6a4 |
| edith.banda@brookfieldcpas.com | blackline.blackline_review_notes.json (author of rn_564e65ce0d594f) | npc persona | 2640ecb4 |

## Anomalies / not-found
None. Every concrete value extracted from the 20 rubric titles grounded verbatim in the per-source `*.json` files.

## Final verdict
GO
