# Verifier Fails — S4 verdict · Task 43_6a62ccaf5853030245ac9d53

**Universe:** StarPM V4 · **Persona:** Carlos Mendez, Onsite Property Manager · **Models:** Opus 4.8 (6 runs) + Gemini 3.6 Flash (6 runs) · **Date:** 2026-07-25

**Headline: PASS on every trajectory gate. 0 rubric changes required. Ship the AF batch.**

---

## Trajectory T3 — Error Rate

Erroneous runs: **0/12** (Opus 0/6, Gemini 0/6). Every run completed to a verifier-evaluable state and every run produced a full 25-row grading block in `8a`/`8b`.
**Verdict: PASS (< 3).**

## Trajectory T2 — Agent Failure Rate

| Model | Runs passing ALL valid rubrics | Completed | pass@1 |
|---|---:|---:|---:|
| Opus 4.8 | 0 | 6 | **0.0%** |
| Gemini 3.6 Flash | 0 | 6 | **0.0%** |
| Combined | 0 | 12 | **0.0%** |

Best single run was Opus at 16/25. Worst was Gemini Run 3 at 11/25.
**Verdict: PASS (0.0% ≤ 40%), per model and combined.**

## Trajectory T1 — Density (StarPM scheme: 40 design target, 15 fail floor, per model)

| Model | Runs | Avg total calls | Avg MCP calls | Min run | Max run | Verdict |
|---|---:|---:|---:|---:|---:|---|
| Opus 4.8 | 6 | **41.7** | 27.2 | 31 | 56 | **PASS** (≥ 40 design target) |
| Gemini 3.6 Flash | 6 | **36.8** | 28.5 | 34 | 42 | **THIN** (15-39 band), clear of the 15 fail floor |
| Combined | 12 | 39.2 | 27.8 | 31 | 56 | PASS vs fail floor |

The FINAL-phase projection was Opus ~45 / Gemini ~36. Measured: Opus 41.7 / Gemini 36.8. The Gemini projection was accurate to within 1 call; the Opus projection was 3 calls optimistic.

The FINAL watch-item was "if the first Gemini run lands < 30, the OE needs another grounded write before any re-upload." Lowest Gemini run was **34**. **Not triggered.** The 4-write / 4-service mitigation (invoice update, Airtable record update, email draft, Slack post) executed on all 12 runs and did the work it was accepted to do.

---

## Run matrix (25 rubrics × 12 runs)

`P` pass · `F` fail · bold rows fail every run.

| # | Criterion (abbrev) | Opus 1-6 | Gemini 1-6 | Fails |
|---|---|---|---|---:|
| 1 | **reports $1,812 corrected pass-through** | `FFFFFF` | `FFFFFF` | **12** |
| 2 | reports $1,622 does not line up | `PPPPPP` | `PPPPPP` | 0 |
| 3 | identifies repaint on vendor bill as $1,340 | `PPPPPP` | `PPPPPP` | 0 |
| 4 | identifies closet trim on vendor bill as $85 | `PFFPPP` | `FFFFFF` | 8 |
| 5 | identifies deep clean as the one matching line | `PPPPPP` | `PPPPPP` | 0 |
| 6 | **reports net understatement as $190** | `FFFFFF` | `FFFFFF` | **12** |
| 7 | excludes $85 Alamo condition walk as in-house | `PPPPPP` | `PPFFFP` | 3 |
| 8 | **keeps $85 closet trim as outside vendor work** | `FFFFFF` | `FFFFFF` | **12** |
| 9 | updates existing invoice 2026-534 | `PPPPPP` | `PPPPPP` | 0 |
| 10 | **corrects invoice 2026-534 to total $1,812** | `FFFFFF` | `FFFFFF` | **12** |
| 11 | raises repaint line $1,140 → $1,340 | `PPPPPP` | `PPPPPP` | 0 |
| 12 | **lowers closet trim line $95 → $85** | `FFFFFF` | `FFFFFF` | **12** |
| 13 | keeps deep clean line at $387 | `PPPPPP` | `PPPPPP` | 0 |
| 14 | does not create a second owner invoice | `PPPPPP` | `PPPPPP` | 0 |
| 15 | updates the Ready-status make-ready record | `PPPPPP`\* | `PPFPPP` | 1 (Gemini 3) |
| 16 | **make-ready record states final owner cost $1,812** | `FFFFFF` | `FFFFFF` | **12** |
| 17 | make-ready record states turn closed owner-side | `PPPPPP`\* | `PPFPPP` | 1 (Gemini 3) |
| 18 | drafts email to linda.castillo@gmail.com | `PPPPPP` | `PPPPPP` | 0 |
| 19 | **email states invoice corrected to $1,812** | `FFFFFF` | `FFFFFF` | **12** |
| 20 | email states repaint was $1,340 | `PPPPPP` | `PPPPPP` | 0 |
| 21 | **email states corrected figure is $190 more** | `FFFFFF` | `FFFFFF` | **12** |
| 22 | email states 4C now closed on her side | `FFFPPP` | `FPFPPF` | 6 |
| 23 | posts corrected cost in a team channel | `PPPPPP` | `PPPPPP` | 0 |
| 24 | **channel message states pass-through corrected to $1,812** | `FFFFFF` | `FFFFFF` | **12** |
| 25 | channel message states supersession | `PPPPPP` | `PPPPPF` | 1 |

\* Rows 15 and 17: Opus Runs 2 and 4 wrote **only** to the stale In Progress row `recbd087a4abd605b` and were passed anyway. Gemini Run 3 did the identical thing and was failed. True pass counts are 9/12 and 9/12, not 11/12 and 11/12. See `S4_judge_errors.md` section B.

**Totals:** 15 of 25 rubrics failed at least once. 9 failed all twelve runs. 10 rubrics were never missed by any run.

---

## Classifications

- **Bucket 1 (rubric invalid): 0 rubrics.** Two candidates examined and rejected with reasoning on record → `S4_fixes.md`.
- **Bucket 2 (judge error): 0 rubrics, 6 run-cells.** 2 wrong-FAIL (appealable), 4 wrong-PASS (recorded for matrix integrity) → `S4_judge_errors.md`.
- **Bucket 3 (legitimate model failure): 15 rubrics** → `S4_AF_justifications.md`. Voice gate `check_justification.py` exit 0.

Every classification carries a trajectory citation. The v15 5-point checklist was answered YES on all five before each AF justification was written; the two criteria where a point came back NO on first pass are the rejected Bucket 1 candidates documented in `S4_fixes.md`.

## All-Failing Rubrics sub-dim

Bucket 1 ratio = **0 / 15 = 0.0%** → **< 25% → 5/5 (PASS).**

Nearly all failures trace to one genuine reasoning failure at a designed landmine, plus a small tail of omissions. The rubric set is sound.

---

## Root-cause analysis

**One reasoning failure produced nine of the fifteen failing rubrics.**

All twelve runs, across both model families, classified the $85 bedroom closet trim touch-up on bill `546359391323` (`DocNumber 2026-519`) as internal Star PM labor and deleted it from the owner pass-through, producing $1,727 instead of $1,812 and a net movement of $105 instead of $190. That single call propagates into the final response, the invoice header, the invoice line array, the Airtable notes, the owner email, and the Slack post, which is why nine atomic criteria fall together.

What every run had in context and did not use:

| Evidence | Points to | Runs that retrieved it | Runs that acted on it |
|---|---|---:|---:|
| `PrivateNote` opens "Internal labor charge for Tony Reyes" | in-house (wrong) | 12 | 12 |
| Slack C004 "Tony got it done today" | in-house (wrong) | 8 | 8 |
| `VendorRef.name` = "Permian Make-Ready Crew" | vendor (right) | 12 | 1 |
| Same note: "Pass-through to owner - pair with corresponding AR invoice" | vendor (right) | 12 | 0 |
| Summary email body: trim sits inside Pete Donovan's repaint scope, "Tony's team handled all internal repairs in-house" | vendor (right) | 9 | **0** |

The last row is the finding worth carrying forward. OE 7 prescribes `search_threads` then `get_thread (threadId: "66132537181ecbe1")`. Nine of twelve runs executed exactly that call. `get_thread` returns the message body in `payload.body.data`, **base64 encoded**, and the StarPM gmail surface has no `get_message` / `read_message` alternative that returns plaintext. Not one run decoded it. Gemini Run 2 ran base64 decoding on other content earlier in the same run (calls 7-12) and still left this payload encoded.

The rubric survives on `VendorRef` plus the pass-through clause alone, which is why this is Bucket 3 and not Bucket 1. But the designed corroboration was, in practice, inert.

**Concentration risk, stated plainly.** Nine rubrics rest on one contested classification. Each is individually atomic and correctly decomposed per the write-action-per-rubric rule, so this is not a bundling defect. It does mean that if a platform reviewer disputes the closet-trim ground truth, nine criteria fall at once. The counter-argument is in `S4_fixes.md` Candidate 1 and should be quoted verbatim if challenged.

---

## Hardness calibration

Stump hypothesis hit rate: **1 of 4 predictions confirmed as written, 1 confirmed after the FINAL re-attribution, 2 over-predicted.**

| # | Prediction | Outcome |
|---|---|---|
| 1 | **[HIGH, both models]** L2 structured-DB skip: agents stop at $1,622, never open the AP bills | **OVER-PREDICTED.** 0/12 stopped at $1,622. "$1,622 does not line up" passed 12/12 and "repaint is $1,340" passed 12/12. Every run reached the AP side and re-derived. |
| 2 | **[MED-HIGH, Opus]** L6 near-miss: wrong $1,340 bill from the 10-bill cluster, or bills Pete Donovan instead of Linda | **OVER-PREDICTED.** The correct invoice (12/12), correct customer (12/12) and correct repaint bill (12/12). The Pete/Linda owner decoy never landed once. |
| 3 | **[MED, Gemini-leaning, "margin item not the engine"]** L11 net-vs-gross: drops the closet $85 → $1,727, or adds the Alamo $85 → $1,897 | **HIT, and it WAS the engine.** 12/12 landed on $1,727 exactly. Predicted as a Gemini-leaning margin item; it swept both models symmetrically and produced 9 of the 15 failing rubrics. The $1,897 branch never fired; the $1,727 branch fired universally. |
| 4 | **[LOW-MED, both]** Duplicate write: creates a second owner invoice | **OVER-PREDICTED.** "Does not create a second owner invoice" passed 12/12. The negative guard was worth keeping but never triggered. |

**The FINAL council's MAJOR-1 re-attribution was correct and should be credited.** It disputed prediction 1's magnitude on the grounds that prompt sentence 3 ("Go back to what each vendor charged us ... and set it against the line items I sent her") is an L29 escape valve pointing straight at the AP side, and predicted the sweep would come from L6/L11 rather than an L2 skip. That is precisely what happened. The instruction that neutralised L2 is also the instruction that made the task solvable enough to be fair, so keeping it was the right call.

**Unpredicted mechanism that did the work.** The plan filed the twin-$85 discrimination under L6 as an Opus-asymmetric near-miss. In reality it fired symmetrically through a mechanism the plan did not name: **prose-on-record contradicting a structured field on the same record**, reinforced by a second in-universe source (Slack) and by the named person being a verifiable internal employee. This is a distinct lever from "near-miss entity" and it is the strongest symmetric stump observed on StarPM so far.

**Dual-row Airtable lever:** fired on 3 of 12 runs (Gemini 3, Opus 2, Opus 4), not the 1 of 12 the raw matrix shows, once the two wrong-PASS cells are corrected. Weaker than a flagship but live on both models.

**Lessons for the next task.** The reliable symmetric stump on this universe is not "will the agent open the structured store" (it will, and reliably) but "which of two contradicting sources inside the same record will it weight". Design the contradiction onto one record, put the misleading half first in the prose, corroborate the wrong reading from a second service, and make the resolving evidence a structured field rather than a body of text that has to be decoded. Do not rely on a Gmail body as the sole corroborator: on this tool surface it comes back base64 and agents do not decode it.

---

## Action items

1. **`7_Rubrics.json`: no changes.** Bucket 1 is empty. Ship as-is.
2. **Submit the Bucket 3 AF batch** in `S4_AF_justifications.md` to the platform. Voice gate clean (exit 0), no em-dashes, no process leakage.
3. **Optionally appeal 2 judge cells** on `rubric[3]` (Opus Runs 2 and 3) for inconsistent application of the vendor-attribution clause against Opus Runs 1, 4 and 6. Strong for Run 2, weaker for Run 3 given its fabricated line-item breakdown. Neither changes any verdict here.
4. **No re-run required.** T1, T2 and T3 all pass on both models; pass@1 is 0.0%; density clears the fail floor on both models and the design target on Opus.
5. **Expect one platform-QC challenge** on "email states 4C now closed on her side" (prompt binds closure to the Airtable record). Counter-argument is in `S4_fixes.md` Candidate 2.
6. **Task is clear to close.** Next trigger: `PIPELINE CLOSE — Tasks/43_6a62ccaf5853030245ac9d53`.
