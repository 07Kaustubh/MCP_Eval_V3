# Rubric Coverage Matrix — Task 26_6a390e724c34487b95645dcc

**Date:** 2026-06-22
**Rubric set:** `7_Rubrics.json` (23 outcome / 0 process)
**Validator:** PASS (0 fails, 6 warns on `$4,820.30` Fact_Ledger format-mismatch false positives, 2 notes)
**Council A:** GO (initial 69 values grounded + 4 touched rubrics re-grounded post-split)
**Council B:** GO (initial 21 rubrics + 4 touched rubrics re-scored post-split)
**AUDIT verdict:** PASS (STRICT) after one REVISE round resolving R7/R8 atomicity bundles (`AUDIT_rubrics.md` REVISE → `AUDIT_rubrics_revise_round2.md` PASS STRICT)

## Rubric ID legend (atomic shorthand)

| Tag | UUID | Sub-type | One-liner |
|---|---|---|---|
| R1 | 7c8e5a12-4b3f-4d8a-9e5c-2f1a3b4d5e60 | 1.1 | Posts SALT JE in FP-2025-12 DR 530000 / CR 230000 $4,820.30 |
| R2 | 8d9f6b23-5c4a-4e9b-af6d-3a2b4c5d6e71 | 1.2 | JE binds to email_scen_068_..._0008 as late-post auth |
| R3 | 9e0a7c34-6d5b-4fac-bf7e-4b3c5d6e7f82 | 1.1 | Uploads memo (kind memo, restricted, IRS_TAX_7Y, related_resource_type journal_entry) |
| R4 | af1b8d45-7e6c-40bd-c08f-5c4d6e7f8093 | 1.2 | Memo content: $4,820.30 + GL trace (230000 vs 103000) |
| R5 | b02c9e56-8f7d-41ce-d190-6d5e7f80a1a4 | 1.2 | Memo content: William's email auth + JE id + entry_number |
| R6 | c13d0f67-9080-42df-e2a1-7e6f8091b2b5 | 1.1 | Sends email to Hannah + William CC (or replies on _0008) |
| R7a | d24e1078-a191-43e0-f3b2-8f70a1a2c3c6 | 1.2 | Email confirms $4,820.30 posted to FP-2025-12 against William's auth |
| R7b | 7e8d9c2b-1a4f-4e5d-9c3f-2a1b3c4d5e60 | 1.2 | Email references posted JE id + entry number |
| R8a | e35f2189-b2a2-44f1-04c3-9081b2b3d4d7 | 1.2 | Email references memo doc under restricted + IRS_TAX_7Y |
| R8b | 8f9e0d3c-2b5f-4f6e-0d4f-3b2c4d5e6f71 | 1.2 | Email confirms package can move to client signature + e-file unblocked |
| R9 | f46a328a-c3b3-45a2-15d4-a192c3c4e5e8 | 1.1 | Updates exc_652c0931bb2546 with reclass disposition under 4-eyes |
| R10 | a57b439b-d4c4-46a3-26e5-b2a3d4d5f6f9 | 1.1 | Deletes reminder_scen_012_orphan_exception_0000 |
| R11 | b68c54ac-e5d5-47a4-37f6-c3b4e5e607aa | 1.1 | Deletes reminder_scen_001_orphan_exception_0000 |
| R12 | c79d65bd-f6e6-48a5-4807-d4c5f6f718bb | 1.1 | Adds comment on polling-bug Linear ops tracker (create-if-missing) |
| R13 | d8ae76ce-07f7-49a6-590a-e5d607082acc | 1.2 | Linear comment: this-week occurrence + March chain + reminder disposal |
| R14 | e9bf87df-1808-4ab7-6a1b-f6e7180a3bdd | 1.1 | Posts status in C006 #tax-prep-and-filings |
| R15 | 0a008e90-2919-4bc8-7b2c-07f8290b4cee | 1.2 | Slack: SALT posted + memo restricted/IRS_TAX_7Y + package cleared |
| R16 | 1b119fa1-3a2a-4cd9-8c3d-1809a30c5dff | 1.2 | Slack: exc_652 reclass + reminder cleared + exc_151 dismissed + polling ticket |
| R17 | 2c220ab2-4b3b-4dea-9d4e-291ab41d600a | 2.1 | Identifies $4,820.30 supported by Northstar GL (230000 vs 103000) |
| R18 | 3d331bc3-5c4c-4efb-ae5f-3a2bc52e711b | 2.1 | Identifies FP-2025-12 closed + late-post auth required + William's email is auth |
| R19 | 4e442cd4-6d5d-4f0c-bf60-4b3cd63f822c | 2.1 | Identifies doc_8f821bbad10c4eb4 is stub + SALT JE not booked |
| R20 | 5f553de5-7e6e-40ad-c071-5c4de740933d | 2.1 | Identifies exc_652 disposition is reclass under 4-eyes (override dismissal) |
| R21 | 60664ef6-8f7f-41be-d182-6d5ef851a44e | 2.1 | Identifies exc_151 closed 2025-08-06 + James/Matthew authorized dismissal 2026-03-16 |

## Prompt sentence → OE step → Rubric mapping

| Prompt fragment | OE(s) | Rubric(s) |
|---|---|---|
| "Hannah just messaged that William cleared the Step 3 partner package…" / "I want to get this actually put to bed before the partner signature comes back, since the e-file path shouldn't be sitting behind accrual housekeeping" | OE1, OE2, OE3 | R17 (GL-derivation override of latching), R19 (L25 stub recognition) |
| "The federal return and the state returns both tie cleanly to the trial balance we locked in our December period for Northstar" | OE4 | R18 (closed-period recognition) |
| "William's reply is the authorization of record we needed for a closed-period booking" | OE2 | R2 (JE auth binding), R18 (auth identification) |
| "Before staging anything I want the shortfall traced back through our own records on the Northstar side so the number we book is one we can ourselves stand behind, not one we copied off the messaging trail" | OE5 | R17 (GL trace identification), R1 (correct JE amount as consequence), R4 (memo records the trace) |
| "Once you have a figure the records support, stage the closed-period entry on the Northstar December period and bind it back to William's reply as the authorization basis" | OE7 | R1 (post JE), R2 (auth binding) |
| "File a short support memo to the vault under the restricted classification with our long tax-return retention, tied to the entry so the audit trail is clean" | OE8 | R3 (upload artifact), R4 (memo body figure + GL trace), R5 (memo body auth + JE id + entry_number) |
| "Then ping Hannah and William so they know the booking is live and the package can move to the client for signature" | OE9 | R6 (send recipient/CC), R7a (posting confirmation), R7b (JE id/entry_number), R8a (memo reference + classification/retention), R8b (signature + e-file clearance) |
| "The May timing recon I sent Daniel for sign-off on June 1 went past its deadline without a response coming back" / "Jones and I had landed on dismissing under materiality" / "I want that actually pushed through and the exception closed out this morning so it stops sitting on me" | OE10, OE11, OE12 | R9 (BlackLine update with reclass disposition under 4-eyes — overrides dismissal), R10 (delete orphan reminder), R20 (identify override fact) |
| "The older one is the stale tickler that keeps firing on the Brookfield intercompany variance from last summer. That item closed in August" / "I had partner-level confirmation back in March that the reminder was fine to dismiss" / "Please clear the reminder so it stops pinging me" | OE13, OE14, OE15 | R11 (delete stale reminder), R21 (identify closure + March authorization chain) |
| "add a quick follow-up note on the open ops ticket for that polling bug so the running record reflects what is happening this week" | OE16 | R12 (Linear write), R13 (Linear comment content) |
| "Then drop a confirmation in the tax channel so Hannah and the team know the FY2025 close is moving and my exception backlog is clear" | OE17 | R14 (Slack post in C006), R15 (SALT cluster content), R16 (exception cleanup content) |

## Hardness lever → rubric coverage

| Lever | OE(s) | Rubric(s) that depend on traversal |
|---|---|---|
| **Lever 1 — Latching** (Hannah's "complete" framing + William's "authorization of record" + Tom's draft-returns slack mask that the SALT JE has not been booked) | OE1, OE2, OE3, OE6 | R17 (forces GL-grounded derivation overriding slack/email anchor), R19 (forces stub-vs-booked reconciliation) |
| **Lever 2 — Structured-DB skip** (must verify SALT against GL 230000 + 103000 rather than copy from slack) | OE5 | R17 (explicit GL-trace identification), R1 (correct DR/CR/period/amount as derivation consequence), R4 (memo records the trace facts) |
| **Lever 8 — Multi-link chain** (A=slack anchor → B=GL absence/recompute → C=closed-period JE staging w/ auth-id binding → D=memo with related_resource_id=posted JE id, and audit-trail email) | OE1 → OE5 → OE7 → OE8 → OE9 | R1+R2 (C-link), R3+R4+R5 (D-link memo), R6+R7a+R7b+R8a+R8b (D-link email), R17 (B-link forcing) |
| **Lever 9 — Universe-grounded gotcha** (exc_652 documented `proposed_resolution`=Reclassify contradicts persona-relayed dismissal; closed-period JE requires `late_post_authorization_id`) | OE4, OE10, OE11 | R9 (BlackLine update records reclass not dismiss), R20 (identifies the override), R2 (auth-id binding), R18 (identifies closed-period auth-required gate) |
| **Lever 10 — Reversal / supersession via L25 existing-output anchor** (doc_8f821bbad10c4eb4 "Signed/E-Filed" stub uploaded same morning reads as filing-complete) | OE6 | R19 (forces explicit recognition of stub-vs-booked), R1 (forces the staging that the L25 anchor would otherwise suppress), R4 (memo content tying the new JE to the trace) |

## Coverage completeness check

- **Every prompt ask has at least one rubric**: ✓ (no gaps)
- **Every rubric ties to a prompt ask or designed Lever 9/10 trap (allowed per project policy)**: ✓ (no surplus — R19, R20, R21 are designed Lever 10 / 9 / 4+5 traps documented in Hardness_Plan.md)
- **Every Hardness lever has ≥1 outcome rubric whose value depends on traversing it**: ✓
- **All 5 levers selected in Hardness_Plan.md covered**: ✓ (Lever 1, 2, 8, 9, 10)
- **Outcome > Process count**: 23 outcome / 0 process — matches V3 reference distribution (100% outcome)
- **Tool-call density projection (Council B + AUDIT realistic-strict)**: 47-52 midpoint, > 40 floor

## Sub-type distribution

| Sub-type | Count | Examples |
|---|---:|---|
| 1.1 (write actions) | 8 | R1, R3, R6, R9, R10, R11, R12, R14 |
| 1.2 (action content) | 10 | R2, R4, R5, R7a, R7b, R8a, R8b, R13, R15, R16 |
| 2.1 (key facts) | 5 | R17, R18, R19, R20, R21 |
| Process | 0 | — |
| **Total** | **23** | |

## Exit criteria — confirmed

- [x] `7_Rubrics.json` exists, all rubrics agent-centric, outcome > process, no tool names in titles
- [x] Validator returns PASS for the rubrics phase
- [x] Council A returns GO with every concrete value grounded (initial + post-split re-run)
- [x] Council B returns GO with every QC rubric sub-dim at 5 and zero adversarial hits (initial + post-split re-run)
- [x] Council B-B3 projected tool-call count >= 40 (midpoint 52, hyper-strict floor 43)
- [x] Council B-B4 all 5 Hardness levers covered by ≥1 Outcome rubric whose value depends on traversal
- [x] Strict veteran AUDIT returns `PASS (STRICT)` after 1 REVISE round (R7/R8 atomicity bundle splits applied)
- [x] Coverage matrix in place (this document)

## Runtime monitor (post-trajectory, per AUDIT NOTE)

- If 6-trajectory avg tool calls < 40 → density retroactively becomes BLOCKER → `PIPELINE REDO`.
- If 6-trajectory pass@1 > 40% → too easy → `PIPELINE REDO`.
