# Reads log — PIPELINE HARDNESS (Task 46, StarPM V4)

v11 E2 compliance gate. One line per doc read, with what was confirmed from it.

## Pipeline governance

- `AGENTS.md` :: Confirmed hard rule 11 is framework-scoped — this task is StarPM/V4, so the density bar is **40+ design target / 15 floor, applied PER MODEL (Opus and Gemini separately)**, NOT the V3-family 50/40 scheme. Confirmed rule 13 (single-target uniqueness, every-service sweep incl. Calendar, naive-agent simulation) and rule 4 (injection permitted for V4 but base rows never modified).
- `Reference/Sessions/HARDNESS.md` :: Phase contract. Two hard gates: INSUFFICIENT_LEVERS (<3) and the tiered density gate. Required outputs: `_aux/Hardness_Plan.md` with 6 sections, `_aux/Todos_hardness.md`, `_aux/Verification_hardness.md`. Confirmed no `_aux/REDO_reason.md` and no `_aux/Candidate_Originals/` exist for this task, so this is a fresh CB build, not a REDO rebuild.
- `Reference/Hardness_Playbook.md` :: The 11-lever catalog with per-lever tool-call costs. Confirmed composition rules: 4-5 levers is the design default; 3 only with high-cost levers plus documented justification. Confirmed the StarPM framework-scoped density note matches AGENTS.md rule 11.
- `Reference/AGENTS.md` :: Card-to-phase routing. Confirmed Hardness_Playbook is the correct card for this phase.
- `Tasks/AGENTS.md`, `Tasks/_meta/AGENTS.md` :: Per-task folder schema and the append protocol for the cross-task logs.

## Empirical calibration (mandatory first read per runbook Step 1)

- `Tasks/_meta/Learnings.md` :: Read end to end, all 338 lines. Entries load-bearing for this task:
  - **L1, L2, L4, L5, L6, L7** — the "does not reliably fail" block. Rules out confirm-already-done shapes, single-hop reductions, near-miss-entity-alone, action-incompleteness-alone, any correct answer stated verbatim in a searchable artifact, and any "it is not there" binary.
  - **L36 (most recent, same universe, Task 45)** — the decisive one. A well-trapped universe contributes **zero** difficulty if the prompt names the traps. Task 45 shipped a strong universe and came back Opus pass@1 = 100%, because every rubric discriminator traced to an explicit prompt clause. Mandates the audit: for each intended discriminator, find the prompt sentence that would satisfy it without discovering anything. Also records Task 45's Opus density at 37.0, below the 40 design target.
  - **Items 11 + 12 (Task 41)** — the banked StarPM dual-model recipe: one symmetric stump (structured-store skip) + two complementary asymmetric stumps (record-pick/latching = Opus-selective; negative-directive = Gemini-selective). Item 12 corrects item 11: L10's genuine role was the supersession READ, not a write stump.
  - **L31 (Task 39)** — explicit NEGATIVE directives are a near-100% Gemini stump and trivial for Opus. Reliable per-model differentiator; must not be relied on to stump Opus.
  - **Item 3 (Task 40)** — StarPM stores tenant arrears as a QuickBooks AP **bill**, not an AR invoice; 0/12 found it. Generalized rule: put the authoritative number in the object type the agent is least likely to query.
  - **Item 17 (Task 43)** — StarPM Gmail bodies are base64 and `get_thread` is the only path; 9/12 runs made the call and 0/12 decoded it. Email bodies are flavour, never the load-bearing discriminator.
  - **Item 9 (Task 41) + item 20 (Task 43)** — the lever-displacement pairing rule, confirmed from both directions. A net-vs-gross lever stacked behind a discovery gate that sweeps 0/12 is never observed; open the gate and it becomes independently measurable.
  - **Items 13, 14, 15, 16 (Task 39 postmortem)** — F7 AMBIGUOUS_TARGET / F8 NON_ATOMIC_ENUM / F9 UNRECONCILED_FUTURE_EVT are now deterministic submission-gate defects. A confirmed future calendar event on the task entity is open work, and Calendar is the service every council skipped.
  - **L33, L35** — grader non-determinism sits at a ~8.5% noise floor per cell and reverses direction between regrades. Design for **margin**, not for a number.
  - **L32** — 60 is the hard rubric-count ceiling; budget against it at S3, which constrains how many content elements this phase may hand downstream.
- `Tasks/_meta/Hardness_Patterns_Log.md`, `Tasks/_meta/Stump_Hypotheses.md` :: pending read before the plan is finalized (prior-task lever ledger + prediction-vs-actual calibration).

## Task-local inputs

- `_aux/S0_Setup_Report.md` :: Read in full. Seven carried-forward notes. Load-bearing: (1) `p_002` does not appear in the split — ground only on `lisa.smith@starpm.com` / "Lisa Smith" / Slack `U6480117503`; (2) Lisa is 11th by ambient density (73 mentions) despite a "deeply rooted" brief, so levers must anchor on her signature scenarios rather than an assumed dense ambient surface; (4) registry landmines to check — near-duplicate decoy files, the Tanya Mitchell accommodation-vs-eviction contradiction, cross-property "Unit 14"; (5) **the Fact Ledger has no Calendar, Gmail or QuickBooks id atoms**, so Calendar and Gmail citations must be grounded directly against the split files, not the ledger — this directly interacts with rule 13's Calendar sweep; (6) `Feasible_Surface.json` omits `airtable.airtable_records` because the builder never descends into `fields`, so make-ready enum values must be checked against `key_facts.md` and the split.
- `_aux/Universe.txt` :: `starpm`. Fixes the framework to V4 and the density scheme to 40/15 per model.
- `_aux/Universe_Index/today_horizon.json` :: universe_today **2026-07-01**, tz America/Chicago, **59 records dated after today**, furthest 2026-12-30. The 59 post-today records are the F9 surface.
- `_aux/Universe_Index/service_inventory.md` :: 33 sources, 3,892 records, all 8 StarPM services present.
- `_aux/Universe_Index/key_facts.md` :: Make-ready turn status enum selProg=56 / selSched=43 / selReady=21. QuickBooks 155 invoice / 117 credit_memo / 113 bill / 54 payment. Linear by state. Slack by channel (C004=144 densest).
- `_aux/Universe_Index/graph_report.md` :: Person-by-artifact-density ranking. Lisa 73 mentions, 11th; Tony Reyes 862 leads. Confirms S0 note 2.
- `_aux/Universe_Index/entities_personas.md` :: 61 unique emails, persona-vs-npc split. Confirms Lisa is one of four Onsite Property Managers (with Carlos Mendez, Denise Morales, Patricia Nguyen) — relevant because three prior tasks used Onsite PMs.
- `_aux/Universe_Index/accounts_per_entity.md` :: No Oracle GL accounts. Confirms the Brookfield account-number trap does not apply here.
- `PersonaBrief.txt` :: Lisa's signature scenarios and their action counts. `fair_housing_reasonable_accommodation` is the one she **leads**, at 6 actions — her deepest single surface.
- `1_Business_Function.txt` / `2_Persona.txt` :: Property Operations / Lisa Smith, Onsite Property Manager. Matches the brief's home function, so no cross-function mismatch to resolve.
- `9_Universe_inject.sql` :: comment-only scaffold header, 0 executable statements. `4_Changelog.json` is `[]`. Injection gate SKIPs; the recorded PASS is vacuous.

## Cross-task similarity inputs (read to avoid re-treading a used shape)

Read `5_Prompt.txt` for every prior StarPM task to establish which scenario shapes are spent:

- `Tasks/39_.../5_Prompt.txt` :: Las Palmas 8D make-ready closeout (James Bennett, Maintenance & Repairs). Shipped a QC fail.
- `Tasks/40_.../5_Prompt.txt` :: **Same persona and business function as this task** — Lisa Smith / Property Operations. Tanya Mitchell Unit 14 make-ready + account status + Brooke email + calendar reminder + ticket update. Highest similarity risk of any prior task.
- `Tasks/41_.../5_Prompt.txt` :: Tanya Mitchell delinquency filing package (Patricia Nguyen, Property Operations).
- `Tasks/42_.../5_Prompt.txt` :: Ridgeview roof owner pass-through + vendor payment (Brooke Phillips).
- `Tasks/43_.../5_Prompt.txt` :: Mesa Vista 4C owner pass-through reconciliation (Carlos Mendez, Property Operations).
- `Tasks/44_.../5_Prompt.txt` :: Preventive Maintenance Push closeout (Jaime Salinas, QC).
- `Tasks/45_.../5_Prompt.txt` :: empty — task was reset to REDO after the L36 failure.

**Conclusion carried into lever selection:** make-ready-turn-closeout is spent (3 uses, 2 failures), owner-pass-through is spent (2 uses), Tanya-Mitchell-delinquency is spent (2 uses). `fair_housing_reasonable_accommodation` — the scenario Lisa leads — is untouched by every prior task.

## Eval / QC spec sub-dimensions relevant to this phase

- Trajectory / **Tool Call Count** — binary QC sub-dim, no 3/4 band. QC-spec fail floor 15; StarPM design target 40+ average, applied per model. This phase's density projection is the forecast against that gate.
- Trajectory / **Agent Failure Rate** — binary. pass@1 must land at or below 40%. The stump hypothesis is the forecast against this gate.
- Universe / **Universe Feasibility** and **Cross-service Coherence** — binary. Every selected lever must be backed by records that actually exist in the split, which is why each lever carries a citation.
- Prompt / **Investigation** — binary. L36 is the empirical statement of this sub-dim: a prompt that names its own traps scores zero investigation load.
