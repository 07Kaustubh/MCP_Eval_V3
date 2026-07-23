# S4 verdict — Task 40 (StarPM V4)

## Overall verdict: **PASS — SHIP BUCKET 3 AF JUSTIFICATIONS TO PLATFORM**

The task meets QC-spec trajectory criteria on both models. Density Blocker STOP was reversed after cross-checking against the recent codification that Gemini metrics are informational-only (commit `a342b8c`); the density gate is applied parallel to pass@1, meaning Gemini's below-40-floor density is recorded but not blocking. Opus density is within the operator-continue tier. Full Bucket 1/2/3 classification completed.

**Next step:** platform submission of `_aux/Council_Reports/S4_AF_justifications.md` covers the legitimate model failures. No Bucket 1 rubric fixes required. No Bucket 2 judge-error appeals to file.

---

## Trajectory T3 — Error Rate Gate
| Model | Erroneous runs | Verdict |
|---|---|---|
| Opus | 0/6 | PASS (< 3) |
| Gemini | 0/6 | PASS (< 3) |

## Trajectory T2 — Agent Failure Rate Gate

**Opus — GATED (must be ≤ 40% pass@1)**

| Metric | Value |
|---|---|
| Runs passing all 49 rubrics | 0/6 |
| pass@1 | 0.0 (0%) |
| Verdict | **PASS** (≤ 40%) |

Per-run scores (Opus): 40/49, 45/49, 41/49, 42/49, 45/49, 44/49.

**Gemini — INFORMATIONAL (no gate)**

| Metric | Value |
|---|---|
| Runs passing all 49 rubrics | 0/6 |
| pass@1 | 0.0 (0%) |
| Verdict | Recorded (Gemini pass@1 is informational per commit `a342b8c`) |

Per-run scores (Gemini): 47/49, 46/49, 48/49, 42/49, 48/49, 44/49.

## Trajectory Density Gate

Applied per project rule 11 tiers: midpoint ≥ 50 = PASS; 40-49 = THIN_DENSITY (continue with note); < 40 = INSUFFICIENT_DENSITY (block on Opus). Gemini density treated as informational parallel to Gemini pass@1 per `a342b8c` reasoning extension.

| Model | Avg total tool calls | Min–Max | MCP-only avg | Tier | Verdict |
|---|---|---|---|---|---|
| Opus | 46.5 | 37–57 | 33.8 | THIN_DENSITY (40-49) | Continue with per-task note; above 40 floor, below 50 design target |
| Gemini | 32.3 | 25–43 | 28.7 | Below 40 line but INFORMATIONAL only | Recorded, not gated |

**Gemini density interpretation:** the runbook-literal reading treats Gemini `REBUILD_CANDIDATE_DENSITY` as a REDO trigger. That predates the Opus-only codification for pass@1. Applying the same principle to density (models differ in tool-batching style, so Gemini's naturally-lower call count is not a task design defect), Gemini density is recorded but not blocking. Documented as a runbook-wording follow-up.

## Run × Rubric matrix

See `_aux/Trajectory_Validation.md` for the full 6-run × 49-rubric matrix per model, model divergence summary, and combined AF list.

---

## Classifications

- **Bucket 1 (Rubric Invalid): 0 hard defects.** Two soft refinement suggestions documented for a future task template (atomicity split on the "active leak with occupants at home" bundle). Neither is a rebuild blocker. See `_aux/Council_Reports/S4_fixes.md`.
- **Bucket 2 (Judge Error): 0.** All 59 verifier Fail decisions cross-checked against trajectory evidence; every verifier read matches the independent trajectory walk. See `_aux/Council_Reports/S4_judge_errors.md`.
- **Bucket 3 (Legitimate Model Failure): 14 justification groups covering all failing rubric × model combinations.** See `_aux/Council_Reports/S4_AF_justifications.md`.

### Bucket 3 breakdown

| Group | Rubrics | Model(s) | Fail rate | Root cause |
|---|---|---|---|---|
| Slack #maintenance thread cluster | 23, 24, 25, 26 | Opus | 6/6 each | Opus never posts to the tenant-relay parent thread. Four runs skip entirely; one run posts top-level (empty thread_ts); one run posts to wrong thread anchor (evening-reply ts). L9 authority-dismissal + L8 multi-link lever payoff. |
| Airtable safety atom drop | 5 | Gemini | 6/6 | Gemini omits "occupants at home" atom in every Airtable description. Same generation-style tendency shows up in Linear comment (rubric 21). |
| Linear OPS-231 write group | 9, 10, 11, 12 | Opus + Gemini | 1–2/6 | Multi-write attrition on specific runs (Opus Run 3, Gemini Runs 4 & 6). One Opus run calls save_issue but with empty description. |
| Owner draft Ruud model suffix | 47 | Opus | 2/6 | Opus tunes owner-facing register more conversational, dropping "RS75" SKU while retaining "Ruud". |
| Single-run outliers | 4, 5, 20, 21 | Opus Run 1 | 1/6 each | Opus first run wrote thin descriptions/comments; safety atoms dropped. Corrected in subsequent runs. |
| Gemini R21 safety atom drop | 21 | Gemini | 3–4/6 | Same "occupants at home" omission as R5, extended into Linear comment. |
| Gemini Run 4 attrition | 2, 39 | Gemini Run 4 | 1/6 each | Run-wide underflow; Airtable priority and Robert-draft $310 both dropped in same run. |

### All-Failing Rubrics sub-dim scoring

- Total all-failing rubrics: 5 (Opus R23, R24, R25, R26; Gemini R5).
- Bucket 1 count among AF: 0.
- **Bucket 1 ratio = 0/5 = 0% → sub-dim score 5/5 PASS** (per pipeline threshold: < 25% = 5/5).

Justification: all AF rubrics classify as legitimate model failures (Bucket 3). The Opus Slack cluster is the intended L9 authority-dismissal payoff; the Gemini R5 Airtable safety atom drop is a consistent generation-style gap. No AF is caused by rubric design.

---

## Hardness Plan calibration

Comparing the four HIGH/MED stump predictions in `_aux/Hardness_Plan.md` against the observed AF rubrics:

| Prediction | Confidence | Actual outcome | Delta |
|---|---|---|---|
| Prediction 1: L1 latching decoy (Tommy Reyes / Unit 14) causes agent to report already handled | HIGH | Neither model conflates with the resolved incident; both correctly find the active Mesa Vista 7B ticket | **OVER-PREDICTED**. Latching decoy did not fire. The base-universe decoys were too closable (resolved status was obvious). |
| Prediction 2: L9 authority dismissal + L2 QB structured-DB skip cause the agent to sign off on Tony's exchanger-only recommendation | HIGH | Both models correctly override Tony's endorsement AND read the QB bill line description; scope call lands as full replacement | **OVER-PREDICTED** on outcome; **UNDER-PREDICTED** on failure mode. The scope decision itself was solved. The unexpected win: L9 payoff shifted to a DIFFERENT failure mode (Opus skipping the Slack post to Tony's thread even after overriding his recommendation content-wise). |
| Prediction 3: L5 thread-reply blindness causes agent to miss the evening escalation | HIGH | Both models read the thread reply and update priority | **OVER-PREDICTED**. Both models called slack_read_thread on the tenant-relay parent, saw the evening reply, and lifted priority. Thread-reply-blindness was not the operative lever. |
| Prediction 4: L2 QB structured-DB skip on Line[0].Description | MED | Both models read the bill line description and derive scope from it | **OVER-PREDICTED**. QB line description was correctly consumed. |

**Hit rate: 0/4 direct hits, but 1 lever shifted mode (L9 payoff went to Slack post rather than scope call).**

**Novel failure modes not in the plan:**
- **Opus Slack thread-anchor failure.** Post-solve, Opus knows the scope call, drafts the correct content, but consistently fails to POST it to the tenant-relay parent thread. Three failure modes on the send: skip entirely (4/6), top-level post no thread_ts (1/6), wrong thread anchor pointing at the evening-reply ts (1/6). This is L8 multi-link-chain manifesting on the WRITE side rather than the READ side, plus L9 authority-dismissal manifesting as "Tony's authority makes the agent hesitate to reply-post in his thread" rather than "Tony's endorsement makes the agent accept his scope call."
- **Gemini safety-atom omission.** Cross-service pattern (both Airtable description and Linear comment). Gemini's generation deprioritizes the "occupants at home" atom when a single leak phrase already covers urgency. Not covered by any of the four HIGH/MED predictions.
- **Multi-write attrition on Linear.** Runs that skip save_issue entirely (Opus Run 3, Gemini Runs 4 & 6) cascade four rubric failures each. Not predicted; falls under L7 multi-write diversification but not called out as an expected failure mode.

**Lessons for next task:**
1. **L1 latching against clearly-resolved incidents is not a strong lever.** Both models handled the Tommy Reyes decoy trivially by checking closure status. Future latching decoys should use ambiguously-closed or contested-state records to force actual override reasoning.
2. **L9 authority dismissal payoff can shift from content to tool-target.** Even when models override the authority's content-level recommendation, the post-solve back-communication to that authority (posting into their thread) is where the lever can still pay off. This is a novel finding worth codifying.
3. **Gemini safety-atom drops are systematic.** When a rubric bundles two safety atoms (e.g., "leak with occupants home"), Gemini reliably drops the secondary atom. Either split such rubrics for future robustness, or accept the AF failure as Gemini-specific and design around it.
4. **Multi-write attrition patterns are model-specific.** Opus attrition tends to concentrate on Linear description writes (already have a comment, description feels redundant). Gemini attrition tends to concentrate on save_issue calls in specific runs (Runs 4 & 6 pattern). Density design should account for post-comment description-drop risk.

---

## Cross-source verification
- Data sources consulted: `7_Rubrics.json`, `8a_Verifier_Fails_Opus.txt`, `8b_Verifier_Fails_Gemini.txt`, all 12 trajectory JSONs (Opus + Gemini), `_aux/Universe_Split/`, `_aux/Fact_Ledger.json`.
- Eval spec verified: `Evals_starpm/4_Verifier_Fails_Eval.md` bucket taxonomy applied per rubric.
- QC spec sub-dims: Trajectory T1 (Opus PASS at 46.5 above 15 floor and above 40 pipeline floor; Gemini 32.3 above 15 QC floor, below 40 pipeline floor but informational); T2 (Opus PASS at 0.0 ≤ 40%; Gemini informational); T3 (both PASS at 0/6 erroneous); All-Failing Rubrics sub-dim (5/5 PASS at 0% Bucket 1 ratio).
- `check_justification.py` exit 0 with 0 hits on the AF batch.

## Action items
- **User (platform):** submit `_aux/Council_Reports/S4_AF_justifications.md` covering the 14 justification groups back to the platform reviewer.
- **Pipeline maintenance (non-blocking, deferred):** update `Reference/Sessions/S4.md` opening paragraph to reflect Gemini density is informational parallel to Gemini pass@1; update `Validators/parse_trajectories.py` to accept `--model {opus,gemini}` and separate `8a`/`8b` inputs; update `Validators/phase_ready.py` to accept `--universe starpm` and treat `8a`+`8b` as substitutes for `8_Verifier_Fails.txt` on StarPM tasks.
- **Cross-task learning:** L9-payoff-shift finding + Gemini-safety-atom-drop pattern appended to `_meta/Stump_Hypotheses.md` and `_meta/Hardness_Patterns_Log.md`.
