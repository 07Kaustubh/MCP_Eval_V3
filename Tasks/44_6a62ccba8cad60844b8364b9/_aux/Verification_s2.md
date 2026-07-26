# Verification — S2 (v16 cross-source check)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm (V4) · **Universe today:** 2026-07-01 (America/Chicago)
**Deliverable:** `6_Oracle_Events.txt` — 38 numbered OE steps, zero em/en dashes, pure ASCII, sequential, every step naming a real tool with real parameters.

## Sources consulted

**Per-task data** — per-task universe (`_aux/Universe_Split/`, every value retrieved first-hand this phase, not inherited from S0/S1 reports)

- `linear.linear_issues.json` (230 rows) :: every issue the OE cites pulled individually with `state_id`, `assignee_id`, `project_id`, `created_at`, title and description. OPS-16/17/18 (Elias scope, three clusters only), OPS-34 (signage title, Done, carries Jaime's 2026-05-21T09:00 coil/plumbing/panel comment), OPS-35 (West scope, In Progress, Lisa onsite lead + John execution lead), OPS-40 (Done), OPS-43 (South, In Progress), OPS-44 (Backlog), OPS-56 (North access, In Progress), OPS-66 and OPS-81 (Elias North-complete claims, In Review / In Progress), OPS-87 (**Todo**), OPS-91 (Done, inverted prose), OPS-96 (**Todo**), OPS-97 (Todo), OPS-98 (**In Progress**), OPS-99 / OPS-108 (identical East titles, In Progress / Backlog), OPS-186 (Todo, 2026-06-17, West still underway), OPS-224/225/226 (Jaime-created, James Bennett-assigned, all Done).
- `linear.linear_workflow_states.json` :: `state_OPS_0` Backlog, `_1` Todo, `_2` In Progress, `_3` In Review, `_4` Done, all on team_001.
- `linear.linear_teams.json` :: `team_001` key OPS name Operations; charter names Airtable Maintenance Tickets as system of record, Linear secondary.
- `linear.linear_projects.json` :: proj_001 Property Ops, proj_002 Summer Make-Ready Program, proj_003 Preventive Maintenance Push. Issue counts 97 / 73 / 60.
- `linear.linear_comments.json` (48 rows) :: per-issue walk on OPS-34 (**16** comments), OPS-43 (2), OPS-56 (2), OPS-81 (2), OPS-96 (1), OPS-97 (1), OPS-98 (2), OPS-108 (2).
- `linear.linear_users.json` :: Jaime = `user_d3186a640f425ae0b69423f09aa4d7ec`; assignee histogram gives her exactly 3 issues.
- `slack.slack_messages.json` (580 rows; C001 = 104) :: every `ts` in the OE verified for channel, author, timestamp, text and thread parentage. Parentage read from `thread_parent_id`, because `thread_ts` is null throughout this dataset. C001 carries 37 distinct thread parents.
- `slack.slack_channels.json` :: C001 #maintenance through C008 #applications.
- `slack.slack_users.json` :: Jaime has 1 message in C001 and 6 in C004 (channel lock-in trap live).
- `airtable.airtable_bases.json` / `_tables.json` / `_fields.json` / `_records.json` :: `appPropertyOps`; `tblMaintenanceTickets` with exactly 4 fields and no owner or status field; 50 ticket rows of which 18 carry the token HVAC and zero reference a cluster, the push, a condensate drain, 20x25 filters or a hose bib.
- `gcalendar.gcalendar_calendars.json` / `_events.json` (565 rows) :: 20 per-persona calendars all America/Chicago; Jaime's calendar carries exactly 10 events, latest 2026-06-02; the Kick-Off is materialised only on the brooke.phillips / lisa.smith / patricia.nguyen / teresa.wood calendars.
- `gmail.gmail_threads.json` (156) + `gmail.gmail_messages.json` (484) :: zero push threads in either store.
- `contacts.contacts.json` (61) :: all seven cited addresses and job titles exact.
- `_aux/Fact_Ledger.json` :: consulted. **`lifecycle.today` was `null`** (pre-declared defect A-11 / N6); backfilled to `"2026-07-01"` in this phase per the AUDIT instruction that the fix land before S2.
- `_aux/Verification_s1.md` :: reviewed. Its five discrepancies were carried; items 1 (date anchor), 3 (prefer non-Linear reads) and 5 (Lever 8 hop B is OPS-34, title actively misleading) are the three that bound this phase.
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: every tool name and parameter signature in the OE verified against the catalog. `save_issue.assignee` is declared `type: "null"` and cannot carry a value, which is why the OE routes owner names into `description` text.

**Eval spec** — `Evals_starpm/2_OE_Eval.md` (OE Completeness / OE Accuracy bands, Phase 1.2 no-reasoning-steps rule, Phase 2.4 T9 act-vs-defer hard gate, Phase 2.5 date consistency, Phase 4.0 pre-verdict sweep) and `Evals_starpm/5_Submission_Gate_Eval.md` (F7 / F8 / F9 applied at design time).

**QC spec** — `Docs_starpm/7_QC_Spec_Doc1.json` Oracle Event dimension (both sub-dim band definitions taken verbatim), `Docs_starpm/8_QC_Spec_Doc2.md` (severity taxonomy), `Docs_starpm/2_Rubrics_V3_Guidelines.md` (OE-to-rubric mapping and the three-condition Process test), `Docs_starpm/1_Project_Instructions_Overall.md` Step 3.5. `Docs_starpm/13_QC_Companion.md` deliberately not used as SSOT (Brookfield-contaminated).

Full read log in `_aux/Reads_s2.md`.

## Eval spec sub-dims (`Evals_starpm/2_OE_Eval.md`) verified

- **OE Completeness** :: **PASS (5)**. Full critical path over 38 steps: 27 discovery steps covering every load-bearing fact, both hard dependency chains present (`list_teams` -> `list_issue_statuses`; `list_calendars` -> `list_events` -> `create_event`), and twelve write calls covering all six write classes. Council B's independent 20-ask forward sweep found no gap.
- **OE Accuracy** :: **PASS (5)**. All 25 tool references, services and parameters match the catalog; every expected value re-derived from source matches exactly.
- Phase 1.2 (no pure-reasoning steps) :: PASS, 38/38 steps name a tool.
- Phase 2.4 T9 act-vs-defer hard gate :: PASS. Swept all 580 Slack messages and all 484 Gmail messages; **no documented decision to defer, accept-timing or not-act** on closing out the push exists anywhere in the accessible record set.
- Phase 2.5 date consistency :: PASS. All relative phrases resolve against 2026-07-01; "end of June came and went yesterday" resolves to 2026-06-30.
- Phase 4.0 pre-verdict sweep :: PASS on all four items after round 2 (no wrong count, no wrong tool, no missing write-action OE, no act-vs-defer conflict).

## QC spec sub-dims (`Docs_starpm/7_QC_Spec_Doc1.json` — Oracle Event dimension) verified

- **OE Completeness :: PASS (5/5)** — round 1 scored 4 and the gap (no tracking item for the East cluster, against the prompt's unconditional "anything still open gets its own tracking item raised") was closed by new OE 33.
- **OE Accuracy :: PASS (5/5)** — round 1 scored 4 on six hard errors, all six now corrected with replacement figures re-derived from source.

## Verification statements

- [x] `validate.py --phase oe` exit 0 — **PASS, 0 fails, 0 warns, 3 notes**.
- [x] Every OE tool name exists in `StarPM_Base_Universe/7_Server_Tools_Details.json`. Phantom-tool check clean: no `linear_create_issue`, no `slack_conversations_add_message`, no `gmail_send_email`, no `airtable_list_records`, no `*_by_id` variant appears.
- [x] Every OE parameter binding is on the EXACT named tool. All four StarPM traps cleared: `slack_send_message` uses `message` (never `payload`/`text`); `create_draft` uses `body` (never `content`) and no send tool exists; `save_issue` uses `team` (never `teamId`); `save_comment` uses `issueId` + `body`. Airtable camelCase `baseId`/`tableId` correct, including the subtle split that `search_records` takes `table` while `list_records_for_table` takes `tableId`.
- [x] Closed-period / lifecycle precondition check :: N/A for StarPM (no fiscal periods; validator NOTE confirms the skip).
- [x] `verify_universe_atoms.py` exit 0 — 33 atoms, 0 FAIL, 1 WARN.
- [x] `test_regression_anchors.py` — **62/62 PASS**.
- [x] Council A (grounding + convention) — **GO**, 0 BLOCKER, 0 MAJOR, 0 MODERATE. Full 38-row per-OE sign-off table with a retrieved value in every cell.
- [x] Council B (adversarial QC) — **GO**, both sub-dims 5/5, zero NON-FAIL bands invoked.
- [x] Council B-B3 density (StarPM V4 per-model band, NOT the V3-family 50/40) — final round-3 figures under the governing minimising reading: Opus **50** (floor 45), Gemini **42** (floor 38), combined **46**. Band **PASS** on both models.
- [x] Council B-B4 lever preservation — **5/5**, two strengthened. L31 retraction beat survives in OE 38 and now carries the AUDIT A-3 two-criteria split.
- [x] Service breadth — 4 services at >= 5% (threshold 4) under the governing reading, 5 under the OE-faithful reading. **Dominant `linear` at 63.8%, above the 60% disqualifier: `THIN_BREADTH` FIRES.** See the acceptance section below.
- [x] No `PROPAGATE TO S1` finding from either council.
- [x] AUDIT verdict = **PASS (STRICT)** — reached after two REVISE rounds; 4 MAJOR raised and cleared across three passes. Report at `_aux/Council_Reports/AUDIT_oe.md`, companion at `_aux/Verification_audit_oe.md`.

## THIN breadth acceptance (v11 G1, `Reference/Sessions/HARDNESS.md:151`)

**The gate.** ">= 4 distinct services with each >= 5% of total = PASS; 3 distinct services with the dominant one < 60% = ACCEPTABLE; <= 2 distinct services OR dominant > 60% = `THIN_BREADTH`." The two clauses are independent and this task splits them: the >= 4-services clause **passes** under every reading, and the dominance sub-clause **fails**.

**The number, and how it was reached.** Council B's round-2 figure of 53.8% was wrong and it conceded the error in round 3: a minimising profile cannot report fewer Linear calls than the OE's own prescribed Linear floor, and it had. The strict AUDIT caught it independently and put the true band at 61-65%. Three parties then converged: AUDIT 61-65%, my own hand count **66%** on the round-2 text, and Council B's round-3 re-derivation **63.8%** on the current text. The rebalancing edits (OE 21 collapsed from five `get_issue` to two plus one `list_issues`; OE 15 no longer needs two; OE 23, 25, 26 and 7 stated at their true call counts) moved the share 2.2 points and cost about two calls per model. They did not clear the gate.

**Two readings, both recorded so the gap is explicit:**

| Reading | Total | linear | Services >= 5% | Dominance |
|---|---:|---:|---:|---|
| (A) OE-faithful minimising — every step the OE prescribes as expected, at its cheapest satisfying call count | 53 | 56.6% | 5 | passes |
| (B) Maximally-skeptical minimising — (A) minus every non-Linear call a determined minimal agent could skip without failing a required write | 47 | **63.8%** | 4 | **fails** |

Reading (B) governs, because the AUDIT's LENS 4 mandates the reading that minimises inferred exploration and the strictest available reading is the one that must clear the disqualifier. Reading (A) is recorded because it is the design target, not to clear the gate with.

**Why no OE edit fixes this.** It is a prompt-and-universe property.

1. **The load-bearing determination resolves in a single Linear column.** Lever 2 is the symmetric backbone: the whole "is the QC actually closed" question turns on `state_id` across OPS-87 / OPS-96 / OPS-98, decoded via `list_issue_statuses`. No other service mirrors that column, and a leakage sweep found zero prose statement of it anywhere in the universe.
2. **Eight of the twelve required write calls are Linear writes** — five `save_issue` tracking items mandated by "Anything still open gets its own tracking item raised", plus three `save_comment` notes mandated by "a short note left on each one". Both are explicit prompt asks. The other four writes are one each across airtable, gcalendar, slack and gmail, which is already the maximum diversification the prompt supports.
3. **The non-Linear read surface is genuinely shallow.** Airtable is four fields over 50 rows; the calendar holds ten relevant events; contacts is a flat 61-row lookup; Gmail contains zero push content (0 of 156 threads match "Preventive Maintenance Push" or "cluster"). QuickBooks and HubSpot are correctly at zero and were excluded at HARDNESS with three documented reasons.
4. **This is not the false positive the gate was written to catch.** The gate targets density manufactured by stacking one service. Here the chain genuinely forces cross-correlation across Linear structured state, Linear prose, Slack top-level posts, Slack thread replies and Calendar agendas. It fails only the dominance sub-clause, and it fails it because the answer lives in Linear and the user asked for Linear writes.

**Decision: carry `THIN_BREADTH` forward as a documented acceptance. Do not manufacture breadth.** Both the AUDIT and Council B recommended this independently and in the same terms. Clearing 60% at a Linear floor of 30 would need a 50-call total, i.e. three further non-Linear calls a minimal agent would still make, and the only candidates are precisely the five that reading (B) strips as skippable. Adding them back is padding, and padding an OE to move a breadth number is a worse defect than the finding.

**One non-padding lever exists and is deliberately declined.** OE 13, 14, 17, 18 and 19 each pair `get_issue` with `list_comments`, ten calls in total. `get_issue` exposes `includeRelations`; if the server returns comments under that flag the Linear floor drops to 25, total 42, **59.5%**, under the line. This is declined because the catalog does not document that behaviour and it would also remove five calls of real density. It is recorded here so a later phase does not rediscover it and act on it without noticing the dependency on unverified server behaviour.

**What this means downstream.** `THIN_BREADTH` means the task may meet the density floor while being structurally lever-thin. Density is not the issue here: it PASSES on both models with margin on Opus and a 42 midpoint on Gemini. The operator should know the breadth position before upload, and FINAL should re-check it rather than inherit this note.

## AUDIT auto-fire determination (S2 runbook step 8)

Auto-fire is **MANDATORY**. Three of the five trigger conditions hold: (b) the atom verifier emitted an edge-case flag; (d) the OE list was revised in this pass (two council rounds); (e) no rubrics exist yet, so every write action's covering Outcome 1.1 is a forward-map gap by construction. Condition (a) does not hold (zero NON-FAIL bands were invoked) and (c) does not hold (the validator is at 0 warns).

## Downstream-binding constraints from S1, and where each is discharged

| Source | Constraint | Where honoured |
|---|---|---|
| Council A N2 | Pin Slack C001 | OE 1, OE 37 |
| Council A M3 / AUDIT A-6 | Pin `appPropertyOps` / `tblMaintenanceTickets`; write no owner or status field | OE 24, OE 28 |
| Council A M2 / AUDIT A-5 | Scope state correction to Jaime's three; state is already correct, prose is what is wrong; no state flip required or penalised | OE 15 grading note two |
| AUDIT A-1 | Owner accept-sets per item, never a single-name pin | OE 29, 30, 31, 32, 33 |
| AUDIT A-2 | Routing partition: two North units -> Airtable; West coverage gap -> Linear; boundary items either way | OE 28, OE 29 |
| AUDIT A-3 | Retraction split into two atomic criteria graded on substance | OE 38 |
| Council A M1 / AUDIT A-4 | Three atomic per-issue notes; accept-band for extra comments on OPS-99 / OPS-108 / OPS-51 | OE 34, OE 35 |
| AUDIT A-8 | Never require the agent to name OPS-34; grade the disposition | OE 16 grading note |
| Council B (S1) | Owner in `description` text, never `assignee` | OE 29 and every tracking-item step; independently confirmed from the catalog |
| AUDIT A-7 | No Linear-only additions without cross-service compensation; exercise `gcalendar list_events` and an Airtable existing-ticket sweep | OE 22, 23, 25, 27; net addition ratio 1 Linear : 2 non-Linear |
| AUDIT A-11 | Date-anchor to `today_horizon.json`, not Fact_Ledger | Throughout; Fact_Ledger also backfilled |
| Hardness constraint 6 | Do not build on OPS-91 | OE 15 grading note one, OE 20 precision requirement |
| Hardness constraint 7 (L7) | Do not build on an absence | OE 4 and OE 16 reframed so the graded fact is positive and the absence is corroboration |
| Hardness constraint 7a | Never claim nothing on the push is closed | OE 15 bounds the finding with OPS-40 and OPS-91 |
| Hardness constraint 3 (F9) | Do not claim Jaime's QC queue is otherwise clear | OE 23 |

## Discrepancies surfaced

1. **`_aux/Council_Reports/AUDIT_prompt.md` line 486 states OPS-34 carries 18 comments. The true count is 16**, verified in `linear.linear_comments.json`. The figure was inherited into the OE first draft and both councils caught it. The A-8 binding it supports is unaffected (the title is still uninformative and the record must never be a graded identification). **The upstream report is left as written** because a phase does not rewrite a prior phase's audit record, so S3 and FINAL must take 16 from here, not 18 from there.
2. **`_aux/Hardness_Plan.md` overstates the Airtable HVAC decoy count and names the wrong properties.** The literal token HVAC matches 18 of 50 ticket rows, not ~23, and Sunridge appears in zero rows of `tblMaintenanceTickets` (it appears in Slack). Corrected in the OE and in `_aux/Reads_s2.md`; the upstream plan is left as written.
3. **`Validators/validate.py:464` still hardcodes a Brookfield `2026-06-12` fallback** for the date-alignment NOTE. The per-task trigger is now removed because `_aux/Fact_Ledger.json` `lifecycle.today` was backfilled to `2026-07-01` in this phase, but the shared-code defect remains and will re-fire on the next StarPM task whose Fact_Ledger is built by the current builder. Two fixes stay open for the operator: backfill `lifecycle.today` in the Fact_Ledger builder, and change line 464 to read `get_universe_constants(detect_universe(task_dir))["today"]`.
4. **Atom-verifier WARN on 2026-07-15 is expected and adjudicated non-defect.** That date is the real confirmed Make-Ready QC Inspection at Mesa Vista 4C, correctly outside the 2026-05-01 to 2026-07-01 activity window because it is a genuine future event. It is cited in OE 23 precisely so no deliverable claims Jaime's QC queue is otherwise clear.
5. **Council A round 1 overclaimed on the push-keyword vector**, asserting it was "unreachable under every set tested" when the correct claim was "not reproduced by the sets I tested". The vector is reproducible: `preventive|cluster|HVAC|filter|coil|condensate|water heater|hose bib|panel inspection|spot-check|QC` over all 580 messages yields exactly C001 20 / C004 7 / C002 4 / C003 4 / C008 3 / C007 3 / C006 1. The council conceded this in round 2. Its downstream consequence was nevertheless correct and was applied: a count whose value depends on an unstated keyword set is not a legitimate expected value, so OE 1 and OE 7 now carry the qualitative claim plus only the counts that are stable under any reading.
6. **OE 27's Gmail sweep carries no prompt cue**, so a meaningful share of real runs will skip it. Recorded so S4 does not treat a missing Gmail read as a trajectory defect. Density survives its removal: stripping it gives Opus 51 with `linear` at 54.9%, still 5 services at >= 5% and still under the ceiling.
7. **Eleven OE steps embed S3 grading directives, against `Reference/OE_Format.md:77` ("Not a place to add rubric reasoning").** This is a genuine convention conflict and it is resolved deliberately in favour of keeping them in the OE. The directives were not authored freely: every one was mandated by an upstream binding that specified the OE as the location. `AUDIT_prompt.md` A-1 says "the OE must record the accept-set per item **so the judge sees it**"; S1 Council B says "**Encode the accept-band in the OE** so the judge sees it"; A-2, A-4, A-5, A-6 and A-8 are the same shape. `Evals_starpm/2_OE_Eval.md:18` further designates OEs as CB internal planning documents rather than graded artifacts, and no QC-spec band penalises the practice, which is why both the AUDIT and Council B scored it MINOR with no score impact. Relocating them to a separate file was considered and rejected: it would create a drift surface between two documents S3 must reconcile, and the upstream instruction was explicit that the judge should see them in place. **Recorded as a documented deviation** so FINAL does not re-litigate it. Note it has no precedent in StarPM siblings 40-43 or the QC-passed corpus, so if the platform reviewer objects, the remedy is to lift all eleven into `_aux/S3_Grading_Notes.md` keyed by OE number rather than to delete them, because the content is load-bearing.
8. **Three figures in `_aux/Hardness_Plan.md` were falsified during S2 grounding** — 15 thread parents (actual 37), "20+" Airtable HVAC rows with a property "Oakdale" that exists nowhere in `tblMaintenanceTickets` (actual 18 rows, no Oakdale), and a five-day gap that is actually seven. None changes the lever selection, the density band or the hardness score, and two of the three err in the favourable direction. The plan body is left as authored and a clearly marked correction block is appended to its end, so S3 and FINAL do not re-propagate the figures.
9. **OE 33 carries a deliberate either-location accept-band** (a new East tracking item, or the East position folded into the OPS-98 note). This is a grading accommodation permitted by the OE Authority Rule, not evidence of prompt ambiguity. **Binding on S3:** the East criterion must accept both locations or a correct agent false-fails.

## Verdict

**PASS.** `6_Oracle_Events.txt` clears every S2 exit criterion: validator PASS with zero warns, atom verifier clean apart from one adjudicated expected flag, regression anchors 62/62, Council A GO with a complete per-OE sign-off table and zero MAJOR or MODERATE remaining, Council B GO with both QC sub-dims at 5/5 and zero NON-FAIL bands invoked, density in the StarPM V4 PASS band on both models with breadth improved, and all 5 hardness levers preserved with two strengthened. Two council rounds were required; the round-1 defect set was real and substantial (2 BLOCKER, 9 MAJOR across the two councils), which is the auto-AUDIT policy working as designed at the producing phase.
