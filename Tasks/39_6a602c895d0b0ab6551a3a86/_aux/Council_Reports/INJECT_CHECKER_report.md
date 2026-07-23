# INJECT-CHECKER Report

Task: `39_6a602c895d0b0ab6551a3a86`
Universe: StarPM (V4)
Post-injection snapshot: `3_UniverseDataForThisTask.json` (changelog stream, 3,965 entries)
SQL source: `9_Universe_inject.sql` (REDO cycle — includes L6 HubSpot additions)

## Per-Record Results

| Table | ID | Operation | Verdict | Notes |
|---|---|---|---|---|
| linear.linear_issues | OPS-224 | UPDATE | LANDED | state_id: state_OPS_4 → state_OPS_3; updated_at → 2026-06-17T16:45:00-05:00; completed_at → NULL. Two subsequent no-op re-runs (empty changed_fields) confirm idempotency. |
| linear.linear_issues | OPS-225 | UPDATE | LANDED | state_id: state_OPS_4 → state_OPS_3; updated_at → 2026-06-17T11:20:00-05:00; completed_at → NULL. Two subsequent no-op re-runs. |
| linear.linear_issues | OPS-226 | UPDATE | LANDED | state_id: state_OPS_4 → state_OPS_3; updated_at → 2026-06-16T15:35:00-05:00; completed_at → NULL. Two subsequent no-op re-runs. |
| linear.linear_comments | comment_a1c47e2d3f8b41e6b9d21c9f4a5e7b02 | INSERT | LANDED | issue_id=OPS-224, author=James Bennett (user_8cd13ca90bca5494ab86e300c4b7829b), created_at=2026-06-17T16:44:00-05:00 |
| linear.linear_comments | comment_b2d58f3e4a9c52f7c0e32d0a5b6f8c13 | INSERT | LANDED | issue_id=OPS-225, author=Bennett, created_at=2026-06-17T11:19:00-05:00 |
| linear.linear_comments | comment_c3e69a4f5bad63a8d1f43e1b6c709d24 | INSERT | LANDED | issue_id=OPS-226, author=Bennett, created_at=2026-06-16T15:34:00-05:00 |
| slack.slack_messages | 01c3f5a2e7d94b681a5c9f2e30b47d5a | INSERT | LANDED | Jaime QC-FAIL decoy parent in C004 #make-ready, ts=1781645520.000200, thread_parent_id=NULL |
| slack.slack_messages | 02d4a6b3f8ea4c792b6d0a3f41c58e6b | INSERT | LANDED | Bennett rework reply nested under parent, thread_parent_id=01c3f5a2e7d94b681a5c9f2e30b47d5a |
| slack.slack_messages | 03e5b7c4a9fb5d803c7e1b4a52d69f7c | INSERT | LANDED | Brooke 6/18 closeout parent, C004, thread_parent_id=NULL |
| gmail.gmail_threads | a7f3c92e1b4d8e56 | INSERT | LANDED | subject "qc inspection failed - las vistas 3c" |
| gmail.gmail_threads | b8e4d0a3f2c5b9e7 | INSERT | LANDED | subject "las vistas 3c - closeout package" |
| gmail.gmail_messages | c9d5e1b4a3f6c0a8 | INSERT | LANDED | Jaime → Carlos cc Brooke, thread_id=a7f3c92e1b4d8e56, from=jaime.salinas@starpm.com |
| gmail.gmail_messages | d0e6f2c5b4a70b19 | INSERT | LANDED | Brooke → Jaime, thread_id=b8e4d0a3f2c5b9e7, from=brooke.phillips@starpm.com |
| hubspot.hubspot_objects | deal_c3a1b2e4f5d67890ab12cd34ef56789a | INSERT | LANDED | L6 canonical Las Vistas 3C deal, object_type=deals (older hs_lastmodifieddate → loses recency sort) |
| hubspot.hubspot_objects | deal_d4b2c3e5f6a78901bc23de45fa6b7c8d | INSERT | LANDED | L6 decoy Las Vistas 9D deal, object_type=deals (newer hs_lastmodifieddate → wins recency sort) |

Idempotency-guard DELETEs at the top of the SQL are followed by matching INSERTs for the same IDs; verified INSERTs above cover them.

## Summary
- Total records checked: 15
- LANDED: 15
- MISSING: 0
- WRONG_VALUE: 0
- DELETION_FAILED: 0

## OVERALL VERDICT: PASS

All 15 expected records from `9_Universe_inject.sql` are present in the post-injection universe with the exact field values the SQL specified. Levers L1 + L6 + L8 + L9 + L25 + L26 are supported by the injected state.

## Blocker details
none
