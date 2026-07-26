# AUDIT (STRICT) - S3 Rubrics - Tasks/39_6a602c8886ebb06f12354d77

Universe: StarPM / V4 (`_aux/Universe.txt` = starpm). Today 2026-07-01 America/Chicago.
Deliverable re-audited: `7_Rubrics.json` (15 Outcome, 0 Process), post the 5 operator tweaks (R1 justif, R4 title, R10 title, R11 title, R14 rewrite).
Method: independently re-derived every literal against `_aux/Universe_Split/` SSOT (row_data json.loads-decoded), re-read S3 Council A + B, ran validator + regression anchors. Did NOT trust the councils.

## VERDICT: PASS (STRICT)

Zero BLOCKER. Zero answer-leak. All 5 levers trace end-to-end. Density PASS (StarPM 40+). Anchors 62/62. Validator exit 0. Persona-scope holds. All 15 rubric TITLES (the scored criteria) are correct and grounded. The two half-applied operator tweaks flagged in the prior pass (R4 evidence, R11 evidence/justification) have been fixed and re-verified byte-exact against the live file (see Post-REVISE re-verification below); Atomicity and Flexibility now both score 5/5, so the deliverable clears every strict gate.

---

## LENS 1 - Strict QC scoring

| Sub-dimension | Score | One-line reason | What the prior council missed |
|---|---|---|---|
| Overall Rubric Quality | 5 | 0 Major, 0 Moderate; the 2 Minors are scored under Atomicity + Flexibility below (no double-count) | Councils graded the pre-tweak file, so neither saw the two half-applied tweaks |
| All-Failing Rubrics | 5 (N/A at S3) | Every target grounded in the per-task universe; no always-fail predicted | - |
| Rubric Category Balance | 5 | 15 Outcome > 0 Process | - |
| Process Rubrics | 5 | Zero is correct; SoR verification folded into R14 (Outcome-first); no ordering precondition among the 4 writes | - |
| Agent-Centric Phrasing | 5 | All criteria "The Agent .." / "The Agent's .."; no tool name in any title; record/ticket/channel ids are data, not tools | - |
| Atomicity (per-set) | 5 | R4 evidence now reads "seized or awaiting a full replacement" (the "not ready to show" tail removed), so evidence matches the trimmed atomic title; no cross-action/cross-service bundling | Prior REVISE finding (evidence re-bundled the trimmed consequence) is resolved; the pre-tweak councils could not have seen it |
| Self-Containment (per-set) | 5 | All expected values embedded (emails, record id, ticket #, channel, enum gloss); no catch-all trap | - |
| Completeness | 5 | All 5 prompt asks + the email 3 sub-asks covered; no gap | - |
| Flexibility (EM vs fuzzy) | 5 | EM for ids/emails/channel/ticket; R11 evidence + justification now carry "a final walk or a closeout step", so the title's added flexibility reaches the verification step | Prior REVISE finding (evidence pinned the narrow "final walk") is resolved |
| Accuracy (per-set) | 5 | Every literal verbatim-grounded (table below) | Council A undersold R1: called John-as-approver "interpretive, not named in data" - it is verbatim in Slack C001 |

All sub-dimensions now score 5/5 after the two REVISE-trail edits (R4 evidence, R11 evidence/justification) were applied and re-verified. See Post-REVISE re-verification.

### Accuracy per-atom evidence table (non-empty; supports Accuracy 5/5 on the scored titles)

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| john.smith@starpm.com = Lead Maintenance Technician | contacts.contacts.json | job "Lead Maintenance Technician", email john.smith@starpm.com | CONFIRMED |
| OPS-227 = disposal jam, Las Palmas 8D | linear.linear_issues.json | id "OPS-227", title "Clear garbage disposal jam - Las Palmas 8D", assignee James Bennett, completed_at null | CONFIRMED |
| MT-2026-1271 open (blank completion) | airtable tblMaintenanceTickets recac236210094352 | fldTicketNumber "MT-2026-1271", fldCompletionDate "" | CONFIRMED OPEN |
| receb057b02f20052 stale selReady 8D row | airtable tblMakeReady | fldUnit "Las Palmas 8D", fldTurnStatus "selReady", fldNotes2 "...cleared for leasing - available to show immediately", created 2026-05-01 | CONFIRMED stale |
| selReady / selProg mapping | airtable.airtable_fields.json fldTurnStatus | choices selReady=Ready, selProg=In Progress, selSched=Scheduled | CONFIRMED |
| C004 = #make-ready | slack.slack_channels.json | id "C004", name "#make-ready" | CONFIRMED |
| "Las Palmas 8D" | airtable (3 make-ready rows + MT-2026-1271) + linear OPS-227 | fldUnit "Las Palmas 8D" x3; OPS-227 title | CONFIRMED |
| disposal seized / full replacement / parts approval | linear.linear_comments.json comment_16a0a0c53f... on OPS-227 | "disposal is seized... flywheel is frozen... needs a full unit replacement... Routing back to you for parts approval" (2026-06-22, no reply) | CONFIRMED via synthesis (issue title = jam; comment = seized) |
| John Smith = the approver (R1 justif) | slack.slack_messages.json C001 | "8D disposal is seized... so I routed it to @john.smith for parts approval" | CONFIRMED verbatim (Council A undersold as interpretive) |
| Airtable = system of record | linear.linear_teams.json team_001 + airtable.airtable_tables.json tblMaintenanceTickets | "Airtable Maintenance Tickets table... is the system of record. Linear is secondary" / "System of record for maintenance work orders; Linear is secondary" | CONFIRMED |
| two later selProg 8D rows | airtable recf7aecc318b2252 (5/14) + rec651427ec0d84dd5a (6/25) | fldTurnStatus "selProg" x2 | CONFIRMED (R3 "in progress is current") |
| rest complete (repairs/carpet/deep clean/punch-list/fridge) | receb notes + rec651 notes + slack C004 | receb "in-house repairs finished, carpet cleaned and sealed, deep clean complete, punch-list resolved"; rec651 "replacement delivered and installed"; C004 "punch-list items taken care of", "deep clean is done" | CONFIRMED |
| Rio Bend 214 / MT-2026-1325 near-miss (NOT 8D) | airtable recb403fe04c2f97683 | fldTicketNumber "MT-2026-1325", "Dishwasher pull-and-replace at Rio Bend 214", fldCompletionDate "2026-06-25" (COMPLETE) | CONFIRMED isolated; no rubric references it |
| john.castillo@gmail.com decoy | contacts.contacts.json | "Water Delivery Representative", gmail | CONFIRMED decoy, unused by any rubric |
| James Bennett = junior Assistant Maintenance Technician | contacts.contacts.json + PersonaBrief p_006 | job "Assistant Maintenance Technician", Junior, 0 scripted actions | CONFIRMED (R1 requests, does not approve) |

---

## LENS 2 - Answer-leakage

Derived answer: "8D not ready; sole blocker = seized garbage disposal awaiting parts approval; MT-2026-1271 open."

- Synthesis required: CONFIRMED. OPS-227 issue TITLE reads "Clear garbage disposal jam" (routine). The seized / full-replacement / parts-approval flip lives ONLY in the separate `list_comments` read (comment_16a0a0c53f...). The "not complete" verdict additionally needs the Airtable ticket read (MT-2026-1271 blank) plus recognizing the 5/1 ready row is superseded. No single read yields the answer.
- Agent-readable leak: NONE. The prompt states the OPPOSITE framing ("on paper it looks about there") and never names the disposal blocker. Rubrics are judge-side only (the agent never sees them), so no rubric body can leak to the agent. OE bodies carry the solution but are judge-side by design.
- Verdict: NO BLOCKER.

---

## LENS 3 - Hardness end-to-end (5 levers, each (a) prompt (b) OE (c) rubric (d) atom)

| Lever | (a) Prompt sentence | (b) OE step | (c) Rubric (traversal-dependent) | (d) Universe atom | Status |
|---|---|---|---|---|---|
| L10 temporal supersession | L1 "this turn has been dragging since May"; L5 "some of it is stale by now" | OE2 (receb 5/1 selReady vs recf7 5/14 + rec651 6/25 selProg); OE4 (ready chatter predates June) | R12 ("not ready despite the logged make-ready status"), R2, R3 | receb057b02f20052 selReady 5/1 vs recf7aecc318b2252 + rec651427ec0d84dd5a selProg | TRACED |
| L2 Airtable-is-SoR skip | L3 "confirm where each piece actually landed instead of going off what someone said in passing" | OE1, OE3 (MT-2026-1271 blank = open in SoR), OE6 (team_001 charter) | R14 ("not complete in Airtable, the system of record, MT-2026-1271 open") | linear_teams team_001 + airtable_tables tblMaintenanceTickets ("system of record") + recac236210094352 blank fldCompletionDate | TRACED |
| L1 latching | L1 "the punch-list got knocked out and the carpet's in, so on paper it looks about there" | OE4 (5/23 carpet, 5/27 punch-list, 5/29 cleared chatter) | R12 ("despite... earlier channel messages indicating it was cleared"), R6, R7 | slack 140558bdd3... ("punch-list items on 8D are taken care of") + 21f0475... ("Carpet is done on 8D") | TRACED |
| L4 search-cap eviction | L3 "Everything that was supposed to happen on that unit, confirm where each piece actually landed" (thoroughness demand) | OE2/OE3 pin exact 8D record ids past the swarm | R2/R3/R4 (pin receb057b02f20052), R14 (pin MT-2026-1271): a 204B-evicted agent cannot produce these exact ids | 61 "204B" vs 6 "8D" occurrences in airtable_records | TRACED (prompt anchor is the softest of the 5 - implicit thoroughness, not an explicit other-unit mention; rubric anchor is hard via exact record id) |
| L3 missing reply | L3 "if something's still open, run down whatever it's waiting on and get it moving" | OE7 ("No reply follows, so the parts approval never came") | R13, R1, R10 (the "full replacement / pending parts approval" facts exist only in the chased OPS-227 comment) | comment_16a0a0c53f... ("Routing back to you for parts approval before I swap it"), no reply | TRACED |

No HARDNESS_REGRESSION. All five trace with cited (a)(b)(c)(d). L4's prompt anchor is the softest (implicit thoroughness) but its rubric anchor (exact record-id pinning) is hard and load-bearing, so the lever is not "probably/implied" - it is id-forced.

---

## LENS 4 - Strict density (StarPM V4: 40 design / 15 floor, per model)

Minimal-exploration trajectory forced by the rubric set: list_bases + list_tables (2), search tblMakeReady 8D (1), search tblMaintenanceTickets 8D (1), read C004 (1), read C001 (1), get_issue OPS-227 (1), list_comments OPS-227 (1), contacts John Smith (1), + optional get_team/schema (0-2), + 4 writes (save_comment R1, update_records R2/R3/R4, slack_send_message R5/R6/R7, create_draft R8-R11).

- Theoretical perfect-agent floor: ~13 (below the 15 QC-spec floor, but this is a best-case not the gate metric).
- Realistic hard minimum (aggressive batching): ~15-18 across 4+ services (clears the 15 floor).
- Realistic per-model midpoint: ~44-47 once the 5 levers add exploration (204B eviction re-queries, channel history reads, comment-thread chase, near-miss Rio Bend disambiguation, SoR cross-check, schema/contact confirms). Consistent with Hardness_Plan component sum (38-59, mid 48.5) and Council B (~47).

Midpoint ~44-47 >= 40 StarPM V4 design target -> PASS (per Opus and per Gemini). Not applying the V3 50/40 scheme. Note: margin over 40 is present but not V3-scale; watch real Opus/Gemini runs for THIN risk if a model batches unusually aggressively.

---

## LENS 5 - Adversarial veteran

- Implicit not-ready framing preserved: YES. Prompt frames it as "looks about there / don't want it coming back on me"; the agent must DERIVE not-ready (R12/R14). No spoiler.
- Entity-drift seams: CLEAN. Rubrics use "John Smith" / "john.smith@starpm.com"; decoy john.castillo@gmail.com unused. No rubric references Rio Bend 214 / MT-2026-1325 / the 204B swarm; every 8D rubric pins 8D-specific ids.
- Silent Process-as-Outcome: NONE. Three-condition test applied to all 15 - every one tests a final state or a derived conclusion, not a method-for-its-own-sake. R1 is method-agnostic (comment OR Slack OR email), so it tests the outcome (approval requested), not a channel.
- Tool-name leak in titles: NONE ("draft", "email", "posts an update", "make-ready record/channel" are generic; C004 is a channel id, not a tool).
- Em-dash / en-dash: 0 across all fields (independently scanned).
- "at least N" without mandate: NONE.
- "approximately" / "(or similar)" near ids/dates: NONE. R14 "no completion date" is exact.
- Single-channel lock-in: only where the prompt named the channel. R1 advance = method-agnostic (correct). R5-R7 make-ready + R8-R11 email = prompt-named (authorized). R14 SoR = accepts MT-2026-1271 OR make-ready selProg (not locked).
- PERSONA-SCOPE (James = JUNIOR assistant tech): NO overreach. R1 requires REQUEST parts approval (routing up to John, matching the C001 "routed it to @john.smith" and the comment "Routing back to you"), never APPROVE/sign-off. R2/R3/R4 correct a data record (in scope). R8-R11 draft up to the Lead. No rubric makes James authorize the parts.
- ACT-VS-DEFER: NO legitimate defer overridden. The live signal (C001) is "8D disposal seized, waiting on parts approval, that unit's still open." No authoritative decision to defer the disposal or leave 8D ready exists; the stale receb row is precisely the artifact being corrected. The write rubrics reflect the "still open" reality.
- NEAR-MISS: an agent reporting Rio Bend 214 / MT-2026-1325 as 8D satisfies ZERO rubrics (all anchor to "Las Palmas 8D" + exact ids receb057b02f20052 / MT-2026-1271 / OPS-227).

---

## LENS 7 - Anti-rationalization log (every considered-and-excluded item)

1. "make-ready ticket MT-2026-1271" label (R14): MT-2026-1271 lives in tblMaintenanceTickets (a Maintenance Ticket), not tblMakeReady. Considered flagging as an Accuracy mislabel. EXCLUDED (hard): the verifiable atom (MT-2026-1271, blank completion, open) is exact and unambiguous; there is no "make-ready ticket" table to confuse it with; the ticket's own description is the make-ready turn's ticket ("Make-Ready Turn record created..."), so "make-ready ticket" is a true functional descriptor. NOTE-level, non-blocking.
2. R14 evidence OR-branch accepts the make-ready record's selProg as an equivalent Airtable-SoR signal. Considered flagging as weakening L2 (agent could skip tblMaintenanceTickets). EXCLUDED (hard): the lever L2 is defined in Hardness_Plan as "Structured-DB (Airtable) skip" - both tblMakeReady and tblMaintenanceTickets are the structured Airtable DB, so either branch still forces Airtable-over-Slack/Linear-chatter, which is the lever mechanism. The evidence is about the agent's RECOGNITION/trajectory grounding (not the record end-state), and the primary branch (MT-2026-1271 blank) is clean and present. Acceptable per the lever definition; not a REVISE.
3. R10 bundles seized + full-replacement + awaiting-parts-approval. Considered flagging as non-atomic. EXCLUDED (hard): all three are attributes of ONE blocker from the single OPS-227 comment in one artifact (email); matches the blessed one-thing-attributes coupling. Optional split remains optional.
4. Density theoretical floor ~13 < 15. Considered flagging as an INSUFFICIENT-density risk. EXCLUDED (hard): the StarPM gate metric is the realistic average of actual runs (design 40+), not the perfect-agent floor; the 5 levers push realistic per-model midpoint to ~44-47. Logged as a THIN watch-item, not a blocker.

No item was rationalized away improperly. The two items NOT excluded (R4 + R11 evidence mismatches) are promoted to the REVISE trail below.

---

## LENS 8 - Regression anchors + validator

- `python3 Validators/test_regression_anchors.py`: 62 passed, 0 failed out of 62 (ANCHORS_EXIT=0). Every anchor fired; no silent validator regression.
- `python3 Validators/validate.py --phase rubrics --task Tasks/39_6a602c8886ebb06f12354d77`: [PASS] 0 fails, 0 warns, 5 notes, VALIDATOR_EXIT=0. The 5 notes are benign (universe=starpm; Feasible_Surface 15 tables; Fact_Ledger 403 amounts / 206 emails; counts outcome=15 process=0; Overall Rubric Quality 0/15 with any issue).

---

## REVISE trail (fix-in-place; both MINOR)

1. [MINOR] R4 evidence over-specifies vs the trimmed title -- `7_Rubrics.json` R4 `evidence` -- change "...for language stating the garbage disposal is seized or awaiting replacement and the unit is not ready to show." to drop the trailing "and the unit is not ready to show" (so the evidence matches the atomic title, which now only requires seized/awaiting-replacement). This completes the operator's atomicity trim, which is currently half-applied (title trimmed, evidence not).
2. [MINOR] R11 evidence + justification negate the title's added flexibility -- `7_Rubrics.json` R11 `evidence` (and `justification`) -- change evidence "...and complete the final walk to close." to "...and complete a final walk or a closeout step to close." and change justification "...then a final walk." to "...then a final walk or a closeout step," so the "or closeout step" flexibility the operator added to the title is honored at the verification step.

Both are one-line edits. The rubric titles (scored criteria) are correct and require no change. After these two edits, Atomicity and Flexibility return to 5/5 and the verdict becomes PASS (STRICT).

## Propagation

None. No PROPAGATE TO S1 / S2. Root cause is two post-council evidence lines in the rubric file itself, not the prompt or OE.


## Post-REVISE re-verification

Both REVISE-trail edits were verified applied byte-exact against the live `7_Rubrics.json` (read directly, not on the operator's word):
- R4 `evidence` now = "Check the updated fldNotes2 on record receb057b02f20052 for language stating the garbage disposal is seized or awaiting a full replacement." The "and the unit is not ready to show" clause is removed; evidence matches the atomic title. Atomicity 4 -> 5.
- R11 `justification` now ends "...then a final walk or a closeout step." and `evidence` now = "...install it, and complete a final walk or a closeout step to close." The title's "or closeout step" flexibility is honored at verification. Flexibility 4 -> 5.

No title/criterion changed; no grounded atom changed. Re-ran this session: em/en-dash scan 0; `validate.py --phase rubrics` PASS (0 fails, 0 warns, 5 notes, exit 0). All 10 rubric sub-dims 5/5; zero BLOCKER; all 5 levers traced; density PASS (StarPM 40+); anchors 62/62. Verdict upgraded REVISE -> PASS (STRICT).