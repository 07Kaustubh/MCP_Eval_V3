# Reads S2 — 39_6a602c895d0b0ab6551a3a86

Reference-doc reading log for the S2 phase. Log every QC spec doc / Reference card / Eval spec / universe file consulted while authoring the fresh REDO OE against R5 prompt.

## Reference cards + format guides
- `Reference/OE_Format.md` :: confirmed numbered-prose format, no em-dashes, real tool names, real parameters with concrete expected values; OE-to-rubric mapping (write action → Outcome 1.1, content requirement → Outcome 1.2, key fact reported → Outcome 2.1); OE authority rule ML-confirmed July 2026 (OEs are CB planning docs, universe is SSOT).
- `Reference/OE_Convention_Inventory.json` :: verified allowed opening-phrase patterns (search_first, action_first, inspect_first, lookup_first), hard parameter traps table, Conclude: clause pattern, branching phrasing form, anti-patterns list.
- `Reference/Hardness_Playbook.md` :: verified StarPM lever composition rules for L1 latching + L8 multi-link chain + L9 param traps + L25 anchor + L26 decoy parent (L6 HubSpot dropped per S1.5 REVISION UPDATE).

## Eval spec
- `Evals_starpm/1_Prompt_Eval.md` :: previously consulted in S1; not re-read for S2 (out of phase scope).
- `Evals_starpm/2_Oracle_Events_Eval.md` :: file not present in this pipeline copy; per AGENTS.md the OE Completeness + OE Accuracy sub-dims are inherited from V3 Brookfield eval spec `Evals/2_Oracle_Events_Eval.md` (verified via Council B B1+B2 protocol in this project).

## QC spec
- `Docs_starpm/` :: OE sub-dim scoring rules verified from `Docs_starpm/7_QC_Spec_Doc1.json` (Oracle Event dimension: OE Completeness sub-dim, OE Accuracy sub-dim); each OE step maps to a prompt sentence (Completeness) and each OE parameter binding is grounded to the per-task universe atom (Accuracy).

## Per-task universe (from _aux/Universe_Split/)
- `airtable.airtable_records.json` :: verified rec291f423370e2a2db (Las Vistas 3C) fldTurnStatus=selReady, fldTargetReady=2026-06-18, fldNotes2 ends with Brooke's supervisory retrospective narrative — Jaime's active first-person signoff line is not yet written.
- `airtable.airtable_bases.json` + `airtable.airtable_tables.json` :: base id `appPropertyOps`, table id `tblMakeReady`.
- `linear.linear_issues.json` + `linear.linear_workflow_states.json` :: team_001 workflow states state_OPS_3 (In Review, started) and state_OPS_4 (Done, completed).
- `linear.linear_comments.json` :: Bennett rework-complete comments confirmed on OPS-224 (comment_a1c47e2d3f8b41e6b9d21c9f4a5e7b02, 2026-06-17T16:44), OPS-225 (comment_b2d58f3e4a9c52f7c0e32d0a5b6f8c13, 2026-06-17T11:19), OPS-226 (comment_c3e69a4f5bad63a8d1f43e1b6c709d24, 2026-06-16T15:34). Note: user_id=null in the split (S1 verification flag) — attribution to Bennett grounded on body content, not user_id.
- `linear.linear_users.json` :: Jaime user_d3186a640f425ae0b69423f09aa4d7ec / Brooke user_0aa171072660514bb4e76ed0fae5bdb9 / Carlos user_d6c1beb9cf67594dae2f5de4529674f1 / Bennett user_8cd13ca90bca5494ab86e300c4b7829b / Sandra user_02f411243d8f550daf3f13d46eb13979.
- `slack.slack_messages.json` :: Slack C004 3C-related parents catalogued — R7 canonical id 03e5b7c4a9fb5d803c7e1b4a52d69f7c ts 1781788320.000202 (Brooke 6/18 morning ping); R5 decoy id 01c3f5a2e7d94b681a5c9f2e30b47d5a ts 1781645520.000200 (Jaime 6/16 QC-FAIL punch list); pre-existing e9cd06014caf5ce4165ada66fdf6e03a (Jaime 6/16 initial fail post) + a72e1b1fd9d27a15ef45ef804ac4df5d (Jaime 6/18 second-pass QC approved) + 1a139eb97c10aa2dca3b1e802452c9c1 (Brooke 6/18 supervisory-close reply).
- `slack.slack_channels.json` :: C004 confirmed as #make-ready (public).
- `slack.slack_users.json` :: Sandra Allen id `UADB2B4E045` — required for the @-mention format in OE27.
- `gmail.gmail_threads.json` + `gmail.gmail_messages.json` :: canonical thread b8e4d0a3f2c5b9e7 subject "Las Vistas 3C - closeout package" message d0e6f2c5b4a70b19 (Brooke 6/18 to Jaime); decoy thread a7f3c92e1b4d8e56 subject "QC Inspection Failed - Las Vistas 3C" (Jaime 6/16 to Carlos); additional pre-rework fail thread 9f0bd31ccf588236 subject "Las Vistas 3C QC punch list" (Jaime to Carlos, pre-6/16).
- `contacts.contacts.json` :: Brooke c46d47256fd95ca6aca770c8dddda5eb / Carlos 8608e0778a655232982787cef4fac0b2 / Bennett 9f49e592505f5fac8e91d72c7c745f26 / Sandra ae1dbd31ad1450a3b781c8c96c0ecf43.

## Tool catalog
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: verified tool signatures for the phase — airtable (list_bases, list_tables_for_base, get_table_schema, search_records, update_records_for_table with camelCase baseId/tableId/records), contacts (contacts_search_contacts with query), linear (list_issues with team+query, get_issue, list_comments, save_comment with issueId+body, save_issue with id+state, list_issue_statuses with team), gmail (search_threads with query, get_thread with threadId, create_draft with to+cc+subject+body+replyToMessageId — DRAFT ONLY, no send tool, body NOT content), gcalendar (list_events with calendarId+startTime+endTime+timeZone+fullText, create_event with summary+startTime+endTime+calendarId+timeZone+description). Slack tool details per AGENTS.md StarPM constants — slack_send_message(channel_id, message, thread_ts) with message NOT payload NOT text; slack_read_channel(channel_id); slack_send_message_draft exists but only drafts (never sends).

## Upstream phase artifacts
- `_aux/Hardness_Plan.md` :: S1.5 REVISION UPDATE confirmed — L6 HubSpot dropped, soft-lever amplifiers added (Bennett per-ticket verify, Airtable pre-read, Sandra contacts lookup), density midpoint target 57.5, L31 realization projection Opus ~42.6 / Gemini ~40.3.
- `_aux/Verification_s1.md` :: R5 prompt confirmed PASS with 7 downstream non-blocking flags for S2/S3 — Bennett user_id=None flag applied to OE13-15 (attribution via body content), null-GCal-showings flag applied to OE28 (null result acceptable), Slack "formal close" distinctness flag applied to OE26/OE27 (operational-cascade-completion signal vs prior QC-pass declarations).
- `_aux/Fact_Ledger.json` :: atoms for the 4 personas + Sandra + injected R5-R11 records verified.
- `_aux/Candidate_Originals/6_Oracle_Events.txt` :: prior-art reference from the density-failed original build — 20 OEs, ~29 required calls, realized Opus avg 37.5 / Gemini avg 35.5. Structural scaffold kept; deltas applied for R5 (Sandra add, HubSpot drop, Bennett-verify strengthen, Airtable pre-read strengthen, decoy-observation expand).

## Cross-source verification notes
- Bennett comment user_id=null in split. Ground OE attribution on body content ("Sanded and repainted the uneven touch-up sections", "Recleaned the refrigerator interior", "Removed the towel ring beside the vanity") rather than a user_id assertion.
- R5 prompt drops the L6 HubSpot leg despite the S1 lever table row line-item remaining in the Verification_s1 table. The OE MUST NOT reintroduce a HubSpot deal-update chain.
- Sandra Allen tag format in OE27 uses the Slack canonical `<@UADB2B4E045>` mention so the tag routes to her.
