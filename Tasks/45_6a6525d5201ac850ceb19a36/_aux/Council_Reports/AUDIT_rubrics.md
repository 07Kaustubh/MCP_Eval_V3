# AUDIT — S3 Rubrics (Veteran QC Second-Opinion, Strictest Interpretation)

**Task:** 45_6a6525d5201ac850ceb19a36 · **Universe:** starpm (V4) · **Phase:** `--phase rubrics`
**Artifact:** `7_Rubrics.json` — **19 outcome, 0 process** (read-only; report only)
**Universe today:** 2026-07-01 America/Chicago · **Correct answer under test:** Mesa Vista 4C is NOT marketing-ready → HOLD / kick-back on the current in-progress turn `recbd087a4abd605b` (fldTurnStatus selProg).
**Mode:** auto-fire per-phase exit gate (S3 always-mandatory) · **Strictest lens:** 5/5 only, every "should" → "must", every soft convention binding, every lever traces prompt→OE→Fact_Ledger.

> **Version note.** Both S3 councils scored the prior **18**-rubric set. The two Council-B minors were applied before this audit: (i) **R12 made atomic** (email held-only; the listing-until-closed condition moved to R14 final response); (ii) **R12b added** to cover the prompt's "email Carlos with the specifics" (the two unpaid carrying-scope bills). This audit scores the shipped **19**-rubric set. Both prior minors are re-verified **RESOLVED** below.

---

## Deterministic gates reproduced this pass (cited, not re-argued)

| Gate | Result | Exit |
|---|---|---|
| `validate.py --phase rubrics` | PASS — 0 fails, 8 warns, 5 notes (warns = 387.00/1340.00/id substring verify-nudges + X2 observation-period; all grounded per Council A) | 0 |
| `check_rubric_antipatterns.py` (mandatory before verdict, rule 18) | **OK — no construction anti-patterns** (19 criteria × 3 fields) | 0 |
| `check_ordering_coverage.py` | OK — **no ordering language in prompt** → 0 Process is correct (rule 23 not triggered) | 0 |
| `check_qc_binary.py` | 1 FAIL — **Prompt/Coherence** heuristic only (see §Coherence); **Rubric Category Balance = PASS** (outcome 19 > process 0) | 1 |
| `check_oe_rubric_sync.py` | SKIP (parser wants `OE n:`; file uses `OE1:`) — no drift signal, not a rubric defect | 0 |
| `check_criterion_dependencies.py` / `check_rubric_signal.py` | SKIP — no verifier export yet (pre-S4; the passing-cell + signal audits run at S4) | 0 |
| `check_council_yield.py` | 138 KB / 9 reports · 4.0 find/10KB · 0 declines · no excessive-prose flag (rule 20 clean; S3_A 0-finding lens stated in one line) | 0 |
| `test_regression_anchors.py` (Lens 8) | **62/62 PASS** — incl. all StarPM SP-1..SP-9 / SP-INJ / SP-SUB anchors; no silent validator regression | 0 |
| Independent tally | 19 rubrics, all `outcome`, **0 em-dashes** in any title/evidence; no tool-catalog token in any title (validate.py greps `7_Server_Tools_Details.json`) | — |

---

## LENS 1 — Strict QC scoring (Rubric dimension, `Docs_starpm/7_QC_Spec_Doc1.json`)

| Rubric sub-dimension | Strict score | Basis |
|---|---|---|
| **Overall Rubric Quality** | **5/5** | 0 Major, 0 Moderate, 0 counting Minor (census below). <5% minor ⇒ Pass(5). |
| **Rubric Category Balance** (binary) | **5/5** | Outcome 19 > Process 0. Spec Pass(5) 05/22: "number of Outcome Rubrics is greater than Process Rubrics." No 3/4 band. |
| **Process Rubrics** | **5/5** | 0 process; none needed — `check_ordering_coverage` confirms no ordering constraint, and the vendor reconciliation is captured by strict structured-value Outcomes (§5F), so no Outcome-uncoverable behavior exists. |
| **Agent-Centric Phrasing** (binary) | **5/5** | Every title = "The Agent" + action verb; zero passive; zero tool names in titles ("tracking issue", "make-ready channel", "record", "email" are user-visible surfaces, not tools). |
| **All-Failing Rubrics** | **5/5 (N/A)** | No verifier runs yet; spec: "If no rubrics failed all completed runs, this dimension is automatically a 5." Re-audit at S4 against the export. |

**Per-atom evidence table (v18 — required to score Accuracy 5/5):**

| Atom asserted (rubric) | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| current turn = `recbd087a4abd605b`, selProg, 6/15, 6/30 (R1-R3,R7,R17) | `airtable_records` tblMakeReady "Mesa Vista 4C" | fldTurnStatus **selProg**, fldMoveOut **2026-06-15**, fldTargetReady **2026-06-30**, created 2026-05-22 | GROUNDED — current turn |
| prior decoy `recc8534b3fd13954`, selReady (R1 justif) | same table | selReady, move-out 2026-06-01, target 2026-06-14, created **2026-05-29 (later)** | GROUNDED — supersession trap real; correctly excluded |
| deep-clean bill $387 unpaid (R5,R15) | `quickbooks_entities` bill 195089456477 | Sunshine Cleaning, DocNo 2026-SC-4C, TotalAmt **387.00**, **Balance 387.00** (unpaid), due 2026-05-31 | GROUNDED — exact structured value |
| interior-repaint bill $1,340 unpaid (R6,R16) | `quickbooks_entities` bill 696089964235 | Permian Make-Ready Crew, DocNo PD-2026-09, TotalAmt **1340.00**, **Balance 1340.00** (unpaid), due 2026-05-31 | GROUNDED — exact structured value |
| QC re-inspection 2026-07-15 (R8,R18) | `gcalendar_events` fullText "Mesa Vista 4C" | "Make-Ready QC Inspection - Mesa Vista 4C" start **2026-07-15**T10:00-05:00, status confirmed (future) | GROUNDED |
| #make-ready = C004 (R9,R10) | `slack_channels` | {"id":"C004","name":"#make-ready"} | GROUNDED |
| Carlos / Brooke (R11,R12,R13) | `contacts` | carlos.mendez@starpm.com (Onsite PM); brooke.phillips@starpm.com (Supervisor) | GROUNDED |
| Operations / OPS board (R4) | `linear_teams` | {"key":"OPS","name":"Operations"} — single Linear team | GROUNDED (no alt board ⇒ no lock-in) |

No empty evidence cell ⇒ Accuracy is not forced ≤3. Every concrete value resolves to the per-task split. **No S2→S3 drift.**

**No LENS-1 sub-dim < 5.**

---

## LENS 2 — Answer-leakage sweep

**Rubrics phase: no leakage vector.** Rubric bodies are the judge's key, never shown to the agent, so they cannot hand the agent a fact. For completeness, the prompt states none of the discriminators verbatim — $387 / $1,340 / selProg / 2026-07-15 are all described only by content ("vendor side reconciled", "target-ready date ... come and gone", "re-inspection ... middle of this month"), forcing discovery across QuickBooks + Airtable + Calendar (that is the S1 concern; not re-opened here). **Clean.**

---

## LENS 3 — Hardness end-to-end (5 engaged levers; carrier pass-value must depend on traversing the lever)

| Lever | Prompt sentence | OE step | Carrier rubric(s) whose PASS requires traversing it | Fact_Ledger atom | Status |
|---|---|---|---|---|---|
| **L2 structured-DB skip** (symmetric) | "vendor side reconciled ... billed but ... unpaid does not count as closed" | OE3/OE6 (tblMakeReady selProg; QB balances vs Slack "bill entered") | R2 (not-Ready knowable only from selProg row), R7/R17 (In-Progress+6/30 only in tblMakeReady), R5/R6/R15/R16 (balances only in QuickBooks) | selProg; 387.00/1340.00 balances | ✅ carried |
| **L1/L10 latching / supersession / wrong-row** (Opus-sel) | "Carlos has 4C down as wrapped ... wants it released" | OE2/OE4 (prior selReady created later; "complete" maint ticket) | R1 (determination MUST land on `recbd087`; evidence FAILS if written to prior selReady turn or a maintenance ticket), R2 (must not flip to Ready) | recbd087 vs recc8534/reca424/rec12969 | ✅ carried |
| **L31 explicit negative directive** (Gemini-sel) | "if it is not, say so plainly and hold it ... does not go to listing" | OE9 (form the kick-back) | R14 (final response states NOT marketing-ready / held / should NOT be listed), reinforced R2/R3/R10/R12/R13 | selProg + HOLD decision | ✅ carried |
| **L7 multi-write (6 distinct writes)** | "record ... open a ticket ... post ... email ... Brooke needs to hear it" | OE10-15 | R1 (Airtable) + R4 (Linear issue) + R5-R8 (Linear comment) + R9 (Slack C004) + R11/R12b (Gmail draft) + R13 (Brooke) — 6 writes / 5 services | recbd087, OPS, C004, Carlos, Brooke | ✅ carried, NOT collapsed to 3 |
| **L9 future-event + past-due** | "re-inspection ... middle of this month ... factors into whether I can call this done"; "target ... come and gone" | OE7/OE3 | R8/R18 (7/15 pending) + R7/R17 (6/30 past due) | 2026-07-15; 2026-06-30 vs 2026-07-01 | ✅ both sub-levers carried |

Every engaged lever has ≥1 Outcome whose pass value depends on actually traversing it. **No HARDNESS_REGRESSION.** The S1-AUDIT mandatory downstream mitigation (preserve 5-6 distinct writes) is satisfied exactly.

---

## LENS 4 — Density (StarPM V4 per-model bar; V3 50/40 scheme NOT applied)

Per task scope and `Hardness_Plan.md` "THIN density acceptance": StarPM band is design-target **40+ per model** (Opus + Gemini scored separately), absolute floor **15**. The rubric set forces **6 distinct writes + a 7-of-8-service discovery sweep**, consistent with a competent projection of **Opus ~43-45 / Gemini ~41-43** (meets 40+); minimizing sketch ~21 and empirical StarPM anchor 33-38 sit in the THIN band, well above the 15 floor. Density was **pre-accepted THIN at S1 AUDIT** with a per-task justification and a **standing hard S4 gate** (per-model average < 40 on real runs → PIPELINE REDO, rule 11). The rubric set aligns with a 40+ competent trajectory and preserves the 6-write mix. **Not re-blocked** (per task MUST-NOT-DO). Clears the 15 floor decisively. **PASS for the rubrics phase.**

---

## LENS 5 — Adversarial veteran review

### OBS-1 — R12b couples two bills (deep-clean + interior-repaint unpaid) — **MINOR (Overly-Broad-adjacent) · bundling exception HOLDS · non-counting**
R12b: *"The Agent's email to Carlos identifies that the deep-clean and interior-repaint bills remain unpaid."* Two content items that can fail independently → prima facie a split candidate.
**Adjudication (the flagged #1 scrutiny item): the bundling exception holds; do NOT split, do NOT count.**
- **2 items, not 3+.** The operative, gate-codified anti-pattern is "**three or more** items under a completeness/step predicate"; the regression definition explicitly excludes two-action bundles. `check_rubric_antipatterns` returned clean.
- **Related, not unrelated.** The atomicity rule targets "two **unrelated** reasons." These are the same class (carrying-scope bill unpaid), named together in the prompt ("the two scopes that carried this turn were the deep clean and the interior repaint"), both mis-claimed by Carlos in one Slack breath ("deep clean is closed out" + "repaint ... bill entered"), discovered in one QuickBooks sweep.
- **No valid-path false-fail.** Carlos was wrong about **both**; a correction naming only one leaves him with a false belief about the other, so requiring both is GT-aligned — an incomplete correction is a genuine fail, not a false-fail.
- **Granular checks live elsewhere.** The per-bill exact amounts are atomic on the ticket (R5/R6) and final response (R15/R16); R12b deliberately tests only "the email corrects Carlos on both scopes." Splitting would duplicate, not sharpen.
*Optional polish (not required for PASS):* split into two 1.2 rubrics if a future pass wants belt-and-suspenders atomicity. Consistent with how R2 and R7/R17 are treated.

### OBS-2 — R7 / R17 couple "In Progress" + "6/30 past due" — **MINOR (Overly-Broad-adjacent) · bundling exception HOLDS · non-counting**
Two facets of one record's schedule-state proposition ("not done and overdue"), causally linked, 2 (not 3+) items, prompt foregrounds the past-due target ("come and gone"). Same exclusion as OBS-1. No false-fail of a competent HOLD trajectory (which states both). Acceptable.

### OBS-3 — R14 title is conjunctive, evidence is disjunctive — **MINOR (polish) · non-counting**
R14 title reads "not marketing-ready **and** being held, **and** should not be released for listing" (AND); the evidence lists "not marketing-ready **/** is being held **/** should not be listed" (OR). The judge evaluates the **title** (conjunctive), so the strict reading requires all facets. This is defensible: "not marketing-ready" ⟺ "held" (synonyms for the kick-back) and the prompt fuses the no-list consequence ("hold it, **because** it does not go to listing"), so a correct HOLD call states all facets and passes under either reading; only an incomplete call is failed. *Optional polish:* align the evidence conjunction to the title (or vice-versa) to remove the AND/OR ambiguity. No valid-path false-fail (rule 16 not triggered — the misreading direction only tightens on incomplete answers).

### R2 (negative anti-latching bundle) — **CLEAN 5**
"does not advance to Ready / does not mark marketing-ready / remains In Progress" = three phrasings of ONE observable (`fldTurnStatus != selReady` on recbd087; enum has no "hold" value, correctly why R2 checks "did not advance to Ready" not a phantom hold enum). Single data point → atomic. Evidence scopes the marketing-ready clause to record updates, so no cross-artifact leak. Wrong-pass guard: a do-nothing agent passes R2 but fails R1 (must record) + R3 (must state hold). Correct decomposition.

### Exact amounts $387 / $1,340 (R5/R6/R15/R16) — **NOT Overly-Specific · CLEAN 5** (load-bearing adjudication)
Under the strictest Overly-Specific lens I stress-tested the alt-path "agent reports both bills unpaid but omits the figures." **Not a defect:** the amounts are **exact static values from a structured source** (QuickBooks Balance), which the guidelines' worked Example 1 makes the *preferred* outcome form ("a value the agent cannot fake without doing the underlying work"). They carry the L2/L11 lever (the figure is the proof the agent went past the Slack "bill entered" chatter into QuickBooks), and the prompt orders exactly this ("vendor side reconciled", "spelling out exactly what is still left", "with the specifics"). Rule 4 correctly keeps them EXACT (not "approximately" — not calculated). Hard exclusion: one-correct-value structured field per the V3 flexibility table. Evidence anchors "the scope named with an unpaid ... bill of $387", so $387 / 387.00 / "$387 balance" all pass.

### Single-target uniqueness — **CLEAN**
R1 binds `recbd087a4abd605b` by content (6/15 move-out + 6/30 target) AND id, and its evidence explicitly fails a determination written to the prior selReady turn `recc8534b3fd13954` or to a maintenance ticket (`reca424`/`rec12969`). Exactly one current in-progress turn exists. **No F7 ambiguous-target.**

### Reverse coverage / no beyond-prompt rubric — **CLEAN**
R1-R3→record determination; R4-R8→ticket "exactly what is still left"; R9-R10→make-ready post; R11-R12b→email Carlos with specifics; R13→notify Brooke; R14→"give me the call"/no-list; R15-R18→first-paragraph direct-report asks ("whether both closed ... vendor side reconciled ... re-inspection factors in"). Every rubric traces to an explicit prompt ask. No rubric exceeds the prompt.

### Final-Response Coverage (R14-R18 = decision + 4 reasons) — **CLEAN**
R14 decision + R15 (deep-clean unpaid) + R16 (repaint unpaid) + R17 (In-Progress/6-30 past due) + R18 (7/15 pending) matches the OE "Final response content" spec exactly.

### 2-artifact grading (ticket R5-R8 + final response R15-R18) — **NOT dilution**
Each of the 4 outstanding facts is graded on exactly two *distinct explicit deliverables* the prompt names separately; they fail independently (a strong ticket + a vague final response passes R5-R8 but fails R15-R18). One-rubric-per-required-artifact, not filler — matches the reference 2-artifact discipline. The HOLD decision on 5 surfaces (R3 Airtable / R10 Slack / R12 email / R13 Brooke / R14 final response) likewise maps to 5 prompt-named communications; no single agent error trips two (e.g. record hold in Airtable but sign off in Slack → R3 passes, R10 fails). No nested accept-set.

### Channel / method lock-in — **CLEAN**
R13 (notify Brooke) is method-agnostic (email OR Slack), matching the prompt's goal ("Brooke needs to hear it from us"). No single-channel lock-in where the prompt named only a goal.

### Process-disguised-as-Outcome — **NONE**
All 19 are genuine 1.1 (write result) / 1.2 (action content) / 2.1 (key fact). The reconciliation is captured by strict Outcome values, not a process rubric. 0 process is correct.

### Old Council-B minors — **RESOLVED**
- MINOR-1 (R12 stacked held + listing-condition): **fixed** — R12 is now held-only; justification confirms the listing condition is carried by R14.
- MINOR-2 (email "with the specifics" not graded on the email): **fixed** — R12b now grades the email's vendor specifics. Prompt ask (f) is now covered by R11 + R12 + R12b.

---

## LENS 7 — Anti-rationalization ledger (each near-miss finding carries a HARD exclusion, not a "probably fine")

| Near-miss | Would-be severity | Hard exclusion cited (why NOT promoted to REVISE) |
|---|---|---|
| R12b two-bill coupling | MINOR Overly-Broad | Gate threshold is 3+ items; these are 2 related same-class items; `check_rubric_antipatterns` clean; GT requires both ⇒ no valid-path false-fail |
| R7/R17 two-facet coupling | MINOR Overly-Broad | Same-proposition schedule state; 2 (not 3+); prompt foregrounds past-due; competent HOLD states both |
| $387 / $1,340 exact amounts | MODERATE Overly-Specific | Exact-match structured one-correct-value field (V3 flexibility table); guidelines' preferred outcome form; carries L2/L11 |
| R14 conjunctive title | MINOR | Facets are synonyms of one decision + prompt-fused consequence; misreading tightens only on incomplete answers |
| Prompt/Coherence exit-1 | (Prompt sub-dim) | Not a rubric sub-dim; adjudicated §Coherence; per task scope no PROPAGATE |

No "I considered flagging X but decided it's fine because ..." line remains without a documented hard exclusion.

---

## LENS 8 — Regression-anchor verification

`python3 Validators/test_regression_anchors.py` → **62 passed, 0 failed out of 62** (exit 0), including StarPM SP-1..SP-9 (auto-detection, contamination, invalid channel, param traps) and SP-INJ / SP-SUB. No silent validator regression; the anti-pattern and grounding gates cited above are trustworthy this pass.

---

## Prompt / Coherence `check_qc_binary` exit-1 — out of scope, no PROPAGATE

The single binary FAIL is on **Prompt / Coherence**, not any Rubric sub-dimension: the bolt-on heuristic reports 24% shared vocabulary (1% under the 0.25 threshold) + a unique "Open" token on the action-directive sentence. Confirmed a **heuristic false-positive, not a rubric defect**: the sentence is load-bearing (carries 3 of the task's deliverables — ticket, make-ready post, Carlos email), is anaphoric to the established QC hold ("post where **it** lands", "**the** specifics"), and passes the spec's real sentence-removal bolt-on test (removing it collapses the task). Already scored PASS (STRICT) by S1 AUDIT and PASS by Council B §5. The S1-locked prompt is not re-opened; the flag introduces no Major/Moderate/Minor on the rubric set. **No PROPAGATE TO S1.**

---

## Severity census (independent — NOT trusting any prior report's self-report, rule 122)

**0 Major · 0 Moderate · 0 counting Minor.** Overall Rubric Quality denominator 19 → 0% issues → Pass(5); pipeline absolute-count gates (Major ≥3, Major+Mod ≥5, all ≥8) all clear. Three non-counting observations (OBS-1/2/3) logged for transparency, each cleared by a documented hard exclusion; all optional polish, none blocking.

## Verification statements
- [x] `validate.py --phase rubrics` re-run this pass; exit 0 (0 fails).
- [x] `check_rubric_antipatterns.py` exit 0 (re-confirmed after reading the shipped set).
- [x] Regression-anchor suite executed this pass; **62/62 PASS**.
- [x] All 5 engaged Hardness levers trace prompt→OE→carrier-rubric→Fact_Ledger atom.
- [x] Single-target uniqueness, final-response coverage, reverse-coverage, no-tool-names, no-em-dash, method-agnostic-notify all verified.
- [x] Anti-rationalization scan complete; every near-miss carries a hard exclusion.
- [x] Density assessed on the StarPM per-model band (NOT V3 50/40); THIN pre-accepted, not re-blocked; 6 writes preserved; 15 floor cleared.
- [x] Prompt/Coherence flag scoped as a prompt-phase heuristic false-positive; no PROPAGATE.

## Discrepancies surfaced
- None blocking. Councils scored the 18-rubric predecessor; the shipped 19-rubric set has both council minors resolved and is cleaner than the reviewed version.

---

**AUDIT VERDICT: PASS (STRICT)**
