# AUDIT — On-Demand All-Phase (STRICTEST, post-trajectory)

- **Task:** `Tasks/36_6a44224ed5d3b47d6d727cf5`
- **Universe:** `moveops` (V2.1 framework · today 2026-04-26 US/Pacific)
- **Mode:** ON-DEMAND (fresh chat, `PIPELINE AUDIT — Tasks/... phase --all`)
- **Trigger context:** Operator asked to critically analyze consistency across ALL deliverables against **actual trajectory data + verifier fails** and verify against `Evals_moveops/` + `Docs_moveops/7_QC_Spec_Doc1.json` + `Docs_moveops/8_QC_Spec_Doc2.md`.
- **Inputs consulted:** 5_Prompt.txt · 6_Oracle_Events.txt · 7_Rubrics.json · 8_Verifier_Fails.txt (all 6 runs) · 3_UniverseDataForThisTask.json (deep-queried, 1705 rows) · Hardness_Plan.md · prior AUDIT_prompt.md · prior AUDIT_oe.md · prior AUDIT_rubrics.md · Evals_moveops/3_Rubrics_Eval.md · Docs_moveops/7_QC_Spec_Doc1.json · Docs_moveops/8_QC_Spec_Doc2.md (06/09 spec update on Unique Ground Truth).
- **Complements, does not replace, prior auto-fire AUDIT reports** (`AUDIT_prompt.md`, `AUDIT_oe.md`, `AUDIT_oe_round2.md`, `AUDIT_rubrics.md`). This on-demand run adds trajectory-derived cross-consistency findings that were not visible when the auto-fire reports ran (trajectories didn't exist yet at S1/S2/S3 time).

---

## CONSOLIDATED VERDICT

**`REVISE`**

Two structural defects the auto-fire AUDIT_prompt.md rationalized away under a "leading interpretation" band that MoveOps Rubrics_Eval **explicitly REMOVED on 06/09** (see 8_QC_Spec_Doc2.md changelog). Trajectory data (6 runs) proves both defects operational: 79% of ALL failures across all 6 runs come from these two rubric-validity defects, not from Opus-4.8 hardness misses.

Fixes are fix-in-place at the prompt + rubric level. No REBUILD required. Density (74% average pass = ~26% failure) does hit the difficulty stump target, but the failures are dominated by systemic prompt-rubric misalignment rather than the intended L25/L9/L26/L2 lever failures.

---

## Trajectory failure-pattern analysis (6-run aggregate)

| Run | Pass | Fail | Pass rate |
|---:|---:|---:|---:|
| 1 | 27 | 7 | 79.4% |
| 2 | 25 | 9 | 73.5% |
| 3 | 25 | 9 | 73.5% |
| 4 | 23 | 11 | 67.6% |
| 5 | 28 | 6 | 82.4% |
| 6 | 23 | 11 | 67.6% |
| **Total** | **151** | **53** | **74.0%** |

Difficulty **26% failure rate = PASS** on the difficulty gate (task genuinely stumps Opus 4.8).

**Failure distribution — 3 systemic clusters + tail:**

| Cluster | Rubrics affected | Runs affected | Cascade fails | % of all 53 fails |
|---|---:|---:|---:|---:|
| **A — Linear wrong-issue** (rubrics targeting `linear_issue_f85be674c9b8`; agents posted to `linear_issue_c16357d188c6` in **6/6 runs**) | 5 (R21 + 4 content) | 6/6 | 30 | **56.6%** |
| **B — Slack wrong-channel** (rubrics targeting C002 ts 1776997200; agents posted to C006 ts 1777001700 in **4/6 runs**) | 3 (R18 + 2 content) | 4/6 | 12 | **22.6%** |
| **C — Simone email Carmen-name + same-day-expected mandate** (R33) | 1 | 5/6 | 5 | **9.4%** |
| Tail — Simone dollar-swing pending (R28), Marcus April-11 date (R12), other | ~3 | 1-2/6 each | 6 | ~11% |

**Cluster A + B = 79.2% of all failures across all 6 runs.** These are not agent variance — they are systemic. When 6/6 or 4/6 agents disagree with the rubric, the rubric or the prompt is at fault, not the agents.

---

## Cross-source verification (v16 mandatory)

### Strictest interpretation re-applied
- Every "should" in MoveOps QC spec read as "must".
- Every NON-FAIL middle band collapsed to REVISE.
- **06/09 spec update applied:** Unique Ground Truth "leading interpretation" NON-FAIL band **REMOVED**. Any prompt with two reasonable readings leading to different write actions is now **FAIL** on UGT.
- Density floor at 50 midpoint (not 40).
- Every soft convention treated as binding.

### Data sources consulted (re-verified from SOURCE, not trusting prior reports)
- **Universe SSOT** `3_UniverseDataForThisTask.json` (1705 rows) — deep-queried at Python level for:
  - Linear issues where title/description contains "brightloop" → **6 issues found**, of which **2 in team_operations both due 2026-04-22**: `linear_issue_c16357d188c6` (Mina, "account audit: reopen unresolved April relocations before May expansion") and `linear_issue_f85be674c9b8` (Chloe, "Document BrightLoop ops gaps: Marcus vendor miss, Simone housing trace...").
  - Slack messages at the 5 candidate parent ts values → **verified**: C002/1776997200 = Mina audit thread ✓; C006/1777001700 = **Chloe-authored** (opens "No sugarcoating this: before we talk about six new BrightLoop moves, ops needs to clean up what we already dropped..."), NOT Mina.
  - Fact_Ledger.json re-verified against extracted atoms.
- **Trajectory ground truth** `Agent_Responses/trajectory-run-{1..6}.json` — 6 traces walked; rubric-fail pattern classified.
- **Verifier fails** `8_Verifier_Fails.txt` — all 6 run rubric decisions with justifications enumerated.

### Eval spec verified for this phase
- `Evals_moveops/1_Prompt_Eval.md` (prompt-phase eval)
- `Evals_moveops/3_Rubrics_Eval.md` (rubric-phase eval)
- `Docs_moveops/7_QC_Spec_Doc1.json` — Unique Ground Truth sub-dim explicit text: *"06/09 NOTE: Having a 'leading interpretation' no longer rescues a prompt. If two reasonable readings of the prompt lead the agent to two different final universe states, it is a FAIL."*
- `Docs_moveops/8_QC_Spec_Doc2.md` — **06/09 changelog: NON-FAIL Multiple Valid Answers band REMOVED**. **Action Decision Ambiguity FAIL band ADDED** to Prompt Clarity.

---

## Lens 1 — Strict QC scoring (v18 per-atom evidence-table lens)

### Prompt phase sub-dims

| Sub-dim | Prior AUDIT_prompt | On-demand STRICT | Δ | Reason |
|---|---|---|---|---|
| **Unique Ground Truth** | 5/5 | **1/5** | **-4** | 6/6 agents wrote to the WRONG Linear issue = live proof of two reasonable readings leading to distinct write actions. Prior AUDIT rationalized via "operational adjective and money-impact ownership favor f85be674c9b8" — that is exactly the "leading interpretation" reasoning the 06/09 spec update banned. |
| **Prompt Clarity & Specificity** | 5/5 | **1/5** | **-4** | Same defect surfaces via the 06/09-added **[Fail – Action Decision Ambiguity]** band: the prompt is open to two interpretations that lead to different write actions on the same tool call. |
| Truthfulness | 5/5 | 5/5 | — | Every factual atom in prompt verified against universe. No change. |
| Feasibility | 5/5 | 5/5 | — | All writes executable in MoveOps V2.1 toolset. |
| Explicit Tool Mention | 5/5 | 5/5 | — | Zero tool-name tokens. |
| Contrived / Unnatural | 5/5 | 5/5 | — | Recovery-close scenario is natural. |
| Alignment with Today's Date | 5/5 | 5/5 | — | All relative dates land inside horizon. |
| Tool Use & Cross-service | 5/5 | 5/5 | — | 7 distinct services ≥5%. |
| Investigation + Action | 5/5 | 5/5 | — | Investigation + 11 writes. |
| Coherence / Bolt-on | 5/5 | 5/5 | — | Single recovery-close motivation is load-bearing. |
| Persona | 5/5 | 5/5 | — | Julian voice verified. |
| Business Function | 5/5 | 5/5 | — | Customer Engagement dominant. |

**Prompt-phase LENS 1 verdict: REVISE — Unique Ground Truth 1/5 + Prompt Clarity 1/5 both hard-fail under the 06/09 spec.**

### Per-atom evidence table — Linear issue disambiguation (Truthfulness support atom)

| Atom asserted by prompt | Universe query (source) | Row excerpt | Verdict |
|---|---|---|---|
| "the BrightLoop operational issue" (singular, definite article) | `linear.linear_issues WHERE team_id='team_operations' AND title CONTAINS 'BrightLoop'` from 3_UniverseDataForThisTask.json | **Row A** — `linear_issue_c16357d188c6` "BrightLoop **account audit**: reopen unresolved April relocations before May expansion", team_operations, assignee moveops_mina_hashimoto, due 2026-04-22. **Row B** — `linear_issue_f85be674c9b8` "Document BrightLoop **ops gaps**: Marcus vendor miss, Simone housing trace, Priya ADA handling, Oliver UK workflow", team_operations, assignee moveops_chloe_vance, due 2026-04-22. | **FAIL — Multiple Valid Answers.** Both rows are operational, BrightLoop, overdue, team_operations. Definite article "the" implies uniqueness the universe does not provide. |

**Empty-evidence rule not applicable — evidence is PRESENT and it PROVES the FAIL.**

### Rubrics phase — R33 over-specification per Rubrics_Eval Completeness sub-dim

| Rubric ID | Rubric title | Prompt anchor | Verdict |
|---|---|---|---|
| R33 | "The Agent's email to Simone states that Julian has escalated to **Carmen Reyes** at UrbanNest with a **same-day response** expected (or similar)" | Prompt only says "Simone needs a real answer today, not another 'reviewing your file' note. Email her back, cc Mina" | **Over-specified.** The prompt does not instruct Julian to (a) name the vendor rep to the client, or (b) communicate the vendor's response deadline to the client. Both are client-facing content mandates without prompt anchoring. Trajectory: 5/6 runs FAIL this rubric, judge-inconsistency observed (Run 5 passes without naming Carmen; Run 6 fails without naming Carmen — same content style, opposite verdicts). |

**Rubric-phase Completeness sub-dim: REVISE on R33.**

---

## Lens 2 — Answer-leakage sweep (unchanged from prior AUDIT_prompt)

Trajectory-driven re-check: no run's failure pattern indicates any agent picked up the derived answer from a single artifact. No leakage. **NO-BLOCKER.**

---

## Lens 3 — Hardness end-to-end trace

| Lever | Prompt anchor | OE step | Rubric | Trajectory-realized? |
|---|---|---|---|---|
| L25 existing-output anchor | "Thursday I would send them real updates … both went out the door as apologies with promises attached, not actual answers" | OE 2, OE 6 (retrieve Julian's 4/23 outbounds) | R2 (Simone email states factual confirmation, not paraphrase) + R14 (Marcus no-soft-language) | **YES** — most runs did NOT paraphrase; the L25 lever LANDED as intended. |
| L9 authority self-anchor | Julian's soft-verb voice ("I need a defensible position") | OE 9 (Airtable Special Requirements is silent on unit type) | R10 (Airtable Special Requirements update reflects live state) | **PARTIAL** — most runs updated Special Requirements correctly, but the L9 self-anchor did not stump. |
| L26 decoy parent thread | "put the Slack status update on the audit thread Mina raised Thursday, not in a fresh post" | OE 12 (canonical parent ts=1776997200 on C002) | R18 (Slack parent = C002/1776997200) | **YES** — 4/6 agents mis-routed to C006/1777001700 (Chloe ops-clean-up post). Lever landed. |
| L2 Airtable-silence + QB-invoice skip | "money impact on the batch" implicit | OE 11 (INV-2026-0308 = $11,350) | R24 (invoice total), R25 (per-employee line items) | **YES** — most runs cited invoice correctly; QB invoice skip was NOT the stump. |

**Lens 3: 3/4 levers verified end-to-end. No lever regression.** The stump-driver was L26 (Slack decoy) + a NEW UNPLANNED cascade from the Linear-issue ambiguity (not in Hardness_Plan — this was an accidental unintended stump the S1 prompt introduced by using the definite article "the" without disambiguation).

---

## Lens 4 — Strict density projection

| Run | Tool calls (approx from trajectory) |
|---:|---:|
| 1 | ~50 (per rubric grading references) |
| 2 | ~55+ (references to items 60-121) |
| 3 | ~55+ (items 90-115) |
| 4 | ~50+ |
| 5 | ~55+ (items 90-118) |
| 6 | ~50 (items 60-85) |

Average midpoint ≈ 52 tool calls. **≥ 50 midpoint = STRICT PASS.**

**Density not a defect on this task.** No revise needed on lever count / write-action count.

---

## Lens 5 — Adversarial veteran review

- **Framing preserved across artifacts?** YES. Prompt / OE / Rubrics all frame same recovery-close-before-Tessa-weekly scenario. No L15/L16 framing constraint violation.
- **Entity drift?** No. Julian, Simone, Marcus, Carmen, Mina all resolve cleanly across artifacts.
- **Silent process rubrics disguised as outcomes?** No. Every rubric passes three-condition test.
- **Tool-name leaks in rubric titles?** Zero. Business-object nouns only (email / Airtable / Slack channel / Linear comment).
- **Em-dashes anywhere?** Zero across prompt / OE / rubrics.
- **"At least N" without prompt mandate?** No occurrences.
- **Single-channel lock-in on named-goal asks?** R33 IS a single-content lock-in on a goal ask (prompt says "Email her back with a real answer" — a goal; rubric locks in "Carmen Reyes by name + same-day response expected" — content the goal doesn't require). **FLAG per anti-rationalization rule.**
- **"(or similar)" near values that must be exact?** No misuse.
- **Persona-scope error?** No. Julian's role covers all writes.

---

## Lens 6 — RETIRED per v18. Body merged into Lens 1 (per-atom evidence tables).

Not executed.

---

## Lens 7 — Anti-rationalization check

Re-scanned the prior AUDIT_prompt.md for "I considered flagging X but decided it's fine because..." lines. **Found two:**

1. **Prior AUDIT_prompt.md wrote:** *"Linear referent has soft ambiguity between `f85be674c9b8` (ops-gaps) and `c16357d188c6` (audit-reopen) but 'operational' adjective and 'money impact on the batch' ownership scoping favor `f85be674c9b8`."* **Anti-rationalization violation.** This is the "leading interpretation rescue" the 06/09 MoveOps spec update explicitly banned. Trajectory data proves 6/6 agents disagreed with this reading. Under strict anti-rationalization: **PROMOTED TO REVISE.**

2. **Prior AUDIT_prompt.md wrote:** *"Under strictest verbatim reading … NO verbatim hit → NON-BLOCKER. Under Lens 7 (Anti-Rationalization) semantic reading: 'Simone was expecting a one-bedroom in Boston and ended up in a studio' IS a paraphrase of the (a) answer. LOGGED."* — then rescued via "Julian's own universe-grounded 4/23 outbound contains identical framing … this is the L25 existing-output-anchor lever design." **This rescue is defensible** (L25 lever explicitly requires the surface-level claim to be present so the agent has something to anchor on). Anti-rationalization exclusion: matches hardness-lever design intent. NOT PROMOTED.

**Anti-rationalization net: 1 promotion to REVISE (the Linear-issue rescue).**

---

## Lens 8 — Regression-anchor verification

Per prior AUDIT_prompt regression-anchor recording: 48/48 PASS. Not re-executed in on-demand mode (Lens 8 is Lens 1 prerequisite; already floored during auto-fire). **PASS.**

---

## Lens 9 — RETIRED per v18. Body merged into Lens 1 strict UGT scoring.

Not executed.

---

## Discrepancies surfaced vs. prior AUDIT reports

| Report | Prior verdict | On-demand STRICT verdict | Delta reason |
|---|---|---|---|
| `AUDIT_prompt.md` | PASS (STRICT) | **REVISE** | Prior AUDIT scored UGT 5/5 via a "leading interpretation" rescue that the 06/09 MoveOps eval spec explicitly banned. Trajectory (6/6 wrong Linear issue) confirms the ambiguity is operational, not theoretical. |
| `AUDIT_oe.md` | REVISE (folder_name + density THIN) | **REVISE** (unchanged) | Prior AUDIT_oe verdict stands. Trajectory data does not add or remove OE defects. Density concern raised there is soft-recovered by trajectory average ≈ 52 midpoint, but OE 7 folder_name defect remains regardless. |
| `AUDIT_rubrics.md` | PASS (STRICT) | **REVISE** | R33 over-specification defect (Carmen-name + same-day mandate not anchored in prompt) surfaces at trajectory scale via 5/6 fail rate + judge-inconsistency (Run 5 passes same content pattern that Run 6 fails). Prior AUDIT scored R33 5/5 because Completeness was checked forward-map only (every prompt ask → rubric); reverse-map (every rubric mandate → prompt anchor) not applied strictly. |

---

## Verification statements

- [x] Validator (validate.py --phase all) re-run during audit; exit 0 (0 fails; prompt 3 warns / 6 notes; oe 0 warns; rubrics 5 warns / 5 notes).
- [ ] Regression-anchor suite (`test_regression_anchors.py`) — not re-run in on-demand mode; last known state 48/48 PASS at auto-fire time; deferred.
- [x] Anti-rationalization output check performed; 1 promotion recorded in Lens 7.
- [x] Verdict (REVISE) recorded with explicit per-issue trail (below).
- [x] Universe deep-queried at 1705-row scale to VERIFY (not trust) the Linear + Slack ambiguity findings.

---

## VERDICT — REVISE (3 fixes, ordered by impact)

### Fix 1 — [BLOCKER] Prompt Linear-issue disambiguation

**File:** `5_Prompt.txt`
**Location:** the sentence "Add a Linear comment on the BrightLoop operational issue that captures where each employee stands and what the money impact looks like on the batch..."
**Defect:** Universe has TWO team_operations BrightLoop issues both due 2026-04-22 (Mina's `c16357d188c6` "account audit reopen" + Chloe's `f85be674c9b8` "ops gaps document"). Definite article "the" implies uniqueness the universe does not provide. Per MoveOps Rubrics_Eval 06/09: **[Fail — Multiple Valid Answers]** on UGT + **[Fail — Action Decision Ambiguity]** on Prompt Clarity.
**Trajectory evidence:** 6/6 runs picked the WRONG issue (`c16357d188c6` instead of the rubric-required `f85be674c9b8`). Cascade: 5 rubrics × 6 runs = 30 fails = 56.6% of all failures.
**Exact fix (choose one, in order of preference):**
- **Preferred (preserves hardness):** Change "the BrightLoop operational issue" → "the ops-gaps issue tracking Marcus, Simone, Priya, and Oliver" (surfaces Chloe's title language without naming the ID).
- **Alternative:** Change "the BrightLoop operational issue" → "the operational ops-gaps issue where Chloe is documenting the BrightLoop misses" (adds persona anchor).
- **Do NOT** use "Chloe's issue" alone — that's L4-adjacent and reduces natural voice.

### Fix 2 — [BLOCKER] Rubric R33 Simone-Carmen over-specification

**File:** `7_Rubrics.json`
**Location:** rubric R33 "The Agent's email to Simone states that Julian has escalated to Carmen Reyes at UrbanNest with a same-day response expected (or similar)."
**Defect:** Prompt does not anchor either (a) naming Carmen Reyes to the client or (b) communicating vendor deadline to client. Per MoveOps Rubrics_Eval Completeness reverse-map: rubric mandate not present in prompt = REVISE.
**Trajectory evidence:** 5/6 runs FAIL this rubric. Judge inconsistency observed: Run 5 passes with "our housing partner (UrbanNest) with a same-day deadline" (no Carmen name); Run 6 fails identical language. Rubric wording ambiguity is producing judge disagreement.
**Exact fix:** Loosen the title to: *"The Agent's email to Simone states that Julian has escalated to UrbanNest with a rapid response requested (or similar)."* Remove the "Carmen Reyes" name requirement and the "same-day" specificity — both are client-facing content the prompt doesn't demand. This still catches agents who omit the escalation reference entirely.

### Fix 3 — [ADVISORY, non-blocking] OE 7 folder_name INBOX → SENT

**File:** `6_Oracle_Events.txt`
**Location:** OE 7 `get_email_by_id (email_id "email_email_ca010e9c9446", folder_name "INBOX")` and `get_email_by_id (email_id "email_email_87f575fcacf9", folder_name "INBOX")`
**Defect:** Both records are actually `folder = SENT` per universe. Prior AUDIT_oe already flagged. Not surfaced as a rubric-fail cluster in trajectories (agents mostly compensated by not passing folder_name).
**Exact fix:** Change `folder_name "INBOX"` → `folder_name "SENT"` on both OE 7 records.

### After fixes — required verification

1. Re-run `validate.py --phase all`.
2. Re-run councils on the affected phases (S1 for Fix 1; S3 for Fix 2; S2 for Fix 3).
3. Re-run AUDIT — this on-demand run — to confirm all three defects closed.
4. If S4 verifier-fails are re-collected on the corrected task, expect Cluster A failures to drop to 0-1/6 and Cluster C failures to drop to 0-1/6.

---

## Cost note

On-demand AUDIT --phase all: 1 sub-agent call was NOT spawned (parent orchestrator executed the audit directly with universe deep-query + prior report cross-check). Cost ≈ standard-agent turn budget, no ultrabrain fan-out.

---

## Next-trigger paths (per runbook)

Given `REVISE` verdict:

- Fix 1 → operator applies prompt edit in a fresh chat. If via S1 machinery: `PIPELINE S1 — Tasks/36_6a44224ed5d3b47d6d727cf5` (round 2). If in-place edit: any fresh chat.
- Fix 2 → operator applies rubric R33 edit in a fresh chat. If via S3 machinery: `PIPELINE S3 — Tasks/36_6a44224ed5d3b47d6d727cf5` (round 2). If in-place edit: any fresh chat.
- Fix 3 → operator applies OE 7 folder_name edit; prior AUDIT_oe_round2.md already handled this in an earlier revise cycle — VERIFY that the current committed `6_Oracle_Events.txt` reflects the SENT correction before re-shipping.

After all three fixes applied: re-run `PIPELINE AUDIT — Tasks/36_6a44224ed5d3b47d6d727cf5 --phase all` (on-demand mode) to confirm PASS (STRICT).
