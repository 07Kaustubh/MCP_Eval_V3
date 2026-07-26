# Cross-Source Verification — S3 (Rubrics) — Tasks/44_6a62ccba8cad60844b8364b9

Universe: `starpm` (V4) · Universe today: 2026-07-01 (America/Chicago) · Deliverable: `7_Rubrics.json`, 64 criteria (64 outcome / 0 process)

## Sources consulted

### Per-task data

- `_aux/Universe_Split/` :: ground-truth values each rubric tests, re-queried directly via Python rather than trusted from upstream reports. Records re-verified at this phase: `linear.linear_issues.json` (OPS-87 Todo, OPS-96 Todo, OPS-98 In Progress, OPS-97 Todo, OPS-99 In Progress, OPS-108 Backlog, OPS-35 In Progress, OPS-186 Todo created 2026-06-17, OPS-43 In Progress, OPS-56 In Progress, OPS-40 Done, OPS-91 Done, OPS-16/17/18, OPS-51/71/79, OPS-34, OPS-44, OPS-66, OPS-81); `linear.linear_workflow_states.json` (state_OPS_0 Backlog .. state_OPS_4 Done); `linear.linear_comments.json` (all 48 — OPS-87 carries zero comments, OPS-96 one dated 2026-05-30, OPS-98 two dated 2026-05-25, OPS-43 two dated 2026-05-14, OPS-56 two, OPS-97 one, OPS-108 two); `slack.slack_messages.json` (all 15 push ts values plus the full 2026-05-24..2026-06-01 window); `contacts.contacts.json` (7 named personas + job titles); `gcalendar.gcalendar_events.json` (Jaime's 10 events; zero on/after 2026-07-01; the 2026-06-02 check-in agenda; all 9 confirmed future events); `airtable.airtable_bases/tables/fields/records.json` (appPropertyOps, tblMaintenanceTickets, exactly 4 fields, no owner field, no status field, 50 rows).
- `_aux/Fact_Ledger.json` :: 206 emails / 403 amounts / 230 linear_issue ids indexed. Confirmed `jaime.salinas@starpm.com` and `brooke.phillips@starpm.com` present; every OPS id in a rubric title present in `ids.linear_issue`.
- `_aux/Verification_s2.md` :: prior-phase verification reviewed for OE-rubric consistency, including the three figure corrections appended to the Hardness Plan at S2 (37 thread parents not 15; 18 HVAC ticket rows not 20+; Lisa's ask 7 days after the wrap not 5). None of the three is load-bearing for any rubric.

### Eval spec

`Evals_starpm/3_Rubrics_Eval.md` read in full (all 1079 lines). Hard gates applied: Blank Fields, Forward Coverage, Atomicity Split-Completely, Act-vs-Defer (T9), Impossible Derivation (T10), Imported Constraint (T10), Write-as-Deliverable Preservation (T12), Prompt-vs-Rubric Action Alignment (Gap 6), Deliverable Destination Consistency, Final-Response Coverage (Gap 3), OE-to-Rubric Cross-Reference (Gap 4), Exclusion/Decoy Coverage, Under-Strict/Overly-Broad, Pre-Submission All-Fail Prediction. Phase 2.7 anti-rationalization rule applied to channel/method lock-in. Phase 2.11 relative-time alignment resolved from 2026-07-01.

### QC spec

`Docs_starpm/7_QC_Spec_Doc1.json` (Rubric dimension, 5 sub-dims + thresholds) and `Docs_starpm/8_QC_Spec_Doc2.md` (severity taxonomy, 9 appendix issue types) re-applied across all 64 criteria under the strictest interpretation. `Docs_starpm/13_QC_Companion.md` deliberately NOT used — it is Brookfield-contaminated and is not StarPM SSOT.

## Eval spec sub-dims (Evals_starpm/3_Rubrics_Eval.md) verified

- Overall Rubric Quality :: **5** — 0 Major, 0 Moderate, 0 Minor on 64 (0.00% on all three threshold lines). PASS(5) gate requires zero Major AND zero Moderate; satisfied.
- Rubric Category Balance :: **5** — 64 Outcome / 0 Process; `#Outcome > #Process` holds.
- Process Rubrics :: **5** — zero Process rubrics; three-condition test re-applied to all 64 to confirm none is a process check mislabeled as outcome.
- Agent Centric Phrasing :: **5** — 64/64 titles begin "The Agent" (possessive forms included, valid per the 06/09 note); zero tool names against the 276-name StarPM catalog; zero passive/artifact subjects.

## QC spec sub-dims (Docs_starpm/7_QC_Spec_Doc1.json — Rubric dimension) verified

All 5 Rubric sub-dims scored under the strictest interpretation by AUDIT and returned 5/5, backed by the mandatory per-atom evidence table (empty evidence cells force a score <= 3; the table was produced). The 9 appendix issue types from `Docs_starpm/8_QC_Spec_Doc2.md` were re-applied across all 64.

## Reference docs consulted

- `Reference/Rubric_Format.md` :: flat 4-field schema confirmed on all 64 (no `id`, no `annotations`, no extras); handling-flexibility patterns re-checked; threshold math including the pipeline's absolute-count gates (inactive above 30 rubrics, and would not fire).
- `Reference/Strict_Convention_Inventory.json` :: allowed phrasings and evidence-field shapes checked. `approximately` 0 uses (no calculated values in this task), `at least` 0 uses, `(or similar)` used only on agent-generated freetext (R29), `must be one of:` used for all five closed-set owner criteria.
- `Docs_starpm/2_Rubrics_V3_Guidelines.md`, `Docs_starpm/12_Always_Failing_Rubrics.md`, `QC_Tasks/V4_Tasks/QC_Passed/Task1..4/7_Rubrics.json` :: logged in `_aux/Reads_s3.md`.

## Verification statements

- [x] Validator (`validate.py --phase rubrics`) exit 0 — 0 fails, 0 warns, 5 notes. No Major issue tally above the 10% threshold (0%).
- [x] Council A (grounding) GO — every concrete value grounded; overclaim sweep clean; persona scope clean.
- [x] Council B (adversarial QC) GO — all 5 sub-dims 5/5; zero adversarial hits; density midpoint 48-49 PASS both models; levers 5/5.
- [x] Outcome > Process (64 > 0). Outcome 1.1 for every OE write action (OE 28-38). Outcome 2.1 for every prompt tell-me cue (P4, P5).
- [x] AUDIT verdict = `PASS (STRICT)` — `_aux/Council_Reports/AUDIT_rubrics.md`.
- [x] Regression-anchor suite executed: **62/62 PASS**, re-run after the final edits.
- [x] Answer-leakage sweep clean — 19 phrasings of the aggregate conclusion searched across the 4.4 MB corpus, 0 hits; no single tool call reveals the determination.

## Discrepancies surfaced

1. **Falsifiable access-notice clause (BLOCKING, fixed).** Three criteria asserted the second round of North cluster tenant access notices was never sent or never confirmed. Falsified by Slack `ts 1779832537.000013`, Carlos Mendez, C001, 2026-05-26: "48-hour notice letters are out to all affected tenants" — a message that appears in no Oracle Event and in no prior council report, and that a compliant agent paging the full 104-message channel history would surface. Verified independently before acting. All three (R13, R34, R45) rewritten to grade the record-grounded fact (two North units held up by tenant scheduling conflicts, follow-up still open on OPS-56), each carrying an explicit judge instruction not to require a never-sent assertion.
2. **Missing "what is actually finished" coverage (Major, fixed).** The original 56-criterion draft graded only open items and gaps; nothing graded the completion half of "Work out what is actually finished and what is not". Added R62 (South electrical panel inspections recorded finished, per OPS-186's description and title) and R63 (crew recorded East coil cleaning and A/C checks complete, per OPS-108's 2026-05-30 comment). Both attribute rather than assert, because their source records sit in non-completed states — AUDIT confirmed this is coherent with, not contradictory to, the criteria that punish prose-over-state reasoning.
3. **Condensate-drain criterion withdrawn (Major, fixed by deletion).** An interim positive-completion criterion graded the OPS-43 drain as cleared. Both councils independently found it collides with Elias's 2026-05-20 wrap flagging two condensate drains for follow-up, and with OE 28, which names "the second of the two condensate drains" as a boundary residual whose routing no criterion may require or penalise. Narrowing was attempted and rejected; the criterion was removed entirely and its function transferred to R62. Residue sweep: `condensate` 0 hits, `drain` 0 hits across all 64 x 3 fields.
4. **Council conflict on the East-owner pair, adjudicated by AUDIT.** Council A held that R24 and R52 were not scoring-independent; Council B held they were load-bearing and non-redundant. AUDIT adjudicated for Council A and identified the cause in this phase's own iteration log: R24's accept-set was widened to include the draft in round 2 *because* the draft criterion had been deleted, and round 3 restored R52 without re-narrowing R24, leaving `pass(R52) implies pass(R24)`. R24's accept-set narrowed back to the tracking layer, which also restores exact OE 33 conformance.
5. **Self-defeating fail clause (Moderate, fixed).** R62's evidence carried "FAIL only if the response asserts ... were never completed" — residue from the withdrawn drain criterion's one-directional guard — which made silence a pass and nullified the criterion. Rewritten to fail both on omission and on the wrong assertion. It was the only exclusive-fail clause in the set.
6. **OE 36 internal ambiguity (Non-Fail, NOT fixed here — `PROPAGATE TO S2`, wording-only).** OE 36 says both "any future slot resolved from the current date of 2026-07-01" and "is dated after 2026-07-01". Since universe today *is* 2026-07-01, the stricter branch would false-fail a same-day booking. R28 takes the permissive reading ("on or after July 1, 2026"). Recommended one-word OE fix: `is dated after 2026-07-01` -> `is dated on or after 2026-07-01`. Not applied — editing `6_Oracle_Events.txt` is outside S3's scope, and AUDIT confirms it gates nothing and did not change the `PASS (STRICT)` verdict. Carried to FINAL for the operator's decision.
7. **Thin single-sourcing on the West/South cluster attribution (Minor, accommodated).** Patricia Nguyen is never assigned to a named cluster anywhere in the universe; zero property-to-cluster mappings exist; OPS-16/17/18 place South under Elias Navarro. R62's South scoping therefore rests solely on OPS-186's title. Not a correctness defect (no falsifier exists), but R62's evidence now explicitly accepts a response that attributes the completion to the record without repeating the word "South".
8. **Process observation banked (AUDIT N7).** Discrepancies 4 and 5 are the same failure twice: an accommodation clause added in one round survived a later criterion replacement without being re-derived, and neither council re-read the prior round's rationale. Recorded for `Tasks/_meta/Learnings.md`.

## Verdict

**PASS.** `7_Rubrics.json` holds 64 criteria (64 outcome / 0 process) and clears every S3 exit gate: validator exit 0 with zero fails and zero warns; Council A (grounding) GO; Council B (adversarial QC) GO with all sub-dims 5/5, density midpoint 48-49 PASS on both models, and 5/5 Hardness levers traced; strict veteran AUDIT `PASS (STRICT)` with all five Rubric sub-dimensions at 5/5 after one REVISE round; regression anchors 62/62; answer-leakage sweep clean. Coverage matrix written with zero gaps and zero surplus. One non-failing wording note (discrepancy 6) is carried to FINAL rather than applied, because it touches `6_Oracle_Events.txt`, which is outside this phase's scope.
