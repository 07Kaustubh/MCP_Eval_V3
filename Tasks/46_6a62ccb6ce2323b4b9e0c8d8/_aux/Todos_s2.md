# Todos — S2 (Oracle Events)

Task: `Tasks/46_6a62ccb6ce2323b4b9e0c8d8` · Universe: `starpm` (V4) · Universe today: 2026-07-01 America/Chicago

Status legend: `[ ]` pending · `[~]` in_progress · `[x]` completed

## Gate + setup

- [x] T01 Run `phase_ready.py --phase s2` and confirm upstream artifacts present
- [x] T02 Create `_aux/Todos_s2.md` (this file) — v11 E1 operator-discipline gate
- [x] T03 Create `_aux/Reads_s2.md` and log every spec doc / card / eval read — v11 E2 compliance gate

## Required reading (log each into Reads_s2.md)

- [x] T04 Read `Docs_starpm/9_Common_Error.md` Part 2 (Oracle Event errors) BEFORE drafting
- [x] T05 Read `Evals_starpm/2_Oracle_Events_Eval.md` (OE Completeness + OE Accuracy sub-dims)
- [x] T06 Read `Docs_starpm/7_QC_Spec_Doc1.json` Oracle Event dimension bands
- [x] T07 Read `Reference/OE_Format.md` format card
- [x] T08 Read `Reference/OE_Convention_Inventory.json` (voice / opening-phrase / param traps)
- [x] T09 Read `StarPM_Base_Universe/7_Server_Tools_Details.json` — exact tool names + parameter signatures
- [x] T10 Read V4 reference OEs `QC_Tasks/V4_Tasks/QC_Passed/Task1..Task4/6_Oracle_Events.txt` for voice/structure
- [x] T11 Re-read `_aux/Hardness_Plan.md` including all three CORRECTION blocks + F7/F8 carry-forward
- [x] T12 Read `_aux/Verification_s1.md` + `_aux/Council_Reports/AUDIT_prompt.md` for upstream cross-check

## Universe grounding (every OE step must cite a real row)

- [x] T13 Ground Airtable: make-ready rows + maintenance tickets for Harris (Sunset Ridge) and Finley clusters — exact `rec*` ids, field names, option ids
- [x] T14 Ground QuickBooks: Finley + Harris invoices, credit memos, customer balances — exact entity ids, DocNumbers, amounts, due dates
- [x] T15 Ground Calendar: all 4 owner-review events — per-calendar row ids, attendee response statuses, Lisa's row presence
- [x] T16 Ground Linear: OPS-10 / OPS-100 / OPS-39 / OPS-93 — issue ids, workflow state ids, comment ids, team + project ids
- [x] T17 Ground Slack: C006 owner-relations channel id, Lisa's May thread reply id + thread parent id
- [x] T18 Ground Contacts / HubSpot: Harris + Finley owner records, Brooke Phillips address for the Gmail draft
- [x] T19 Cross-check every atom against `_aux/Fact_Ledger.json`

## Draft

- [x] T20 Decompose `5_Prompt.txt` sentence by sentence into explicit + implicit asks; map each to discovery steps and write actions
- [x] T21 Confirm all 5 Hardness levers (L1, L2, L7, L10, L11) each have ≥1 covering OE step
- [x] T22 Confirm the contrast pair (Finley cash-blocked vs Harris operationally-blocked) is separable from the OE chain
- [x] T23 Draft `6_Oracle_Events.txt` — numbered `OE1:`, `OE2:` … sequential prose, concrete expected values
- [x] T24 Self-check: no em-dashes; every tool name real; every parameter name real for that exact tool
- [x] T25 Self-check F7: no bare Calendar base id pinned; every target uniquely resolvable
- [x] T26 Self-check F9: every completeness claim reconciled against the 9 post-today calendar events
- [x] T27 Add `S3 must decompose this into one criterion per content element (...)` directives on multi-element write OEs

## Gates

- [x] T28 Run `python3 Validators/validate.py --phase oe --task Tasks/46_6a62ccb6ce2323b4b9e0c8d8`; fix every FAIL; re-run until clean
- [x] T29 Run `python3 Validators/verify_universe_atoms.py` on the OE atoms
- [x] T30 Council A: 7 rounds, closing verdict GO pinned to sha a8522f8d.
- [x] T31 Council B: 7 rounds, closing verdict GO pinned to sha a8522f8d, Completeness 5/5 and Accuracy 5/5.
- [x] T32 Loop: 3 fix rounds against the councils (22 findings) then 3 REVISE rounds against AUDIT (11 findings). Validator re-run clean after every round.
- [x] T33 AUDIT: 7 rounds, closing verdict PASS (STRICT) pinned to sha a8522f8d.

## Exit

- [x] T34 Write `_aux/Verification_s2.md` (cross-source verification, v16 gate)
- [x] T35 Append coverage map + OE-to-rubric preview + AUDIT verdict to `_aux/Reasoning/OE_solvability.md`
- [x] T36 Update `_aux/Handoff_S2_S3.md` with the S3 carry-forward constraints
- [x] T37 STOP gate reached. All exit criteria met; every gate verdict pinned to the shipped sha.

## Round history

| Round | Gate | Verdict | Findings | Applied |
|---|---|---|---|---|
| 1 | Council A | BLOCK | 7 BLOCK, 6 MODERATE, 3 MINOR | yes |
| 1 | Council B | BLOCK | 6 MAJOR, 5 MODERATE, 6 MINOR | yes, minus 1 rejected on evidence |
| 2 | Council A | BLOCK | closed 7 of 7; new BLOCK-A, BLOCK-B, MOD-C, MOD-D, 3 MINOR | yes |
| 2 | Council B | BLOCK | closed 15 of 17; Completeness 5/5, Accuracy 4/5; N1 N2 N3 F10 F12 F11 | yes |
| 3 | AUDIT | REVISE | 6 MAJOR, 4 MODERATE, 10 replacements | yes |
| 4 | AUDIT | REVISE | 2 MAJOR, 4 MODERATE, all introduced by round-3 replacements | yes |
| 5 | AUDIT | REVISE | 1 MAJOR, 2 replacements | yes |

Council confirmation runs on the final file: 4 attempts, 4 infrastructure failures (2 connection/abort,
1 thirty-minute inactivity timeout, 1 permission stall).

Findings I rejected after re-deriving from the rows rather than applying:
- Council B r1 F9, that OE 8's date was wrong. `latest_reply` on the C006 thread parent is a dangling
  pointer matching zero messages; the reply's own `ts` and `created_at` both read 2026-05-28. Council B
  withdrew it itself in round 2 and measured the general case at 6 dangling pointers out of 251.
- Council A r1's "7 root threads" count for the C006 campaign messages. I measured 7 top-level and 26
  distinct roots, so the claim was ambiguous rather than wrong; the assertion was removed instead.
