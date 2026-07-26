# Verification — S4 (StarPM V4 dual-model)

## Data sources consulted
- 7_Rubrics.json :: 15-rubric set being classified (all Outcome)
- 8a_Verifier_Fails_Opus.txt :: Opus verifier output (6 runs)
- 8b_Verifier_Fails_Gemini.txt :: Gemini verifier output (6 runs)
- Agent_Responses/Opus/trajectory-run-{1..6}.json :: Opus trajectories walked per failing rubric (nested-content schema)
- Agent_Responses/Gemini/trajectory-run-{1..6} (1).json :: Gemini trajectories walked per failing rubric (flat tool_use schema)
- _aux/Universe_Split/airtable.airtable_records.json :: 3 make-ready rows + MT-2026-1271 re-confirmed
- _aux/Universe_Split/linear.linear_issues.json + linear.linear_comments.json :: OPS-227 title/description + 6/22 seized comment
- _aux/Fact_Ledger.json / _aux/Hardness_Plan.md :: stump-hypothesis calibration source
- 5_Prompt.txt :: every rubric traced back to a prompt ask (checklist item 3)

## Eval spec verified
- Evals_starpm/4 (Verifier Fails, dual-model) :: bucket taxonomy (Rubric Invalid / Judge Error / Legit Fail) applied once per model
- 5-point pre-write checklist applied before every AF justification
- 9/10/11 QC-dispute trio confirmed 0-byte -> qc_verdict.py parse/classify/audit N/A (no dispute stage)

## QC spec sub-dims verified
- All-Failing Rubrics sub-dim (Bucket 1 ratio) = 0% -> 5/5
- Trajectory T1 (>= 15 tool-call floor) :: Opus 43.5, Gemini 33.0 (both >= 15)
- Trajectory T2 (pass@1 <= 40%) :: 0% both models
- Trajectory T3 (<= 2 error runs) :: 0 error runs both models

## Verification statements
- [x] Trajectory walk recorded for EVERY failing rubric, per model (see _aux/S4_bucket3.md). Not just Bucket 2.
- [x] T2 + T3 hard gates evaluated and recorded per model (S4_verdict.md).
- [x] Bucket 1 ratio computed (0/11 = 0%); All-Failing Rubrics sub-dim scored 5/5.
- [x] 5-point checklist confirmed YES on all 5 before each AF justification (R2/R3/R4 and R14 explicitly stress-tested against ground truth in S4_fixes.md).
- [x] check_justification.py exit 0 on the AF batch; no em-dashes in the AF file.
- [x] Ground-truth atoms re-grepped: receb057b02f20052 (selReady stale), rec651427ec0d84dd5a (selProg, real not hallucinated), recf7aecc318b2252 (selProg), MT-2026-1271/recac236210094352 (blank completion date), OPS-227 (title "jam" overridden by 6/22 "seized/replace/parts approval" comment).
- [x] R6 all-fail and Opus-Run5-R3 spot-checked from raw trajectory params to rule out judge error (S4_judge_errors.md).

## Discrepancies surfaced
1. `parse_trajectories.py` undercounts Gemini density to 0 (flat tool_use schema not recognized); `_aux/Trajectory_Stats.json` stores the wrong Gemini figure. Corrected by hand to 33.0 avg. Non-blocking for this task (Opus 43.5 drives PASS; Gemini's true 33.0 >= 15 floor). Recommend a parser patch as a separate follow-up — NOT applied here (shared, regression-pinned validator, out of S4 scope).
2. `phase_ready.py --phase s4` exits 1 ONLY because upstream `Verification_final.md` is missing its `## Sources consulted` / `## Verdict` sections (a FINAL-phase doc-format issue). All five S4 inputs are present and `parse_trajectories.py` ran clean; this does not block S4 classification.
3. Gemini Run 6 verifier called rec651427ec0d84dd5a "hallucinated"; it exists in the universe. Sub-fact error only; the Fail verdict still stands.


## Deep re-verification pass (operator-requested — full trajectory + OE + prompt-binary + rubric-quality)

### Full trajectory read (living proof, all 12 runs)
Built a complete ordered tool-call trace for every run (Opus 6 + Gemini 6) plus the load-bearing params (OPS-227 comment bodies, every update_records payload with record IDs + fields, all C004 Slack bodies, all draft bodies, all final responses). Read boundary (honest): full call-path + load-bearing params/responses were read; raw intermediate tool-RESULT blobs were not read verbatim (not needed — result states were cross-checked against the universe directly).

**Fail-to-OE parity confirmed mechanistically:**
- Opus disposal-cluster fails (runs 1, 3) = the ONLY two Opus runs that skipped `list_comments` OPS-227 (OE 7). They read `get_issue` (the "jam" title) but never the 6/22 "seized/replace" comment. Runs 2,4,5,6 read the comment and passed the cluster.
- Gemini R2/R3/R4 fails (5/6) = updated rec651427/recac236, never the stale receb057 (OE 9's named record). Only Run 2 touched receb057 -> only Run 2 passed.
- Gemini R6 fails (6/6) = OE 11's "should not be marketed or shown" clause omitted; zero don't-show language in all 6 C004 bodies.
- R14 fails = OE 3/6 Airtable-SoR reasoning skipped; Gemini runs 3,5 backfilled a completion date onto MT-2026-1271 — the exact trap OE 9 warns against ("the agent must not mark it complete").
- R11 fails = wrong path (Opus 1,3 reset-not-replace) or missing closeout (Gemini 3,5). R15 fails (Opus 1,4) = 6/25 fridge (OE 2/3 row) left unconfirmed / over-escalated.
Every fail maps to a specific skipped OE step or a specific rubric criterion the output missed. No orphan fails; no fail that contradicts its trajectory.

### OE coverage with trajectory as living proof
12 OEs cover the full critical path. OE->rubric map: OE8->R1, OE9->R2/R3/R4, OE11->R5/R6/R7, OE12->R8/R9/R10/R11, discovery OE2/3/5/7->R12/R13/R14/R15. No orphan OE; every OE (discovery 1-7 + writes 8-12) is exercised in the traces. The OE7 comment-read is proven load-bearing by the Opus 1,3 failures. PASS.

### Prompt binary-criteria audit (Evals_starpm/1)
Command-List PASS, Bolt-on/Coherence PASS, Pre-Solving PASS, Tool-Mention PASS, Unique-Ground-Truth PASS (all 12 runs converged on one end-state; wrong-record = failure, not a different valid state), Feasibility PASS, Truthfulness PASS (punch-list/carpet done = true; no tight IDs to be phantom), Clarity+Delegation PASS (no "I'll [verb]" ambiguity; all readings -> same 4 writes), Cross-service / Investigation+Action / Min-Complexity PASS, Contrived / Date-alignment / Persona / Business-Function PASS. All sub-dims 5. Only soft note: fuller-side stacking (5 asks) — explicit soft flag, not a fail. NO prompt binary criterion fails.

### Rubric quality audit (Evals_starpm/3 hard gates)
- Under (missing coverage): NONE. Forward coverage complete; final-response 2.1 coverage complete (R12-R15); OE-to-rubric mapping complete.
- Wrong (incorrect / misattributed / role-overreach / act-vs-defer / impossible-derivation / imported-constraint): NONE. All values universe-verified; every write-action attributed to the agent (not the user); persona-scope correct (James routes approval UP to John via R1, never approves himself — no segregation overreach); no defer decision exists to contradict R1/R2-4; no derived quantitative values; no imported constraints; self-contained; agent-centric; objective (no banned words); category-correct (15 Outcome, 0 Process, Outcome>Process).
- Over (channel/value lock-in, evidence-stricter, fabricated, at-least-N): NONE at Major. R1 channel-flexible; R5/6/7 + R8-11 match prompt-named channels; no fabricated literals; no reward-hackable at-least-N.
- Unatomic: R2/R3/R4 properly split (safe); no rubric bundles independent WRITE ACTIONS across services/channels (the actual violation pattern).
- SINGLE BORDERLINE: R11 (completion-path bundle + closeout requirement) — at most Moderate/overly-specific under the strict split gate; defensible, zero false fails, does not move pass@1. Logged in S4_fixes.md obs #3. 1 possible-Moderate / 15 = 6.7% < 15% Overall-Rubric-Quality threshold -> still PASS.

### Net effect on S4 verdict
Unchanged: STRONG PASS. The deep pass confirms full prompt/OE/rubric/trajectory parity, a clean prompt on every binary gate, complete OE coverage proven by the traces, and no under/wrong/Major-over/Major-atomic rubric. R11 is the lone borderline (non-blocking).