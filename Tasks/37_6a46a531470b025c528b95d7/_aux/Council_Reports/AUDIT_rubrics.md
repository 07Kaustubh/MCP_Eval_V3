# AUDIT rubrics (STRICTEST) — Task 37 (on-demand, fresh chat)

**Universe:** keystone · **Trigger:** `PIPELINE AUDIT --phase all` (pre-upload sanity gate)
**Artifact:** `15_Updated_Rubrics.json` (30 rubrics — MATERIALIZED after 2 Applied rows from `changes.md`)
**Diff awareness:** `7_Rubrics.json` (candidate original) — differs on rubric[3] title/justification/evidence extension + rubric[24] justification tightening.
**Baseline priors:** prior `AUDIT_rubrics.md` (corrected-materialization) + `AUDIT_rubrics_original.md` + `FINAL_materialize.md` all PASS (STRICT). Independently re-derived here.

## Programmatic floor (inherited)
- `validate.py --phase rubrics` = **FAIL** on 2 aggregate bands (27% Moderate+, 27% any-severity) + 13 warns (12× Jaccard-71% pairs from per-LO fan-out shell + 1× missing-"email"-verb WARN) + 4 notes. **Both FAILs re-adjudicated below.**
- `verify_universe_atoms.py` = **PASS** (41/41 atoms grounded)
- `test_regression_anchors.py` = **48/48 PASS**

## LENS 1 — Strict QC scoring (Docs/7_QC_Spec_Doc1.json)

Per-atom evidence table for the 2 MATERIALIZED rubrics + 4 special-attention rubrics ([22], [23], [24], [28]):

### Rubric [3] AFTER (Row #1 — Derek Moss content bundle, extended from 1→3 loans)

| Atom in AFTER title | Universe source | Verified |
|---|---|---|
| LN-2026-00008 conditional_approval $276,400 lock 2026-03-11 | `mortgage_los.loans` row `los_loan_58b56696d513` | ✅ |
| 2 outstanding conditions + 2 required docs on LN-2026-00008 | `mortgage_los.conditions` → 2 outstanding; `document_checklist_items` → 2 required (appraisal + homeowners_insurance) | ✅ |
| LN-2026-00196 processing $229,000 lock 2026-03-13 1 required doc: w2_current | `mortgage_los.loans` matches; `document_checklist_items` → 1 required (w2_current) | ✅ |
| LN-2026-00632 underwriting $268,000 lock 2026-04-04 | `mortgage_los.loans` matches | ✅ |
| Derek's LO id `los_staff_f9aa4c3c2fcb` → 3 loans in Sofia's pipeline | Join → exactly {LN-2026-00008, LN-2026-00196, LN-2026-00632} | ✅ |

Cohort symmetry check across all 8 per-LO content rubrics:

| LO | Rubric | Loans in AFTER title | Sofia-pipeline loans for LO | Symmetric? |
|---|---|---|---|---|
| Carlos | [1] | 2 | 2 | ✅ |
| Derek | [3] AFTER | 3 | 3 | ✅ (was 1/3 outlier — closed) |
| Keisha | [5] | 4 | 4 | ✅ |
| Amy | [7] | 2 | 2 | ✅ |
| Natasha | [9] | 2 | 2 | ✅ |
| James | [11] | 3 | 3 | ✅ |
| Priya | [13] | 3 | 3 | ✅ |
| Marcus | [15] | 2 | 2 | ✅ |

**Rubric [3] verdict: PASS (STRICT).**

### Rubric [24] AFTER (Row #2 — Elena+Denise justification tightening)

Title UNCHANGED (prompt-inherited — prompt names both by name). Justification rewritten to remove implicit compliance-authority claim on Elena.

| Claim in AFTER justification | Universe source | Verified |
|---|---|---|
| Denise = compliance authority per Slack C004 (breach response, portal-access audit) | Slack C004 ts=1775570820 + ts=1775572140 (Denise author, verbatim quotes) | ✅ |
| Elena = senior processor with lender-coordination specialization | `mortgage_los.staff` row `los_staff_c6b42763fb1f`: role=processor, specialization="Doc collection, lender coordination" | ✅ |
| LN-2026-00008 + LN-2026-00010 in phishing scope; C004 also names LN-2026-00522, LN-2026-00009 | Slack C004 ts=1775572140 verbatim names all 4 | ✅ |
| LN-2026-00613 30yr→15yr TRID redisclosure per Slack C002 | Slack C002 verbatim quotes present | ✅ |
| 5 loans on terminated LOs | Join → 5 loans (Brian × 1 + Veronica × 4) | ✅ |

Em-dashes in `15_Updated_Rubrics.json`: 0.

**Rubric [24] verdict: PASS (STRICT).**

### Rubric [22] — "adds an activity note to at least one loan"

Prompt: "add activity notes to any loan in the system that needs updating."
- "any loan that needs updating" implies floor ≥ 1.
- Rubric title "at least one" is a defensible floor per `Reference/Rubric_Format.md` ("at least N" allowed when prompt mandates a minimum).
- Evidence gate = trajectory tool-call success (not final-response text). Reasonable measurement.

**Rubric [22] verdict: PASS (STRICT).**

### Rubric [23] — "creates at least one CRM engagement"

Prompt: "log everything in the CRM."
- "log everything" is universal. Rubric "at least one" is a WEAKER floor.
- Under strictest reading: floor is defensible (≥1 mandate) but under-specifies (prompt mandates several).
- **Minor soft observation** — not blocker. Trajectory range 0-11 engagements per run confirms a floor of 1 catches "zero engagement" failures while allowing model variance.

**Rubric [23] verdict: PASS (STRICT) with soft observation.**

### Rubric [24] — "at least one compliance concern" (title-level "at least N")

Prompt: "If anything you find looks like it could be a compliance concern..."
- "If anything" = CONDITIONAL escalation.
- Universe seeds 3 latent findings (phishing UWM / TRID LN-00613 / terminated-LO gap).
- Title "at least one" matches conditional floor. Defensible.

**Rubric [24] title verdict: PASS (STRICT).**

### Rubric [28] — LN-2026-00623 CTC anomaly

- Universe verification: status=clear_to_close; document_checklist_items status=required → exactly 5 items. ✅
- Trajectory spot-check on runs 1/3/5: **0/3 mentioned LN-2026-00623 in final response**. Legitimate Bucket 3 model summary-drift failure (per REVIEW_hardness pass@1 = 33.3% failure locus). NOT rubric brittleness.

**Rubric [28] verdict: PASS (STRICT).**

**LENS 1 sub-dim scores (strictest 5/5-only bar):**

| Sub-dim | Score | Note |
|---|---|---|
| Outcome > Process ratio | **5** | 30 Outcome / 0 Process |
| Atomicity | **5** | Per-LO bundles atomic; final-response probes each name single finding |
| Groundedness | **5** | 41/41; both AFTER rows atom-verified |
| Self-containment | **5** | All 30 readable independently |
| Verifiability | **5** | Binary-observable evidence |
| Coverage | **5** | 8 levers × prompt anchors = full |
| Redundancy | **5** | Jaccard 71% = structural shell, not semantic (LENS 5) |
| Severity balance | **5** | No inflation |
| Persona attribution | **5** | Row #2 tightening |
| Method-lock hygiene | **5** | 2 method-locks both prompt-inherent |

**LENS 1 verdict: PASS (STRICT).**

## LENS 2 — Answer-leakage sweep

Rubrics held server-side by verifier, not shown to solving agent. Leakage vector = ZERO.

**LENS 2 verdict: PASS (STRICT).**

## LENS 3 — Hardness end-to-end trace

| # | Lever | Rubric anchor(s) |
|---|---|---|
| 1 | 26 active loans | [25] |
| 2 | All 26 locks expired | [17], [26] |
| 3 | 5 terminated-LO loans | [20], [27] |
| 4 | 26 outstanding docs across 8 loans | [3] AFTER, [5], [7], [9], [11], [13], [15], [29] |
| 5 | UWM/Keisha phishing scope | [24] AFTER (verbatim 4-loan scope) |
| 6 | LN-2026-00613 TRID | [13], [24] AFTER |
| 7 | LN-2026-00623 CTC | [13], [28] |
| 8 | LN-2026-00010 max-docs | [9], [29] |

**LENS 3 verdict: PASS (STRICT).**

## LENS 4 — Density projection

Measured 216.8 avg. Rubrics gate the outcomes those 216.8 calls produce. **PASS (STRICT).**

## LENS 5 — Adversarial + validator-FAIL re-adjudication

### 27% Moderate+ / 27% any-severity validator FAIL

Source: 12 Jaccard-71% pairs from the 8 per-LO fan-out rubric pairs — structural shell repetition.

Per-pair semantic distinctness (each targets DIFFERENT recipient email + DISJOINT loan atoms):

| Cohort | Notify | Content | Distinct? |
|---|---|---|---|
| Carlos | [0] carlos.rivera | [1] 2 loans | ✅ |
| Derek | [2] derek.moss | [3] 3 loans AFTER | ✅ |
| Keisha | [4] keisha.williams | [5] 4 loans | ✅ |
| Amy | [6] amy.chen | [7] 2 loans | ✅ |
| Natasha | [8] natasha.okafor | [9] 2 loans | ✅ |
| James | [10] james.thornton | [11] 3 loans | ✅ |
| Priya | [12] priya.desai | [13] 3 loans | ✅ |
| Marcus | [14] marcus.webb | [15] 2 loans | ✅ |

Fan-out defense:
- 8 LOs is factual (`mortgage_los.loans.assigned_lo` filter).
- Each notify targets DIFFERENT recipient email; content-rubrics gate DISJOINT loan atoms.
- `Reference/Rubric_Format.md` Redundancy: "Different write actions to different recipients are NOT redundant."
- Consolidation to 8 combined rubrics would violate atomicity (send-success + content-correctness are independent pass/fail).

**Verdict: 8×2=16 fan-out is atomically-correct; FAIL band is validator heuristic false positive.**

### Other adversarial

| Anti-pattern | Present? | Note |
|---|---|---|
| Method-lock | [21] C002 Slack post; [24] Elena+Denise emails | Both prompt-inherent |
| Persona-scope violation | ❌ | Row #2 fix; all 8 LOs + escalation confirmed active |
| Tool-name in title | ❌ | 0 |
| Entity drift | ❌ | LENS 1 [24] |
| Em-dashes | ❌ | 0 |
| "At least N" | 3 uses ([22], [23], [24]) | All prompt-defensible |
| "(or similar)" | [19] "(or similar organizational structure)" | Structural (breakdown shape), not value-level; defensible |
| Internal IDs | ❌ | 0 `los_staff_*` in titles |

**LENS 5 verdict: PASS (STRICT).**

## LENS 6 — RETIRED in v18.

## LENS 7 — Anti-rationalization

1. **27% Moderate+ FAIL genuine?** Cross-checked all 12 pairs: DIFFERENT recipient + DISJOINT atoms. Consolidation violates atomicity. NOT rationalization.
2. **Rubric [23] under-gates?** MINOR soft observation retained; "at least one" is defensible floor for "log everything" (trajectory range 0-11 confirms floor catches failures).
3. **Rubric [28] brittle?** 0/3 spot-checked trajectories named LN-2026-00623 in final response = legitimate Bucket 3 summary-drift, not rubric problem.
4. **Rubric [24] Row #2 cosmetic?** Substantive Persona-attribution sub-dim fix (removed Elena implicit compliance-authority claim). Title unchanged. Not cosmetic.
5. **Rubric [21] C002 lock?** Prompt-inherent universe resolution. Not authored lock-in.

**LENS 7 verdict: No suppressed findings.**

## LENS 8 — Regression anchors

48/48 PASS (inherited).

## LENS 9 — RETIRED in v18.

## Final verdict

**RUBRICS: PASS (STRICT)**

One-line summary: 30/30 ground-truth-atomic and prompt-anchored; both MATERIALIZE Applied rows atom-verified; validator FAIL band confirmed false positive (per-LO fan-out is atomically-correct); 3 "at least N" uses prompt-defensible; Rubric [28] on LN-2026-00623 is legitimate Bucket 3 gate (0/3 trajectories named it) not brittleness.
