# S2 Cross-Source Verification — Task 45 (StarPM V4)

Deliverable: `6_Oracle_Events.txt` (15 OEs). Universe: **starpm**. Universe today 2026-07-01 America/Chicago. Correct outcome = HOLD / kick-back on Mesa Vista 4C current turn recbd087a4abd605b (selProg).

## Sources consulted
- Per-task data :: `_aux/Universe_Split/` :: every OE record re-grounded — airtable recbd087a4abd605b (selProg, moveOut 2026-06-15, targetReady 2026-06-30), recc8534b3fd13954 (selReady prior-turn decoy), reca424761ae15355 (MR-4C-2026-08 "complete" ticket), rec12969a3fdb0852 (MT-2026-084); quickbooks bills 195089456477 ($387 deep clean), 696089964235 ($1340 repaint), 991582431419 ($85 intake-walk inspection — set aside), 546359391323 ($85 prior-turn closet-trim — set aside), invoice 445653930748 ($1622 receivable); gcalendar event 360b2149b7d0c10fa65224c281cdb53f (2026-07-15 QC re-inspection); slack C004 (#make-ready) + Carlos 5/23 chatter; contacts carlos.mendez/brooke.phillips/jaime.salinas@starpm.com; linear team Operations (OPS).
- Per-task data :: `_aux/Fact_Ledger.json` :: amounts (387.00, 1340.00, 1622.00), dates (2026-06-15/06-30/07-15), record ids, personas verified.
- Per-task data :: `_aux/Verification_s1.md` :: prior-phase verification reviewed; prompt content-pin (mid-June move-out / end-of-month target) carried into OE disambiguation.
- Reference :: `StarPM_Base_Universe/7_Server_Tools_Details.json` :: tool names + parameter signatures verified for every OE step (airtable search_records/list_records_for_table/update_records_for_table/create_record_comment, gcalendar list_events/get_event, gmail create_draft, linear save_issue/save_comment, quickbooks get_aged_payables/get-bill, slack_send_message/slack_read_channel/slack_search_public, contacts_search_contacts, hubspot search_crm_objects).
- Eval spec :: Evals_starpm OE eval :: OE Completeness + OE Accuracy scored 5/5 (detail in the Eval spec sub-dims section below).
- QC spec :: Docs_starpm/7_QC_Spec_Doc1.json (Oracle Event dimension) :: OE Completeness + OE Accuracy PASS (detail in the QC spec sub-dims section below).

## Eval spec sub-dims (Evals_starpm OE eval) verified
- OE Completeness :: **PASS (5/5)** — full critical path: disambiguate 2 make-ready rows -> read selProg SoR -> cross-check "complete" ticket -> Slack chatter -> QuickBooks four-bill sweep scoped to the two carrying scopes -> future 7/15 calendar event -> people lookup -> QC determination -> 6 writes -> final response. Rule-13 every-service sweep applied (OE6 now surfaces all four 4C bills and sets aside the two non-carrying-scope charges).
- OE Accuracy :: **PASS (5/5)** — every tool exists + correct service + correct params (all StarPM traps: slack `message`, gmail `body` draft-only, linear `team`/`issueId`, airtable camelCase, search `table` vs list `tableId`); every id/amount/date/email grounded verbatim; set-aside reasons grounded.

## QC spec sub-dims (Docs_starpm/7_QC_Spec_Doc1.json — Oracle Event dimension) verified
- OE Completeness :: **PASS** (3/4/5 NON-FAIL band; scored 5 under strict AUDIT).
- OE Accuracy :: **PASS** (3/4/5 NON-FAIL band; scored 5 under strict AUDIT).

## Verification statements
- [x] Validator (validate.py --phase oe) exit 0 — PASS (0 fails, 0 warns, 3 notes), re-run after the OE6 fix.
- [x] verify_universe_atoms.py — 0 fails, 1 WARN (date 2026-07-15 outside active window = the INTENTIONAL confirmed future QC re-inspection, lever L9, explicitly acknowledged by the prompt; benign).
- [x] Every OE step tool name exists in StarPM_Base_Universe/7_Server_Tools_Details.json.
- [x] Every OE parameter binding is on the EXACT named tool (StarPM traps checked).
- [x] Closed-period-post prerequisite check :: N/A for StarPM (no GL / no closed fiscal periods; validator note confirms).
- [x] Council A (grounding) GO — 28/28 base atoms + 2 new bill atoms grounded verbatim; receivable reclassification confirmed.
- [x] Council B (adversarial QC; B1/B2/B3/B4/B8/B9) GO — OE Completeness 5/5, OE Accuracy 5/5; HOLD uniquely determined; all 5 levers preserved; 6 distinct writes; correct service mapping; B3 density THIN per-model (pre-accepted per Hardness_Plan).
- [x] AUDIT verdict = PASS (STRICT) — after REVISE round 1 (OE6 vendor-sweep fix); AUDIT conceded its round-1 PROPAGATE-TO-S1 and "in-scope $85 bill" errors on quote-backed re-read.
- [x] Regression anchors (test_regression_anchors.py) = 62/62 PASS (AUDIT Lens 8).
- [x] No em-dash / en-dash anywhere (grep clean, confirmed by all three gates).

## Discrepancies surfaced
- AUDIT round-1 flagged an under-inclusive vendor reconciliation (rule-13 omission-blind: 4 unpaid 4C bills, not 2) and escalated PROPAGATE-TO-S1. Adjudicated (rule 19, quote-backed) as S2-locus, not S1: the prompt names exactly two scopes verbatim ("the deep clean and the interior repaint"); the two extra $85 bills are a third scope (intake-walk inspection labor, 991582431419) and a prior-turn close-out (546359391323, tied to selReady recc8534), neither a named carrying scope. Fixed in place at OE6 (surface all four, scope determination to the two named carrying scopes, set aside the two decoys with grounded reasons, label $1622 a receivable). Re-verified: AUDIT PASS (STRICT), Council A GO, Council B GO.
- Universe data quirk (non-blocking): bill 696089964235 VendorRef "Permian Make-Ready Crew" while its line/PrivateNote reference "Pete Donovan Painting"; OE6 cites the bill by id + DocNumber PD-2026-09 + amount 1340 (not by vendor name), so grounding is unaffected.

## Verdict
- PASS — 6_Oracle_Events.txt clears every S2 exit criterion: validator PASS (0 fails, 0 warns, 3 notes), verify_universe_atoms PASS (1 benign future-date WARN = the intentional 2026-07-15 QC re-inspection, lever L9), Council A GO (all atoms grounded verbatim), Council B GO (OE Completeness 5/5, OE Accuracy 5/5; HOLD uniquely determined; all 5 levers preserved; 6 distinct writes; B3 density THIN per-model, pre-accepted per Hardness_Plan), AUDIT PASS (STRICT) after REVISE round 1 (OE6 vendor-sweep fix), regression anchors 62/62. Ready for S3.

## Note
- Section headers normalized at S3 entry to the canonical check_verification.py shape (`Sources consulted` + `Verdict`), matching the passing Verification_s0/s1/hardness docs. S2 substance unchanged — this was the stale-runbook-template quirk flagged in Verification_s1.md discrepancy (c). No S2 re-run; every referenced S2 gate artifact (Validator_Reports/oe.md, Council_Reports/S2_A_grounding.md, S2_B_adversarial.md, AUDIT_oe.md) is present on disk.
