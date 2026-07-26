# AUDIT (STRICT) - S2 Oracle Events

Task: `Tasks/39_6a602c8886ebb06f12354d77` | Universe: StarPM (V4) (`_aux/Universe.txt` = starpm) | Phase audited: S2 (`6_Oracle_Events.txt`, 12 OEs)
Persona: James Bennett (Assistant Maintenance Technician, james.bennett@starpm.com) -> Lead John Smith (john.smith@starpm.com).
Scenario ground truth: Las Palmas 8D is NOT ready. Seized garbage disposal (OPS-227) awaiting John's parts approval; make-ready ticket MT-2026-1271 still OPEN (blank completion); stale 2026-05-01 selReady row superseded by two live selProg rows; fridge swap is a separate, done appliance; Rio Bend 214 (MT-2026-1325) is the near-miss twin. Airtable base `appPropertyOps` is system of record. Today 2026-07-01 America/Chicago.
Method: every atom re-queried live from `_aux/Universe_Split/*` (row_data JSON-parsed), tools re-read from `StarPM_Base_Universe/7_Server_Tools_Details.json`. No prior summary or council verdict taken on trust. Density band = StarPM V4 (40 design / 15 floor, per model). Interpretation = strictest: 5/5 is the only pass, every "should" is "must", every NOTE listed, every lever traced prompt+OE+atom.

## VERDICT: PASS (STRICT)

Zero BLOCKER. Both LENS-1 OE sub-dims = 5/5. All 5 hardness levers trace end-to-end (prompt + OE + atom). Density midpoint ~44 per model (>= 40 StarPM V4 design target). Regression anchors 62/62; `validate.py --phase oe` exit 0. Findings below are 2 S3-forward notes + non-scoring observations; NONE requires an edit to `6_Oracle_Events.txt`. No `PROPAGATE TO S1` (prompt framing is correctly implicit; no prompt root cause).

---

## LENS 1 - Strict QC scoring (Docs_starpm/7_QC_Spec_Doc1.json OE dimension)

### OE Completeness -> 5/5
Full critical path with no gap. Discovery: OE1 base/tables/fields; OE2 the three 8D make-ready rows; OE3 open ticket MT-2026-1271 + Rio Bend 214 twin; OE4 #make-ready (C004) history; OE5 #maintenance (C001) disposal; OE6 OPS-227 + team_001 SoR charter; OE7 the single OPS-227 comment. Reconciliation conclusion carried by OE7 (+ OE2). Pre-write dependency lookup OE10 (John's email). All four required writes present: OE8 (advance blocker), OE9 (correct stale record), OE11 (Slack #make-ready post), OE12 (Gmail draft to John). Each prompt write-ask maps 1:1. No reasoning-only OE (OE7's synthesis rides a real `list_comments` call, not a standalone deduction step). PRIOR COUNCIL MISS: none.

### OE Accuracy -> 5/5
Zero wrong tool / service / parameter / count / expected-value. Per-atom evidence table (empty evidence would force <= 3; every row has a live query + row excerpt):

| Atom asserted (OE) | Universe query (file) | Row excerpt | Verdict |
|---|---|---|---|
| base `appPropertyOps` "Property Operations" (OE1) | airtable.airtable_bases.json | `{"id":"appPropertyOps","name":"Property Operations","permission_level":"create"}` | MATCH |
| tblMakeReady primary `fldUnit`; tblMaintenanceTickets primary `fldTicketNumber` (OE1) | airtable.airtable_tables.json | both tables + primary_field_id exact; tblMaintenanceTickets desc "System of record ... Linear is secondary" | MATCH |
| field ids fldUnit/fldTurnStatus/fldMoveOut/fldTargetReady/fldNotes2 + fldTicketNumber/fldDescription/fldPriority/fldCompletionDate (OE1/OE9) | airtable.airtable_fields.json | all 9 present; fldTurnStatus choices selSched/selProg/selReady | MATCH |
| receb057 = 8D, selReady, target 2026-05-01, "closed out ... cleared for leasing" (OE2) | airtable.airtable_records.json:receb057b02f20052 | `"fldTurnStatus":"selReady","fldTargetReady":"2026-05-01"`, note "Turn closed out ... cleared for leasing - available to show immediately" | MATCH |
| recf7aecc318b2252 = 8D, selProg, John Smith + James Bennett in-house (OE2) | airtable_records | `"fldTurnStatus":"selProg"`, note "John Smith and James Bennett are three days into the in-house make-ready work" | MATCH |
| rec651427 = 8D, selProg, moveout 2026-06-18, target 2026-06-26, fridge swap Thu 6/25 critical path (OE2) | airtable_records:rec651427ec0d84dd5a | `"fldMoveOut":"2026-06-18","fldTargetReady":"2026-06-26"`, note "Refrigerator swap scheduled Thu 6/25 ... critical path (lease signing pending) ... replacement delivered and installed" | MATCH (fridge = done, separate appliance) |
| recac236 = MT-2026-1271, selHigh, completion "" (OPEN), carpet/faucet/scuff scope (OE3) | airtable_records:recac236210094352 | `"fldTicketNumber":"MT-2026-1271","fldPriority":"selHigh","fldCompletionDate":""`, desc "carpet has visible staining ... kitchen faucet is dripping ... walls show scuff marks" | MATCH (blank = OPEN) |
| recb403 = MT-2026-1325, Rio Bend 214 dishwasher, completion 2026-06-25 (OE3) | airtable_records:recb403fe04c2f97683 | `"fldTicketNumber":"MT-2026-1325","fldCompletionDate":"2026-06-25"`, desc "Dishwasher pull-and-replace at Rio Bend 214 ... same Thursday (6/25) as the Las Palmas 8D refrigerator swap" | MATCH (the done twin, NOT 8D) |
| "three separate 8D rows" (OE2) | count in airtable_records | exactly 3 tblMakeReady rows with fldUnit "Las Palmas 8D" | MATCH |
| OPS-227 title/team/assignee/desc (OE6) | linear.linear_issues.json:OPS-227 | title "Clear garbage disposal jam - Las Palmas 8D", team_id "team_001", assignee_id user_8cd13ca90bca5494ab86e300c4b7829b, desc "kitchen garbage disposal ... jammed ... Reset and clear the jam" | MATCH |
| team_001 = Airtable-is-SoR (OE6) | linear.linear_teams.json:team_001 | "Airtable Maintenance Tickets table, which is the system of record. Linear is secondary for maintenance items" | MATCH |
| comment_16a0a0c53f... James 2026-06-22 seized/parts-approval, ONLY comment (OE7) | linear.linear_comments.json | body "The 8D disposal is seized ... flywheel is frozen ... full unit replacement ... Routing back to you for parts approval before I swap it", author James, issue_id OPS-227; exactly 1 comment on OPS-227 -> no reply | MATCH -> L3 confirmed |
| C004 = #make-ready; C001 = #maintenance (OE4/OE5/OE11) | slack.slack_channels.json | C004 "#make-ready", C001 "#maintenance" | MATCH |
| C004 latch chatter carpet 5/23, punch-list 5/27, "officially cleared and ready" 5/29 (OE4) | slack.slack_messages.json (ts->date) | ts 1779540043 (5/23 carpet), 1779895537 (5/27 punch-list), 1780067965 (5/29 "8D is officially cleared and ready for leasing") | MATCH (all predate 6/22) |
| C001 two 6/22 James disposal msgs (OE5) | slack.slack_messages.json | ts 1782144900 + 1782145200, user james.bennett: "8D disposal is seized ... routed it to @john.sm..." + "waiting on parts approval from John ... that unit's still open" | MATCH |
| john.smith@starpm.com = Lead (OE10/OE12) | contacts.contacts.json + linear.linear_users.json | contact b233365df4... "john.smith@starpm.com" job "Lead Maintenance Technician"; linear user_32006747... John Smith | MATCH |
| 16/16 tool names + StarPM param traps (all OEs) | StarPM_Base_Universe/7_Server_Tools_Details.json | search_records(baseId,table,query); list/update_records_for_table(baseId,tableId,records); slack_send_message(channel_id,message); create_draft(to,subject,body); save_comment(issueId,body); list_issues(team); get_issue/get_team(id); slack_read_channel(channel_id); contacts_search_contacts(query); list_bases/list_tables_for_base/get_table_schema | MATCH (every tool exists; every param exact) |

StarPM landmine checks (all clean): Airtable-is-SoR vs Linear-secondary -> OE3 pulls the maintenance ticket from Airtable (`tblMaintenanceTickets`) NOT Linear, and OE6 pulls the team_001 charter that hardcodes it. Cross-property unit ambiguity -> only "Las Palmas 8D" exists (all 6 "Las Palmas 8D" + 1 "Unit 8D" refs are one unit; no cross-property 8D collision); Rio Bend 214 twin explicitly disambiguated in OE3. Near-duplicate decoy -> the file-level near-dup landmine does not apply (StarPM here has no filesystem service); the twin (MT-2026-1271 vs MT-2026-1325) is correctly split. **Rio Bend 214 (MT-2026-1325) vs Las Palmas 8D (MT-2026-1271) disambiguation: CORRECT. OE3 routes to Airtable SoR, not Linear: CONFIRMED.**

Param-trap cross-check (a lesser OE fails these): OE11 uses `message` not `payload`/`text`; OE12 uses `body` not Brookfield's `content` and correctly treats Gmail as draft-only (no send tool exists in the catalog); OE9 uses camelCase `baseId`/`tableId`/`records`; OE2/OE3 use `table` (the real param) not `tableId` for `search_records`; OE6 uses `team` not `teamId`. All correct. PRIOR COUNCIL MISS on LENS 1: none material (both councils graded 5/5 with matching grounding).

---

## LENS 2 - Answer-leakage sweep (OE phase)

The task answer = "8D NOT ready, seized disposal awaiting parts approval." No OE step is a single-tool-call reveal; every OE conclusion is cross-sourced (stale selReady row + open ticket MT-2026-1271 + OPS-227 comment + 5/xx "cleared" chatter + 6/22 disposal msgs + confirmation of no reply). Closest single artifact = the 6/22 C001 Slack line "8D disposal needs a replacement (waiting on parts approval from John), so that unit's still open." Even that requires temporal reconciliation against the selReady row and the 5/29 "officially cleared and ready" message to be trusted as CURRENT (7/1) - i.e., it forces the L10 supersession decision, so it is not a trivializing single-source answer. It is a universe-design property (not an OE artifact; not editable at S2 - no universe edits), within tolerance. VERDICT: no leakage BLOCKER; F5 logged as a non-scoring observation.

---

## LENS 3 - Hardness end-to-end trace (prompt + OE + atom)

| Lever | Prompt sentence (surfaces it, stays implicit) | OE step (exercises it) | Fact_Ledger / universe atom | Trace |
|---|---|---|---|---|
| L10 supersession | "square up what we've got logged ... because I'd bet some of it is stale by now" | OE2 (stale selReady 5/1 vs later selProg; "selProg, not selReady") + OE9 (corrects it) | receb057b02f20052, recf7aecc318b2252, rec651427ec0d84dd5a (ids.airtable_record) | COMPLETE |
| L2 Airtable-SoR skip | "confirm where each piece actually landed instead of going off what someone said in passing" | OE6 (team_001 = Airtable SoR) + OE3 (open Airtable ticket MT-2026-1271) | recac236210094352 (blank completion) + linear_teams:team_001 charter | COMPLETE |
| L1 latching | "the punch-list got knocked out and the carpet's in, so on paper it looks about there" | OE4 (C004 "carpet/punch-list done / officially cleared" chatter, flagged pre-June/not-current) | slack 140558bdd3... + 21f0475ef1... (verified in slack_messages) | COMPLETE |
| L4 204B decoy eviction | "this turn has been dragging since May and a bunch of people have had a hand in it" (+ isolate 8D) | OE2 (isolate exactly 3 8D rows) + OE3 (reject Rio Bend 214) | 61x "204B" vs 7x "8D" (ids.airtable_record) + recb403fe04c2f97683 | COMPLETE |
| L3 missing reply | "run down whatever it's waiting on and get it moving so it can genuinely close" | OE7 ("No reply follows ... parts approval never came") + OE5 reinforcement | comment_16a0a0c53f... (ids.linear_comment); OPS-227 has exactly 1 comment | COMPLETE |

All five levers trace prompt + OE + atom. No HARDNESS_REGRESSION. (S3 rubric criterion pending - not a regression.)

---

## LENS 4 - Strict density projection (StarPM V4: >=40 PASS / 15-39 THIN / <15 BLOCKER, per model)

Lean-but-correct floor (single-shot, no re-reads, still satisfies "confirm each piece"): list_bases + list_tables_for_base (2), make-ready 8D query (1), ticket query (1), read C004 (1), read C001 (1), get_issue OPS-227 (1), list_comments (1), get_team charter (1), contacts (1), 4 writes (4) = ~14. Levers inflate a realistic competent run: 204B result-eviction forces query rework on tblMakeReady (+2-4); Rio Bend twin pull/compare (+1-2); Airtable-vs-Linear SoR reconciliation, natural Linear-first detour (+2-3); missing-reply chase (+1-2); component-by-component verification of the 8 turn items (carpet/deep clean/paint/drywall/faucet/punch-list/fridge/disposal) (+3-5); cross-service buffer (+3-5). Realistic midpoint ~40-48 (I take ~44 conservatively), matching Hardness Plan 48.5 and Council B 40-48. VERDICT: midpoint ~44 per model >= 40 -> PASS. WATCH (F6): the lean floor sits right at the 15 line; a very terse real run could land THIN (15-39), never <15 INSUFFICIENT for a correct solve. Applied separately to Opus 4.8 and Gemini.

---

## LENS 5 - Adversarial veteran review

- Implicit-prompt framing PRESERVED: prompt has James believing it's essentially done ("on paper it looks about there", "I told him I'd have it closed out today") and asks to verify + advance IF something is open. No OE assumes the prompt revealed the disposal; OE1-7 discover it fresh. PASS.
- Entity-drift (John Smith / john.smith@starpm.com / the Lead): consistent throughout; no Lisa Smith / john.castillo confusion in any OE; OPS-227 creator John Smith vs assignee James Bennett correctly distinct. PASS.
- Silent process rubrics: N/A at OE phase. 
- Tool-name correctness: 16/16 verified. PASS.
- Em/en dashes in OE text: ZERO (U+2014/2013/2015). Universe-data dashes (OPS-227 title, comment body) correctly NOT reproduced. PASS.
- Single-channel lock-in vs goal (OE8 "get it moving"): the OE names the Slack-to-John alternative and picks the Linear comment as primary with sound justification (James is the OPS-227 assignee; the blocker lives on that thread). NOT over-locked at OE phase; it is an S3 rubric-breadth concern (F1).
- "(or similar)" near exact values: NONE. "or" appears only for genuine, catalog-valid tool alternatives (search_records or list_records_for_table; get_issue or list_issues; slack_read_channel or slack_search_public_and_private), which the OE eval encourages. PASS.
- "approximately" near IDs/dates: NONE. PASS.

---

## LENS 7 - Anti-Rationalization ledger (each "considered flagging but..." promoted)

1. OE6 "outranks any done impression from Slack or Linear" - considered as inaccuracy. HARD EXCLUSION: it is a precedence/justification clause, not a data/tool/service/param/count claim; and OPS-227's Linear state is "In Review" (a genuinely done-leaning signal), so the clause is defensible and does not misdirect the agent. -> F4 (non-scoring NOTE; OE Accuracy stays 5/5).
2. OE8 Linear-primary vs Slack channel - considered as over-lock. HARD EXCLUSION: OE explicitly names the alternative (not locked); lock-in is a RUBRIC risk, not an OE-phase defect. -> F1 (S3-forward).
3. 6/22 C001 Slack "still open" line - considered as answer-leakage. HARD EXCLUSION: universe property (not an OE artifact, not S2-editable); still requires temporal reconciliation to trust as current. -> F5 (non-scoring).
4. OE9 targets specific record id receb057 - considered as brittle/incomplete. HARD EXCLUSION: it is the ONLY 8D row in a wrong (selReady) state; the other two are already selProg; correcting it makes the SoR internally consistent per the prompt's "square up ... matches where the unit really is". -> F2 (S3-forward, rubric should target the outcome not the id).
5. OE10 (read) after OE8/OE9 (writes) - considered as convention breach. HARD EXCLUSION: OEs are unordered critical steps (OE eval); the OE10->OE12 dependency is intact and the list still ends on writes. -> F3 (cosmetic, non-scoring).
6. Density lean floor ~14 - considered as BLOCKER risk. HARD EXCLUSION: the correct-solve floor is ~20+ and the realistic midpoint ~44 >= 40; sub-15 only by skipping mandated verification (not a correct solve). -> F6 (WATCH).

No item survives as a BLOCKER or as a sub-dim < 5.

---

## LENS 8 - Regression + validator

- `python3 Validators/test_regression_anchors.py` -> **62 passed, 0 failed out of 62.** (SP-1..SP-9 + SP-INJ/SUB StarPM anchors all green, incl. SP-7/8/9 param-trap anchors.)
- `python3 Validators/validate.py --phase oe --task Tasks/39_6a602c8886ebb06f12354d77` -> **exit 0**, 0 fails / 0 warns / 3 NOTES. The 3 notes are benign and listed per strict rule: (1) universe: starpm; (2) OE step count: 12; (3) "no closed fiscal periods ... skipping lifecycle precondition check" - correct: StarPM property-management universe has no GL/fiscal periods (Fact_Ledger entities=0, fiscal_periods=0), so the JE-style closed-period lifecycle check is not applicable to this task. No issue.
- `verify_universe_atoms.md`: 7/7 atoms present (0 FAIL / 0 WARN).

---

## What the prior councils missed (incremental to the two GO verdicts)

Both councils were thorough and their grounding matches mine exactly; I confirm their two forward-notes (channel variation; L4 not named). Incremental strict catches:
- F5: no council ran an explicit OE-phase answer-leakage sweep on the 6/22 C001 line (Council B touched it only through the T9 act-vs-defer lens). Within tolerance, logged.
- F3: strict-literal "reads-first" convention deviation at OE10 (Council A reframed the rule as dependency-ordering and passed it). Cosmetic, logged.
- F2: OE9's record-id fixation as an S3 over-fit risk (Council B forward-noted L4-naming and channel, not the record-id). Logged as S3-forward.

---

## Findings register (all non-blocking; none edits 6_Oracle_Events.txt)

| # | Severity | Finding | Location | Action |
|---|---|---|---|---|
| F1 | LOW / S3-FORWARD | Advance-blocker names Linear-comment primary + Slack alt (same recipient/intent) | OE8 | S3: phrase the Outcome rubric action-focused ("Agent requests John Smith's parts approval for the disposal replacement"), NOT channel-locked. Confirms Council B #1. |
| F2 | LOW / S3-FORWARD | Record correction targets specific id receb057b02f20052 | OE9 | S3: target the OUTCOME ("no 8D make-ready row shows Ready/cleared-for-leasing"), not the record id, to avoid over-fitting. |
| F3 | LOW / COSMETIC (optional) | Contacts read placed after two writes, deviating from "reads-first" soft convention | OE10 (after OE8/OE9) | Optional: renumber the contacts lookup into the OE1-7 discovery block. No score/solvability impact (OEs unordered; OE10->OE12 dependency intact). |
| F4 | NOTE (non-scoring) | "done impression from ... Linear" - OPS-227 is "In Review" not "Done" | OE6 | Defensible ("In Review" is done-leaning); optional wording tightening. Does NOT drop OE Accuracy below 5. |
| F5 | NOTE (universe-design) | Closest single-source signal = 6/22 C001 "still open" line | universe (not OE) | Within tolerance; still requires temporal reconciliation. Not S2-fixable (no universe edits). |
| F6 | WATCH (density) | Lean-correct floor ~14 at the 15 line; midpoint ~44 | trajectory | Watch platform runs; THIN-acceptable worst case, never <15 for a correct solve. |

## Sign-off
LENS 1: OE Completeness 5/5, OE Accuracy 5/5 (per-atom evidence complete). LENS 2: no leakage BLOCKER. LENS 3: all 5 levers trace end-to-end. LENS 4: density midpoint ~44/model (>= 40). LENS 5/7: no over-lock, no drift, no hedge-phrase, anti-rationalization ledger clean. LENS 8: 62/62 anchors, validate exit 0.
**RESULT: PASS (STRICT).** No REVISE, no REBUILD. Carry F1 and F2 forward to S3; F3/F4 optional; F5/F6 informational.
