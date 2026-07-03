# REVIEW triage — Task 37

## QC scoresheet (Prompt + Universe sub-dims from `Docs/7_QC_Spec_Doc1.json`)

### Prompt sub-dims
| Sub-dim | Score | Reason |
|---|---|---|
| Feasibility | 5 | 6/6 measured runs completed; 4/6 achieved 28+/30 rubrics — task is solvable within one context window |
| Coherence (bolt-on / command-list) | 5 | All 3 bolt-on WARNs are false-positives on universe re-check; register is natural |
| Contrivance | 5 | Boss-panic scenario + 3 pm deadline is a realistic mortgage-shop pattern |
| Pre-solving | 5 | Prompt hides ALL counts, all loan IDs, all lender names, all borrower names, all termination facts |
| Explicit Tool Mention | 5 | Zero tool names in prompt body |
| Single-Service Tool Use | 5 | Requires ≥5 distinct services (LOS, email, Slack, CRM, contacts) |
| Truthfulness (universe alignment) | 5 | All persona/entity/staff/loan references verified via universe queries |
| Date alignment | 5 | "today" and "this morning" resolve inside universe today = 2026-04-28 |
| Unique ground-truth end-state | 5 | 26 loans / 8 LO recipients / one Camille summary / one Grace report / one Slack post — all uniquely determined |
| Word count / dashes / linter | 5 | 343 words (< 500 cap); no em-dashes; no linter blocker at submission time |
| Persona coherence | 5 | Sofia (processor) writing to boss + lock desk + LOs + compliance is fully coherent |

### OE sub-dims
| Sub-dim | Score | Reason |
|---|---|---|
| Completeness (reverse-map from rubrics) | 5 | Every rubric traces to ≥ 1 OE; every write action has an OE |
| Accuracy (atom grounding) | 5 | Every "expected discovery" verified against universe |
| Lifecycle order | 5 | Reads precede writes; no closed-period conflict |
| Tool-name presence | 5 | Every OE names verbatim tool(s) + parameter names |
| Method / service consistency | 5 | Method-agnostic where prompt allows; method-locked where prompt names channel |

### Rubric sub-dims
| Sub-dim | Score | Reason |
|---|---|---|
| Atomicity | 5 | 30 rubrics; per-LO bundling is single-message atomicity, defensible |
| Self-Containment | 5 | Every rubric readable independently; no cross-references |
| Truthfulness (evidence grounding) | 5 | 100% atom-verified via universe |
| Outcome vs Process ratio | 5 | 30 Outcome / 0 Process — Outcome outnumbers Process; no missing-Process propagation flag |
| Method-lock hygiene | 5 | 2 method-locks (Slack C002, Elena+Denise emails) both prompt-inherent |
| "At least N" hygiene | 5 | 3 uses — all minimum-bar acceptable (activity note, CRM engagement, compliance concern) |
| Coverage symmetry across cohort | **3** | Rubric [3] Derek Moss only checks 1 of 3 loans; asymmetric with all 7 other LO cohorts (Moderate) |
| Persona / attribution grounding | **4** | Rubric [24] Elena Marchetti attribution: LOS role = processor, no compliance evidence. Denise IS compliance. Defensible but Minor. |
| All-Failing Rubrics (S4 bucket) | 5 | Bucket 1 ratio = 0/8 = 0% (well below 25% threshold) |
| No "at least N" in title unless mandated | 5 | 3 uses defensible (see above) |
| No tool names in title | 5 | Zero rubric titles contain tool names |

**Worst sub-dim: 3 (Rubric coverage symmetry on Derek Moss) → NON-FAIL band**
**Worst prompt/OE sub-dim: 5**
**Overall QC band: NON-FAIL band. Two sub-dims below 5 — both require fixes to reach ship bar of clean 5/5.**

## Hardness numbers (from `_aux/Trajectory_Stats.json`)

- Density: **avg total 216.8 / avg MCP 194.7 tool calls** (design target ≥ 50, floor 40) — **PASS**
- Difficulty: **pass@1 = 33.3% (2/6)** — **PASS** (below 40% cap, 6.7 pp headroom)
- All 6 runs completed (0 errors) — **T3 PASS**
- Bucket 1 ratio: 0% — **All-Failing Rubrics sub-dim 5/5**
- Hardness verdict: **PASS**

## Triage decision table walk

| Trigger | Fires? | Notes |
|---|---|---|
| Business function mismatch | NO | Prompt is Loan Operations end-to-end; matches assigned business function |
| Persona mismatch (need swap within business function) | NO | Sofia (Processor) is the correct persona for a pipeline-review-owns-files task |
| ANY prompt/universe sub-dim in 1-2 (FAIL band) | NO | Worst prompt sub-dim: 5; worst OE sub-dim: 5 |
| Hardness fail (pass@1 > 40% OR avg tool calls < 40 OR levers don't trigger OR answer leakage) | NO | pass@1 = 33.3%; avg tool calls = 216.8; all 8 levers trigger; no leakage |
| Otherwise (every sub-dim scores 3-5, no hardness failure) | YES | SALVAGEABLE |

## VERDICT — **SALVAGEABLE**

Fix path:
1. **Rubric [3] coverage extension** (Moderate) → extend to cover Derek's LN-2026-00196 + LN-2026-00632, matching the pattern used for all 7 other LO cohorts. Raises Coverage-symmetry sub-dim from 3 → 5.
2. **Rubric [24] Elena attribution note** (Minor) → tighten justification to reflect actual universe evidence (Denise = confirmed compliance authority via Slack C004; Elena = plausible but not universe-authoritative). Optionally reword rubric title to accept EITHER Elena OR Denise (both allowed but not both required) if the operator wants to loosen. Alternatively leave rubric as-is and note the attribution question in candidate feedback.

Post-fix, expected: 5/5 on every sub-dim.

**No REBUILD trigger fires. Proceed to `PIPELINE MATERIALIZE` in a fresh chat.**
