# Reads log — HARDNESS phase · `Tasks/44_6a62ccba8cad60844b8364b9`

v11 E2 compliance gate. One line per reference doc / spec / data surface consulted.

## Pipeline contracts and specs

- `AGENTS.md` :: confirmed hard rules 1-13; rule 11 density is framework-scoped (V4 StarPM = 40+ avg PER MODEL, floor 15); rule 4 injection allowed for V4 but not needed here; rule 13 single-target uniqueness + every-service-incl-Calendar sweep + naive-agent simulation.
- `Reference/Sessions/HARDNESS.md` :: the phase contract — 6 required plan sections, StarPM-scoped density bands (>=40 PASS / 15-39 THIN / <15 INSUFFICIENT), >=3 levers, service-breadth gate, STOP-gate discipline.
- `Reference/Hardness_Playbook.md` :: the 11-lever catalog with per-lever tool-call cost ranges; composition rules (4-5 levers default, first link findable, every lever grounded in this task's split); "what hardness is NOT".
- `Tasks/_meta/Learnings.md` :: read end to end. L1-L7 do-not-rely block, L8-L14 reliable-lever block, L15-L21 prompt/rubric rules, L23-L31 + the 2026-07 numbered StarPM items. Entries carried into lever selection: L2, L6, L7, L9, L12, L13, L14, L15, L16, L24, L31, and StarPM items 3, 6, 11, 15, 16, 17, 18, 19, 20.
- `Docs_starpm/1_Project_Instructions_Overall.md` :: confirmed "average tool call count is 40+" is the V4 hard gate (Mar 12 2025 amendment row) and "many tool calls across multiple services".
- `Docs_starpm/11_Taxonomy.md` :: confirmed 40+ average tool calls; "if not, add more data, more stakes, and more asks".
- `Docs_starpm/10_How_To_Load_and_Edit_Universe.md` :: pass@k must be 0 < score <= 0.4 alongside the 40+ tool-call aim.
- `Validators/check_verification.py` :: required verification-doc sections (Sources consulted / Verification statements / Discrepancies surfaced / Verdict) and the three required source categories.
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: full tool catalog read for reachability + param traps. Confirmed every projected write path exists: `linear.save_issue` (accepts `status`), `linear.save_comment`, `linear.list_issue_statuses`, `slack.slack_send_message(channel_id, message, thread_ts?)`, `gmail.create_draft(to[], subject, body)` with NO send tool, `airtable.create_records_for_table` / `update_records_for_table`, `gcalendar.create_event(summary, startTime, endTime, ...)`. Learnings item 6 reachability check satisfied.

## Per-task data surfaces

- `_aux/S0_Setup_Report.md` :: 3,892 records / 33 tables; universe today 2026-07-01 America/Chicago; 59 post-today records; Jaime ranks 15th by artifact density (48 mentions), so levers must be built on the surface around her, not on a Jaime-led scenario.
- `_aux/Universe_Index/today_horizon.json` :: universe today 2026-07-01; last event 2026-12-30.
- `_aux/Universe_Index/graph_report.md` :: co-actor density (tony.reyes 862, brooke.phillips 740, carlos.mendez 525, elias.navarro 40); Linear state distribution by `state_id`; Slack C001=104 / C004=144.
- `_aux/Universe_Index/key_facts.md`, `service_inventory.md`, `entities_personas.md`, `accounts_per_entity.md` :: per-service record counts; confirmed no GL/entity/account surface (single-entity property-management universe).
- `_aux/Fact_Ledger.json` :: atom counts (206 emails, 403 amounts, 192 dates, 230 Linear issue ids, 48 Linear comment ids, 8 Slack channels, 61 personas) used to confirm lever feasibility.
- `_aux/Feasible_Surface.json` :: 15 tables / 19 enum columns — confirms the `tblMakeReady` and `tblMaintenanceTickets` enum vocabularies for any Airtable write.
- `_aux/Universe_Split/linear.linear_issues.json` + `linear_comments.json` + `linear_workflow_states.json` + `linear_projects.json` + `linear_users.json` :: the load-bearing surface. State-id map confirmed (`state_OPS_0`=Backlog, `_1`=Todo, `_2`=In Progress, `_3`=In Review, `_4`=Done).
- `_aux/Universe_Split/slack.slack_messages.json` + `slack_channels.json` + `slack_users.json` :: full C001 read (104 messages) plus keyword sweep across all 8 channels.
- `_aux/Universe_Split/airtable.airtable_records.json` + `airtable_fields.json` :: 120 `tblMakeReady` + 50 `tblMaintenanceTickets` rows; field/enum schema for both tables.
- `_aux/Universe_Split/gcalendar.gcalendar_events.json` :: all 565 rows swept, including the mandatory future-event sweep (rule 13 / F9 / Learnings item 15).
- `_aux/Universe_Split/gmail.gmail_messages.json` :: keyword sweep with base64 body decoding (Learnings item 17 confirmed — bodies are base64, `snippet` is the only plaintext and it truncates).
- `_aux/Universe_Split/quickbooks.quickbooks_entities.json` :: 8 vendors + 134 HVAC-keyword entities inspected; deliberately EXCLUDED from the lever set (rationale recorded in the plan).
- `_aux/Universe_Split/contacts.contacts.json` :: confirmed Jaime Salinas (Quality Control Inspector), Brooke Phillips (Apartment Property Supervisor), Elias Navarro (Lead Maintenance Technician), Carlos Mendez / Lisa Smith (Onsite Property Managers).
- `Tasks/39_*/5_Prompt.txt`, `40_*`, `41_*`, `42_*`, `43_*` :: read the shipped StarPM prompts to steer the scenario away from the prior five (similarity pre-check).

## Eval spec sub-dims relevant to this phase

- Trajectory / Tool Call Count :: V4 average 40+ per model is the design target; 15 is the QC-spec fail floor.
- Trajectory / pass@1 :: 0 < pass@1 <= 40%, which is what the lever selection is engineered against.
- `Evals_starpm/5_Submission_Gate_Eval.md` families F7 / F8 / F9 :: pre-registered as constraints on the S1/S3 write-target design, not deferred.
