# PIPELINE HARDNESS — Lever Scan + Stump Hypothesis + Tool-Call Density

Triggered by: `PIPELINE HARDNESS — Tasks/<TASK_DIR>`

## What this phase does

Reads the per-task universe and identifies which Opus-4.8 stumping levers are present without any universe edits. Projects expected tool-call density across the 6 final runs. Produces a `Hardness_Plan.md` that the S1 prompt-writing phase consumes verbatim.

**Two hard gates: INSUFFICIENT_LEVERS (< 3 levers) and INSUFFICIENT_DENSITY (< 40 projected tool calls).** Either stops the pipeline and forces user intervention.

## Required inputs

| File | Source |
|---|---|
| `Tasks/<TASK_DIR>/PersonaBrief.txt` | S0 produced |
| `Tasks/<TASK_DIR>/2_Persona.txt` | user-pasted |
| `Tasks/<TASK_DIR>/1_Business_Function.txt` | user-pasted |
| `Tasks/<TASK_DIR>/_aux/Universe_Split/*` | S0 produced |
| `Tasks/<TASK_DIR>/_aux/Universe_Index/*` | S0 produced |
| `Reference/Hardness_Playbook.md` | the 11-lever catalog with per-lever tool-call costs |

## Procedure

1. **Spawn a deep-reasoning sub-agent** (`oracle` or `ultrabrain`). Pass it:
   - The 11-lever catalog from `Reference/Hardness_Playbook.md` with tool-call costs
   - All 5 files in `_aux/Universe_Index/`
   - Direct access to grep `_aux/Universe_Split/`
   - The persona brief, persona name, business function

2. **Sub-agent task: lever scan.** For each of the 11 levers, the sub-agent answers:
   - Is this lever present in the per-task universe? (yes / no / partial)
   - If yes, what specific records back it? Cite by file + record index (or inner row id).
   - One short paragraph: how would the prompt engineer this lever into a natural ask?

3. **Sub-agent task: select levers.** Pick the 3 to 5 strongest. Maximize independence (don't pick 3 latching variants). Pair structured-DB-skip with multi-write where possible.

4. **Sub-agent task: tool-call density projection.** Sum:
   - Base discovery: 5 to 8 tool calls
   - Per selected lever: use the cost ranges from `Reference/Hardness_Playbook.md`
   - Write actions: 9 to 12 (assuming 3+ writes × ~3 supporting reads each)
   - Cross-service triangulation buffer: 5 to 8
   - **Total range estimate.** Use the midpoint of each range.

5. **Sub-agent task: stump hypothesis.** Given the available levers, predict 2 to 4 specific rubric outcomes Opus 4.8 will most likely miss across the 6 final runs. Each prediction needs:
   - The specific failure (which fact, which write action, which entity confusion).
   - Confidence (high / med / low) with one-line reasoning citing levers.
   - The mechanism (latching, structured-DB skip, missing reply, etc.).

6. **Produce `_aux/Hardness_Plan.md`** with these sections:

   ```markdown
   # Hardness Plan

   ## Persona and Business Function
   - <persona name> (<role>)
   - <business function>

   ## Levers Available
   | # | Lever | Status | Evidence | Cost range |
   |---|---|---|---|---|
   | 1 | Latching | yes / no / partial | <file>:<row_id> ... | 5-8 |
   | ... | ... | ... | ... | ... |

   ## Selected Levers (3 to 5)
   - Lever <n> — <one-line rationale> — projected cost <midpoint>
   - ...

   ## Tool-Call Density Projection
   | Component | Range | Midpoint |
   |---|---|---|
   | Base discovery | 5-8 | 6.5 |
   | Lever <n> | <range> | <mid> |
   | ... | ... | ... |
   | Write actions (3+ writes) | 9-12 | 10.5 |
   | Cross-service buffer | 5-8 | 6.5 |
   | **TOTAL projected** | <low>-<high> | <midpoint> |

   **Gate:** midpoint ≥ 40 = PASS. Midpoint < 40 = INSUFFICIENT_DENSITY.

   ## Stump Hypothesis (2 to 4 predictions)
   1. [HIGH] <prediction>. Mechanism: <lever>. Reasoning: <one line>.
   2. [MED] ...

   ## Hardness Score
   <selected>/5 — <PASS | INSUFFICIENT_LEVERS | INSUFFICIENT_DENSITY>

   ## Hardness Brief for the Prompt Writer
   <one tight paragraph the S1 sub-agent will use, naming the selected levers and the projected tool-call density target>
   ```

7. **Gates.** Stop the pipeline if any of:
   - **Fewer than 3 levers available** → `INSUFFICIENT_LEVERS (n/5)` — user must edit the universe or pick a different task.
   - **Projected tool-call midpoint < 40** → `INSUFFICIENT_DENSITY (n/40)` — pick more levers (4-5 instead of 3), expand the write-action mix (add Records Vault / Linear / Airtable writes), or both. If even the maximum lever combination cannot reach 40, the per-task universe is too thin and the user must decide whether to continue.
   - Print a clear `STOP: <reason>` message to the chat.

## Exit criteria

- `_aux/Hardness_Plan.md` exists with all 6 sections.
- At least 3 levers selected (PASS) OR explicit `INSUFFICIENT_LEVERS`.
- Projected tool-call midpoint ≥ 40 (PASS) OR explicit `INSUFFICIENT_DENSITY`.

## Next phase

`PIPELINE S1 — Tasks/<TASK_DIR>` (unless INSUFFICIENT — user must intervene first)

## Bootstrap

Read root `AGENTS.md` first. The PIPELINE HARD RULES apply. The per-task universe is the only source of truth — base universe descriptions of "what scenarios exist" are stale.
