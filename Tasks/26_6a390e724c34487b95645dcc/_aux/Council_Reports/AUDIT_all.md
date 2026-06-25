# AUDIT — All-phase Veteran QC (Strictest Interpretation) — POST-REVIEWER

**Task:** 26_6a390e724c34487b95645dcc
**Phase scope:** `--phase all` (prompt + OE + rubrics, cross-artifact)
**Mode:** On-demand (post-platform-reviewer retrospective)
**Trigger:** `PIPELINE AUDIT --phase all` after reviewer rating Poor 2/5 (reviewer c79c70, 2026-06-23)
**Universe today:** 2026-06-12 (US/Eastern)
**Audit date:** 2026-06-25
**Auditor stance:** STRICTEST possible interpretation. 5/5 only. Every "should" read as "must". Density bar 50+ midpoint. Any derived-answer leak = BLOCKER.
**Prior audit verdicts:** AUDIT_prompt PASS (STRICT) · AUDIT_oe PASS (STRICT) · AUDIT_rubrics PASS (STRICT after round 2) · FINAL PASS · S4 SHIP (Trajectory_Stats verdict OK, 0/6 pass@1, density 79.8 avg).
**All prior audits and FINAL council MISSED the structural defects the reviewer surfaced.**

---

## Inputs re-read

- `5_Prompt.txt` (post-revise v3)
- `6_Oracle_Events.txt` (OE1–OE17)
- `7_Rubrics.json` (23 outcome / 0 process)
- `_aux/Hardness_Plan.md`
- `_aux/Fact_Ledger.json`
- `_aux/Trajectory_Stats.json` (S4 ground truth from 6 runs)
- `_aux/Council_Reports/*.md` (all prior verdicts)
- `Brookfield_Base_Universe/8_Server_Tools_Details.json` (tool registry — SSOT for parameter schemas)
- Reviewer feedback (Poor 2/5, dated 2026-06-23, reviewer c79c70)
- `Tasks/_meta/Learnings.md` (Opus 4.8 failure modes)

---

## LENS 1 — Strict QC scoring

### Prompt (5_Prompt.txt)

| Sub-dim | Score | Reason | Prior Council Miss |
|---|---:|---|---|
| Unique Ground Truth | **1** | **MAJOR.** Prompt L19–21 instructs "Jones and I had landed on dismissing under materiality. I want that actually pushed through and the exception closed out this morning". The BlackLine record `exc_652c0931bb2546.proposed_resolution = "Reclassify to the correct cost center via standard 4-eyes approval"`. Two divergent end states (dismiss vs reclassify) with no disambiguating cue in the prompt. The "lever 9 universe-grounded gotcha" framing assumes the agent doubts the persona and audits BlackLine first — but the prompt's voice is confident, time-pressured ("this morning so it stops sitting on me"), and gives no hint to audit. Universe-grounded gotchas require either a textual cue ("verify against the record") or a structural cue (figure mismatch the agent must reconcile). This prompt has neither. | S1_A_grounding, S1_B_adversarial, AUDIT_prompt all approved the lever as "stump-grade challenge". They graded the design intent (override is the right answer per Learnings L27) rather than auditing whether the prompt actually surfaces the override path. |
| Action Decision Ambiguity | **1** | **MAJOR.** "Push through dismissal" vs "reclassify via 4-eyes" are two distinct, non-overlapping write paths (different `blackline_update_exception` payloads and different downstream artifacts). The prompt commits to dismissal. The rubric mandates reclassification. The agent has no in-prompt signal that the write-path must invert. Reviewer flags this as Action Decision Ambiguity at the write-action level. | Same — all prior councils accepted the "override" pattern as legitimate without testing whether the prompt's voice gives the agent any path to discover the override is required. |
| Single-Path Closed-Period Booking | **1** | **MAJOR.** Prompt mandates "stage the closed-period entry on the Northstar December period". `northstar_legal_FP-2025-12` is locked (locked_at 2026-01-05, locked_by julia.vance). Posting requires `oracle_gl_post_journal_entry` with `late_post_authorization_id` AND an unlocked period. Period unlock requires `oracle_gl_unlock_fiscal_period` which is **VP-only**. Tom Chang is a Tax Associate (not VP). The structural path the prompt mandates is **not executable by the persona**. S4 confirms: 0/6 runs successfully posted. | Prompt-phase council noted the lever ("L9 universe-grounded gotcha") but never end-to-end traced the post path against the tool schema + role gate. |
| Implicit-Framing Preservation | **2** | Cross-artifact framing is broken at two seams: dismiss→reclassify, and create-with-auth→post-with-auth. L15+L16 framing constraint requires the rubric to match the prompt's stated framing OR the prompt to explicitly cue the override. Neither holds. | FINAL council was supposed to catch this. It did not. |
| Other prompt dims (length, dashes, tool names, internal IDs, etc.) | 5 | Validator clean. | n/a |

**Prompt verdict: REBUILD.** Two MAJOR structural defects that fix-in-place cannot repair without rewriting the prompt's voice on both work streams (the dismissal framing and the closed-period mandate).

---

### Oracle Events (6_Oracle_Events.txt)

| Sub-dim | Score | Reason | Prior Council Miss |
|---|---:|---|---|
| Tool Parameter Accuracy (OE7) | **1** | **BLOCKING.** OE7 says: *"Use oracle_gl_create_journal_entry with ... late_post_authorization_id 'email_scen_068_northstar_annual_corp_tax_0008' ..."*. Tool registry confirms `oracle_gl_create_journal_entry` parameters are: `period_id, posting_date, description, lines, entry_type, is_standard_entry, source_module, business_justification, attachments, prepared_by`. `late_post_authorization_id` is **NOT** a parameter of create — it is a parameter of `oracle_gl_post_journal_entry`. OE7 also fires post but never specifies that `late_post_authorization_id` must be passed on POST. | S2_A, S2_B, AUDIT_oe all approved OE7. None cross-verified the parameter binding against the tool registry. This is the highest-cost miss in the audit history. |
| Unlock Path Completeness (OE7) | **1** | **BLOCKING.** `northstar_legal_FP-2025-12` is closed (locked_at 2026-01-05). Posting to a closed period requires unlock via `oracle_gl_unlock_fiscal_period` (VP-only) before `oracle_gl_post_journal_entry` accepts the post even with `late_post_authorization_id`. OE7 has **no unlock step**. Even if the agent were to call unlock, Tom is not a VP — the call would be rejected. There is no executable path from OE7's intent to a posted JE for this persona. | OE-phase councils never traced the role gate. |
| Persona-Override Cue Sufficiency (OE10) | **2** | OE10 instructs the judge: *"The persona-relayed 'dismiss' framing must be overridden"*. But this is a judge instruction, not a prompt instruction. The prompt itself gives no cue to the agent. Universe-grounded gotchas at the L9 level work when the universe contains a contradiction the agent will hit while gathering basic facts (e.g., a figure mismatch). Here, the agent must distrust the persona AND choose to fetch the BlackLine record AND notice `proposed_resolution` differs from the prompt language — a chain of three optional choices that 0/6 runs completed. | OE councils treated this as a legitimate lever; reviewer treats it (correctly under strict reading) as the rubric/judge expecting impossible-to-discover behavior. |
| Other OE dims | 5 | Slack channel ids, email ids, exception ids, reminder ids all verified against universe. | n/a |

**OE verdict: REBUILD.** Two BLOCKING structural defects on OE7 (wrong parameter binding + missing unlock + role gate) that propagate to 5 downstream OEs (OE8, OE9, OE17 reference the posted JE id; OE10/OE12 reference the reclassification path).

---

### Rubrics (7_Rubrics.json — 23 outcome)

| Sub-dim | Score | Reason | Prior Council Miss |
|---|---:|---|---|
| Reachability (R1) | **1** | **BLOCKING.** R1 requires `oracle_gl_create_journal_entry + submit + approve + post` cycle on closed period ending in `posted` status. Universe blocks this path (period closed, no in-OE unlock, Tom not a VP). S4 confirms: 0/6 runs reached `posted`. Rubric is structurally unreachable. |  Prior rubrics audit scored Reachability 5/5 without trajectory cross-check. |
| Tool Parameter Accuracy (R2) | **1** | **BLOCKING.** R2 evidence says: *"check the late_post_authorization_id parameter on the oracle_gl_create_journal_entry call. The value must be 'email_scen_068_northstar_annual_corp_tax_0008'"*. This parameter does **not** exist on that tool. The check the judge is asked to perform is impossible. Even if the agent inferred the right authorization, no `late_post_authorization_id` will ever appear on a create-call payload. |  Catastrophic miss across S3 + AUDIT_rubrics + AUDIT_rubrics_revise_round2 + FINAL. |
| Reachability cascade (R3, R4, R5, R7a, R7b, R8a) | **1** | **BLOCKING (×6).** All six depend on the posted JE id from R1. Since R1 is unreachable, none of these can fire even if the agent does perfect work on memo upload / email content / classification / retention. Combined with R1 and R2, this is the **7 structurally-invalid rubric set** the reviewer flagged (ids: `7c8e5a12`, `8d9f6b23`, `9e0a7c34`, `af1b8d45`, `b02c9e56`, `d24e1078`, `7e8d9c2b`). Reviewer's reduction: when these were removed, AF dropped from 17→4. | Prior audits' Reachability dim scored 5/5 across all 7. The chain-dependency on R1 was never traced. |
| Disposition Override Reachability (R11, R22) | **2** | R11 requires `blackline_update_exception` payload that records **reclassification**. R22 requires the agent's final response to **identify** the documented disposition. The prompt's voice gives no cue to invert. Universe-grounded gotcha is mechanically possible (the agent COULD `blackline_get_exception` first) but the prompt actively pushes against it. S4 shows 0/6 on R11 and 0/6 on R22 — confirming the gotcha is unreachable in practice. | Prior councils accepted L9 as a hard challenge; should have been flagged as unreachable given prompt voice. |
| Cross-rubric ordering / atomicity / V3 voice / em-dashes / "at least N" / tool-name leaks | 5 | Validator clean; prior atomicity splits (R7a/b, R8a/b) hold. | n/a |

**Rubrics verdict: REBUILD.** 7 of 23 rubrics (30%) are structurally unreachable. 2 of 23 (R11/R22) are reachable only by an inversion the prompt actively suppresses. Any fix-in-place that touches these rubrics requires upstream prompt + OE rewrites (because R2 depends on a wrong parameter binding in OE7, which itself reflects a misunderstanding of the GL tool schema).

---

## LENS 2 — Answer-leakage sweep

No new derived-answer leaks. The `$4,820.30` figure appears in the prompt-adjacent universe (William's email body) and in the rubrics, but the trace requirement (R19) holds. Not a blocker — but moot given the structural blockers above.

---

## LENS 3 — Hardness end-to-end trace

| Lever | Prompt sentence | OE step | Rubric | Trace status |
|---|---|---|---|---|
| L2 — GL triangulation | "traced back through our own records" | OE5 | R19 | TRACES (3/6 in S4) |
| L4 — search-result-cap eviction | "older one is the stale tickler from last summer" | OE14 | R23 | TRACES (5/6 in S4) |
| L5 — thread-reply blindness | "with a side note about the underlying polling bug" | OE14, OE16 | R15, R23 | TRACES (5/6 + 0/6) — split signal |
| L8 — A→B→C→D multi-link chain | "stage the closed-period entry … bind … tied … ping" | OE7→OE8→OE9 | R1→R3→R6 | **BROKEN at C** — JE never posts → D never fires |
| L9 — universe-grounded gotcha (×2) | (none for dismiss/reclassify); ("closed-period booking") for late-post | OE10 / OE4+OE7 | R11, R22 / R20 | **BROKEN ×2** — no prompt cue (R11/R22 → 0/6) and tool schema mismatch (R1/R2 → 0/6) |
| L10 — stub recognition | "Hannah just messaged that William cleared … e-file path shouldn't be sitting behind" | OE6 | R21 | TRACES (0/6 — separate signal-strength concern) |
| L25 — stub forward-look | (same as L10) | OE6 | R21 | TRACES (0/6) |
| L27 — soft-instruction over-compliance | "I want that actually pushed through" | OE10 | R11, R22 | **BROKEN** — design intent assumes agent overrides; prompt's voice rewards compliance, not override |

**Hardness regression:** **3 of 8 levers broken** at the artifact-chain or prompt-cue level. Threshold for REBUILD (per AUDIT runbook strict reading) is "3+ levers untriggered by prompt framing." **Threshold met.**

---

## LENS 4 — Density projection

| Source | Value | vs strict bar 50+ |
|---|---:|---|
| Council B midpoint | 52 | PASS |
| S4 actual avg total | 79.8 | PASS |
| S4 actual avg MCP-only | 65.5 | PASS |

Density is fine. Reviewer did not flag density. Density was never the issue on this task — the issue is the rubric set / OE schema / prompt voice. Density-only S4 verdict ("OK") masked the structural defects because S4 does not re-cross-verify rubric reachability against the trajectory failure pattern; it only buckets fails and assumes Bucket 3 ("legitimate model failure") covers everything not classified Bucket 1 (rubric invalid) or Bucket 2 (judge error). S4 should have flagged R1+R2+R3+R4+R5+R7a+R7b as Bucket 1 (rubric invalid — wrong tool schema, structurally unreachable). It did not. **This is a process learning for S4 itself.**

---

## LENS 5 — Adversarial veteran review

| Check | Finding |
|---|---|
| Implicit-prompt framing preserved across artifacts? | **NO.** Prompt commits to dismiss; rubric mandates reclassify. Prompt commits to "stage the closed-period entry" assuming an executable path; OE7 + tool schema + persona role make the path unexecutable. |
| Entity-drift seams? | None. Email addresses, period ids, exception ids, reminder ids all clean. |
| Silent process rubrics disguised as outcomes? | None. 23/23 outcome, validator clean. |
| Tool-name leaks in prompt or rubric titles? | None. |
| Em-dashes / "at least N" / "approximately" near IDs / "(or similar)" near exact values? | None. |
| Single-channel lock-in where prompt named only a goal? | None on the email channel (R6 allows reply or send). |
| Validator WARNs | 6× `$4,820.30 not in Fact_Ledger amounts` — figure is present in William's auth email body and in OE2/OE7, but never re-indexed into Fact_Ledger after S0. Cosmetic — flagged for completeness. |
| REVIEW-flow-only checks (`13_Feedback.txt`) | n/a — CB-built task, not REVIEW flow. |
| S4 Bucket 3 classification on R1–R7b | **WRONG.** These should be Bucket 1 (rubric invalid: wrong tool schema + unreachable path). S4 misclassified all 7 as Bucket 3 (legitimate model failure), inflating AF count and masking the structural defect. |
| Trajectory_Stats verdict "OK" | **WRONG under strict reading.** density_ok_at_40 + difficulty_ok_at_40pct are necessary, not sufficient. A task can be "OK" on those gates while having a 30%-unreachable rubric set. The strict version of the verdict should add a Bucket-1 reachability check. |

**Adversarial verdict: REBUILD with cross-pipeline process learnings.**

---

## Cross-lens roll-up

| Lens | Result | BLOCKERS |
|---|---|---|
| L1 — Strict QC scoring | Prompt REBUILD · OE REBUILD · Rubrics REBUILD | 11 |
| L2 — Answer leakage | Clean (moot) | 0 |
| L3 — Hardness end-to-end trace | 3 of 8 levers broken | 3 |
| L4 — Density projection | PASS | 0 |
| L5 — Adversarial veteran review | Framing broken at 2 seams; S4 misclassification | 2 |

---

## Resolution of reviewer feedback (Poor 2/5, c79c70, 2026-06-23)

| Reviewer claim | Verifiable? | Audit finding |
|---|---|---|
| Prompt "dismiss / push through" contradicts BlackLine `proposed_resolution = "Reclassify via 4-eyes"` → Major Unique Ground Truth | YES — prompt L19–21 vs `_aux/Universe_Split/blackline/exceptions.json` `exc_652c0931bb2546.proposed_resolution` | CONFIRMED (L1 prompt + L3 lever-9 trace) |
| Same contradiction at write-action level → Major Action Decision Ambiguity | YES — R11 + R22 invert the prompt's stated write path | CONFIRMED (L1 prompt + L5 framing) |
| 7 rubrics structurally invalid (`f74f3d71`, `41a27395`, `636b3306`, `89461400`, `a7dbc0d2`, `e021cf28`, `aed52226`) | Reviewer's id list refers to the platform's reviewer-side IDs; map to the current 7 dependent rubrics in `7_Rubrics.json`: `7c8e5a12` (R1, post JE), `8d9f6b23` (R2, late_post auth bind on create), `9e0a7c34` (R3, vault memo `related_resource_type=journal_entry` tied to posted JE), `af1b8d45` (R4, memo body), `b02c9e56` (R5, memo cites posted JE id), `d24e1078` (R7a, email confirms posted), `7e8d9c2b` (R7b, email references JE id + entry_number) | CONFIRMED (L1 rubrics — all 7 depend on a posted JE id that no run can produce; 0/6 on each in S4) |
| `oracle_gl_create_journal_entry` hard-rejects closed period with OGL.PERIOD_CLOSED | Reviewer's claim re: server behavior; tool registry confirms `late_post_authorization_id` is NOT a create-call param (only post) and `oracle_gl_unlock_fiscal_period` is VP-only | CONFIRMED via tool schema + S4 0/6 on the post-success rubric |
| OE7 tells judges to look for `late_post_authorization_id` on create | YES — OE7 text explicitly says so; tool registry shows that parameter does not exist on create | CONFIRMED |
| OE7 never includes the unlock step | YES — OE7 has no `oracle_gl_unlock_fiscal_period` call; even if it did, Tom Chang is not a VP | CONFIRMED |
| Removing 7 invalid rubrics dropped AF from 17→4 | Reviewer's empirical result after fix | NOT INDEPENDENTLY RE-RUN here, but consistent with the chain analysis: R1 + R2 + R3 + R4 + R5 + R7a + R7b unreachable + 4 cascade fails on R6/R8a/R8b/R10 (memo/email content) = 11 of 14 AFs are structural, leaving ~3–4 legitimate model failures, matching reviewer's "AF reduced to 4" |
| "Prompt itself still contained fundamental ambiguities and contradictions, so it requires a rewrite and I had to redo the whole task again" | YES — even with rubrics fixed, the dismiss/reclassify contradiction and the closed-period unreachability remain in the prompt | CONFIRMED — REBUILD scope, not REVISE |

**All seven reviewer claims confirmed under strict re-audit.**

---

## VERDICT

**REBUILD**

Structural defects that fix-in-place cannot repair:

1. **Prompt → OE → Rubric chain on the SALT late-post is structurally unreachable.** Closed-period booking via the prompt-mandated path is blocked at the tool-schema and role-gate level. 7 rubrics (`7c8e5a12`, `8d9f6b23`, `9e0a7c34`, `af1b8d45`, `b02c9e56`, `d24e1078`, `7e8d9c2b`) cannot fire on any run. Confirmed by S4: 0/6 across all 7.
2. **Prompt → OE → Rubric chain on the exc_652c reclassification inverts the prompt's stated write path.** R11 + R22 require the agent to override the prompt's "dismiss" instruction with a "reclassify" path that the prompt never cues. Confirmed by S4: 0/6 on R11, 0/6 on R22.
3. **3 of 8 hardness levers (L8 multi-link chain, L9 universe-grounded gotcha ×2 instances, L27 soft-instruction override) are broken at the prompt-framing or tool-schema level.** AUDIT runbook threshold for REBUILD is "3+ levers untriggered by prompt framing." Threshold met.

### Recommended REDO scope

`PIPELINE REDO — Tasks/26_6a390e724c34487b95645dcc` — full rebuild of `5_Prompt.txt` + `6_Oracle_Events.txt` + `7_Rubrics.json`.

Required structural changes for the rebuild (operator-facing — REDO chat will re-plan from S0/HARDNESS):

- **Closed-period booking path:** either (a) drop the closed-period mandate from the prompt and let the agent post in current period with a properly-anchored adjusting-entry voice, OR (b) keep the closed-period mandate AND ensure OE includes an `oracle_gl_unlock_fiscal_period` step authorized by a VP persona (not Tom), with the rubric checking `late_post_authorization_id` on **post** (not create) and the unlock as a prerequisite step. Option (b) requires switching the prompt's executing persona to a VP-level role (e.g., Matthew Li) or splitting the work across personas (Tom prepares; VP unlocks).
- **Dismiss-vs-reclassify contradiction:** either (a) rewrite the prompt to give the agent a textual cue to verify the BlackLine record before acting (e.g., "Daniel's gone quiet; I want you to verify the BlackLine disposition before pushing anything through"), OR (b) drop the override gotcha and let the rubric check the dismissal path the prompt actually instructs. Hybrid options (e.g., keep "I think we agreed dismiss" with a verify-first cue) preserve the lever while making the override discoverable.
- **Rubric reachability discipline:** every rubric that depends on a runtime tool-call output (posted JE id, vault doc id) must be traced against the actual tool registry and against a constructed happy-path trajectory before the rubric is approved. Add a Bucket-1 reachability check to S4 so structurally-unreachable rubrics are flagged before the SHIP verdict.

### Pipeline-level process learnings (for `Tasks/_meta/Audit_Log.md` + `Tasks/_meta/Learnings.md`)

1. **Strict per-phase audit MUST cross-verify every tool parameter cited in OE / rubrics against `Brookfield_Base_Universe/8_Server_Tools_Details.json`.** AUDIT_oe and AUDIT_rubrics both missed `late_post_authorization_id` being on post-not-create because they never re-grepped the tool schema. Add a mechanical schema-cross-check to the AUDIT prompt template (L1.5 lens).
2. **Strict per-phase audit MUST trace every closed-period / role-gated tool call against the persona's role.** Tom is not a VP; the unlock path is structurally blocked. Persona role gates are universe constants and should be enumerated in `_aux/Universe_Index/`.
3. **S4 Bucket classification MUST include a "structurally unreachable" check** before classifying any 0/6 rubric as Bucket 3 (legitimate model failure). When 0/6 runs satisfy a rubric, the auditor should first ask: "Is the rubric reachable on the happy path?" If not, it is Bucket 1 (invalid), not Bucket 3.
4. **FINAL council MUST run a prompt-voice-vs-rubric-write-path reconciliation.** When a rubric mandates the inverse of the prompt's stated write path, FINAL should require a textual cue in the prompt that surfaces the override — otherwise the lever is unreachable by design.
5. **Auto-fire AUDIT rounds returning PASS (STRICT) must include explicit evidence of the schema cross-check and reachability trace.** A "PASS (STRICT)" without those traces is no stronger than the per-phase Council B verdict it is supposed to harden.

---

VERDICT: **REBUILD**

Next trigger: `PIPELINE REDO — Tasks/26_6a390e724c34487b95645dcc`
