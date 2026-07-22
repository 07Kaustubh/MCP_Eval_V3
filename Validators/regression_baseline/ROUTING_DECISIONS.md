# Doc / Eval Routing Decisions (per universe)

Durable record of which spec docs are the source of truth for each universe, so a
fresh-context phase agent never cross-loads another universe's constants. Referenced
by `Reference/Sessions/AUDIT.md`, `Reference/Sessions/FEEDBACK.md`, and
`Reference/Sessions/FINAL.md`. Every claim below is verified against the extracted
upstream drops (see `Validators/check_source_sync.py`).

## Routing table (keyed by `_aux/Universe.txt`)

| Consumer | Brookfield | KeyStone | MoveOps | StarPM (V4) |
|---|---|---|---|---|
| Evals | `Evals/` | `Evals_keystone/` | `Evals_moveops/` | `Evals_starpm/` (adds `0_Injection_Quality`, `5_Submission_Gate`) |
| QC spec docs | `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` | `Docs_keystone/7+8` | `Docs_moveops/` QC guidelines | `Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md` |
| Persona briefs | `Brookfield_Base_Universe/2_Persona_Briefs.md` | `Mortgage_Base_Universe/3_Persona_Briefs.md` | `MoveOps_Base_Universe/2_Persona_Briefs.md` | `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` (space in name) |
| Tool catalog | `Brookfield_Base_Universe/8_Server_Tools_Details.json` | `Mortgage_Base_Universe/6_...` | `MoveOps_Base_Universe/6_...` | `StarPM_Base_Universe/7_Server_Tools_Details.json` (prefix 7) |
| QC verdict corpus | `QC_Tasks/V3_Buckets/` | `QC_Tasks/V3.1_Buckets/` | `QC_Tasks/V2.1_Buckets/` | `QC_Tasks/V4_Tasks/` |
| Task template | `Tasks_Template/` | `Tasks_Template_keystone/` | `Tasks_Template_moveops/` | `Tasks_Template_starpm/` |

Rule: NEVER cross-load. A StarPM task reading Brookfield personas (or vice versa) is
the context-pollution failure DoD 2 forbids. The `universes.py` registry is the
single routing authority; runbooks read `_aux/Universe.txt` and substitute per the
table above.

## V4-specific decisions

- **The V4 rubric/OE/prompt framework is the same V3 framework** (Outcome/Process,
  three-condition test, agent-centric phrasing). What actually changes for StarPM:
  fixed date July 1 2026 (America/Chicago), dual-model verification (Opus 4.8 +
  Gemini), a property-management domain, and two extra eval phases (injection,
  submission gate). Do not treat V4 as a different rubric grammar.
- **Density is framework-scoped.** StarPM design target is 40+ average tool calls
  (Docs_starpm/1 hard gate), QC-spec fail floor 15, applied per model. Do NOT apply
  the Brookfield 50/40 scheme to StarPM or vice versa.
- **Injection is first-class in V4** and presence-gated for all universes: any task
  whose `9_Universe_inject.sql` carries executable statements runs
  `validate.py --phase injection`. V4 uses the fixed window 2026-05-01..2026-07-01;
  V3-family uses date ceiling = that universe's registry `today`.

## Contamination flags (do NOT treat as SSOT)

- **`Docs_starpm/13_QC_Companion.md` is Brookfield-contaminated** - its content is
  Brookfield accounting fixtures (Acme Cloud, Northstar, BlackLine, AICPA retention
  codes, `oracle_gl`), NOT StarPM universe facts. It is verdict-logic reference only;
  never cite it as a StarPM universe source.
- **Upstream `Docs/7_QC_Spec_Doc1.json` (Brookfield) still ships KeyStone-mislabeled
  prose** ("v3 = Keystone Mortgage", `Mortgage_Base_Universe/` paths). The repo keeps
  the flavor-corrected Brookfield copy; the divergence is pinned in
  `Validators/source_sync_deviations.json`. All scoring rules are upstream-verbatim.
- **The 16 (x3) + 80 labeled QC bucket tasks are content-flavored per their own
  universe** but are verdict-logic ground truth first; `qc_verdict.py` cross-references
  each task against its own universe SSOT, never a hardcoded universe.
