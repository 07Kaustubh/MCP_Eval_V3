# Verification — PIPELINE FINAL (Step 0.5 cross-source re-check), round 2

Universe `harmonygames` · framework `hg` · model under test Claude Opus 4.7 · universe today 2026-02-28.
Round 2 re-gates the artifacts that were edited after round 1 closed. Nothing below is carried forward
from the round-1 report; every figure was re-derived from source.

## Data sources consulted

Categories: **Per-task data** (the HG contract descriptor plus the hydrated base export it points at) ·
**Eval spec** (`Evals_harmonygames/0-5`) · **QC spec** (`Docs_harmonygames/7_QC_Spec_Doc1.json` +
`8_QC_Spec_Doc2.md`) · pipeline reference (`Reference/Sessions/FINAL.md`, `Reference/Council_Protocol.md`, `AGENTS.md`).

- **Per-task data** :: `3_UniverseDataForThisTask.json` read as the 940-byte contract descriptor it is,
  resolved through `Validators/universe_data_source.py` to
  `HarmonyGames_Base_Universe/Services_Data/` overlaid by `4_Changelog.json` (empty — this task injects
  nothing). Not read as if it were data.
- **Eval spec** :: `Evals_harmonygames/0_Injection_Quality_Eval.md`, `1_Prompt_Eval.md`,
  `2_OE_Eval.md`, `3_Rubrics_Eval.md`, `4_Verifier_Fails_Eval.md`, `5_Submission_Gate_Eval.md`.
- **QC spec** :: `Docs_harmonygames/7_QC_Spec_Doc1.json` (7 dims / 38 sub-dims, 18 binary) and
  `Docs_harmonygames/8_QC_Spec_Doc2.md` (severity ladder; Overly Broad = Moderate here), plus
  `Docs_harmonygames/12_Always_Failing_Rubrics.md` and `14_Persona_ACL.md`. No other universe's spec
  was loaded.
- All 3 artifacts (`5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json`) read together, plus the
  round-2 pre-edit backups to establish exactly what the post-FINAL edits changed.
- `HarmonyGames_Base_Universe/Services_Data/` (the HG `base_export_plus_changelog` source of truth,
  hydration verified first) :: snowflake tables re-aggregated row by row; all four cited Slack
  channels and the one cited DM opened; all 16,249 Robert Gmail threads swept.
- `_aux/Universe_Split/` :: cross-checked for the end-to-end dependency chain.
- `_aux/Fact_Ledger.json` :: used only as an index. Every load-bearing figure was recomputed from
  `Services_Data/` rather than accepted from the ledger.
- `_aux/Hardness_Plan.md` :: five selected levers traced prompt sentence to OE step to criterion.
- `_aux/Verification_s1.md` / `Verification_s2.md` / `Verification_s3.md` :: cross-referenced.
- `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` and `4_Persona_ACL_Roster.json`.

## All eval specs verified
- `Evals_harmonygames/1_Prompt_Eval.md` :: re-applied at the integration layer; `validate.py --phase prompt` PASS.
- `Evals_harmonygames/2_OE_Eval.md` :: re-applied; `validate.py --phase oe` PASS.
- `Evals_harmonygames/3_Rubrics_Eval.md` :: re-applied per criterion. Four HARD GATEs did work this
  round — the `category` enum (BLOCKER-3), Accuracy / observability (MAJOR-3), Atomicity
  decomposition (MAJOR-2) and Requirement Provenance (MAJOR-4).
- `Evals_harmonygames/4_Verifier_Fails_Eval.md` :: Lens 6 bucket simulation, 0/32 Bucket_1_Risk.
- `Evals_harmonygames/5_Submission_Gate_Eval.md` :: `validate.py --phase submission_gate` PASS.
- `Evals_harmonygames/0_Injection_Quality_Eval.md` :: `--phase injection` PASS; task injects nothing.

## QC spec coverage check (`Docs_harmonygames/7_QC_Spec_Doc1.json` + `8_QC_Spec_Doc2.md`)
7 dimensions / 38 sub-dimensions, 18 binary. All Prompt, Universe, Oracle-Event and Rubric sub-dims
scored at this phase. `check_qc_binary.py` clears all 6 that are measurable pre-trajectory.
Trajectory sub-dims (tool-call count, agent failure rate, error rate) and
*Universe / Cross-service Coherence* are deferred to S4 by spec construction, not skipped —
the specific coherence item to watch is named in the FINAL report's Carry-into-S4 list.

## Verification statements
- [x] `validate.py --phase prompt / oe / rubrics / injection / submission_gate` all exit PASS, 0 fails, 0 warns.
- [x] `check_rubric_antipatterns.py`, `check_oe_rubric_sync.py`, `check_ordering_coverage.py`,
      `check_qc_binary.py`, `check_persona_acl.py`, `check_hydration.py`, `phase_ready.py` all clean.
- [x] 6 FINAL lenses returned PASS after one REVISE round applied in place.
- [x] Zero answer leakage: `10,800` and `8,452` return zero word-boundary hits across every
      Robert-reachable Slack channel and all 16,249 threads in his mailbox.
- [x] Every Hardness lever still triggers end-to-end; L10 hop 1 is now directly graded, upgrading the
      round-1 PARTIAL.
- [x] Every tight identifier re-verified against source. One phantom claim was found (OE 20's
      "three Singular invoices at 6,250 each") and corrected.
- [x] All 22 OE tool names and every bound parameter verified against that specific tool.
- [x] Rubric count 32 (cap 60); Process 1/32 = 3.1% (cap 40%); category enum spec-conformant.
- [x] Density midpoint ~48 across 6 services, against the HG 40+ / 3+ target and the >=15 QC floor.
- [x] Calendar sweep cleared manually (gcal empty universe-wide), since F9 is unavailable for HG.

## Discrepancies surfaced
1. **OE 20 stated a Singular reconciliation that does not exist in the mailbox.** Corrected; the two
   criteria that depended on the vendor figures were removed rather than widened. Full reasoning in
   `Council_Reports/FINAL_council.md` BLOCKER-1 and BLOCKER-2.
2. **The rubric `category` enum had been downgraded to the legacy two-value form** after round 1.
   Restored.
3. **OE 8 contradicted criterion 4 and OE 24 on the acquisition-spend window.** Resolved in favour of
   the prompt's own "last day there is anything to look at".
4. **Two criteria could not fail on any run** (the ACL-invisible 12K, and Gmail send discipline
   against a catalog with no send tool). Both removed; the reasoning is recorded in the OE as new
   OE 28 so it is not silently re-added.
5. **One non-atomic criterion** (two versioned marts bundled). Split.
6. **Two criteria were absent from their OE decompose directives.** Mirrored back into OE 24 and OE 27.
7. **Open, not a defect:** criterion 5's four-way engagement accept set is Overly Broad (Moderate on
   the HG ladder) and is kept deliberately, because the prompt asks for the engagement side without
   naming a figure. Recorded rather than closed.

## Verdict

**PASS.** Six lenses clear after one REVISE round applied in place and re-gated. Four criteria removed,
one split, the category enum restored, eight OE steps corrected and one added. Every deterministic gate
re-run on the corrected 28-OE / 32-criterion set returns 0 fails and 0 warns. Cleared for platform
upload; next trigger is `PIPELINE S4` in a fresh chat once six trajectories and the verifier fails exist.

## Post-verdict addendum: platform rubric linters (2026-08-07)

Four rubric linters run after the verdict. Two PASS, two with findings, both against criteria this
verification had already listed as residual risk. Detail in `Council_Reports/FINAL_council.md`
addendum; responses in `_aux/Linter_Justifications.md` (clears `check_justification.py`).

- **Unrequested Scope (FAIL)** on the 24,275 R&D exclusion: accepted. Criterion rewritten to pin the
  funds-available figure at 13,300 rather than name the credit. Leakage re-checked and clean.
  Mirrored into OE 18, OE 24 and OE 28.
- **Atomicity** on the four-way engagement disjunction: accepted, which closes discrepancy item 7
  above. Pinned to the 801 peak with `across both platforms` in the title, because the per-platform
  maximum is 426 on a different date. OE 24 narrowed to match.
- **Atomicity** on "two or three figures": dismissed. The range is the prompt's own closing line, and
  narrowing it would breach the Prompt Specificity Ceiling.
- Criterion count unchanged at 32. Every gate re-run: 0 fails, 0 warns across all five phases and all
  five supporting checkers.

New residual to watch at S4, replacing item 7: criterion 26 pins a summed figure, so an account
stating 10,800 and 2,500 without printing the 13,300 total is the one shape that could fail it
unfairly.

## Post-verdict addendum 2: scope linter, second pass (2026-08-07)

Scope linter re-fired on the versioned-mart criteria. Accepted, and the rule from addendum 1 was
applied to the whole exclusion family rather than only to the flagged pair. Removed the two mart
criteria (subsumed by the 0.00 revenue and 7,483.42 spend criteria) and the monthly-net-burn criterion
(zero signal); rewrote the Metabase and dbt criterion to ask about the cancellation list the prompt
itself raises; kept the sale-versus-licence criterion, whose subject the prompt names. 32 to 29
criteria. OE 24 and OE 28 mirrored. All gates re-run: 0 fails, 0 warns. Detail in
`Council_Reports/FINAL_council.md` addendum 2, responses in `_aux/Linter_Justifications.md`.

## Post-verdict addendum 3: overlap linter (2026-08-07)

Overlap linter flagged the net-proceeds criterion as subsumed by the gross-versus-net criterion.
Accepted; this reverses discrepancy item note 2 in the Lens 6 residuals, which had argued the pair was
a partial-credit split. The gross-versus-net criterion was cut rather than the net-proceeds one,
because its interpretive verb can fail a correct account that gives the gross implicitly, and because
the lever it guarded is guarded three more times. 29 to 28 criteria; OE 24 mirrored. All gates re-run:
0 fails, 0 warns. Detail in `Council_Reports/FINAL_council.md` addendum 3.
