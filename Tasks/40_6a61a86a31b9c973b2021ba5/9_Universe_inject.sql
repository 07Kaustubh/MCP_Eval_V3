-- =============================================================================
-- Task 40_6a61a86a31b9c973b2021ba5 -- Universe injection
-- Scenario: Water heater failure at Mesa Vista Unit 7B, scope-correction on
-- 2026-07-01. Carlos Mendez (Onsite PM) must catch that the vendor + Tony Reyes
-- endorsed narrow scope (heat exchanger swap, ~$310) is contradicted by the
-- diagnostic bill's Line[0].Description which recommends full unit replacement.
--
-- Levers activated by these injections:
--   L1 Latching                 -- resolved Unit 14 water-heater incident
--                                  (Tommy Reyes / Linda Castillo, 5/15-5/27)
--                                  is already in base universe as decoy
--   L2 QB structured-DB skip    -- record 6 (bill Line[0].Description)
--   L5 Slack thread-reply blind -- records 3 + 4 (parent + hidden reply)
--   L7 Multi-write diversification (5+ writes across 5 services) -- landing
--                                  targets seeded by records 1, 5, 6, 7
--   L8 Multi-link chain          -- Slack (records 3-4) -> Airtable (record 1)
--                                  -> Linear (record 5) -> QB bill (record 6)
--   L9 Authority-figure dismissal -- record 2 (Tony Reyes)
--
-- FK targets (verified in StarPM_Base_Universe/Data/):
--   Carlos Mendez slack user  U07E4512181
--   Tony  Reyes  slack user  UD4432C1F56
--   Slack channel #maintenance C001
--   Airtable user Carlos  usr_carlos_mendez
--   Airtable table  tblMaintenanceTickets (base appPropertyOps)
--   Linear team  team_001 (OPS)
--   Linear In Progress state  state_OPS_2
--   Linear user Carlos  user_d6c1beb9cf67594dae2f5de4529674f1
--   QB vendor Hill Country Plumbing  id 201
--
-- IDs assigned as next-unused (collision-checked against base):
--   Airtable record  rec92f4a1c8e17bd3   Ticket  MT-2026-1327 (last base 1326)
--   Slack msg IDs    3 fresh 32-hex values, ts .000301..000303 (last base .000293)
--   Linear issue     OPS-231 (last base OPS-230), number 231
--   QB bill entity   id 195836274018, DocNumber B2026-211 (last base B2026-210)
--   Gmail thread     d1e2f3a4b5c6789a, message e2f3a4b5c6d789ab (16-hex)
--
-- Time window: all records fall within 2026-05-01 to 2026-07-01 (America/Chicago).
-- Business communications on weekdays (Mon 2026-06-29, Tue 2026-06-30).
-- =============================================================================


-- -----------------------------------------------------------------------------
-- Record 1 -- Airtable maintenance ticket (Mesa Vista Unit 7B)
-- Landing target for L7 (priority write) and L8 chain hop 2.
-- Priority intentionally selMedium at creation; the evening thread reply
-- (record 4) is what should flip Carlos to selHigh.
-- -----------------------------------------------------------------------------
INSERT INTO airtable.airtable_records (
    id, table_id, fields, created_time, last_modified_time,
    created_by_id, last_modified_by_id
) VALUES (
    'rec92f4a1c8e17bd3',
    'tblMaintenanceTickets',
    '{"fldPriority": "selMedium", "fldDescription": "Water heater assessment at Mesa Vista Unit 7B. Tenant reported dripping and intermittent hot water on 06-29 evening. Hill Country Plumbing completed diagnostic 06-29 afternoon. Scope call pending before Thursday install slot.", "fldTicketNumber": "MT-2026-1327", "fldCompletionDate": ""}'::jsonb,
    '2026-06-29 21:14:00',
    '2026-06-29 21:14:00',
    'usr_carlos_mendez',
    'usr_carlos_mendez'
);


-- -----------------------------------------------------------------------------
-- Record 2 -- Slack C001 (#maintenance) top-level -- L9 Authority dismissal
-- Tony Reyes (Lead Maintenance Technician) posts a plausible narrow-scope
-- endorsement. Frames as cheaper path on Robert's June budget with EOD tomorrow
-- silent-approval default. The truth in the QB bill's Line[0].Description
-- contradicts on tank condition.
-- -----------------------------------------------------------------------------
INSERT INTO slack.slack_messages (
    id, ts, channel_id, type, user_id, text,
    thread_parent_id, thread_ts_legacy,
    reply_count, reply_users_count, latest_reply,
    is_activity_message, subtype,
    reactions_json, files_json, attachments_json,
    created_at
) VALUES (
    'a1b2c3d4e5f6789012345678901234ab',
    '1782789240.000301',
    'C001',
    'message',
    'UD4432C1F56',
    'Hill Country came by Mesa Vista 7B this afternoon. Diagnostic came back: heat exchanger is failing but the tank tested sound on the pressure hold. They quoted the exchanger swap only, about 310 dollars, install Thursday AM. Cheaper path and keeps us on Robert''s June budget. Going to approve unless someone flags before EOD tomorrow.',
    NULL, NULL,
    0, 0, NULL,
    false, NULL,
    '[]', '[]', '[]',
    '2026-06-30 03:14:00+00:00'
);


-- -----------------------------------------------------------------------------
-- Record 3 -- Slack C001 (#maintenance) parent -- Carlos-relayed tenant framing
-- Morning update from Carlos framing situation as low urgency ("no rush,
-- kids at grandma's"). Records reply_count=1 and latest_reply pointing to
-- record 4's ts (the priority-flipping evening reply).
-- -----------------------------------------------------------------------------
INSERT INTO slack.slack_messages (
    id, ts, channel_id, type, user_id, text,
    thread_parent_id, thread_ts_legacy,
    reply_count, reply_users_count, latest_reply,
    is_activity_message, subtype,
    reactions_json, files_json, attachments_json,
    created_at
) VALUES (
    'b2c3d4e5f6a789012345678901234abc',
    '1782824160.000302',
    'C001',
    'message',
    'U07E4512181',
    'Update from Tanya at Mesa Vista 7B this morning: small drip under the water heater, hot water is coming and going. She said no rush, kids are at grandma''s this week. Logging under medium priority for now.',
    NULL, NULL,
    1, 1, '1782863220.000303',
    false, NULL,
    '[]', '[]', '[]',
    '2026-06-30 12:56:00+00:00'
);


-- -----------------------------------------------------------------------------
-- Record 4 -- Slack C001 thread reply -- L5 Hidden thread reply
-- Evening reply from Carlos: no hot water, water pooling, kids back home
-- tonight. Flips the ticket priority. Reachable ONLY via slack_get_thread
-- on record 3's ts. Does NOT state "full unit replacement" -- that scope
-- truth lives only in the QB bill line description (record 6).
-- -----------------------------------------------------------------------------
INSERT INTO slack.slack_messages (
    id, ts, channel_id, type, user_id, text,
    thread_parent_id, thread_ts_legacy,
    reply_count, reply_users_count, latest_reply,
    is_activity_message, subtype,
    reactions_json, files_json, attachments_json,
    created_at
) VALUES (
    'c3d4e5f6a7b89012345678901234abcd',
    '1782863220.000303',
    'C001',
    'message',
    'U07E4512181',
    'Following up on Tanya at 7B. She just called: no hot water since 4 PM and there is a puddle spreading on the kitchen floor now. Kids are back home tonight. Bumping this back up. We need to move on the scope call today or first thing tomorrow.',
    'b2c3d4e5f6a789012345678901234abc',
    '1782824160.000302',
    0, 0, NULL,
    false, NULL,
    '[]', '[]', '[]',
    '2026-06-30 23:47:00+00:00'
);


-- -----------------------------------------------------------------------------
-- Record 5 -- Linear issue OPS-231 (In Progress, assignee Carlos, priority High)
-- Landing target for L7 (Linear write) and L8 chain hop 3. Description
-- redirects to "diagnostic bill on file" (the QB bill in record 6). Agents
-- that read only the Linear body and skip QB will not surface the scope truth.
-- -----------------------------------------------------------------------------
INSERT INTO linear.linear_issues (
    id, uuid, team_id, title, description, number,
    state_id, project_id, cycle_id, milestone_id, parent_id,
    assignee_id, creator_id, priority, estimate, due_date,
    completed_at, label_ids, is_archived, url,
    git_branch_name,
    sla_started_at, sla_medium_risk_at, sla_high_risk_at,
    sla_breaches_at, sla_type,
    created_at, updated_at
) VALUES (
    'OPS-231',
    'a5b3c9d2-4e8f-4a7b-9c1e-2f6d8b3a5c7e',
    'team_001',
    'Mesa Vista 7B water heater diagnostic and scope decision',
    'Tenant reported leak evening 2026-06-29. Hill Country Plumbing on-site same-day afternoon; diagnostic bill on file with vendor id 201. Scope decision pending before Thursday AM install slot. See #maintenance thread and Airtable ticket for context.',
    231,
    'state_OPS_2',
    NULL, NULL, NULL, NULL,
    'user_d6c1beb9cf67594dae2f5de4529674f1',
    'user_d6c1beb9cf67594dae2f5de4529674f1',
    2, NULL, NULL,
    NULL, '[]'::jsonb, false,
    'https://linear.app/synthetic/issue/OPS-231',
    '',
    NULL, NULL, NULL, NULL, NULL,
    '2026-06-29T22:20:00-05:00',
    '2026-06-30T18:47:00-05:00'
);


-- -----------------------------------------------------------------------------
-- Record 6 -- QuickBooks bill B2026-211 -- L2 Load-bearing structured-DB record
-- Diagnostic-visit bill from Hill Country Plumbing (vendor 201). The scope
-- truth lives inside properties.Line[0].Description:
--   "Corrosion visible on burner assembly and tank base, thermocouple out,
--    heat exchanger cracked. Full unit replacement recommended..."
-- Agents that skim TotalAmt via list_entities and skip the line expansion
-- will lock in the vendor + Tony narrow scope from records 2 and 7.
-- -----------------------------------------------------------------------------
INSERT INTO quickbooks.quickbooks_entities (
    entity_type, id, sync_token, properties, active,
    created_time, last_updated_time
) VALUES (
    'bill',
    '195836274018',
    '1',
    '{"Line": [{"Id": "1", "Amount": 185.0, "DetailType": "AccountBasedExpenseLineDetail", "Description": "Diagnostic visit, 12 yr Ruud RS75 water heater at Mesa Vista Unit 7B. Corrosion visible on burner assembly and tank base, thermocouple out, heat exchanger cracked. Full unit replacement recommended, approx 1850 dollars for equal model swap. Piecemeal repair not advised on unit this age.", "SalesItemLineDetail": null, "AccountBasedExpenseLineDetail": {"AccountRef": {"name": "Repairs & Maintenance", "value": "60"}}}], "Balance": 185.0, "DueDate": "2026-07-29", "TxnDate": "2026-06-29", "MetaData": {"CreateTime": "2026-06-29T21:45:00Z", "LastUpdatedTime": "2026-06-29T21:45:00Z"}, "TotalAmt": 185.0, "DocNumber": "B2026-211", "VendorRef": {"name": "Hill Country Plumbing", "value": "201"}, "PrivateNote": "Diagnostic only. Full replacement quote to follow on approval."}'::jsonb,
    true,
    '2026-07-01T14:00:00.000000Z',
    '2026-07-01T14:00:00.000000Z'
);


-- -----------------------------------------------------------------------------
-- Record 7a -- Gmail thread -- container for Hill Country vendor message
-- -----------------------------------------------------------------------------
INSERT INTO gmail.gmail_threads (
    id, history_id, snippet, subject_normalized,
    last_internal_date, created_at
) VALUES (
    'd1e2f3a4b5c6789a',
    '1782763920000',
    'Carlos, our tech was out at Mesa Vista Unit 7B this afternoon. Diagnostic summary attached. Bottom line for the quick call: the heat exchanger is failing and the thermocouple is out, but the tank held pressure on',
    'mesa vista 7b water heater diagnostic summary and next steps',
    '1782763920000',
    '2026-07-01T14:00:00.000000Z'
);


-- -----------------------------------------------------------------------------
-- Record 7b -- Gmail message from Hill Country to Carlos
-- Vendor-side scope narrative that mirrors Tony's authority dismissal. Body
-- text does NOT state "full unit replacement" -- that truth is only in the
-- QB bill Line[0].Description (record 6). Agents that read Gmail and stop
-- there lock in the narrow scope.
-- payload.body.data is base64 of the plaintext body (487 bytes).
-- -----------------------------------------------------------------------------
INSERT INTO gmail.gmail_messages (
    id, thread_id, history_id, label_ids, snippet,
    internal_date, size_estimate, payload,
    from_address, to_addresses, cc_addresses,
    subject, has_attachments,
    created_at, updated_at
) VALUES (
    'e2f3a4b5c6d789ab',
    'd1e2f3a4b5c6789a',
    '1782763920000',
    '["INBOX"]'::jsonb,
    'Carlos, our tech was out at Mesa Vista Unit 7B this afternoon. Diagnostic summary attached. Bottom line for the quick call: the heat exchanger is failing and the thermocouple is out, but the tank held pressure on',
    '1782763920000',
    487,
    '{"body": {"data": "Q2FybG9zLCBvdXIgdGVjaCB3YXMgb3V0IGF0IE1lc2EgVmlzdGEgVW5pdCA3QiB0aGlzIGFmdGVybm9vbi4gRGlhZ25vc3RpYyBzdW1tYXJ5IGF0dGFjaGVkLiBCb3R0b20gbGluZSBmb3IgdGhlIHF1aWNrIGNhbGw6IHRoZSBoZWF0IGV4Y2hhbmdlciBpcyBmYWlsaW5nIGFuZCB0aGUgdGhlcm1vY291cGxlIGlzIG91dCwgYnV0IHRoZSB0YW5rIGhlbGQgcHJlc3N1cmUgb24gdGhlIGhvbGQgdGVzdC4gUmVjb21tZW5kaW5nIGV4Y2hhbmdlciBzd2FwIHBsdXMgYSBuZXcgdGhlcm1vY291cGxlLCBhbGwgbGFib3IgYW5kIHBhcnRzIGFib3V0IDMxMCBkb2xsYXJzLiBXZSBjYW4gYmUgb24gc2l0ZSBUaHVyc2RheSBtb3JuaW5nIGlmIHlvdSBhcHByb3ZlLiBQbGVhc2UgY29uZmlybSBzY29wZSBieSBlbmQgb2YgYnVzaW5lc3MgdG9tb3Jyb3cgc28gd2UgY2FuIGdldCBwYXJ0cyBwdWxsZWQuIFRoYW5rcy4gRGlhbmUgYXQgSGlsbCBDb3VudHJ5IFBsdW1iaW5nLg==", "size": 487}, "parts": [], "partId": "", "headers": [{"name": "From", "value": "ap@hillcountryplumbing.com"}, {"name": "To", "value": "carlos.mendez@starpm.com"}, {"name": "Subject", "value": "Mesa Vista 7B water heater diagnostic summary and next steps"}, {"name": "Date", "value": "2026-06-29T20:12:00+00:00"}, {"name": "Message-ID", "value": "<e2f3a4b5c6d789ab@gmail-mock>"}], "filename": "", "mimeType": "text/plain"}'::jsonb,
    'ap@hillcountryplumbing.com',
    '["carlos.mendez@starpm.com"]'::jsonb,
    '[]'::jsonb,
    'Mesa Vista 7B water heater diagnostic summary and next steps',
    false,
    '2026-07-01T14:00:00.000000Z',
    '2026-07-01T14:00:00.000000Z'
);
