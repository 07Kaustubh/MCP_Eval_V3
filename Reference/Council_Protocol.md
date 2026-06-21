# Council Protocol

Every deliverable (S1 prompt, S2 OEs, S3 rubrics, REVIEW intake) must pass two councils before shipping. Validators run first as a cheap gate. Councils run after. Both councils must return GO with zero Major issues.

Each council is one sub-agent call but enumerates **multiple perspectives** in its prompt template. The structure: Council A covers 2 perspectives (A1 Grounding, A2 Convention). Council B covers 6 perspectives (B1 QC Scoring, B2 Adversarial Alt-Path, B3 Tool-Call Density, B4 Hardness Preservation, B5 Tool-Leak / Phrasing Scan, B6 Upstream Propagation). This is the "multi-council" coverage from every perspective without paying for 6 separate sub-agent calls per deliverable.

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

### B6 — Upstream propagation
When you find an issue that originates in an UPSTREAM artifact (not the one under review), flag it with a `PROPAGATE TO <PHASE>: ...` tag instead of patching it downstream. The principle: fix the issue at the phase where the root cause lives, then re-run downstream phases. Patching a downstream artifact to paper over an upstream root cause silently embeds the bug forever.

Concrete trigger examples:

- During **S2 OE review**, you notice the prompt has a truthfulness gap (a claim that does not ground to `Fact_Ledger.json` or a second valid reading the prompt allows that flips a write action) → flag `PROPAGATE TO S1: prompt has <issue> — re-run S1 to fix, do not patch the OE around it`.
- During **S2 OE review**, you notice a Hardness lever the prompt was supposed to surface is no longer visible to the agent under the prompt's framing → flag `PROPAGATE TO S1: prompt framing kills Lever <n>, OE cannot trigger it post-hoc`.
- During **S3 rubric review**, you notice an OE step expects a tool parameter that does not match `8_Server_Tools_Details.json` or references a record that is not in `_aux/Universe_Split/` → flag `PROPAGATE TO S2: OE<n> has <issue> — re-run S2 to fix, do not encode the wrong value into the rubric`.
- During **S3 rubric review**, you notice the prompt's framing is implicit ("execute on the figure") but the rubric set demands an explicit investigation step ("flag the discrepancy first") → flag `PROPAGATE TO S1: prompt framing mismatch — re-frame the prompt to make the investigation step explicit, OR drop the rubric (do not silently keep both)`.
- During **FINAL holistic review**, any cross-artifact issue that traces to a root cause in S1 or S2 → flag `PROPAGATE TO <S1|S2>: ...` with the exact upstream sentence / step at fault.

Output format for each finding: `PROPAGATE TO <PHASE>: <one-line root cause> -- upstream file:location -- recommended upstream fix`.

A B6 finding is BLOCKING — the deliverable under review cannot ship until the upstream phase has been re-run with the fix and the downstream phase re-run on the fresh upstream artifact. Do NOT accept "fix it in place at the current phase" as an alternative when the root cause is upstream.

### Role-Lens Anchoring (apply across B1-B5)

Each B perspective is reviewed through five role lenses — read the deliverable five times, once per lens, and combine findings. This is a single sub-agent call but the prompt forces multi-perspective coverage so single-model blind spots are caught.

| Lens | Question to ask | Maps strongest to |
|---|---|---|
| **Architect** | Does the deliverable's structure fit the V3 framework cleanly? Are the abstractions right? | B1, B4 |
| **Implementer** | Will this actually run? Every tool name real, every ID format valid, every recipient resolvable? | B5 |
| **Red-team** | How do I break this? What's the most adversarial valid agent path? What's the second valid reading? | B2 |
| **Ground-truth** | Is every claim in the deliverable grounded in this task's universe (per-task SSoT)? Any base-universe assumption? | B1, B5 |
| **Integration** | Does this deliverable hold together with the upstream ones? Prompt-OE-rubrics consistency? Hardness levers preserved end to end? Any issue whose root cause is in an upstream artifact rather than the one under review? | B3, B4, B6 |

A `BLOCK` from any lens propagates to the perspective it maps to. The verdict is the union of all five lens reads, not the average.

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

Apply five role lenses across the perspectives below. Read the deliverable
five times, once per lens, and combine findings (the verdict is the union):

  Architect     - structural fit to V3 framework, abstractions, cohesion
  Implementer   - will it run? real tool names, valid ID formats, resolvable recipients
  Red-team      - how to break it? adversarial valid path? second valid prompt reading?
  Ground-truth  - every claim grounded in PER-TASK universe (Fact_Ledger.json, Universe_Split/)?
  Integration   - prompt-OE-rubrics consistency, hardness levers preserved end-to-end

A BLOCK from any lens propagates to its mapped perspective (B1-B5).

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

[B6] Upstream propagation. For every issue you find whose ROOT CAUSE lives
in an upstream artifact (not the one under review), output:
PROPAGATE TO <PHASE>: <one-line root cause> -- <upstream file:location> --
<recommended upstream fix>.
A B6 finding is BLOCKING. Do NOT accept "fix it in place" as a substitute
when the root cause is upstream — patching downstream silently embeds the
bug. The fix is to re-run the upstream phase and then re-run the current
phase against the fresh upstream output.

Verdict:
  GO: every QC sub-dim >= 5 (or NON-FAIL bands explicitly justified by per-
      task universe), AND no adversarial divergence found, AND projected
      tool calls >= 40, AND every Hardness lever still triggered, AND no
      phrasing hits, AND no PROPAGATE TO <upstream> flags raised.
  BLOCK: list each Major / Moderate issue with the perspective cited (B1-B6)
         and the fix. For B6 findings the fix MUST name the upstream phase
         to re-run.

Save to _aux/Council_Reports/<phase>_B_adversarial.md.
```

**Pass criteria:**
- B1: every applicable QC sub-dim scores 5 (or 3-4 is explicitly justified against per-task universe state).
- B2: returns "no divergence found".
- B3: projected tool calls ≥ 40.
- B4: every lever from Hardness_Plan.md is still triggered.
- B5: returns "no hits".
- B6: returns "no upstream propagation flags". If any `PROPAGATE TO <upstream>` flag is raised, the deliverable is BLOCK — the operator must re-run the named upstream phase, then re-run the current phase against the fresh upstream output. Patching downstream is not an acceptable resolution.

---

## Opt-in: True multi-model Council B (`COUNCIL_MODE=multi`)

The default Council B is one `oracle` sub-agent call applying 5 lenses in sequence. The lenses overlay catches most of what 5 separate model invocations would catch, at 1/5 the cost.

For maximum rigor on a critical task (final deliverable for a benchmark seat, a task that has already been bounced by the platform reviewer, or a 5/5-or-die deliverable), invoke the multi-model variant by prefixing the trigger: `PIPELINE S3 — Tasks/<TASK_DIR> COUNCIL_MODE=multi`. The runbook does this instead:

1. **Spawn 5 sub-agents in parallel**, one per lens, each `read-only`. Each gets the same brief (deliverable + upstream + Hardness_Plan + QC spec + relevant inventory). The model + role assignment:

   | Seat | Lens | Sub-agent | What it owns |
   |---|---|---|---|
   | 1 | Architect | `oracle` | Structural fit to V3 framework, abstractions, cohesion. Maps to B1 + B4. |
   | 2 | Implementer | `oracle` | Will it run? Real tool names, valid ID formats, resolvable recipients. Maps to B5. |
   | 3 | Red-team | `ultrabrain` | How to break it. Adversarial valid path. Second valid prompt reading. Maps to B2. |
   | 4 | Ground-truth | `oracle` | Every claim grounded in PER-TASK universe (`_aux/Fact_Ledger.json`). Maps to B1 + B5. |
   | 5 | Integration | `oracle` | Prompt-OE-rubrics consistency, hardness levers preserved end-to-end. Maps to B3 + B4. |

2. **Each seat returns the same output contract** as the single-call Council B (B1-B5 perspectives), plus a `LENS: <name>` header so the consensus knows the origin.

3. **Crash / empty / quorum.** If a seat errors or returns empty, re-spawn it (up to 2 retries). The round needs ≥ 4 successful seats. If fewer, the round is INVALID — do NOT synthesize a PASS; escalate to the user.

4. **Consensus synthesis.** Spawn a 6th `oracle` sub-agent with the role of CONSENSUS. It receives all 5 seat outputs labeled by lens. Its job:
   - Deduplicate findings across seats.
   - Rank by severity (BLOCKER > MAJOR > MINOR).
   - Resolve disagreements by citing repo evidence (the per-task universe, the QC spec). A seat's verdict without cited evidence is ignored.
   - **Veto propagation.** Any single seat BLOCKER forces REVISE unless the consensus disproves it with cited evidence. Any `UNKNOWN` on a hard constraint counts as REVISE.
   - Output: `VERDICT: PASS | REVISE`, `ROUND VALID: yes/no`, deduped issue list with per-issue fix, proceed recommendation.

5. **Cost note.** Multi-mode is 6 sub-agent calls per Council B invocation vs 1 in default. Use it when the stakes justify the spend.

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
