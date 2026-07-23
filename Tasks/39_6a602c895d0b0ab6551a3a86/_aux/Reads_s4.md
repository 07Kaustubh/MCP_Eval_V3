# Reads — S4

- Reference/Sessions/S4.md :: full S4 runbook + StarPM V4 dual-model procedure + 5-point AF pre-write checklist + Bucket 1 ratio scoring
- Reference/Sessions/AGENTS.md :: skills / commands / runbook conventions
- Evals_starpm/4_Verifier_Fails_Eval.md :: StarPM V4 verifier-fails eval spec (dual-model, 8a/8b files, Agent_Responses/{Model}/ trajectory subfolders, environment-bug hard gate)
- Tasks/39_6a602c895d0b0ab6551a3a86/5_Prompt.txt :: shipped prompt — 15 lines, terse Jaime voice, no explicit threading instruction for Slack or Gmail
- Tasks/39_6a602c895d0b0ab6551a3a86/6_Oracle_Events.txt :: shipped OEs — OE24 (Gmail thread selection) + OE26/27 (Slack thread selection) both direct threading, but OE is a CB planning doc, NOT ground truth per StarPM V4 OE Authority Rule
- Tasks/39_6a602c895d0b0ab6551a3a86/7_Rubrics.json :: shipped rubrics — 32 rubrics all Outcome; rubric 20 (Gmail thread_ts) + rubric 24 (Slack thread_ts) + rubric 28 (calendarId=jaime) are the AF candidates
- Tasks/39_6a602c895d0b0ab6551a3a86/8a_Verifier_Fails_Opus.txt :: Opus verifier output — R1 29/32, R2 25/32, R3 25/32, R4 29/32, R5 25/32, R6 25/32; pass@1 = 0/6
- Tasks/39_6a602c895d0b0ab6551a3a86/8b_Verifier_Fails_Gemini.txt :: Gemini verifier output — R1 30/32, R2 31/32, R3 30/32, R4 31/32, R5 31/32, R6 31/32; pass@1 = 0/6
- Tasks/39_6a602c895d0b0ab6551a3a86/Agent_Responses/Opus/Run{1..6}_Trajectory.json :: Opus per-run trajectories; walked for rubric 20/24/28 classification
- Tasks/39_6a602c895d0b0ab6551a3a86/Agent_Responses/Gemini/Run{1..6}_Trajectory.json :: Gemini per-run trajectories; walked for rubric 20/24 classification
- Tasks/39_6a602c895d0b0ab6551a3a86/_aux/Hardness_Plan.md :: hardness levers L1/L8/L9/L25/L26 (post-S1.5 revision after L6 HubSpot removal); Stump Hypothesis 5 predictions to calibrate against actual AF outcomes
- Tasks/39_6a602c895d0b0ab6551a3a86/_aux/Trajectory_Stats_Opus.json :: measured Opus avg tool calls = 39.7 (min 30, max 50) — below 40-call floor
- Tasks/39_6a602c895d0b0ab6551a3a86/_aux/Trajectory_Stats_Gemini.json :: measured Gemini avg tool calls = 38.0 (min 28, max 59) — below 40-call floor
- Reference/Linter_Playbook.md :: AF justification voice (concise, first-person Jaime, no em-dashes, no framework references)
- Docs_starpm/12_Always_Failing_Rubrics.md :: (not present in Docs_starpm at time of read; used Docs/12_Always_Failing_Rubrics.md pattern reference instead)
- StarPM_Base_Universe/7_Server_Tools_Details.json :: tool catalog confirmed for parameter/tool checks (slack_send_message, create_draft, create_event, save_comment, save_issue, update_records_for_table)
