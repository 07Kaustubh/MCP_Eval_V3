# REVIEW Score Summary

Task: `24_6a36e84723508b4e3f391cfc`
Scoring per `Docs/7_QC_Spec_Doc1.json` (5 = shippable, 1 = unsalvageable).

## Prompt

| Sub-dim | Score |
|---|---:|
| Unique Ground Truth | 3 |
| Feasibility | 4 |
| Persona / Business-function fit | 4 |
| Coherence (no bolt-on) | 4 |
| Contrived language | 5 |
| Investigation pre-solved | 5 |
| Single-service tool use | 3 |
| **Maximalism (density floor)** | **1** |
| Word count / format | 4 |
| **Strict-language conventions** | **2** |
| Tool / system name leakage | 4 |
| Truthfulness / lever fit | 3 |

- Worst dim: Maximalism (1).
- Overall: **FAIL** (any sub-dim at 1-2 = FAIL band).

## Oracle Events

| Sub-dim | Score |
|---|---:|
| Completeness vs prompt | 3 |
| **OE count vs V3 range** | **2** |
| **Action-verb openings** | **2** |
| Atomicity | 3 |
| Truthfulness (atoms exist) | 4 |
| **Strict-language conventions** | **2** |

- Worst dim: OE count, Action-verb openings, Strict-language (all 2).
- Overall: **FAIL**.

## Rubrics

| Sub-dim | Score |
|---|---:|
| Atomicity | 4 |
| Self-containment | 5 |
| Outcome-process balance | 5 |
| Binding to prompt | 4 |
| **Truthfulness against ground truth** | **1** |
| Title hygiene | 5 |
| No tool names in titles | 5 |

- Worst dim: Truthfulness (1) - Rubric R4 keyed to a nonexistent ground-truth artifact (no Acme Cloud engagement-scope doc in vault).
- Overall: **FAIL**.

## Overall verdict

**FAIL across all three artifacts.** Triage: **REBUILD**.
