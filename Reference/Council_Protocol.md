# Council Protocol

Every deliverable (S1 prompt, S2 OEs, S3 rubrics, REVIEW intake) must pass two councils before shipping. Validators run first as a cheap gate. Councils run after. Both councils must return GO with zero Major issues.

Each council is one sub-agent call but enumerates **multiple perspectives** in its prompt template. The structure: Council A covers 2 perspectives (A1 Grounding, A2 Convention). Council B covers 4 perspectives (B1 QC Scoring, B2 Adversarial Alt-Path, B3 Tool-Call Density, B4 Hardness Preservation). This is the "multi-council" coverage from every perspective without paying for 6 separate sub-agent calls per deliverable.

---

## Council A — Grounding and Convention

**Role:** verifies every concrete claim in the deliverable is backed by the per-task `_aux/Universe_Split/` AND that the deliverable matches V3 reference conventions.

**Tool:** `explore` sub-agent.

**Inputs:**
- The deliverable file
- `_aux/Universe_Split/*` (the only universe source of truth)
- `_aux/Universe_Index/*` (cheap lookups)
- `Reference/<Prompt|OE|Rubric>_Format.md`
- `Reference/Strict_Convention_Inventory.json` (rubric phase)
- `Reference/OE_Convention_Inventory.json` (OE phase)
- 2 to 3 sample V3 reference files for the phase

**Perspectives covered (single prompt template, both must pass):**

### A1 — Grounding sweep
For every dollar amount, email, JE id, exception id, recon id, vendor id, AP invoice id, document id, Linear issue id, Airtable record id, account number, retention code, classification, persona / NPC name, period id, and date in the deliverable, confirm the value appears in `_aux/Universe_Split/`. For each: `VALUE → FILE:RECORD_INDEX (or NOT FOUND)`.

### A2 — Convention sweep
Compare the deliverable's structure (phrasing patterns, field shapes, qualifier usage, opening-phrase patterns, parameter-naming conventions) against:
- `Reference/<phase>_Format.md`
- The relevant inventory file (`Strict_Convention_Inventory.json` for rubrics, `OE_Convention_Inventory.json` for OEs)
- The sample V3 reference files.
Flag any structural drift.

**Prompt template:**

```
You are Council A — Grounding and Convention.

DELIVERABLE: <path>
PHASE: <prompt | oe | rubrics>
PER-TASK UNIVERSE: Tasks/<TASK_DIR>/_aux/Universe_Split/
INDEX: Tasks/<TASK_DIR>/_aux/Universe_Index/
FORMAT CARD: Reference/<phase>_Format.md
INVENTORY: Reference/{Strict_Convention_Inventory.json | OE_Convention_Inventory.json}
SAMPLES: QC_Tasks/V3_Tasks/Task11..Task14/{Rubrics.json | Oracle_Events.txt | Prompt.txt}

TASK:

[A1 — Grounding] For every concrete claim in the deliverable, verify against
the per-task universe split. Output: VALUE -> FILE:RECORD_INDEX (or NOT FOUND).

[A2 — Convention] Compare structure against the format card, inventory, and
sample V3 references. Flag any drift.

Verdict:
  GO: zero ungrounded claims AND zero convention drift on Major fields.
  BLOCK: list each issue with location + fix.

Save to _aux/Council_Reports/<phase>_A_grounding.md.
```

**Pass criteria:**
- A1: zero ungrounded concrete claims.
- A2: zero convention drift on Major fields (rubric category, agent-centric phrasing, tool names in title, "at least N" without prompt mandate, OE numbered-prose format, OE parameter traps).

---

## Council B — Adversarial QC + Density + Hardness Preservation

**Role:** scores against every applicable QC sub-dim, attempts adversarial moves, projects tool-call density vs the 40+ baseline, and confirms the deliverable still triggers the hardness levers HARDNESS phase selected.

**Tool:** `oracle` (or `ultrabrain` for S3 rubrics phase).

**Inputs:**
- The deliverable file
- The prompt and (for OE / rubrics phases) the upstream deliverables
- `_aux/Hardness_Plan.md` (the lever selection + density projection)
- `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md`
- The relevant phase eval (`Evals/<n>_<phase>_Eval.md`)
- `_aux/Universe_Index/*`

**Perspectives covered (single prompt template, all four must pass):**

### B1 — QC sub-dim scoring
Score every applicable sub-dimension from `Docs/7_QC_Spec_Doc1.json`. For each: `SUB-DIM → SCORE (1-5) → ONE-LINE REASON`. Bar is 5 on every dim. Any sub-dim < 5 must be explicitly justified against per-task universe state (never against base-universe assumptions).

### B2 — Adversarial alt-path
Sketch a valid agent path that satisfies the prompt intent but would fail an Outcome rubric. If such a path exists, the rubric is over-specific OR the prompt has a second valid reading that the rubric set doesn't cover.

For S1 prompt phase: also attempt a second-reading attack. Read the prompt with a different but reasonable interpretation. Does it produce a different set of write actions, a different recipient, or a different final universe state? If yes, the prompt fails Unique Ground Truth or Clarity & Specificity.

### B3 — Tool-call density projection
Sketch the trajectory a competent Opus 4.8 agent would take to satisfy the deliverable. Count expected tool calls. The bar is **40+ on average across 6 runs**. The HARDNESS phase produced a projected midpoint; this perspective re-validates that the deliverable as written still hits that target.

If sketch produces < 40 tool calls: flag as `INSUFFICIENT_DENSITY` — the deliverable does not meet the tool-call baseline. For S1 prompt phase, this means the prompt is too lean and must be expanded with more asks or more service breadth. For S2 OE phase, this means the OE list is too thin (a competent agent would not need all the steps). For S3 rubrics phase, the rubric set under-covers the trajectory.

### B4 — Hardness preservation
For each lever selected in `_aux/Hardness_Plan.md`, verify the deliverable still triggers it.
- S1 prompt phase: does the prompt's framing actually surface each lever to the agent? (e.g., if Lever 3 is "missing reply", does the prompt's situation naturally lead the agent to search for replies?)
- S2 OE phase: does at least one OE step exercise each lever?
- S3 rubrics phase: does at least one Outcome rubric depend on the agent traversing the lever to satisfy it?

If any lever is no longer triggered, flag `HARDNESS_REGRESSION` — the deliverable lost a lever the prompt was designed around.

### B5 — Tool-leak / phrasing scan (lightweight)
Search the deliverable for tool names in forbidden positions, internal IDs in the prompt, em-dashes / en-dashes, "at least N" phrases, "approximately" misuse, "(or similar)" near exact values. Report each hit.

**Prompt template:**

```
You are Council B — Adversarial QC + Density + Hardness Preservation.

DELIVERABLE: <path>
PHASE: <prompt | oe | rubrics>
PROMPT: <path>
OE: <path> (if reviewing rubrics)
HARDNESS PLAN: Tasks/<TASK_DIR>/_aux/Hardness_Plan.md
QC SPEC: Docs/7_QC_Spec_Doc1.json + Docs/8_QC_Spec_Doc2.md
PHASE EVAL: Evals/<n>_<phase>_Eval.md
UNIVERSE INDEX: Tasks/<TASK_DIR>/_aux/Universe_Index/

TASK:

[B1] QC sub-dim scoring. For each sub-dim in the QC spec, output:
SUB-DIM -> SCORE (1-5) -> ONE-LINE REASON. Bar is 5 on every dim.

[B2] Adversarial alt-path. Sketch a valid agent path that fails an Outcome
rubric (or a second valid reading of the prompt that flips a write action).
If found, name the divergence.

[B3] Tool-call density projection. Sketch the trajectory and count expected
tool calls. The bar is 40+. If sketch produces < 40, flag INSUFFICIENT_DENSITY.

[B4] Hardness preservation. For each lever in Hardness_Plan.md, verify the
deliverable still triggers it. If any lever is no longer triggered, flag
HARDNESS_REGRESSION with the missing lever.

[B5] Tool-leak / phrasing scan. Report any tool name in title (rubrics) or
prompt body, internal IDs in the prompt, em-dashes, 'at least N' without
mandate, 'approximately' before IDs/dates, '(or similar)' near exact values.

Verdict:
  GO: every QC sub-dim >= 5 (or NON-FAIL bands explicitly justified by per-
      task universe), AND no adversarial divergence found, AND projected
      tool calls >= 40, AND every Hardness lever still triggered, AND no
      phrasing hits.
  BLOCK: list each Major / Moderate issue with the perspective cited (B1-B5)
         and the fix.

Save to _aux/Council_Reports/<phase>_B_adversarial.md.
```

**Pass criteria:**
- B1: every applicable QC sub-dim scores 5 (or 3-4 is explicitly justified against per-task universe state).
- B2: returns "no divergence found".
- B3: projected tool calls ≥ 40.
- B4: every lever from Hardness_Plan.md is still triggered.
- B5: returns "no hits".

---

## Both councils must GO before the deliverable ships

If either returns BLOCK:
1. Apply the fixes.
2. Re-run the validator.
3. Re-run BOTH councils (not just the one that blocked).
4. Loop until clean.

Do not negotiate with a BLOCK by editing the rubric to make it lenient. Tighten the deliverable. The councils exist precisely because the bar is 5/5 on every QC dim and 40+ tool calls minimum.

---

## When BOTH councils GO but density still feels marginal

If Council B's B3 returns "exactly 40" or "40-42 midpoint", consider:
- Adding one more write action to push the floor higher.
- Adding one more lever to widen the projected range.

A target midpoint of 50+ is the comfortable zone. 40 is the floor.
