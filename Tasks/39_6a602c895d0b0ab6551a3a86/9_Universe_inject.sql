-- ============================================================
-- 9_Universe_inject.sql
-- Task 39_6a602c895d0b0ab6551a3a86
-- Universe: StarPM (V4)
-- Scenario: Jaime Salinas second-pass QC closeout - Las Vistas 3C
-- Levers supported: L1 + L6 + L8 + L9 + L25 + L26
-- Schema note: gmail array columns (label_ids/to_addresses/cc_addresses)
--              are jsonb in the live DB, encoded as JSONB array literals.
-- REDO note: R2-R9 (Linear/Slack/Gmail) may already be in the platform from
--            the previous injection cycle. Idempotency DELETEs cover all
--            records so the full script can be re-run safely. R10-R11
--            (HubSpot deals for L6) are new in this REDO pass.
-- ============================================================

BEGIN;

-- Idempotency guard: clear any prior partial-insert state so this script
-- can be re-run safely. Platform commits per statement, so an earlier
-- failed run may have left the Linear comments / Slack messages / Gmail
-- threads already in the DB.
DELETE FROM gmail.gmail_messages WHERE id IN ('c9d5e1b4a3f6c0a8','d0e6f2c5b4a70b19');
DELETE FROM gmail.gmail_threads WHERE id IN ('a7f3c92e1b4d8e56','b8e4d0a3f2c5b9e7');
DELETE FROM slack.slack_messages WHERE id IN ('01c3f5a2e7d94b681a5c9f2e30b47d5a','02d4a6b3f8ea4c792b6d0a3f41c58e6b','03e5b7c4a9fb5d803c7e1b4a52d69f7c');
DELETE FROM linear.linear_comments WHERE id IN ('comment_a1c47e2d3f8b41e6b9d21c9f4a5e7b02','comment_b2d58f3e4a9c52f7c0e32d0a5b6f8c13','comment_c3e69a4f5bad63a8d1f43e1b6c709d24');
DELETE FROM hubspot.hubspot_objects WHERE id IN ('deal_c3a1b2e4f5d67890ab12cd34ef56789a','deal_d4b2c3e5f6a78901bc23de45fa6b7c8d');

-- L1 + L8: Roll OPS-224/225/226 back from Done to In Review
UPDATE linear.linear_issues
SET state_id = 'state_OPS_3', updated_at = '2026-06-17T16:45:00-05:00', completed_at = NULL
WHERE id = 'OPS-224';
UPDATE linear.linear_issues
SET state_id = 'state_OPS_3', updated_at = '2026-06-17T11:20:00-05:00', completed_at = NULL
WHERE id = 'OPS-225';
UPDATE linear.linear_issues
SET state_id = 'state_OPS_3', updated_at = '2026-06-16T15:35:00-05:00', completed_at = NULL
WHERE id = 'OPS-226';

-- L8: James Bennett rework-complete comments
INSERT INTO linear.linear_comments (id, body, issue_id, author_id, parent_id, created_at, project_id, updated_at, archived_at, document_id, quoted_text, resolved_at, milestone_id, initiative_id)
VALUES ('comment_a1c47e2d3f8b41e6b9d21c9f4a5e7b02', 'Sanded and repainted the uneven touch-up sections along the living room baseboard this afternoon. Blended finish is even and dry. Ready for QC re-check.', 'OPS-224', 'user_8cd13ca90bca5494ab86e300c4b7829b', NULL, '2026-06-17T16:44:00-05:00', NULL, '2026-06-17T16:44:00-05:00', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO linear.linear_comments (id, body, issue_id, author_id, parent_id, created_at, project_id, updated_at, archived_at, document_id, quoted_text, resolved_at, milestone_id, initiative_id)
VALUES ('comment_b2d58f3e4a9c52f7c0e32d0a5b6f8c13', 'Recleaned the refrigerator interior (shelves, drawers, seals) and the oven interior. Both are clean and presentable. Ready for QC re-check.', 'OPS-225', 'user_8cd13ca90bca5494ab86e300c4b7829b', NULL, '2026-06-17T11:19:00-05:00', NULL, '2026-06-17T11:19:00-05:00', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO linear.linear_comments (id, body, issue_id, author_id, parent_id, created_at, project_id, updated_at, archived_at, document_id, quoted_text, resolved_at, milestone_id, initiative_id)
VALUES ('comment_c3e69a4f5bad63a8d1f43e1b6c709d24', 'Removed the towel ring beside the vanity and reinstalled it in the correct orientation. Fixture secure and level. Ready for QC re-check.', 'OPS-226', 'user_8cd13ca90bca5494ab86e300c4b7829b', NULL, '2026-06-16T15:34:00-05:00', NULL, '2026-06-16T15:34:00-05:00', NULL, NULL, NULL, NULL, NULL, NULL);

-- L26: Slack decoy parent (6/16 Jaime QC-FAIL) in #make-ready
INSERT INTO slack.slack_messages (id, ts, text, type, subtype, user_id, channel_id, created_at, files_json, reply_count, latest_reply, reactions_json, attachments_json, thread_parent_id, thread_ts_legacy, reply_users_count, is_activity_message)
VALUES ('01c3f5a2e7d94b681a5c9f2e30b47d5a', '1781645520.000200', 'Ran QC on Las Vistas 3C this afternoon. Three items didn''t pass: living room baseboard touch-ups uneven, refrigerator and oven interiors dirty, bathroom towel ring installed reversed. Kicking back to rework. Punch list going to Linear.', 'message', NULL, 'U2CD1BC03B2', 'C004', '2026-06-16T21:32:00+00:00', '[]', 1, '1781651100.000201', '[]', '[]', NULL, NULL, 1, FALSE);

-- L26: Bennett rework-in-progress reply nested under R5
INSERT INTO slack.slack_messages (id, ts, text, type, subtype, user_id, channel_id, created_at, files_json, reply_count, latest_reply, reactions_json, attachments_json, thread_parent_id, thread_ts_legacy, reply_users_count, is_activity_message)
VALUES ('02d4a6b3f8ea4c792b6d0a3f41c58e6b', '1781651100.000201', 'Towel ring reinstall done this afternoon. Baseboard sand and repaint tomorrow AM, appliance interiors right after.', 'message', NULL, 'UD92EEA47D7', 'C004', '2026-06-16T23:05:00+00:00', '[]', 0, NULL, '[]', '[]', '01c3f5a2e7d94b681a5c9f2e30b47d5a', '1781645520.000200', 0, FALSE);

-- L26: Brooke's canonical 6/18 closeout parent
INSERT INTO slack.slack_messages (id, ts, text, type, subtype, user_id, channel_id, created_at, files_json, reply_count, latest_reply, reactions_json, attachments_json, thread_parent_id, thread_ts_legacy, reply_users_count, is_activity_message)
VALUES ('03e5b7c4a9fb5d803c7e1b4a52d69f7c', '1781788320.000202', 'Jaime, Las Vistas 3C came off rework yesterday. When you finish today''s re-check, drop the closeout note here and let Carlos know so leasing can activate showings. Thanks.', 'message', NULL, 'U9741B657FE', 'C004', '2026-06-18T13:12:00+00:00', '[]', 0, NULL, '[]', '[]', NULL, NULL, 0, FALSE);

-- L26: Gmail decoy FAIL thread (6/16 Jaime -> Carlos, cc Brooke)
INSERT INTO gmail.gmail_threads (id, snippet, created_at, history_id, last_internal_date, subject_normalized)
VALUES ('a7f3c92e1b4d8e56', 'Carlos, QC on 3C did not pass this afternoon. Punch items: living room baseboard touch-ups uneven, refrigerator and oven interiors dirty, bathroom towel ring installed rever', '2026-06-16T21:40:00.000000Z', '1781646000000', '1781646000000', 'qc inspection failed - las vistas 3c');
INSERT INTO gmail.gmail_messages (id, payload, snippet, subject, label_ids, thread_id, created_at, history_id, updated_at, cc_addresses, from_address, to_addresses, internal_date, size_estimate, has_attachments)
VALUES ('c9d5e1b4a3f6c0a8', '{"body": {"data": "Q2FybG9zLAoKUUMgb24gM0MgZGlkIG5vdCBwYXNzIHRoaXMgYWZ0ZXJub29uLiBQdW5jaCBpdGVtczogbGl2aW5nIHJvb20gYmFzZWJvYXJkIHRvdWNoLXVwcyB1bmV2ZW4sIHJlZnJpZ2VyYXRvciBhbmQgb3ZlbiBpbnRlcmlvcnMgZGlydHksIGJhdGhyb29tIHRvd2VsIHJpbmcgaW5zdGFsbGVkIHJldmVyc2VkLiBLaWNraW5nIGJhY2sgdG8gcmV3b3JrLCB3aWxsIHJlLWluc3BlY3Qgb25jZSBKYW1lcyBzaWduYWxzIGRvbmUuCgpKYWltZQ", "size": 250}, "parts": [], "partId": "", "headers": [{"name": "From", "value": "jaime.salinas@starpm.com"}, {"name": "To", "value": "carlos.mendez@starpm.com"}, {"name": "Cc", "value": "brooke.phillips@starpm.com"}, {"name": "Subject", "value": "QC Inspection Failed - Las Vistas 3C"}, {"name": "Date", "value": "2026-06-16T21:40:00+00:00"}, {"name": "Message-ID", "value": "<c9d5e1b4a3f6c0a8@gmail-mock>"}], "filename": "", "mimeType": "text/plain"}'::jsonb, 'Carlos, QC on 3C did not pass this afternoon. Punch items: living room baseboard touch-ups uneven, refrigerator and oven interiors dirty, bathroom towel ring installed rever', 'QC Inspection Failed - Las Vistas 3C', '["INBOX"]'::jsonb, 'a7f3c92e1b4d8e56', '2026-06-16T21:40:00.000000Z', '1781646000000', '2026-06-16T21:40:00.000000Z', '["brooke.phillips@starpm.com"]'::jsonb, 'jaime.salinas@starpm.com', '["carlos.mendez@starpm.com"]'::jsonb, '1781646000000', 486, FALSE);

-- L26: Gmail canonical closeout thread (6/18 Brooke -> Jaime)
INSERT INTO gmail.gmail_threads (id, snippet, created_at, history_id, last_internal_date, subject_normalized)
VALUES ('b8e4d0a3f2c5b9e7', 'Hey Jaime, 3C came off rework yesterday. When you finish today''s re-check, send Carlos the confirm and cc me. Denise is asking whether leasing can activate showings this a', '2026-06-18T12:58:00.000000Z', '1781787480000', '1781787480000', 'las vistas 3c - closeout package');
INSERT INTO gmail.gmail_messages (id, payload, snippet, subject, label_ids, thread_id, created_at, history_id, updated_at, cc_addresses, from_address, to_addresses, internal_date, size_estimate, has_attachments)
VALUES ('d0e6f2c5b4a70b19', '{"body": {"data": "SGV5IEphaW1lLAoKM0MgY2FtZSBvZmYgcmV3b3JrIHllc3RlcmRheS4gV2hlbiB5b3UgZmluaXNoIHRvZGF5J3MgcmUtY2hlY2ssIHNlbmQgQ2FybG9zIHRoZSBjb25maXJtIGFuZCBjYyBtZS4gRGVuaXNlIGlzIGFza2luZyB3aGV0aGVyIGxlYXNpbmcgY2FuIGFjdGl2YXRlIHNob3dpbmdzIHRoaXMgYWZ0ZXJub29uLgoKVGhhbmtzLApCcm9va2U", "size": 197}, "parts": [], "partId": "", "headers": [{"name": "From", "value": "brooke.phillips@starpm.com"}, {"name": "To", "value": "jaime.salinas@starpm.com"}, {"name": "Subject", "value": "Las Vistas 3C - closeout package"}, {"name": "Date", "value": "2026-06-18T12:58:00+00:00"}, {"name": "Message-ID", "value": "<d0e6f2c5b4a70b19@gmail-mock>"}], "filename": "", "mimeType": "text/plain"}'::jsonb, 'Hey Jaime, 3C came off rework yesterday. When you finish today''s re-check, send Carlos the confirm and cc me. Denise is asking whether leasing can activate showings this a', 'Las Vistas 3C - closeout package', '["INBOX"]'::jsonb, 'b8e4d0a3f2c5b9e7', '2026-06-18T12:58:00.000000Z', '1781787480000', '2026-06-18T12:58:00.000000Z', '[]'::jsonb, 'brooke.phillips@starpm.com', '["jaime.salinas@starpm.com"]'::jsonb, '1781787480000', 429, FALSE);

-- L25 anchor: Airtable rec291f423370e2a2db intentionally NOT modified.
-- L9 parameter traps: enforced at tool-call time, not by data.

-- L6: HubSpot canonical deal - Las Vistas 3C (older hs_lastmodifieddate = loses recency sort)
INSERT INTO hubspot.hubspot_objects (id, created_at, properties, updated_at, archived_at, object_type)
VALUES (
    'deal_c3a1b2e4f5d67890ab12cd34ef56789a',
    '2026-06-11T10:30:00-05:00',
    '{"amount": 15000.0, "dealname": "Las Vistas 3C - Leasing Activation", "closedate": "2026-07-15T17:00:00-05:00", "dealstage": "qualifiedtobuy", "company_id": "comp_mesaverde", "contact_id": "contact_2f6f1ae97cd25bf09d48fa927b197822", "createdate": "2026-06-11T10:30:00-05:00", "description": "Unit coming off second-pass make-ready rework. Denise Morales has a pending showing request from Catalina Reyes queued for this week. QC second-pass re-inspection scheduled for today 6/18. Once QC clears, advance to appointment-scheduled so leasing can confirm the showing. Do not release showing slot until QC signoff lands.", "hs_object_id": "deal_c3a1b2e4f5d67890ab12cd34ef56789a", "hubspot_owner_id": "owner_denise_morales", "hs_lastmodifieddate": "2026-06-11T10:30:00-05:00"}'::jsonb,
    '2026-06-11T10:30:00-05:00',
    NULL,
    'deals'
);

-- L6: HubSpot decoy deal - Las Vistas 9D (newer hs_lastmodifieddate = wins recency sort, same dealstage)
INSERT INTO hubspot.hubspot_objects (id, created_at, properties, updated_at, archived_at, object_type)
VALUES (
    'deal_d4b2c3e5f6a78901bc23de45fa6b7c8d',
    '2026-06-14T09:00:00-05:00',
    '{"amount": 14800.0, "dealname": "Las Vistas 9D - Leasing Activation", "closedate": "2026-07-20T17:00:00-05:00", "dealstage": "qualifiedtobuy", "company_id": "comp_mesaverde", "contact_id": null, "createdate": "2026-06-14T09:00:00-05:00", "description": "Unit at Las Vistas 9D cleared standard make-ready. Kevin Okafor reached out to three applicant referrals this week. No open holds -- unit is available for showing coordination pending leasing team calendar sync.", "hs_object_id": "deal_d4b2c3e5f6a78901bc23de45fa6b7c8d", "hubspot_owner_id": "owner_brooke_phillips", "hs_lastmodifieddate": "2026-06-20T15:45:00-05:00"}'::jsonb,
    '2026-06-20T15:45:00-05:00',
    NULL,
    'deals'
);

COMMIT;
