# Reads log — S4 (Tasks/41_6a61a86a3453b3714bdc72ef)

- Reference/Sessions/S4.md :: S4 runbook; V4 dual-model section (Opus + Gemini), bucket taxonomy, All-Failing sub-dim scoring
- Evals_starpm/4_Verifier_Fails_Eval.md :: authoritative 3-bucket taxonomy (Rubric Invalid / Judge Error / Legit Fail), Phase 1-4, AF-validity Step 5, environment-bug hard gate
- Reference/Linter_Playbook.md :: AF justification style (2-4 sentences, no em-dashes, no process leakage) + AF template + examples
- 5_Prompt.txt :: shipped prompt (Patricia Nguyen closing Tanya Mitchell filing package — balance, eviction status, unit hold, 4 write deliverables)
- 6_Oracle_Events.txt :: OE list (referenced via rubric justifications; OE 15/17 = petition-not-filed + owner-approved)
- 7_Rubrics.json :: 20 rubrics, all Outcome
- 8a_Verifier_Fails_Opus.txt / 8b_Verifier_Fails_Gemini.txt :: per-model verifier output, all 6 runs each
- Agent_Responses/{Opus,Gemini}/trajectory-run-*.json :: 12 trajectories (spot-checked $2,287.50 present 12/12, $1,832 absent, harry.harris in Opus 1-5, QR-2026-0441 only a dir-listing filename)
- _aux/Trajectory_Stats.json :: pass@1=0.0 both models, density 43.4 total / 29.6 mcp, verdict OK
- _aux/Hardness_Plan.md :: 5 selected levers (L2 structured-DB skip flagship, L10 reversal, L1 latching, L11 net-vs-gross, L31 Gemini negative-directive) + 5 stump hypotheses
- Universe_Split/quickbooks.quickbooks_entities.json :: bill QR-2026-0441 (847/925/210 + 150 credit, Balance 2132, VendorRef Alamo HVAC, no CustomerRef); invoice 7214 (1125/975/187.50 + 5885.94 credit, Balance 0, CustomerRef Tanya); bill 2026-EV-047 ($185 filing-prep decoy)
- Universe_Split/contacts.contacts.json :: harry.harris + linda.castillo BOTH "Property Owner"; john.castillo = Water Delivery Rep decoy
- Universe_Split/airtable.airtable_records.json :: tblMakeReady recc83c05d889b354 (current JP-coord) + reca8230a8fd9ff51 (identity anchor "Sunset Ridge Unit 14"); superseded chain receee45491536859/rec3782834f35df50/rec91517a5acab558; Rio Bend decoy rec94e86a3007dd5e (selReady); EVF-2026-014 rec922b9a2d1b9451 (owner auth = Linda Castillo)
- Universe_Split/gmail.gmail_messages.json :: eviction-auth thread — Brooke request → Linda Castillo authorization reply (06-30)
- Universe_Split/linear.linear_issues.json :: OPS-32 "Eviction Hearing - Mitchell, Harris Property" — stale latching decoy (hearing set, Harry Harris owner)
- Validators/check_justification.py :: forbidden-term scanner (rubric numbers, internal artifacts, script/phase names, universe meta)
- _aux/Council_Reports/S4_{fixes,judge_errors,verdict}.md (prior pass) + S4_AF_justifications.md :: prior-chat classification + the R6/OE-14 fix history — reconciled against this post-fix re-grade
- Agent_Responses raw parse (this run) :: per-run tool-call extraction — Opus schema (message.content[].tool_use) + Gemini schema (top-level type:tool_use with tool_name/parameters); confirmed create_draft recipients, C004 slack bodies, and final-result balance figures first-hand
