# Council B - Adversarial QC + Density + Hardness Preservation - S2 Oracle Events

Task: `Tasks/39_6a602c8886ebb06f12354d77` | Universe: StarPM (V4) | Phase: S2 (Oracle Events)
Persona: James Bennett (Assistant Maintenance Technician, james.bennett@starpm.com) -> Lead John Smith
Scenario: reconcile the Las Palmas 8D make-ready turn and report its true state. Ground truth: 8D is NOT ready (seized garbage disposal, OPS-227, awaiting John's parts approval; make-ready ticket MT-2026-1271 still OPEN).
Today: 2026-07-01 America/Chicago. Reviewed against 5_Prompt.txt, _aux/Hardness_Plan.md, Docs_starpm/7_QC_Spec_Doc1.json + 8_QC_Spec_Doc2.md (OE dimension), Evals_starpm/2_OE_Eval.md, per-task Universe_Split.

Five role lenses applied (Architect / Implementer / Red-team / Ground-truth / Integration); verdict is the union of all five.

---

## B1 - OE Sub-Dimension Scoring (bar = 5 on both)

`SUB-DIM OE Completeness -> SCORE 5/5 -> REASON`
The 12-OE chain covers the full critical path with no gap: discovery (OE1 base/tables; OE2 the three 8D make-ready rows; OE3 open ticket MT-2026-1271 + Rio Bend 214 twin; OE4 #make-ready C004 history; OE5 #maintenance C001 disposal; OE6 OPS-227 issue + team_001 SoR charter; OE7 OPS-227 single comment), an explicit reconciliation conclusion (OE7: "8D cannot genuinely close until the disposal replacement is approved and installed; everything else in the turn is done"; reinforced by OE2's "current status is selProg, not selReady"), a pre-write contact lookup (OE10), and all four required writes (OE8 Linear save_comment advance; OE9 Airtable update_records_for_table correct stale row; OE11 Slack slack_send_message C004; OE12 Gmail create_draft to John). Dependency ordering is sound (discovery precedes writes; contact lookup precedes draft). No missing critical step.

`SUB-DIM OE Accuracy -> SCORE 5/5 -> REASON`
Every sampled tool, service, parameter, and expected value was verified against the per-task Universe_Split and the StarPM tool catalog. 16/16 tool names FOUND in `StarPM_Base_Universe/7_Server_Tools_Details.json`. All 5 cited Airtable records exact (statuses, dates, notes, ticket numbers, blank completion). Linear OPS-227 title/team_001/assignee(James Bennett)/comment body exact. team_001 charter ("Airtable Maintenance Tickets table ... is the system of record. Linear is secondary") exact. Slack timestamps resolve exactly to the OE-claimed dates (C004 carpet 5/23, punch-list 5/27, cleared 5/29; C001 disposal x2 on 6/22, both authored by James Bennett UD92EEA47D7). Contacts John Smith -> john.smith@starpm.com present. Bases/tables/primary-fields exact (appPropertyOps; tblMakeReady primary fldUnit; tblMaintenanceTickets primary fldTicketNumber). Following the OEs literally produces a correct trajectory.

Both OE sub-dims meet the 5/5 bar.

---

## B2 - Adversarial Alt-Path / Second Reading

Trap-path integrity is strong; the OE chain names and neutralizes every decoy (stale selReady row, ready-chatter, Rio Bend 214 twin, done-fridge-vs-open-disposal, MT-2026-1271 "leave open"). One genuine second-reading exists, and it stays inside the NON-FAIL band:

- **"Get the blocker moving" channel variation (OE8).** The prompt asks James to "run down whatever it's waiting on and get it moving." The direct action is a follow-up requesting John's parts approval on the seized-disposal blocker. The OE itself flags Slack-to-John as an alternative to the Linear comment on OPS-227. Both readings target the SAME recipient (John) with the SAME intent (approve parts for the disposal replacement); only the channel differs. Per QC Spec Prompt-Clarity Non-Fail band, "channel-of-delivery to the same recipient" is NON-FAIL, not an action-decision ambiguity. No divergence in final universe state -> not a UGT/clarity fail. **Forward note to S3 (non-blocking):** phrase the advance-blocker Outcome rubric broadly ("Agent follows up with John Smith requesting parts approval for the disposal replacement"), NOT locked to a Linear comment, so a valid Slack-to-John path also passes.

No other divergence: the record-correction resolves uniquely to the stale selReady row `receb057b02f20052` (the only 8D row in a wrong state; the other two are already selProg); the Slack post is uniquely #make-ready (C004); the email recipient is uniquely John. Closing MT-2026-1271 is a trap, not a valid alt-path (disposal unresolved) and OE9 correctly forbids it.

**T9 act-vs-defer gate (HARD GATE): PASS.** Scanned accessible C004 + C001 + James's Gmail. Every "ready/complete" signal is either stale (Slack C004 5/23-5/29; Gmail "Las Palmas 8D. Ready to Show" 5/26 to Carlos) - all pre-dating the 6/22 disposal seizure - or finish-pressure (C004 6/25 "critical path ... marketing-ready by end of week; take the fridge swap first"). NONE is a documented decision to DEFER the disposal or to NOT correct the record. The disposal advance and record squaring are EXPLICIT prompt asks; absent any defer decision, the writes are the only valid path. No accuracy divergence.

---

## B3 - Tool-Call Density Projection (StarPM V4 band: 40+ design / 15 floor, PER MODEL)

Competent Opus 4.8 trajectory sketch:
- Discovery: list_bases + list_tables_for_base + get_table_schema (~3); make-ready query for 8D amid the 120-row / 61x "204B" swarm, with refinement/pagination (~3-5); maintenance-ticket query + Rio Bend twin pull/compare (~2-3); read C004 + search (~2); read C001 + search "8D disposal" (~2); get_issue OPS-227 / list_issues (~2); get_team team_001 (~1); list_comments OPS-227 (~1); contacts_search_contacts John Smith (~1); component-by-component verification that each turn item (carpet, deep clean, paint, punch-list, fridge, disposal) actually landed (~3-5).
- Writes: save_comment + update_records_for_table + slack_send_message + create_draft (4).

Clean-minimal floor is ~20; the levers (204B result-eviction forcing query rework, twin disambiguation, Airtable-vs-Linear SoR reconciliation, missing-reply chase, fridge-vs-disposal appliance split) inflate a realistic run to a **midpoint ~40-48 per model** (range ~28-55), consistent with the Hardness Plan's ~48.5. This is genuine cross-service breadth (airtable + linear + slack + gmail + contacts), not a single-service deep trap, which sustains the count.

`DENSITY -> midpoint ~40-48 per model -> >= 40 design target -> PASS.` Never at risk of the 15 INSUFFICIENT floor even on a lean run (~25-30 = THIN-acceptable at worst). Applied separately to Opus and Gemini. No BLOCK.

---

## B4 - Hardness Preservation (5 selected levers)

| Lever | Exercised by | Status |
|---|---|---|
| **L10 supersession** | OE2 surfaces stale selReady 2026-05-01 row vs later selProg rows and concludes "selProg, not selReady"; OE9 corrects the stale row | PRESERVED |
| **L2 Airtable-SoR skip** | OE6 pulls team_001 charter (Airtable = SoR, Linear secondary); OE3 pulls the OPEN Airtable ticket MT-2026-1271 (blank completion) | PRESERVED |
| **L1 latching** | OE4 surfaces the C004 "carpet done / punch-list done / officially cleared and ready" chatter and explicitly flags it as pre-June-disposal and not current state | PRESERVED |
| **L4 204B decoy eviction** | OE2 requires isolating exactly three 8D rows out of a 120-row tblMakeReady dominated by 61x "Las Palmas 204B"; OE3 rejects the Rio Bend 214 near-miss twin | PRESERVED |
| **L3 missing reply** | OE7 reads the OPS-227 thread and concludes "No reply follows, so the parts approval never came"; OE5 reinforces "waiting on parts approval from John ... unit is still open" | PRESERVED |

No HARDNESS_REGRESSION. All five independent-mechanism levers are exercised by at least one OE step. Minor forward note (non-blocking): OE2/OE3 preserve L4 via the discrimination requirement but do not name the "204B volume" explicitly; S3 could add a correct-unit-isolation rubric to reward it.

---

## B6 - Upstream Propagation

No issue whose root cause is in the prompt (S1). The one second-reading (B2, advance-blocker channel) is same-recipient channel variation = NON-FAIL under the QC spec; the record-correction and all other writes converge on a single end-state. **No `PROPAGATE TO S1`.** (Informational only, not OE-phase and not a prompt root cause: HARDNESS already flagged that S0_Setup_Report.md overclaims a passing injection while `9_Universe_inject.sql` is a comment-only stub; the scenario is nonetheless fully baked into the per-task export - every load-bearing row verified present - so OE solvability is unaffected.)

---

## B8 - OE Completeness Semantic Walk (must-take steps)

| Must-take step | OE | Present |
|---|---|---|
| Discovery: 3 make-ready 8D rows | OE2 | Yes |
| Discovery: open ticket MT-2026-1271 | OE3 | Yes |
| Discovery: Rio Bend 214 twin disambiguation | OE3 | Yes |
| Discovery: #make-ready (C004) + #maintenance (C001) history | OE4 + OE5 | Yes |
| Discovery: OPS-227 issue + its single comment | OE6 + OE7 | Yes |
| Discovery: team_001 SoR charter | OE6 | Yes |
| Reconciliation conclusion (8D not ready; disposal outstanding) | OE7 (+ OE2) | Yes |
| Write 1: advance OPS-227 blocker | OE8 | Yes |
| Write 2: correct the stale make-ready row | OE9 | Yes |
| Write 3: post true status to #make-ready | OE11 | Yes |
| Write 4: draft John's status email | OE12 | Yes |
| Contact lookup before draft | OE10 -> OE12 | Yes |

No `OE_INCOMPLETE` flags.

---

## B9 - OE Service Mapping (StarPM map)

| OE | Data type | Service used | Correct? |
|---|---|---|---|
| OE1 bases/tables | make-ready/units/property records | airtable | Yes |
| OE2 make-ready rows | make-ready records | airtable (tblMakeReady) | Yes |
| OE3 maintenance ticket | maintenance ticket (StarPM SoR = Airtable per team_001) | airtable (tblMaintenanceTickets) | Yes* |
| OE4 #make-ready history | chat | slack (C004) | Yes |
| OE5 #maintenance disposal | chat | slack (C001) | Yes |
| OE6 OPS-227 issue + team | Linear issue (secondary mirror) | linear (get_issue/get_team) | Yes |
| OE7 OPS-227 comment | Linear comment | linear (list_comments) | Yes |
| OE8 advance blocker | Linear issue write | linear (save_comment) | Yes |
| OE9 correct record | make-ready record write | airtable (update_records_for_table) | Yes |
| OE10 John's email lookup | contact | contacts (contacts_search_contacts) | Yes |
| OE11 post status | chat write | slack (slack_send_message) | Yes |
| OE12 draft email | email draft (draft-only) | gmail (create_draft) | Yes |

*OE3 correctly targets Airtable (not Linear) for the maintenance ticket - this is exactly the StarPM SoR rule (team_001: Airtable is SoR, Linear secondary) and the core of lever L2. No `OE_SERVICE_MISMATCH`.

---

## Verification Evidence (spot-checks independently run, not taken on trust)

- Airtable `receb057b02f20052` = Las Palmas 8D, selReady, target 2026-05-01, note "Turn closed out ... cleared for leasing". `recf7aecc318b2252` = 8D, selProg, John Smith + James Bennett in-house. `rec651427ec0d84dd5a` = 8D, selProg, moveout 2026-06-18, target 2026-06-26, "Refrigerator swap scheduled Thu 6/25 ... lease signing pending; ... replacement delivered and installed" (fridge DONE, separate appliance). `recac236210094352` = MT-2026-1271, selHigh, fldCompletionDate "" (OPEN). `recb403fe04c2f97683` = MT-2026-1325, Rio Bend 214 dishwasher, completion 2026-06-25 (the done twin).
- Exactly 3 Las Palmas 8D make-ready rows (matches OE2 "three separate 8D rows").
- Linear OPS-227 title "Clear garbage disposal jam - Las Palmas 8D", team_001, assignee = James Bennett; comment `comment_16a0a0c53f543a1221f08de6a786cb66` body "The 8D disposal is seized ... flywheel is frozen ... full unit replacement ... Routing back to you for parts approval before I swap it. - James"; team_001 desc confirms Airtable-is-SoR.
- Slack C001 disposal msgs both 2026-06-22 (11:15 / 11:20 CDT), author James Bennett (UD92EEA47D7) - so the disposal signal exists in BOTH Slack C001 and Linear OPS-227 (OE5 is accurate; Hardness Plan cited only Linear). C004 chatter carpet 2026-05-23, punch-list 2026-05-27, cleared 2026-05-29 - all exact.
- Contacts: John Smith -> john.smith@starpm.com (Lead Maintenance Technician).
- Airtable base appPropertyOps "Property Operations"; tblMakeReady primary fldUnit; tblMaintenanceTickets primary fldTicketNumber.
- 16/16 OE tool names FOUND in StarPM_Base_Universe/7_Server_Tools_Details.json (list_bases, list_tables_for_base, get_table_schema, search_records, list_records_for_table, slack_read_channel, slack_search_public_and_private, get_issue, list_issues, get_team, list_comments, save_comment, update_records_for_table, contacts_search_contacts, slack_send_message, create_draft).
- Gmail T9 defer-scan: only 8D/make-ready match is "Las Palmas 8D. Ready to Show" (2026-05-26, to Carlos) - stale pre-disposal ready-chatter, NOT a defer/accept-timing decision.

---

## Issue Register

| # | Perspective | Severity | Issue | Fix |
|---|---|---|---|---|
| 1 | B2 / (S3 forward) | Low / non-blocking | Advance-blocker step (OE8) admits Linear-comment vs Slack-to-John; same recipient/intent (NON-FAIL channel variation) | S3: phrase the advance-blocker Outcome rubric broadly ("Agent requests John Smith's parts approval for the disposal replacement"), not channel-locked |
| 2 | B4 / (S3 forward) | Low / non-blocking | L4 (204B eviction) preserved via discrimination requirement but not named explicitly | S3: optional correct-unit-isolation rubric rewarding 8D isolation from the 204B/Rio-Bend decoys |

No blocking issue on any perspective (B1-B9). Both forward notes are S3 rubric-breadth guidance, not OE defects.

---

VERDICT: GO
