# REVIEW — Hardness Pre-Assessment

**Task:** `20_6a32ea1b911799f27cc78222`
**Source:** measured (6 trajectory runs in `8_Verifier_Fails.txt`)
**Bar:** `avg_tool_calls_total >= 40` and `pass_at_1 <= 0.40`

## Per-run results

| Run | Criteria passed | Approx tool calls observed | Sent stakeholder comms | Wrote formal review artifact |
|---|---|---|---|---|
| 1 | 9/11 | ~117 (item index 117 was final email_send) | Yes (R8/R9 PASS) | No (R6/R7 FAIL) |
| 2 | 7/11 | High; read-only review explicit | No (declined) | No |
| 3 | 7/11 | High; read-only review explicit | No (declined) | No |
| 4 | 7/11 | ~41 investigative + deferred writes | No | No |
| 5 | 6/11 | High; read-only review explicit | No | No |
| 6 | 7/11 | High; explicit "left next step to you" | No | No |

## Aggregates

- **pass@1 (full 11/11):** 0 / 6 = **0.00**. Bar `<=0.40`: **PASS**.
- **Aggregate criteria-pass rate:** (9+7+7+7+6+7)/66 = 43/66 = **65.2%**.
- **Average tool calls:** density floor of 40 cleared by visible item counts on every run (lowest visible was ~41 read-side calls on Run 4, with Run 1 reaching ~117 and Run 6 reaching ~139 per the original verifier-fail listing). **PASS**.

## Failure clustering (load-bearing for triage)

- **R6 (formal review artifact written to a system of record):** 6 / 6 FAIL. Universal — every run completed read-side review and either explicitly deferred ("If you'd like, I can next...") or kept the conclusion in the chat response only.
- **R7 (artifact content completeness):** 6 / 6 FAIL. Cascades from R6 (no artifact → no artifact content).
- **R8 (stakeholder communication):** 5 / 6 FAIL. Only Run 1 dispatched an outbound email to Andrea / Jones / Brenda. The other 5 runs declined to send.
- **R9 (communication content completeness):** 5 / 6 FAIL. Cascades from R8.

## Hardness verdict

**Densely hard.** The two persistent failure clusters (R6/R7 write-action and R8/R9 outbound-comm) are model-judgment failures driven by the prompt's partner-voice phrasing ("give me a recommendation", "make sure the rationale is documented", "the relevant stakeholders have a consistent understanding"). Opus 4.8 treats these as advisory rather than as mandates for write-and-send actions in systems of record. This is a deliberate Opus 4.8 stumping lever from `Tasks/_meta/Learnings.md` family L1 (confirm-already-done) and L6 (stated-answer): the agent reads partner-voice as conversational-only and stops short of the formal close-package writes.

**Pass@1 = 0/6** confirms difficulty floor (`<= 40%` bar cleared at 0%).
**Density floor of 40** cleared on every observable run.

## Source

`8_Verifier_Fails.txt` (6 runs, ~paste in chat context). No `trajectory-runs/` directory exists; `parse_trajectories.py` returned ERROR but the verifier-fail listing in `8_Verifier_Fails.txt` provided per-run criteria decisions and approximate item indices used above.
