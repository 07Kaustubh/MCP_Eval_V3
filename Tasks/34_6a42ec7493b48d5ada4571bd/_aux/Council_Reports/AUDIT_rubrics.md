# AUDIT — S3 Rubrics (STRICT)

**Task:** `Tasks/34_6a42ec7493b48d5ada4571bd` · **Universe:** MoveOps (V2.1 framework)
**Inputs audited:** `7_Rubrics.json` (22 outcome / 0 process), `5_Prompt.txt`, `6_Oracle_Events.txt` (22 OEs), `_aux/Hardness_Plan.md` (L1+L2+L7+L8+L11, THIN 47-midpoint), `_aux/Fact_Ledger.json`.
**Lens set:** rubrics-phase, strictest reading. 5/5 only. Every "should" = "must".
**Universe spot-check:** ran direct queries against `3_UniverseDataForThisTask.json` (per memory `review_audit_must_deep_query_universe.md`) — Craig's Apr 11 email, Marcus's rider email, Pam escalation, Emilia Airtable row (with full pre-existing Special Requirements text), Linear retention issue, Slack C006 = "operations", and `BILL-KEYMOVE-2026-0417` $1,200 line all verified verbatim. Council A grounding GO + Council B B7 zero fabrications independently re-confirmed at the data layer.

---

## LENS 1 — Overall Rubric Quality (atomicity, self-containment, justification quality)

**Verdict: PASS (STRICT).** Every Outcome ground-truth atom is embedded in the title. Verbatim atoms (`email_email_1f1459bff84c`, `email_email_7168baed8438` [excluded], `recEmiliaCruzChicagoDenver`, `tblRelocations01`, `appMoveOpsOps001`, `C006`, `linear_issue_c8cdba4408f1`, `blessing.okafor@moveops.com`, `david.chen@moveops.com`, `catalina.dubois@moveops.com`, `pam.kowalski@northwindtech.com`, `$1,200`, `2026-04-27`) are unqualified — `(or similar)` qualifiers (#2, #3, #4, #6, #7, #8, #12, #13, #14, #15, #17, #19, #20, #21) attach to verb form or paraphrase scope, never to the verbatim atom itself. Justifications cite the specific prompt sentence + lever + universe surface that makes each rubric load-bearing. No bundled 2+ independent facts in any title except the calendar-event note in LENS 7 (borderline).

## LENS 2 — Rubric Category Balance

**Verdict: PASS (STRICT).** 22 outcome / 0 process. Process share 0% (cap 50%). Outcome outnumbers Process 22:0. Three-condition test for Process is vacuous — none added. Matches the V3 reference distribution (Task11..14 all zero-process) and the project default.

## LENS 3 — Hardness Lever Coverage

**Verdict: PASS (STRICT).** All 5 selected levers have ≥1 covering Outcome rubric whose value depends on traversing the lever:

| Lever | Covering rubrics | Lever-dependent atom |
|---|---|---|
| L1 latching ($1,200 + Marcus L9 frame) | #2, #6, #9, #13, #19 | `$1,200` named verbatim; #9 negative-rubric tests the latching stump (no fabricated customer-side $) |
| L2 structured-DB skip (Emilia Airtable row + Mosaic precedent shape) | #11, #12, #13, #14, #15 | `recEmiliaCruzChicagoDenver`/`tblRelocations01`/`appMoveOpsOps001` named verbatim; #12 enforces preserve-existing-content (the Mosaic-shaped two-sided expansion the agent must derive from querying the precedent) |
| L7 multi-write diversification | #1, #5, #11, #16, #18, #22 | 6 distinct writes / 5 services + reminder |
| L8 multi-link chain (Craig→Marcus→Pam→Linear→Catalina) | #1+#3 (Craig), #2/#6/#13/#19 (Marcus), #10 (Pam exclusion), #18-#21 (Linear retention), #5 (Catalina) | every chain node has a rubric touching it |
| L11 net-vs-gross (vendor gross ≠ customer net) | #7, #9, #14, #20 | client-side-open flag + no-fabricated-$ negative-rubric — directly anchors the stump |

## LENS 4 — Density

**Verdict: PASS (THIN_DENSITY explicitly accepted).** Hardness Plan midpoint = 47 (range 40-58), below the strict 50+ design target. Per-task carry-forward justification (Hardness_Plan.md §"THIN density acceptance") is substantive: (a) 6 writes is the realistic persona-scoped ceiling — pushing to 7+ corrupts L25; (b) Lever 8 upper bound (9) pushes midpoint to 51; (c) L9-anchored stumps naturally land in the 40s by design (the agents who short-circuit L1+L9 are *intended* to miss density); (d) explicit rescope path defined if real-platform midpoint < 45. Projecting from the rubric set alone (22 outcome rubrics × ~2 tool-call expectations each, plus discovery overhead from OE1-OE15) yields 44-58 — consistent. Under the strictest reading this is THIN, not INSUFFICIENT, and the per-task justification clears the AUDIT bar. **Flag: at-risk of underflow on platform — re-evaluate after first trajectory cycle as the plan instructs.**

## LENS 5 — Final-Response Coverage

**Verdict: PASS (STRICT).** Walked every prompt cue. The six asks are all write actions: reply to Craig (write), update record (write), email D/C (write), Slack post (write), Linear comment (write), Monday reminder (write). The "Remind me Monday" clause is explicitly an outbound calendar action (rubric #22), not a "tell me Monday" — no final-response ask is implied. No 2.1-style rubric is needed. Zero false-negatives.

## LENS 6 — Adversarial alt-path (over-specificity)

**Verdict: PASS (STRICT).** Per-rubric over-specificity probes:
- **#1** `reply_to_email` with `email_id`: prompt says "direct reply" — verb-locks the threaded reply. New-email path would violate prompt intent.
- **#5** single email to both D+C: prompt says "a tight read" (singular). Two separate emails would not satisfy "a read".
- **#11** update vs create: prompt says "Update Emilia's relocation record" — verb-locked. New record fails prompt intent.
- **#16** C006: prompt anchors on "ops team will see it"; hardness plan documents C002/C005 as the known wrong-channel stump traps. Tight, correct.
- **#18** comment on existing issue: prompt says "There is already a Linear item open … leave the operational facts on that item" — verb-locked.
- **#22** date 2026-04-27: prompt says "Monday"; only 2026-04-27 is the next Monday. Tight, correct.
- **#9, #10, #12** negative rubrics are appropriately scoped — #9 explicitly permits the vendor-side `$1,200` mention while forbidding a customer-side $, #10 names the exact forbidden address, #12 permits extending and forbids overwriting. No false-positive failure modes for compliant agents.

## LENS 7 — Atomicity decomposition

**Verdict: PASS (STRICT) — with one borderline note.** Most rubrics fail for exactly one reason. The 4 Airtable-update sub-checks (#11, #12, #13, #14, #15) are deliberately decomposed by field-content concern (record identity / preservation / vendor-side / client-side / lesson) rather than bundled — model textbook split. The 4 Linear-comment sub-checks (#18, #19, #20, #21) follow the same pattern. The 2 email-to-D/C content checks (#6, #7) are split from the 1 routing check (#5) and the 1 negative scope check (#9) and the 1 recipient-exclusion check (#10) — clean.

**Borderline:** Rubric #22 bundles (a) date = `2026-04-27` and (b) topic = Craig-formal-claim follow-up. These ARE independent failure modes (correct date / wrong topic; correct topic / wrong date). STRICTEST decomposition would split into #22a (date) and #22b (topic). However, both atoms describe a single deterministic write (one calendar event), and the V3 reference-task convention is to bundle date+topic on single-event calendar rubrics. Flagged as a Minor optional-split opportunity, not REVISE-grade. The current bundling is consistent with the V3/V2.1 conventional pattern.

## LENS 8 — Process-disguised-as-Outcome write actions

**Verdict: PASS (STRICT).** No rubric title names an execution trace. Every title describes the outcome state ("X email is sent to Y", "record is updated", "comment is added", "event is created", "post lands on channel"). Evidence sections name tool-call shapes (correct — the judge needs that to verify), never as the rubric's pass condition. Zero misclassifications.

## LENS 9 — Cross-artifact consistency

**Verdict: PASS (STRICT).** Spot-checked all verbatim atoms against `3_UniverseDataForThisTask.json`:

| Atom | Universe verified | Notes |
|---|---|---|
| `email_email_1f1459bff84c` | ✓ | Craig Nguyen 2026-04-11; body ends verbatim "Please let me know whether you want us to open a formal insurance claim on our side now or hold pending your client's review." — rubric #3's load-bearing direction is grounded |
| `email_email_99e10a978b48` | ✓ | Marcus Thorne 2026-04-17; subject names `$1,200`, body confirms |
| `email_email_7168baed8438` | ✓ | Pam Kowalski escalation — rubric #10 exclusion is grounded |
| `recEmiliaCruzChicagoDenver` / `tblRelocations01` | ✓ | Special Requirements field actual content confirms "Steinway", "specialty piano movers", "Three-vendor coordination", "27-day lease overlap" — rubric #12 preservation atom is grounded |
| `linear_issue_c8cdba4408f1` | ✓ | Title: "NorthWind retention response plan after April escalations" |
| `C006` | ✓ | name="operations", purpose="Apartment sourcing, flight booking, move coordination, and vendor management" |
| `BILL-KEYMOVE-2026-0417` | ✓ | TotalAmt = 1200 |
| `2026-04-27` | ✓ | Monday after Apr 24 (Friday docket close) |
| `pam.kowalski@northwindtech.com` | ✓ | 8 emails in universe — external NorthWind escalator, correctly forbidden from internal D/C handoff |

Zero fabrications. Every title atom traces prompt → OE → universe atom.

## LENS 10 — Service Metadata Completeness

**Verdict: PASS (STRICT).**
- Email rubrics: #5/#6/#7/#8/#9/#10 name `david.chen@moveops.com` + `catalina.dubois@moveops.com`; #1's recipient is implicit-by-`email_id` (the reply tool keys on email_id) which is the V3-correct shape for `reply_to_email`; #10 names `pam.kowalski@northwindtech.com` for the exclusion check.
- Slack rubrics: #16/#17 name `C006` and "#operations".
- Linear rubrics: #18/#19/#20/#21 name `linear_issue_c8cdba4408f1`.
- Airtable rubrics: #11/#12/#13/#14/#15 name `appMoveOpsOps001` + `tblRelocations01` + `recEmiliaCruzChicagoDenver`.
- Calendar rubric: #22 names `2026-04-27`.

Complete.

## LENS 11 — Wording alignment (Strict_Convention_Inventory + V2.1 deltas)

**Verdict: PASS (STRICT).** Verb shapes match V3 reference ("The Agent replies / sends / updates / posts / adds / creates"). No banned-in-title tokens — no tool names, no service names (`reply_to_email`, `airtable_update_records`, `linear_create_comment` etc. appear only in evidence sections, correctly). No em-dashes in any title (scanned all 22 — only ASCII hyphens for compound modifiers like `vendor-side`, `client-side`, `walkup-assessment`). No "at least N" — prompt has no minimum-count mandate. The MoveOps V2.1 parameter conventions are correctly reflected (`payload` for Slack, `content` for email, `issueId`+`body` for Linear, `base_id`+`table_id` for Airtable). Service-metadata wording is consistent with `Docs_moveops/2_Rubrics_V3_Guidelines.md`.

## LENS 12 — Operator-discipline gate

**Verdict: PASS (STRICT).** Both files present:
- `_aux/Todos_s3.md` (1377 bytes, dated Jun 30 17:34)
- `_aux/Reads_s3.md` (3024 bytes, dated Jun 30 17:47)

Discipline evidence is on the record.

---

## Summary table

| Lens | Verdict | Note |
|---|---|---|
| 1 Overall quality | PASS | atoms verbatim, qualifiers safe |
| 2 Category balance | PASS | 22/0 outcome/process |
| 3 Lever coverage | PASS | all 5 levers covered |
| 4 Density | PASS (THIN) | midpoint 47, per-task justification on record |
| 5 Final-response | PASS | all asks are writes |
| 6 Over-specificity | PASS | all locks defensible |
| 7 Atomicity | PASS | one borderline note on #22 (optional split) |
| 8 Process-as-Outcome | PASS | no execution traces |
| 9 Cross-artifact | PASS | all atoms verified in universe |
| 10 Service metadata | PASS | complete on every write |
| 11 Wording | PASS | V3/V2.1-aligned, no em-dashes, no banned tokens |
| 12 Operator discipline | PASS | Todos_s3.md + Reads_s3.md present |

## Optional surgical improvements (not blocking)

- **#22 split (LENS 7 borderline):** if the operator wants the absolute strictest atomic decomposition, split into:
  - #22a — calendar event/reminder dated `2026-04-27`
  - #22b — event title or description references Craig Nguyen follow-up on the KeyMove formal-claim direction
  This is a refinement, not a defect — current bundling matches V3 reference convention.

## Density flag (carry forward)

THIN_DENSITY (midpoint 47) carries forward into the trajectory phase per Hardness_Plan.md operator decision. If first-cycle real-platform tool-call average lands <45, the documented rescope path is: add `tblClientAccts01` NorthWind ARR-context read + a Friday EOD anchor event create. Do NOT add levers that pull persona into finance/customer-comm scope.

---

`VERDICT: PASS (STRICT)`
