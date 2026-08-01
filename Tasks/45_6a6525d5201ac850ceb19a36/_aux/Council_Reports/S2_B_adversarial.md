# Council B - Adversarial QC + Density + Hardness Preservation - S2 Oracle Events

**Task:** 45_6a6525d5201ac850ceb19a36 (StarPM V4) - Mesa Vista 4C make-ready QC hold
**Deliverable:** 6_Oracle_Events.txt (15 OEs + final-response spec)
**Persona:** Jaime Salinas (Quality Control Inspector, jaime.salinas@starpm.com)
**Universe today:** 2026-07-01 America/Chicago
**Reviewer mode:** read-only, five role lenses (Architect / Implementer / Red-team / Ground-truth / Integration), OE list read x5
**Verdict:** **GO**

---

## Grounding ledger (every OE atom verified against Universe_Split + tool catalog)

| Atom | OE ref | Universe_Split source | Result |
|---|---|---|---|
| recbd087a4abd605b = Mesa Vista 4C, selProg, moveOut 2026-06-15, targetReady 2026-06-30, created 2026-05-22 | OE1/2/3/10 | airtable_records L515 | EXACT. fldNotes2 matches OE3 verbatim ("still tracking... signed off") |
| recc8534b3fd13954 = Mesa Vista 4C, selReady, moveOut 2026-06-01, targetReady 2026-06-14, created 2026-05-29 (LATER) | OE1/2 | airtable_records L539 | EXACT. Supersession decoy; created 5/29 > 5/22 confirmed |
| reca424761ae15355 = MR-4C-2026-08 "all complete/market-ready/Brooke notified", created 2026-06-02 | OE4 | airtable_records L443 | EXACT. "complete" maintenance-ticket decoy |
| rec12969a3fdb0852 = MT-2026-084 "make-ready turn opened for unit 4C" | OE4 | airtable_records L55 | EXACT. Turn-opened ticket |
| Bill 195089456477 = Sunshine Cleaning, doc 2026-SC-4C, TotalAmt 387.00, Balance 387.00, DueDate 2026-05-31 | OE6 | quickbooks_entities L235 | EXACT. UNPAID |
| Bill 696089964235 = interior repaint, doc PD-2026-09, TotalAmt 1340.00, Balance 1340.00, DueDate 2026-05-31 | OE6 | quickbooks_entities L467 | EXACT. UNPAID |
| Invoice 445653930748 = owner pass-through, doc 2026-534, Balance 1622.00 | OE6 | quickbooks_entities L2087 | EXACT. UNPAID (PrivateNote "All work confirmed complete" = extra latching bait, correctly treated as unpaid money) |
| Calendar 7/15 QC inspection, event_id 360b2149b7d0c10fa65224c281cdb53f, confirmed, attendees carlos/brooke/wesley | OE7 | gcalendar_events L2211-2219 | EXACT. One logical event mirrored across 3 calendars. ONLY future 4C event |
| Slack C004 = #make-ready | OE5/13 | slack_channels L23 | EXACT |
| C004 5/23 posts ("Sunshine invoice is in QuickBooks...closed out" / "Pete's repaint is done, bill entered" / "4C is market-ready, Brooke") | OE5 | slack_messages L595/859/863 | EXACT (verbatim) |
| Carlos Mendez = Onsite Property Manager; Brooke Phillips = Apartment Property Supervisor; Jaime Salinas = QC Inspector | OE8/14/15 | contacts L27/23/99 | EXACT |
| Linear team "Operations" (key OPS, team_001, unique) | OE11 | linear_teams L3 | EXACT. Team desc even reinforces "Airtable Maintenance Tickets is SoR, Linear secondary" |

**4C census (F7):** exactly 4 airtable records match "Mesa Vista 4C" (2 make-ready + 2 tickets). No hidden third make-ready row. Uniqueness holds.

## Tool + parameter ledger (StarPM_Base_Universe/7_Server_Tools_Details.json)

| Tool (OE) | Exists? | Params verified | StarPM trap check |
|---|---|---|---|
| search_records | Yes L117 | baseId, **table**, query | OE1 correctly uses `table` (NOT tableId) for search |
| list_records_for_table | Yes L79 | baseId, **tableId** | OE1/4 correct - distinct from search |
| update_records_for_table | Yes L165 | baseId, tableId, records | OE10 correct |
| create_record_comment | Yes L239 | baseId, tableId, recordId, text | OE10 equivalent path valid |
| slack_search_public / slack_read_channel | Yes L4780/4918 | query / channel_id | OE5 correct |
| slack_send_message | Yes L5048 | channel_id, **message** | OE13 correct - `message`, NOT payload/text |
| get_aged_payables / get-bill | Yes L2898/3020 | - | OE6 both real (search_bills/read_invoice also exist) |
| list_events / get_event | Yes L601/643 | **fullText** / eventId | OE7 correct |
| contacts_search_contacts | Yes L545 | query | OE8 correct |
| list_users / search_crm_objects | Yes L1727/1131 | - | OE8 alternates real - NOT phantom |
| save_issue | Yes L1451 | title, description, **team**, state | OE11 correct - `team`, NOT teamId |
| save_comment | Yes L1789 | **issueId**, body | OE12 correct |
| create_draft | Yes L935 | to[], subject, **body** | OE14/15 correct - `body` draft-only, NO send tool exists |

**No em-dash / en-dash** in the OE file (grep clean). Hard block passes.

---

## Perspective findings

### [B1] QC sub-dim scoring (2_OE_Eval.md bands)

| Sub-dim | Score | Reason |
|---|---|---|
| **OE Completeness** | **5/5 (PASS)** | Full critical path: disambiguate 2 rows (OE1-2) -> read SoR selProg (OE3) -> cross-check "complete" ticket (OE4) -> Slack chatter (OE5) -> QB unpaid-bill reconciliation (OE6) -> future 7/15 calendar event (OE7) -> people lookup (OE8) -> QC determination (OE9) -> 6 writes (OE10-15) -> final response (L31). Dependency chain complete; no missing discovery or write step. |
| **OE Accuracy** | **5/5 (PASS)** | Every tool exists + correct service + correct params (incl. all StarPM traps); every id/amount/date/email/status grounded verbatim; zero count errors; fldNotes2 quoted exactly. No inaccuracy found across 15 OEs. |

Binary sub-dims implicated by the OE set (informational; scored at trajectory time): Tool-name discipline clean; write set maps to Cross-service (7 services). No OE-level binary FAIL.

### [B2] Adversarial alt-path - HOLD is uniquely determined
Four "done" decoys push a **sign-off / mark-Ready** end state: prior selReady row recc8534, "complete" ticket reca424, C004 5/23 "market-ready" chatter, and the owner-invoice PrivateNote "All work confirmed complete." A second reading that flips the write set to sign-off requires **misreading the target row** - i.e. acting on recc8534 (move-out 6/1, target 6/14) or trusting the ticket. The prompt pins the target by content ("moved out in the **middle of June**" = 6/15; "target-ready date at the **end of the month**" = 6/30), which selects **only** recbd087; and frames Jaime as explicitly NOT trusting the report ("I am not signing off... until I have run my own pass"). The SoR (make-ready record, reinforced by the Linear team description) is selProg + unpaid bills + un-run 7/15 re-inspection. **No valid alt-path to a different end state; the sign-off path is the intended stump, not a second valid reading.** No T9 act-vs-defer conflict: the correct path already IS the hold/defer, and the accessible C004 comms that say "done" are the bait the SoR defeats. **No B6 propagate on the write-set axis.**

### [B3] Tool-call density projection (per-model; StarPM target 40+, floor 15) - THIN, pre-accepted, NOT a block
Honest competent-trajectory midpoints:
- **Opus 4.8 ~30** (discovery sweep 13-16 + 6 writes + 2-4 re-read/verify; range ~24-34).
- **Gemini ~26** (leaner discovery 11-14 + 6 writes + 0-2 verify; range ~19-30).

The plan's 45/43 leans on a generous 14-24 base-discovery line a focused agent undercuts; the S1 AUDIT minimizing sketch was ~21/model; empirical StarPM real runs land 33-38 (agents wander/retry, so real > my clean midpoint). **All comfortably above the 15 QC-spec fail floor; both likely UNDER the 40 design target.** Reported honestly per instruction; **not blocked** (Hardness_Plan "THIN density acceptance" pre-accepts this task).
- **Live downstream risk:** real-run average may land ~30-37. The S4 hard gate (per-model avg < 40 -> PIPELINE REDO, AGENTS.md rule 11 / Hardness_Plan mitigation #2) is material - do not ship on a sub-40 real-run average. S2 preserved the maximal 6-write set, which is the only prompt-coherent floor-raiser available.

### [B4] Hardness preservation - all levers exercised, no regression
| Lever | Exercised by | Status |
|---|---|---|
| L2 structured-DB skip (SYMMETRIC) | OE3 reads recbd087 selProg SoR truth; OE4 subordinates the "complete" ticket to the make-ready SoR | PRESERVED |
| L1 latching + L10 supersession (OPUS-SEL) | OE2 rejects the LATER-created selReady decoy; OE4 rejects the "complete" ticket | PRESERVED |
| L31 explicit negative directive (GEMINI-SEL) | OE9 "NOT marketing-ready... do not mark Ready / do not release"; OE10 "do NOT advance to selReady"; OE13/14/15 carry the do-not-market negative | PRESERVED |
| L7 multi-write (density) | OE10-15 = 6 writes across airtable/linear/slack/gmail | PRESERVED |
| L9 future-event gotcha | OE7 reconciles the confirmed 7/15 QC event ("cannot be called done ahead of it"); OE3/9 flag the 6/30 past-due target | PRESERVED |

No HARDNESS_REGRESSION.

### [B6] Upstream propagation
No BLOCKING B6. Root cause of every finding is at S2/S3, not the prompt. The prompt's content-pin + sign-off-OR-kick-back ask correctly ground L31 and close F7. No S1 re-run required.

### [B8] OE Completeness semantic - forward + reverse coverage
**Forward (every prompt sentence -> >=1 OE):** "record your QC determination on that turn" -> OE10; "give me the call / sign-off-or-hold" -> OE9 + L31; "does not go to listing until every scope closed and signed off" -> OE9 hold rationale; "Open a ticket spelling out what is still left" -> OE11(+OE12); "post where it lands in the make-ready channel" -> OE13; "email together for Carlos with the specifics" -> OE14; "Brooke needs to hear it from us before she markets it" -> OE15. **Full.**
**Reverse (every OE -> a real prompt ask):** all map, with ONE soft flag (see Notes #1: OE12 separate Linear comment). No scope creep beyond that.

### [B9] OE Service mapping - all correct
make-ready/units + tickets -> airtable (SoR) [OE1-4,10]; bills/vendors -> quickbooks [OE6]; issue/comment -> linear [OE11-12]; calendar -> gcalendar [OE7]; email drafts -> gmail draft-only [OE14-15]; chat -> slack C004 [OE5,13]; people -> contacts/linear/hubspot [OE8]. **No OE_SERVICE_MISMATCH.**

### Write-set confirmation
6 DISTINCT writes: (1) OE10 Airtable QC determination on recbd087 (fldNotes2 hold OR record comment, status NOT advanced to selReady) - correctly avoids inventing a nonexistent "hold" enum; (2) OE11 Linear issue; (3) OE12 Linear comment; (4) OE13 Slack C004 post; (5) OE14 Gmail draft to Carlos; (6) OE15 Brooke notification. OE15 correctly channel-agnostic ("any channel that reaches Brooke") - avoids method lock-in (Rubrics-eval Major). Matches Hardness_Plan 5-6 mitigation.

---

## Issues (all Minor - none block; carry-forward to S3)

| # | Perspective | OE + location | Severity | Finding | Fix / carry-forward |
|---|---|---|---|---|---|
| 1 | B8 reverse-coverage | OE12 (L23) | Minor (S3 handoff) | "Open a ticket spelling out what is still left" is satisfiable by OE11's issue **description** alone; OE12's separate comment re-enumerates the same 4 items. Valid + intended as a density write, but not uniquely prompt-mandated. | S3: phrase Linear coverage to accept issue-description **OR** comment; do NOT bind a hard rubric to "a distinct comment artifact exists" (would be Overly Specific / risks F8 non-atomic enum). Keep as density, not as a graded distinct write. |
| 2 | B1/ground-truth | OE5 (L9) | Minor (cosmetic) | OE5 attributes the three C004 5/23 posts to "Carlos Mendez"; the messages are from slack user U07E4512181 (mapping not verified). | Harmless - the prompt itself frames Carlos as the "wrapped" source and OE5's load-bearing point ("bill entered != bill paid") is correct + grounded. Optionally soften to "the onsite-PM chatter" if S3 quotes attribution. |
| 3 | B3 density | whole set | Minor (already logged) | Per-model competent midpoint (~30/~26) below the 40 design target. | THIN pre-accepted; enforce the S4 sub-40 -> REDO gate. Not an S2 defect. |

---

## Verdict

**GO.** OE Completeness 5/5, OE Accuracy 5/5. Every atom grounded verbatim; every tool + param correct including all StarPM traps; all five hardness levers preserved; the HOLD outcome is uniquely determined by the prompt's content-pin and cannot be flipped by the four "done" decoys; 6 distinct writes correctly mapped and channel-appropriate. The only findings are three Minor carry-forwards to S3 (chiefly: do not let OE12 become an Overly-Specific "separate Linear comment" rubric). Density is honestly THIN per-model (~30 Opus / ~26 Gemini, empirical anchor 33-38) - reported, not blocked, per the pre-accepted THIN-density justification; the S4 sub-40 REDO gate remains live and material.

---

## REVISE round 1 re-verification (2026-07-27) - OE6 expansion only

**Scope of this pass:** OE1-5, OE7-15, and the final-response line are byte-unchanged from the GO above and are NOT re-litigated. Only OE6 changed (two-bill naming -> four-bill sweep + explicit two-scope mapping + set-aside of the two $85 bills + receivable clarification). Re-verified fresh against Universe_Split. Deterministic re-run confirmed: validate.py --phase oe PASS (0 fails / 0 warns / 3 notes); verify_universe_atoms 0 fails / 1 WARN (intentional L9 future 7/15 event).

**Verdict on the delta: GO.** OE Completeness 5/5 and OE Accuracy 5/5 hold; the expansion improves Completeness (closes the rule-13 omission-blind gap) with zero new inaccuracy and zero scope creep.

### New-atom grounding (the two set-aside bills)

| Atom | OE6 claim | Universe_Split | Result |
|---|---|---|---|
| Bill 991582431419 | doc 2026-481-566, "Unit condition inspection and punch list documentation", turnover intake-walk labor, a separate scope, $85, past due | quickbooks_entities L511: entity_type **bill**, Balance 85.00, DueDate 2026-05-31, DocNumber 2026-481-566, line "Unit condition inspection and punch list documentation - Mesa Vista Unit 4C...", PrivateNote "Internal labor charge for Carlos Mendez's make-ready walk of Mesa Vista 4C... turnover intake process" | EXACT. Set-aside reason accurate: intake/documentation labor, NOT the deep clean or repaint. |
| Bill 546359391323 | doc 2026-519, "Bedroom closet trim paint touch-up ... following final QC walkthrough", prior-turn close-out tied to selReady recc8534b3fd13954, $85, past due | quickbooks_entities L447: entity_type **bill**, Balance 85.00, DueDate 2026-05-31, DocNumber 2026-519, line "Bedroom closet trim paint touch-up, Mesa Vista Unit 4C - same-day repair following final QC walkthrough", PrivateNote "...Flagged during Jaime Salinas's QC inspection; completed same day... pair with corresponding AR invoice to Pete Donovan's owner account for 4C make-ready close-out" | EXACT on id/amount/doc/description. Close-out attribution grounded (see Obs A). |

Re-confirmed unchanged OE6 atoms: 195089456477 (Sunshine, 2026-SC-4C, $387 / Bal 387, due 5/31, deep clean) L235 EXACT; 696089964235 (Permian, PD-2026-09, $1340 / Bal 1340, due 5/31, interior repaint "walls, ceilings, and trim") L467 EXACT; invoice 445653930748 (Linda Castillo, 2026-534, Bal 1622) L2087 EXACT and correctly entity_type=**invoice** (receivable), not a payable.

### Four-bill sweep is exhaustive and correctly typed
Exactly FOUR entity_type=bill rows for Mesa Vista 4C carry DueDate 2026-05-31: 195089456477 ($387), 696089964235 ($1340), 991582431419 ($85), 546359391323 ($85). The $1622 owner pass-through 445653930748 is entity_type=invoice, so a faithful get_aged_payables returns the four bills and NOT the invoice - OE6's "four bills... the owner pass-through invoice... is a receivable... corroboration only" is exactly right. Exhaustiveness corroborated by the AUDIT sweep that drove this REVISE + verify_universe_atoms 0 fails.

### Set-aside reasoning is accurate and defeats two well-built decoys
- 991582431419's line item name-drops "deep cleaning scope, full interior repaint..." - a conflation / double-count bait. OE6 classifies by the actual charge (inspection + punch-list documentation labor, per line item + PrivateNote), not by the name-dropped scopes. Correct. OE6 also declines to cite the vendor (Alamo HVAC billing an inspection is itself decoupled in this universe); classifying by line item is the right discipline.
- 546359391323 is a post-QC "close-out" touch-up. The universe's OWN owner invoice 445653930748 models this as a SEPARATE line (Line 3, "Paint touch-up, bedroom closet trim... QC correction", $95) distinct from the repaint (Line 2). So OE6 treating the closet-trim touch-up as NOT the interior repaint matches the universe's own modeling.

### Scores + scope discipline
- **OE Completeness 5/5 (improved):** a faithful vendor-side reconciliation returns four 4C bills; the prior OE6 named only two, leaving the extra two unexplained (rule-13 omission-blind). Expanded OE6 now accounts for all four and scopes the determination to the two prompt-named carrying scopes. Gap closed; no discovery/write step lost.
- **OE Accuracy 5/5 (preserved):** every new id / amount / doc / description / vendor verbatim; set-aside reasons grounded; no new inaccuracy.
- **No scope creep / no reverse-coverage inflation:** the set-aside is EXCLUSIONARY, not a new agent deliverable. OE6's closing line ("the determination turns on those two named scopes, not on the separate intake-inspection charge or the prior-turn touch-up") is precisely the S3 binding instruction: bind write / response rubrics to the two carrying-scope bills (195089456477 $387 + 696089964235 $1340) ONLY; do NOT bind rubrics to the two $85 charges. This PREVENTS S3 scope creep rather than causing it. An agent that identifies the deep clean + repaint as billed-but-unpaid and holds still fully satisfies the determination whether or not it mentions the $85 items.
- **HOLD still uniquely determined:** the two named carrying scopes remain billed-but-unpaid (Bal 387 + 1340), current turn selProg with 6/30 target past due, 7/15 QC re-inspection future. The set-aside removes noise and cannot flip the call - even granting the owner invoice's "All work confirmed complete" bait, the prompt's own standard ("finished with the bill still sitting unpaid does not count as closed") holds both AP balances open -> HOLD. Strengthened, not flipped.
- **No em / en-dash introduced** (validate.py --phase oe PASS; quoted descriptions use U+002D spaced hyphen).

### Observations (non-blocking)
- **Obs A - close-out attribution is an inference, not a hard field.** 546359391323 carries no field linking it to recc8534b3fd13954; the linkage rests on (i) the bill's own "following final QC walkthrough" + owner-account "close-out" language and (ii) the current turn's QC being FUTURE (2026-07-15), so a post-QC touch-up cannot belong to the still-in-progress turn. The load-bearing conclusion (this $85 touch-up is neither the deep clean nor the repaint, so it does not enter the determination) holds from the line item alone, independent of the exact recc8534 attribution. S3 should NOT bind any rubric to the recc8534 linkage; it is OE-body rationale for the set-aside, not a graded fact.
- **Obs B - new S3 carry-forward (adds to Issues #1/#2 above).** Because OE6 now enumerates four bills, S3 must (a) bind the "unpaid scope" rubrics to the two carrying-scope bills by content ($387 deep clean, $1340 repaint), and (b) NOT create any criterion requiring the agent to enumerate, classify, or exclude the two $85 bills - such a criterion would be Overly Specific and could false-fail a correct HOLD. Keep the $85 set-aside as oracle rationale only.

**Delta verdict: GO.** No BLOCK. The overall S2 verdict is unchanged (GO); OE6's expansion is a strict improvement that closes the omission-blind gap while holding 5/5 on both OE sub-dims and tightening - not loosening - the S3 rubric-binding surface.
