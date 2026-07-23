# Verification — S2 Oracle Events (Task 40, StarPM V4)

## Sources consulted

### Per-task data
- `_aux/Universe_Split/slack.slack_messages.json` :: 3 injected messages (Tony authority parent ts 1782789240.000301; Carlos tenant-relay parent ts 1782824160.000302; Carlos escalation reply ts 1782863220.000303, thread_parent linked to Carlos's parent) programmatically verified present with exact ts + thread linkage.
- `_aux/Universe_Split/quickbooks.quickbooks_entities.json` :: bill id 195836274018 (DocNumber B2026-211) verified; Line[0].Description matches OE 10 word-for-word; TotalAmt 185.00; VendorRef `{name: Hill Country Plumbing, value: 201}`.
- `_aux/Universe_Split/linear.linear_issues.json` :: OPS-231 verified with team_id team_001 (team key OPS), state_id state_OPS_2 (In Progress), assignee user_d6c1beb9cf67594dae2f5de4529674f1 (Carlos), priority 2.
- `_aux/Universe_Split/airtable.airtable_records.json` :: rec92f4a1c8e17bd3 (MT-2026-1327) verified; fldPriority selMedium; fldDescription matches injection plan.
- `_aux/Universe_Split/airtable.airtable_fields.json` :: fldPriority singleSelect choices verified as selLow / selMedium / selHigh (matches OE 12 target selHigh).
- `_aux/Universe_Split/gmail.gmail_messages.json` :: msg e2f3a4b5c6d789ab in thread d1e2f3a4b5c6789a verified from ap@hillcountryplumbing.com; subject "Mesa Vista 7B water heater diagnostic summary and next steps".
- `_aux/Universe_Split/contacts.contacts.json` :: Tanya Mitchell (tanya.mitchell@gmail.com), Robert Finley (robert.finley@gmail.com), Carlos Mendez (carlos.mendez@starpm.com) all verified.
- `_aux/Universe_Split/hubspot.hubspot_objects.json` :: Robert Finley HubSpot contact_5e77eae71d865fe38318e10facf62de9 verified.
- `_aux/Universe_Split/slack.slack_users.json` :: Carlos U07E4512181, Tony UD4432C1F56 verified as authors of the 3 injected Slack messages.
- `_aux/Fact_Ledger.json` :: 4 grounded atoms passed `verify_universe_atoms.py --task Tasks/40_6a61a86a31b9c973b2021ba5` (exit 0, 0 fails, 0 warns).
- `_aux/Hardness_Plan.md` :: 6 levers L1/L2/L5/L7/L8/L9 traced end-to-end into 19-step OE.

### Eval spec
- `Evals_starpm/2_OE_Eval.md` :: OE Completeness + OE Accuracy sub-dims re-scored 5/5 by Council B + AUDIT.

### QC spec
- `Docs/7_QC_Spec_Doc1.json` :: OE dimensions (Completeness 3/4/5 NON-FAIL only; Accuracy 3/4/5 NON-FAIL only) — both landed at 5.
- `Reference/OE_Format.md` :: format-card compliance — 19 steps numbered sequentially, no em-dashes, real tool names, real parameter values, Conclude clause used for L5 critical reasoning (OE 4) and L2 load-bearing conclusion (OE 10).
- `Reference/OE_Convention_Inventory.json` :: opening-phrase patterns matched (Look up..., Search..., Read..., Locate..., Update..., Draft..., Create...), parameter traps respected.
- `Reference/Hardness_Playbook.md` :: 6-lever selection reconciled with StarPM adaptation table.
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: all 20 tool names cited in OE verified present in catalog; parameter names verified against catalog signatures for every write tool.

## Verification statements
- [x] Validator `validate.py --phase oe` PASS, exit 0, 0 fails, 1 WARN, 3 notes. The 1 WARN is a false-positive X3 service-mapping heuristic on the word "budget" inside a Slack message quote (Tony's "keeps us on Robert's June budget" quoted in OE 3) — no QuickBooks call is being described.
- [x] Every OE step tool name exists in `StarPM_Base_Universe/7_Server_Tools_Details.json` (20/20 verified).
- [x] Every OE parameter binding uses the exact StarPM-canonical name on the exact named tool (Slack `message` not payload; Gmail `body` not content; Linear `team` not teamId; Airtable camelCase; QB `get-bill` hyphen; `slack_send_message` NOT `slack_send_message_draft` — trap flagged explicitly in OE 15).
- [x] Gmail is draft-only in StarPM — 3 email OEs (16, 17, 18) all use `create_draft`, none claim a send.
- [x] StarPM has no closed-fiscal-period lifecycle in this scenario; lifecycle precondition check N/A per validator note.
- [x] Council A grounding + convention resolved to PASS after programmatic verification of 3 initial concerns (all false-alarms) documented in `_aux/Council_Reports/S2_A_grounding_resolution.md`.
- [x] Council B adversarial GO — OE Completeness 5/5, OE Accuracy 5/5, no adversarial divergences, all 6 hardness levers preserved end-to-end, no PROPAGATE TO S1 flags, all 8 write actions atomic and rubric-covering-ready, service mapping clean.
- [x] Council B-B3 density projection: THIN midpoint 38-40 (spread 32-44), accepted under Hardness_Plan.md documented THIN carry per AGENTS.md Rule 11.
- [x] Strict veteran AUDIT verdict = PASS (STRICT). All 19 per-OE sign-off rows PASS. All 6 lever end-to-end traces confirmed. No answer leakage. No PROPAGATE flags.
- [x] `verify_universe_atoms.py` PASS, exit 0, 0 fails, 0 warns, 4 atoms checked.

## Discrepancies surfaced
- Council A raised 3 apparent BLOCK-severity concerns (Slack ts coordination, QB Line[0].Description content verification, 4 tool names not in partial catalog dump). All 3 confirmed false-alarms via programmatic verification of the actual Universe_Split + full StarPM tool catalog. Resolution: `_aux/Council_Reports/S2_A_grounding_resolution.md`. Council A's grounding sub-agent lacked programmatic access to grep Universe_Split and could only see partial catalog excerpts; the OE itself is grounded correctly.
- Density THIN under strictest AUDIT re-projection (~28-30 midpoint). ACCEPTED under Hardness_Plan.md documented per-task THIN carry (root cause is prompt-level, not OE-level; S1 AUDIT already accepted the THIN carry). HARD FLAG carried forward to FINAL and platform-run monitoring: if real-run average across 6 runs lands below 40 tool calls, route to `PIPELINE REDO`.

## Verdict
PASS — S2 cleared validator, Council A (post-resolution), Council B, and AUDIT (STRICT). One hard flag on density to monitor at FINAL / platform review. Ready for S3.
