# Reads — FINAL (cross-artifact holistic council)

## QC spec docs
- `Docs/7_QC_Spec_Doc1.json` :: rubric / OE / prompt sub-dim scoring rules re-applied at integration layer; cross-artifact consistency surfaced as a holistic Lens 3 + 5 + 6 check.
- `Docs/8_QC_Spec_Doc2.md` :: rubric scoring narrative cross-checked for Service Metadata Completeness, atomic write-action pairing, evidence-stricter-than-criterion patterns.
- `Docs_moveops/2_Rubrics_V3_Guidelines.md` :: V2.1 framework deltas read; no FINAL-phase sub-dim scoring delta surfaced — rubric-set is all-outcome which keeps V2.1 + V3 identical at the holistic gate.

## Eval specs
- `Evals/1_Prompt_Eval.md` :: Prompt-phase eval re-applied at integration layer (anti-pattern checks + tool-mention sweep + entity / date / persona consistency across the 3 artifacts).
- `Evals/2_Oracle_Events_Eval.md` :: OE-phase eval re-applied (tool-parameter binding accuracy, OE-to-prompt coverage in BOTH directions, lifecycle precondition compliance).
- `Evals/3_Rubrics_Eval.md` :: Rubrics-phase eval re-applied (atomicity, Outcome > Process count, evidence-cites-OE binding, no-tool-name-in-title, service-metadata completeness).
- `Evals/4_Verifier_Fails_Eval.md` :: Lens 6 simulates bucket classification for every rubric — flags Bucket_1_Risk patterns (channel lock-in / evidence-stricter / AND-bundling / subjective terms / write-verb Process / approximately on IDs / per-rubric cross-artifact mismatch).

## Reference cards
- `Reference/Council_Protocol.md` :: 6-lens FINAL council contract + B3 tiered density gate (SSOT) + Lens 5 narrative-state + Lens 6 pre-upload verifier-fails simulation.
- `Reference/Sessions/FINAL.md` :: phase runbook for cross-artifact holistic council; 3-REVISE iteration cap; PASS-required-before-platform-upload exit contract.
- `Reference/Hardness_Playbook.md` :: 11-lever catalog; verify each selected lever (L1/L2/L7/L8/L11) still triggers end-to-end across the artifact set.
- `Reference/Rubric_Format.md` :: schema + dilution math + agent-centric phrasing + service-metadata completeness rules.
- `Reference/Prompt_Format.md` :: 500-word cap, no em-dashes, no tool names, no "at least N", implicit-prompt framing rules.
- `Reference/OE_Format.md` :: numbered prose, tool-parameter binding, MoveOps service / param convention (bare-name email, `payload` slack, `issueId` linear, `base_id`+`table_id` airtable).
- `Reference/Strict_Convention_Inventory.json` + `Reference/OE_Convention_Inventory.json` :: V3 convention frequencies cross-checked at the integrated artifact-set level.

## Per-task data (cross-artifact consistency re-checks)
- `Tasks/34_6a42ec7493b48d5ada4571bd/5_Prompt.txt` :: read as the framing-anchor of the artifact set; each prompt ask traced to OE + rubric.
- `Tasks/34_6a42ec7493b48d5ada4571bd/6_Oracle_Events.txt` :: 22 OEs read holistically; each OE step traced back to prompt + forward to rubric coverage.
- `Tasks/34_6a42ec7493b48d5ada4571bd/7_Rubrics.json` :: 22 rubrics read alongside OE + prompt; every concrete value (IDs, dates, addresses, channel IDs, base_id, table_id, record_id) grep-checked against Fact_Ledger atoms.
- `Tasks/34_6a42ec7493b48d5ada4571bd/_aux/Hardness_Plan.md` :: 5 selected levers re-mapped to prompt sentence + OE step + rubric; THIN_DENSITY 47-midpoint plan-justification carried forward.
- `Tasks/34_6a42ec7493b48d5ada4571bd/_aux/Fact_Ledger.json` :: 216 emails / 64 amounts / 154 dates / 132 personas atomized; integrated-artifact concrete-value grounding verified.
- `Tasks/34_6a42ec7493b48d5ada4571bd/_aux/Universe_Index/*.md` :: service inventory, entity / persona inventory, key facts, today_horizon (universe_today 2026-04-26), accounts_per_entity, graph_report — re-read for cross-artifact end-state consistency.
- `Tasks/34_6a42ec7493b48d5ada4571bd/_aux/Verification_s1.md` / `Verification_s2.md` / `Verification_s3.md` :: prior phase PASS-STRICT records carried into FINAL grounding.
- `Tasks/_meta/Learnings.md` :: L6 (answer-leakage hard rule), L8 (multi-link chain), L9 (authority dismissal), L10 (structured-DB skip), L13 (first-framing), L25 (existing-output anchor), L26 (decoy-parent / channel-misalignment), L29 (escape-valve mitigation) cross-checked end-to-end.

## Validator gates (pre-FINAL)
- `Validators/phase_ready.py --phase final --task Tasks/34_6a42ec7493b48d5ada4571bd` :: PASS (all 5 upstream artifacts + valid upstream Verification_s3.md).
- `Validators/validate.py --phase all --task Tasks/34_6a42ec7493b48d5ada4571bd` :: PASS (prompt 0F 0W, oe 0F 0W, rubrics 0F 3 benign WARNs documented in Verification_s3.md).
