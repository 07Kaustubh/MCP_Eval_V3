# REVIEW triage — Task 30_6a3de5194c34125ef86fb36f

## Per-sub-dim QC scoresheet (Prompt + OE + Rubrics + Universe)

### Prompt sub-dims (against QC Spec Doc1 — Prompt section)

| # | Sub-dim | Score | One-line reason (per-task universe citation) |
|---|---|---:|---|
| P1 | Feasibility | 5 | All actions (look up JE, delete reminder, upload memo, post Slack, send email) map to existing tools and grounded atoms; trajectories prove feasibility. |
| P2 | Unique ground-truth end state | 4 | One JE, one reminder, one memo, one thread, one email — but the memo *content* requirements are partly inferential (Marina's "active coordinator role" wording), which the rubric exploits as a fail point. Borderline 4 → 5. |
| P3 | Persona / Business Function fit | 5 | Marina Soko = Compliance Officer ↔ Compliance & Internal Controls — clean match; emails confirm Marina is the actual case owner. |
| P4 | Coherence (not bolt-on) | 5 | All work strands flow from the closing of one AML case; nothing reads as artificially stapled. |
| P5 | Not contrived | 4 | The case is plausible but the prompt EXPLICITLY hands the agent the trigger amount ($57,077.69), late-April date, and the four named participants — the investigative discovery step is almost zero. Borderline 4. |
| P6 | Investigation not pre-solved | 3 | "$57,077.69" + "late April" + named CDD chain (Farah, Marina, Anita, Steven, Matthew, Steven) pre-resolve OE01 (find the JE) and OE02 (locate clearance trail) to near-trivial lookups. Agents who skip the email/Slack search and just use the prompt facts still pass. |
| P7 | Single-service tool use | 5 | Multi-service: oracle_gl, reminder, records_vault, slack, email — five services. |
| P8 | Truthfulness (no Major errors) | 5 | All cited atoms verified in `_aux/Universe_Split`: JE exists, reminder exists, thread_ts exists, all four named personas exist, no existing AML disposition memo for this JE (gap is real). |
| P9 | Word budget (≤ 500) | 5 | 213 words. |
| P10 | No tool names in prompt | 5 | No tool identifiers leaked. |
| P11 | No em-dashes / "at least N" | 5 | Validator clean. |
| P12 | Adequate hardness lever density | 3 | Hardness rests on ONE rubric (Marina coordinator-role). Other 23 rubrics are pass-by-default. Single-lever fragility. |

### OE sub-dims

| # | Sub-dim | Score | One-line reason |
|---|---|---:|---|
| O1 | Coverage of prompt requests | 5 | All 8 OEs map to prompt asks; nothing missing. |
| O2 | Atomicity (one action per OE) | 5 | Each OE = one action. |
| O3 | Tool/parameter accuracy | 5 | Tool names + parameter values verified against `8_Server_Tools_Details.json` and per-task universe (entity_id, period_id, channel_id, reminder_id, thread_ts all correct). |
| O4 | Convention — action-first verb opening | 3 | Validator WARN: 0/8 OE lines start with a recognized verb. Candidate uses `Action: <verb-phrase>` prefix; V3 references open action-first (`Search...`, `Send...`). Convention drift, not factual error. |
| O5 | No tool names in titles | n/a | OEs don't use rubric-style titles. |

### Rubric sub-dims

| # | Sub-dim | Score | One-line reason |
|---|---|---:|---|
| R1 | Valid JSON | **1 (FAIL)** | Validator FAIL: `Expecting ',' delimiter: line 1 column 2410`. Unescaped double quotes around `"Acme Cloud"`, `"Acme Cloud Solutions,"`, `"Acme Cloud Inc."` inside the `evidence` string of rubric #4. JSON does not parse. |
| R2 | Atomicity (one fail mode each) | 5 | 24 rubrics, each binary. |
| R3 | Self-containment | 5 | Each rubric is independently graded; no rubric depends on another's outcome. |
| R4 | Outcome > Process ratio | 5 | 24 outcome, 0 process — matches V3 reference precedent. |
| R5 | No tool names in titles | 5 | Titles use natural language. |
| R6 | Title doesn't mandate "at least N" without prompt basis | 5 | No "at least N" titles. (The `at least two of the following identifiers` lives in evidence, not title — acceptable.) |
| R7 | Evidence is grader-actionable | 5 | Every evidence block names the exact tool call + parameter/value to check. |
| R8 | Lever diversity | 3 | 5 of 6 failing runs trip the SAME rubric (#13). 23 rubrics are pass-by-default for nearly every agent. |
| R9 | Concentration — memo rubrics | 3 | 9 of 24 rubrics (#1, #3, #4, #5, #8, #9, #10, #11, #12, #13) check the SAME `records_vault_upload_document` call's title/content. Heavy concentration on one tool call's payload. |
| R10 | Groundedness in per-task universe | 5 | Every reminder_id, channel_id, thread_ts, email address, journal entry id verified. |

### Universe sub-dims

| # | Sub-dim | Score | One-line reason |
|---|---|---:|---|
| U1 | All cited atoms exist | 5 | JE-acme_cloud-FP-2026-04-0052, reminder_scen_041_audit_compliance_0000, thread_ts 1776969000.000000, all named contacts — all verified. |
| U2 | Reminder is genuinely overdue at universe today | 5 | Due 2026-05-02, today is 2026-06-12 — 41 days overdue. |
| U3 | Documentation gap is real | 5 | Vault contains FY2026 BO refresh and FY2026 AML Risk Assessment Memo, but NO disposition memo for the specific JE-FP-2026-04-0052 clearance. Gap genuine. |
| U4 | Clearance chain is documented | 5 | Email thread fully shows Marina → Anita → Steven; Farah's findings posted in Slack; Matthew confirmed engagement context in opening message. |

## Hardness numbers (from `Trajectory_Stats.json`)

- pass@1 = 0.167 (≤ 0.40 bar) → OK
- avg tool calls = 43.2 (≥ 40 floor) → OK but THIN
- Script verdict: OK
- Lever-coverage observation: single-rubric monopoly on failures = fragile

## Triage trigger evaluation

| Trigger row | Fires? | Detail |
|---|---|---|
| ANY QC sub-dim scores 1-2 (FAIL band) | **YES — R1 (Valid JSON) = 1** | `7_Rubrics.json` is structurally invalid (unescaped quotes inside string at char 2409). |
| Hardness fails (pass@1 > 0.40 OR density < 40 OR projected lever miss OR answer leakage) | NO | Density 43.2, pass@1 0.167. |
| Otherwise — every sub-dim 3-5, no hardness failure | n/a | Pre-empted by row 1. |

## Verdict

**SALVAGEABLE — with one Major and several Moderate findings to raise sub-scores to 5/5 before ship.**

Strict reading of the decision table: R1 = 1 (FAIL band) fires the REBUILD trigger. **BUT** the JSON-invalidity defect is mechanically fixable in-place (escape the inner quotes inside one evidence string) — it does not touch the scenario design, the rubric semantics, or the hardness lever. Rebuilding the task from scratch over a string-escape bug would be disproportionate. Treat R1 = 1 as "FAIL-band defect that is structurally trivial to repair", apply the fix via `changes.md`, and re-validate. If the operator preferred strict rule-following, the alternative is REDO — but the per-task universe still supports the scenario as written, so REDO would produce a near-identical task.

Per-phase fixes are listed in `changes.md`. After Applied, re-score targets:

- Prompt: raise P5/P6 from 4/3 → 5/5 by pivoting "$57,077.69" and "late April" to less specific language so the agent has to discover the JE from the trigger rather than the amount.
- OE: raise O4 from 3 → 5 by rewriting OE openings action-first.
- Rubrics: raise R1 from 1 → 5 by escaping quotes; raise R8/R9 from 3 → 5 by adding 2-3 rubrics that probe other levers (retention-code precision, threaded-reply discipline beyond the existing one, email recipient discipline beyond name-presence) so failures distribute, not monopolize on rubric #13.

## Caveats

- The hardness profile is at the floor. If the operator fixes the JSON defect and ships without rebalancing rubric levers, a re-run may still hit pass@1 ≈ 16.7% (the Marina-coordinator-role rubric continues to monopolize failures) but with reduced confidence in real-platform reproduction.
- If subsequent platform runs show pass@1 > 0.40 OR avg density < 40, escalate to `PIPELINE REDO`.
