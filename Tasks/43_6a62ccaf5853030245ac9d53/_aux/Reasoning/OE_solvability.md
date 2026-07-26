# OE Solvability - Task 43_6a62ccaf5853030245ac9d53 (S2)

Universe: StarPM (V4, dual-model). Persona: Carlos Mendez, Onsite Property Manager. Business function: Property Operations.
Deliverable: `6_Oracle_Events.txt`, 28 numbered steps, 24 discovery steps + 4 write actions.

## The reconciliation in one line

Linda Castillo was billed 1622.00 on invoice 2026-534 (445653930748) for the Mesa Vista 4C turn. The four vendor bills for the unit show the repaint was 1340.00 (not the 1140.00 on her invoice) and the closet trim 85.00 (not 95.00), while the 85.00 unit condition walk is in-house time that stays off her side. Corrected owner pass-through: 387.00 + 1340.00 + 85.00 = 1812.00, a net 190.00 understatement. The figure exists nowhere in the universe as a total; it only exists as a derivation across four AP bills.

## OE-to-prompt coverage map (forward)

| Prompt ask (sentence) | Covering OE |
|---|---|
| Close out Mesa Vista 4C on the owner side / log it closed | OE 2, 3, 4, 5, 6, 25 |
| Linda Castillo owns that unit | OE 1, 9 |
| I billed her and sent a summary calling it done (three named scopes) | OE 7, 10, 11 |
| Be sure what she was actually charged holds up | OE 11, 13, 14, 15, 17, 21 |
| Every dollar must line up with what we paid out, to the dollar, no more and no less | OE 13, 21 |
| Go back to what each vendor charged us and set it against her line items | OE 13, 14, 15, 16, 17, 18 |
| Only outside vendor work belongs on her side | OE 19, 20 |
| Our own time, an internal walk or a condition check, stays off her bill | OE 4, 18, 19, 20 |
| If clean, log closed; if not, do not create a second bill | OE 12, 24 |
| Correct the invoice she is holding so it carries the right figure | OE 24 |
| Get the 4C make-ready record in Airtable updated with final owner cost and unit fully closed | OE 5, 25 |
| Email Linda a short note letting her know where it landed | OE 1, 26 |
| Drop a line in our channel for the crew and front office | OE 22, 23, 27 |

Reverse map: no OE step goes beyond the prompt. OE 16 and OE 20 exist to bind the correction to the right record and to prevent the exclusion from being mis-grounded on payee identity, both of which serve the "to the dollar" and "only outside vendor work" asks. No Linear step was written: the prompt asks for no ticket, and StarPM routes make-ready state to Airtable with Linear as the secondary mirror, so a Linear write would have been both scope creep and a service mismatch.

## OE-to-rubric mapping preview (for S3)

| OE | Becomes |
|---|---|
| OE 24 (update_invoice on 445653930748 to 1812.00) | Outcome 1.1 write, plus Outcome 1.2 content on the corrected line amounts (1340.00 repaint, 85.00 closet). Also the negative-guard rubric: does NOT create a second owner invoice or credit memo. |
| OE 25 (update_records_for_table on recc8534b3fd13954) | Outcome 1.1 write, plus Outcome 1.2 content on final owner cost + closed state in fldNotes2. Grade on content, not record id (OE 25 says so explicitly). |
| OE 26 (create_draft to linda.castillo@gmail.com) | Outcome 1.1 write, plus Outcome 1.2 content on the corrected figure and the two line corrections. Draft only, no send tool exists, so no rubric may require a sent email. |
| OE 27 (slack_send_message to C004) | Outcome 1.1 write, plus Outcome 1.2 content on the corrected figure superseding the original. Must NOT lock the channel: C005 and C006 are valid alternatives, so channel-lock-in would be a Major per the Rubrics Eval 2.7 escalation rule. |
| OE 28 (facts the agent must land) | Outcome 2.1 candidates: the 1812.00 corrected pass-through; the 190.00 net understatement; the exclusion of the 85.00 internal walk. |
| OE 1 to OE 23 | Pure discovery. No rubric. The Outcome rubrics above prove the reads happened. Atomicity note carried from Learnings item 5 (Task 40 R12): do not bundle two facts sourced from different records into one content rubric. The 1340.00 repaint (bill PD-2026-09) and the 85.00 closet trim (bill 2026-519) come from separate records and must be separate criteria. |

## Hardness levers exercised

| Lever | OE steps |
|---|---|
| L2 structured-DB skip (symmetric flagship) | OE 13, 15, 17, 21 - the 1340.00 and 85.00 actuals exist only on AP bills |
| L10 reversal / supersession | OE 3, 7, 11, 15, 17, 24, 27 - the stale AR invoice and the stale Airtable row are superseded by the bills |
| L6 near-miss entity | OE 1 and OE 9 (Linda vs Pete vs John Castillo, at both the contacts and customer layers), OE 3 (date-field inversion between the two 4C rows), OE 10 (2026-537 phantom invoice number, 2026-AP-0184 same-owner 1340.00 decoy carrying a "Tommy Reyes unit" surname collision, 2547 same-owner 385.00 deep-clean pass-through at Rio Bend), OE 16 (ten-bill 1340.00 cluster plus the 1140-versus-1380 mirror bill 173322471681 on the same account code), OE 17 to OE 19 (twin 85.00) |
| L11 / L9 net-vs-gross | OE 18, 19, 21, 25, 28 - the 1897.00, 1727.00 and 1810.00 decoy figures. DISPLACED, per Learnings item 9 (Task 41 pattern): the lever is co-located with L2's discovery gate rather than sitting two hops behind it, so it is reachable in the same search_bills call, but under the plan's own roughly 0-of-12 solve prediction it will still produce no independent observable fail. Do not credit it at S4 as a separate measured stump. |
| L1 latching (reserve) | OE 3, 4, 6, 7 - "market-ready", "fully wrapped up", selReady |

## The pivotal question, and how the OE arms it

The task's hardest judgment is which of two 85.00 charges on the same unit is owner-billable. Both AP bills open with the same "Internal labor charge for <a StarPM person>" template (the only two such records in a 625-entity ledger), so that phrase discriminates nothing. Council A and Council B both blocked round 1 for resolving this by omission. OE 17 now quotes the closet bill's PrivateNote in full including that opening phrase; OE 18 states outright that the phrase appears on both records; and OE 19 decides the question on five grounds (the shared template marks who performed the work not who was paid; the genuinely in-house 4C items produced no AP bill at all so "our own time" generated no payout to pass through; the walk bill is literally a condition inspection matching the prompt's exclusion wording; account coding 64 Owner Reserve (Trust) versus 61 Supplies; pass-through instruction versus intake-that-drives-pass-through) while explicitly naming and answering the three records that attribute the trim fix to Tony Reyes. This matters downstream: rubrics written from an under-armed OE would grade a well-reasoned 1727.00 run as a model failure when part of the failure was OE concealment.

## Density and breadth

Per-model, StarPM scheme (>= 40 PASS, 15-39 THIN, < 15 INSUFFICIENT). AUDIT re-anchored these on 36 real trajectories from Tasks 39, 40 and 41 rather than on the Hardness Plan's assumed uniform Gemini delta of minus 9.5, which does not hold empirically (Task 40's delta was 1.5):

| Model | Solving run | Stumped run | Blended | Band |
|---|---:|---:|---:|---|
| Opus 4.8 | 47 | 38 | 39.5 | PASS |
| Gemini | 41 | 31 | 32.7 | THIN, far clear of the 15 floor |

Breadth: 5 distinct services (QuickBooks ~45-48%, Airtable ~21%, Gmail ~18%, Slack ~9%, Contacts ~7%), dominant well under 60%, meeting the Hardness Brief's "4-write / 5-service OE" target. The plan's breadth table projected 6 services including Linear; no Linear step was written because the prompt asks for no ticket and StarPM routes make-ready state to Airtable with Linear as the secondary mirror, so a Linear step would have been both scope creep and a service mismatch.

Two carry-forwards for S4. First, the plan's THIN acceptance rests partly on "writes execute on BOTH models", and that does not hold on the modal branch: prompt sentence 8 makes three of the four writes conditional on the charges not being clean, so a stumped run (predicted at roughly 0 of 12) takes the one-write branch and sheds calls. Second, the actionable Gemini anomaly threshold is below 24, not below 30; a Gemini run in the high twenties is the expected stumped shape, not a density defect.

## Verdicts

- `validate.py --phase oe`: PASS, 0 fails, 0 warns, 3 notes (28 OE steps).
- `verify_universe_atoms.py`: PASS, 0 fails, 0 warns, 15 atoms.
- `test_regression_anchors.py`: 62/62 PASS.
- Council A (grounding + convention + narrative state + action-vs-prescription + solvability): round 1 BLOCK on 4 Major (selective quotation on OE 17, false asymmetry on OE 18/19, omitted C004 message, unique-ground-truth risk) plus 4 Moderate. All fixed in place. Round 2 verdict recorded in `_aux/Council_Reports/S2_A_grounding.md`.
- Council B (QC scoring + adversarial + density + hardness + propagation + completeness + service mapping): round 1 BLOCK on 1 Major with OE Completeness 5/5 and OE Accuracy 4/5; all 11 issues addressed; round 2 GO with both sub-dims 5/5, no scope creep, no service mismatch, no hardness regression, all four Phase 4.0 sweep items passing, and no `PROPAGATE TO S1`. Report: `_aux/Council_Reports/S2_B_adversarial.md`.
- Strict veteran AUDIT: round 1 REVISE on 5 Major and 10 Minor (every finding independently verified against the universe before it was applied); round 2 `PASS (STRICT)` with OE Completeness 5/5 and OE Accuracy 5/5, zero remaining Major, and no `PROPAGATE TO S1` in either round. Two Minor residuals adjudicated and recorded in `_aux/Verification_s2.md` items 6 and 7; AUDIT withdrew its own verbosity finding on re-read. Report: `_aux/Council_Reports/AUDIT_oe.md`; cross-source check: `_aux/Verification_audit_oe.md`.

The single most valuable catch of the whole pass came from AUDIT, not the councils, and it was a defect Council A had introduced: Council A demanded the Jaime Salinas Slack post be added to OE 22, then signed off without checking that OE 22's queries could reach it. They cannot, because that message names neither the unit nor the property, so only the channel read in OE 23 surfaces it. AUDIT's framing of the pattern miss is worth carrying forward: both councils verified atom EXISTENCE and never atom RETRIEVABILITY.
