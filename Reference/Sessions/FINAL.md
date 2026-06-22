# PIPELINE FINAL — Cross-Artifact Holistic Council

**Trigger:** `PIPELINE FINAL — <TASK_DIR>`

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
| `<TASK_DIR>/5_Prompt.txt` | S1 + S1.5 output |
| `<TASK_DIR>/6_Oracle_Events.txt` | S2 output |
| `<TASK_DIR>/7_Rubrics.json` | S3 output |
| `<TASK_DIR>/_aux/Hardness_Plan.md` | HARDNESS output (levers + Stump Hypothesis) |
| `<TASK_DIR>/_aux/Fact_Ledger.json` | S0 atom surface |
| `<TASK_DIR>/_aux/Universe_Index/` | S0 summaries |
| `Submitted-Tasks/_meta/Learnings.md` | empirical Opus 4.8 failure modes |
| `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` | QC scoring |
| `Reference/Council_Protocol.md` | council instructions |

## Roster (4 perspectives in a single high-rigor sub-agent call)

Council B is the per-phase QC reviewer. PIPELINE FINAL adds a separate **Final Council** call that reads all 4 artifacts holistically. It uses 4 lenses:

| Lens | What it checks |
|---|---|
| **Truthfulness** | Every tight identifier in prompt + OE + rubrics greps to a real row in `Fact_Ledger.json`. Derived figures are recomputable from atoms. Single ground-truth end-state. The correct/derived answer is NEVER stated verbatim in any prompt sentence, OE step, or rubric criterion. |
| **Rubric binding** | Rubrics are atomic; not too-tight (no method-channel lock-in when the prompt named a goal) and not too-loose (exact values MANDATORY for IDs / dates / account numbers / dollar amounts; "approximately" only on truly derived/rounded values; "(or similar)" only on agent freetext). Self-contained. Outcome > Process. Each rubric's `evidence` cites at least one OE step. |
| **Cross-artifact holism** | Every prompt ask traces through OE → rubric and back with nothing missing and nothing extra. Every Hardness lever from `Hardness_Plan.md` is still triggered end-to-end. Entity references consistent across the three artifacts (no drift). The implicit-prompt framing is preserved across the rubric set. |
| **Red-team adversarial** | Can the task be passed by a shortcut path that does not exercise the levers? Can a second valid reading of the prompt flip a write action or final universe state? Is the correct figure recoverable from a single high-quality search the agent will obviously do? Drift sweep: em-dashes, "at least N" without mandate, tool names in rubric titles, Keystone/MoveOps tokens. |

Use the `oracle` or `ultrabrain` sub-agent. Single call, 4 lenses applied in sequence.

## Hard rules the council enforces (binding gates)

| Rule | Why | Failure type |
|---|---|---|
| Correct derived figure is NEVER stated verbatim in prompt / OE / rubric title / email body / Slack body / document body / Records Vault content | L6 (Learnings.md): agents read full thread depth 100% — stated answer = 100% pass | BLOCKER |
| Every tight identifier in any artifact exists in `Fact_Ledger.json` | Phantom IDs cause hallucinated tool calls or wrong-entity actions | BLOCKER |
| Every Hardness lever from `Hardness_Plan.md` is still triggered by the final artifact set | Lever regression after S2/S3 edits | BLOCKER |
| Integrated tool-call density projection ≥ 40 | 40+ is the binding floor | BLOCKER |
| Outcome > Process count; no rubric has tool name in title; no em-dashes anywhere | V3 framework + project conventions | BLOCKER |
| Prompt's primary work-content matches the assigned business function category (per `Docs/5_Prompt_Diversity_Business_Function.md`). Persona-fit (whether the persona is plausible for the work) is a SEPARATE Persona-dim check and does NOT satisfy this gate. | Pre-2026-06 misses traced to reasoning "persona fits, therefore function fits"; the two are independent sub-dims in `Docs/7_QC_Spec_Doc1.json` | BLOCKER |
| Entity references consistent across prompt / OE / rubrics | Drift causes the agent to act on the wrong entity | MAJOR |
| Implicit-prompt framing preserved (no rubric demands an investigation step the prompt explicitly says not to do) | L15 + L16 framing constraint | MAJOR |
| Every per-phase Council B report (`_aux/Council_Reports/prompt_B_adversarial.md`, `oe_B_adversarial.md`, `S3_B_adversarial.md`) scored every QC spec sub-dim for its phase. No sub-dim silently dropped; no invented sub-dim substituted. | Council B sub-agents have historically dropped real sub-dims (e.g. Business Function, Alignment with Today's Date) and invented non-spec substitutes (e.g. Pre-Solving, Naturalness, Write-Action Diversity) | MAJOR |
| OE step count + opening-verb coverage match `OE_Convention_Inventory.json` distribution | Convention drift | MINOR |

## Phase-readiness gate (run FIRST)

```
python Validators/phase_ready.py --phase final --task <TASK_DIR>
```

Refuses if upstream artifacts are missing. If it STOPs, run the upstream phase first.

## Procedure

1. **Verify upstream artifacts exist.** All three deliverables + Hardness_Plan + Fact_Ledger must be in place.

2. **Run validators first.** `python Validators/validate.py --phase all --task <TASK_DIR>` must exit 0 before the council runs. If any FAIL, fix and re-run validators before invoking the council.

3. **Spawn the Final Council** as a single `oracle` (or `ultrabrain`) sub-agent. Prompt template:

```
You are the Final Council on a Brookfield MCP Eval V3 task. You read all 3
deliverables TOGETHER and check cross-artifact consistency + answer leakage +
hardness preservation that per-phase councils cannot see.

INPUTS:
- <TASK_DIR>/5_Prompt.txt
- <TASK_DIR>/6_Oracle_Events.txt
- <TASK_DIR>/7_Rubrics.json
- <TASK_DIR>/_aux/Hardness_Plan.md
- <TASK_DIR>/_aux/Fact_Ledger.json
- <TASK_DIR>/_aux/Universe_Index/
- Submitted-Tasks/_meta/Learnings.md
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
  calls. < 40 = BLOCKER.
- BF map: confirm the prompt's primary work-content falls within the
  assigned business function category (read 1_Business_Function.txt, then
  match against Docs/5_Prompt_Diversity_Business_Function.md). Persona-fit
  alone is NOT sufficient — the WORK must fit the category. Mismatch =
  BLOCKER. Common pitfall: a persona who plausibly authors the task does
  not make the task's work-content fit the assigned function.
- Council coverage: confirm every per-phase Council B report scored every
  QC spec sub-dim for its phase (12 for prompt, 2 for OE, 5 for rubrics).
  Any silent drop or invented sub-dim = MAJOR.

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

VERDICT:
  PASS   if no BLOCKER hits AND no MAJOR hits >2.
  REVISE otherwise — list each hit as [SEVERITY] <one-line issue> -- <file>:<location> -- <exact fix>.

Save the report to <TASK_DIR>/_aux/Council_Reports/FINAL_council.md.
```

4. **Read the verdict.** Two outcomes:

| Verdict | Action |
|---|---|
| `PASS` | Task is cleared for platform upload. Append a one-line entry to `Submitted-Tasks/_meta/Hardness_Patterns_Log.md`: which levers were selected and confirmed end-to-end. |
| `REVISE` | Apply the fixes IN PLACE. Re-run validators. Re-run PIPELINE FINAL. Iteration cap: **3 REVISE rounds**. After 3, escalate to the user with the full issue list — do NOT silently downgrade or accept. |

5. **Exit criteria.** `<TASK_DIR>/_aux/Council_Reports/FINAL_council.md` exists with `VERDICT: PASS` and PASS evidence cited for every hard rule in the table above.

## STOP gate

This phase ends here after `VERDICT: PASS` (or after the 3-REVISE iteration cap is hit). End your response.

Two next-trigger paths:
- `VERDICT: PASS` → user uploads the 4 deliverables to the platform and runs 6 trajectories. After results: `PIPELINE S4 — <TASK_DIR>` (paste verifier fails) in a fresh chat, or `PIPELINE REDO — <TASK_DIR>` if the task came back too easy / too thin.
- 3 REVISE rounds hit without PASS → end your response with the full issue list. The user decides whether to keep iterating (re-invoke FINAL in a fresh chat) or escalate.

Do NOT proceed to platform-upload guidance or `PIPELINE S4` inside this chat.

## Bootstrap

Read root `AGENTS.md` first. This phase is mandatory before platform upload — never ship a task without a Final Council PASS. The cross-artifact gate is the last line of defense before the platform reviewer sees the work.
