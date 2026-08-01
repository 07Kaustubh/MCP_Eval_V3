# REDO Reads Log — Tasks/45_6a6525d5201ac850ceb19a36

Reference/Sessions/REDO.md :: REDO = archive candidate originals -> clear in-place 5/6/7 -> FAIL feedback -> STOP. CB rebuild runs in fresh chats. Step 1 (confirm failure from trajectories) is a hard gate before any destructive step.
Reference/AGENTS.md :: confirmed REDO runbook mapping + card index.
AGENTS.md (root) :: Hard rule 1 (Opus 4.8 is the model under test). Hard rule 11 (V4 density 40+ average design target, per model; 15 = QC-spec fail floor). Rule 13 (future confirmed calendar event = open work).
Tasks/AGENTS.md :: per-task folder schema; _aux is safe-to-rebuild working state.
_aux/Trajectory_Stats.json :: authoritative computed numbers. Opus pass@1=1.0 (6/6 all rubrics), Gemini pass@1=0.5 (3/6), overall pass@1=0.75. difficulty_ok_at_40pct=false. avg_tool_calls_total=40.2 (Opus 37.0 / Gemini 43.3). verdict=REBUILD_CANDIDATE_DIFFICULTY.
Validators/parse_trajectories.py (fresh run) :: reproduced the above from Agent_Responses/{Opus,Gemini}/ + 8a/8b verifier fails. 40% difficulty ceiling encoded in the validator; verdict REBUILD_CANDIDATE_DIFFICULTY.
5_Prompt.txt :: candidate prompt under redo — Mesa Vista 4C June make-ready QC reconciliation (deep clean + interior repaint closure, vendor billed/unpaid reconciliation, mid-month re-inspection on calendar, sign-off-or-hold + ticket + channel post + email to Carlos + notify Brooke).
