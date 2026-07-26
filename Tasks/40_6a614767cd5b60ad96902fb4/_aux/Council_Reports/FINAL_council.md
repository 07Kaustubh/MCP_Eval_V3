# FINAL Council — Tasks/40_6a614767cd5b60ad96902fb4 (StarPM V4)

**Role:** Last integration gate before platform upload. Read all 3 deliverables together + Hardness_Plan + Fact_Ledger + Universe_Index + universe SSOT. Deterministic gates already green (`validate.py --phase all` = PASS; `--phase injection` = PASS; `--phase submission_gate` = PASS); this council adjudicates the notes those gates deferred, plus cross-artifact holism / answer-leakage / lever preservation.

**VERDICT: PASS** — 0 BLOCKER, 0 MAJOR, Lens-6 Bucket-1 risk 0%. Cleared for dual-model (Opus 4.8 + Gemini) verification.

---

## Tightened-gate semantic confirmations (requested)

- **(A) $2,132.00 grounded — CONFIRMED.** `quickbooks_entities` id `232176553533`, DocNumber `QR-2026-0441`, **Balance 2132.0 / TotalAmt 2132.0**; Line items 847.00 (carried May arrears) + 925.00 (June rent) + 210.00 (accumulated late fees) + 150.00 = 2132.00; Line descriptions read "Tanya Mitchell, Unit 14". The float `2132.0` == rubric #10's `$2,132.00` after Decimal-normalization. F4's fix is semantically correct: the figure is present, not absent. (Vendor label "Alamo HVAC Services" is a decoy; rubric #10 correctly grades on amount+tenant, not vendor label.)
- **(B) 2026-07-06/07 calendar reminder legit — CONFIRMED.** Prompt line 9 explicitly requests it ("set a reminder on my Google Calendar to come back to Unit 14 early next week"). 2026-07-01 is a Wednesday; "early next week" resolves to Monday **2026-07-06** or Tuesday **2026-07-07** (rubric #14 accepts both). Near-term (5-6 days out, << 2026-08-01 ceiling). This is a prompt-sanctioned near-term calendar create, not a future-universe-state expectation. F2's exemption holds.

---

## LENS 1 — Truthfulness + Answer-Leakage — PASS

- **Tight-id existence (universe SSOT grep, all >= 1):** recc83c05d889b354, reca8230a8fd9ff51, rec94e86a3007dd5e, rec769c9f03f0b85f, rec8005502043b755, rec91517a5acab558, recc0ecc885e9645e, rec922b9a2d1b9451, appPropertyOps, tblMakeReady, tblMaintenanceTickets, OPS-32/38/54, EVF-2026-014, DLQ-2026-0601, QR-2026-0441, 2026-EV-047, ticket_8faab56c663352cfb8d61c994b2bae88, contact_b30b8045f674569c9f15298ab9ce95d8, cfabf41121992633, 37a90450b4c2de2c, 9f2b3cd66c907597, proj-2e48594aab7, 232176553533, 146128608253, 283231782926. **No phantom id.**
- **Derived figures recomputable:** $2,132.00 = QR-2026-0441 Balance; $185.00 = 2026-EV-047 Balance (id 146128608253); $75 late fee = DLQ-2026-0601 fldDescription; $8,173.44 = invoice 7214 TotalAmt (Balance 0.00 via linked payment 952690463873, UnappliedAmt 0). All grounded.
- **Answer-leakage scan (bodies read at depth 1):**
  - String "2132" in prose bodies: **0** in airtable notes / gmail_threads / linear / hubspot. The slack + gmail_messages "hits" are false positives (substring of a hex message-id and of base64-encoded email bodies in an unrelated mass-email/standup thread — decoded to "Hi Alicia... 100-word cap... standup", zero relation to Tanya arrears).
  - QR-2026-0441 PrivateNote: "Consolidated rent ledger compiled by Teresa Wood... Reflects all outstanding charges and partial credits... Net balance forwarded to Patricia Nguyen and Brooke Phillips for filing." — does NOT state the figure in prose, does NOT state the synthesized conclusion.
  - Invoice 7214 PrivateNote: "...Mitchell account remains delinquent with no cure received." — a single-fact anchor (grounds OE9's books-vs-notes tell); does NOT state the arrears figure, the hold, the ESA, or the wrong-unit disambiguation.
  - recc83c05d889b354 fldNotes2: states only the possession-hold ("make-ready work on this unit cannot begin until the legal process concludes and possession is formally returned"). This is the source-of-record fact OE3/OE14 require the agent to discover — one fact, not the whole answer.
  - **No universe artifact body pre-states the full conclusion** (not-cleared + breached-plan + active-eviction + hold + $2,132 + ESA + Sunset-not-Rio-Bend). It must be synthesized across airtable + slack + quickbooks + hubspot + gmail. This is the "universe legitimately contains the atoms" case, not "a message states the answer."

## LENS 2 — Rubric binding — PASS
16 rubrics, all `outcome` (Outcome 16 / Process 0 — Outcome > Process). Each is atomic (one independent claim), self-contained (judge needs no external lookup), and cites a discoverable surface.
- Exact-value rubrics correctly mandatory-exact: #1 (record ids), #10 ($2,132.00 / QR-2026-0441), #12 (EVF-2026-014), #14 (07-06/07-07), #15 (OPS-32). No "approximately"/"(or similar)" on any id/date/amount/email/channel.
- Not-over-tight where the prompt is open: #2 evidence is careful ("FAIL only if advanced to selProg/selReady" — leaving Scheduled by set-or-no-op passes); #1 accepts either recc83c05d889b354 OR reca8230a8fd9ff51 (both the Sunset Ridge Unit 14 turn) and only FAILs on Rio Bend rec94e86a3007dd5e.
- Channel/recipient locks (#4 C004; #7 brooke.phillips@starpm.com) are **prompt-specified**, not agent-open-goal — legitimate, not bad channel-lock-in.
- Service metadata complete: #4 names the channel (C004); #7 names the recipient + draft-not-sent; #14 names the calendar target. No email-without-recipient / Slack-without-channel.

## LENS 3 — Cross-artifact holism — PASS
**Forward map (5 asks -> OE + rubric):** update record -> OE3/OE14 + R1/R2/R3; post #make-ready status -> OE15 + R4/R5/R6; draft email to Brooke -> OE16 + R7-R13; calendar reminder -> OE17 + R14; update ticket -> OE18 + R15/R16. Every ask has >=1 OE and >=1 rubric.
**Reverse map:** OEs 1-13 are discovery supporting the writes; OE19 consolidates write-content requirements; no OE or rubric introduces work beyond the 5 asks.
**Lever map (all 5 triggered end-to-end):**
- S1 possession-not-returned / negative-directive (L31): prompt "ready to re-rent" push -> OE3/OE14 hold -> R3/R6/R11/R16.
- S2 delinquency supersession / latching: prompt "nonpayment side is cleared" -> OE4/OE7/OE9 -> R5/R9/R10.
- S3 HubSpot ESA structured-DB skip (L10): prompt gives no reason to open HubSpot -> OE10/OE11 -> R13.
- S4 near-miss Unit 14 (L4): prompt "tied to Tanya Mitchell's unit specifically" -> OE2 -> R1/R8.
- S5 authority-relayed "owner signed off" (L9): prompt "owner signed off... filing is squared away" -> OE5(EVF)/OE6(Slack) -> R5/R12.
**Entity map:** Tanya Mitchell / Sunset Ridge Unit 14 / recc83c05d889b354+reca8230a8fd9ff51 / Brooke Phillips (brooke.phillips@starpm.com) / OPS-32 consistent across all 3 artifacts. Rio Bend rec94e86a3007dd5e is the EXCLUDE decoy everywhere; no drift.
**Implicit framing preserved:** prompt is written from Lisa Smith's mistaken belief; no rubric penalizes discovering the reversal (R2 explicitly does not penalize Scheduled), and none demands a forbidden step (prompt itself invites "confirm where it genuinely stands today before you touch anything").

## LENS 4 — Red-team adversarial — PASS
- **Shortcut path named:** trust the prompt's rosy frame + grab the already-rent-ready Rio Bend Unit 14 -> fails R1, R2, R3, R5, R6, R9, R10, R11, R12, R13. The lazy path is heavily penalized; >=2 levers are forced. Not exploitable.
- **Second-reading flip:** "get it ready to re-rent" could be read as "advance the turn," but the record note + R2's careful grading override it; final state (hold at Scheduled) is unambiguous.
- **Trap depth:** conclusion requires airtable + slack + quickbooks + hubspot + gmail; arrears require finding QR-2026-0441 past the "Alamo HVAC" vendor label; ESA requires opening HubSpot with no conversational cue. Not one-search-shallow.
- **Drift sweep (all 3 files):** em-dash 0, en-dash 0, "at least" none, foreign-universe tokens (oracle_gl/105000/AICPA/brookfieldcpas/mortgage_los/keystonemortgage/tblRelocations/@moveops) none, tool names in rubric titles none.

## LENS 5 — Narrative-State + Action-Prescription — PASS
- States consistent and shared by OE/rubric chain: make-ready selSched; EVF-2026-014 "Owner Approved - Ready to File" (fldCompletionDate 2026-06-30) but possession not yet returned; ESA approved in gmail 9f2b3cd66c907597 while HubSpot ticket_8faab... still OPEN.
- Prescribed next step is HOLD; the prompt's "get it moving" is the mistaken frame the agent reconciles against the record (L9). OE14 carries the explicit "Do NOT advance to selProg/selReady."
- **Param bindings on exact StarPM tools (all correct traps):** OE15 slack_send_message(channel_id "C004", **message**); OE16 create_draft(to[], subject, **body**) draft-only; OE17 create_event(**calendarId** "lisa.smith@starpm.com" email-style); OE18 save_comment(**issueId** "OPS-32", **body**); OE14 update_records_for_table(**baseId**, **tableId**, records). No param on the wrong tool. Every write (OE14-18) is preceded by its discovery reads (OE1-13); no write to a locked/again-state without prerequisite.
- Channel confirm: C004 = #make-ready, C003 = #general (rubric #4 / OE15 target correct).

## LENS 6 — Verifier-Fails pre-upload (Bucket-1 risk) — PASS (0%)
Simulated all 16 rubrics against Evals_starpm/4. None exhibits channel/method lock-in on an open-goal verb (channels/recipients are prompt-specified), evidence-stricter-than-criterion, AND-bundling, subjective-only terms, write-verb Process, "approximately"/"(or similar)" on exact values, cross-property mis-target, persona drift, or per-rubric value disagreeing with its OE step (recc83c05 / C004 / brooke email / $2,132+QR-2026-0441 / EVF-2026-014 / 07-06+07 / OPS-32 all match OEs 14-18). **Bucket-1 risk 0/16 = 0% <= 20%.**
Note: R3/R6/R11/R16 restate the hold across 4 distinct write surfaces (record note, Slack, email, ticket) — this is intentional per-surface atomic coverage (the L31 differentiator applied to each artifact), not redundant AND-bundling; each is an independent observable.

---

## HARD-RULE PASS/FAIL EVIDENCE
| # | Hard rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Derived figure / full conclusion never stated verbatim in a body the agent reads | **PASS** | No prose "$2,132"; QB/airtable notes carry only single-fact anchors; conclusion distributed across 5 services |
| 2 | Every tight id exists in universe / Fact_Ledger | **PASS** | All 27 probed ids grep >=1 in SSOT |
| 3 | Every hardness lever triggered end-to-end | **PASS** | S1-S5 each mapped prompt->OE->rubric (Lens 3) |
| 4 | Density (StarPM 40+ target; <15 BLOCKER) | **PASS** | integrated estimate ~44 (see below) |
| 5 | Outcome > Process | **PASS** | 16 outcome / 0 process |
| 6 | No tool name in rubric title | **PASS** | grep of title lines clean |
| 7 | No em-dashes | **PASS** | em-dash count 0 across all 3 files |
| 8 | Entity consistency (MAJOR) | **PASS** | Tanya/Sunset Ridge U14/Brooke/OPS-32 consistent; Rio Bend correctly excluded |
| 9 | Implicit framing preserved (MAJOR) | **PASS** | mistaken-belief prompt; no rubric penalizes the reversal |
| 10 | Injection difficulty >= 3.5 | **PASS** | rendered 4.3/5 (see below) |
| 11 | Bucket-1 risk <= 20% | **PASS** | 0% |

## Injection difficulty score: 4.3 / 5
9_Universe_inject.sql is **comment-only** (0 INSERT/UPDATE/DELETE/ALTER/CREATE); 4_Changelog.json empty. No first-class injected rows — the hard scenario is native to the base per-task universe (legitimate for this build). Score rendered on the native-scenario composite that the deferred Eval0 checks target: P4 fact/status/amount/timeline contradiction = STRONG (plan-active rec769c9f03f0b85f vs breach vs possession-hold; invoice-7214 zero-balance "paid" vs QR-2026-0441 $2,132 arrears vs "delinquent, no cure" note; timeline May-commit -> 06-23 breach -> 06-26 3-day notice -> 06-29 deadline -> 07-01 hold); P5 register match = consistent property-mgmt comms; P6 tool-chain depth = 14 discovery OEs / 8 services (>>5). Comfortably >= 3.5.

## Integrated density estimate: ~44 tool calls (per model)
Base discovery (list_bases + list_tables + make-ready search/read + eviction records + maintenance tickets) ~7; Slack eviction thread C003 + accommodation channel C002 ~4; QuickBooks (search_customers + search_invoices + read_invoice + search_bills + read 2-3 bills) ~6; HubSpot ESA ticket ~3; Gmail ESA threads (search + 2-3 gets) ~4; Linear (list + get OPS-32) ~2; contacts ~2; 5 writes (update_records + slack_send + create_draft + create_event + save_comment) = 5; re-read/verify buffer ~8. Total ~41-48. StarPM V4 target 40+ met (design target, not THIN); floor 15 not breached. Applies per model (Opus + Gemini).

## Dual-model sign-off note
Verification is dual-model: 8a_Verifier_Fails_Opus + 8b_Verifier_Fails_Gemini and Agent_Responses/{Opus,Gemini}/ expected downstream. The L31 negative-directive beat (R3/R6/R11/R16) is the engineered Gemini-stump differentiator (legitimate Bucket-3 asymmetry — Gemini names the blocker but frames positively; Opus issues the hold); the HubSpot ESA skip (R13) is the Opus-stump. Both models must clear the 40+ average independently.

## Observations (non-blocking)
- OBS-1: invoice 7214 PrivateNote states "delinquent" plainly at depth 1 — benign single-fact anchor (the intended books-vs-notes tell), not a conclusion leak.
- OBS-2: injection is comment-only; scenario native to base universe — legitimate.
- OBS-3: R3/R6/R11/R16 repeat the hold fact across 4 surfaces — intentional per-surface atomic coverage, not bundling.

## Optional future considerations (max 2)
1. None required. (OE9's 7214 "delinquent" wording is fully grounded — confirmed against the PrivateNote.)
2. If a future platform run shows Opus also issuing the hold reliably, monitor whether R3/R6/R11/R16 over-credit; no change now.

**FINAL VERDICT: PASS — cleared for platform upload / dual-model verification.**
