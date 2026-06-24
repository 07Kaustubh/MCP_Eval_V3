# AUDIT_rubrics.md — Strict Veteran Audit (S3 rubrics, Round 2)

**Phase:** Rubrics (S3, AUDIT REVISE round 2 of 3)
**Task:** Tasks/27_6a39fd19048f9213281ec7b
**Persona:** Ben Arinzo, Bookkeeper, Brookfield CPAs & Advisors
**Auditor:** strict veteran reading; every "should" read as "must"; 5/5 only; density bar 50+ midpoint; any answer-leakage hit on a derived figure = BLOCKER
**Date:** 2026-06-23
**Deliverable:** `7_Rubrics.json` (**24 rubrics**, all `outcome`, V3 nested schema; +2 vs round 1)
**Prior round:** REVISE (F1 + F2 + F3)
**Verdict:** **PASS (STRICT)**

---

## Summary

Producer applied all three round-1 fixes verbatim:

| Fix | Status | Evidence |
|---|---|---|
| **F1** — Add vault rubric for USD-cash gotcha (P9 lever vault gap) | **Applied** | New rubric `c3d84f2b-...03e6` at index 6: "The Agent's Records Vault write-up notes that account 102000 is brookfield's USD Cash - Payroll account so the recon's FX-revaluation explanation cannot apply on principle (or similar)." — mirrors R10 and R20 wording. Justification explicitly cites P9 lever traceability. |
| **F2** — Add vault rubric for FP-2025-11 record refutation (OE 20(a) coverage gap) | **Applied** | New rubric `b2c75e1a-...92c4` at index 3: "The Agent's Records Vault write-up notes that the FP-2025-11 102000 reconciliation BL-8DCA6908E272 actually carried a variance of $3.42 with no variance_explanations and no attachments recorded (or similar)." — mirrors R8 (email) and R17 (final response) wording. |
| **F3** — Strip `approximately` from 5 rubrics targeting exact static single-record dollar figures | **Applied** | Round-2 string-scan: zero `approximately $` hits in any title. R2, R7, R14 now say `$617.63` (no qualifier). R8, R17 now say `$3.42`. R14 now says `$617.63, not $42`. Round-1 had 6 `approximately $` hits in titles; round-2 has **0**. |

All round-1 findings resolved. Re-running the five lenses against the 24-rubric set:

- **LENS 1** — every applicable sub-dim now scores **5/5** (Overall Rubric Quality recovered; Completeness vs prompt asks recovered via F1+F2; Qualifier placement recovered via F3).
- **LENS 2** — answer-leakage CLEAN (confirmed unchanged from round 1; the two new rubrics add agent-output content checks, not new agent-readable source artifacts).
- **LENS 3** — **6/6 hardness levers trace end-to-end across all three write surfaces**. P9 (USD-cash) now traces through R10 (email) + R20 (final response) + new vault rubric `...03e6`. P8 multi-link chain strengthened: FP-2025-11 record refutation now travels through R8 (email) + R17 (final response) + new vault rubric `...92c4`.
- **LENS 4** — strict midpoint **35–42**, realistic **43–56**, observed avg **53**. Same band as round 1 (THIN at 50+ strict bar; PASS at 40 floor with observed-trajectory support). Two new rubrics add incentive to populate vault `content_b64` more thoroughly without adding tool calls — slight upward pressure on the realistic centroid (+0 to +1).
- **LENS 5** — clean: persona-recanting framing preserved through R-NEW2 (USD-cash in vault); L25 anchor-trap on R12 unchanged; no process rubrics; zero tool-name leaks; zero em-dashes; zero `at least N`; zero internal IDs in prompt; channel-of-delivery locks anchored in prompt.

**Soft caveat acknowledged (NOT a finding per user instruction):** F3 stripping introduces strict-match rigidity on `$617.63` / `$3.42` / `$42`. Real false-negative risk in practice is **bounded by the `(or similar)` qualifier already present at end of every affected title and evidence field**, which gives the judge prose latitude. Risk classification per figure: $617.63 = LOW-MEDIUM (agents may round to $617 or $618; judge discretion under `(or similar)` covers it), $3.42 = LOW (small amount, agents preserve cents), $42 = LOW (verbatim thread token, agents reproduce). See OBS A below.

REVISE NOT triggered. REBUILD NOT triggered. **PASS (STRICT)** on round 2.

---

## LENS 1 — Strict QC scoring (confirm 5/5 across all sub-dims)

### Round-1 → round-2 delta on the three sub-dims that scored below 5

| Sub-dim | Round 1 | Round 2 | Fix verified |
|---|:-:|:-:|---|
| **Overall Rubric Quality** | **4/5** (5/22 rubrics with `approximately` near exact static $ figures = 22.7%, crossed QC ">20% Minor = FAIL" threshold) | **5/5** | F3 applied. String-scan: zero `approximately $` hits over `7_Rubrics.json` titles. The one remaining `approximately mid-June 2026` in R11 is a **calculated deadline derived from FP-2026-05 cert lock**, allowed under `Strict_Convention_Inventory.json` `approximately.use_for: [calculated aggregates, ..., derived percentages]`. |
| **Completeness vs prompt asks** | **3/5** (vault surface skipped OE 20(a) FP-2025-11 refutation and OE 20(c) USD-cash gotcha) | **5/5** | F1 + F2 applied. Vault surface now carries R1 (upload metadata) + R2 (precedent identification) + R-NEW1 `...92c4` (FP-2025-11 refutation) + R3a + R3b (evidence mismatches) + R-NEW2 `...03e6` (USD-cash gotcha) = 6 rubrics symmetric with email surface (R6 + R7 + R8 + R9a + R9b + R10) and final response (R13 + R14 + R15 + R16 + R17 + R18 + R19 + R20). |
| **Qualifier placement** | **4/5** | **5/5** | F3 applied. `(or similar)` placements unchanged (end-of-sentence prose relaxation, judge-latitude-only, not value-relaxation). |

### Full sub-dim matrix on 24-rubric set

| Sub-dim | Score | Reason |
|---|:-:|---|
| Overall Rubric Quality | **5/5** | 0/24 `approximately` near exact statics; 0/24 tool-name leaks; 0/24 em-dashes; 0/24 `at least N` |
| All-Failing Rubrics | **5/5** | N/A at S3 stage |
| Rubric Category Balance | **5/5** | 24/24 outcome, 0 process; outcome >> process |
| Process Rubrics | **5/5** | 0 process; three-condition test passes vacuously |
| Agent-Centric Phrasing | **5/5** | All 24 titles open "The Agent ..." or "The Agent's <artifact> ..."; service-level prose only |
| Self-containment | **5/5** | All concrete values embedded in titles |
| Atomicity | **5/5** | Allowed bundling (same tool call / same record) where used; per-row splits maintained (R3a/R3b/R9a/R9b/R18/R19) |
| Grounding | **5/5** | All values verifiable per Council A re-verification; $617.63 + $3.42 confirmed in `_aux/Fact_Ledger.json` |
| Completeness vs prompt asks | **5/5** | Symmetric across all 3 write surfaces + final response after F1 + F2 |
| Qualifier placement | **5/5** | 0 `approximately $` titles; `(or similar)` placed at end of every title where used |
| Tool-name leakage in titles | **5/5** | Zero hits |
| Em-dashes / en-dashes | **5/5** | Zero hits |
| Internal IDs in prompt (downstream check) | **5/5 (intentional in rubrics; clean in prompt)** | IDs in rubric titles required for self-containment; prompt confirmed clean |
| L25 anchor-trap framing on R12 | **5/5** | Unchanged from round 1; both existing reminder IDs named, framing distinct |
| Implicit-prompt framing (L24/L29: Ben recanting, not contradiction-hunt) | **5/5** | Preserved; R-NEW2 phrases "the recon's FX-revaluation explanation cannot apply on principle" (mirrors R10/R20) — never accuses persona explicitly |

**All sub-dims at 5/5. LENS 1 verdict: PASS (STRICT).**

---

## LENS 2 — Answer-leakage sweep (brief; v1 finding carried)

The two new rubrics (R-NEW1 vault FP-2025-11 + R-NEW2 vault USD-cash) are **agent-output content checks on the vault `content_b64` parameter**, not changes to the prompt or any agent-readable source artifact. The prompt is unchanged; the OE list is unchanged; the agent-readable artifacts (Slack thread `1780147500.000000`, the two disposition emails, the messaging conversation, the two RV docs `doc_01b7c6e1cbe94529` / `doc_b3633a2899a04e9e`) are unchanged. The discriminating figures `$617.63` and `$3.42` continue to appear only in rubric titles + OE bodies + Fact_Ledger (allowed per AGENTS.md rule 7).

Re-verified: no leakage delta between round 1 and round 2.

**LENS 2 verdict: CLEAN.** Zero leakage hits across prompt, source artifacts, arithmetic neighbors.

---

## LENS 3 — Hardness end-to-end trace (re-trace through 24-rubric set)

Per `_aux/Hardness_Plan.md` Selected Levers: P1 + P2 + P7 + P8 + P9 + L9-overlay.

| Lever | Prompt sentence (surfacing) | OE step exercising | Rubric criteria (24-set) | Trace |
|---|---|---|---|:-:|
| **P1 latching** | "a precedent someone cited in the channel and on the supporting evidence stapled to the recon" + "Take the precedent claim from where it was raised" | OE 6, OE 7, OE 8, OE 9 | R4 (thread reply target C005 / 1780147500.000000) + R5 (thread reply references exc_aade06f6129e43 + BL-333FF9956BC6) + R8 (refutes thread $42 vs BL-8DCA6908E272 record) + R14 (final response contrasts $617.63 vs $42 thread claim) | **PASS** |
| **P2 structured-DB skip (blackline_evidence → RV)** | "Do the same on the supporting evidence the recon is leaning on. Read what each piece is labelled as. Then open the underlying documents..." | OE 15, OE 16, OE 17 | R3a + R3b (vault) + R9a + R9b (email) + R18 + R19 (final response) — **6 per-row rubrics across 3 surfaces, symmetric** | **PASS** |
| **P7 multi-write diversification** | "drop a write-up... into the vault" + "Drop a short note into the channel" + "send George a direct line" + "Set me a reminder" | OE 20, OE 21, OE 22, OE 23 | R1 (vault) + R4 (Slack) + R6 (email) + R11 (reminder) — 4 surfaces | **PASS** |
| **P8 multi-link chain (LOAD-BEARING precedent dig)** | "Pull the record for the period that was named and lay it next to the claim. If that period is not the closest fit... tell me which recent prior-period record on this account is the closer fit" | OE 10, OE 11, OE 12, OE 13, OE 14 | **VAULT:** R2 (precedent identification) + **R-NEW1 `...92c4` (FP-2025-11 refutation — NEW)**. **EMAIL:** R7 + R8. **FINAL RESPONSE:** R13 + R14 + R15 + R16 + R17. — 9 rubrics across 3 surfaces, **now symmetric** | **PASS** (strengthened — vault gap closed by F2) |
| **P9 universe-grounded gotcha (USD-cash → no FX)** | "I want to re-check both pieces against what is actually there" + "If the contents do not back the cause the recon is asserting, say so plainly." | OE 4, OE 20(c), OE 22(4), OE 24(b) | **VAULT:** **R-NEW2 `...03e6` (USD-cash — NEW)**. **EMAIL:** R10. **FINAL RESPONSE:** R20. — **3 rubrics across 3 surfaces, now symmetric** | **PASS** (vault gap closed by F1) |
| **L9 authority-dismissal overlay** | persona-named "George" + soft directives "send George a direct line letting him know what the records actually show on each piece, so he has it before he takes the disposition" | OE 7 (George), OE 8 (Daniel + Hannah), OE 9 (Ryan), OE 5 (Blue), OE 3 (Ben's own variance_explanation) | R13–R17 (four-pillar refutation grounded in records); 5-way cluster implicit through record-vs-thread contrast, not explicitly named | **PASS** |

### Round-1 vs round-2 P8 / P9 trace delta

| Lever | Round 1 — vault | Round 1 — email | Round 1 — final | Round 2 — vault | Round 2 — email | Round 2 — final |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| P8 precedent identification | R2 ✓ | R7 ✓ | R13 ✓ | R2 ✓ | R7 ✓ | R13 ✓ |
| P8 FP-2025-11 refutation | **MISSING** | R8 ✓ | R17 ✓ | **R-NEW1 ✓** | R8 ✓ | R17 ✓ |
| P9 USD-cash gotcha | **MISSING** | R10 ✓ | R20 ✓ | **R-NEW2 ✓** | R10 ✓ | R20 ✓ |

**Both vault gaps closed.** All 6 levers now trace through every output surface that the prompt + OE require.

**LENS 3 verdict: PASS (STRICT).** 6/6 levers trace end-to-end. No HARDNESS_REGRESSION.

---

## LENS 4 — Strict density projection (re-project after F1 + F2)

### Did the two new rubrics push the centroid up?

**Net effect on strict-min count:** **0 calls**. Both new rubrics check content inside the same `records_vault_upload_document` call as R1 + R2 + R3a + R3b. No new tool calls required to satisfy F1 + F2 — the agent already has to read `oracle_gl_get_account 102000` (OE 4) for R10/R20, and already has to read `BL-8DCA6908E272` (OE 10) for R8/R17. The new vault rubrics simply require those facts to also travel into the `content_b64` payload.

**Net effect on realistic centroid:** **+0 to +1 call**. F1 + F2 sharpen the reward gradient for fully chasing the USD-cash check + the FP-2025-11 record before drafting the vault upload, but don't add discrete tool calls. The vault upload payload gets denser, which moderately incentivizes agents to re-fetch fact sources (e.g., re-confirm `account_name` from `oracle_gl_get_account` if the first call's result was paginated out) — pushing centroid up by maybe +1.

### Strict midpoint re-projection

| Block | Calls (round 1) | Calls (round 2) | Note |
|---|:-:|:-:|---|
| Base discovery (contacts × 2 + period + open recon + open exception + USD-cash account) | 6 | 6 | unchanged |
| P1 latching (Slack thread + emails + messaging) | 7 | 7 | unchanged |
| P2 evidence chase (`blackline_show_data` + 2 × `records_vault_get_document`) | 3 | 3 | unchanged |
| P8 precedent dig (BL-8DCA6908E272 + run_9e4afe5f93d549 + `list_exceptions` filtered + `exc_d8fc13aa2cc742` + BL-782A2EC69343) | 7 | 7 | unchanged |
| `reminder_get_all_reminders` (R12 anti-anchor) | 1 | 1 | unchanged |
| Writes × 4 | 4 | 4 | unchanged |
| Pagination buffer | 2–4 | 2–4 | unchanged |
| Cross-service buffer | 4–6 | 4–6 | unchanged |
| **Strict midpoint TOTAL** | **35–41** | **35–42** | +0 to +1 from vault-content thoroughness incentive |
| Realistic midpoint | **42–55** | **43–56** | +1 |
| Observed avg (per `_aux/Trajectory_Stats.json`) | **53** | **53** | unchanged baseline; no re-run |

### Verdict

**Strict midpoint 35–42:** below the 50+ strict bar; **THIN at 40–49 band; lower bound dips slightly below 40 floor under most-strict minimization**. Realistic midpoint 43–56 supports PASS at 40 floor and approaches 50+ bar. Observed avg 53 confirms PASS at 50+ in practice. Same band as round 1 — no fresh blocker introduced; no regression.

This is the same disposition accepted as PASS (STRICT) at AUDIT_prompt and AUDIT_oe. The rubric phase doesn't drive trajectory shape directly; it incentivizes coverage. Carrying forward as **OBS B** unchanged from round 1.

**LENS 4 verdict: THIN at 50+ strict bar; PASS at 40 floor with observed-trajectory support.** Not a fresh blocker.

---

## LENS 5 — Adversarial veteran review (re-check key items)

| Check | Status | Detail |
|---|:-:|---|
| Implicit-prompt framing preserved on R-NEW2 (USD-cash vault) — Ben recanting his own variance_explanation | **PASS** | R-NEW2 phrases "the recon's FX-revaluation explanation cannot apply on principle" — identical pattern to R10 + R20, not explicit accusation. The recon's variance_explanation was Ben's authored, but the rubric uses "the recon's" indirection. L24/L29 holds. |
| L25 anchor-trap (R12 unchanged) | **PASS** | unchanged |
| Silent process rubrics on new vault rubrics | **PASS** | R-NEW1 and R-NEW2 both verify content of the `content_b64` parameter (Outcome 1.2). Not process. |
| Tool-name leaks in 2 new rubric titles | **PASS** | Service-level prose only ("Records Vault write-up", "the recon's FX-revaluation explanation"). |
| Em-dashes in 2 new rubrics | **PASS** | Zero hits. |
| `at least N` in 2 new rubrics | **PASS** | Zero hits. |
| `(or similar)` placement on 2 new rubrics | **PASS** | End-of-sentence prose relaxation; matches pattern across all 24. |
| F3 strict-match rigidity — false-negative risk in practice | **OBS A (see below)** | Bounded by `(or similar)` at end of titles + evidence fields. |

### OBS A — F3 strict-match rigidity assessment

Per user instruction: flag if real false-negative risk in practice; do not REVISE on it.

**Risk classification per figure:**

| Figure | Strict-match risk if agent rounds | Mitigation via `(or similar)` | Net risk |
|---|---|---|---|
| `$617.63` (R2, R7, R14 titles; R2, R7 evidence) | MEDIUM — agent might naturally report "approximately $617" or "$618" instead of `$617.63` | `(or similar)` end-of-title clauses give judge latitude on prose surrounding the figure. Judge can accept "$617" / "$618" / "approximately $617" as describing the same record. | **LOW–MEDIUM** |
| `$3.42` (R8, R17 titles; R8 evidence) | LOW — small variance amounts agents typically preserve to the cent | `(or similar)` covers prose. Agents reporting "approximately $3" instead of "$3.42" would be wrong-grain (the precedent contrast loses force at "approximately $3"). | **LOW** |
| `$42` (R14 title) | LOW — verbatim text from George's Slack message ts `1780152480.000000`; agents reproducing the thread typically quote it verbatim | `(or similar)` covers prose; agents could say "the $42 figure" or "$42 as the thread claimed", all match-equivalent. | **LOW** |

**Net assessment:** The strict-match rigidity is real but bounded by the `(or similar)` qualifier at end of every affected title and evidence field. Judge latitude under `(or similar)` covers reasonable rounding variants. The bigger risk than rounding is wholesale-omission (agent fails to surface the figure at all) — and stripping `approximately` arguably tightens this signal correctly (agent must actually surface the discriminating number, not gesture at "approximately a few hundred dollars").

**No REVISE on OBS A.** Recommend carrying forward to FINAL for re-confirmation against fresh trajectories. If FINAL or post-platform reviewers flag false-negatives on R2/R7/R14 due to agent rounding, the fix is to re-add `approximately` with explicit justification documenting the boundary call — round-3 reversal is a fix-in-place.

### Other observations

**OBS B (carried from round 1) — Density THIN at 50+ strict midpoint.** Strict 35–42, realistic 43–56, observed avg 53. Same disposition as prior AUDIT_prompt and AUDIT_oe. Not a fresh blocker. Re-confirm at FINAL.

**OBS C — Round-2 fixes did not introduce any new symbol families.** F1 + F2 + F3 used existing record IDs, amounts, account labels, and titles already grounded by Council A. Validator re-run not strictly necessary for grounding (no new universe atoms), but worth running for em-dash + tool-name + word-count + JSON-schema verification on the 2 inserted rubrics.

---

## VERDICT SYNTHESIS

| Lens | Round 1 | Round 2 |
|---|---|---|
| LENS 1 — Strict QC scoring | 3 sub-dims < 5 (Overall Rubric Quality 4/5, Qualifier placement 4/5, Completeness 3/5) | **All sub-dims 5/5** |
| LENS 2 — Answer-leakage sweep | CLEAN | CLEAN (unchanged) |
| LENS 3 — Hardness end-to-end trace | 5/6 PASS; P9 FAIL at vault | **6/6 PASS** (P9 vault gap closed via R-NEW2; P8 vault FP-2025-11 gap closed via R-NEW1) |
| LENS 4 — Strict density projection | THIN at 50+; PASS at 40 floor (35–41 strict, 42–55 realistic, 53 observed) | **THIN at 50+; PASS at 40 floor** (35–42 strict, 43–56 realistic, 53 observed; +0 to +1 centroid pressure) |
| LENS 5 — Adversarial veteran review | 3 STRICT FAILs (`approximately` × 5, USD vault, FP-2025-11 vault) | **CLEAN** (3 round-1 findings resolved); OBS A on F3 strict-match rigidity carried forward, bounded by `(or similar)` |

**Blocker hits:** 0
**Lens-1 sub-dims below 5:** 0
**Untraced levers:** 0
**Density below 40 floor:** No (mid-band PASS at 40; THIN at 50+ with observed-trajectory support)
**New BLOCKER not in v1 findings:** **NONE**

---

## VERDICT: PASS (STRICT)

All three round-1 findings are resolved. The 24-rubric set clears every applicable QC sub-dim at 5/5 under strictest reading. All 6 hardness levers trace end-to-end across all 3 write surfaces + final response. Answer-leakage sweep is CLEAN. Density THIN at 50+ strict bar but PASS at 40 floor with observed-trajectory support (same band as prior AUDIT_prompt and AUDIT_oe).

**Producer phase closes. S3 deliverable is shippable to FINAL.**

---

## Forward-looking observations (carry into FINAL)

**OBS A — F3 strict-match rigidity bounded by `(or similar)`.** Stripping `approximately` from R2/R7/R8/R14/R17 introduces strict-match rigidity on $617.63 / $3.42 / $42. Risk in practice is LOW–MEDIUM, bounded by `(or similar)` qualifier giving judge prose latitude. Re-confirm against fresh trajectories at FINAL. If platform reviewers flag false-negatives, re-add `approximately` with explicit justification.

**OBS B — Density THIN at 50+ strict midpoint.** Carried forward unchanged from round 1 and prior phase audits. Strict 35–42, realistic 43–56, observed avg 53. Not a blocker.

**OBS C — Vault surface symmetry now complete.** Vault rubric set carries 6 rubrics symmetric with email (6) and final response (8). Future similar tasks should run a coverage matrix against OE write-action sub-parts at S3 drafting time to catch latent asymmetries before audit. Council A and Council B both missed the round-1 vault gap because they evaluated each rubric in isolation rather than as a cross-surface matrix.

**OBS D — Validator re-run optional but recommended.** F1 + F2 + F3 reused existing universe atoms; no new groundedness exposure. JSON-schema + em-dash + word-count sweep on the 2 inserted rubrics is recommended as a sanity check before FINAL.

---

## Exit criteria (verified, round 2)

- [x] All 24 rubrics scanned under strictest reading
- [x] Round-1 F1 applied: vault USD-cash gotcha rubric inserted, mirrors R10 / R20
- [x] Round-1 F2 applied: vault FP-2025-11 record refutation rubric inserted, mirrors R8 / R17
- [x] Round-1 F3 applied: zero `approximately $` hits in titles or evidence parameters across all 24 rubrics
- [x] Universe re-grounding: no new symbol families introduced; existing Council A grounding holds
- [x] Answer-leakage sweep: CLEAN
- [x] Six-lever trace: 6/6 PASS across all 3 write surfaces
- [x] Density projection: PASS at 40 floor; THIN at 50+ strict bar with observed-trajectory support
- [x] Adversarial pattern recognition: no new BLOCKERs surfaced
- [x] Round 2 within REVISE iteration cap (cap = 3, this is round 2)
- [x] **PASS (STRICT) on round 2** — exit criterion MET

Producer phase closes. Proceed to **FINAL** in a fresh chat with `PIPELINE FINAL — Tasks/27_6a39fd19048f9213281ec7b`.
