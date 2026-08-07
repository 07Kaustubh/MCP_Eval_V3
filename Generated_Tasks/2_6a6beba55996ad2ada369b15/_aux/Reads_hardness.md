# Reads — PIPELINE HARDNESS — `2_6a6beba55996ad2ada369b15`

v11 E2 compliance gate. One line per spec doc / Reference card / eval / registry file read in this phase, with what was confirmed from it.

## Pipeline governance

- `AGENTS.md` :: confirmed HarmonyGames routing — working dir is `Generated_Tasks/` not `Tasks/`; framework key is `hg` (single-model verification like V3-family PLUS V4's injection and submission_gate phases); model under test is **Claude Opus 4.7**, not 4.8, making this the one universe where hard rule 1 is universe-scoped.
- `AGENTS.md` (Harmony Games v22 section) :: confirmed the landmines that constrain lever selection — Gmail is read-only with no send/reply/compose/draft tool; Snowflake is query-only; two Slack send tools carry different text params (`text` vs `payload`); persona emails are irregular and must be resolved via the roster, never constructed; today 2026-02-28 is a Saturday, month-end and mid-Q1, so weekend-comms and "Q1 close" framings are temporal violations.
- `AGENTS.md` hard rule 2 :: confirmed the HarmonyGames payload inversion — `3_UniverseDataForThisTask.json` is a 940-byte contract descriptor, not data. Verified by reading it: it says "Do NOT extract or paste the full universe data". Source of truth is the base export resolved through the `base_export_plus_changelog` contract, which S0 has already materialised into `_aux/Universe_Split/`.
- `AGENTS.md` hard rule 32 :: confirmed persona ACL read-scoping is a PROMPT FEASIBILITY gate, not a difficulty lever — seven services scoped (gmail, slack, gcal, gdrive, gdocs, gsheets, gslides), six unscoped (contacts, github, snowflake, trello, linear, confluence). ACL does not govern writes and an ACL-denied write must never be load-bearing.
- `AGENTS.md` hard rule 33 :: confirmed the constant-memory requirement for any gate reading an export-backed universe. Applied by never loading `Universe_complete_data.json` (1.5 GB) and by reading only the per-service split shards.
- `AGENTS.md` hard rule 36 / Learnings L36 :: confirmed the governing failure mode for this phase — a well-trapped universe contributes zero difficulty if the prompt names the traps.
- `AGENTS.md` deviation HG-U11 :: confirmed `v4_gates.py` skips F9 UNRECONCILED_FUTURE_EVT for HarmonyGames, so the hard-rule-13 Calendar sweep is manual here. Moot for this task: the split contains no `gcal.*` files at all.

## Reference cards

- `Reference/Sessions/HARDNESS.md` :: the phase contract — two hard gates (INSUFFICIENT_LEVERS below 3 levers, plus a tiered density gate), the six required `Hardness_Plan.md` sections, the service-breadth table, and the mandatory Step 0 / Step 0.5 discipline files. Confirmed the density bands are explicitly framework-scoped and that the 50/40 V3-family scheme must not be applied to a non-V3 universe.
- `Reference/Hardness_Playbook.md` :: the 11-lever catalog with per-lever tool-call cost ranges (L1 latching 5-8 · L2 structured-DB skip 4-7 · L3 missing reply 3-5 · L4 search-cap eviction 3-5 · L5 thread-reply blindness 2-4 · L6 near-miss entity 3-5 · L7 multi-write diversification 9-12 · L8 multi-link chain 6-9 · L9 universe-grounded gotcha 3-5 · L10 reversal/supersession 4-6 · L11 net-vs-gross 4-7). Confirmed the composition rules: 4-5 levers is the design default, levers must be discoverable rather than buried, each must be grounded in this task's split, and 3+ writes across 3+ services is the minimum.
- `Reference/AGENTS.md` :: confirmed runbook routing and that every runbook resolves its universe from `_aux/Universe.txt` and reads constants from the `Validators/universes.py` registry.

## Cross-task learning logs

- `Tasks/_meta/Learnings.md` :: read end to end, all 338 lines. The load-bearing calibration for lever selection:
  - **L1-L7, the "does not reliably fail" block** — confirm-already-done tasks, single-hop reductions, near-miss entities alone, action-incompleteness alone, correction artifacts that state the answer, and binary "is it posted?" traps all pass at or near 100%. Picking any of these alone wastes the task budget.
  - **L6 (HARD)** — the correct answer must never appear verbatim in any searchable artifact. It must be derived.
  - **L8-L14, the "reliably fails" block** — stacked reductions across structurally different systems, authority-figure dismissal (the single most effective mechanism), structured-source invisibility, first-framing anchoring, and correct-observation/wrong-conclusion.
  - **L15/L16 (HARD)** — implicit prompts only; the persona must believe the wrong number and ask for execution, never hint at investigation.
  - **L25** — the existing-output anchor trap, the highest-yield novel stump observed: plant a prior artifact that superficially matches the requested write but lacks one or two rubric-tested fields.
  - **L29** — an escape-valve clause inviting the agent to surface contradictions neutralises the structured-source-skip lever on the surface it points at.
  - **L31** — a rubric demanding an explicit negative directive is a near-100% Gemini stump and trivial for Opus. Noted as NOT applicable here: HarmonyGames is single-model, so there is no cross-model asymmetry to exploit and no second model to carry the differentiator.
  - **L33 Rule 4 / L35** — criterion shape predicts grading stability: criteria grading a created artifact and its contents moved 0 of 120 cells across gradings, while criteria grading the agent's characterisation of a pre-existing record's claim absorbed most of the movement. Carry levers on created artifacts wherever the choice exists.
  - **L34** — widening an accept-set recovers real agent work and is cheap at authoring time; it fixes destination mismatches and does nothing for genuine misses, which is the separation wanted.
  - **L36** — difficulty is withheld inference, not universe trap density. Task 45 shipped a genuinely strong universe and came back Opus pass@1 = 100% because every rubric discriminator traced to an explicit prompt clause. This is the single most expensive recent lesson and it governs how each selected lever is recorded here.
- `Tasks/_meta/AGENTS.md` :: confirmed the append protocol for `Hardness_Patterns_Log.md` (predicted levers now, actual failures at S4) and `Stump_Hypotheses.md` (predictions now, calibration delta at S4).

## Per-task S0 artifacts

- `_aux/Universe.txt` :: `harmonygames`.
- `_aux/Universe_Index/today_horizon.json` :: universe today 2026-02-28, America/Chicago; last event timestamp seen 2026-02-22T02:03:50Z; zero records dated after today.
- `_aux/Universe_Index/graph_report.md` :: usable only for the Slack-id mention ranking (Robert = `usr_robert`, 969 mentions; `EMPLOYEE_0016_SLACK_ID` in the message corpus). Every other section — JE density by period, BlackLine exceptions and reconciliations, pending AP by vendor, Records Vault documents by kind and classification — is **empty**, because the generator is Brookfield-shaped and HarmonyGames has none of those services. Recorded as a known index limitation, not a data gap.
- `_aux/Universe_Index/key_facts.md`, `entities_personas.md`, `accounts_per_entity.md` :: all effectively empty for the same reason (zero unique emails extracted, no Oracle GL accounts). Lever evidence therefore comes from direct reads of `_aux/Universe_Split/`, not from the index.
- `_aux/Universe_Index/service_inventory.md` :: the one index file that is informative here — per-source record counts across confluence, contacts, gdocs, gdrive, gsheets, github, linear, slack, snowflake and trello.
- `_aux/Fact_Ledger.json` :: persona and alias surface. Confirmed `robert@harmonygames.co` -> name `Robert`, `is_user` true, `contact_id` `5f647df33ba6e92fbd56b05b`; confirmed the irregular-email landmine directly in the alias map (`arthur.blake@`, `julia.lawson@`, `martin.walsh@` all resolve by roster, not by construction) and confirmed genuine first-name collisions that matter for near-miss-entity work: **marcus** resolves to two people (`marcus.bennett@` and `marcus.lee@`), **claire** to two, **thomas** to two, **brian** to two, **victor** to two, **megan** to two, **baker** to two. Lifecycle and fiscal-period sections are empty, as expected for a non-GL universe.
- `3_UniverseDataForThisTask.json` :: the 940-byte contract descriptor. Read to confirm it is a descriptor and not data, per hard rule 2.
- `9_Universe_inject.sql` / `4_Changelog.json` :: inject file is the comment-only upstream template header with no executable statements; changelog is `[]`. Injection posture is therefore "none authored", `validate.py --phase injection` would SKIP, and levers must come from data already present unless injection is explicitly recommended.

## Eval / QC spec sub-dimensions relevant to this phase

- Trajectory `Tool Call Count` :: HarmonyGames carries three normatively separate thresholds rather than one — authoring target 40+ calls AND 3+ services, prompt-eval hard gate >15 NECESSARY calls AND 2+ services with multiple meaningful writes and information friction, and a trajectory QC floor of >=15 average. `set_acting_user`, ACL-denied reads and retries against inaccessible records count toward none of them.
- Trajectory `Agent Failure Rate` :: pass@1 must be <= 40%, i.e. 0-2 of 6 completed runs may pass.
- Trajectory `Error Rate` :: fails at 3+ of 6 runs not completing; an empty trajectory file is an errored run and is excluded from rubric-fail counts.
- Prompt `Tool use and Cross-service requirement` :: binary. Drives the 3+ services requirement that the service-breadth table in the plan evidences.
- Prompt `Feasibility with Tools` :: the gate that persona ACL read-scoping and the Gmail read-only landmine both feed. A lever requiring an unavailable action or an unreadable record is a task defect scored here, not a model miss.
