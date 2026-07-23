# Verification — S3 Rubrics (Task 40, StarPM V4)

## Sources consulted

**Per-task data:**

- `_aux/Universe_Split/airtable.airtable_records.json` :: `rec92f4a1c8e17bd3` / `MT-2026-1327` / `fldPriority=selMedium` (pre-update) verified via `row_data` JSON parse.
- `_aux/Universe_Split/airtable.airtable_fields.json` :: `fldPriority` singleSelect option `selHigh` verified in choices list.
- `_aux/Universe_Split/linear.linear_issues.json` :: `OPS-231` verified — team_id `team_001` (OPS/Operations), state_id `state_OPS_2` (In Progress), assignee `user_d6c1beb9cf67594dae2f5de4529674f1` (Carlos), priority 2 (High).
- `_aux/Universe_Split/slack.slack_messages.json` :: 3 injected messages verified — Tony authority parent ts `1782789240.000301`, Carlos tenant-relay parent ts `1782824160.000302` (`reply_count=1`), Carlos evening reply ts `1782863220.000303` (`thread_parent_id=b2c3d4e5f6a789012345678901234abc` linking to Carlos parent) — all in `channel_id=C001`.
- `_aux/Universe_Split/quickbooks.quickbooks_entities.json` :: bill `id=195836274018` / `DocNumber=B2026-211` / `TotalAmt=185.00` / `VendorRef={name=Hill Country Plumbing, value=201}` / `Line[0].Description=Diagnostic visit, 12 yr Ruud RS75 water heater at Mesa Vista Unit 7B. ... Full unit replacement recommended, approx 1850 dollars for equal model swap. ...` verified verbatim.
- `_aux/Universe_Split/gmail.gmail_messages.json` :: message `id=e2f3a4b5c6d789ab` / `thread_id=d1e2f3a4b5c6789a` / `from=ap@hillcountryplumbing.com` / `to=[carlos.mendez@starpm.com]` / `subject=Mesa Vista 7B water heater diagnostic summary and next steps` verified; body base64-decoded and matches OE 5.
- `_aux/Fact_Ledger.json` :: emails (`ap@hillcountryplumbing.com`, `tanya.mitchell@gmail.com`, `robert.finley@gmail.com`, `carlos.mendez@starpm.com`), amounts (`310.00`, `1850.00`), date (`2026-07-02` Thursday), personas (Carlos Onsite PM, Tanya Tenant, Robert Property Owner) all verified.
- `_aux/Verification_s2.md` :: OE-phase verification PASS — reviewed for consistency; no OE-vs-rubric drift.

**Eval spec:** `Evals_starpm/3_Rubrics_Eval.md` :: all 4 rubric sub-dims scored below.

**QC spec:** `Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md` :: all 5 rubric-dimension sub-dims scored below.

## Eval spec sub-dims (Evals_starpm/3_Rubrics_Eval.md) verified

- **Overall Rubric Quality** :: 5/5 — 0 Major, 0 Moderate, 0 Minor. Percentage AND absolute-count gates clear at zero.
- **Rubric Category Balance** :: 5/5 — 16 outcome / 0 process = 100% outcome (matches V3 refs Task 11-14).
- **Process Rubrics** :: 5/5 — zero present; three-condition test correctly kept the count at zero.
- **Agent Centric Phrasing** :: 5/5 — all 16 titles start with "The Agent" or "The Agent's"; no passive voice; no subjective language.

Hash drift warning on `Evals_starpm/3_Rubrics_Eval.md` observed at phase-ready; per AGENTS.md "Pipeline Deviations from Eval Specs" table, pipeline reads current text; no interpretation-affecting changes noted.

## QC spec sub-dims (Docs/7_QC_Spec_Doc1.json — Rubric dimension) verified

- **Atomicity** :: 5/5 — pure existence checks + single-artifact narrative bundles per V3 pattern; multi-recipient send rule satisfied by per-recipient 1.1s on 3 Gmail drafts.
- **Self-Containment** :: 5/5 — every value embedded verbatim in title.
- **Completeness** :: 5/5 — 8 OE write actions × (1.1 + 1.2) = 16 rubrics; all covered end-to-end.
- **Flexibility** :: 5/5 — `(or similar phrasing)` on agent-generated free text; `approximately` on rounded amounts; exact-match on IDs / emails / dates / thread_ts / structured option values.
- **Accuracy** :: 5/5 — all values grounded to Universe_Split records; 0 fails / 0 warns per S3 Council A grounding sweep.

## Reference docs consulted

- `Reference/Rubric_Format.md` :: FLAT schema + qualifier rules + ML July 2026 severity swap + multi-recipient atomicity + severity absolute-count gates.
- `Reference/Strict_Convention_Inventory.json` :: allowed phrasings, verb inventory, evidence-field patterns.
- `Reference/Sessions/S3.md` :: full 12-step runbook.
- `Reference/Sessions/AUDIT.md` :: strict veteran audit protocol.
- `Reference/Council_Protocol.md` :: Council A + Council B protocols.
- `QC_Tasks/V3_Tasks/Task11..Task14/Rubrics.json` :: reference voice / structure (all outcome, zero process).

## Verification statements

- [x] Validator (`validate.py --phase rubrics`) exit 0; PASS with 9 non-blocking WARNs (Slack channel-name flexibility fixed; remaining WARNs are false-positive validator heuristics on rubric-OE consistency for amount atoms — amounts ARE in Fact_Ledger and QB Line description prose).
- [x] Council A (A1 grounding, A2 convention, A6 persona scope, A13 open-ended atomicity, S3 §6 O1 co-occurrence) clean — GO.
- [x] Council B (B1 sub-dims all 5/5, B2 no over-specification, B3 THIN inherited, B4 6/6 levers, B5 16/16 reverse-covered, B6 no atomicity/entity-swap, B7 cross-artifact consistency clean, B10 OE↔rubric map complete, B11 zero tell-me correctly = zero 2.1) — GO.
- [x] Outcome (16) > Process (0). ✓ Outcome 1.1 present for every OE 12-19 write action. Outcome 2.1 not present because prompt has zero explicit tell-me cues (content correctly embedded in writes).
- [x] AUDIT verdict = PASS (STRICT). All 16 rubrics per-row PASS. 6/6 hardness levers preserved with lock-and-key rubric coverage. 0 PROPAGATE flags. 0 REVISE flags. 0 REBUILD flags.

## Discrepancies surfaced

- **THIN density carry** inherited from S1/S2 AUDIT: strict re-projection ~38-40 midpoint (generous ~56). Root cause is prompt-level (scope of ask), NOT rubric-attributable — rubric set neither narrowed nor expanded scope beyond OE. HARD FLAG carried forward to FINAL and platform-run monitoring: if 6-run avg < 40 tool calls, route to `PIPELINE REDO`.
- **Two-Dianes universe ambiguity** (Diane Flores at Lonestar Maintenance Supply vs unnamed Diane at Hill Country AP). Resolved at rubrics 10/11 via exact-email routing (`ap@hillcountryplumbing.com`), which cannot resolve to Diane Flores. Non-blocking. FINAL should confirm no artifact accidentally names "Diane Flores" where Hill Country is meant.
- **Rubric 8 send-vs-draft functional distinction** ("using the send-message action rather than the draft action") — under strictest reading is closest to the tool-name-in-title line but is FUNCTIONAL, not a tool-identifier. Verified via strict comparison against StarPM tool identifiers `slack_send_message` / `slack_send_message_draft` (underscore-separated code identifiers vs natural-language descriptions). Council B v3 + AUDIT Lens 6 both confirmed non-defect.

## Verdict

**PASS** — S3 cleared validator, Council A (grounding), Council B (adversarial), and AUDIT (STRICT). Coverage matrix in place. One HARD FLAG on density carried forward to FINAL and platform-run monitoring. Ready for `PIPELINE FINAL`.
