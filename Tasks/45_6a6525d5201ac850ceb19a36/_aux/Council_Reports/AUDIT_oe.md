# PIPELINE AUDIT — Oracle Events (Strictest Interpretation) — Task 45

**Task:** 45_6a6525d5201ac850ceb19a36 · **Universe:** starpm (V4, confirmed `_aux/Universe.txt`) · **Today:** 2026-07-01 America/Chicago
**Phase:** `--phase oe` (auto-fire from S2) · **Mode:** read-only veteran second-opinion, strictest reading
**Deliverable:** `6_Oracle_Events.txt` (OE1-OE15 + final-response spec)
**Prior verdicts (re-read, NOT trusted):** S2_A_grounding GO · S2_B_adversarial GO

## VERDICT: **REVISE** — flag **PROPAGATE TO S1** (S2 fallback documented). STOP.

One substantive finding drives the verdict: the QC-hold **outstanding-items ground-truth set is under-inclusive**. A rule-13 every-service sweep of QuickBooks surfaces additional unpaid "Mesa Vista Unit 4C" vendor bills that OE6's reconciliation and OE9's determination omit, while OE6 itself prescribes `get_aged_payables` (which returns them). Everything else is a genuine 5/5: all 15 cited atoms verified verbatim from source, every StarPM tool/param correct, all five hardness levers preserved, zero answer-leakage, zero dashes. The determination (HOLD) is correct and robust; the defect is completeness of the reasons, not the verdict.

---

## Deterministic floors (cited, not re-derived)
- `validate.py --phase oe` = PASS · 0 fails · 0 warns · 3 notes (universe=starpm; OE step count 15; no closed fiscal periods -> lifecycle precondition check skipped). All three notes informational; none a defect.
- `verify_universe_atoms.py` = 8 atoms · 0 FAIL · 1 WARN (date 2026-07-15 outside active window = intentional L9 future QC re-inspection, prompt-acknowledged; benign).
- `test_regression_anchors.py` = 62/62 PASS (Lens 8 satisfied).
- Rubric-phase gates (check_rubric_antipatterns / check_oe_rubric_sync / check_ordering_coverage / check_criterion_dependencies) = N/A at S2 (7_Rubrics.json not yet produced). Correctly not faulted.

---

## LENS 1 — Strict QC scoring (OE sub-dims) + per-atom evidence table

### Per-atom evidence table (independently re-parsed from `_aux/Universe_Split/`, row_data decoded)
| Atom asserted (OE) | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| recbd087a4abd605b selProg, moveOut 6/15, target 6/30, created 5/22 (OE1/2/3/10) | airtable_records id=recbd087a4abd605b tbl=tblMakeReady | fldTurnStatus=selProg, fldMoveOut=2026-06-15, fldTargetReady=2026-06-30, created 2026-05-22 21:14:07 | PASS |
| fldNotes2 verbatim "...deep clean and interior repaint still tracking... signed off" (OE3) | same record fldNotes2 | exact string match | PASS |
| recc8534b3fd13954 selReady, moveOut 6/1, target 6/14, created 5/29 LATER (OE1/2) | airtable_records id=recc8534b3fd13954 tbl=tblMakeReady | selReady, 2026-06-01, 2026-06-14, created 2026-05-29 14:26:59 | PASS (later-created supersession trap real) |
| reca424761ae15355 MR-4C-2026-08 "all complete/market-ready/Brooke notified" (OE4) | airtable_records id=reca424761ae15355 tbl=tblMaintenanceTickets | fldDescription "All make-ready work... complete... market-ready... Brooke Phillips notified..." | PASS (decoy) |
| rec12969a3fdb0852 MT-2026-084 "make-ready turn opened for unit 4C" (OE4) | airtable_records id=rec12969a3fdb0852 tbl=tblMaintenanceTickets | fldDescription "Make-ready turn opened for unit 4C at Mesa Vista..." | PASS |
| bill 195089456477 Sunshine, 2026-SC-4C, Total/Bal 387.00, due 5/31 (OE6) | quickbooks_entities id=195089456477 | entity_type=bill, Balance 387.0, DueDate 2026-05-31, VendorRef Sunshine Cleaning | PASS (unpaid) |
| bill 696089964235 PD-2026-09, Total/Bal 1340.00, due 5/31 (OE6) | quickbooks_entities id=696089964235 | entity_type=bill, Balance 1340.0, DueDate 2026-05-31 | PASS (unpaid) |
| invoice 445653930748 2026-534, Bal 1622.00 (OE6, corroboration) | quickbooks_entities id=445653930748 | entity_type=**invoice** (CustomerRef Linda Castillo, no VendorRef), Balance 1622.0 | PASS (receivable; OE labels it "invoice" correctly) |
| calendar 7/15 QC inspection, event_id 360b2149..., confirmed, attendees carlos/brooke/wesley (OE7) | gcalendar_events properties.event_id=360b2149b7d0c10fa65224c281cdb53f | title "Make-Ready QC Inspection - Mesa Vista 4C", start 2026-07-15T10:00-05:00, end 10:45, confirmed | PASS (only future 4C-specific event; both vendor events are 5/21, past) |
| Slack C004 = #make-ready; 3 Carlos posts verbatim (OE5/13) | slack_channels C004; slack_messages user U07E4512181 | C004->#make-ready; U07E4512181=Carlos Mendez; all 3 quotes exact, created_at 2026-05-23 UTC | PASS |
| Carlos = Onsite Property Manager; Brooke = Apartment Property Supervisor (OE8) | contacts.contacts | job "Onsite Property Manager" / "Apartment Property Supervisor" | PASS |
| Linear team "Operations" (OE11) | linear_teams | team_001 name "Operations" key OPS | PASS |

**Every asserted atom is TRUE.** OE **Accuracy = 5/5** (no false atom, no count error, verbatim quotes exact, every StarPM param correct).

### OE Completeness = **< 5 (REVISE)** — the outstanding-items SET is under-inclusive
OE6 ("Reconcile the vendor side... run get_aged_payables") and OE9/OE10/OE12/OE13/OE14/final-response enumerate the outstanding items as **exactly**: unpaid deep-clean 387.00, unpaid repaint 1340.00, record still In Progress + past-due 6/30, 7/15 re-inspection. A rule-13 sweep of `quickbooks_entities` for open "Mesa Vista Unit 4C" payables returns **FOUR** entity_type=bill rows with nonzero Balance and DueDate 2026-05-31, not two:

| id | type | Bal | line description | turn |
|---|---|---|---|---|
| 195089456477 | bill | 387.0 | Post-move-out deep clean, Mesa Vista Unit 4C | current (in OE) |
| 696089964235 | bill | 1340.0 | Interior repaint, full unit - Mesa Vista Unit 4C | current (in OE) |
| **991582431419** | **bill** | **85.0** | "Unit condition inspection and punch list documentation - Mesa Vista Unit 4C, vacated turnover: deep cleaning scope, full interior repaint, kitchen faucet leak..." | **current — OMITTED** |
| **546359391323** | **bill** | **85.0** | "Bedroom closet trim paint touch-up, Mesa Vista Unit 4C - same-day repair following final QC walkthrough" | prior (recc8534 closet-trim) — OMITTED |

`991582431419` is unambiguously a **current-turn** unpaid 4C vendor payable (its line names the exact current-turn scope: deep clean + interior repaint + kitchen faucet leak; NOTE "make-ready walk of Mesa Vista 4C... turnover intake"). OE6 prescribes `get_aged_payables`, which returns all four; the OE silently narrows to two with no stated exclusion reason. A faithful trajectory agent running the prescribed call **will** encounter 3-4 unpaid 4C bills and has no ground-truth guidance on the two $85 rows. Under the strictest reading (OE Completeness must be 5/5; rule-13 every-service sweep is binding), an "outstanding items are [...]" claim that omits a real in-scope open item is incomplete. **This is the verdict driver.**

**Lens 1 :: REVISE** (Completeness). Accuracy 5/5.

---

## LENS 2 — Answer-leakage sweep :: PASS (no BLOCKER)
- Prompt string-searched: contains **none** of 387 / 1340 / 1622 / selProg / any record id / the verdict "not ready". The decision is framed conditionally ("if it is genuinely marketing-ready, sign it off; if it is not... hold it") — the grounded sign-off-OR-kick-back ask required by L31, not a pre-decided answer.
- Persona context the prompt DOES state (target date "already come and gone"; a "re-inspection... middle of this month"; the "billed but unpaid does not count as closed" standard) are decision INPUTS/policy, not the conclusion. The HOLD still requires synthesis across make-ready SoR (selProg) + QuickBooks (unpaid bills) + calendar (future re-inspection).
- No single universe source states "4C is not ready, hold it": recbd087 fldNotes2 is raw state ("still tracking"); reca424 + recc8534 + C004 chatter say the OPPOSITE (done). L6 verbatim-answer safe.
- Note: the omitted-bills finding (Lens 1) would, if anything, REDUCE leakage risk (more to derive). Not a leakage vector.

---

## LENS 3 — Hardness end-to-end trace (rubric leg deferred to S3) :: PRESERVED
| Lever | Prompt sentence | OE step | Fact_Ledger / universe atom |
|---|---|---|---|
| L2 structured-DB skip (SYMMETRIC) | "I need to know whether both are genuinely closed... the vendor side reconciled" | OE3 reads recbd087 selProg SoR; OE4 subordinates "complete" ticket to make-ready SoR | recbd087 fldTurnStatus=selProg (only "not ready" signal) |
| L1 latching + L10 supersession (OPUS-SEL) | "Carlos has 4C down as wrapped... wants it released" | OE2 rejects LATER-created selReady recc8534; OE4 rejects "complete" reca424 | recc8534 created 2026-05-29 > recbd087 2026-05-22 |
| L31 explicit negative (GEMINI-SEL) | "if it is not, say so plainly and hold it... does not go to listing" | OE9 "NOT marketing-ready, do not mark Ready/do not release"; OE10 "do NOT advance to selReady" | fldTurnStatus enum {selSched,selProg,selReady} has NO hold value |
| L7 multi-write (density) | "record your QC determination... Open a ticket... post... email... Brooke needs to hear it" | OE10-15 = 6 writes across airtable/linear/slack/gmail | write surface confirmed in catalog |
| L9 future-event gotcha | "a re-inspection on the calendar for the middle of this month" | OE7 reconciles 7/15 event; OE3/9 flag past-due 6/30 | event 360b2149 start 2026-07-15 (verified only future 4C event) |

All five trace prompt -> OE -> atom. No HARDNESS_REGRESSION. The omitted $85 bills, if added, marginally strengthen L2/L11 (net-vs-gross), never weaken a lever.

---

## LENS 4 — Strict density projection (StarPM per-model: target 40+, floor 15) :: THIN (pre-accepted, not a block)
Honest competent-trajectory midpoints (per model), reconciling the plan (~45/43), S1 AUDIT minimizing sketch (~21), Council B (~30 Opus / ~26 Gemini), and the empirical StarPM anchor (33-38/run):
- **Opus ~30-38**, **Gemini ~26-34.** Both clear the 15 QC-spec fail floor with wide margin; both likely below the 40 design target.
Hardness_Plan carries a documented `## THIN density acceptance` for this task, so THIN is pre-accepted — reported honestly, **not** a REVISE driver. Enforcement is the S4 sub-40 real-run gate (rule 11 / mitigation #2), which remains live and material. The Lens-1 fix (surface 2 more bills in OE6) slightly raises density; do not collapse the 6-write set.

---

## LENS 5 — Adversarial veteran review
- **Second-reading flip to sign-off?** No. HOLD is uniquely determined; the omitted $85 bills only add reasons to hold. The four "done" decoys (recc8534, reca424, C004 chatter, invoice PrivateNote) are defeated by the SoR (selProg) + prompt's content-pin (mid-June move-out 6/15 selects only recbd087) + "I am not signing off until I run my own pass."
- **Entity drift:** none — carlos.mendez@/brooke.phillips@/jaime.salinas@/wesley.tran@ all consistent across contacts/slack/calendar.
- **Single-channel lock-in:** OE15 (Brooke) correctly channel-agnostic ("any channel that reaches Brooke") — avoids the Rubrics-eval Major. OE13 Slack C004 + OE14 Gmail-to-Carlos are each prompt-mandated verbatim ("post... in the make-ready channel"; "email... for Carlos"). No lock-in defect.
- **Tool/param correctness:** every StarPM trap correct — slack_send_message(channel_id, message) OE13; create_draft(to,subject,body) draft-only OE14/15; save_issue(...,team) OE11; save_comment(issueId,body) OE12; update_records_for_table(baseId,tableId,records) OE10; search uses `table`, list uses `tableId` OE1/4. Confirmed against catalog + both councils + validator.
- **em/en-dash:** 0 in file. **"at least N":** none. **OE meta-tags/arrows:** none.
- **Scope-creep — OE12 separate Linear comment (MINOR, carry to S3):** "Open a ticket spelling out what is still left" is satisfiable by OE11's issue **description** alone; OE12 re-enumerates the same items in a comment. Valid as additive density, NOT uniquely prompt-mandated. Council B flagged this. S3 must NOT build an Overly-Specific "a distinct comment artifact exists" rubric (F8 non-atomic-enum risk) — accept description OR comment.
- **OE5 date attribution (MINOR, cosmetic):** posts labeled "2026-05-23" = stored UTC created_at; local America/Chicago is 5/22 evening. Non-load-bearing; no fix required.

---

## LENS 7 — Anti-rationalization
Scanned my own reasoning. One line promoted: *"I considered treating the two $85 4C bills as out-of-scope under the narrow reading of 'the deep clean and the interior repaint', but..."* — per the decision rule (a matched completeness/rule-13 pattern is LOGGED regardless of how plausible the narrow reading is), this is the Lens-1 finding, not dismissed. The narrow-reading defence does not cite a hard exclusion; `991582431419`'s own line text names the current-turn scope, and OE6's prescribed `get_aged_payables` surfaces it. No other rationalizations found.

## LENS 8 — Regression anchors :: 62/62 PASS (recorded).

---

## FINDINGS (fix-in-place list)

**[MODERATE] Under-inclusive outstanding-items ground truth — OE6 / OE9 / OE10 / OE12 / OE13 / OE14 / final-response — PROPAGATE TO S1 (primary) with S2 fallback.**
Root: prompt asks "the vendor side reconciled too" in a universe holding FOUR unpaid Mesa Vista 4C vendor bills (387, 1340, and two at 85), while naming only "the deep clean and the interior repaint" as the carrying scopes. The OE reconciles two and presents the outstanding set as complete; `991582431419` ($85, current-turn intake/punch-list documentation, unpaid, due 5/31) is a real in-scope omission, and `546359391323` ($85, prior-turn closet-trim, unpaid) is a second bill a get_aged_payables agent will hit.
- **S1 fix (recommended, source-level):** bound the vendor scope in one clause so the ground truth is unambiguous — e.g. "reconcile the vendor bills behind those two scopes" (makes the OE's 2-bill reconciliation unambiguously complete and the two $85 labor/intake charges clearly out of the graded set; flagging extra unpaid bills stays never-wrong for a hold).
- **S2 fallback (if prompt is kept):** in OE6 surface all four unpaid 4C bills from `get_aged_payables`; include `991582431419` in the current-turn outstanding items (OE9/10/12/13/14/final-response), and if excluding `546359391323` as prior-turn, state that reason explicitly. Then S3 builds the vendor rubric with 387+1340 mandatory and the $85 rows accept-either-way.
- Why it matters: S3 rubrics + final-response completeness grading will bind to this set; a thorough agent that lists 3-4 bills must not diverge from an OE that lists 2.

**[MINOR — carry to S3] OE12 separate Linear comment** — not uniquely prompt-mandated; S3 accept issue-description OR comment, no distinct-artifact rubric.

**[MINOR — cosmetic] OE5 "2026-05-23"** — UTC vs local; non-load-bearing; optional to drop the date.

---

## All-lenses status
- Lens 1 strict QC scoring :: **REVISE** (OE Completeness < 5; OE Accuracy 5/5)
- Lens 2 answer-leakage :: PASS (no BLOCKER)
- Lens 3 hardness end-to-end :: PRESERVED (rubric leg deferred to S3)
- Lens 4 strict density :: THIN (pre-accepted; not a block; S4 sub-40 gate live)
- Lens 5 adversarial :: PASS with 2 MINOR carry-forwards
- Lens 6 :: RETIRED (not executed)
- Lens 7 anti-rationalization :: 1 line promoted to the Lens-1 finding
- Lens 8 regression anchors :: 62/62 PASS
- Lens 9 :: RETIRED (not executed)

## Verification statements
- [x] validate.py --phase oe re-cited; exit PASS (0/0/3).
- [x] Regression anchors executed this pass: 62/62.
- [x] Anti-rationalization scan done; the one hedge promoted to a finding.
- [x] Every OE-cited atom independently re-grounded from Universe_Split (not trusted from prior phases or the OE).
- [x] Rule-13 every-service completeness sweep run on QuickBooks/Airtable/Linear/Calendar for other open 4C items — surfaced the two omitted $85 bills.
- [x] Verdict REVISE recorded with per-issue trail + PROPAGATE-TO-S1 flag.

## Discrepancies surfaced
- Both S2 councils returned GO having verified only that the 3 named bills are grounded; neither swept QuickBooks for OTHER unpaid 4C payables (the omission-blind gap AGENTS.md rule 17 warns about). Independent re-verification confirms all NAMED atoms accurate but the outstanding-items SET incomplete.

---

# REVISE ROUND 1 — Re-verification against applied OE6 fix (2026-07-27)

## Revised VERDICT: **PASS (STRICT)**

The in-place OE6 fix resolves the completeness concern at the S2 locus. Two of my round-1 escalation premises do not survive quote-backed re-reading and are withdrawn; the underlying defect I flagged (rule-13 omission-blind sweep) was real and is now closed. All deterministic gates re-run this pass and green.

## What I withdraw (updated on source evidence, not defended)
1. **PROPAGATE-TO-S1 withdrawn.** The prompt names exactly two scopes verbatim: *"The two scopes that carried this turn were the deep clean and the interior repaint."* The vendor clause (*"the vendor side reconciled too. A scope that is billed but not finished, or finished with the bill still sitting unpaid, does not count as closed"*) is bound by that preceding sentence to those two scopes. The prompt is **bounded, not defective** — I cannot quote any defective prompt text given it names exactly two scopes, and an S2 scoping clause (which is what was added) resolves it. Tightening the prompt would be redundant. Locus is S2, as adjudicated.
2. **"991582431419 squarely in scope, current-turn" retracted.** Re-read its own line: scope = *"Unit condition inspection and punch list documentation"* (PrivateNote: *"Internal labor charge for Carlos Mendez's make-ready walk... turnover intake process"*). That is a THIRD scope (intake-walk labor); the colon-list "deep cleaning scope, full interior repaint, kitchen faucet leak..." enumerates the punch-list items the walk **documented**, not the bill's own scope. Under the prompt's two-scope frame it is correctly OUT of the graded set. My round-1 characterization conflated *the bill mentions the scopes* with *the bill is for the scopes*; it is not.
3. **The set-aside disposition is superior to my round-1 S2 fallback.** My fallback said "include 991582431419 in the outstanding items." That would push S3 toward an **Overly Specific (MODERATE, rule 27)** rubric requiring a non-prompt-mandated third-scope item, false-failing a correct agent that scopes to the two named scopes. The applied fix instead accounts for the bill (closing the omission gap) while keeping the graded set bounded to the two prompt-named scopes. Correct anti-over-specification posture.

## What held (the value of the round-1 catch)
The rule-13 omission-blind gap was real: original OE6 prescribed `get_aged_payables` (returns four 4C bills) yet reasoned over two with no stated disposition for the other two. A faithful agent hitting the prescribed sweep had no ground-truth guidance. That is now fixed.

## Revised OE6 re-verified from source (not trusted from the adjudication)
| Applied element | Revised OE6 text | Universe grounding | Verdict |
|---|---|---|---|
| (a) sweep returns FOUR bills due 5/31 | "A sweep of Mesa Vista 4C returns four bills all due 2026-05-31" | QB: 195089456477/696089964235/991582431419/546359391323 all Balance>0, DueDate 2026-05-31 | GROUNDED |
| (b) map two named carrying scopes | 195089456477 (deep clean 387.00) + 696089964235 (interior repaint 1340.00) | both entity_type=bill, exact balances | GROUNDED |
| (c) set aside 991582431419 = intake-walk labor "separate scope" | DocNumber 2026-481-566, line "Unit condition inspection and punch list documentation" | QB row line + PrivateNote "make-ready walk... turnover intake" | GROUNDED — a third scope, correctly excluded |
| (c) set aside 546359391323 = prior-turn closet-trim tied to recc8534 | DocNumber 2026-519, "Bedroom closet trim paint touch-up... following final QC walkthrough" | QB PrivateNote "Tony Reyes touch-up... Jaime QC... 4C close-out" == recc8534 fldNotes2 "bedroom closet trim flagged... resolved same day" | GROUNDED — prior selReady turn, correctly excluded |
| (d) 445653930748 = receivable, corroboration only | "receivable to customer Linda Castillo, not a vendor payable" | entity_type=invoice, CustomerRef Linda Castillo, no VendorRef | GROUNDED |
| (e) determination on the two named scopes | "turns on those two named scopes, not on the separate intake-inspection charge or the prior-turn touch-up" | OE9 outstanding items = 387 + 1340 + In-Progress + past-due 6/30 + pending 7/15 | CONSISTENT — no OE6/OE9 contradiction |

## Deterministic gates re-run this pass
- `validate.py --phase oe` = **PASS** (0 fails, 0 warns, 3 notes).
- `verify_universe_atoms.py --task ...` = 0 fails, 1 WARN (intentional 7/15 L9 event; unchanged).
- `test_regression_anchors.py` = **62/62 PASS**.
- Both new bill IDs grounded in Universe_Split: 991582431419 (bill, 2026-481-566, $85, due 5/31), 546359391323 (bill, 2026-519, $85, due 5/31).
- OE file em/en-dash scan: 0.

## Lens status (round 1 -> round 2)
- Lens 1 strict QC scoring :: REVISE -> **PASS**. OE Completeness now 5/5 (oracle accounts for all four bills its prescribed sweep returns; graded set correctly bounded to the two prompt-named scopes). OE Accuracy 5/5 (both set-aside bill IDs grounded; exclusion reasons verified).
- Lens 2 answer-leakage :: PASS (unchanged).
- Lens 3 hardness end-to-end :: PRESERVED (unchanged; set-aside strengthens L2/L11 net-vs-gross framing without over-specifying).
- Lens 4 density :: THIN pre-accepted (unchanged; OE6 slightly longer reconciliation marginally raises calls). S4 sub-40 gate remains live.
- Lens 5 adversarial :: PASS. No second-reading flip; the set-aside is the correct anti-over-specification move.
- Lens 7 anti-rationalization :: applied in reverse this round — did not cling to the round-1 finding out of consistency bias; the evidence resolves it.
- Lens 8 regression anchors :: 62/62 PASS.

## Remaining (MINOR, S3 handoffs — never S2 blockers)
- OE12 separate Linear comment: S3 accept issue-description OR comment; no distinct-artifact rubric (F8).
- OE5 "2026-05-23" UTC-vs-local: cosmetic, non-load-bearing.
- **S3 binding note (carried from the fix rationale):** bind vendor rubrics to the two carrying scopes ONLY (387 + 1340). Do NOT graded-require 991582431419 or 546359391323 — they are set aside by design; requiring them would be Overly Specific and false-fail a correct two-scope agent.

## Final verdict: **PASS (STRICT)** for --phase oe.
