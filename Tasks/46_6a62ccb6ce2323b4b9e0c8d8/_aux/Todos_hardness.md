# Todos — PIPELINE HARDNESS (Task 46, StarPM V4)

Task: `Tasks/46_6a62ccb6ce2323b4b9e0c8d8`
Universe: `starpm` (V4) — density scheme is **40+ design target / 15 floor, PER MODEL** (Opus and Gemini separately). The V3-family 50/40 scheme does NOT apply.
Persona: Lisa Smith, Onsite Property Manager (`lisa.smith@starpm.com`, Slack `U6480117503`; the authoring id `p_002` does not appear in the split).
Business Function: 1 · Property Operations.
Flow: fresh CB build. No `_aux/REDO_reason.md`, no `_aux/Candidate_Originals/` — confirmed absent.

## Step 0 — gates and bootstrap

- [x] Run `phase_ready.py --phase hardness` — passed, 3 upstream artifacts present, `Verification_s0.md` valid
- [x] Create this todo file (v11 E1 operator-discipline gate)
- [x] Create `_aux/Reads_hardness.md` (v11 E2 compliance gate)
- [x] Read `AGENTS.md` hard rules; confirm the framework-scoped density bar for StarPM
- [x] Read `Reference/Sessions/HARDNESS.md` (phase contract)
- [x] Read `Reference/Hardness_Playbook.md` (11-lever catalog + costs + composition rules)
- [x] Confirm no REDO inputs exist

## Step 1 — empirical calibration (runbook mandates this FIRST)

- [x] Read `Tasks/_meta/Learnings.md` end to end (338 lines)
- [x] Read `Tasks/_meta/Hardness_Patterns_Log.md` (prior lever ledger)
- [x] Read `Tasks/_meta/Stump_Hypotheses.md` (prediction-vs-actual calibration)
- [x] Read `_aux/S0_Setup_Report.md` + all 6 `_aux/Universe_Index/` files
- [x] Read every prior StarPM task's `5_Prompt.txt` to establish spent scenario shapes
- [x] Read the StarPM tool catalog `7_Server_Tools_Details.json` — 268 tools across 8 servers
- [x] Derive empirical per-model density anchors from prior tasks via `parse_trajectories.py`
- [x] Read `_aux/Fact_Ledger.json` + `_aux/Feasible_Surface.json` for atom / action feasibility
- [x] Confirm the V4 density bar directly from `Validators/universes.py` FRAMEWORKS and `Docs_starpm/1`
- [x] Confirm V4 injection posture from `Evals_starpm/0_Injection_Quality` (injection is first-class for V4)

### Calibration conclusions carried into lever selection

- **Spent scenario shapes (do not re-use as the centre):** make-ready single-unit closeout (39, 40, 45 — two of the three failed), owner pass-through billing reconciliation (42, 43), Tanya Mitchell delinquency / eviction (40, 41), preventive-maintenance-push closeout (44).
- **Highest similarity risk:** Task 40 is the same persona AND the same business function (Lisa Smith / Property Operations).
- **Density is shape-driven.** Single-entity StarPM scenarios land 33-48 per model and straddle the 40 gate; the one multi-entity portfolio sweep (Task 44) landed 62.5 Opus / 79.8 Gemini. Margin requires a multi-entity enumeration structure.
- **Bank these levers** (confirmed across three gradings): the persona's own undispositioned field observation (6/6 Opus pass, 6/6 Gemini fail, 0 of 48 cells moved); duplicate records carrying the same title in different workflow states (0/12); Slack thread-reply blindness (near-total Gemini miss, roughly half on Opus); a same-cluster / same-noun entity pair differing only in *why* each is open.
- **Do NOT select** the L31 retraction / negative-directive beat when the prompt must name the verdict — falsified 12/12 across three gradings. Revised rule: it fires only when the negative is *implied by the situation*, never when the prompt names it as a required output.
- **Do NOT build a lever whose only carrier is the agent's characterisation of a pre-existing record's claim** — that is where all grader noise concentrates. Carry levers on created artifacts.
- **L36 is the governing constraint:** difficulty is withheld inference, not universe trap density. Task 45 shipped a strong universe and returned Opus pass@1 100% because the prompt named every discriminator.
- **Meta-lesson, logged twice:** score the *reasoning* step separately from the *retrieval* step. Prior plans scored levers by retrieval difficulty and the runs failed on reasoning difficulty.

## Step 2 — universe surface mapping (delegated, parallel)

- [x] Fire explore: fair-housing / reasonable-accommodation surface (`bg_a6c9e76b`)
- [x] Fire explore: Lisa Smith full cross-service footprint (`bg_887db82e`)
- [x] Fire explore: structured-store skip surfaces + post-today Calendar sweep (`bg_6cdb3e30`)
- [x] Fire explore: alternate signature scenarios + decoy / ambiguity landmines (`bg_73d59764`)
- [x] Collect all four results
- [x] Reconcile the findings against each other; resolve any disagreement by re-reading the split

## Step 3 — lever scan (delegated to deep-reasoning sub-agent)

- [x] Spawn the deep-reasoning sub-agent with: the 11-lever catalog + costs, the Learnings / patterns / hypotheses distillation, all 6 Universe_Index files, `Fact_Ledger.json`, grep access to `_aux/Universe_Split/`, the persona brief, the business function, the spent-shape list, and the empirical per-model density anchors
- [x] For each of the 11 levers: present / partial / absent, with evidence cited by file + row id
- [x] For each present lever: one paragraph on how the prompt engineers it into a natural ask
- [x] For each selected lever: cite the Learnings entry that justifies it

## Step 4 — select levers

- [x] Pick 4-5 (playbook default; 3 only with high-cost levers plus documented justification)
- [x] Maximise independence — no two levers that collapse into one measured stump
- [x] Verify no lever is displaced behind a discovery gate that already sweeps 0/12 (the lever-displacement rule)
- [x] Verify single-target uniqueness for every pinned record (hard rule 13 / F7 AMBIGUOUS_TARGET)
- [x] Sweep EVERY service including Calendar before any "only open item" framing (rule 13 / F9)

## Step 5 — density projection

- [x] Build the component table (base discovery, per-lever, write actions, cross-service buffer)
- [x] Project **per model separately** — Opus and Gemini
- [x] Band each: >= 40 PASS / 15-39 THIN / < 15 INSUFFICIENT
- [x] Populate the service-breadth table with the StarPM service list and apply the breadth gate

## Step 6 — stump hypothesis

- [x] 2-4 predictions, each with the specific failure, confidence, mechanism, and a Learnings citation
- [x] Label each prediction SYMMETRIC / OPUS-SELECTIVE / GEMINI-SELECTIVE
- [x] For each prediction, pre-register which lever fires and what the alternative attribution would be
- [x] Audit each intended discriminator against L36: could a prompt sentence satisfy it without discovery?

## Step 7 — write outputs

- [x] Write `_aux/Hardness_Plan.md` with all 6 required sections
- [x] Write `_aux/Verification_hardness.md` (v16 cross-source gate)
- [x] Run `Validators/check_verification.py` on the hardness verification doc
- [x] Append the predicted-lever entry to `Tasks/_meta/Hardness_Patterns_Log.md`
- [x] Append the prediction entry to `Tasks/_meta/Stump_Hypotheses.md`

## Step 8 — gates and exit

- [x] Levers gate: >= 3 selected, else `INSUFFICIENT_LEVERS`
- [x] Density gate per model: PASS / THIN_DENSITY (justify) / INSUFFICIENT_DENSITY (STOP)
- [x] Breadth gate: >= 4 distinct services each >= 5%
- [x] Print the explicit `PASS` / `THIN` / `STOP` verdict to chat
- [x] STOP. Do not draft the prompt in this chat. The next trigger is `PIPELINE S1`.
