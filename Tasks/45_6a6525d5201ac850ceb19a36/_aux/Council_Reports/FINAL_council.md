# FINAL COUNCIL — Task 45 (StarPM V4) · Mesa Vista 4C QC Hold

**Universe:** starpm (V4) · today 2026-07-01 America/Chicago · window 2026-05-01..2026-07-01
**Role:** cross-artifact holistic + answer-leakage + lever-preservation (read-only)
**Inputs read:** 5_Prompt / 6_Oracle_Events / 7_Rubrics (19 outcome) / Hardness_Plan / Fact_Ledger / Universe_Split (direct grep) / Validator_Reports (submission_gate, injection) / Evals_starpm 5 + 0 / v4_gates.py

## VERDICT: **PASS**

No BLOCKER. MAJOR = 1 (density THIN, already-accepted carry-forward under a mandatory S4 gate). Lens-6 Bucket-1 risk approx 5% (<=20%). The submission_gate FAIL is a **false positive with a clean resolution (Path B)**. All four PASS conditions met. Ship 5/6/7 unchanged; two carry-forwards below.

---

## THE SUBMISSION-GATE ADJUDICATION (the requested decision)

**Your 4 analysis points — independently verified, ALL CONFIRMED:**

1. **CONFIRMED.** Evals_starpm/5 Phase 2 (line ~146) defines F2 "Future-as-past" as *"Rubric expects analysis of events not yet happened per effective date"* — i.e. a rubric that treats a future event AS IF already happened (announces its outcome). Rubrics #8/#19 require the agent to STATE the 7/15 event *"has not yet occurred"* = future-as-**future** = the spec-correct opposite. This is NOT the F2 defect.
2. **CONFIRMED.** v4_gates.py L521-530: fail unless `prompt_wants_future_write AND rubric_is_cal_create AND today < d <= today+31d`. `prompt_wants_future_write`=True (prompt "re-inspection on the calendar"). `rubric_is_cal_create`=`_CAL_RUBRIC_RE.search(title+evid)` (L109) — its alternation `\b(...|schedule|...)\b` does NOT match the inflection **"scheduled"** (trailing "d" kills the boundary), and #8/#19 carry no "calendar"/"reminder"/"follow-up" token. So `rubric_is_cal_create`=False and the only carve-out (calendar-CREATE write-targets) does not reach "flag an existing confirmed future event as pending." Gate routes to FAIL. Over-flag confirmed.
3. **CONFIRMED (grep).** 2026-07-15 is a real `status=confirmed` gcalendar row — "Make-Ready QC Inspection - Mesa Vista 4C", event_id `360b2149b7d0c10fa65224c281cdb53f`, attendees carlos/brooke/wesley@starpm.com. It is the ONLY future 4C event (the other two 4C events, Sunshine deep-clean + interior-repaint, are 2026-05-21, past). Genuine atom, not phantom.
4. **CONFIRMED.** #8 (issue) and #19 (final response) are the sole end-to-end carriers of Hardness lever **L9** (universe-grounded future-event gotcha) and **Stump Hypothesis #4 [MED SYMMETRIC]**. Softening/removing the 7/15 reference regresses L9 -> FINAL BLOCKER under the lever-preservation rule. The fix must NOT weaken them.

**Interplay worth naming:** the same 7/15 event that F2 flags is exactly the event the F9 "unreconciled future event" net (v4_gates.py L689-715) REQUIRES an OE to reconcile — and OE7 does. F9 rewards asserting the event as still-pending; F2 penalizes it. F2's negation-blindness is the bug.

### RECOMMENDED PATH: **B (negation-aware gate fix), operator-implemented under the regression harness. Reject A. The two F2 fails do not block GO.**

The gate implements "future date after today = FAIL" with one carve-out whose guard (`rubric_is_cal_create`) means "this rubric asks the agent to CREATE a near-term calendar/reminder write-target." Rubrics #8/#19 are not create-targets; they READ a confirmed event and assert it is still pending, which per Evals_starpm/5 P2 is the spec-correct handling of a grounded future event and precisely what F9 rewards when an OE cites the date (OE7). A deterministic gate that FAILS a spec-compliant rubric is itself a defect (AGENTS.md rules 18-20: gate correctness over prose; detect the true defect shape mechanically). The correct, generalizing fix is to make the F2 net negation-aware: when a future date co-occurs with future-acknowledging language ("has not yet occurred", "still pending", "not yet done", "upcoming", "yet to occur"), classify future-as-future -> NOTE, not FAIL — aligning the code with its own spec line and closing this false-positive class for all future tasks. **Path A is rejected**: inserting "calendar" into #8/#19's evidence to trip `rubric_is_cal_create` is factually true and marginally improves self-containment, but it clears the gate only by matching a regex whose intent ("calendar-create write target") is FALSE for these rubrics and makes the gate emit a mislabeled NOTE ("prompt-sanctioned calendar/reminder write target") — papering over the defect by gaming a misnamed exemption, the exact anti-pattern rules 18-20 forbid. Because v4_gates.py is regression-frozen (62 anchors + 21 report hashes over 7 snapshot tasks) and FINAL is read-only, Path B is executed by the operator and gated on `check_regression.py` showing **0 of 21 frozen report hashes move** (expected: none of the snapshots carries a future-date-plus-negation rubric — that construction is this task's novel pattern; if any hash moves, that snapshot was itself being false-failed and should be re-frozen with the same rationale). Until the gate lands, the two F2 fails are recorded as a KNOWN FALSE POSITIVE with this rationale; #8/#19 ship unchanged to preserve L9.

---

## SIX LENSES (verdict = union)

### LENS 1 — Truthfulness / Answer-leakage: **PASS** (no phantom)
Every tight identifier greps to a real row (Universe_Split / Fact_Ledger):
- `recbd087a4abd605b` tblMakeReady selProg, fldMoveOut **2026-06-15**, fldTargetReady **2026-06-30**, "deep clean and interior repaint still tracking" (TRUTH). Decoy `recc8534b3fd13954` selReady 06-01/06-14 created 2026-05-29. Tickets `reca424761ae15355` (MR-4C-2026-08 "complete/market-ready") + `rec12969a3fdb0852` (MT-2026-084 turn opened). All 4 records confirmed.
- Bills: `195089456477` Sunshine deep clean TotalAmt/Balance **387.00**, Due 2026-05-31, DocNumber 2026-SC-4C; `696089964235` Permian interior repaint TotalAmt/Balance **1340.00**, Due 2026-05-31, DocNumber PD-2026-09. Correctly set-aside: `991582431419` ($85 intake walk), `546359391323` ($85 prior-turn touch-up); receivable `445653930748` ($1622, CustomerRef Linda Castillo = not a payable). Exact.
- gcalendar 7/15 confirmed event (above). C004 = #make-ready. baseId `appPropertyOps`, `tblMakeReady`, `tblMaintenanceTickets`, OPS board (230 OPS-* issues) all ground. Emails carlos/brooke/jaime/wesley@starpm.com ground.
- **Answer-leakage: clean.** Prompt frames "wrapped" as Carlos's belief (correct per L15/L16), gives the QC STANDARD ("billed-but-unpaid is not closed") as a rule not the answer, mentions the 7/15 event EXISTS but not that it defeats completion, and asks Jaime for sign-off-OR-kick-back. The discriminators (which row is truth, that bills are unpaid, that 7/15 is future) are never stated outright. No decoy-vs-truth discriminator leaked.

### LENS 2 — Rubric binding: **PASS** (1 MINOR)
- Atomic; exact values on ids/dates/amounts; self-contained (each carries the 6/15 move-out + 6/30 target + recbd087 pins). No method lock-in: **R14** "email OR equivalent Slack that reaches her" is goal-level (matches prompt "Brooke needs to hear it from us", no channel named) — GOOD; R5-R8 "issue (or a comment on it)" surface-flexible — GOOD.
- **[MINOR] R13** AND-bundles "deep-clean AND interior-repaint bills unpaid" in one email criterion (7_Rubrics.json lines ~74-79). Acceptable: per-bill amounts are atomically graded on the issue (R5/R6) and final response (R16/R17), and the prompt names both scopes jointly ("the deep clean and the interior repaint"). Optionally split; LOW risk.
- **Category balance:** 19 outcome / 0 process. QC-spec binary Rubric Category Balance (Outcome > Process) -> PASS.
- **Ordering (rule 23):** prompt has NO genuine agent-action A-before-B constraint. "post where it lands" = the disposition/content, not sequence (graded by R10). "before she markets it" sequences against Brooke's non-agent future action, satisfied by the notification existing (R14). "When you have the actual picture, record..." = investigate-before-write, naturally enforced. No Process rubric required; 0 process defensible.
- Evidence <-> OE aligned throughout (R1<->OE10, R4<->OE11, R5/R6<->OE6/OE12, R8<->OE7/OE12, R9/R10<->OE13, R11-R13<->OE14, R14<->OE15, R15-R19<->OE9/final).

### LENS 3 — Cross-artifact holism + density: **PASS** (density THIN = MAJOR carry-forward)
- **Forward + reverse map complete**, no orphan rubric, no unrouted prompt ask.
- **Lever map (every selected lever has prompt + OE + rubric):**
  - **L2 structured-DB skip (SYMMETRIC)** — prompt "whether both are genuinely closed and signed off or still open" -> OE1/OE3 (query tblMakeReady SoR, read selProg) -> R1/R2/R3.
  - **L1 latching + L10 supersession (OPUS-SEL)** — prompt "Carlos has 4C down as wrapped... Brooke is ready to market on his word" -> OE2 (do not act on decoy recc8534) + OE4 (ticket = claim) -> R1 evidence ("if written to the prior completed Ready turn or a maintenance ticket, this fails") + R2.
  - **L31 explicit negative (GEMINI-SEL)** — prompt "if it is not, say so plainly and hold it... does not go to listing until every outstanding scope is closed" -> OE9 (do NOT mark Ready / do NOT release) -> R2 + R15 ("should not be released for listing") + R10/R12/R14.
  - **L7 multi-write** — prompt "record... Open a ticket... post... email... Brooke needs to hear" -> OE10-15 -> R1/R4/R9/R11/R14.
  - **L9 future-event gotcha** — prompt "re-inspection on the calendar for the middle of this month... factors into whether I can call this one done" -> OE7 -> R8 + R19 (the gate-flagged rubrics; PRESERVED).
  -> No lever missing a piece. NO BLOCKER.
- **Entity map** consistent (Carlos / Brooke / Jaime / recbd087) across all 3 artifacts; no write-target drift to recc8534 or the tickets.
- **Density (per-model; StarPM target 40+, floor 15):** integrated trajectory both models = discovery sweep (airtable search/list 2 make-ready rows + read + 2 tickets + QB aged-payables + 4 get-bill + slack C004 + gcalendar list/get + contacts) approx 18-24; reconcile approx 4-6; 6 writes + post-write verify approx 8-11; param-trap retries approx 3-5. **Per-model projection: competent Opus approx 40-43 / Gemini approx 38-41; minimizing floor approx 21; empirical StarPM anchor 33-38.** The **6 DISTINCT writes are preserved** in OE10-15 and mirrored in rubrics (R1, R4, [R5-R8 comment], R9, R11, R14). THIN was accepted at S1 AUDIT with per-task justification; it clears the 15 fail-floor with wide margin. **MAJOR carry-forward, not a FINAL blocker** (decision already adjudicated) — with the MANDATORY S4 gate: real-run per-model avg < 40 -> PIPELINE REDO (rule 11 / Hardness mitigation 2).

### LENS 4 — Red-team: **PASS**
- **No <2-lever shortcut.** Passing the full set forces: read the selProg SoR row (L2) AND resist the "done" ticket/prior-turn/chatter (L1/L10) [R2/R3], reconcile QB balances not just "bill entered" (L2/L11) [R5/R6/R16/R17], hit the calendar (L9) [R8/R19], and execute 6 writes (L7). "Trust Carlos/the ticket" fails R2/R3/R5/R6/R8/R15.
- **Wrong-row hole closed.** R1 evidence explicitly fails a determination on recc8534 or a ticket; R2 pins the current turn recbd087 not advanced to Ready; the prompt disambiguates by content (6/15 mid-June move-out + 6/30 end-month target uniquely = recbd087; decoy is 6/01-6/14).
- **Depth present** — "done" is the first-surfaced signal; truth needs the second make-ready row + QB balances + the calendar (multi-hop).
- **Drift sweep (grep-verified):** em-dash 0/0/0; "at least" 0; cross-universe tokens (mortgage_los/stripe/keystonemortgage/oracle_gl/105000/brookfield/payload/teamId/`content=`) 0; tool-fn names in rubric titles 0; stray future dates in rubrics = only 2026-07-15 (plus today 2026-07-01 in justifications). CLEAN.

### LENS 5 — Narrative-State + Action-Prescription: **PASS** (2 MINOR)
- selProg vs selReady consistent; "wrapped" framed as Carlos's claim (correct). No invented enum: the hold is a fldNotes2 note / record comment, status stays selProg (OE10 explicit; R2 "remains In Progress" + R3 "states held" demand no nonexistent enum).
- **StarPM tool-param bindings correct:** OE13 slack_send_message(channel_id "C004", **message**); OE14 gmail create_draft(to[], subject, **body**) draft-only; OE11 save_issue(**team** "Operations"); OE12 save_comment(issueId, body); OE10 update_records_for_table(**baseId** "appPropertyOps", **tableId** "tblMakeReady", records[id]). Airtable is SoR over Linear (OE4 explicit).
- **[MINOR]** OE1 references search_records param as `table` (vs `tableId` in list_records_for_table) — 6_Oracle_Events.txt OE1; verify search_records signature (write path OE10 correct; non-blocking).
- **[MINOR]** OE11 literal `team "Operations"` — 6_Oracle_Events.txt OE11; confirm save_issue `team` accepts name "Operations" vs key OPS. R4 binds to the grounded **key OPS** (230 OPS-* issues), so the rubric is safe regardless of the OE string.

### LENS 6 — Verifier-Fails pre-upload (Evals_starpm/4 bucket-risk): **PASS** (approx 5%)
- Every rubric classifies **Bucket 3 (legit AF)** if failed on a real run — they punish the designed trap (wrong row / advance-to-Ready / trusting "bill entered" / ignoring 7/15).
- **Ambiguous-target check (R1/R2/R3 pin recbd087 while 2 make-ready rows share 4C):** the PROMPT disambiguates by content (6/15 move-out / 6/30 target), so a competent agent lands on recbd087 -> NOT F7.
- **Unreconciled future event:** OE7 reconciles 7/15 (F9-clean); R8/R19 assert it future = spec-correct (the gate F2 fail is a GATE defect, not a Bucket-1 rubric defect).
- HIGH Bucket-1 checklist: channel/method lock-in NONE (R14 flexible); evidence-stricter-than-title NONE; service metadata complete (channel C004 / recipient carlos@ / brooke@ all named); AND-bundle only R13 (LOW, mitigated); subjective terms NONE; write-verb-Process NONE; "approximately"/"or similar" on exact values NONE.
- Bucket-1 risk approx 1/19 (R13) approx 5% <= 20% -> PASS.

---

## FINDINGS (severity-tagged)

- **[FALSE-POSITIVE -> Path B]** submission_gate 2x F2 on #8/#19 -- v4_gates.py L521-530 / Evals_starpm/5 P2 (~L146) -- operator: make F2 negation-aware (NOTE when a future date co-occurs with "not yet occurred / still pending / upcoming / yet to occur"); gate on `check_regression.py` 0/21 hashes; ship #8/#19 unchanged. Reject Path A. Task GO not blocked.
- **[MAJOR / carry-forward]** Per-model density THIN (competent ~40/38; empirical 33-38) -- Hardness_Plan THIN acceptance -- MANDATORY S4 gate: real-run per-model avg < 40 -> PIPELINE REDO. Not a FINAL blocker (accepted; clears 15 floor).
- **[MINOR]** R13 AND-bundles deep-clean + interior-repaint in one email criterion -- 7_Rubrics.json R13 (~L74-79) -- optionally split; acceptable given atomic R5/R6/R16/R17 + joint prompt framing.
- **[MINOR]** OE1 `table` vs `tableId` on search_records -- 6_Oracle_Events.txt OE1 (L1) -- verify signature; write path OE10 correct.
- **[MINOR]** OE11 literal `team "Operations"` -- 6_Oracle_Events.txt OE11 (L21) -- confirm `team` accepts name vs key; R4 binds to grounded key OPS.
- **[OBSERVATION]** appPropertyOps + OPS board grounded; em-dash / at-least / cross-universe / tool-name-in-title sweeps clean; injection deterministic layer PASS.

---

## INJECTION COUNCIL one-line judgments
Note: inject.sql = untouched template header; 4_Changelog.json = `[]` -> this task solves on **base-universe data (no scenario injection)**. Judgments are against the materialized atoms I verified directly.
- **P4 (contradiction vs base universe): CLEAN.** No injected rows; the decoy-vs-truth tension (2 make-ready rows + 2 "done" tickets vs the selProg row) is intended base-data hardness, internally consistent and reconciled by OE2/OE4 — no fact/status/amount/timeline contradiction that would cause an unintended agent failure.
- **P5 (register/formality): CLEAN.** No injected messages; base atoms (QB DocNumbers 2026-SC-4C / PD-2026-09, vendor names, @starpm.com, Jaime's factual QC voice, calendar title) all match StarPM channel norms.
- **P8 (difficulty >= 3.5): SATISFIED.** Multi-lever base-data trap (structured-DB skip + latest-row supersession + billed-but-unpaid + confirmed future event + past-due target); one symmetric + two asymmetric stumps; Hardness 4/5. >= 3.5 met.
- (P6 chain-depth >5: SATISFIED — solvable path >= 18 calls across 6-7 services; load-bearing fact is 3+ hops deep.)

**FINAL: PASS — ship 5/6/7 unchanged; resolve the gate false-positive via Path B (operator, regression-gated); hold the mandatory S4 density gate (redo if per-model avg < 40).**


---

## OPERATOR ADDENDUM (2026-07-27) — Path B landed, blocker resolved

The council's recommended **Path B** was implemented and verified this session:
- `Validators/v4_gates.py`: added `_FUTURE_ACK_RE` + a negation-aware branch in the F2 date loop. A post-window future date co-occurring with future-acknowledging language ("not yet occurred", "still pending", "not yet done", "yet to occur", "upcoming") now emits a **COUNCIL NOTE** instead of a **FAIL**, aligning the code with Evals_starpm/5 P2 (~L146).
- **Regression clean:** `check_regression.py` PASS (anchors 62/62, reports 21/21 identical, verdicts 7/7 unchanged); `test_regression_anchors.py` 62/62. **0 of 21 frozen hashes moved** — the council's precondition is met; no snapshot carried the future-date+negation construction.
- **Re-run gates (Task 45):** `submission_gate` now **PASS** (0 fails / 4 notes — rubrics #8 and #19 are the two reclassified NOTEs, correctly describing future-as-future). `injection` PASS. `validate --phase all` PASS (prompt/oe/rubrics 0 fails).
- Path A rejected as recommended. Rubrics `5/6/7` shipped **UNCHANGED**. `v4_gates.py` change is additive and left in the working tree (not committed — no commit without explicit request).
- The NOTE's "COUNCIL confirm the date is a grounded universe atom" is satisfied by Lens 1 point 3 above (2026-07-15 grep-verified as a `status=confirmed` gcalendar row).

**All deterministic gates GREEN + Final Council VERDICT: PASS. Task 45 is cleared for platform upload (dual-model, 6 runs each). Hold the mandatory S4 per-model density gate: real-run avg < 40 -> PIPELINE REDO.**