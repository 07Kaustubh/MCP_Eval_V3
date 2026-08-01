# Rubric Coverage Matrix — Task 45 (StarPM V4)

**Artifact:** `7_Rubrics.json` — 19 Outcome, 0 Process.
**Correct answer under test:** Mesa Vista 4C is NOT marketing-ready -> HOLD / kick-back on the current in-progress turn `recbd087a4abd605b` (fldTurnStatus selProg).
**Validator:** PASS (0 fails, 8 benign warns). **Council A:** GO (all grounded). **Council B:** GO (0 Major / 0 Moderate / 2 Minor, both fixed pre-AUDIT).
**AUDIT verdict:** PASS (STRICT) (`bg_3c49d506`) - 0 Major / 0 Moderate / 0 counting Minor; all 5 levers carried; regression anchors 62/62. All S3 gates GREEN; ready for PIPELINE FINAL.

## Rubric index (file order)

| # | Sub | Rubric (short) | Write/response surface |
|---|---|---|---|
| R1 | 1.1 | records QC determination on the current turn recbd087a4abd605b | Airtable |
| R2 | 1.2 | does NOT advance the turn to Ready; stays In Progress | Airtable (negative) |
| R3 | 1.2 | recorded determination states held / not signed off | Airtable |
| R4 | 1.1 | opens Linear issue on Operations team (OPS) for the 4C QC hold | Linear |
| R5 | 1.2 | ticket states deep-clean bill $387 unpaid | Linear ticket |
| R6 | 1.2 | ticket states interior-repaint bill $1,340 unpaid | Linear ticket |
| R7 | 1.2 | ticket states turn In Progress with 2026-06-30 target past due | Linear ticket |
| R8 | 1.2 | ticket states 2026-07-15 QC re-inspection pending | Linear ticket |
| R9 | 1.1 | posts in #make-ready (C004) about 4C | Slack |
| R10 | 1.2 | post states 4C held / not marketing-ready | Slack |
| R11 | 1.1 | drafts email to carlos.mendez@starpm.com about 4C | Gmail draft |
| R12 | 1.2 | email states 4C held / not signed off | Gmail draft |
| R13 | 1.2 | email identifies the deep-clean + interior-repaint bills unpaid (the specifics) | Gmail draft |
| R14 | 1.1 | notifies Brooke (brooke.phillips@starpm.com or Slack) held / do not market | Gmail or Slack (method-agnostic) |
| R15 | 2.1 | final response: 4C not marketing-ready / held / not released | final response |
| R16 | 2.1 | final response: deep-clean bill $387 unpaid | final response |
| R17 | 2.1 | final response: interior-repaint bill $1,340 unpaid | final response |
| R18 | 2.1 | final response: turn In Progress with 2026-06-30 target past due | final response |
| R19 | 2.1 | final response: 2026-07-15 QC re-inspection not yet occurred | final response |

## Prompt sentence -> OE step -> rubric(s)

| Prompt clause | OE step(s) | Rubric(s) |
|---|---|---|
| "wrapped from its June turn ... wants it released ... Brooke ready to market on his word" (latching setup, L1) | OE1, OE4, OE5 (decoys) | (context; drives investigation — no rubric, correctly) |
| "I am not signing off ... I need the real state of that turn" | OE1-OE9 | R15 (real state = held) |
| "moved out in the middle of June ... target-ready date at the end of the month, which has already come and gone" | OE1, OE2, OE3 | R1 (binds recbd087 by this content), R7, R18 (6/30 past due) |
| "The two scopes that carried this turn were the deep clean and the interior repaint" | OE6 | R5, R6, R13, R16, R17 |
| "whether both are genuinely closed ... vendor side reconciled" | OE6 | R5, R6 (ticket unpaid), R16, R17 (response unpaid) |
| "billed but not finished, or finished with the bill still sitting unpaid, does not count as closed" (the QC standard) | OE6, OE9 | applied by R5/R6/R16/R17 (finished-but-unpaid = not closed) |
| "a re-inspection on the calendar for the middle of this month ... factors into whether I can call this one done" | OE7 | R8 (ticket), R19 (response) |
| "record your QC determination on that turn and give me the call ... hold it ... does not go to listing until every outstanding scope is closed and signed off" | OE9, OE10 | R1, R2, R3 (record determination = hold on recbd087), R15 (give the call plainly) |
| "Open a ticket on the issue tracker spelling out exactly what is still left on it" | OE11, OE12 | R4 (issue) + R5, R6, R7, R8 (spell out the 4 items) |
| "post where it lands in the make-ready channel" | OE13 | R9, R10 |
| "get an email together for Carlos with the specifics" | OE14 | R11, R12, R13 |
| "If I am holding it back, Brooke needs to hear it from us before she markets it" | OE15 | R14 (method-agnostic) |

## Gap check (every prompt ask has a rubric)
No gaps. Each of the 6 write asks (record determination / open ticket / post channel / email Carlos / notify Brooke) plus the investigation-report ask (give the call + specific reasons) has >=1 carrier. The QC standard (billed-but-unpaid != closed) is operationalized by the unpaid-bill rubrics.

## Surplus check (every rubric maps to a prompt ask)
No surplus. R1-R3 -> record determination; R4-R8 -> ticket; R9-R10 -> channel post; R11-R13 -> email Carlos; R14 -> notify Brooke; R15 -> give the call; R16-R17 -> vendor reconcile; R18 -> past-due target; R19 -> re-inspection. R15-R19 are legitimate 2.1 key-fact rubrics grounded in the prompt's first-paragraph direct-report asks ("I need the real state", "I need to know whether both are genuinely closed", "factors into whether I can call this one done"). No beyond-prompt rubric.

## Anti-dilution design
- Each of the 4 outstanding FACTS graded in exactly 2 artifacts: the Linear ticket (R5-R8, "spelling out exactly what is still left") and the final response (R16-R19, "give me the call / the reasons"). They fail independently (perfect ticket + vague response fails R16-R19 while R5-R8 pass). Matches the Task1 V4-reference 2-artifact discipline; not 3x repetition.
- The email specifics (R13) grade the two unpaid bills as ONE coupled rubric (the crux Carlos claimed were handled), not a re-atomization of all 4 items.
- The HOLD DECISION graded on 5 surfaces (R3 Airtable / R10 Slack / R12 email / R14 Brooke / R15 final response) because the prompt names each surface explicitly. Independent, non-overlapping (a single error trips only one).

## Hardness-lever carrier map (Council B + AUDIT confirm)
| Lever | Carrier rubric(s) whose value depends on traversing it |
|---|---|
| L2 structured-DB skip (SYMMETRIC) | R2 (not-advanced-to-Ready, only knowable from the selProg row), R7/R18 (In Progress + 6/30, only in tblMakeReady), R16/R17 (unpaid balances, only in QuickBooks) |
| L1/L10 latching / supersession (OPUS-sel) | R1 (determination must land on recbd087, not the recc8534 selReady decoy or the maint tickets), R2 (must not flip to Ready) |
| L31 explicit negative directive (GEMINI-sel) | R15 (final response NOT marketing-ready / held / not listed); reinforced by R2/R3/R10/R12/R14 |
| L7 multi-write | R1 + R4 + R9 + R11 + R14 (6 distinct writes across 5 services) |
| L9 future-event + past-due | R8/R19 (7/15 re-inspection pending) + R7/R18 (6/30 past due) |

## Sub-category tally
Outcome 1.1 (write actions): R1, R4, R9, R11, R14 = 5. Outcome 1.2 (action content): R2, R3, R5, R6, R7, R8, R10, R12, R13 = 9. Outcome 2.1 (final-response facts): R15, R16, R17, R18, R19 = 5. Process: 0 (check_ordering_coverage confirms no ordering language). Total 19.
