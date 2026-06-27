# REVIEW score summary — Task 30_6a3de5194c34125ef86fb36f

Scored against `Docs/7_QC_Spec_Doc1.json` (5 = clean ship, 3-4 = NON-FAIL but unacceptable for our 5/5 bar, 1-2 = FAIL band).

## Prompt

| Sub-dim | Score |
|---|---:|
| P1 — Feasibility | 5 |
| P2 — Unique ground-truth end state | 4 |
| P3 — Persona / Business Function fit | 5 |
| P4 — Coherence | 5 |
| P5 — Not contrived | 4 |
| P6 — Investigation not pre-solved | 3 |
| P7 — Single-service tool use | 5 |
| P8 — Truthfulness | 5 |
| P9 — Word budget | 5 |
| P10 — No tool names | 5 |
| P11 — No em-dashes / "at least N" | 5 |
| P12 — Hardness lever density | 3 |

- Worst dim: **P6 (Investigation not pre-solved) = 3** and **P12 (Hardness lever density) = 3**
- Overall: **NON-FAIL** (no sub-dim in 1-2 FAIL band, but ≥ one sub-dim below 5)

## Oracle Events

| Sub-dim | Score |
|---|---:|
| O1 — Coverage | 5 |
| O2 — Atomicity | 5 |
| O3 — Tool/parameter accuracy | 5 |
| O4 — Convention (action-first opening) | 3 |

- Worst dim: **O4 (Convention) = 3**
- Overall: **NON-FAIL**

## Rubrics

| Sub-dim | Score |
|---|---:|
| R1 — Valid JSON | **1 (FAIL)** |
| R2 — Atomicity | 5 |
| R3 — Self-containment | 5 |
| R4 — Outcome > Process ratio | 5 |
| R5 — No tool names in titles | 5 |
| R6 — No unjustified "at least N" | 5 |
| R7 — Evidence grader-actionable | 5 |
| R8 — Lever diversity | 3 |
| R9 — Concentration on one tool call | 3 |
| R10 — Groundedness | 5 |

- Worst dim: **R1 (Valid JSON) = 1 — Major / FAIL band**
- Overall: **FAIL** (R1 = 1)

## Universe

| Sub-dim | Score |
|---|---:|
| U1 — All cited atoms exist | 5 |
| U2 — Reminder genuinely overdue | 5 |
| U3 — Documentation gap real | 5 |
| U4 — Clearance chain documented | 5 |

- Worst dim: 5 across the board
- Overall: **PASS**

## Headline

- One Major: **invalid rubric JSON** — blocks ship until escape fix is applied.
- Three Moderate: investigation pre-solved + hardness lever density + memo-rubric concentration.
- Two Minor: OE convention + persona file completeness.

Triage verdict (see `REVIEW_triage.md`): **SALVAGEABLE** with the fixes in `changes.md`.
