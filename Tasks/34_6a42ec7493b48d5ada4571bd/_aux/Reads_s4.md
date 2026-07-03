# Reads — S4

- `Tasks/34_6a42ec7493b48d5ada4571bd/8_Verifier_Fails.txt` :: 6 Run Detail blocks; rubrics R01/R03 fail 6/6; R04 fails 2/6 (Run 5, Run 6)
- `Tasks/34_6a42ec7493b48d5ada4571bd/5_Prompt.txt` :: Blessing operational damage-docket closeout; references Craig Apr 11 email, Marcus rider review, Mosaic precedent (carrier vs. client-facing pieces), walkup-assessment admission, David/Catalina handoff
- `Tasks/34_6a42ec7493b48d5ada4571bd/7_Rubrics.json` :: 22 rubrics, all outcome category; R01 = reply-to-email lock-in; R03 = hold-pending direction; R04 = walkup-assessment restate to Craig
- `Tasks/34_6a42ec7493b48d5ada4571bd/_aux/Hardness_Plan.md` :: 5 selected levers (L1 latching $1,200, L2 structured-DB skip, L7 multi-write, L8 multi-link chain, L11 net-vs-gross); 4 stump hypotheses (H1 customer-side docket miss, H2 Airtable/Mosaic skip, H3 wrong Slack channel, H4 Craig question unanswered)
- `Tasks/34_6a42ec7493b48d5ada4571bd/_aux/Trajectory_Stats.json` :: density 41.5 avg (THIN_DENSITY at 40-49 band), pass@1 0%, 0 error runs
- `Tasks/34_6a42ec7493b48d5ada4571bd/Agent_Responses/Run{1..6}_Trajectory.json` :: 6 completed trajectories; all 6 used `email_send_email` (fresh) instead of `email_reply_to_email` for Craig; all 6 directed Craig to "open formal claim now"
- `Tasks/34_6a42ec7493b48d5ada4571bd/_aux/Universe.txt` :: moveops
- `Reference/Linter_Playbook.md` :: AF justification style (first-person, concise, no em-dashes, no guide/spec references, cite concrete fact + specific gap)
- `Docs_moveops/12_Always_Failing_Rubrics.md` (if exists; falling back to `Docs/12_Always_Failing_Rubrics.md`) :: AF rubric patterns
- `Evals/4_Verifier_Fails_Eval.md` :: bucket taxonomy (Rubric Invalid / Judge Error / Legit Fail)
- `MoveOps_Base_Universe/6_Server_Tools_Details.json` :: tool catalog (confirmed `email_reply_to_email` exists with `email_id` + `content` parameters)
- `AGENTS.md` :: Pipeline Deviations table — "channel/method lock-in is Major by default when a valid alternative path exists" rule applied to R01
