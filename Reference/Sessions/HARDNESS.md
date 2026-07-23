# PIPELINE HARDNESS — Lever Scan + Stump Hypothesis + Tool-Call Density

Triggered by: `PIPELINE HARDNESS — Tasks/<TASK_DIR>`

## What this phase does

Reads the per-task universe and identifies which Opus-4.8 stumping levers are available. Projects expected tool-call density across the 6 final runs. Produces a `Hardness_Plan.md` that the S1 prompt-writing phase consumes verbatim.

**StarPM (V4) addition:** Because the StarPM base universe is fixed and CBs inject task-specific scenario data, HARDNESS additionally produces an `## Injection Plan` section in `Hardness_Plan.md`. This plan specifies exactly what records to inject — which services, tables, field values, cross-service references, and decoys — to support the chosen levers. The INJECTION phase reads this plan and authors `9_Universe_inject.sql` from it. For V3 universes (Brookfield, Keystone, MoveOps), the injection planning step is skipped entirely.

**Two hard gates: INSUFFICIENT_LEVERS (< 3 levers) and a tiered density gate.** Density bands: midpoint ≥ 50 = PASS (design target — produces ~40+ tool calls in real platform runs); midpoint 40-49 = THIN_DENSITY (operator may continue with explicit per-task justification, but the task is at risk of underflow on real runs); midpoint < 40 = INSUFFICIENT_DENSITY (STOPs the pipeline — operator must expand levers or write actions). INSUFFICIENT_LEVERS or INSUFFICIENT_DENSITY both force user intervention.

## Required inputs

| File | Source |
|---|---|
| `Tasks/<TASK_DIR>/PersonaBrief.txt` | S0 produced |
| `Tasks/<TASK_DIR>/2_Persona.txt` | user-pasted |
| `Tasks/<TASK_DIR>/1_Business_Function.txt` | user-pasted |
| `Tasks/<TASK_DIR>/_aux/Universe_Split/*` | S0 produced |
| `Tasks/<TASK_DIR>/_aux/Universe_Index/*` | S0 produced |
| `Tasks/<TASK_DIR>/_aux/Fact_Ledger.json` | S0 produced |
| `Reference/Hardness_Playbook.md` | the 11-lever catalog with per-lever tool-call costs |
| `Tasks/_meta/Learnings.md` | **READ FIRST** — empirical Opus 4.8 failure-mode evidence. Every lever picked in this phase must cite a Learnings entry that justifies it (or you document a new finding if you try a novel pattern). |
| `Tasks/<TASK_DIR>/_aux/REDO_reason.md` | **READ IF PRESENT** — when HARDNESS is invoked as part of a `PIPELINE REDO` rebuild, this file documents the previous attempt's specific failure (pass@1 > 40% / density < 40 / FINAL BLOCKER). The new lever selection MUST address that specific failure — don't pick the same lever combination that already failed. |
| `Tasks/<TASK_DIR>/_aux/Candidate_Originals/` | **READ IF PRESENT** — when invoked via REDO, the archived candidate's originals reveal what the previous attempt looked like. Useful to avoid repeating the same scenario shape. |

## Phase-readiness gate (run FIRST)

```
python Validators/phase_ready.py --phase hardness --task Tasks/<TASK_DIR>
```

Refuses if S0 hasn't run. If it STOPs, invoke `PIPELINE S0` first.

## Step 0: Create your TODO list (MANDATORY)

Before any other action, create `Tasks/<TASK_DIR>/_aux/Todos_hardness.md` listing every step in the Procedure below as a discrete atomic todo. Mark `in_progress` / `completed` as you progress. v11 E1 operator-discipline gate.

## Step 0.5: Cross-Source Verification (v16 — MANDATORY before exit)

Before declaring done, write `Tasks/<TASK_DIR>/_aux/Verification_hardness.md` declaring the cross-source check:

```
## Data sources consulted
- _aux/Universe_Split/ :: <which tables sampled for lever scanning>
- _aux/Fact_Ledger.json :: <amount/email/id counts checked for lever feasibility>
- _aux/Universe_Index/graph_report.md :: <density signals consulted>

## Reference docs consulted
- Reference/Hardness_Playbook.md :: <which of the 11 levers were considered + selected>
- Tasks/_meta/Learnings.md :: <which L<n> entries cited as lever rationale>

## Eval spec sub-dims relevant to this phase
- Trajectory dim Tool Call Count (≥ 15 floor; pipeline targets 50+ midpoint) :: <projected midpoint>

## QC spec sub-dims relevant to this phase
- Trajectory T1 Tool Call Count :: <projected midpoint, band>

## Verification statements
- [ ] At least 3 levers selected; each cites a Learnings.md entry.
- [ ] Density midpoint projection is one of {PASS ≥ 50, THIN 40-49, INSUFFICIENT < 40}.
- [ ] Service breadth table populated (v11 G1).

## Discrepancies surfaced (if any)
- <none / list>
```

## Procedure

1. **Read `Tasks/_meta/Learnings.md` end to end.** This is the mandatory first action of HARDNESS. The entries (L1, L2, ...) calibrate which levers actually fail Opus 4.8 and which are wasted effort. The L1-L7 "does not reliably fail" block is just as important as the L8-L14 "reliably fails" block — picking a single-hop reduction or a near-miss-entity-only trap wastes the task budget.

2. **Spawn a deep-reasoning sub-agent** (`oracle` or `ultrabrain`). Pass it:
   - The 11-lever catalog from `Reference/Hardness_Playbook.md` with tool-call costs
   - The full text of `Tasks/_meta/Learnings.md`
   - All 6 files in `_aux/Universe_Index/` (including `graph_report.md`)
   - `_aux/Fact_Ledger.json` for atom verification
   - Direct access to grep `_aux/Universe_Split/`
   - The persona brief, persona name, business function

3. **Sub-agent task: lever scan.** For each of the 11 levers, the sub-agent answers:
   - Is this lever present in the per-task universe? (yes / no / partial)
   - If yes, what specific records back it? Cite by file + record index (or inner row id).
   - One short paragraph: how would the prompt engineer this lever into a natural ask?
   - Which Learnings entry justifies picking this lever? (cite L<n>).

4. **Sub-agent task: select levers.** Pick the 3 to 5 strongest. Default to the L8 + L9 + L10 anatomy (3 reductions across 3 services + authority-figure dismissal + subledger reduction). Maximize independence (don't pick 3 latching variants). Never rely solely on L4 (near-miss entity) or L5 (action-incompleteness) — Learnings says they are ineffective alone.

   **If `_aux/REDO_reason.md` exists (REDO rebuild):** the new lever combination MUST materially differ from what the previous attempt used. Read the candidate's originals in `_aux/Candidate_Originals/`. If they used L8 + L4 and failed density, drop L4 and replace with L9 + L10 + multi-write density buffer. If they used L8 + L9 and failed difficulty, the issue was probably L6 / L7 (stated answer or binary trap) — verify the new lever set explicitly avoids those failure patterns. Document the lever delta in `Hardness_Plan.md` under a new section `## Lever changes from previous attempt`.

5. **Sub-agent task: tool-call density projection.** Sum:
   - Base discovery: 5 to 8 tool calls
   - Per selected lever: use the cost ranges from `Reference/Hardness_Playbook.md`
   - Write actions: 9 to 12 (assuming 3+ writes × ~3 supporting reads each)
   - Cross-service triangulation buffer: 5 to 8
   - **Total range estimate.** Use the midpoint of each range.

6. **Sub-agent task: stump hypothesis.** Given the available levers, predict 2 to 4 specific rubric outcomes Opus 4.8 will most likely miss across the 6 final runs. Each prediction needs:
   - The specific failure (which fact, which write action, which entity confusion).
   - Confidence (high / med / low) with one-line reasoning citing levers and the Learnings entry.
   - The mechanism (latching, structured-DB skip, missing reply, authority dismissal, etc.).

6a. **(StarPM V4 only) Sub-agent task: Base Universe Investigation Scan.** `[PROJECT POLICY — cites no spec; step 6a scoping and structure authorized by plan §7.1]` Skip this step entirely for Brookfield, Keystone, and MoveOps. For StarPM, produce a `## Base Investigation Surface` section in `Hardness_Plan.md` documenting the natural investigation demand of the base StarPM universe for the target scenario before any injection is planned. Every field below cites a QC spec sub-dimension from `Docs_starpm/7_QC_Spec_Doc1.json` and `Docs_starpm/8_QC_Spec_Doc2.md`, and is grep-verified against `_aux/Universe_Split/`.

   The sub-agent produces four fields:

   - **Natural service touches (cites §4.1 — Prompt → Tool use and Cross-service requirement):** list ≥ 3 StarPM services the scenario naturally requires touching without any injection, each with a one-line evidence pointer to a base universe record. §4.1 Pass (5) requires investigation across 2+ services; the ≥ 3 target sits above the spec floor to lift tool-call density organically under §4.9 (Trajectory → Tool Call Count).
   - **Scattered facts (cites §4.1 — Prompt → Tool use and Cross-service requirement):** list the load-bearing facts the scenario needs and where each one lives in the base universe, showing they are naturally distributed across the ≥ 3 services above. §4.1 Fail band explicitly disqualifies scenarios that "only trivially touches a second service"; the scattered-fact inventory demonstrates non-trivial cross-service reconciliation.
   - **Natural investigation path (cites §4.2 — Prompt → Investigation):** one paragraph describing the discovery arc a competent agent takes through the base universe to reach the correct answer, with no shortcut. §4.2 Pass (5) requires the prompt to "clearly require investigation, and it logically follows from investigation"; documenting the arc before injection prevents pre-solving under the §4.2 Fail band.
   - **Cohesive single-situation grounding (cites §4.3 — Prompt → Coherence):** one sentence naming the single business situation that ties every scattered fact and every service touch together, satisfying §4.3 Pass (5) "One cohesive situation; stacked asks all tie back to the same purpose." §4.3 Fail band disqualifies bolt-on requests; the scan proves the situation is unitary before the prompt is written.

   `[PROJECT POLICY — cites §4.1, §4.2 and §4.9; downstream sequencing authorized by plan §7.1]` The Base Investigation Surface exists so the Injection Plan in Step 6.5 augments the natural surface rather than shortcutting it. Every subsequent injection is scored against whether it preserves the scan's ≥ 3-service touch under §4.1 and its natural investigation path under §4.2, which together keep the projected tool-call midpoint above the §4.9 spec floor.

6.5 **(StarPM V4 only) Sub-agent task: Injection Planning.** Skip this step entirely for Brookfield, Keystone, and MoveOps. For StarPM, the INJECTION phase will author `9_Universe_inject.sql` from this plan — it must be precise enough to write correct SQL without further research. For each selected lever, specify:

   - **Service + table:** which of the 8 StarPM services (gmail, slack, linear, airtable, quickbooks, hubspot, gcalendar, contacts) and which table
   - **Operation:** INSERT (new record) / UPDATE (modify existing) — avoid DELETE unless essential
   - **Records — field list for every injected record:**
     - IDs: describe the naming pattern (e.g., "follow Linear issue format `MT-2026-NNNN`, next unused after sampling base") — do NOT invent specific IDs here; the INJECTION phase will sample base and assign
     - Amounts / dates: specify exact values (e.g., `$4,200`, `2026-06-18`, weekday)
     - Text fields: draft the actual message / email / comment text — short and casual for Slack, natural length for Gmail; no corporate filler, no emojis
     - Foreign key references: name the exact base record this links to (e.g., "link to existing contact `cnt_041` Maria Lopez")
   - **Cross-service references:** for each injected record that mentions another service's entity, name both sides (e.g., "Slack message references Linear ticket `MT-2026-0072` — confirm that ticket exists in base OR plan a matching injection")
   - **Decoys / traps:** for each decoy record, describe what makes it misleading (e.g., "nearly-matching invoice amount $4,020 from a different vendor — correct amount is $4,200")
   - **Reachability path:** name the MCP tool + filter that surfaces this record (e.g., `gmail_search_threads(query="HVAC Las Palmas")`)
   - **Coherence (cites §4.7 — Universe → Cross-service Coherence):** name every base record this injection touches and state one sentence per touch confirming the injected value stays internally consistent with the touched base record on names, dates, amounts, status, and relationships. §4.7 Fail band disqualifies universe edits that "create contradictions that break solvability or realism AND cause an agent failure," and separately disqualifies injections that create misaligned-data traps between two sources; both risk flags must read `zero` before the injection is approved.
   - **Feasibility contribution (cites §4.8 — Universe → Universe Feasibility (Data Exists)):** name the exact required fact this injected record makes retrievable and the tool that will surface it. §4.8 Pass (5) requires "All core facts required to solve the task exist in the universe and are retrievable via tools"; the field forces one-to-one traceability from the injected record to a load-bearing fact the prompt asks for.
   - **Investigation extension (cites §4.2 — Prompt → Investigation):** one sentence describing the natural discovery step an agent takes to reach this record from the Base Investigation Surface arc produced in Step 6a, confirming no shortcut compresses the investigation. §4.2 Fail band disqualifies pre-solving; the field forces the injection to extend the natural investigation arc rather than collapse it.
   - **Cross-service anchor (cites §4.1 — Prompt → Tool use and Cross-service requirement):** name the base service this injected record clusters with and state whether the injection preserves the ≥ 3-service natural touch surface from Step 6a or augments it with an additional service. §4.1 Pass (5) requires investigation across 2+ services; the field prevents an injection from silently collapsing the cross-service surface into a single-service shortcut.

   This plan must be complete enough that the INJECTION phase can write correct SQL without returning to you for clarification. Target Phase 8 difficulty minimums: Cross-Service Spread ≥ 4 services, Tool Call Depth midpoint ≥ 3.5, Reasoning Chain midpoint ≥ 3.5.

7. **Produce `_aux/Hardness_Plan.md`** with these sections:

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

   **Gate (tiered):** midpoint ≥ 50 = PASS (design target); midpoint 40-49 = THIN_DENSITY (continue with per-task justification documented under `## THIN density acceptance` subsection); midpoint < 40 = INSUFFICIENT_DENSITY (STOP).

   ## Service Breadth (v11 G1)
   List each service the projected trajectory exercises with the projected call count per service. Cross-service breadth is a hardness multiplier — 50 calls across 5 services is structurally harder for Opus 4.8 than 50 calls in one service (single-service traps allow context lock-in; multi-service forces persistent cross-correlation).

   **Use the universe-correct service rows.** Read `_aux/Universe.txt` and fill in only the services that exist in that universe:
   - **Brookfield / KeyStone / MoveOps:** oracle_gl, email, slack, records_vault, blackline, linear, airtable, sap, contacts, other
   - **StarPM (V4):** airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack, other

   | Service | Calls | % of total |
   |---|---|---|
   | <service_1> | <n> | <pct> |
   | <service_2> | <n> | <pct> |
   | <service_3> | <n> | <pct> |
   | <service_4> | <n> | <pct> |
   | <service_5> | <n> | <pct> |
   | other | <n> | <pct> |
   | **Distinct services** | **<count>** | — |

   **Breadth gate:** ≥ 4 distinct services with each ≥ 5% of total = PASS; 3 distinct services with the dominant one < 60% = ACCEPTABLE (mark NOTE in plan); ≤ 2 distinct services OR dominant > 60% = `THIN_BREADTH` — the density may meet the floor but the task is structurally lever-thin. Document why the prompt cannot pull in more services (e.g., persona's role is single-domain) under `## THIN breadth acceptance` subsection.

   This catches the false-positive density pattern where the projected 50+ midpoint is achieved by stacking 50 GL calls (a single-service deep trap) instead of the cross-correlation chains that Opus 4.8 actually fails on.

   ## Stump Hypothesis (2 to 4 predictions)
   1. [HIGH] <prediction>. Mechanism: <lever>. Reasoning: <one line>.
   2. [MED] ...

   ## Hardness Score
   <selected>/5 — <PASS | INSUFFICIENT_LEVERS | INSUFFICIENT_DENSITY>

   ## Hardness Brief for the Prompt Writer
   <one tight paragraph the S1 sub-agent will use, naming the selected levers and the projected tool-call density target>

   ## Base Investigation Surface (StarPM V4 only — omit entirely for Brookfield / Keystone / MoveOps)

   **Natural service touches (§4.1):**
   - <service_1> — <one-line evidence pointer to base record>
   - <service_2> — <one-line evidence pointer>
   - <service_3> — <one-line evidence pointer>
   - <additional services if applicable>

   **Scattered facts (§4.1):**
   - <fact_1> lives in <service:table:record> — <one-line description>
   - <fact_2> lives in <service:table:record> — <one-line description>
   - <additional facts>

   **Natural investigation path (§4.2):**
   <one paragraph describing the discovery arc a competent agent takes through the base universe to reach the correct answer, with no shortcut>

   **Cohesive single-situation grounding (§4.3):**
   <one sentence naming the single business situation that ties every scattered fact and every service touch together>

   ## Injection Plan (StarPM V4 only — omit entirely for Brookfield / Keystone / MoveOps)

   ### Lever <n> → Records to inject

   **Service:** <service_name>
   **Table:** <table_name>
   **Operation:** INSERT / UPDATE
   **Fields:**
   - id: <naming pattern — INJECTION will sample base and assign the next unused value>
   - <field>: <exact value>
   - <text_field>: "<exact draft text — short, casual, human-sounding>"
   **Foreign keys:** <e.g., channel_id: C001 #maintenance (existing base record)>
   **Cross-service refs:** <e.g., this email body references QB bill INV-0089 — confirm that bill exists in base>
   **Reachability:** `<tool_name>(param="<filter>")` → record surfaces
   **Decoy record (if any):** <service/table> — <description: what makes it misleading and why it is wrong>
   **Coherence (§4.7):** <base records touched + one-sentence internal-consistency confirmation per touch; misaligned-data risk = zero>
   **Feasibility contribution (§4.8):** <the specific load-bearing fact this record makes retrievable + surfacing tool>
   **Investigation extension (§4.2):** <natural discovery step from the Base Investigation Surface arc; no shortcut>
   **Cross-service anchor (§4.1):** <base service cluster + whether the injection preserves or augments the ≥ 3-service natural touch surface>

   ### Lever <n+1> → Records to inject
   <repeat pattern above>

   ### Injection Summary
   | Service | New records | Tables |
   |---|---|---|
   | <service> | <count> | <table names> |
   | **Total** | **<n>** | — |

   **Phase 8 difficulty targets:** Cross-Service Spread ≥ 4 / Tool Call Depth ≥ 3.5 / Reasoning Chain ≥ 3.5
   ```

8. **Gates.** Tiered handling:
   - **Fewer than 3 levers available** → `INSUFFICIENT_LEVERS (n/5)` — STOP. User has three fallback options: (a) edit the universe to surface more levers, (b) swap to a different persona within the SAME business function (this is allowed in both CB and REVIEW flows — the business function is the fixed scope anchor but persona is flexible; pick a persona whose role surfaces more hardness levers, document the swap in `Hardness_Plan.md` under `## Persona swap`), or (c) pick a different task.
   - **Projected tool-call midpoint < 40** → `INSUFFICIENT_DENSITY (n/40)` — STOP. Pick more levers (4-5 instead of 3), expand the write-action mix (add Records Vault / Linear / Airtable writes), or both. If even the maximum lever combination cannot reach 40, the per-task universe is too thin and the user must decide whether to continue.
   - **Projected tool-call midpoint 40-49** → `THIN_DENSITY (n/50)` — operator decision: either expand to push midpoint to ≥ 50 (preferred — design target produces ~40+ on real runs), OR continue with explicit per-task justification documenting why this task cannot reach 50 (e.g., universe is structurally thin on a specific service). Document the choice in `Hardness_Plan.md` under a new subsection `## THIN density acceptance` if continuing.
   - **Projected tool-call midpoint ≥ 50** → PASS. Proceed to S1.
   - Print a clear `STOP: <reason>` or `PASS` or `THIN: <justification required>` message to the chat.

## Exit criteria

- `_aux/Hardness_Plan.md` exists with all 6 sections.
- At least 3 levers selected (PASS) OR explicit `INSUFFICIENT_LEVERS`.
- Projected tool-call midpoint ≥ 50 (PASS) OR explicit `INSUFFICIENT_DENSITY` (< 40, STOP) OR explicit `THIN_DENSITY` (40-49) with per-task justification documented in `Hardness_Plan.md` under `## THIN density acceptance`.
- **(StarPM V4 only)** `## Base Investigation Surface` section exists in `Hardness_Plan.md` with all four spec-cited fields populated (natural service touches under §4.1, scattered facts under §4.1, natural investigation path under §4.2, cohesive single-situation grounding under §4.3), grep-verified against `_aux/Universe_Split/`. `[PROJECT POLICY — cites §4.1, §4.2, §4.3, §4.7, §4.8; exit-criterion added per plan §7.1]` Every injected record in `## Injection Plan` additionally populates the four downstream spec-cited fields (Coherence §4.7, Feasibility contribution §4.8, Investigation extension §4.2, Cross-service anchor §4.1) added in Step 6.5.

## STOP gate

This phase ends here. End your response.

- **Brookfield / Keystone / MoveOps (V3):** Wait for the user to invoke `PIPELINE S1 — Tasks/<TASK_DIR>` in a fresh chat.
- **StarPM (V4):** Wait for the user to invoke `PIPELINE INJECTION — Tasks/<TASK_DIR>` in a fresh chat. The INJECTION phase will read `## Injection Plan` from `Hardness_Plan.md`, author `9_Universe_inject.sql`, audit it via oracle council, then instruct the CB to inject on the platform before S1 begins.

If a STOP gate fired (`INSUFFICIENT_LEVERS` or `INSUFFICIENT_DENSITY`): also end your response with the stop reason clearly stated — the user has to decide whether to (a) edit the universe (V3: forbidden; StarPM: extend the Injection Plan to add more records/services), (b) swap the persona to a different one within the SAME business function (allowed in both CB and REVIEW flows), (c) swap the task, or (d) accept a lower hardness target before proceeding.

Do NOT proceed to prompt drafting in this chat.

## Bootstrap

Read root `AGENTS.md` first. The PIPELINE HARD RULES apply. The per-task universe is the only source of truth — base universe descriptions of "what scenarios exist" are stale.
