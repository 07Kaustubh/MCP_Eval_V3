# Verification — HARDNESS phase · `Tasks/44_6a62ccba8cad60844b8364b9`

v16 Cross-Source Verification Discipline. Universe: `starpm` (V4). Universe today: 2026-07-01 (America/Chicago).

## Sources consulted

### Per-task data

- `_aux/Universe_Split/linear.linear_issues.json` :: read every issue in the Preventive-Maintenance-Push surface (OPS-16, 17, 18, 27, 35, 40, 43, 44, 51, 56, 66, 71, 79, 80, 81, 87, 91, 96, 97, 98, 99, 108, 186, 199). Confirmed the `state_id` values that the levers rest on: OPS-87 `state_OPS_1`, OPS-96 `state_OPS_1`, OPS-98 `state_OPS_2`, OPS-97 `state_OPS_1`, OPS-108 `state_OPS_0`, OPS-44 `state_OPS_0`, OPS-91 `state_OPS_4`.
- `_aux/Universe_Split/linear.linear_workflow_states.json` :: state-id to name map verified directly rather than inferred (`state_OPS_0` Backlog, `_1` Todo, `_2` In Progress, `_3` In Review, `_4` Done). Cross-checked against the counts in `_aux/Universe_Index/key_facts.md` and `graph_report.md`, which agree (61 / 60 / 51 / 36 / 22).
- `_aux/Universe_Split/linear.linear_comments.json` :: all 48 comments enumerated; the 12 on push issues read in full. Confirmed Jaime's two OPS-98 comments, her OPS-96 comment, Elias's two OPS-43 comments, Elias's two OPS-56 comments, Carlos's OPS-97 comment.
- `_aux/Universe_Split/slack.slack_messages.json` :: full read of C001 (104 messages) with parent/reply structure resolved, plus a keyword sweep across all 8 channels. Every `ts` cited in the plan was read from this file, including the two thread replies under parent `1779308442.000001` and the reply under parent `1779567943.000011`.
- `_aux/Universe_Split/gcalendar.gcalendar_events.json` :: all 565 rows swept. 53 match the HVAC/QC/inspection keyword set; 4 unique Preventive-Maintenance-Push events read in full including the 2026-06-02 mid-initiative agenda. Future-event sweep run separately (see below).
- `_aux/Universe_Split/airtable.airtable_records.json` + `airtable.airtable_fields.json` :: 120 `tblMakeReady` and 50 `tblMaintenanceTickets` rows inspected; unit-count distribution computed; the 24 HVAC-keyword maintenance tickets read. Confirmed **zero** Airtable rows reference the cluster push, spot-checks or the Preventive Maintenance Push, so the Airtable HVAC surface is decoy noise and any Airtable write is unique by construction.
- `_aux/Universe_Split/gmail.gmail_messages.json` :: keyword sweep with base64 decoding across all 484 messages; 23 HVAC-keyword hits read in full. Confirmed **zero** emails reference the cluster push, and confirmed bodies are base64 with `snippet` the only plaintext field.
- `_aux/Universe_Split/quickbooks.quickbooks_entities.json` :: all 8 vendors listed; 134 HVAC-keyword entities inspected; the Lone Star Maintenance Supply and Alamo HVAC Services transaction sets read line by line.
- `_aux/Universe_Split/contacts.contacts.json` :: role titles confirmed for Jaime Salinas, Brooke Phillips, Elias Navarro, Carlos Mendez, Lisa Smith.
- `_aux/Universe_Split/Universe_complete_data.json` :: string-searched for eleven answer-leakage phrasings; all returned zero hits.
- `_aux/Fact_Ledger.json` :: atom counts checked for lever feasibility (230 Linear issue ids, 48 comment ids, 8 Slack channel ids, 61 personas, 192 dates). No amount atom is load-bearing for this task, which is consistent with the deliberate non-monetary answer shape.
- `_aux/Universe_Index/graph_report.md` :: density signals consulted — Jaime at 48 mentions (15th), co-actors Brooke 740 / Carlos 525 / Elias 40; Linear state distribution; Slack channel distribution C004 144 / C003 127 / C001 104.
- `_aux/Universe_Index/today_horizon.json` + `_aux/S0_Setup_Report.md` :: universe today and the 59 post-today records confirmed.
- `_aux/Feasible_Surface.json` :: enum vocabularies confirmed for the two Airtable tables (`fldTurnStatus` selSched/selProg/selReady, `fldPriority` selLow/selMedium/selHigh).

### Eval spec

- `Evals_starpm/5_Submission_Gate_Eval.md` families F7 AMBIGUOUS_TARGET, F8 NON_ATOMIC_ENUM, F9 UNRECONCILED_FUTURE_EVT :: applied at design time as pre-registered S1/S3 constraints rather than deferred to a downstream gate. F7 is the live risk on this task (three interchangeable Jaime QC issues) and is addressed by preferring writes that are unique by construction. F9 was swept and is clean on the push chain.
- Trajectory Tool Call Count sub-dim :: V4 design target is a 40+ average per model, with 15 the QC-spec fail floor. Projected midpoint for this task is **55.5** (range 44-67).
- Trajectory pass@1 sub-dim :: target 0 < pass@1 <= 40%. The selected lever mix is engineered against it, with the symmetric plus two-asymmetric recipe from Learnings item 11 chosen specifically so neither model family sweeps.
- `Evals_starpm/0_Injection_Quality_Eval.md` :: not engaged. No injection is proposed, `9_Universe_inject.sql` remains comment-header-only and `4_Changelog.json` remains `[]`, so the S0 injection PASS stands unchanged and does not need re-running.

### QC spec

- `Docs_starpm/1_Project_Instructions_Overall.md` :: the Mar 12 2025 amendment row confirms the gate is on the **average** tool call count being 40+, not on any single run, and requires the calls to span multiple services. The breadth table answers the second half.
- `Docs_starpm/11_Taxonomy.md` :: 40+ average tool calls, with the prescribed remedy for a shortfall being more data, more stakes, more asks. No shortfall here.
- `Docs_starpm/10_How_To_Load_and_Edit_Universe.md` :: pass@k between 0 and 0.4 alongside the 40+ aim.
- QC Trajectory T1 Tool Call Count :: projected midpoint 55.5, band **PASS** on the StarPM scheme, applied separately to Opus and to Gemini.
- QC Truthfulness :: pre-registered as a design constraint. The persona's belief is phrased as what she logged, which is literally what OPS-87 / OPS-96 / OPS-98 record, per the soft-verb rule in Learnings L24.
- QC Contrived / Unnatural Prompts :: the ask is a QC inspector confirming her own sign-off holds before an initiative closes, which is her documented job function, and the close-out deadline it hangs on is a real universe date that has passed.

### Reference docs

- `Reference/Hardness_Playbook.md` :: all 11 levers considered and scored (7 yes, 3 partial, 1 no). Selected: 1 Latching, 2 Structured-DB skip, 5 Thread-reply blindness, 8 Multi-link chain, 9 Authority dismissal. Lever 7 multi-write engineered in and scored in the Write-actions row rather than double-counted. Levers 3, 4, 6, 10 carried as corroboration and noise with no rubric dependency. Lever 11 dropped for lack of backing data rather than manufactured.
- `Tasks/_meta/Learnings.md` :: entries cited as lever rationale — **L2** and **L11** (structured-DB skip, Lever 2), **L9** and **L16** (authority dismissal / persona believes the wrong thing, Lever 9), **L13** and **L25** (first-framing and existing-artifact anchoring, Lever 1), **L8** and **L14** (three-service chain, correct-observation-wrong-conclusion, Lever 8), **L12** (thread-reply blindness, Lever 5), **L31** (negative-directive omission, the Gemini-selective differentiator), **L5** (writes are density not stumping), **L24** (soft verbs on the authority anchor), **L29** (no escape-valve at the load-bearing surface), **L6** and **L7** (no stated answer, no absence-as-answer), **L15** (implicit prompt only), plus StarPM items **3** (authoritative fact in the least-queried object type), **6** (tool reachability before crediting a lever), **11** (symmetric plus two asymmetric recipe), **13-16** (deterministic F7/F8/F9 discipline and the Calendar sweep), **17** (base64 email bodies), **19** (unreliable vendor attribution), and **20** (pre-register the lever re-attribution).
- `Reference/Sessions/HARDNESS.md` :: the six required plan sections, the StarPM-scoped density bands, the breadth gate thresholds.
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: every projected write path confirmed present in the catalog before being counted (Learnings item 6).

## Verification statements

- [x] At least 3 levers selected; 5 selected, and each cites a specific Learnings entry.
- [x] Density midpoint projection stated and banded on the correct scheme: 55.5, StarPM v4 PASS (>= 40), applied per model. The V3-family 50/40 bands were not applied.
- [x] Service breadth table populated: 7 services exercised, 6 at >= 5%, dominant service 34% against the 60% ceiling. Breadth PASS.
- [x] Every evidence pointer in the plan was read from `_aux/Universe_Split/` and cited by file plus record id or Slack `ts`. No record id, issue id or timestamp in the plan is inferred or invented.
- [x] Linear state-id to name mapping verified from `linear_workflow_states.json` directly, and cross-checked against two independent index files, rather than assumed from the id ordering.
- [x] Answer-leakage scan run: eleven phrasings of the aggregate conclusion searched across the whole-universe file, all zero hits. The conclusion is derivable only by aggregation.
- [x] Tool reachability confirmed for every projected read and write path against the StarPM catalog before counting it in the density projection.
- [x] Calendar swept in full, including the future-event sweep required by hard rule 13 and Learnings item 15: 9 unique confirmed events on or after 2026-07-01, none touching the push, the clusters or Jaime. F9 clean on the selected chain, with two adjacent events recorded as named watch items.
- [x] Single-target uniqueness pre-checked on every projected write. The F7 risk (three interchangeable Jaime QC issues) is identified and carried forward as a binding S1/S3 constraint rather than left for a downstream gate to catch.
- [x] Naive-agent simulation run with the intended answer out of view; documented in the plan.
- [x] REDO inputs checked: neither `_aux/REDO_reason.md` nor `_aux/Candidate_Originals/` exists, so this is a fresh CB build with no prior lever set to differ from.
- [x] Similarity pre-check performed against the five shipped StarPM tasks (39-43); the scenario, answer shape, primary store and persona all differ. Formal `calc_similarity.py` run is S1's gate, not this phase's.

## Discrepancies surfaced

1. **Corrected mid-analysis, recorded for honesty.** An early read of the QuickBooks surface concluded there was no Lone Star Maintenance Supply vendor. There is one, and there is also a near-miss twin, Lone Star Electric. Re-reading the transaction set then produced the more consequential finding: `VendorRef.name` is unreliable in this universe, since bills attributed to Alamo HVAC Services carry landscaping, legal-review and tenant-arrears lines. This is why QuickBooks is excluded from the lever set rather than used for the filter-restock trail.
2. **The cluster set is genuinely inconsistent across the universe.** Elias's HVAC scope issues (OPS-16, OPS-17, OPS-18) name three clusters — South, East, North. The Preventive Maintenance Push also carries a West cluster (OPS-35, OPS-91, OPS-186). This inconsistency is the substance of Lever 1, but it means no rubric may assert a specific total cluster count. The defensible claim is narrower and fully grounded: Jaime's own three QC issues never cover West.
3. **OPS-91 is an inverted pair.** Its `state` is Done while its description says "Moving this issue to In Progress". It cuts against the plan's general prose-versus-state direction, so it is explicitly excluded from rubric grounding in constraint 6 of the plan.
4. **Near-duplicate Linear issues in opposing states.** OPS-99 (In Progress) and OPS-108 (Backlog) share an identical title; OPS-51 (In Review) and OPS-71 (Backlog) share an identical title. Good latching noise, and a further reason no rubric may pin an issue id the prompt names only by topic.
5. **Two future events sit adjacent to the scenario without contradicting it.** The 2026-07-15 Mesa Vista 4C make-ready QC inspection and the 2026-07-23 Q3 make-ready planning and budget review. Neither belongs to the push, but both constrain what the deliverables may claim: nothing may assert Jaime's QC queue is otherwise clear, and nothing may assert the maintenance-budget question is settled.
6. **Runbook step 2 deviation, disclosed.** The runbook prescribes spawning a deep-reasoning sub-agent for the lever scan. This session carries an explicit standing instruction not to invoke the Agent tool unless the user asks for it, and the user did not. The scan, lever selection, density projection and stump hypothesis were therefore performed inline at full depth with direct grep and read access to `_aux/Universe_Split/`, which satisfies the substance of steps 2 through 6. Every input the runbook specifies passing to the sub-agent was read directly: the 11-lever catalog, the full Learnings file, all six `Universe_Index` files, the Fact Ledger, the persona brief, the persona name and the business function.

## Verdict

**PASS.** Hardness 5/5. Five independent levers, each grounded in this task's universe split and each citing a Learnings entry. Projected tool-call density midpoint 55.5 with a 44 low end, clearing the StarPM v4 design target of 40 per model on both ends of the range. Service breadth 6 at or above 5% with the dominant service at 34%. No answer leakage, no absence-as-answer dependency, F9 clean on the selected chain, and the F7 and F8 risks identified and bound as forward constraints rather than deferred. Proceed to S1.
