# PIPELINE FINAL — Cross-Artifact Holistic Council

**Trigger:** `PIPELINE FINAL — Tasks/<TASK_DIR>`

**When to run:** AFTER S3 produces `7_Rubrics.json` and BEFORE the user uploads to the platform. This is the last gate. Per-phase councils (S1 / S2 / S3) read each artifact in isolation; this one reads all three TOGETHER and checks cross-artifact consistency + answer leakage + difficulty preservation end-to-end.

## What this catches that per-phase councils cannot

| Class | Example | Per-phase miss reason |
|---|---|---|
| Answer leakage | Correct derived figure `$117,000` appears verbatim in an email body the prompt asks the agent to read | S1 didn't see rubric values; S3 didn't see prompt body |
| Rubric-OE mismatch | Rubric checks a figure that no OE step ever discovers | S2 didn't see rubrics; S3 didn't trace back to OEs |
| Hardness regression | HARDNESS picked Lever 7 (thread-reply invisibility) but the OE list discovers the reply at depth 1 | S2 didn't re-verify lever triggering |
| Cross-artifact entity drift | Prompt references `Andrea Phil`, OE references `Andrea Phil`, rubric references `andrea.phil@brookfieldcpas.com` — fine; but Prompt says `the partner`, OE infers `Steven Perry`, rubric checks `andrea.phil` — entity drift | Per-phase saw consistent local references |
| Implicit-vs-explicit prompt drift | Prompt is implicit ("execute on the figure"), but a rubric expects the agent to "flag the discrepancy first" — agent who executes correctly fails the rubric | S3 didn't model the prompt's framing constraint |
| Tool-call density per artifact-trace | Prompt + OE + rubric set together suggest 32 tool calls, not 40+ | B3 in each phase scored its own artifact's density, not the integrated trace |

## Required inputs

| File | Source |
|---|---|
| `Tasks/<TASK_DIR>/5_Prompt.txt` | S1 + S1.5 output |
| `Tasks/<TASK_DIR>/6_Oracle_Events.txt` | S2 output |
| `Tasks/<TASK_DIR>/7_Rubrics.json` | S3 output |
| `Tasks/<TASK_DIR>/_aux/Hardness_Plan.md` | HARDNESS output (levers + Stump Hypothesis) |
| `Tasks/<TASK_DIR>/_aux/Fact_Ledger.json` | S0 atom surface |
| `Tasks/<TASK_DIR>/_aux/Universe_Index/` | S0 summaries |
| `Tasks/_meta/Learnings.md` | empirical Opus 4.8 failure modes |
| `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` | QC scoring |
| `Reference/Council_Protocol.md` | council instructions |

## Roster (4 perspectives in a single high-rigor sub-agent call)

Council B is the per-phase QC reviewer. PIPELINE FINAL adds a separate **Final Council** call that reads all 4 artifacts holistically. It uses 6 lenses:

| Lens | What it checks |
|---|---|
| **Truthfulness** | Every tight identifier in prompt + OE + rubrics greps to a real row in `Fact_Ledger.json`. Derived figures are recomputable from atoms. Single ground-truth end-state. The correct/derived answer is NEVER stated verbatim in any prompt sentence, OE step, or rubric criterion. |
| **Rubric binding** | Rubrics are atomic; not too-tight (no method-channel lock-in when the prompt named a goal) and not too-loose (exact values MANDATORY for IDs / dates / account numbers / dollar amounts; "approximately" only on truly derived/rounded values; "(or similar)" only on agent freetext). Self-contained. Outcome > Process. Each rubric's `evidence` cites at least one OE step. |
| **Cross-artifact holism** | Every prompt ask traces through OE → rubric and back with nothing missing and nothing extra. Every Hardness lever from `Hardness_Plan.md` is still triggered end-to-end. Entity references consistent across the three artifacts (no drift). The implicit-prompt framing is preserved across the rubric set. |
| **Red-team adversarial** | Can the task be passed by a shortcut path that does not exercise the levers? Can a second valid reading of the prompt flip a write action or final universe state? Is the correct figure recoverable from a single high-quality search the agent will obviously do? Drift sweep: em-dashes, "at least N" without mandate, tool names in rubric titles, Keystone/MoveOps tokens. |
| **Narrative-State + Action-Prescription** (Lens 5) | Every state-implying claim consistent with universe lifecycle + action-prescriptions match record fields OR include explicit override + every OE tool-parameter binding is on the EXACT named tool + every closed-period post has a prerequisite unlock or `late_post_authorization_id`. |
| **Verifier-Fails-Spec Pre-Upload Check** (Lens 6) | For every rubric, simulate `Evals/4_Verifier_Fails_Eval.md` bucket classification IF the rubric failed. Flag high-Bucket-1-risk rubrics (channel lock-in / evidence-stricter / service-metadata-incomplete / AND-bundling / subjective terms / write-verb Process / approximately on IDs / "(or similar)" on exact values / account-number entity-trap / persona-scope drift / per-rubric cross-artifact mismatch). > 20% Bucket_1_Risk = REVISE before upload. |

Use the `oracle` or `ultrabrain` sub-agent. Single call, 6 lenses applied in sequence.

## Hard rules the council enforces (binding gates)

| Rule | Why | Failure type |
|---|---|---|
| Correct derived figure is NEVER stated verbatim in prompt / OE / rubric title / email body / Slack body / document body / Records Vault content | L6 (Learnings.md): agents read full thread depth 100% — stated answer = 100% pass | BLOCKER |
| Every tight identifier in any artifact exists in `Fact_Ledger.json` | Phantom IDs cause hallucinated tool calls or wrong-entity actions | BLOCKER |
| Every Hardness lever from `Hardness_Plan.md` is still triggered by the final artifact set | Lever regression after S2/S3 edits | BLOCKER |
| Integrated tool-call density projection ≥ 50 (design target) / ≥ 40 (absolute floor) | 50+ is the design target; 40+ is the absolute floor below which task fails density on real platform runs | < 40 BLOCKER, 40-49 THIN (per-task justification required from HARDNESS) |
| Outcome > Process count; no rubric has tool name in title; no em-dashes anywhere | V3 framework + project conventions | BLOCKER |
| Entity references consistent across prompt / OE / rubrics | Drift causes the agent to act on the wrong entity | MAJOR |
| Implicit-prompt framing preserved (no rubric demands an investigation step the prompt explicitly says not to do) | L15 + L16 framing constraint | MAJOR |
| OE step count + opening-verb coverage match `OE_Convention_Inventory.json` distribution | Convention drift | MINOR |
| Every state-implying claim in the prompt matches universe lifecycle state | Lens 5 — Narrative-State Consistency (prevents Truthfulness failure pattern from completed-but-claimed-in-progress narratives) | BLOCKER |
| Every prompt action aligns with the relevant universe record's `proposed_resolution` / `recommended_action` / `next_step` field, OR includes explicit override language | Lens 5 — Action-vs-Universe-Prescription (prevents Unique Ground Truth failure from divergent end-states without disambiguation) | BLOCKER |
| Every OE tool-parameter binding is on the EXACT named tool in `8_Server_Tools_Details.json` (per-tool strictness — `late_post_authorization_id` on `oracle_gl_create_journal_entry` is INVALID because that parameter only exists on `oracle_gl_post_journal_entry`) | Lens 5 — Tool-parameter binding (prevents structural API failure across all 6 runs) | BLOCKER |
| Every OE step creating / posting / approving to a lifecycle-locked state (closed period, locked record, expired SLA) includes the prerequisite unlock / authorization step EARLIER in the OE chain | Lens 5 — Lifecycle precondition (prevents `OGL.PERIOD_CLOSED` and similar structural rejections) | BLOCKER |
| ≤ 20% of rubrics surface as Bucket_1_Risk on the verifier-fails-spec simulation | Lens 6 — Verifier-Fails-Spec Pre-Upload Check (catches drift between S3 fixes and S1/S2 not re-triggering; prevents shipping a rubric set where >1-in-5 rubrics would fail-as-Bucket-1-invalid in real runs) | > 20% BLOCKER; ≤ 20% MAJOR-notes |

## Phase-readiness gate (run FIRST)

```
python Validators/phase_ready.py --phase final --task Tasks/<TASK_DIR>
```

Refuses if upstream artifacts are missing. If it STOPs, run the upstream phase first.

## Step 0: Create your TODO list (MANDATORY)

Before any other action, create `Tasks/<TASK_DIR>/_aux/Todos_final.md` listing every step in the Procedure below as a discrete atomic todo. Mark `in_progress` / `completed` as you progress. v11 E1 operator-discipline gate.

## Procedure

1. **Verify upstream artifacts exist.** All three deliverables + Hardness_Plan + Fact_Ledger must be in place.

2. **Run validators first.** `python Validators/validate.py --phase all --task Tasks/<TASK_DIR>` must exit 0 before the council runs. If any FAIL, fix and re-run validators before invoking the council.

3. **Spawn the Final Council** as a single `oracle` (or `ultrabrain`) sub-agent. Prompt template:

```
You are the Final Council on a Brookfield MCP Eval V3 task. You read all 3
deliverables TOGETHER and check cross-artifact consistency + answer leakage +
hardness preservation that per-phase councils cannot see.

INPUTS:
- Tasks/<TASK_DIR>/5_Prompt.txt
- Tasks/<TASK_DIR>/6_Oracle_Events.txt
- Tasks/<TASK_DIR>/7_Rubrics.json
- Tasks/<TASK_DIR>/_aux/Hardness_Plan.md
- Tasks/<TASK_DIR>/_aux/Fact_Ledger.json
- Tasks/<TASK_DIR>/_aux/Universe_Index/
- Tasks/_meta/Learnings.md
- Docs/7_QC_Spec_Doc1.json + Docs/8_QC_Spec_Doc2.md

Apply four lenses in sequence; the verdict is the union.

LENS 1 — Truthfulness
For every tight identifier (channel names, doc IDs, JE IDs, ticket IDs, vendor
and entity names, account numbers, dollar amounts, dates, fiscal periods,
retention codes) in any of the 3 artifacts, grep Fact_Ledger.json. Any miss =
BLOCKER (phantom ID). For every derived figure stated in the prompt or in a
2.1 rubric, verify it is RECOMPUTABLE from Fact_Ledger atoms.
ANSWER-LEAKAGE CHECK: pick the correct derived answer the task is built around
(from Hardness_Plan.md or by inference). String-search the prompt body, every
OE step, every rubric title, and every artifact-body-text the prompt asks the
agent to read for that exact figure. Any hit = BLOCKER.

LENS 2 — Rubric binding
For each rubric:
  - Atomic? (exactly one independent claim)
  - Too-tight? (locks a channel/method/tool path the prompt left open)
  - Too-loose? (vague where the prompt expects an exact value)
  - Self-contained? (judge needs no external lookup)
  - Outcome vs Process category correct?
Verify evidence field cites at least one OE step (Per OE# / See OE#).
Outcome count > Process count.

LENS 3 — Cross-artifact holism
- Forward map: every prompt ask maps to >=1 OE step AND >=1 rubric.
- Reverse map: every OE step + every rubric traces back to a prompt ask.
- Lever map: for each lever in Hardness_Plan.md, name the prompt sentence + OE
  step + rubric that triggers it. Any lever with a missing piece = BLOCKER.
- Entity map: every named persona / entity / account in the prompt is the
  same entity in the OEs and rubrics. Flag drift.
- Density: sketch the integrated agent trajectory and count expected tool
  calls. < 40 = BLOCKER. 40-49 = THIN_DENSITY (acceptable only if HARDNESS
  plan documented per-task justification, otherwise BLOCKS). 50+ = PASS.

LENS 4 — Red-team adversarial
- Can a shortcut path satisfy the prompt without exercising at least 2 of the
  Hardness levers? If yes, name the shortcut.
- Is there a second valid reading of the prompt that produces a different
  write-action set? If yes, name the divergence.
- Can the correct figure be recovered from one obvious search the agent will
  do first? If yes, the trap is too shallow.
- Drift sweep across all 3 files: em-dashes, "at least N" without prompt
  mandate, tool names in rubric titles, Keystone/MoveOps tokens
  (mortgage_los, stripe, @keystonemortgage.com, April 28 2026).

LENS 5 — Narrative-State + Action-Prescription Cross-Artifact Consistency
Read prompt + OE + rubric set TOGETHER and verify:
- Every state-implying claim in the prompt is consistent with universe
  lifecycle state (Fact_Ledger lifecycle atoms + Universe_Split records) AND
  the OE/rubric chain assumes the SAME state. A prompt that says "X is in
  progress" while the rubric expects an "override of X's completed sign-off"
  is a structural fail.
- Every action the prompt prescribes is consistent with the universe's
  record-prescribed actions (proposed_resolution / recommended_action /
  next_step / assigned_to fields). Divergence without explicit override
  language in the prompt is a Unique Ground Truth fail (two valid end states).
- Every OE tool-parameter binding matches the named tool's EXACT parameter
  list in 8_Server_Tools_Details.json (per-tool strictness — the parameter
  must be on THAT tool, not just any tool). Parameter on wrong tool = BLOCKER.
- Every OE step that creates / posts / approves to a lifecycle-locked state
  (closed period, locked record, expired SLA) includes the prerequisite
  unlock / authorization step earlier in the chain. Missing precondition =
  BLOCKER.

LENS 6 — Verifier-Fails-Spec Pre-Upload Check
Read Evals/4_Verifier_Fails_Eval.md mentally. For EVERY rubric in 7_Rubrics.json
ask: IF this rubric failed in a real platform run, would it be classified as
Bucket 1 (Rubric Invalid), Bucket 2 (Judge Error), or Bucket 3 (Legit AF)?

Flag rubrics at HIGH Bucket 1 risk (the rubric itself is the problem if it
fails, not the agent's behavior):
- Channel/method lock-in when prompt used open-ended goal verbs ("notify",
  "reach out", "let X know") — would fail an agent that picked a different
  valid channel.
- Evidence field has stricter values than criterion text (judge grades
  criterion first; evidence is for ambiguity resolution).
- Service metadata incomplete (email rubric without recipient; Slack rubric
  without channel).
- AND-bundling — two independent actions in one rubric; an agent doing one
  but not the other fails the whole rubric ambiguously.
- Subjective terms in criterion (thorough / professional / enough / properly).
- Process rubric with write-action verb in title (should be Outcome 1.1).
- "approximately" in front of an ID, date, account, or exact dollar amount.
- "(or similar)" near an email address, channel name, or exact JE/exception/
  vendor ID.
- Account-number entity-trap (105000 means different things on Brookfield vs
  Northstar vs Acme — rubric must verify per-entity assignment).
- Persona-scope drift — rubric tests a value the persona has no claim to
  when prompt used possessive scope ("my X", "our X").
- Per-rubric cross-artifact mismatch — rubric value disagrees with the
  matching OE step value.

For each high-risk rubric: [BUCKET_1_RISK] rubric[i]: <criterion> -- risk:
<which anti-pattern> -- fix: <how to harden so failure = Bucket 3 Legit AF,
not Bucket 1 Rubric Invalid>.

Threshold: if MORE THAN 20% of rubrics surface as Bucket_1_Risk, the rubric
set is FRAGILE — REVISE before platform upload. <= 20% Bucket_1_Risk = MAJOR
notes (fix where cheap, ship if expensive). 0% Bucket_1_Risk = PASS.

This lens is the LAST CHANCE check before platform upload: per-phase gates
already enforce most of these anti-patterns, but Lens 6 catches drift introduced
by S3 fixes that didn't propagate back to re-trigger S2/S1.

For each inconsistency: [BLOCKER] <one-line issue> -- <file>:<location> --
<exact fix>.

VERDICT:
  PASS   if no BLOCKER hits AND no MAJOR hits >2 AND Lens 6 Bucket_1_Risk <= 20%.
  REVISE otherwise — list each hit as [SEVERITY] <one-line issue> -- <file>:<location> -- <exact fix>.

Save the report to Tasks/<TASK_DIR>/_aux/Council_Reports/FINAL_council.md.
```

4. **Read the verdict.** Two outcomes:

| Verdict | Action |
|---|---|
| `PASS` | Task is cleared for platform upload. Append a one-line entry to `Tasks/_meta/Hardness_Patterns_Log.md`: which levers were selected and confirmed end-to-end. |
| `REVISE` | Apply the fixes IN PLACE. Re-run validators. Re-run PIPELINE FINAL. Iteration cap: **3 REVISE rounds**. After 3, escalate to the user with the full issue list — do NOT silently downgrade or accept. |

5. **Exit criteria.** `Tasks/<TASK_DIR>/_aux/Council_Reports/FINAL_council.md` exists with `VERDICT: PASS` and PASS evidence cited for every hard rule in the table above.

## STOP gate

This phase ends here after `VERDICT: PASS` (or after the 3-REVISE iteration cap is hit). End your response.

Two next-trigger paths:
- `VERDICT: PASS` → user uploads the 4 deliverables to the platform and runs 6 trajectories. After results: `PIPELINE S4 — Tasks/<TASK_DIR>` (paste verifier fails) in a fresh chat, or `PIPELINE REDO — Tasks/<TASK_DIR>` if the task came back too easy / too thin.
- 3 REVISE rounds hit without PASS → end your response with the full issue list. The user decides whether to keep iterating (re-invoke FINAL in a fresh chat) or escalate.

Do NOT proceed to platform-upload guidance or `PIPELINE S4` inside this chat.

**If the user pastes follow-up content in this chat** (verifier fails, a new task, fix attempts on a different deliverable, platform paste-back rubrics, or an unrelated question), do NOT process it. Reply: "This chat is single-shot for the FINAL cross-artifact council. Please open a fresh chat and invoke the appropriate next trigger from the dispatch table." Chaining inside one chat defeats the entire pipeline.

## Bootstrap

Read root `AGENTS.md` first. This phase is mandatory before platform upload — never ship a task without a Final Council PASS. The cross-artifact gate is the last line of defense before the platform reviewer sees the work.
