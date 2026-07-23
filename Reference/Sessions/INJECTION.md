# PIPELINE INJECTION — Session Runbook

**Trigger:** `PIPELINE INJECTION — Tasks/<TASK_DIR>`

**Universe:** StarPM (V4) only. This phase does not apply to Brookfield, Keystone, or MoveOps tasks.

**Position in pipeline:** Runs AFTER HARDNESS (which produces the Injection Plan in `Hardness_Plan.md`) and BEFORE S1. Two-phase: (A) author the injection SQL, (B) audit it via oracle council. Hard gate — no prompt work begins until INJECTION returns PASS.

---

## Purpose

Author task-specific universe injection data based on the HARDNESS-produced Injection Plan, then validate that the injection is structurally sound, temporally consistent, cross-service coherent, naturalistic, reachable by MCP tools, appropriately obscured, and genuinely difficult.

Phase A (Author) writes `9_Universe_inject.sql` directly in this session. Phase B (Audit) fires an oracle sub-agent against the 7-gate eval spec. If the audit fails, the agent revises the SQL inline and re-audits (cap 3 rounds). On PASS, the CB takes the SQL to the platform.

---

## Spec authority

QC spec §4.7 — Universe → Cross-service Coherence (Docs_starpm/7_QC_Spec_Doc1.json, Docs_starpm/8_QC_Spec_Doc2.md) — is the ultimate spec authority on injection quality. §4.7 Fail band disqualifies universe edits that "create contradictions that break solvability or realism AND cause an agent failure" and separately disqualifies injections creating misaligned-data traps between two sources; §4.7 Pass (5) requires "Universe edits (if any) are internally consistent and coherent across services." Related spec sub-dims include §4.8 (Universe → Universe Feasibility (Data Exists)) for reachability and §4.9 (Trajectory → Tool Call Count) as the spec floor the difficulty target sits above.

`Evals_starpm/0_Injection_Quality_Eval.md` is the operational implementation of §4.7 as 7 structural gates (Phases 1-7) plus a difficulty score (Phase 8). `[PROJECT POLICY — cites §4.7; audit-authority chain authorized by plan §7.2]` Every Phase A authoring rule and every Phase B audit gate below cites either §4.7 directly (or a related spec sub-dim) or the specific eval-spec Phase that implements it under §4.7; no injection-quality gate exists in this runbook that lacks that traceability chain.

---

## Prerequisites

Before invoking, verify ALL of these are true:

- [ ] `_aux/Universe.txt` contains `starpm`
- [ ] `_aux/Hardness_Plan.md` exists and contains an `## Injection Plan` section (produced by HARDNESS)
- [ ] `S0_Setup_Report.md` exists in `_aux/` (S0 has completed)
- [ ] `_aux/Universe_Split/` is populated
- [ ] `_aux/Universe_Index/` is populated

If any prerequisite is missing, STOP and print: `INJECTION BLOCKED: <missing item> not yet available. Complete the prerequisite step before invoking INJECTION.`

**Note:** `9_Universe_inject.sql` does NOT need to exist before invoking — this phase creates it. `4_Changelog.json` is provided by the platform after the CB injects there.

---

## Required Reading

| File | Role |
|---|---|
| `Tasks/<TASK_DIR>/_aux/Hardness_Plan.md` | PRIMARY — `## Injection Plan` section drives everything: which services, tables, records, values, and decoys to inject |
| `StarPM_Base_Universe/8_Universe_Schema.json` | Schema — column names, types, NOT NULLs, FKs, enum sets |
| `StarPM_Base_Universe/Data/` | Base universe — sample existing IDs to establish patterns; verify FK targets; check for collisions |
| `StarPM_Base_Universe/7_Server_Tools_Details.json` | MCP tool inventory — reachability planning |
| `Tasks/<TASK_DIR>/_aux/Fact_Ledger.json` | Entity atoms — names, emails, IDs already in use |

---

## Execution

### Phase A — Author

**You (the orchestrating agent) author the SQL directly.** Do not delegate Phase A to a sub-agent — you have the Injection Plan context and need to write correct SQL.

**Step A1: Sample existing IDs per table.**
For every table you will inject into, read 3+ existing records from `StarPM_Base_Universe/Data/` to establish the ID pattern (format, prefix, numbering scheme). Pick the next unused ID that fits the pattern. Never invent IDs that deviate from the established convention. (Implements `Evals_starpm/0_Injection_Quality_Eval.md` Phase 2.1-2.3; traces to §4.7 — Universe → Cross-service Coherence, since ID-pattern mismatch or duplicate IDs create cross-service contradictions.)

**Step A2: Verify FK targets.**
For every foreign key field in the Injection Plan, confirm the referenced record exists in `StarPM_Base_Universe/Data/`. If it does not, either use a correct existing record or add an additional INSERT for the FK target (ordered before the dependent record in the SQL). (Implements eval spec Phase 1.4; traces to §4.7 — a broken FK is a cross-service contradiction — and to §4.8 — Universe → Universe Feasibility (Data Exists), since the injected record's referent must exist to be retrievable.)

**Step A3: Assign timestamps.**
All timestamps must fall within 2026-05-01 to 2026-07-01 (America/Chicago). Business communications (Slack, Gmail) on weekdays only (Mon–Fri). For Slack `ts` fields, compute the UNIX timestamp from the intended datetime and confirm it resolves to a date within the window. Reply timestamps must be strictly greater than parent timestamps. Email `sent_at` must be before `received_at`. (Implements eval spec Phase 2.4 + Phase 3.1-3.4; traces to §4.7 — temporal violations create cross-service contradictions when the timestamp misaligns with related base records.)

**Step A4: Draft text fields.**
Write Slack messages in the casual, short style of existing messages in `#maintenance`, `#leasing`, `#general` in the base universe. Write Gmail email bodies matching the formality and length of existing threads. No corporate filler phrases ("circle back", "per our earlier discussion"), no emojis, no unnaturally long messages. 3+ injected text fields with clear AI-tell patterns = audit failure. (Implements eval spec Phase 5.2-5.8; `[PROJECT POLICY — cites §4.7]` — naturalness is a pipeline-authored gate specific to LLM-authored injections that traces to §4.7 in that AI-tell patterns break "realism" as named in the §4.7 Fail band.)

**Step A5: Write `Tasks/<TASK_DIR>/9_Universe_inject.sql`.**
One SQL statement per record. Include a brief SQL comment (`--`) above each block naming the lever it supports (e.g., `-- L8: subledger-reduction — QB bill for HVAC compressor replacement`). Order: INSERTs for FK-referenced tables first, then dependent records. `[PROJECT POLICY — cites no spec; SQL formatting convention authorized by plan §7.2 (audit against eval spec, retain non-gate procedural conventions)]` FK ordering ensures Step A2 (§4.7 / §4.8) can be satisfied by the SQL executor.

**Step A6 — done.** Phase A ends after the SQL is written. `4_Changelog.json` is NOT authored by the pipeline — it is provided by the platform after the CB executes the SQL there.

---

### Phase B — Audit

Fire an `oracle` sub-agent with the full eval from `Evals_starpm/0_Injection_Quality_Eval.md`. The 7 structural gates (Phase 1-7) and Phase 8 difficulty scoring in the eval spec are the operational implementation of QC spec §4.7 (Universe → Cross-service Coherence) plus related sub-dims (§4.8 Universe Feasibility for the Reachability gate, §4.9 Trajectory → Tool Call Count as the floor the Phase 8 difficulty target sits above). `[PROJECT POLICY — cites §4.7, §4.8, §4.9; audit-delegation contract authorized by plan §7.2]` The sub-agent enforces the eval spec verbatim; the runbook adds no injection-quality gate that is not defined in the eval spec.

**Sub-agent prompt:**

```
You are the INJECTION QUALITY EVALUATOR for a StarPM (V4) task.

TASK DIR: Tasks/<TASK_DIR>
EVAL SPEC: Evals_starpm/0_Injection_Quality_Eval.md
PRIMARY INPUT: Tasks/<TASK_DIR>/9_Universe_inject.sql
CHANGELOG: Tasks/<TASK_DIR>/4_Changelog.json (optional — may not exist yet; use the SQL as primary source if absent)
BASE UNIVERSE: StarPM_Base_Universe/Data/
SCHEMA: StarPM_Base_Universe/8_Universe_Schema.json
TOOL CATALOG: StarPM_Base_Universe/7_Server_Tools_Details.json

TASK:
Execute every phase of the Injection Quality Eval in order (Phase 0 through Phase 9).
The mandatory TODO list in Phase 0 is a hard gate — create and track it before proceeding.
Produce a verdict for each of the 7 structural gates (Phase 1-7) plus the difficulty score
(Phase 8). Save the full report to:
  Tasks/<TASK_DIR>/_aux/Council_Reports/INJECTION_report.md

Final verdict format (at end of report):
  GATE 1 Schema & Structure:      PASS / FAIL — <one-line finding>
  GATE 2 ID Format:               PASS / FAIL — <one-line finding>
  GATE 3 Date & Time:             PASS / FAIL — <one-line finding>
  GATE 4 Cross-Service Consistency: PASS / FAIL — <one-line finding>
  GATE 5 Naturalness:             PASS / FAIL — <one-line finding>
  GATE 6 Reachability:            PASS / FAIL — <one-line finding>
  GATE 7 Pre-Solve Check:         PASS / FAIL — <one-line finding>
  DIFFICULTY SCORE: <composite 1.0-5.0> / RATING: <Too Easy|Medium|Hard|Very Hard>
  OVERALL VERDICT: PASS / FAIL
  BLOCKER ISSUES: <specific fix instructions per gate, or "none">
```

---

### Revision Loop (if FAIL)

If the oracle returns FAIL or difficulty < 3.5 (per eval spec Phase 8, which enforces §4.7 → §4.9 traceability):

1. Read `_aux/Council_Reports/INJECTION_report.md` and extract the BLOCKER ISSUES list.
2. Revise `9_Universe_inject.sql` in place to address every listed blocker.
3. Re-fire the oracle audit sub-agent against the revised files.
4. Repeat until PASS or the cap is reached (3 revision rounds total). `[PROJECT POLICY — cites no spec; 3-round revision cap authorized by plan §7.2 as a procedural termination bound]` The cap prevents unbounded revision loops when the underlying Injection Plan is fundamentally flawed; the fallback is to re-run HARDNESS with an amended plan.

**After 3 failed rounds:** STOP. Print the final `INJECTION_report.md` blocker list and tell the user:

```
INJECTION BLOCKED after 3 revision rounds.
Manual intervention required — review blockers in:
  Tasks/<TASK_DIR>/_aux/Council_Reports/INJECTION_report.md

Options:
  (a) Amend the ## Injection Plan section in _aux/Hardness_Plan.md to address the structural
      issues, then re-run PIPELINE INJECTION in a fresh chat.
  (b) If the plan is fundamentally flawed (wrong services, unreachable data), re-run
      PIPELINE HARDNESS in a fresh chat to produce a revised Injection Plan.
```

---

## Exit Criteria — INJECTION PASS

When all 7 gates PASS AND difficulty score ≥ 3.5 (eval spec Phase 9 verdict — implementing §4.7 Pass (5) "Universe edits (if any) are internally consistent and coherent across services" with §4.8 feasibility on the Reachability gate and the §4.9 tool-call-count spec floor as the anchor the difficulty target sits above):

1. Print the gate summary from `INJECTION_report.md`.
2. Print the following CB instructions verbatim:

```
INJECTION PASS (difficulty: <score> / <rating>)

Next steps for the CB:
1. Open Tasks/<TASK_DIR>/9_Universe_inject.sql — execute it on the platform to inject
   the scenario data into the StarPM task universe.
2. After injection, the platform will provide updated universe data. Paste whichever
   the platform exports into Tasks/<TASK_DIR>/:
     - 3_UniverseDataForThisTask.json (full post-injection snapshot — preferred), and/or
     - 4_Changelog.json (structured change manifest)
   At minimum one of these must be present before the next step.
3. Then invoke in a fresh chat:
     PIPELINE INJECT-CHECKER — Tasks/<TASK_DIR>
   INJECT-CHECKER will verify every injected record landed correctly and auto-rebuild
   _aux/Universe_Split/ on PASS. Do NOT manually run data.py — INJECT-CHECKER does it.
```

---

## Output Files

| File | Written by | When |
|---|---|---|
| `Tasks/<TASK_DIR>/9_Universe_inject.sql` | Phase A — this session | Before Phase B |
| `Tasks/<TASK_DIR>/4_Changelog.json` | Platform (after CB injection) | After CB executes SQL on platform |
| `Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json` | Platform (after CB injection) | After CB executes SQL on platform |
| `Tasks/<TASK_DIR>/_aux/Council_Reports/INJECTION_report.md` | Phase B — oracle sub-agent | After each audit round |

---

## How INJECTION fits in the full StarPM pipeline

```
PIPELINE NEW       — scaffold task folder
PIPELINE S0        — split base universe, build index + fact ledger
PIPELINE HARDNESS  — lever identification + injection planning → _aux/Hardness_Plan.md
PIPELINE INJECTION — THIS PHASE:
                     Phase A: author 9_Universe_inject.sql
                     Phase B: oracle audit (7 structural gates + difficulty score)
                     Revise loop if FAIL (cap 3 rounds)
                   ← CB takes 9_Universe_inject.sql to platform, executes it
                   ← CB pastes back 3_UniverseDataForThisTask.json (post-injection snapshot)
PIPELINE INJECT-CHECKER — verifies all records landed, auto-rebuilds _aux/Universe_Split/
PIPELINE S1        — prompt authoring (BLOCKED until INJECT-CHECKER PASS)
PIPELINE S1.5      — linter blocker handling (if needed)
PIPELINE S2        — oracle events
PIPELINE S3        — rubrics
PIPELINE FINAL     — cross-artifact holistic review
PIPELINE SUBMISSION_GATE — zero-tolerance final check
PIPELINE S4        — verifier fails (after platform runs, dual-model)
PIPELINE CLOSE     — final sanity check
```

## Bootstrap

Read root `AGENTS.md` first. The PIPELINE HARD RULES apply. `_aux/Hardness_Plan.md → ## Injection Plan` is the single source of truth for what to inject — do not deviate from it without documenting a specific reason in `INJECTION_report.md`.
