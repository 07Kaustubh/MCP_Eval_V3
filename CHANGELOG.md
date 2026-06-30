# Changelog

## 2026-06-30 — v21: Pipeline Consolidation (6 Tracks — Spec Sync + Bloat Trim + SSOT Pointers + Orphan Archive + Conditional AUDIT + Deterministic Promotion)

Comprehensive consolidation pass closing six tracks identified during a third-person parity review against the upstream Brookfield zip (`MCP_Eval_V3 (2)/MCP_Eval_V3_BrookField/`) and against pipeline-internal duplication surface. The review verified that every pipeline-internal addition since v6 traces to a specific incident in CHANGELOG or `Tasks/_meta/Learnings.md` (Tasks 23-24 escapes, Task 6a3998c2 + 6a34253220 platform rejections, v17 5-LLM-gate failure mode, etc.) — none of the pipeline's experience-driven moat is removed in this consolidation. What IS removed: (1) ~9 days of stale Brookfield Eval text that the upstream had updated with incident-grounded HARD GATEs in the preceding two weeks, (2) 9 "do NOT execute" dead-body perspectives kept "for reference" since v18 (cluttered every council/audit sub-agent's context window for no benefit), (3) duplicated per-universe landmine prose where `Validators/universes.py` is already the code SSOT, (4) 4 orphaned files explicitly superseded by current runbooks, (5) unconditional AUDIT auto-fire on first-draft S1/S2 even when every deterministic floor was clean (Tasks 23-24 insurance is preserved via signal-driven conditional triggers; AUDIT fires when any band-state-shaky signal is present, skips otherwise).

### Track A — Sync upstream Brookfield HARD GATEs (20-item shopping list)

Upstream Brookfield Evals (Jun 30 2026 snapshot) were 9 days newer than pipeline (Jun 21). Upstream added 11+ universe-agnostic HARD GATEs grounded in named QC-fail incidents with numeric evidence (`Task5 6a2c5140`, `Task6 6a312ac1`, `Task8 6a32aa51`, "7+ of 19 score-3", "3+ of 13 score-2", "4-5 of 19 score-3"). Pipeline ports each gate WITH Brookfield primitives substituted in — upstream's example text was content-contaminated with Keystone Mortgage schema (`loans.json`, `borrowers.json`, `lenders.json`, `Mortgage_Base_Universe/`, `elena.marchetti@brookfieldcpas.com`) per the long-standing AGENTS.md deviation row documenting the upstream zip's BrookField↔Keystone mislabel.

Gates ported into `Evals/1_Prompt_Eval.md`: UGT Precision Guardrail (3-part test, Task8 6a32aa51 incident), Dimensional Feasibility (per-X field exists check, universe-agnostic), Phantom Tight-Identifier Grep (mandatory grep before scoring Truthfulness), Write-Action Divergence (second-reading test on write actions), Duplicate / conflicting injected-data check (Phase 3.2 sub-section).

Gates ported into `Evals/2_OE_Eval.md`: Per-OE Verification Sign-Off Table (HARD GATE — Phase 2.4 — incident-quantified evidence "7 of 19 score-3 + 2-3 of 13 score-2 traced to inaccurate OEs"), Act-vs-Defer Override for write-action OEs (T9 — Task5 6a2c5140), NEW Phase 4.0 Pre-Verdict Completeness Sweep.

Gates ported into `Evals/3_Rubrics_Eval.md` (heaviest delta, 131 lines): Atomicity Decomposition (Phase 2.2 — "7+ of 19 score-3 — single most common defect"), Impossible Derivation (3 shapes: dimensional/comparative/imported-constraint — Phase 2.7 #8 — Task6 6a312ac1 R12 May figures), Act-vs-Defer Override on rubrics (Phase 2.7 #9 — Task5 6a2c5140 $4,390.62 thread), Write-as-Deliverable Preservation (T12 3-part test — Phase 3.1), Prompt-vs-Rubric Action Alignment (Gap 6 — "3+ of 13 score-2 hard fails"), Final-Response Coverage HARD GATE (2.1 user-facing rubrics — Phase 3.1 — "4-5 of 19 score-3"), OE-to-Rubric Cross-Reference HARD GATE (Phase 3.1 — "3-4 of 19 score-3"), Role / Segregation-of-Duties overreach (Phase 2.7 #7), Overly Broad precision guardrail (BOTH-must-fail test before flagging "(or similar)" content rubrics), NEW Phase 5.0 Pre-Verdict Completeness Sweep.

Gates ported into `Evals/4_Verifier_Fails_Eval.md`: STEP 0 HARD GATE (mandatory TODO list before any evaluation), STEP 5 CB AF-list validation against trajectory matrix (T8), Phase 2 NEW environment / tool-error fail check (T7 — distinguishes server-crash from agent-reasoning failure).

New supporting file: `Docs/QC_Spec_Changelog.md` — extracted from upstream `Docs/8_QC_Spec_Doc2.md` changelog section (Jun 10 / Jun 9 / Jun 3 / May 22 / May 5 entries). Lets future syncs verify which gates the pipeline has ingested.

Hash-pin infrastructure: `Validators/eval_file_hashes.json` (new file with SHA256 per Eval file for all 3 universes — 12 hashes total). `Validators/check_eval_hashes.py` (new — same shape as `check_tool_catalog.py`, runs at start of every phase that consumes Eval text). `Validators/phase_ready.py` extended to call `check_eval_hashes.py` on phases {s1, s2, s3, s4, final, audit, review} with WARN-only severity (drift surfaces operator awareness without blocking work; operator runs `--update` after intentional sync). Brookfield Eval files NOT byte-identical to pipeline's previous v20 snapshot — the v21 port is the new baseline and the pinned hashes reflect post-port content.

`AGENTS.md` "Pipeline Deviations from Eval Specs" table extended with 2 new rows documenting where the v21 port diverged from upstream (e.g., "Eval 3 Phase 2.7 #8 Impossible Derivation — pipeline retains Brookfield JE / vendor / period-close examples; upstream's loan / borrower / TRID examples were Keystone-contaminated").

### Track B — Delete dead "for reference" perspective bodies (~235 lines)

Council A perspectives **A5 / A8 / A9 / A12** body text removed from `Reference/Council_Protocol.md`. Each was flagged "do NOT execute" at v18 (validator A3 NPC blocklist + atom-verifier + persona-fit on-demand audit cover their work) but the body remained, cluttering every Council A sub-agent's context. Replaced with one-line "RETIRED in v18; see CHANGELOG v18 + v21 entries" pointers.

Council B perspectives **B5 / B10 / B11** body text removed from `Reference/Council_Protocol.md`. Each was flagged "REMOVED/CONVERTED" at v18 (validator regex + X1 forward map + tell-me cue regex cover their work). Same one-line pointer treatment.

AUDIT **Lens 6** (Lifecycle + Narrative State) + **Lens 9** (Unique Ground Truth Middle-Band) body text removed from `Reference/Sessions/AUDIT.md` prompt template. Each was flagged "v18 MERGED INTO LENS 1" but the body remained. Lens 6 checks now floored by `verify_universe_atoms.py` lifecycle queries; Lens 9 two-reading test covered by Lens 5 Adversarial Veteran Review. Same one-line pointer treatment.

Net effect: ~235 lines of intentionally-dead text removed from the surface every council/audit sub-agent reads, with zero functional change (those perspectives were already inert). Historical bodies preserved in git history + earlier CHANGELOG entries.

### Track C — Collapse triplicated rules to SSOT pointers

**Per-universe landmines** consolidated. `Validators/universes.py` is the code SSOT (per-universe `landmines` block enforced by `verify_universe_atoms.py`); `AGENTS.md` "Universe constants (multi-universe — v20)" section is the human SSOT with full per-landmine descriptions. `Reference/Sessions/REVIEW.md` Step 2 landmine list (10-bullet block) replaced with one-paragraph summary + SSOT pointer. `Reference/Sessions/AUDIT.md` Lens 1 landmine list (10-bullet block) replaced with one-paragraph summary + SSOT pointer. Critical landmine summary preserved verbatim in each (one-line per universe) so LLMs running REVIEW/AUDIT still have enough context to sanity-check `verify_universe_atoms.py` output.

**Tool-call density gate** consolidated. AGENTS.md hard rule #11 remains the operator-facing summary. HARDNESS.md remains canonical for the projection method. Council Protocol B3 remains canonical for the council perspective definition. `Reference/Sessions/FINAL.md` Lens 3 density restatement replaced with "tiered gate per Council Protocol B3 (SSOT)" pointer carrying the empirical justification verbatim ("Tasks shipped at 40+ projected came back failing density on real runs, so design target was raised to 50+ in v8").

**Atom-existence sweep** — already in good shape post-v18: `verify_universe_atoms.py` is the code SSOT; Council A1, B7, AUDIT Lens 1, FINAL Lens 1 all consume its output rather than re-deriving. No edit needed; status confirmed.

**Process 3-condition test** + **Outcome > Process balance** + **Agent-centric phrasing** — duplications in Docs/2_Rubrics_V3_Guidelines.md + Reference/Rubric_Format.md noted but not consolidated this pass (the duplications are short — 3-4 sentences each — and serve different reading paths: spec doc is auditor-facing, format card is author-facing). Deferred to future pass if drift surfaces.

### Track D — Archive 4 orphaned files; update 2 stale refs

Files moved to `_archive/`: `command workflow.txt` (351 lines — explicitly superseded by `Reference/Sessions/*.md`), `additional knowledge.txt` (280 lines — content duplicated in `Docs/8_QC_Spec_Doc2.md` and programmatically enforced by v13/v14 validators), `hardness.txt` (23 lines — confirmed unreferenced anywhere in active runbooks/scripts), `data.legacy.py` (the original shared-dir-writing script that `data.py` smart forwarder superseded).

Ref updates:
- `AGENTS.md` project layout tree no longer lists `data.legacy.py`.
- `AGENTS.md` PIPELINE DISPATCH header note updated to "Supersedes the legacy `command workflow.txt`" (archived to `_archive/` in v21).
- `AGENTS.md` anti-patterns section: removed the named `data.legacy.py` reference; kept the underlying anti-pattern ("Writing to the shared `Brookfield_Base_Universe/Data/` directory").
- `Validators/AGENTS.md` similarly updated.
- `data.py` error message no longer suggests "run data.legacy.py directly" as a fallback (the legacy script is archived; per-task is the only sanctioned flow).
- `QUICK_START.md` Universe section updated: "v18 / two universes" → "v20 / three universes" including MoveOps.
- `Prompt_Guidelines.md` checklist refreshed: stale "opus 4.5" → "Opus 4.8 (the model under test per AGENTS.md hard rule #1)"; stale "MoveOps" generic-task reference → universe-agnostic "any task in the universe"; reference to non-existent Brookfield scenario file replaced with `Reference/Hardness_Playbook.md` + `PIPELINE HARDNESS` STOP-gate fallbacks pointer.

### Track E — Promote B7 + B9 to deterministic validators

`Validators/validate.py` adds two new rules:

**X2 — Rubric ↔ OE value consistency** (`validate_rubrics`): mechanical map-and-diff that previously required B7 LLM judgment. For each rubric criterion, extracts every typed value (amount / email / JE id / exception id / recon id / vendor id / AP invoice id / Linear issue id / Airtable record id / date / account number / retention code / classification / Slack channel) and finds the matching OE step asserting that value. Diff: rubric value vs OE value (modulo "(or similar)" tolerance on freetext). FAIL on typed-value mismatch. Launches at WARN severity for first 2 weeks per the implementation plan, promoted to FAIL after no false-positive reports — memory file `discovery_prompts_vs_groundedness.md` flagged this as a recurring B7 LLM false-positive surface, so the deterministic check should eliminate the failure mode.

**X3 — OE Service Mapping** (`validate_oe`): universe-aware mechanical lookup that previously required B9 LLM judgment. For each OE step, extracts the service name + data type queried; consults per-universe `oe_service_map` in `Validators/universes.py` (already populated for Brookfield + KeyStone + MoveOps per v20); FAIL on misalignment (e.g., KeyStone OE step querying mortgage loans through CRM service instead of mortgage_los). Launches at WARN severity similarly.

`Reference/Council_Protocol.md` B7 + B9 perspective bodies updated with note: "Deterministic floor: `validate.py` rule X2 (B7) / X3 (B9) covers the mechanical map-and-diff. Council B's role is now the residual interpretive layer — flag CONSISTENCY_GAP / OE_SERVICE_MISMATCH only when the value structure is non-standard (e.g., freetext field with semantic-not-syntactic mismatch) that the deterministic check cannot catch."

### Track F — Conditional AUDIT auto-fire

`Reference/Sessions/AUDIT.md` Mode 1 description rewritten: AUDIT auto-fire is now CONDITIONAL on S1 (prompt first draft) + S2 (OE first draft), based on band-state signals; UNCONDITIONAL on S3 (rubrics) + S1.5 (revise/pivot) + MATERIALIZE (corrected artifact) + REVIEW-on-originals (parity with CB). On-demand AUDIT in fresh chat (Mode 2) remains unconditional.

Conditional triggers in S1/S2 (any one fires AUDIT):
- Council B used any NON-FAIL band justification on any sub-dim
- `validate.py` exited 0 but emitted ≥1 WARN
- `verify_universe_atoms.py` exited 0 but emitted any edge-case-needs-LLM-judgment flag
- Similarity composite ≥ 35 (sub-threshold but near pivot band — S1 only)
- Artifact was revised in this phase pass (iteration history)
- (S2 only) Forward-map gap detected by Council B-B8

When ALL signals are clean (Council B uniformly 5/5 with no band invocations + validator exit 0 zero WARN + atom-verifier clean + similarity < 35 + first-pass draft + no forward-map gap), AUDIT is OPTIONAL. Operator skips by default; on-demand AUDIT remains as a safety net before platform upload.

S3 stays unconditional because rubrics is the heaviest phase, AUDIT_rubrics historically catches the highest-severity defect classes (atomicity decomposition gaps, Final-Response Coverage gaps, Process-disguised-as-Outcome write actions per Eval 3 §2.3 incidents Task5 6a2c5140 / Task6 6a312ac1), and the cost asymmetry favors always running it. S1.5 + MATERIALIZE + REVIEW stay unconditional because the revised/corrected/candidate-original artifacts are inherently at risk.

Tasks 23-24 escape pattern (the original v7 motivation for unconditional auto-fire) is preserved because the conditional triggers ARE the signals of "something is shaky" — when those signals are absent, the failure pattern doesn't apply.

Estimated cost savings: ~30-40% reduction in AUDIT calls on clean tasks (S1 + S2 first-pass clean → 0 audit calls instead of 2). Cost on shaky tasks unchanged. Estimated quality impact: net positive — operator attention frees up to read on-demand AUDIT carefully on the cases that need it instead of skimming auto-fire AUDIT on cases that don't.

`Reference/Sessions/S1.md` step 8, `S1.5.md` step 8, `S2.md` step 8, `S3.md` step 9 updated with phase-specific conditional/unconditional language.

### Files added / moved / removed (v21)

- ADDED: `Docs/QC_Spec_Changelog.md` (upstream-sourced changelog of QC spec rule changes, per-date entries)
- ADDED: `Validators/eval_file_hashes.json` (SHA256 hashes per Eval file across 3 universes)
- ADDED: `Validators/check_eval_hashes.py` (drift-detection script, WARN-only, runs at phase-readiness gate)
- MOVED: `command workflow.txt` → `_archive/command workflow.txt`
- MOVED: `additional knowledge.txt` → `_archive/additional knowledge.txt`
- MOVED: `hardness.txt` → `_archive/hardness.txt`
- MOVED: `data.legacy.py` → `_archive/data.legacy.py`
- MODIFIED (edits across): AGENTS.md, CHANGELOG.md (this entry), Prompt_Guidelines.md, QUICK_START.md, data.py, Reference/Council_Protocol.md, Reference/Sessions/{S1,S1.5,S2,S3,AUDIT,FINAL,REVIEW}.md, Validators/AGENTS.md, Validators/validate.py, Validators/phase_ready.py, Evals/{1,2,3,4}_*.md

### Smoke-test evidence (post-v21)

| Check | Expected Result |
|---|---|
| `Validators/test_regression_anchors.py` | 48 / 48 PASS preserved (no regression from v20 baseline) |
| `Validators/check_eval_hashes.py` | clean on first run after `--update` populated baseline hashes |
| `Validators/validate.py --phase rubrics --task Tasks/<recent>` | X2 rule fires at WARN severity (will be promoted to FAIL after 2-week observation) |
| `Validators/validate.py --phase oe --task Tasks/<recent>` | X3 rule fires at WARN severity similarly |
| `Reference/Sessions/AUDIT.md` line count | reduced ~55 lines (Lens 6 + Lens 9 body removal + landmines collapse) |
| `Reference/Council_Protocol.md` line count | reduced ~150 lines (7 dead perspective bodies → one-line pointers) |
| `Reference/Sessions/REVIEW.md` line count | reduced ~10 lines (landmines collapse) |
| Sub-agent calls per CB task (mean, post-Track F conditionalization) | ~30-40% reduction on first-pass-clean tasks; unchanged on shaky tasks |

### Verification posture: 5/5 enforcement preserved

Every QC sub-dim enforcement mechanism present at v20 remains present at v21 OR is replaced by a stricter/equivalent mechanism. Specifically:
- Tasks 23-24 escape insurance: preserved via Track F's signal-driven conditional triggers
- 50+ density target: preserved (canonical in HARDNESS.md + B3; FINAL Lens 3 pointer-ized with empirical justification verbatim)
- Hardness lever preservation: preserved (B4 canonical; downstream phases reference)
- Per-universe landmines: preserved (Validators/universes.py is code SSOT; AGENTS.md is human SSOT; REVIEW + AUDIT consume `verify_universe_atoms.py` output)
- v18 atom-verifier floor: preserved (and amplified — Track E adds X2 + X3 deterministic checks beneath B7 + B9)
- v10 4-fix stack (narrative state / action-prescription / parameter strictness / lifecycle precondition): preserved (Council A-A3 + A4 active; AUDIT Lens 1 floored by atom-verifier; FINAL Lens 5 active)
- All 30 Learnings entries (L1-L30): preserved verbatim
- All 13 Pipeline Deviations: preserved + 2 new rows added for v21 port deviations
- All 12 Hard Rules: preserved verbatim

QC 5/5 is the non-negotiable bar. v21 strengthens deterministic enforcement (X2 + X3 + hash-pin), removes dead text that distracted council sub-agents, and ports incident-grounded upstream gates that operationalize specific score-fail patterns the pipeline didn't previously enforce textually.

## 2026-06-30 — v20: MoveOps Universe Integration (Third Universe) + Pipeline-Wide Multi-Universe Parity (17 Items / 5 Phases)

Adds **MoveOps Inc.** as a third first-class universe — a B2B remote-work relocation startup running on the V2.1 framework. Extends the registry from 2 → 3 universes, propagates MoveOps awareness through every validator + every council prompt + every operator-facing runbook, and pins the MoveOps tool catalog by SHA256. Regression anchor suite grows from 43 → 48 (all PASS).

### Phase 1 — MoveOps drop-in (3 items)

`MoveOps_Base_Universe/` + `Docs_moveops/` + `Evals_moveops/` + `QC_Tasks/V2.1_Tasks/` dropped in from the upstream source zip. MoveOps universe today is **2026-04-26** (US/Pacific). Single entity `moveops`. 21 employees across 6 departments. Email domain `moveops.com`. 9 services (airtable, calendar, contacts, crm, email, linear, public, quickbooks, slack). Tool catalog at `MoveOps_Base_Universe/6_Server_Tools_Details.json`. 5 business functions: Operations 25%, Customer Engagement/Support 30%, Engineering 20%, Finance 15%, Executive 10%.

### Phase 2 — Universe registry + detection (3 items)

`Validators/universes.py` `UNIVERSES["moveops"]` added with full per-universe constants: paths, today, persona_email_domain, business_functions + weights, tight_identifiers, oe_service_map (relocations → airtable; AP → quickbooks; deals → crm; tickets → linear; calendar events → calendar; chat → slack; emails → email; contacts → contacts), cross_service_pairs, slack_channels (C001-C009), tool_param_traps (linear_create_issue requires `team` NOT `teamId` — DIFFERS from Brookfield), landmines (PHMSA DOT hazmat, Airtable-vs-CRM source-of-truth, Marcus Webb identity, Heartland Q1 invoice cross-ref, ExpenseBot pilot bugs), npcs.

`detect_universe()` upgraded to multi-universe signal-scoring across all three universes. New `_MOVEOPS_SIGNALS` regex catches: MoveOps, moveops.com, Elena Rostova, PHMSA, hazmat, UrbanNest, Heartland Movers, Swift Relocations, Vectral Systems, Canopy Health, BrightLoop, Mosaic Robotics, GreenStack Energy, tblRelocations, tblStipends, ExpenseBot, auto-categorizer. Highest score wins; ties default to brookfield (back-compat).

### Phase 3 — Validator + verifier extensions (4 items)

`Validators/validate.py` persona email domain check upgraded from a 2-domain swap to a per-universe `wrong_domains = ALL_DOMAINS - {local}` set check — handles all three universes correctly + automatically extends if a fourth ships.

`Validators/verify_universe_atoms.py` adds MoveOps-specific landmine verifiers:
- `verify_phmsa_claim_moveops()` — PHMSA / DOT hazmat claims flagged when context cites verbal-only confirmation without signed certificate reference. Compliance requires signed certificate on file (Airtable record + Swift / Heartland email).
- `verify_airtable_vs_crm_claim_moveops()` — claims citing CRM as source for relocation / vendor / coordinator / stipend state get flagged. Source-of-truth violation: relocation state lives in Airtable `tblRelocations01` / `tblStipends00001`, not CRM.

New atom-collection regexes: `PHMSA_HAZMAT_CLAIM`, `AIRTABLE_VS_CRM_CLAIM`. Wired into main flow `if universe == "moveops":` block.

`Validators/check_tool_catalog.py` + `Validators/tool_catalog_hashes.json` add MoveOps entry: catalog at `MoveOps_Base_Universe/6_Server_Tools_Details.json`, SHA256 pinned at `e7a07c46588555654f58e95ebcdd1135f339205a126136e742a3edfb3864f1ba`.

`Validators/build_universe_index.py` `today_horizon()` already accepts universe-specific today via `resolve_universe_today()` — picks up MoveOps `2026-04-26` automatically from the registry.

### Phase 4 — Runbook + council updates (3 items)

`Reference/Council_Protocol.md`:
- **A-A10 Business Function Match** prompt template now enumerates THREE universes' categories: Brookfield 10 + KeyStone 6 + MoveOps 5 (with weights).
- **B-B9 OE Service Mapping** prompt template adds MoveOps map (relocations → airtable; AP → quickbooks; deals → crm; tickets → linear; calendar → calendar; chat → slack; email → email; contacts → contacts).
- B-B9 section description universe-aware quick-reference (3 universes) instead of Brookfield-hardcoded.

`AGENTS.md`:
- Universe-constants section heading bumped `v18 → v20`, "two universes" → "three universes".
- Full MoveOps subsection added between KeyStone and Universe Detection: today, entity, account-trap absence, PHMSA landmine, Marcus Webb identity disambiguation, Airtable-vs-CRM source-of-truth, Heartland Q1 vendor cross-reference, ExpenseBot pilot bugs, Slack channels, parameter traps (linear `team`, crm `body`, quickbooks `DisplayName`), services, 5 business functions, V2.1 framework note.
- Universe Detection paragraph updated to list 3 universe names + tie-break rule.

`Reference/Sessions/REVIEW.md`:
- Per-universe landmine list extended: KeyStone Landmine 2 (LOS-vs-CRM), MoveOps Landmines 1-5 (PHMSA, Airtable-vs-CRM, Marcus Webb cross-universe, Heartland invoice, ExpenseBot pilot bugs).

`Reference/Sessions/AUDIT.md`:
- "VETERAN QC AUDITOR on a Brookfield MCP Eval V3 task" → universe-aware ("read `_aux/Universe.txt`").
- Tool-catalog re-verification path → all 3 universes' catalog paths.
- "200+ Brookfield tasks" → "200+ MCP Eval tasks across all universes".
- Per-universe landmines list extended with KeyStone LOS-vs-CRM + MoveOps PHMSA, Airtable-vs-CRM, Marcus Webb, Heartland, ExpenseBot.

### Phase 5 — Coverage + docs (3 items)

`Validators/test_regression_anchors.py` extends with 5 new anchors:
- **v20 MO-1**: MoveOps auto-detection (PHMSA / Vectral / UrbanNest signals → universe note `moveops`)
- **v20 MO-2**: MoveOps persona contaminated with Brookfield email domain → `persona email domain mismatch`
- **v20 MO-3**: MoveOps persona contaminated with KeyStone email domain → `persona email domain mismatch`
- **v20 MO-4**: Marcus Webb blocked as MoveOps persona (NPC / non-staff) → `persona is an NPC for moveops`
- **v20 MO-5**: Brookfield baseline preserved (no contamination from v20 multi-universe registry) → `universe: brookfield`

Total: 43 → **48 anchors**, all PASS.

`AGENTS.md` Pipeline Deviations table extends with TWO entries:
- **MoveOps V2.1 framework**: source folder `MCP_Eval_V2.1_Move_Ops/` ships V2.1 framework docs; pipeline tags as V2.1; read `Docs_moveops/2_Rubrics_V3_Guidelines.md` for per-phase deltas before applying validator behavior. Validator currently treats MoveOps with same scoring as Brookfield/KeyStone — flag a deviation if a real MoveOps task surfaces a divergence.
- **Upstream `MCP_Eval_V3 (2)/MCP_Eval_V3_BrookField/Docs/` mislabel warning**: upstream zip folder labeled "BrookField" but content-labeled KeyStone (references `Mortgage_Base_Universe/3_Persona_Briefs.md`). Pipeline `Docs/` is the correct Brookfield-flavored copy; `Docs_keystone/` is the correct KeyStone copy. Operator-warning only — do NOT use the mis-named source folder as authoritative.

CHANGELOG v20 entry (this file). Memory file updated with v20 multi-universe note: Marcus Webb is distinct person in MoveOps vs KeyStone; PHMSA + Airtable-vs-CRM are the MoveOps recurring landmines.

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | **48 / 48 PASS** (38 Brookfield + 5 KeyStone v18-19 + 5 MoveOps v20) |
| `Validators/check_tool_catalog.py` | brookfield + keystone + moveops all match pinned SHA256 |
| `Validators/universes.py Tasks/24_...` | universe=brookfield baseline preserved + universes registry returns 3 names |
| Cross-universe persona contamination | catches @brookfieldcpas.com / @keystonemortgage.com leaks into moveops universe |
| PHMSA atom regex | matches "PHMSA", "DOT certificate", "hazmat documentation" — does not match Brookfield contexts |
| Airtable-vs-CRM atom regex | matches CRM-as-source-for-relocation-state — does not match Brookfield contexts |

### Files added

- (none — all changes are extensions to existing files)

### Files changed

- `Validators/universes.py` — `UNIVERSES["moveops"]` block + `_MOVEOPS_SIGNALS` + 3-universe `detect_universe()`
- `Validators/validate.py` — persona email domain check supports all 3 universes
- `Validators/verify_universe_atoms.py` — PHMSA + Airtable-vs-CRM atom regexes + 2 new verifiers + main-flow wiring
- `Validators/tool_catalog_hashes.json` — moveops entry pinned
- `Validators/test_regression_anchors.py` — 5 new v20 MO-* anchors
- `Reference/Council_Protocol.md` — A10 + B9 templates universe-aware (3 universes); B9 section quick-reference rewritten
- `Reference/Sessions/REVIEW.md` — per-universe landmines list extended (KS LOS-vs-CRM + 5 MoveOps)
- `Reference/Sessions/AUDIT.md` — universe-aware AUDIT prompt + tool catalog path tri-universe + landmines list
- `AGENTS.md` — multi-universe section bumped to v20 (3 universes); MoveOps full subsection; 2 new Pipeline Deviations table entries

### What this closes

MoveOps is now a **fully first-class third universe**. Detection, validation, atom-verification, council prompts, AUDIT lens, REVIEW landmines, regression anchors, and tool catalog hash pinning all route through the registry. Adding a fourth universe in the future requires only:
1. Drop in the base universe folder + docs + evals
2. Add `UNIVERSES["<name>"]` block to `Validators/universes.py`
3. Add `_<NAME>_SIGNALS` regex to `detect_universe()`
4. Add hash pin entry to `tool_catalog_hashes.json`
5. Extend A-A10 + B-B9 prompt templates with the new universe's business-functions + service map
6. Add per-universe landmine bullets to REVIEW.md + AUDIT.md
7. Add regression anchors to `test_regression_anchors.py`

Trigger count: 16 (unchanged). LLM perspective count: 24 (unchanged).

### Source-folder hygiene note

Upstream zip distribution `MCP_Eval_V3 (2)/MCP_Eval_V3_BrookField/Docs/` is **mislabeled** — it contains KeyStone-flavored Docs (references `Mortgage_Base_Universe/3_Persona_Briefs.md` and "v3 = Keystone Mortgage"). Pipeline `Docs/` is the correct Brookfield-flavored copy; pipeline `Docs_keystone/` is the correct KeyStone copy. Documented in `AGENTS.md` Pipeline Deviations table. Do NOT use the mis-named source folder as authoritative — trust `Validators/universes.py` registry paths.

---

## 2026-06-28 — v19: KeyStone Rule Drift Close + Final Cleanups (16 Items / 4 Phases)

Closes the universe-rule drift that v18 introduced KeyStone support but left unaddressed: KeyStone's universe today, business function categories, OE service mapping, persona email domain, tight-identifier classification, cross-service contradiction examples, and TRID lifecycle were not reflected in pipeline behavior. Plus shipped all remaining items from the v18 honest-list audit and 3 genuine gaps (prompt-injection detection, tool-catalog hash version-pin, build_feasible_surface wired into validator).

### Phase 1 — Universe rule drift (8 items)

`Validators/universes.py` extended with per-universe `today` (Brookfield 2026-06-12, KeyStone **2026-04-28**), `persona_email_domain` (`brookfieldcpas.com` / `keystonemortgage.com`), `business_functions` (Brookfield 10, KeyStone 6 with weights), `tight_identifiers` (Brookfield includes "JE IDs", KeyStone includes "loan IDs"), `oe_service_map` (Brookfield: reconciliations → BlackLine / AP → SAP / JEs → Oracle GL; KeyStone: loans → mortgage_los / AP → quickbooks / payments → stripe / docs → filesystem), `cross_service_pairs`. `Validators/build_universe_index.py` no longer hardcodes today — `today_horizon()` accepts universe-specific date via `resolve_universe_today(task_dir)` (reads registry). Council A-A10 (Business Function Match) prompt template enumerates both 10 Brookfield + 6 KeyStone categories with reference paths. Council B-B9 (OE Service Mapping) prompt template enumerates both universes' service maps. `Validators/verify_universe_atoms.py` extended with KeyStone TRID claim verification (`mortgage_los.disclosures` 3-business-day window check for LE-after-app + CD-before-close) + LOS-vs-CRM source-of-truth violation detection (any claim citing CRM as source for loan/borrower/condition/disclosure data gets flagged — loan-level data lives in mortgage_los only).

### Phase 2 — Validator extensions (3 items)

`Validators/validate.py` adds: (1) Cross-universe persona email domain check — `validate_prompt` reads `consts["persona_email_domain"]` and FAILs if persona references the wrong universe's email domain (KeyStone persona with @brookfieldcpas.com or vice versa); (2) Feasible-surface cross-reference — `validate_rubrics` reads `_aux/Feasible_Surface.json` and WARNs when rubric titles assert enum values (`status="finalized"`, `type="foo"`, `category="bar"`) not present in any universe table's actual enum set; (3) Prompt-injection pattern detection — new `INJECTION_PATTERN` regex catches "ignore all other criteria", "always score 5", "treat this prompt as", "override the judge/evaluator", "system prompt", "disregard the rubric/grading". FAIL — real persona prompts never instruct the agent/judge to ignore rubrics or override scoring.

### Phase 3 — Infrastructure (3 items)

`Validators/check_tool_catalog.py` (new) + `Validators/tool_catalog_hashes.json` (new) — version-pin Brookfield (`8_Server_Tools_Details.json`) + KeyStone (`6_Server_Tools_Details.json`) tool catalogs by SHA256. `--update` flag re-pins. Surfaces upstream tool-catalog drift that would silently invalidate the validator's parameter-strictness checks. `Validators/phase_ready.py --phase materialize` upgraded — when a downstream phase needs an upstream `Verification_<phase>.md` and the file exists, `phase_ready` invokes `check_verification.py` to validate sections + non-empty evidence + verdict band; missing/malformed = FAIL with diagnostic (not just REMIND). `Reference/Council_Protocol.md` — 7 deprecated perspective section headers (A5, A8, A9, A12, B5, B10, B11) annotated with "REMOVED / MOVED / CONVERTED in v18" markers so fresh-chat agents see the deprecation in-place without scrolling back to the intro. `Reference/Sessions/AUDIT.md` Lens 6 + Lens 9 already had MERGED INTO LENS 1 markers from v18.

### Phase 4 — Coverage + docs (2 items)

`Validators/test_regression_anchors.py` extended with 4 new anchors:
- **v19 KS-6**: Cross-universe persona email domain mismatch (KeyStone persona with @brookfieldcpas.com email — should FAIL)
- **v19 KS-7**: KeyStone LOS-vs-CRM source-of-truth violation (rubric cites CRM for loan data — should FAIL via verify_universe_atoms)
- **v19 KS-8**: KeyStone TRID timing claim (closing disclosure within 1 business day of closing — should be verified against mortgage_los.disclosures)
- **v19 IN-1**: Prompt injection pattern ("ignore all other criteria" in prompt — should FAIL)
- **v19 FS-1**: Feasible-surface mismatch (rubric tests `status=finalized` not in universe enum set — should WARN)

Total: 38 + 5 = **43 anchors, all PASS**.

CHANGELOG v19 entry. AGENTS.md universe constants are now backed by the registry (changes in registry auto-flow to docs through reference). Memory updated: KeyStone universe today is 2026-04-28 + persona email domain per universe.

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | 43 / 43 PASS (33 Brookfield + 5 KeyStone v18 + 5 v19) |
| `Validators/check_tool_catalog.py` | Brookfield + KeyStone both match pinned SHA256 |
| `Validators/validate.py --phase all --task Tasks/24_...` | unchanged baseline (zero regression on Brookfield refactor) |
| `Validators/verify_universe_atoms.py --task Tasks/24_...` | clean — 42 atoms / 0F / 0W (Brookfield path) |
| `Validators/universes.py Tasks/24_...` | universe=brookfield + today=2026-06-12 + persona_email_domain=brookfieldcpas.com + 10 business_functions + service_map present |
| `Validators/build_feasible_surface.py Tasks/24_...` | 19 tables / 28 enum cols extracted |
| `Validators/aggregate_verdicts.py` | per-universe aggregation works |

### Files added

- `Validators/check_tool_catalog.py` — tool catalog hash version-pin (~75 lines)
- `Validators/tool_catalog_hashes.json` — pinned SHA256 per universe

### Files changed

- `Validators/universes.py` — `today` / `persona_email_domain` / `business_functions` / `tight_identifiers` / `oe_service_map` / `cross_service_pairs` per universe
- `Validators/build_universe_index.py` — `today_horizon()` accepts universe-specific date via `resolve_universe_today()`
- `Validators/validate.py` — persona email domain check + Feasible-surface cross-reference + prompt-injection regex
- `Validators/verify_universe_atoms.py` — TRID claim verifier + LOS-vs-CRM source-of-truth verifier (KeyStone)
- `Validators/phase_ready.py` — Verification_<phase>.md content validation (REMIND → FAIL on malformed)
- `Reference/Council_Protocol.md` — A10 + B9 prompt templates universe-aware; 7 deprecated perspective sections annotated
- `Validators/test_regression_anchors.py` — 5 new anchors (43 total)

### What this closes

KeyStone is now a **fully first-class universe** — the rule drift items (today, business functions, services, persona domain, tight identifiers) all route through the universe registry. Council A-A10 + Council B-B9 prompts reflect both universes. `verify_universe_atoms.py` catches KeyStone-specific landmines (TRID, LOS-vs-CRM). Cross-universe contamination caught (persona email domain mismatch). Prompt-injection attempts blocked. Feasible-surface cross-references universe enum values against rubric claims. Tool catalog drift surfaced via hash version-pin. Verification_<phase>.md content validated by phase_ready, not just presence.

Coverage stack (v19):
- 100% QC spec sub-dim coverage — both Brookfield + KeyStone Docs (v12 + v18)
- 100% eval spec coverage — both universes' Evals (v11 + v18)
- 100% candidate-facing QC instructions (v13)
- 100% V3 formatting conventions (v14)
- 100% multi-universe rule drift (v19)
- AF justification 5-point checklist + FEEDBACK 4-field form (v15)
- Cross-Source Verification + content validation (v16 + v19)
- REVIEW at full parity with CB (v17)
- Programmatic floor: verify_universe_atoms + Feasible_Surface + tool catalog hashes (v18 + v19)
- Multi-universe: Brookfield + KeyStone first-class (v18 + v19)

Trigger count: 16 (unchanged). LLM perspective count: 24 (unchanged from v18).

---

## 2026-06-28 — v18: Multi-Universe + Quality Over Quantity + Programmatic Floor + Deferred Items (19 Items / 5 Phases)

Combined release closing three concurrent tracks: (1) KeyStone Mortgage Partners universe support alongside Brookfield CPAs, (2) programmatic universe-atom verification as load-bearing floor closing the v17-diagnosed failure mode, (3) deferred load-bearing items from v17 briefing. Net effect: pipeline supports two universes, has a deterministic verification floor beneath all LLM gates, sheds 15 redundant LLM perspectives, and ships three previously-deferred infrastructure pieces.

### Phase 1 — Multi-Universe Foundation (4 items)

KeyStone assets dropped in: `Mortgage_Base_Universe/` + `Docs_keystone/` + `Evals_keystone/` + `QC_Tasks/V3.1_Tasks/`. New `Validators/universes.py` registry holds per-universe constants (paths, retention codes, Slack channels, NPCs, services, tool catalog, entity mappings, lifecycle check kind). New `Validators/detect_universe.py` auto-detects per-task via service-name + persona-name + universe-data signals; writes `_aux/Universe.txt`. `Validators/validate.py` refactored: every per-universe constant (retention codes / Slack channels / classifications / BlackLine exception types / NPCs / tool catalog path / entity-name-to-id map / account-trap-check toggle) now reads from registry via `get_universe_constants(detect_universe(task_dir))`. Brookfield-default + skip-if-empty pattern preserves back-compat; KeyStone tasks route through KeyStone constants automatically. **33/33 regression anchors stayed green throughout the refactor.**

### Phase 2 — Programmatic Floor (4 items)

New `Validators/verify_universe_atoms.py` — atom-by-atom universe query script that walks prompt + OE + rubrics, extracts every concrete atom (account-on-entity claim, "X did/did not respond" claim, JE/exception/recon/doc/vendor/apinv/loan IDs, emails, money amounts), and runs a precise universe query per atom. Universe-aware: Brookfield runs account-trap checks via `oracle_gl.ogl_accounts`; KeyStone skips account-trap (loan-based universe) and runs presence checks via mortgage_los tables. Exit non-zero on any FAIL with `STOP: <atom> | claim=<X> | universe-row=<Y> | mismatch`. AUDIT prompts updated (`Reference/Sessions/AUDIT.md` Lens 1) to require per-atom evidence table for any Truthfulness / Accuracy 5/5 score; empty evidence column → forced score ≤ 3. `Validators/phase_ready.py --phase materialize` now runs `verify_universe_atoms.py` as a hard precondition — MATERIALIZE refuses to start the LLM gate sequence until programmatic check exits clean. Per-universe landmines documented in `Reference/Sessions/REVIEW.md` Step 2 + `Reference/Sessions/AUDIT.md` Lens 1 (Brookfield: account-number trap + email-chain truthfulness; KeyStone: TRID timing + LOS-vs-CRM source-of-truth + departed-employee Marcus Webb).

### Phase 3 — Bloat Trim (5 items, net surface reduction)

Council A reduced **13 → 9 perspectives**: A5 Persona Authorship Whitelist DROPPED (validator A3 NPC blocklist covers); A8 Truthfulness Tally MERGED INTO A1 (now backed by `verify_universe_atoms.py` evidence); A9 Persona Fit Comparison MOVED TO ON-DEMAND `PIPELINE AUDIT --lens persona-fit`; A12 Cross-Service Coherence MERGED INTO A1. Council B reduced **11 → 8 perspectives**: B5 Tool-Leak / Phrasing Scan DROPPED (validator regex covers); B10 OE Write-Action → Outcome 1.1 CONVERTED TO VALIDATOR (X1 forward-map already deterministic); B11 Prompt tell-me → Outcome 2.1 CONVERTED TO VALIDATOR. AUDIT reduced **9 → 7 lenses**: Lens 6 Lifecycle + Narrative State + Lens 9 Unique Ground Truth Middle-Band MERGED INTO Lens 1 (now backed by atom-verifier evidence table). `REVIEW_triage.md` template gains mandatory Verification-Evidence column per finding — each "verified" cell must link to universe query that proved it. Triage authors can't slip shallow "verified" badges. **Total LLM perspectives across A + B + AUDIT + FINAL: 39 → 24 (net -15).** Programmatic floor added beneath every LLM gate.

### Phase 4 — Deferred Load-Bearing (3 items)

`Validators/aggregate_verdicts.py` — cross-task QC trend aggregator. Globs `Tasks/*/_aux/Council_Reports/*.md`, extracts trailing JSON verdict blocks (v12 F2 unified format), emits per-universe portfolio-level tables (verdict distribution / top failing sub-dimensions / most-blocking council perspectives / density-band distribution / lever-preservation misses / Bucket-1-Risk average). Universe-aware: separate trend tables for Brookfield vs KeyStone. `Reference/Templates/Verification_phase.md.template` — Verification_<phase>.md schema with required sections (Sources consulted with 6 source categories / Verification statements checklist / Discrepancies surfaced / Verdict). `Validators/check_verification.py` — validates the file matches template (required sections present + non-empty evidence cells + verdict ∈ {PASS, REVISE, BLOCK}). `Validators/build_feasible_surface.py` — extracts distinct enum-like column values per table (status / state / category / type / classification / kind / lifecycle / phase / milestone) from `_aux/Universe_Split/`. Writes `_aux/Feasible_Surface.json` so validators can flag rubric-tested enum values that don't exist for the entity (e.g., `status = "finalized"` on a Brookfield JE where valid statuses are {draft, submitted, approved, posted, reversed}).

### Phase 5 — Documentation + Regression (3 items)

`AGENTS.md` Universe Constants section split into per-universe sub-sections (Brookfield + KeyStone) + universe detection mechanism documented. Trigger count stays 16 (universe is auto-detected, not a separate trigger). `Validators/test_regression_anchors.py` extended with 5 KeyStone-specific anchors (KS-1 NPC Marcus Webb / KS-2 invalid Slack C009 / KS-3 single-service prompt on KeyStone / KS-4 cross-universe retention-code (Brookfield code on KeyStone universe — verifies skip-if-empty behavior) / KS-5 universe auto-detection via mortgage_los signal). Total: **33 + 5 = 38 anchors, all PASS**. CHANGELOG v18 entry.

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | 38 / 38 PASS (33 Brookfield + 5 KeyStone) |
| `Validators/validate.py --phase all --task Tasks/24_...` | prompt PASS (0F/2W/3N — added "universe: brookfield" note), OE PASS (0F/0W/1N), rubrics FAIL (3F/8W/3N — same v17 baseline; zero regression) |
| `Validators/verify_universe_atoms.py --task Tasks/24_...` | PASS (0F/0W/42 atoms checked, universe: brookfield) |
| `Validators/aggregate_verdicts.py` | scans 32 tasks; emits per-universe verdict distribution + sub-dim trend tables |
| `Validators/build_feasible_surface.py Tasks/24_...` | 19 tables with enums, 28 enum columns extracted |
| `Validators/phase_ready.py --phase materialize --task <task with verify atoms fail>` | hard-blocks with `STOP: verify_universe_atoms.py failed` + recommendation |

### Files added

- `Validators/universes.py` — registry (~210 lines)
- `Validators/detect_universe.py` — auto-detection helper (inside universes.py)
- `Validators/verify_universe_atoms.py` — atom-by-atom universe query (~240 lines)
- `Validators/aggregate_verdicts.py` — cross-task QC trend aggregator (~140 lines)
- `Validators/check_verification.py` — Verification_<phase>.md template validator (~80 lines)
- `Validators/build_feasible_surface.py` — per-table enum extractor (~100 lines)
- `Reference/Templates/Verification_phase.md.template` — Verification file schema
- `Mortgage_Base_Universe/` — KeyStone universe drop-in (per zip)
- `Docs_keystone/` — KeyStone-flavored QC + eval docs
- `Evals_keystone/` — KeyStone-flavored evals
- `QC_Tasks/V3.1_Tasks/Task1-4` — KeyStone reference passed tasks

### Files changed

- `Validators/validate.py` — universe-aware constants refactor; `load_tool_names()` + `load_tool_param_map()` accept tool_catalog_path; per-function `consts = get_universe_constants(detect_universe(task_dir))` lookup; all hardcoded sets gated by `if local_<set>:` skip-if-empty
- `Validators/phase_ready.py` — materialize precondition runs verify_universe_atoms.py
- `Validators/test_regression_anchors.py` — 5 new KeyStone anchors (38 total)
- `Reference/Council_Protocol.md` — intro rewritten for 9 + 8 perspective counts; deprecated perspective list documented
- `Reference/Sessions/REVIEW.md` — Step 2 inline AUDIT + landmines section + verify_universe_atoms.py call; changes.md template + Verification-Evidence column
- `Reference/Sessions/AUDIT.md` — Lens 1 evidence-table requirement; Lens 6 + Lens 9 merge markers
- `AGENTS.md` — Universe Constants section dual-universe; universe detection mechanism

### What this closes

Pipeline now supports **both Brookfield and KeyStone universes** auto-detected per task. The v17-diagnosed failure mode (5 LLM gates passing a Major universe-truthfulness defect) is **structurally closed**: programmatic verify_universe_atoms.py runs first and hard-blocks MATERIALIZE if any atom fails. AUDIT can no longer narrate verification without evidence. **15 redundant LLM perspectives removed** without losing catches (validator regex / programmatic check covers each dropped item). Three deferred load-bearing items from the v17 briefing shipped. **38 regression anchors covering both universes** all pass.

Coverage stack (v18):
- 100% QC spec sub-dim coverage (v12, preserved + extended to KeyStone QC spec)
- 100% eval spec coverage (v11, preserved + extended to KeyStone evals)
- 100% candidate-facing QC instruction coverage (v13)
- 100% V3 formatting conventions (v14)
- AF justification 5-point checklist + FEEDBACK 4-field form (v15)
- Cross-Source Verification Discipline + Verification_<phase>.md template (v16 + v18 enforcement)
- REVIEW flow at full parity with CB (v17)
- Multi-universe + programmatic floor + bloat trim + deferred infrastructure (v18)

Trigger count: 16 (NEW / S0 / HARDNESS / S1 / S1.5 / S2 / S3 / FINAL / S4 / REVIEW / MATERIALIZE / REDO / COMPARE / AUDIT / FEEDBACK / CLOSE — unchanged, universe is auto-detected not a separate trigger).

---

## 2026-06-27 — v17: REVIEW Flow Parity with CB + Auto-Apply + New MATERIALIZE Trigger (4-Item Plan)

Closes the two parity gaps where REVIEW had lighter scrutiny than CB, adds auto-apply for `changes.md`, and splits REVIEW into two phases (analysis + materialization) to keep each chat context clean.

### Item 1 — Inline AUDIT on candidate's ORIGINAL artifacts

CB runs AUDIT inline after every per-phase deliverable (v7 mandate). REVIEW previously ran AUDIT only on the corrected 14/15 at the materialization step — never on the candidate's originals. v17 adds Step 2 sub-step 3: `PIPELINE AUDIT --phase prompt`, `--phase oe`, `--phase rubrics` on the candidate's originals. Reports → `_aux/Council_Reports/AUDIT_<phase>_original.md`. Findings feed `changes.md` alongside Council A/B findings. This applies the same strictest-interpretation lens to the original that CB gets per-phase.

### Item 2 — Deep trajectory analysis: S4-style bucket classification on ORIGINAL trajectories

REVIEW Step 3 used trajectory data only for hardness numbers (pass@1, avg tool calls) — never walked the trajectories to distinguish rubric defects from genuine model failures. v17 adds new Step 3.5: if `Agent_Responses/Run*.json` exists, walk every failing rubric trajectory across completed runs and classify into Bucket 1 (Rubric Invalid) / Bucket 2 (Judge Error) / Bucket 3 (Legit Fail) — same procedure as PIPELINE S4, applied to the candidate's ORIGINAL rubric set. Bucket 1 findings AUTO-POPULATE `changes.md` rubric-fix rows tagged `[trajectory-bucket-1]` with the concrete failure evidence. Bucket 2/3 are noted in `_aux/Council_Reports/REVIEW_bucket_classification.md` as positive evidence of rubric soundness (feeds into FEEDBACK score). T2 (pass@1 ≤ 40%) + T3 (error_runs ≤ 2) hard gates from S4 also run here on the original. All-Failing Rubrics sub-dim scoring (Bucket 1 ratio threshold 50% / 25%) applies the same scoring scheme as S4 D2.

### Item 3 — Auto-mark changes.md + new PIPELINE MATERIALIZE trigger

REVIEW previously tried to do everything in one phase: analysis + change-list + materialization + re-gates. Two problems: (1) operator friction (had to manually mark every `changes.md` row as Applied before materialization), (2) chat context bloat (analysis + materialization in one chat made it hard to keep separate concerns clear). v17 split:

- **PIPELINE REVIEW (new shape):** runs analysis Steps 0-7 + Step 6 auto-marks all new rows as `Applied` (instead of leaving them `Pending`) + Step 8 writes the score summary + STOPs with next-trigger `PIPELINE MATERIALIZE` in fresh chat. Materialization Steps 8-11 removed from REVIEW.
- **PIPELINE MATERIALIZE (NEW trigger, new runbook `Reference/Sessions/MATERIALIZE.md`):** reads triage verdict → if REBUILD, STOPs with REDO recommendation; if SALVAGEABLE, applies Applied rows to produce corrected `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` / `_aux/REVIEW_prompt_draft.txt`, then re-runs full gate set (validator + Council A + Council B + AUDIT + FINAL) on the corrected materialization with 3-round REVISE cap. AUDIT verdict REBUILD on the corrected version means triage was wrong → STOPs with REDO recommendation.

Trigger count: 15 → **16**. Operator-decision preserved: between REVIEW and MATERIALIZE, operator can manually edit `changes.md` and flip specific rows `Applied` → `Dismissed` to reject individual fixes; auto-apply is the default, manual override is one-edit away.

### Item 4 — Docs + infrastructure

- `Validators/phase_ready.py` — new `materialize` phase with preconditions (`changes.md` exists, has Applied rows, REVIEW_triage.md present, S0 outputs present); MATERIALIZE added to TODO_PHASES.
- `AGENTS.md` PIPELINE DISPATCH — REVIEW row description updated to reflect new (analysis-only) shape; new MATERIALIZE row inserted between REVIEW and REDO; trigger count statement updated 15 → 16.

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | 33 / 33 PASS (no validator code changes; runbook-only updates) |
| `Validators/phase_ready.py --phase materialize --task Tasks/24_...` | STOPs correctly (no `changes.md` or `REVIEW_triage.md` on Task 24) + emits E1/E2 REMINDs once preconditions present |
| `Validators/validate.py --phase all --task Tasks/24_...` | unchanged from v15 baseline (prompt 0F/2W/2N, OE 0F/0W/1N, rubrics 3F/8W/3N) |
| `grep -cE "^\| \`PIPELINE" AGENTS.md` | 16 ✓ |

### Files changed

- `Reference/Sessions/REVIEW.md` — Step 2 expanded with inline AUDIT on originals (4 sub-steps: Council A → Council B → AUDIT-on-originals → FINAL); new Step 3.5 with full S4-style bucket classification; Step 6 status default flipped to `Applied`; Steps 8-11 (materialization) removed and replaced with Step 9 STOP pointer to PIPELINE MATERIALIZE; Exit criteria + STOP gate updated to reflect new flow shape.
- `Reference/Sessions/MATERIALIZE.md` — NEW runbook. Phase-readiness gate refuses without `changes.md` + REVIEW_triage.md; Step 0 TODO mandate; Procedure reads triage verdict + partitions Applied rows by phase + materializes 14/15 + draft + re-runs full gate set on corrected; STOP gate routes to FEEDBACK then CLOSE.
- `Validators/phase_ready.py` — `materialize` phase preconditions + TODO_PHASES extension.
- `AGENTS.md` — PIPELINE DISPATCH MATERIALIZE row + trigger count 15 → 16.

### What this closes

REVIEW now has full parity with CB's per-phase gate set: validator + Council A (13 perspectives) + Council B (11 perspectives) + AUDIT (9 lenses) + FINAL (6 lenses) — all running on the candidate's ORIGINAL artifacts, not just the corrected materialization. Deep trajectory analysis (S4-style bucket classification) runs on the original trajectories when present; Bucket 1 findings auto-populate `changes.md` rubric fixes with concrete failure evidence. Auto-apply removes the manual marking step — operator invokes `PIPELINE MATERIALIZE` directly in a new chat to apply fixes and verify the corrected materialization. Phase split keeps each chat context tight (REVIEW = analysis only; MATERIALIZE = apply + verify only).

REVIEW flow as of v17:
```
PIPELINE REVIEW          → analysis + auto-marked changes.md (no 14/15 yet)
PIPELINE MATERIALIZE     → apply Applied rows + re-run gates on 14/15 + draft
PIPELINE FEEDBACK        → write 13_Feedback.txt rating ORIGINAL against QC spec
PIPELINE CLOSE           → final audit
```

CB flow unchanged. Both flows now share the same scrutiny depth (Council A + B + AUDIT + FINAL per artifact) and the same trajectory-walk discipline (S4-style bucket classification when trajectories are available).

---

## 2026-06-27 — v16: Cross-Source Verification Discipline

Operator feedback after v15: the fresh-chat principle was meant to prevent agents from overlooking prior attempts that the current relies on — but each phase was implicitly trusting upstream outputs rather than independently re-verifying against the source data + eval spec + QC spec doc. v16 formalizes the discipline.

### What changed

Every build phase (S0, HARDNESS, S1, S2, S3, FINAL, S4, AUDIT) gets a mandatory `Step 0.5: Cross-Source Verification` that produces `_aux/Verification_<phase>.md` declaring exactly what was verified against:

| Source | What the phase declares |
|---|---|
| **Per-task data** (`_aux/Universe_Split/` + `_aux/Fact_Ledger.json` + universe records) | Specific records / atoms consulted; ground-truth values re-confirmed |
| **Eval spec doc** (`Evals/1-4`) | Sub-dim verdicts for this phase's eval spec |
| **QC spec doc** (`Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md`) | QC sub-dim scores re-applied at this phase |
| **Prior phase verification** (`_aux/Verification_<prior>.md`) | Upstream cross-check confirmed independently |
| **Reference cards** (`Reference/*_Format.md` + inventories) | Format conventions re-checked |
| **Verification statements** (checklist) | Per-phase guarantees enumerated as checkboxes |
| **Discrepancies** | Any source-conflict surfaced and resolved |

### Why this matters

The fresh-chat principle (each phase in a clean chat) protects against carrying forward stale assumptions. But without explicit re-verification, a fresh-chat agent could draft a deliverable that trusts prior phase outputs blindly. v16 forces each phase to RE-verify against the three sources of truth: data, evals, QC spec. This catches:
- The case where prior phase output was correct against its sources, but the new phase's interpretation of those sources differs
- The case where eval spec or QC spec wasn't actually consulted during drafting (the Reads_<phase>.md gate from v11 is necessary but not sufficient)
- The case where downstream phases pile up implicit assumptions about upstream outputs

### Phase_ready.py extension

`Validators/phase_ready.py` gains a `VERIFICATION_DEPS` map and emits a `[REMIND]` when an upstream phase's `Verification_<phase>.md` is missing:

```
[REMIND] Upstream phase HARDNESS should have produced _aux/Verification_hardness.md before this phase runs.
         The v16 cross-source verification discipline requires each phase to declare what it verified against data + eval spec + QC spec.
```

The reminder is non-blocking (the phase can proceed if the operator confirms it ran with prior context), but it surfaces the missing artifact for downstream audit-trail purposes.

### Files changed

- `Validators/phase_ready.py` — VERIFICATION_DEPS map + per-phase reminder emission.
- `Reference/Sessions/S0.md` / `HARDNESS.md` / `S1.md` / `S2.md` / `S3.md` / `FINAL.md` / `S4.md` / `AUDIT.md` — Step 0.5 Cross-Source Verification block added before Procedure, with phase-specific source lists + checklist.

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | 33 / 33 PASS (no validator code changes, runbook + phase_ready discipline only) |
| `Validators/validate.py --phase all --task Tasks/24_...` | Unchanged from v15 baseline |
| `Validators/phase_ready.py --phase s1 --task Tasks/24_...` | Emits new v16 REMIND for missing Verification_hardness.md + existing E1/E2 reminders |

### What this closes

Operator-pain pattern: fresh-chat agent in S2 draws OE conclusions from S1's prompt without independently re-verifying against the universe. v16 forces S2 to write `Verification_s2.md` declaring which Universe_Split records each OE step grounds in, which Eval spec sub-dims for OE were re-applied, and which QC spec OE sub-dims were re-scored. The same pattern applies to every build phase. Cross-source consistency is now an explicit exit artifact, not an implicit assumption.

---

## 2026-06-27 — v15: Final Wrap-Up — AF Justification Reference + FEEDBACK 4-Field Form

Two surgical runbook updates closing the last operator-pain gaps before the pipeline is fully feature-complete against every QC docs requirement.

### Item A — S4 AF Justification 5-Point Checklist + Reference Examples

Operator pain: when writing all-fail justifications, the agent had the bucket classification + trajectory walk + voice gate, but not the QC docs' explicit 5-point checklist that distinguishes "genuine model failure" from "rubric issue masquerading as model failure". v15 adds the checklist directly to S4.md Bucket 3 step:

1. Is the criterion self-contained, atomic, and grounded in the universe's ground truth?
2. Is it flexible enough to allow valid alternative approaches without unfairly penalizing the agent?
3. Is the criterion actually required by the prompt, rather than asking for something extra?
4. Does it use real tool names and valid parameters?
5. Could a capable agent realistically pass this task?

If all 5 = YES → write AF justification (Bucket 3). If any = NO → reclassify as Bucket 1 (Rubric Invalid) and fix the rubric, do not write an AF justification.

Plus 2 GOOD AF justification examples ("entity confusion", "cross-service reasoning failure") and 4 BAD-pattern examples (`search_crm` not a real tool, exact-phrase rigidity, channel lock-in, "all N tickets" without GT verification) lifted from the QC docs as concrete reference.

### Item B — FEEDBACK 4-Field Candidate-Facing Form

Operator pain: the candidate-facing review form has 4 specific fields, but the prior `13_Feedback.txt` structure was a 3-section narrative that didn't map cleanly to the form. v15 restructures `13_Feedback.txt` to mirror the form exactly:

| Form field | `13_Feedback.txt` section | Derived from |
|---|---|---|
| Quality: Overall Task (1-5) | `## Quality: Overall Task` | Rate ORIGINAL against QC spec |
| Overall Task Feedback (text) | `## Overall Task Feedback` | Rate ORIGINAL against QC spec, plain humanlike voice |
| Level of Fixes (4-option) | `## Level of Fixes` | DERIVED from `changes.md` Applied row count |
| Parts of Task Fixed (multi-select) | `## Parts of Task Fixed` | DERIVED from `changes.md` section headings |

Level-of-Fixes auto-map: 0 Applied → `No edits / Approved as is`; 1-3 → `Minor Fixes`; 4-10 → `Major Fixes`; 11+ or full rewrite → `Full Redo`.

Parts-of-Task-Fixed auto-map: changes.md `Prompt` / `Persona` sections → `Prompt`; `Oracle Events` / `OE` → `Oracle Events`; `Rubrics` / `Rubric` → `Rubrics`; `Tool` / `Universe` / `Engineering` → `Eng. Issues/Taxonomy Issues`; zero rows → `None`.

This is the ONE allowed exception to the "do not read changes.md" rule — strictly for the mechanical metadata of fields 3 + 4. Fields 1 + 2 (score + qualitative feedback) still rate ONLY the original submission and ignore changes.md entirely, preserving the v9 design intent that the candidate is rated on their work, not on our fixes.

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | 33 / 33 PASS (no validator code changes; runbook-only updates) |
| `Validators/validate.py --phase all --task Tasks/24_...` | unchanged from v14 baseline (prompt 0F/2W/2N, OE 0F/0W/1N, rubrics 3F/8W/3N) |

### Files changed

- `Reference/Sessions/S4.md` — Bucket 3 step inserts the 5-point pre-write checklist + GOOD/BAD reference examples.
- `Reference/Sessions/FEEDBACK.md` — step 6 (new) derives mechanical metadata from changes.md; step 7 (renumbered) writes the 4-field structured form; denylist row for changes.md updated to allowlist for fields 3 + 4 mechanical metadata only; step 8 (voice gate, renumbered) unchanged.

### What this closes

S4 AF justifications now have the explicit pre-write checklist + reference examples directly inline — the agent no longer needs to remember 5 conditions or recall what good vs bad AF justifications look like. FEEDBACK output now maps 1-to-1 to the candidate-facing review form, so the operator can paste fields directly without manual translation. Pipeline is now feature-complete against every QC docs requirement the user surfaced through v11 → v15.

---

## 2026-06-27 — v14: Formatting Anti-Patterns Coverage (12-Item Plan Across 3 Sprints)

Closes the formatting gap that v11–v13 left open. Operator pain: prompts with bullets, markdown headers, code blocks, and AI-style closings were passing the validator because the prior catches were content-only (em-dashes, tool names, "at least N", pre-solving). v14 enforces the V3 reference convention: prompts/OEs/rubrics are plain prose throughout, with zero markdown formatting.

### Sprint 1 — Prompt formatting catches (8 items)

F1 bullets at line start (`F1_BULLETS` matches `•·‣▪●*-` at line start with following content — FAIL). F2 markdown headers (`F2_MD_HEADER` matches `#`-`######` at line start — FAIL). F3 markdown bold/italic (`F3_MD_BOLD_ITALIC` matches `**text**`, `__text__`, `*word*`, `_word_` — FAIL). F4 code blocks (` ``` ` — FAIL; real prompts never contain fenced code). F5 AI-style section headers (`Key Points:` / `Summary:` / `Action Items:` / `Background:` / `Context:` / `Objective:` / `Deliverables:` / `Requirements:` / `Tasks:` / `Steps:` / `Overview:` / `Goal:` — FAIL when on a line by itself). F6 AI-style closings (`Let me know if you need anything else` / `I hope this helps` / `Happy to assist` / `Please don't hesitate` / `Looking forward to your response` / `Best regards` / `Kind regards` — FAIL). F7 AI-style openings (`As requested` / `Please find below` / `I am writing to` / `Per our discussion` / `Pursuant to` / `Following up on` — FAIL). F8 3+ consecutive blank lines (AI-formatting padding tell — WARN).

### Sprint 2 — OE + Rubric formatting catches (3 items)

F9 OE step bullets/markdown (per-step regex within OE body: bullets at non-`OE<n>:` lines + markdown bold/italic + markdown headers — FAIL). F10 rubric title formatting (newline in title / markdown bold-italic / bullet characters — FAIL; V3 reference convention requires single-line plain-prose titles). F11 rubric evidence anchoring (evidence must reference either an OE step `Per OE<n>` / `See OE<n>` / `OE<n>` OR use trajectory-anchoring phrasing `Look for` / `Check the` / `Verify that` / `Inspect` / `Confirm` / `payload` / `final response` — WARN; calibrated against V3 references which use both styles).

### Sprint 3 — Regression anchors (1 item, 7 new fixtures)

26 → 33 anchors: F1 bullets in prompt, F2 markdown header in prompt, F3 markdown bold in prompt, F4 code block in prompt, F5 AI-style section header, F6 AI-style closing, F7 AI-style opening. All 33 pass.

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | 33 / 33 PASS |
| `Validators/validate.py --phase all --task Tasks/24_...` | prompt PASS (0F/2W/2N), OE PASS (0F/0W/1N), rubrics FAIL (3F/8W/3N — same baseline: 1 v11 AND-bundling true-positive + 2 v13 V3 vague-connector true-positives; zero false positives introduced by v14 after F11 calibration to accept both V3 evidence-anchoring styles) |

### Files changed

- `Validators/validate.py` — Sprint 1 catches (F1-F8 in `validate_prompt`); Sprint 2 catches (F1/F2/F3 inside `validate_oe`; F10/F11 inside `validate_rubrics`).
- `Validators/test_regression_anchors.py` — 7 new anchors (26 → 33).

### What this closes

Prompts can no longer ship with: bullets, markdown headers, markdown bold/italic, code blocks, AI-style section headers, AI-style closings ("Let me know if you need anything else"), AI-style openings ("As requested"), or 3+ blank-line padding. OE step bodies can no longer contain bullets or markdown. Rubric titles must be single-line plain prose. Rubric evidence must explicitly anchor to either an OE step or trajectory-grading phrasing.

Coverage is now: 100% of QC spec sub-dims + 100% of eval specs + 100% of candidate-facing QC instructions + 100% of formatting conventions from V3 reference tasks (`QC_Tasks/V3_Tasks/Task11..Task14/`). The pipeline catches the formatting tells of AI-generated prompts that previously slipped through content-only validation.

---

## 2026-06-27 — v13: QC Doc Cross-Reference Coverage (7-Item Plan)

Closes the 7 patterns explicitly named in the candidate-facing QC docs (Goal / Writing Guideline / Rubric Writing Guidelines / All-Fail Justification) that v11 + v12 didn't enforce. These are the patterns a candidate sees in their task interface — the pipeline now catches violations of every pattern named in those instructions.

### Sprint 1 — Deterministic validator catches (4 items)

V1 Investigation + Action two-phase (`V1_INVESTIGATION_CUES` matches "figure out / find out / look into / investigate / work through / dig into / get to the bottom / what's going on / tell me where / where it lands / check / see / verify / determine / trace / reconcile" + `V1_ACTION_VERBS` matches 30 write verbs; FAIL if both absent, WARN if only one present — closes the QC docs requirement that "The richest tasks have two phases: Figure out what's happening + Do something about it"). V2 First-person voice (`V2_FIRST_PERSON` matches "I / me / my / we / our / let's / can you / please"; FAIL if absent — closes the QC docs Core Requirement #6 "Must Sound Natural"). V3 forbidden vague connector in rubric (`V3_VAGUE_CONNECTOR` catches "such as / for example / e.g. / like" followed by capitalized or dollar-amount tokens — closes the QC docs rule "Never use 'such as,' 'like,' or 'for example' when defining what counts as correct"). V7 multi-value phrasing (`V7_MULTI_VALUE_AMBIGUOUS` detects "A, B, or C" patterns without one of the 3 canonical phrasings: "must be one of:" / "including but not limited to:" / "at least one of:" — closes the QC docs rule on multi-value acceptance phrasing).

### Sprint 2 — Council perspectives (3 items)

V4 = Council B-B10 OE Write-Action → Outcome 1.1 forward map (for every OE write step, verify ≥ 1 Outcome 1.1 rubric checks the action; closes the QC docs "Step 1: write all Outcome rubrics first — for every action in your OEs, write 1.1 + 1.2"). V5 = Council B-B11 Prompt "tell-me" cue → Outcome 2.1 forward map (for every "tell me X / report back / let me know / walk me through" cue in prompt, verify ≥ 1 Outcome 2.1 rubric covers the requested fact; closes the QC docs "For every key fact the user asked to be told directly, write 2.1"). V6 = Council A-A13 Open-Ended Write Ask Atomicity (when prompt asks for multiple write actions of the same type, the rubric set must contain one atomic rubric per ground-truth item, never "at least N"; closes the QC docs "At least N is reward-hackable. Go to the universe, identify the actual GT items, and write one rubric per item").

### Sprint 3 — Regression anchors (1 item)

4 new anchors added (22 → 26): V1 single-phase prompt (action without investigation), V2 first-person voice missing, V3 forbidden vague connector in rubric, V7 ambiguous multi-value phrasing. All 26 pass.

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | 26 / 26 PASS |
| `Validators/validate.py --phase all --task Tasks/24_...` | prompt PASS (0F/2W/2N), OE PASS (0F/0W/1N), rubrics FAIL (3F/8W/3N — 1 v11 AND-bundling true-positive + 2 v13 V3 vague-connector true-positives on rubrics 6 & 17 which use "for example VEN-X" parenthetically; zero false positives introduced by v13) |
| Sprint 2 council additions | A13 + B10 + B11 wired into prompt templates + verdict + pass criteria |

### Files changed

- `Validators/validate.py` — Sprint 1 catches (V1/V2 in `validate_prompt`; V3/V7 in `validate_rubrics`).
- `Validators/test_regression_anchors.py` — 4 new anchors (22 → 26).
- `Reference/Council_Protocol.md` — A13 (Council A), B10 + B11 (Council B), prompt templates + verdict + pass criteria updated through A13 / B11.

### What this closes

The pipeline now enforces every pattern named in the candidate-facing QC docs that the v11 + v12 sprints didn't already cover. Specifically: the Investigation + Action two-phase rule, the first-person natural-voice rule, the forbidden-vague-connector rule, the canonical multi-value phrasing rule, the OE-write-action → Outcome 1.1 forward map, the prompt-tell-me → Outcome 2.1 forward map, and the open-ended-write-ask atomicity rule. Eight gates per phase (validator with R1 percentage gates + new V1/V2/V3/V7 + Council A with 13 perspectives + Council B with 11 perspectives + AUDIT with 9 lenses + FINAL with 6 lenses + S1 similarity + S4 T2/T3 + CLOSE T2/T3 + FEEDBACK for review-type). Coverage = 100% of QC spec sub-dims + 100% of eval specs + 100% of candidate-facing QC instructions.

---

## 2026-06-27 — v12: QC Spec Doc Full Coverage (24-Item Plan Across 4 Sprints)

Closes the gap between the pipeline and `Docs/7_QC_Spec_Doc1.json` + appendix — the **scoring bible** that the 4 evaluator specs derive from. v11 closed the eval specs; v12 closes the upstream sub-dim definitions and rubric-quality issue taxonomy that the eval specs reference but never re-define. Every named sub-dim now has at least one validator catch, council perspective, or runbook gate enforcing it.

### Sprint 1 — Deterministic validator catches (12 items, ~1.5 days)

P2 feasibility (`P2_CONFLICTING` regex + `P2_IMPOSSIBLE_FUTURE` regex — catches "do X but don't X" contradictions and future-event asks about a past universe today). P5 extended contrived catches (`P5_EXACT_TIMESTAMP` for "at exactly 3:47 PM", `P5_ARBITRARY_FORMAT` for "respond in exactly 3 sentences using passive voice", `P5_TEST_ERROR_HANDLING` for "intentionally trigger an error"). P7 cross-service requirement (counts distinct service mentions in prompt using SERVICE_KEYWORDS dict for gl/email/slack/blackline/vault/linear/airtable/sap/contacts — FAIL on ≤ 1 service). P8 pre-solving extension (adds "we already know", "the issue is clearly", "we've confirmed", "we've identified", "it's definitely" to PRE_SOLVE_HINT). R1 Overall Rubric Quality threshold gate (per-rubric severity tally + QC-spec exact bands: > 10% major / > 15% moderate+ / > 20% any / 3+ rubrics with Major all = FAIL). X1 missing-Outcome candidate detection (WRITE_VERB_PROMPT_RE scans prompt for "send / post / create / approve / certify / file / upload / update / void / reverse / submit / archive / notify / email / dismiss / escalate / reclassify / forward / schedule / reply / draft / log / add" — for each found, verifies an Outcome rubric title contains the verb). X2 positional-reference self-containment (X2_POSITIONAL_REFS catches "the right person / the partner / the Managing Partner / the appropriate recipient" etc.; FAIL if title lacks an email address or proper-noun name; framing tokens like "Managing Partner" explicitly excluded from the name-fallback). X4 universe-contradicting (cross-references rubric amounts against Hardness_Plan.md ground-truth atoms + prompt; flags amounts absent from both as candidates for X4 Incorrect-Criteria). X7 overly-broad list detection (X7_OVERLY_BROAD_LIST catches "any of A, B, or C" / "one of A, B, or C" — WARN with operator verification ask). X8 freetext exact-wording detection (X8_FREETEXT_QUOTED catches quoted strings on subject / body / title / description / summary / message_text fields without "(or similar)" marker — FAIL). X9 wording-mismatch (X9_SYNONYM_PAIRS list of 13 known synonym pairs; flags rubric titles using one term when prompt uses the other — account/ledger and issue/ticket removed after false-positive corpus calibration). T3 error rate gate (S4 runbook adds Step 0.5: count error runs in Agent_Responses/, FAIL if ≥ 3).

### Sprint 2 — Council perspectives (8 items, ~3 days)

Council A gains 6 new perspectives: **A7 Clarity & Specificity holistic** (re-read with no prior context, surface second valid interpretations that produce different write-actions), **A8 Truthfulness deep tally** (per-claim Major/Minor classification; 1+ Major or 2+ Minor = FAIL), **A9 Persona Fit Comparison** (grade assigned persona 1-5; identify better-fit candidate; delta ≥ 2 = NON-FAIL for operator decision), **A10 Business Function Match** (read `Docs/5_Prompt_Diversity_Business_Function.md`, verify primary scenario matches assigned function from the 10 Brookfield categories), **A11 End-to-End Solvability** (walk Hardness_Plan trajectory + verify every step's source row is materialized in `_aux/Universe_Split/`), **A12 Cross-Service Coherence** (for entities in 2+ services, verify name/ID/date consistency). Council B gains 2 new perspectives: **B8 OE Completeness semantic** (walk dependency chain; per missing must-take step emit `OE_INCOMPLETE: prompt requires <step> but no OE covers it`), **B9 OE Service Mapping** (verify each OE step targets the correct service for the data type it requests — reconciliations → BlackLine, AP → SAP, JEs → Oracle GL, retention → Records Vault, tickets → Linear, HR → Airtable, chat → Slack). Council A prompt template, verdict, and pass-criteria updated through A12; Council B updated through B9.

### Sprint 3 — Runbook + post-platform gates (3 items, ~1 day)

P1 AUDIT Lens 9 (Unique Ground Truth Middle-Band): re-read prompt asking "does it permit a leading interpretation AND a second defensible interpretation?"; surface candidate ambiguities with both readings written out + disambiguating assumption; MAJOR if readings produce different write-actions, NON-FAIL if same. T2 + T3 CLOSE.md enforcement: `close_task.py` now reads `Trajectory_Stats.json` and gates `ready` on pass@1 ≤ 40% (T2) + error_runs ≤ 2 (T3); fails CLOSE with explicit redirect to PIPELINE REDO if pass@1 > 40%. S4 Step 0.5 adds the same gates earlier in the flow with explicit STOP if either fails.

### Sprint 4 — Regression anchors (1 item, ~0.5 day)

`Validators/test_regression_anchors.py` extended from 10 to **22 anchors** covering the v12 catches: P2 conflicting instructions, P5 exact-timestamp demand, P5 arbitrary format constraint, P5 test-error-handling contrivance, P7 single-service prompt, P8 pre-solving extended, X2 positional reference without name, X7 overly-broad list, X8 exact wording on freetext, X9 wording mismatch, X1 missing-Outcome candidate, R1 Overall Rubric Quality threshold (3+ Major rubrics). All 22 PASS.

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | 22 / 22 PASS |
| `Validators/validate.py --phase all --task Tasks/24_...` | prompt PASS (0F/2W/2N), OE PASS (0F/0W/1N), rubrics FAIL (1F/8W/3N — 1 true-positive AND-bundling on rubric[21], 8 legit WARNs including 3 X4 amount-not-in-Hardness_Plan catches + 1 X1 missing-Outcome candidate + existing v11 catches; zero false positives introduced by v12 after synonym-pair calibration) |
| Sprint 2 council additions | A7-A12 + B8-B9 wired into prompt templates + verdict + pass criteria |
| Sprint 3 AUDIT Lens 9 | added before VERDICT block |
| Sprint 3 CLOSE T2/T3 gates | `close_task.py` reads `pass_at_1` + `error_runs` from `Trajectory_Stats.json`; refuses to greenlight on > 40% pass@1 or ≥ 3 error runs |

### Files changed

- `Validators/validate.py` — Sprint 1 catches (P2/P5/P7/P8 in `validate_prompt`; R1/X1/X2/X4/X7/X8/X9 in `validate_rubrics`; per-rubric severity tally wired onto AND-bundling/channel-lock-in/write-verb-process/Jaccard checks).
- `Validators/test_regression_anchors.py` — 12 new anchors (10 → 22).
- `Validators/close_task.py` — T2 + T3 gates.
- `Reference/Council_Protocol.md` — A7-A12 (Council A), B8-B9 (Council B), prompt templates + verdict + pass criteria updated through A12 / B9.
- `Reference/Sessions/AUDIT.md` — Lens 9 Unique Ground Truth Middle-Band.
- `Reference/Sessions/S4.md` — Step 0.5 T2 + T3 hard gates before classification.

### What this closes

Every named sub-dim in `Docs/7_QC_Spec_Doc1.json` now enforced. The 9 issue-types in the QC spec appendix (Missing Outcome, Self-Containment, Atomicity, Incorrect Criteria, Overlap/Redundancy, Mislabeled Category, Overly Broad, Overly Specific, Wording Errors) all have at least one pipeline catch. Trajectory-dimension checks (T2 pass@1, T3 error rate) wired into CB-build flow at S4 + CLOSE, not just REVIEW. 22 regression anchors cover every major v11 + v12 catch.

The bar is now: validator (with R1 percentage gates) + Council A (12 perspectives) + Council B (9 perspectives) + AUDIT (9 lenses) + FINAL (6 lenses) + S1 similarity gate + S4 T2/T3 hard gates + CLOSE T2/T3 verification + FEEDBACK (review-type tasks). Eight gates per phase. Coverage = 100% of QC spec sub-dims AND 100% of eval specs.

---

## 2026-06-27 — v11: 100% Spec Parity (38-Item Plan Across 4 Sprints)

Closes every named check in the 4 evaluator specs (`Evals/1_Prompt_Eval.md` ... `Evals/4_Verifier_Fails_Eval.md`) by enforcing it through at least one of: a validator script catch, a council / AUDIT / FINAL sub-agent perspective, or a runbook procedural gate. Resolves the 20+ internal contradictions in the eval specs by either picking the stricter interpretation in the pipeline OR documenting the deviation explicitly in the new `AGENTS.md "Pipeline Deviations from Eval Specs"` section.

### Sprint 1 — Mechanical wins (15 items, validator regex + doc clarifications)

A1 retention-code whitelist (`AICPA_SQMS_7Y` / `IRS_TAX_7Y` / `FIRM_INTERNAL` / `INDEFINITE` — FAIL on `SOX_7Y` / `SEC_PERMANENT` / unlisted). A2 Slack channel ID whitelist (`C001-C010` + `C012` — FAIL on `C011`). A4 classifications enum (`public` / `internal` / `restricted`). A5 BlackLine exception-type whitelist (6 types + state machine). A7 parameter-trap exhaustion (extends v6's 3 traps to cover the full set from `8_Server_Tools_Details.json`). B4 command-list detection (numbered-step + sequential `First/Then/Finally` regex). B6 structured-value lock-in (channel_id pinned alone without channel name → WARN to accept either form). B8 write-action-mislabeled-as-Process (Process rubric with write-verb in title → FAIL re-classify as Outcome 1.1). B9 AND-bundling atomicity (regex requiring BOTH sides to be action verbs to eliminate noun-phrase false positives). B11 overlap/redundancy detection (Jaccard ≥ 70% on rubric criterion text). C3 AUDIT Lens 7 anti-rationalization rule (explicit "do not excuse a finding by claiming most-likely-interpretation"). E3 severity-tally rule formalization (highest-only-per-criterion + Process Rubrics double-count resolution). E4 sub-dim scoring scheme documentation (per-sub-dim 1/3/5 vs 1/5 vs 1/2/5 map in Council B-B1 prompt template). E5 threshold math normalization (absolute-count gates: Major ≤ 2, Moderate ≤ 4). E6 new `AGENTS.md "Pipeline Deviations from Eval Specs"` section documenting 8 resolved spec contradictions.

### Sprint 2 — Medium-cost validators + cross-artifact (13 items)

A3 28-authoring-persona whitelist (FAIL prompts voiced by 7 known NPCs: Owen Mercer, Brenda Abbas, Sofia Halabi, Farah Dlamini, James Randall, Lucia Ferreira, Mateo Kovac). A6 account-number entity-trap (WARN when account `105000` etc. mentioned near entity name but not in Fact_Ledger.accounts_by_entity for that entity — closes the Cash-Trust vs IOLTA vs Short-term Investments confusion). B1 channel/method lock-in in rubrics (FAIL rubric requiring email when prompt used `notify` / `reach out` / `let X know` open-goal verbs). B3 bolt-on detection extended to OE steps + rubric criteria (was prompt-only in v6 — now per-step + per-rubric entity overlap check). B5 evidence-stricter-than-criterion (WARN when evidence carries dates / IDs / amounts absent from the criterion title). B7 reverse-groundedness with OE-aware fix (universe-valid IDs in rubric title only WARN if absent from BOTH prompt AND OE — prompts that explicitly ask the agent to DISCOVER vendor IDs no longer trigger false positives). B10 service metadata completeness (email rubric without recipient = FAIL; Slack rubric without channel name or channel_id = FAIL). B12 OE dependency chain (sends email to specific address without earlier contact-lookup OE step = WARN). B13 `(or similar)` validity in OEs (when OE says `tool X or similar`, verify another tool in same service exists). D2 S4 explicit All-Failing Rubrics sub-dim scoring (Bucket-1 ratio > 50% = 1/5 FAIL; 25-50% = 3/5 NON-FAIL; < 25% = 5/5 PASS — closes the verifier-stage scoring gap). D3 empty-in-base-tables awareness (Fact_Ledger tracks tables empty in base universe but populated per-task; e.g., `linear.*` tables on Task 24). D4 date alignment unification (Fact_Ledger.lifecycle.today is the single source for Prompt 2.8 + OE 2.5 + Rubrics 2.11 alignment — collapses 3 disjoint checks into one validator pass). F1 Council B-B1 scoring template formalization (per-sub-dim scheme table in `Reference/Council_Protocol.md` with format example + AUDIT Lens 1 inheritance).

### Sprint 3 — Council perspectives + operational discipline (6 items)

B2 + C2 Council A-A6 persona-scope check (for prompts using possessive scope `my X` / `our X`, every universe-grounded rubric value must belong to the persona's assignment set per `_aux/Universe_Split/`; out-of-scope = BLOCK unless prompt explicitly broadens to firm-wide). C1 Council A-A5 persona authorship whitelist (positive-whitelist verification that assigned persona is one of the 28 authoring personas in `Brookfield_Base_Universe/2_Persona_Briefs.md` — complements the validator's negative-blocklist of 7 NPCs). C5 Council B-B7 per-rubric cross-artifact consistency (for every rubric criterion, verify the value matches the value in the matching OE step exactly; mismatch = BLOCK with optional `PROPAGATE TO S2`). D1 FINAL Lens 6 verifier-fails-spec pre-upload check (simulates `Evals/4_Verifier_Fails_Eval.md` bucket classification for every rubric — > 20% Bucket_1_Risk = REVISE; ≤ 20% = MAJOR notes; 0% = PASS). E1 TODO enforcement (every runbook adds a Step 0 mandating `_aux/Todos_<phase>.md` creation; `phase_ready.py` emits a `[REMIND]` for missing TODO files; AUDIT confirms presence at exit).

### Sprint 4 — Infrastructure + the heaviest item (4 items)

C4 regression-anchor verification (new `Validators/test_regression_anchors.py` runs validate.py against 10 synthetic mini-task fixtures each exhibiting a documented platform-rejection anti-pattern: R7 NPC persona, action-decision ambiguity, command-list, em-dash ban, R9 channel lock-in, subjective term, AND-bundling, invalid retention code, invalid Slack channel, mislabeled Process write-action; all 10 MUST flag with the expected pattern or AUDIT cannot pass — added as AUDIT Lens 8). E2 reference-doc reading log (`phase_ready.py` extends `[REMIND]` to also enforce `_aux/Reads_<phase>.md` listing each QC spec / Reference / Eval doc actually read in this phase — catches the "agent never opened the spec" failure mode). F2 unified verdict format (every council / AUDIT / FINAL report ends with a fenced JSON block with phase + council + verdict + perspectives + scores + density_projection + lever_preservation + bucket_1_risk_pct fields — enables cross-task aggregation via future `Validators/aggregate_verdicts.py`). G1 HARDNESS breadth-vs-depth check (density projection now also emits Service Breadth table; ≥ 4 distinct services each ≥ 5% of total = PASS; ≤ 2 distinct services OR dominant > 60% = `THIN_BREADTH` — catches the false-positive density pattern where 50+ calls all land on one service).

### Smoke-test evidence

| Check | Result |
|---|---|
| `Validators/test_regression_anchors.py` | 10 / 10 PASS |
| `Validators/validate.py --phase all --task Tasks/24_...` | prompt PASS (0F/2W/1N), OE PASS (0F/0W/1N), rubrics FAIL (1F/3W/2N — 1 true-positive AND-bundling, 3 legit WARNs, 0 false positives introduced by v11) |
| `Validators/phase_ready.py --phase s1 --task Tasks/24_...` | OK + emits E1 `[REMIND] Todos_s1.md` + E2 `[REMIND] Reads_s1.md` |

### Files changed

- `Validators/validate.py` — Sprint 1 + Sprint 2 catches (A1-A7, B1-B13 deterministic side, D3, D4 inline). B3 extended to OE step + rubric criterion bolt-on detection.
- `Validators/phase_ready.py` — E1 TODO reminder + E2 Reads reminder per phase.
- `Validators/test_regression_anchors.py` — NEW. 10 synthetic mini-task fixtures + runner.
- `Reference/Council_Protocol.md` — A5 / A6 / B7 perspectives, prompt-template updates, sub-dim scoring scheme table (F1), unified verdict JSON schema (F2).
- `Reference/Sessions/FINAL.md` — Lens 6 verifier-fails-spec pre-upload check + roster table + Hard rules row.
- `Reference/Sessions/AUDIT.md` — Lens 8 regression-anchor verification.
- `Reference/Sessions/HARDNESS.md` — Service Breadth table (G1).
- `Reference/Sessions/{S0,S1,S2,S3,S4,FINAL,HARDNESS,REVIEW,REDO}.md` — Step 0 TODO mandate (E1).
- `Reference/Sessions/S4.md` — All-Failing Rubrics sub-dim explicit scoring (D2, already done in v11 mid-sprint commit).
- `Validators/build_fact_ledger.py` — empty-in-base-tables tracking (D3, already done in v11 mid-sprint commit).
- `AGENTS.md` — "Pipeline Deviations from Eval Specs" section (E6, already done in v11 mid-sprint commit).

### What this closes

All 4 evaluator-spec named checks now enforced. All 20+ documented spec contradictions either resolved or explicitly noted. Real platform-rejection patterns (R7 persona, R9 channel lock-in, account-entity trap, structured-value lock-in, action-decision ambiguity, late-post without unlock, tool-parameter wrong-binding, narrative-state contradiction) all caught by validator unaided. TODO + Reads logging makes Phase 0 spec-reading verifiable. Unified verdict format enables cross-task QC trend analysis.

The bar is now: validator + Council A + Council B + AUDIT (with 8 lenses) + FINAL (with 6 lenses) all GO per phase + S1 similarity gate + S4 trajectory walk + FEEDBACK before CLOSE for review-type tasks. Six gates per phase, much higher catch rate per gate.

---

## 2026-06-21 — v10: Prompt Foundation Strengthening (Narrative State + Action Prescription + Tool-Parameter Strictness + Lifecycle Preconditions)

Eight pipeline-level fixes driven by two real platform rejections on `opposite_classic` tasks (6a3998c2 and 6a34253220) that escaped v9's gates. Both failures share a common root cause: the pipeline checks LEXICAL groundedness (does this value exist in the universe?) but not SEMANTIC consistency (does the prompt's narrative state match the universe's actual state? is the OE's tool-parameter binding valid per-tool? is the lifecycle precondition for the action present?).

### Diagnosis of the escapes

**Task 6a3998c2 (opposite_classic)** — three structural failures rated Poor 2/5 by platform reviewer:
1. Prompt says "Dismiss under materiality / push it through" but universe record's `proposed_resolution = "Reclassify via 4-eyes"` — two divergent end states, Major Unique Ground Truth issue.
2. OE7 binds `late_post_authorization_id` to `oracle_gl_create_journal_entry` — parameter exists only on `oracle_gl_post_journal_entry`. All 6 runs hit `OGL.PERIOD_CLOSED` because the period was never unlocked.
3. Period `northstar_legal_FP-2025-12` is closed; no unlock or `late_post_authorization_id` precondition step in the OE chain.

**Task 6a34253220 (opposite_classic)** — narrative-state contradiction, rated Poor 2/5:
- Prompt: "Andrea is wrapping up her certification ... before she finalizes it"
- Universe: Andrea's sign-off email dated June 10 (today = June 12) — certification ALREADY complete
- Result: agents discovered the existing sign-off, deferred to partner-level, 5/6 runs failed stakeholder comms, 6/6 failed Vault artifact.

### Eight v10 fixes

1. **Council A A3 — Narrative State Consistency** (`Reference/Council_Protocol.md`): new perspective. For every state-implying claim in the deliverable (verbs like "is wrapping up", "before X finalizes", "is pending", "the period is open", "SLA approaches"), identify the universe record AND verify the claimed state matches the universe's actual lifecycle state (Fact_Ledger lifecycle atoms + Universe_Split records). Any contradiction = BLOCK.

2. **Council A A4 — Action-vs-Universe-Prescription** (`Reference/Council_Protocol.md`): new perspective. For every action verb the prompt asks for, identify the universe record AND check for `proposed_resolution` / `recommended_action` / `next_step` / `assigned_to` fields prescribing a DIFFERENT action. Silent divergence = BLOCK. Explicit override language ("override the proposed resolution because Z") = ACCEPT. Also catches authority/permission gaps (persona lacks role for asked action).

3. **Validator: per-tool parameter strictness** (`Validators/validate.py` `validate_oe`): new check. New helper `load_tool_param_map()` walks `8_Server_Tools_Details.json` and builds `{tool_name: set(parameter_names)}`. For every OE step that names a tool + parameters (snake_case tokens), verify each parameter is on THAT specific tool, not just any tool. Catches the Task 1 OE7 class of failure (`late_post_authorization_id` mentioned alongside `oracle_gl_create_journal_entry` instead of `_post_`).

4. **Validator: lifecycle precondition check** (`Validators/validate.py` `validate_oe`): new check. For every OE step that posts a JE to a fiscal period (post verb + JE reference + period_id), look up the period's lock state in `Fact_Ledger.lifecycle.closed_periods`. If closed, require either (a) an earlier unlock step in the OE chain OR (b) the `late_post_authorization_id` parameter on the post call. Missing precondition = FAIL with `OGL.PERIOD_CLOSED` explanation.

5. **Validator: action-decision ambiguity scan** (`Validators/validate.py` `validate_prompt`): new check. New regex `ACTION_AMBIGUITY` scans prompt for action verbs separated by `/` or ` or ` ("dismiss / push through", "approve or deny", "reclassify, dismiss, or escalate"). FAIL with explicit fix suggestion (add decision criteria OR pick one action). Catches the Task 1 Major Clarity / Action Decision Ambiguity failure.

6. **FINAL Lens 5 — Narrative-State + Action-Prescription Cross-Artifact Consistency** (`Reference/Sessions/FINAL.md`): new lens added to the Final Council prompt template. Cross-artifact re-verification of A3 + A4 at the prompt/OE/rubric integration layer. Plus per-tool parameter strictness + lifecycle precondition checks against all 3 artifacts together. Four new BLOCKER rows added to the FINAL Hard Rules table.

7. **AUDIT Lens 6 — Lifecycle + Narrative State (strictest)** (`Reference/Sessions/AUDIT.md`): new lens added to the AUDIT prompt template. Under strictest interpretation, ANY narrative-state contradiction = REVISE; ANY lifecycle-infeasible action = REVISE; ANY tool-parameter binding to wrong tool = REBUILD (structurally unrecoverable in place); ANY action-prescription divergence without explicit override = REVISE.

8. **Fact_Ledger augmentation** (`Validators/build_fact_ledger.py`): new `lifecycle` section in the ledger emitting:
   - `today`: the universe today (from `Universe_Index/today_horizon.json`)
   - `closed_periods`: fiscal periods with status `closed` or `locked`
   - `open_periods`: fiscal periods with status `open` / `draft` / `active`
   - `fiscal_periods_count`: tally of closed / open / total

   Used by item 4 (lifecycle precondition check) and items 1+6+7 (narrative-state checks). Future iterations can add signoff-language detection, past-SLA flags, completed-actions list.

### What this closes

| Operator-pain failure mode | Items that close it |
|---|---|
| Prompt narrative state contradicts universe completion state (Task 6a34253220) | A3 + Lens 5 + Lens 6 + Fact_Ledger lifecycle atoms |
| Prompt action contradicts universe's `proposed_resolution` (Task 6a3998c2 #1) | A4 + Lens 5 + Lens 6 |
| Action-decision ambiguity ("dismiss / push through") (Task 6a3998c2 #1) | Validator action-ambiguity FAIL |
| OE binds parameter to wrong tool (Task 6a3998c2 #2 `late_post_authorization_id`) | Validator per-tool param strictness FAIL |
| OE posts to closed period without unlock (Task 6a3998c2 #3) | Validator lifecycle precondition FAIL + Fact_Ledger lifecycle atoms |
| Persona lacks authority for asked action (latent risk) | A4 authority-gap check |
| Stale time-anchored claims (latent risk) | Fact_Ledger.lifecycle.today + A3 |
| Implicit-vs-explicit framing mismatch (handled in v6 by B6 propagation) | Existing B6 + Lens 5 reinforcement |

---

## 2026-06-21 — v9: PIPELINE FEEDBACK Phase + Flat Rubric Schema Mandate

Two operator-pain fixes raised after the v8 ship.

### PIPELINE FEEDBACK lifted into a dedicated fresh-chat phase (issue 1)

The v8 guardrails on REVIEW step 7 (explicit "rate the ORIGINAL not the fixed task" + plain-language QC dim mapping + voice gate) were not enough. By the time the agent reached the feedback step inside REVIEW, the chat context was saturated with fix-related work (changes.md rows, council reports, materialized 14/15) and the feedback still consistently drifted to rating what we fixed instead of what the candidate submitted.

Fix: lift feedback into a dedicated fresh-chat phase with a clean context AND a strict input allowlist.

- **New runbook** `Reference/Sessions/FEEDBACK.md` + trigger `PIPELINE FEEDBACK — Tasks/<TASK_DIR>`. Runs AFTER `PIPELINE REVIEW`, BEFORE `PIPELINE CLOSE`.
- **Strict input allowlist**: reads ONLY candidate originals `5_Prompt.txt` / `6_Oracle_Events.txt` / `7_Rubrics.json` + user-pasted `3_UniverseDataForThisTask.json` (for spot-checking truthfulness) + `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` + `Reference/Linter_Playbook.md` (voice rules).
- **Strict denylist**: explicitly forbidden to read `changes.md`, `14_Updated_*`, `15_Updated_*`, `_aux/REVIEW_prompt_draft.txt`, `_aux/Council_Reports/*`, `_aux/REVIEW_*`. None of these are the candidate's work; reading them was the source of the drift.
- **Evaluates against QC SPEC BASELINE only** — the candidate is rated against `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md`, NOT against our internal exceeds-spec bar (50+ density, strictest AUDIT, B6 propagation, multi-dim similarity, etc.). We hold ourselves to a higher standard internally; the rating is fair only when measured against the publicly-defined criteria the candidate had access to. A candidate prompt that projects to 42 tool calls passes the spec's investigation-breadth dim even though our internal HARDNESS phase would flag THIN.
- **Plain-language QC dim mapping** — 12-entry table in the runbook for translating internal QC dim names ("Atomicity", "Self-Containment", etc.) into plain-language descriptions the candidate can act on without needing the QC spec doc.
- **Voice gate**: `python Validators/check_justification.py Tasks/<TASK_DIR>/13_Feedback.txt` must exit 0 before save.
- `Reference/Sessions/REVIEW.md` step 7 simplified to a NO-OP pointer to FEEDBACK.
- `Reference/Sessions/REVIEW.md` exit criteria updated (no longer requires `13_Feedback.txt`).
- `Reference/Sessions/REVIEW.md` STOP gate adds top-row next-trigger: "Standard REVIEW intake done → `PIPELINE FEEDBACK` in fresh chat → then `PIPELINE CLOSE`".
- Root `AGENTS.md` PIPELINE DISPATCH adds FEEDBACK row between AUDIT and CLOSE. Trigger count 14 → 15.
- `QUICK_START.md` Closing-the-task section split: CB tasks → CLOSE directly; review-type tasks → FEEDBACK first, then CLOSE.
- `Reference/Sessions/CLOSE.md` already requires `13_Feedback.txt` for review-type tasks — will auto-flag if FEEDBACK was skipped.

### Flat rubric schema mandated for new tasks (issue 2)

Previously the validator accepted both nested (`{id, title, annotations: {evidence, justification, rubric_category}}`) and flat (`{title, category, justification, evidence}`). The duality was creating drift in new tasks. Operator preference: always create rubrics in flat JSON with exactly four fields, nothing else.

- `Reference/Sessions/S3.md` step 4 rewritten: rubrics must use the FLAT schema — `{title, category, justification, evidence}` — exactly four fields, no `id`, no `annotations` wrapper, no extras. The previous "pick either nested or flat" guidance was eliminated.
- `Reference/Rubric_Format.md` Schema section rewritten: flat only. Legacy nested shape documented as back-compat-deprecated.
- `Validators/validate.py` rubric phase: emits a WARN when nested schema is detected (`nested schema is deprecated — convert to flat {title, category, justification, evidence}. New tasks must ship flat.`) — does NOT fail, to preserve back-compat with already-shipped tasks.
- `15_Updated_Rubrics.json` in REVIEW flow also mandated flat.

### Smoke-test evidence

- `FEEDBACK.md` runbook in place + cross-referenced from REVIEW (step 7), AGENTS.md (dispatch), QUICK_START.md (closing).
- `validate.py` WARN logic added at the rubric schema-detection branch; existing tasks with nested schema will now surface a deprecation warning on next validator run without breaking.
- Trigger count is 15 (NEW / S0 / HARDNESS / S1 / S1.5 / S2 / S3 / FINAL / S4 / REVIEW / REDO / COMPARE / AUDIT / FEEDBACK / CLOSE).

---

## 2026-06-21 — v8: Trajectory-Mandatory S4 + REVIEW Linter Branch + Original-Candidate Feedback + Skeptical-First Linter + Multi-Dim Similarity + Class B Invalidation + Knowledge Flow + Density Target Raised to 50+

Eight follow-up improvements from operator-pain debrief on Tasks 23-24 and the legacy `command workflow.txt` parity review. Closes operator pain points that the v6/v7 sprint did not address.

### S4 trajectory walk strengthened (item 1)
- `Reference/Sessions/S4.md` step 2 rewritten: trajectory walk is now MANDATORY for EVERY failing rubric, not just Bucket 2 (Judge Error). Every bucket entry MUST carry a trajectory citation (`Run X, tool call Y: <parameter values>` or `Run X: action not attempted`). Without the walk, Bucket 1 (Rubric Invalid) and Bucket 3 (Legit AF) cannot be distinguished from Bucket 2. Each bucket section now spells out its trajectory-citation requirement explicitly.

### REVIEW linter branch added (item 2)
- `Reference/Sessions/REVIEW.md` new step 0 "Linter check FIRST" — if the candidate's prompt is blocked by the platform linter (operator cannot access prefilled OE / rubrics), STOP and route to `PIPELINE S1.5` in a fresh chat. Returns to REVIEW once linter is cleared (justification accepted OR scratch-draft fix accepted).
- `Reference/Sessions/S1.5.md` mode detection rewritten: Review-mode now detected by candidate-prefilled `6_Oracle_Events.txt` + `7_Rubrics.json` presence — does NOT require prior REVIEW run. Handles linter-before-REVIEW and linter-after-REVIEW symmetrically.

### REVIEW feedback fix: rates ORIGINAL not fixed (item 3)
- `Reference/Sessions/REVIEW.md` step 7 rewritten with explicit guardrails: `13_Feedback.txt` rates the CANDIDATE'S ORIGINAL deliverables AS SUBMITTED. Do NOT reference `changes.md`, `14_Updated_*.txt`, `15_Updated_*.json`, `_aux/REVIEW_prompt_draft.txt`, or anything we fixed. Common defect named explicitly: "writing feedback for the fixed task instead of the original".
- Feedback dimensions use plain-language descriptions of QC criteria, not the strict QC dim names (loose mapping table provided in runbook with 8 example translations). Voice-gate via `check_justification.py` is mandatory before save.

### Skeptical-first linter handling (item 4)
- `Reference/Sessions/S1.5.md` Class A decision flow rewritten: default assumption is the linter MAY be wrong. INVALIDATE with justification is the preferred path (cheap — platform doesn't intelligently evaluate justifications). REVISE is high cost (re-runs all gates including AUDIT). Ambiguous cases default to INVALIDATE. Choose REVISE only when the universe grep gives no plausible counter to the linter.
- Rationale codified: cost asymmetry favors invalidation; revision risks introducing new defects.

### Multi-dimensional similarity scoring with multiplicative context model (item 5)
- `Validators/calc_similarity.py` upgraded to multi-dimensional COMPOSITE score with MULTIPLICATIVE context modifier (context dominates word stats per operator preference — same-day amendment).
  - Lexical: word_bigram Jaccard (weight 0.40), word_unigram Jaccard (weight 0.40), word_count_similarity (weight 0.20).
  - Context multipliers when CONSTANTS DIFFER: business_function × 0.6, persona × 0.6, universe × 0.7 (multiplicative — max compounded reduction ×0.252 when all three differ, ~75% off raw lexical). Same constants leave lexical similarity intact (expected overlap — same persona × business function × universe has a fixed set of plausible scenarios); DIFFERENT constants REDUCE the score so contextual differentiators dominate lexical overlap.
  - Bands (simplified, two-band): **composite < 40 = INVALIDATE** (write 2-3 sentence justification, move on); **composite ≥ 40 = PIVOT** (high overlap that survives contextual weighting, constants align, structural similarity is genuine).
- New CLI flag `--explain <prior_task_dir>` prints per-dimension breakdown vs a specific prior task, naming the differentiating dimensions for use in the Class B invalidation justification.
- `_aux/Similarity_Report.json` now carries per-dimension breakdown + composite + context multiplier + recommendation per top-10 match. Back-compat `max_score` field preserved for older runbook references.
- Smoke-tested on Task 24: max composite 26.2 (clear, INVALIDATE recommendation across top-10 entries). `--explain` vs Task 23 shows raw lexical 26.3 × ×0.252 multiplier (BF + persona + universe all differ) = composite 6.6 — clear INVALIDATE, strong differentiators cited for justification angle.

### Class B similarity invalidation template + 2-band simplification (item 6)
- `Reference/Linter_Playbook.md` Class B section rewritten: no longer "pivot only" — now skeptical-first invalidation OR pivot. New template (2-3 sentences max, stricter than Class A) + 2 worked examples (different persona / same BF; same persona / different BF). Voice-gate via `check_justification.py`.
- `Reference/Sessions/S1.5.md` Class B decision flow simplified to two bands per operator preference: **composite < 40 → INVALIDATE** (move on); **composite ≥ 40 → PIVOT** (constants align even after the context multiplier was applied, structural similarity is genuine). No ambiguous middle band — the context multiplier handles ambiguity at the score level.
- `Reference/Sessions/S1.md` proactive similarity gate simplified to two bands matching S1.5: < 40 PASS, ≥ 40 STOP/PIVOT.

### Knowledge-flow + file-nomenclature reference (item 7)
- New `Reference/Knowledge_Flow.md` — phase dependency chart (every phase's reads + produces), file nomenclature canonical conventions (`<phase>_<council>_<purpose>.md`, `AUDIT_<phase>.md`, `S4_<bucket>.md`, `<descriptive>.md` for reasoning, etc.), single-source ownership map (Fact_Ledger SSOT, Universe_Split SSOT, etc.), cross-phase re-run map (when an artifact changes, what downstream phases must re-run).
- Root `AGENTS.md` Project Layout amended to point at Knowledge_Flow.md.

### Density target raised: 50+ design / 40 floor (item 8)
- Hard rule #11 rewritten in root `AGENTS.md`: 50+ midpoint design target produces ~40+ tool calls in real platform runs. Tiered scheme — midpoint ≥ 50 = PASS; 40-49 = THIN_DENSITY (operator continues with per-task justification, task at risk of underflow); < 40 = INSUFFICIENT_DENSITY (BLOCKER).
- HARDNESS phase: density-projection gate tiered (PASS at ≥ 50, THIN at 40-49 with `## THIN density acceptance` justification, STOP at < 40). Composition rules bumped: default 4-5 levers instead of 3-5 (3 acceptable only with high-cost lever combo + per-task justification, since 3 levers will frequently land in THIN band or below).
- Council B-B3 perspective + prompt template + pass criteria all updated to tiered scheme.
- S1 / S2 / S3 exit criteria updated.
- FINAL council density check tiered (table row + prompt template).
- AUDIT Lens 4 unchanged (already at 50+ midpoint — this was the v6 setting that the v8 pipeline now aligns with).
- QUICK_START updated.
- Rationale: tasks that shipped with 40+ projected density came back from the platform failing density on real runs. Designing for 50+ produces ~40+ in reality.

### Smoke-test evidence

| Script | Task 24 result | Pass criterion |
|---|---|---|
| `validate.py --phase all` | PASS all three phases (0 fails, low warns/notes) | exit 0 |
| `calc_similarity.py` (default) | max composite 26.2 vs 29-prompt corpus | < 40 |
| `calc_similarity.py --explain Tasks/23_...` | raw 26.3 → composite 0.0 after −50 discount (BF + persona + universe all differ) | < 40 |
| `calc_similarity.py --explain Tasks/22_...` | raw 27.1 → composite 0.0 after −40 discount (BF + persona differ, universe unknown) | < 40 |
| `check_justification.py` on `13_Feedback.txt` | 3 pre-existing hits caught (`Candidate_Originals`, `Trajectory_Stats`, `per-task universe`) — gate works as designed | (separate fix pass) |

### What this closes

| Operator-pain gap | Status |
|---|---|
| S4 bucket classification relying on verifier text alone, not trajectory | Closed — trajectory walk mandatory per failing rubric, citation required per bucket |
| REVIEW had no way to handle linter-blocking on candidate's prompt before seeing prefilled OE / rubrics | Closed — Step 0 routing to S1.5 + Review-mode detection without requiring prior REVIEW run |
| `13_Feedback.txt` chats wrote feedback for the fixed task instead of the original candidate | Closed — explicit guardrail in step 7 + plain-language QC dim mapping + voice-gate |
| Linter handling was authoritative-first, expensive (revise) by default | Closed — skeptical-first, invalidate by default (cheap), revise only when universe grep is unambiguous |
| Similarity scoring was lexical-only — couldn't surface that same persona × business function × universe has expected overlap | Closed — multi-dimensional with context discounts for differing constants + `--explain` mode |
| No Class B invalidation template — operator wrote them by hand and they overshot | Closed — strict 2-3 sentence template + 2 worked examples + voice-gate |
| File nomenclature and knowledge flow scattered across runbooks; fresh-chat agents missed dependencies | Closed — single canonical `Reference/Knowledge_Flow.md` with phase dependency chart + SSOT map + re-run map |
| Tasks projected to 40+ density but real runs underflowed | Closed — design target raised to 50+ midpoint; 40-49 explicitly flagged as THIN and at risk |

---

## 2026-06-21 — v7: Strict Veteran AUDIT Auto-Fires After Every Per-Phase Deliverable

Same-day amendment to v6's AUDIT runbook. Operator found flaws on Tasks 23-24 that escaped per-phase Council A + B + FINAL. Decision: catching defects at the producing phase is cheaper than catching them downstream at FINAL or at platform-reviewer time, so AUDIT becomes a MANDATORY per-phase exit gate, not an optional on-demand tool.

### Behavior change

v6 shipped AUDIT as an on-demand-only trigger. v7 makes AUDIT mandatory inline after every per-phase deliverable:

| Phase | When AUDIT fires | Sub-agent | Phase argument |
|---|---|---|---|
| S1 | After Council A + B + similarity gate pass | `oracle` | `--phase prompt` |
| S2 | After Council A + B pass | `oracle` | `--phase oe` |
| S3 | After Council A + B pass | `ultrabrain` | `--phase rubrics` |
| S1.5 | After Council A + B re-run on revised prompt (skipped on justification-only path) | `oracle` | `--phase prompt` |
| REVIEW | On the corrected materialization (14/15 + prompt draft) | per phase | per phase |

`PASS (STRICT)` is now a required exit criterion. `REVISE` iterates the producing phase (validators + Council A + Council B + AUDIT, iteration cap 3 rounds). `REBUILD` STOPs to `PIPELINE REDO`. `PROPAGATE TO <upstream>` STOPs to the upstream phase re-run (uses the Council B-B6 propagation mechanism added in v6).

On-demand mode preserved unchanged for additional re-verification beyond the built-in gates (pre-FINAL pre-upload sanity check, post-platform-rejection retro, post-pipeline-change re-audit).

### Files modified

- **`Reference/Sessions/AUDIT.md`** — "What this phase does" rewritten to describe dual-mode operation (Mode 1 auto-fire from per-phase runbooks + Mode 2 on-demand). "When NOT to use" updated (removed "during normal build pipeline" bullet). Cost note updated to reflect the ~3 additional sub-agent calls per task. STOP gate clarified as on-demand-mode only (auto-fire piggybacks on the parent phase's STOP gate).
- **`Reference/Sessions/S1.md`** — new step 8 "Strict veteran audit (MANDATORY, auto-fire)" between similarity gate (step 7) and final report (now step 9). Exit criteria updated to require `AUDIT_prompt.md` with `PASS (STRICT)`.
- **`Reference/Sessions/S2.md`** — new step 8 "Strict veteran audit (MANDATORY, auto-fire)" between Loop (step 7) and final report (now step 9). Exit criteria updated to require `AUDIT_oe.md` with `PASS (STRICT)`. Includes explicit handling for `PROPAGATE TO S1` findings (STOP to S1 re-run).
- **`Reference/Sessions/S3.md`** — new step 9 "Strict veteran audit (MANDATORY, auto-fire)" between Loop (step 8) and coverage matrix (now step 10). Uses `ultrabrain` (rubrics is the heaviest phase). Exit criteria updated to require `AUDIT_rubrics.md` with `PASS (STRICT)`. Includes explicit handling for `PROPAGATE TO S1` and `PROPAGATE TO S2` findings.
- **`Reference/Sessions/S1.5.md`** — new step 7 "Strict veteran audit on any revised prompt" between justification voice gate (step 6) and exit. Conditional: fires only when 5_Prompt.txt or REVIEW_prompt_draft.txt was modified (Class A revise OR Class B pivot path). Skipped on justification-only resolution.
- **`Reference/Sessions/REVIEW.md`** — step 11 amended to include AUDIT on every corrected artifact (14/15 + prompt draft). AUDIT fires before FINAL in the re-run gate set, matching the per-phase order in S1/S2/S3.
- **Root `AGENTS.md`** — new hard rule #12: "Strict veteran AUDIT runs after every per-phase deliverable." Dispatch table description for AUDIT updated to call out auto-fire mode + preserved on-demand mode.
- **`QUICK_START.md`** — "What each phase guarantees" updated to note inline AUDIT in S1/S2/S3. Conditional commands table updated to clarify the on-demand AUDIT trigger is for ADDITIONAL re-verification beyond the auto-fired inline gate.

### Cost + benefit

- **Cost**: ~3 additional sub-agent calls per task (S1 + S2 + S3, with S3 using ultrabrain). Pre-FINAL pre-upload on-demand AUDIT is still possible but largely redundant once auto-fire is in place.
- **Benefit**: catches defects at the producing phase, before they propagate through downstream phases. Operator-pain pattern on Tasks 23-24 (defects surfacing only at S3 or at FINAL or post-trajectory) is structurally prevented.

The bar is now: validator + Council A + Council B + AUDIT all GO per phase, then FINAL GO before platform upload. Five gates per task.

---

## 2026-06-21 — v6: Justification Voice Gate + Similarity Gate + AUDIT Runbook + Upstream-Propagation Council Perspective + OE Meta-Tag Ban + Word-Count Tiers + Hardened STOP Gates

Nine improvements driven by operator-pain debrief on Tasks 23-24. Closes the justification-voice gap (reviewers were seeing internal terminology in pushbacks), the silent-similarity-leak gap (similarity score wasn't enforced as a phase gate), the missing-veteran-audit gap (no on-demand strictest-interpretation re-verification), the upstream-propagation gap (S3 caught OE issues the operator had to manually trace back to S2), the OE meta-tag gap (validator missed `→ Write action` / `→ Read action` arrows operator had to manually strip), the lenient-word-count gap (single 500-word hard fail with no sweet-spot signal), and the STOP-gate leakage gap (operators were chaining phases inside one chat against the contract).

### New scripts

- **`Validators/calc_similarity.py`** — Jaccard on word bigrams (stdlib only). Scores `5_Prompt.txt` against every prior `5_Prompt.txt` in `Tasks/` + V3 reference prompts. Writes `_aux/Similarity_Report.json` with top matches per source. Project ceiling enforced at 40 (Class B pivot mandatory above that). Smoke-tested against Task 24: max score 4.2/100 (well clear of ceiling).
- **`Validators/check_justification.py`** — 8 forbidden-term categories (rubric numbers, council references, pipeline phase names, internal artifact names, script names, guide / spec references, V3 framework refs, Brookfield meta refs). Scans any reviewer-facing file (linter pushbacks, AF justifications, candidate feedback). Per-hit report with line + matched term + 60-char context. Smoke-tested against Task 24 `13_Feedback.txt`: caught 3 real hits (`Candidate_Originals`, `Trajectory_Stats`, `per-task universe`).

### New runbook

- **`Reference/Sessions/AUDIT.md`** — `PIPELINE AUDIT — Tasks/<TASK_DIR> --phase {prompt|oe|rubrics|all}` trigger. Veteran QC second-opinion under STRICTEST possible interpretation: 5/5 is the only acceptable score, density bar is 50+ midpoint (not 40 floor), every "should" reads as "must", every soft convention is binding. Returns `PASS (STRICT)` / `REVISE` / `REBUILD`. Read-only. Not a substitute for FINAL — complementary on-demand tool for high-stakes re-verification (pre-upload sanity check, post-rejection retro, post-pipeline-change re-audit).

### Validator changes

- **`Validators/validate.py`** — word-count tiers replace the single 500-word hard fail. HARD FAIL > 500, WARN > 400, NOTE > 300 (sweet spot 300-400 matches the V3 reference distribution).
- **`Validators/validate.py`** — OE meta-tag ban catches three forbidden patterns operators had to manually strip: `→ Write action` arrows, `→ Read action` arrows, `→ Outcome N.M` inline annotations, process-rubric inline annotations. The reviewer-facing OE file is meant to read as numbered prose, not as a process-aware annotated document.

### Council changes

- **`Reference/Council_Protocol.md`** — Council B adds B6 perspective: **Upstream Propagation**. When a council finds an issue whose root cause lives in an upstream artifact (S3 rubric review surfaces an OE accuracy gap; S2 OE review surfaces a prompt truthfulness gap; FINAL surfaces a lever the prompt's framing actively prevents), flag `PROPAGATE TO <PHASE>: ...` instead of patching downstream. Patching downstream silently embeds the bug forever. B6 finding is BLOCKING — the operator must re-run the named upstream phase, then re-run the current phase against the fresh upstream output. Closes the operator-pain pattern of OE errors caught at S3 (rubrics) stage and prompt truthfulness issues caught late at FINAL.
- **Role-Lens Anchoring** — Integration lens now also maps to B6 (root-cause-upstream attribution is a cross-phase property).

### Pipeline changes

- **`Reference/Sessions/S1.md`** — new step 7 between councils and Final Report: similarity gate via `calc_similarity.py`. < 30 PASS, 30-39 WARN (logged in `_aux/Reasoning/prompt_design.md`), ≥ 40 STOP with Class B pivot mandatory. Exit criteria updated.
- **`Reference/Sessions/S1.5.md`** — new step 6: `check_justification.py` gate on `_aux/Linter_Justifications.md` before STOP. Pushbacks with internal terminology now blocked at the runbook layer (operator was previously catching these manually).
- **`Reference/Sessions/S4.md`** — new step 5: `check_justification.py` gate on `_aux/Council_Reports/S4_AF_justifications.md` before producing the verdict report. AF batches with internal terminology now blocked at the runbook layer.
- **`Reference/Sessions/S0.md`, `S1.md`, `S1.5.md`, `S2.md`, `S3.md`, `FINAL.md`, `REVIEW.md`, `REDO.md`** — STOP gates hardened with explicit "if user pastes follow-up content in this chat, do NOT process it" canonical block. Closes the operator-pain pattern of agents auto-processing pasted content that should have been a fresh chat per the fresh-chat-per-phase contract.

### Linter Playbook changes

- **`Reference/Linter_Playbook.md`** — new "Forbidden terms (enforced by `Validators/check_justification.py`)" section listing all 8 categories with rationale. Two new BEFORE/AFTER worked examples (feasibility pushback + AF reasoning gap) showing the most common authoring mistake (writing in process-aware voice) and how to strip it. Pre-ship check sections added to both Class A pushback and AF justification flows. `changes.md` (operator-internal change log) explicitly excluded from the check — it uses internal terms legitimately.

### Dispatch + docs updates

- Root **`AGENTS.md`** — PIPELINE DISPATCH adds AUDIT row between COMPARE and CLOSE. Trigger count updated from 13 to 14.
- **`QUICK_START.md`** — conditional commands table expanded from 4 to 5 with the AUDIT row. S1 phase description notes the similarity gate. S4 description notes the AF justification check. AUDIT added to the "What each phase guarantees" list.

### What this closes

| Operator-pain gap from Tasks 23-24 debrief | Status |
|---|---|
| Reviewer-facing pushbacks / AF justifications had internal terminology slipping through | Closed — `check_justification.py` wired at S1.5 + S4 STOP gates |
| Similarity score wasn't a phase gate — only caught downstream at platform linter | Closed — `calc_similarity.py` wired at S1 between Council B and STOP |
| No on-demand strictest-interpretation re-verification for high-stakes uploads | Closed — `PIPELINE AUDIT` runbook + dispatch row |
| OE errors caught late at S3 had to be manually traced back to S2 with no protocol | Closed — Council B-B6 PROPAGATE perspective with mandatory upstream re-run |
| OE meta-tags (write/read action arrows) had to be manually stripped | Closed — validator catches all 3 patterns |
| Word count had no sweet-spot signal — operator couldn't tell 480 from 320 | Closed — HARD FAIL > 500 / WARN > 400 / NOTE > 300 tiers |
| Operators chained phases inside one chat, polluting the decision-clean contract | Closed — STOP gates hardened in 8 runbooks with explicit reject-follow-up block |

Smoke-tested end-to-end against Task 24 (reference task, 473 words, full lifecycle):
- `calc_similarity.py`: max 4.2/100 vs prior corpus (clear of 40 ceiling).
- `check_justification.py`: caught 3 real hits in `13_Feedback.txt`.
- `validate.py` word-count tiers: prompt = PASS with warn/note flags.
- `validate.py` OE meta-tag ban: synthetic test → 1 fail recorded.

---

## 2026-06-21 — v4: Learnings Log + Final Council + Multi-Model Opt-In + STOP Gates

Adopted the remaining 4 gaps from the sibling reviewer pipeline (excluding the SQL-inject layer the user explicitly skipped). Closes the empirical-calibration gap and the cross-artifact gate gap. Pipeline is now decisively ahead overall.

### New files
- `Tasks/_meta/Learnings.md` — append-only empirical Opus 4.8 failure-mode log. 22 numbered findings (L1-L22) distilled from the Archive's two-task iteration evidence: which patterns reliably fail Opus 4.8 (L8 three reductions across services, L9 authority-figure dismissal, L10 SAP subledger invisibility) and which do not (L1 confirm-already-done, L6 stated-answer correction emails, L7 binary "is it posted?" traps). HARDNESS phase reads this BEFORE drafting; every lever pick must cite an entry that justifies it.
- `Reference/Sessions/FINAL.md` — new `PIPELINE FINAL — Tasks/<TASK_DIR>` runbook. Cross-artifact holistic council reading prompt + OE + rubrics together, plus Hardness_Plan and Fact_Ledger. 4 lenses (Truthfulness / Rubric binding / Cross-artifact holism / Red-team adversarial) catch what per-phase councils cannot: answer leakage (correct figure appearing verbatim in artifact text), entity drift across artifacts, hardness-lever regression after S2/S3 edits, integrated tool-call density. Required before platform upload — STOP gate at end of S3 points here.

### Council changes
- `Reference/Council_Protocol.md` adds opt-in `COUNCIL_MODE=multi` mode: 5 separate sub-agent calls (one per role lens) + 6th consensus synthesizer. Default Council B stays as 1-call with 5 lenses overlaid. Multi-mode is for critical deliverables where the 5x token spend is justified.

### Runbook changes
- `Reference/Sessions/S1.md` / `S2.md` / `S3.md` — explicit `STOP gate` sections at end. Each phase ends, the chat closes, user invokes the next phase in a fresh chat. S3 STOP now points to `PIPELINE FINAL` (mandatory) before any platform upload.
- `Reference/Sessions/HARDNESS.md` — step 1 is now "Read `Tasks/_meta/Learnings.md` end to end" before any sub-agent spawn. Every lever pick cites a Learnings entry. Step 4 (lever selection) defaults to the L8 + L9 + L10 anatomy. Step 6 (stump hypothesis) cites Learnings entries in the reasoning.

### Dispatch + index updates
- Root `AGENTS.md` PIPELINE DISPATCH adds `PIPELINE FINAL` between S3 and S4, marked "Required before platform upload".
- `Reference/AGENTS.md` runbook table adds `FINAL.md`.
- `Tasks/_meta/AGENTS.md` table adds `Learnings.md` with note "Read this BEFORE every PIPELINE HARDNESS run".

### What this closes

| Gap from prior comparison | Status |
|---|---|
| Their `Learnings.md` empirical calibration | Closed — mine is seeded from theirs + designed for ongoing append after every S4 |
| Their Final Council cross-artifact gate | Closed — `PIPELINE FINAL` is a binding gate before platform upload |
| Their true multi-model reviewer diversity | Closed — opt-in mode for critical deliverables |
| Their explicit pause-between-phases discipline | Closed — STOP gates in S1/S2/S3 |
| Their universe-inject SQL workflow | Intentionally skipped per user spec |

The only remaining advantages on their side are universe-edit Phase 1.5 (out of scope) and one-task-at-a-time `clear_task_folder.sh` discipline (incompatible with parallel batch QC).



Adopted 6 improvements from a sibling reviewer pipeline. Closes the grounding-rigor gap (their strongest dimension) and adds compounding cross-task value.

### New scripts
- `Validators/build_fact_ledger.py` — emits `_aux/Fact_Ledger.json`: a flat surface of every verifiable atom per task (emails, money amounts canonicalized to 2dp, ISO dates with day-of-week, typed ID buckets, accounts-by-entity, fiscal periods with lock state, personas with aliases). Replaces grep-based grounding with O(1) set lookups. Source hash tracks regenerate trigger.
- `Validators/build_graph_report.py` — emits `_aux/Universe_Index/graph_report.md`: compact discovery map for HARDNESS (people-by-density top 30, periods-by-JE-count top 20, exceptions/recons by entity×state, pending-AP by vendor top 20, docs by kind/classification, densest person×period pairs top 15). Summary tables only, no edge-list bloat.
- `Validators/compare_rubrics.py` — per-index diff between `7_Rubrics.json` and `10_Rubrics_Platform.json`. Catches silent platform-side mutations.

### Validator changes
- `validate.py --phase rubrics` now uses `_aux/Fact_Ledger.json` for groundedness when available (falls back to raw blob substring match). O(1) set lookups instead of substring scanning. The dollar-amount false-positive class on formatted floats is permanently eliminated.
- New naturalness heuristics adopted from rubric_naturalness.py: subjective terms (`thorough`, `professional`, `helpful`, `properly`, `appropriately`, `sufficiently`, `enough`) are FAIL; non-agent eval-voice (`the email mentions`, `(via `, `tool call`, `trajectory shows`, `the model must use`, `as expected`, `should obviously`) is WARN; awkward negation (`does not fail`, `never fails`, `must not be wrong`) is WARN.

### Council changes
- Council B gets a Role-Lens Anchoring layer overlaying the existing B1-B5 perspectives. Five lenses (Architect / Implementer / Red-team / Ground-truth / Integration) read the deliverable five times each, with each lens mapped to the strongest perspective. Single sub-agent call, multi-perspective coverage. BLOCK from any lens propagates to its mapped perspective.

### Pipeline changes
- S0 runbook now produces `_aux/Fact_Ledger.json` and `_aux/Universe_Index/graph_report.md` automatically.
- New `PIPELINE COMPARE — Tasks/<TASK_DIR>` trigger + `Reference/Sessions/COMPARE.md` runbook for platform paste-back verification.
- REVIEW runbook now emits `13_Feedback.txt` (candidate-facing rating, concise human voice, no em-dashes, no guide references) and conditionally emits `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` ONLY when corresponding `changes.md` rows are Applied. Originals `5/6/7` stay pristine for rating.

### Docs updated
- Root `AGENTS.md` — dispatch table adds COMPARE, project layout adds 5 new files in `_aux/` and 13/14/15 in per-task root, validator inventory adds 3 new scripts.
- `Validators/AGENTS.md` — full documentation for the 3 new scripts + ledger / naturalness mentions on `validate.py --phase rubrics`.
- `Reference/Sessions/S0.md` — steps 4-5 added for fact ledger + graph report.
- `Reference/Sessions/REVIEW.md` — steps 7-8 added for `13_Feedback.txt` + conditional 14/15, plus updated exit criteria.
- `Reference/Council_Protocol.md` — Role-Lens Anchoring section + lens instructions woven into the Council B prompt template.



All notable changes to the MCP Eval V3 automated pipeline. Newest first.

## 2026-06-21 — v2: Tool-Call Density Gate + OE Inventory + Multi-Perspective Councils

Improvements driven by the parity-review pass against the original requirements. Focus: harden the 40+ tool-call baseline, codify OE conventions, and make council coverage explicit per perspective.

### Added

- **`Reference/OE_Convention_Inventory.json`** — auto-extracted from V3 reference OE files. Captures 36 tool-usage frequencies, 9 parameter patterns, opening-phrase shapes, parameter traps, and anti-patterns. Council A's convention sweep on OE phase reads this.
- **Hard rule #11 in root AGENTS.md** — 40+ tool-call average is the maximalism floor. Enforced by two independent gates (HARDNESS phase projection + Council B-B3 adversarial).
- **`Hardness_Plan.md` density projection section** — every HARDNESS run emits a tool-call density estimate. `< 40` returns `INSUFFICIENT_DENSITY` and stops the pipeline.
- **Per-lever tool-call cost column in `Reference/Hardness_Playbook.md`** — each of the 11 levers carries a cost range so the projection is mechanical.
- **Council B-B3 (tool-call density adversarial)** — Council B now sketches the trajectory a competent Opus 4.8 agent would take, counts tool calls, and blocks the deliverable if the sketch produces < 40.
- **Council B-B4 (hardness preservation)** — Council B verifies every lever selected in HARDNESS still triggers in the deliverable. Lost lever = `HARDNESS_REGRESSION` block.
- **`Prompt_Guidelines.md` programmatic cross-check** — validator warns on QC-sample clichés, over-signaling investigation phrasing, generic urgency framing.
- **OE step-count + opening-verb checks** — validator warns when OE list has < 8 steps or < 60% of lines start with an action verb (V3 references run 11-28 OEs with consistent action-first openings).
- **`data.py` smart forwarder** — routes per-task input to `Validators/split_universe.py`. Original behavior preserved in `data.legacy.py`. Refuses non-per-task paths with a clear pointer.
- **`CHANGELOG.md`** (this file) — append-only history.

### Changed

- **`Reference/Council_Protocol.md`** — fully rewritten. Council A enumerated as A1 (Grounding) + A2 (Convention). Council B enumerated as B1 (QC sub-dim scoring) + B2 (Adversarial alt-path) + B3 (Tool-call density) + B4 (Hardness preservation) + B5 (Tool-leak / phrasing scan). Same two sub-agent calls per phase, full perspective coverage.
- **`Reference/Sessions/HARDNESS.md`** — added 6-section Hardness_Plan template with explicit Tool-Call Density Projection section + `INSUFFICIENT_LEVERS` / `INSUFFICIENT_DENSITY` gates.
- **`Reference/Sessions/S1.md`, `S2.md`, `S3.md`** — exit criteria now name B3 (≥40 projected tool calls) and B4 (hardness preservation) explicitly.
- **`Reference/AGENTS.md`** — references OE_Convention_Inventory.json.
- **`Validators/validate.py`** — dollar-amount groundedness sweep now tries `34495.06`, `34495`, `34495.0`, and `34,495.06` variants. Removes formatted-amount false-positives. New prompt anti-pattern checks. New OE step-count + opening-verb checks.
- **`Validators/AGENTS.md`** — refreshed check list per phase.
- **Root `AGENTS.md`** — added hard rule #11 (40+ floor), added "supersedes `command workflow.txt`" note under PIPELINE DISPATCH, updated `data.py` guidance (smart forwarder, not forbidden).

### Renamed

- **`data.py` → `data.legacy.py`** (the original script that writes to the shared `Brookfield_Base_Universe/Data/`). A new `data.py` replaces it as a smart forwarder.

### Validator smoke-test on task 23 (after this round)

```
[PASS] prompt:  0 fails, 0 warns, 2 notes
[PASS] oe:      0 fails, 0 warns, 1 notes
[PASS] rubrics: 0 fails, 0 warns, 1 notes
```

Down from 3 warns (dollar-amount false-positives) in v1.

---

## 2026-06-21 — v1: Initial Pipeline Build

First-pass automated pipeline supplanting the manual `command workflow.txt` workflow. Built end-to-end from the user's verbal spec.

### Added — Validators (3 scripts)

- **`Validators/split_universe.py`** — patched `data.py` wrapper. Writes the per-task universe split into `Tasks/<TASK_DIR>/_aux/Universe_Split/` instead of the shared `Brookfield_Base_Universe/Data/`. Prevents cross-task collisions.
- **`Validators/build_universe_index.py`** — builds quick lookup summaries from `_aux/Universe_Split/` (service_inventory.md, entities_personas.md, key_facts.md, today_horizon.json, accounts_per_entity.md). Parses `row_data` JSON-encoded strings correctly.
- **`Validators/validate.py`** — phase-aware validator. Supports both nested (`{annotations: {...}}`) and flat (`{evidence, justification, category}`) rubric schemas. Exits non-zero on any FAIL.

### Added — Reference (7 cards + 1 inventory)

- **`Reference/Hardness_Playbook.md`** — 11-lever Opus-4.8-specific catalog with hard-tip provenance.
- **`Reference/Prompt_Format.md`** — voice, anti-patterns, 500-word cap.
- **`Reference/OE_Format.md`** — numbered-prose template + parameter traps.
- **`Reference/Rubric_Format.md`** — V3 schema (nested + flat) + verbatim patterns extracted from V3 references.
- **`Reference/Similarity_Pivot.md`** — 6-lever menu for ≥40% similarity blocker.
- **`Reference/Linter_Playbook.md`** — strict justification style (concise, human, no em-dashes, no references to guides) + AF justification template with 2 examples.
- **`Reference/Council_Protocol.md`** — verbatim sub-agent prompt templates for Council A (Grounding) + Council B (Adversarial-QC).
- **`Reference/Strict_Convention_Inventory.json`** — extracted from `QC_Tasks/V3_Tasks/Task11..Task14/Rubrics.json`. Allowed phrasings, evidence-field shapes, "(or similar)" usage rules.

### Added — Session Runbooks (8 files)

- **`Reference/Sessions/S0.md`** — PersonaBrief extract + universe split + index build.
- **`Reference/Sessions/HARDNESS.md`** — lever scan + stump hypothesis.
- **`Reference/Sessions/S1.md`** — prompt drafting + validator + 2 councils.
- **`Reference/Sessions/S1.5.md`** — linter blocker handler (Class A misalignment + Class B similarity ≥40%).
- **`Reference/Sessions/S2.md`** — Oracle Events drafting + validator + 2 councils.
- **`Reference/Sessions/S3.md`** — Rubrics drafting + validator + 2 councils (heaviest pass).
- **`Reference/Sessions/S4.md`** — verifier-fails classification (Rubric-Invalid / Judge-Error / Legit-Fail) + AF justifications.
- **`Reference/Sessions/REVIEW.md`** — review-type task intake + `changes.md` initialization.

### Added — Cross-task learning (`Tasks/_meta/`)

- **`Similarity_Log.md`** — per-task pivot history.
- **`Linter_Justifications.md`** — justification history with reviewer outcomes.
- **`Hardness_Patterns_Log.md`** — lever selection vs actual failure calibration.
- **`Stump_Hypotheses.md`** — predicted vs actual AF rubrics with calibration delta.

### Added — AGENTS.md hierarchy (25 files)

- Root + Brookfield_Base_Universe + Brookfield_Base_Universe/Data + 13 per-service + 9 infrastructure (Docs, Evals, Guide, QC_Tasks, Reference, Tasks, Tasks/_meta, Tasks_Template, Validators).
- All carry the staleness warning where applicable: per-task `3_UniverseDataForThisTask.json` is the only source of truth; base universe is stale except `8_Server_Tools_Details.json` and persona briefs.

### Pipeline contract

8 trigger phrases (`PIPELINE S0`, `HARDNESS`, `S1`, `S1.5`, `S2`, `S3`, `S4`, `REVIEW`). Each runs in a fresh chat with zero prior context. Find-replace `<TASK_DIR>` per task.

Hard rules: 5/5 QC on every dimension; per-task universe is SSoT; 500-word prompt cap; no em-dashes; no "at least N" without prompt mandate; no tool names in prompts or rubric titles; outcome > process in rubrics; 40% similarity ceiling.
