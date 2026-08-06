# MCP Eval V3 — Project Knowledge Base

**Updated:** 2026-07-22

> **Operator?** Read [`QUICK_START.md`](QUICK_START.md) — the 1-page how-to.

## What this project is

An evaluation pipeline for MCP-task deliverables (prompts, oracle events, rubrics) built on the **Brookfield CPAs & Advisors** synthetic universe. The pipeline produces 5-of-5 QC-grade deliverables that meaningfully stump **Opus 4.8** during the 6-run agent verification step.

## Hard rules (apply to every phase, every chat)

1. **Opus 4.8 is the model under test** for Brookfield / KeyStone / MoveOps / StarPM. **HarmonyGames verifies against Claude Opus 4.7** (`Guide_harmonygames/How_To_Use_This_Eval.md`, `Docs_harmonygames/1_Project_Instructions_Overall.md:388`), so read `model_under_test` from the registry rather than assuming 4.8. All hardness engineering targets known Opus 4.8 failure modes from `Docs/4_Prompt_Hard_Tips.md` and `Reference/Hardness_Playbook.md`.
2. **Per-task `3_UniverseDataForThisTask.json` is the ONLY universe source of truth — except HarmonyGames.** Always work from the split written to `Tasks/<TASK_DIR>/_aux/Universe_Split/` for the current task. **HarmonyGames inverts this**: its per-task file is a 940-byte contract descriptor that says "This task uses the Base Universe data by default... Do NOT extract or paste the full universe data", so the source of truth is `HarmonyGames_Base_Universe/Services_Data/` overlaid by `4_Changelog.json`, resolved through `Validators/universe_data_source.py` (`base_export_plus_changelog` contract). Reading the descriptor as if it were data is the root cause of the phantom-atom class of bug.
3. **`Brookfield_Base_Universe/` is stale by default.** The one stable file is `8_Server_Tools_Details.json` (tool definitions). Persona briefs in `2_Persona_Briefs.md` are also stable (personas do not change per task). Everything else in that directory describes a snapshot that may not match the per-task universe.
4. **No universe edits in this pipeline.** Hardness comes from levers already present in the per-task data. If S0/HARDNESS finds fewer than 3 levers, stop and ask the user to decide. **V4 (StarPM) exception: INJECTION is allowed and first-class.** A V4 task may ADD scenario data via `9_Universe_inject.sql` + `4_Changelog.json` - that is injection, not editing: base universe rows are never modified or deleted, and every injection must clear `validate.py --phase injection` (Evals_starpm/0: 7 hard gates + a council difficulty floor that is **per-universe** - 3.5 for StarPM, 2.5 for HarmonyGames, read from the framework key `injection_difficulty_floor`). Editing existing base-universe data remains forbidden in ALL universes. As of v21.2 every upstream Tasks_Template (all five universes, HarmonyGames included) ships `9_Universe_inject.sql` + `4_Changelog.json`, and `validate.py --phase injection` runs for ANY universe whenever the inject file carries executable statements (comment-only template headers SKIP): V4 gets the full Evals_starpm/0 window gates; V3-family gets the same deterministic gates with the date ceiling set to that universe's registry `today`.
5. **500-word cap on prompts. No em-dashes anywhere.** Validator blocks both.
6. **No "at least N" in rubric titles** unless the prompt explicitly mandates a minimum. Atomic rubrics for multi-item write actions. Deliberately stricter than the guidelines, which permit "at least N" when ground truth is genuinely indeterminate: in practice that exemption has been claimed for determinate ground truth and produced reward-hackable thresholds, so the pipeline requires an explicit prompt mandate instead. Practice-learned, not a transcription of spec prose.
7. **No tool names in prompts. No tool names in rubric titles.** Allowed only in OE bodies and in rubric evidence / justification fields.
8. **Outcome must outnumber Process in rubrics** (Brookfield / KeyStone / MoveOps / StarPM; authority `Docs/7_QC_Spec_Doc1.json:151`, dated 05/22). **HarmonyGames is the exception:** its own QC spec replaces the Outcome-majority requirement with a flat binary cap of Process <= 40% of the set, and states that zero Process is valid. Each universe follows its own spec. All 4 V3 reference tasks have zero process rubrics. Default to zero. Three-condition test before adding any. Deliberately stricter than the guidelines, which removed the fixed ratio on 2026-05-20: the ratio is retained because process rubrics that survive the three-condition test are rare in practice and a process-heavy set has correlated with QC rejections. Practice-learned.
9. **Platform similarity ≥ 40% is not allowed.** Pivot the prompt using `Reference/Similarity_Pivot.md`.
10. **5 of 5 on every QC sub-dim is the bar.** Both councils must return GO before any deliverable ships.
11. **Density is framework-scoped. V3-family (Brookfield/KeyStone/MoveOps): 50+ tool calls midpoint is the design target; 40 is the absolute floor. V4 (StarPM): 40+ average is the design target (Docs_starpm/1 hard gate), 15 is the QC-spec fail floor, applied PER MODEL (Opus and Gemini separately).** For V3-family: Council B-B3 (tool-call density projection), HARDNESS, AUDIT, and FINAL all use this tiered scheme: midpoint ≥ 50 = PASS; midpoint 40-49 = THIN_DENSITY (operator can continue with explicit per-task justification, but the task is at risk of underflow on real platform runs); midpoint < 40 = INSUFFICIENT_DENSITY (BLOCKER, STOPs the pipeline). The 50+ design target was set after tasks shipped with 40+ projected density came back from the platform failing density on real runs — designing for 50+ produces ~40+ tool calls in reality.
12. **Strict veteran AUDIT runs after every per-phase deliverable.** S1/S2/S3 (and S1.5 on prompt revise, and REVIEW on corrected materialization) auto-fire an AUDIT sub-agent inline after Council A + Council B pass. `PASS (STRICT)` is a required exit criterion for those phases. `REVISE` iterates the producing phase (cap 3 rounds); `REBUILD` STOPs to `PIPELINE REDO`. Catching defects at the producing phase is the project policy — downstream re-iteration at FINAL or platform-reviewer time is more expensive than the ~3 additional sub-agent calls per task that auto-AUDIT costs.
13. **Single-target uniqueness, every-service sweep (incl. Calendar), naive-agent simulation.** Before writing any write-action rubric that pins a record, confirm exactly ONE universe record matches the prompt's described target. If two or more match (e.g. three make-ready rows for the same unit), disambiguate in the prompt or (V4) inject a disambiguator - never hard-code one row id the prompt names only by entity. Before any 'complete' or 'only open item' claim, sweep the entity across EVERY service INCLUDING Calendar (a confirmed future event is open work). Review the prompt WITHOUT the OE in view and confirm no reasonable agent could pick a different valid target. Enforced deterministically for V4 by `validate.py --phase submission_gate` (F7 AMBIGUOUS_TARGET / F8 NON_ATOMIC_ENUM / F9 UNRECONCILED_FUTURE_EVT). Origin: `Tasks/_meta/Postmortem_2026-07-25_Task39_LasPalmas_QC_Fail.md`.
14. **60 rubrics is the hard upper limit on `7_Rubrics.json` (and `15_Updated_Rubrics.json`).** Operator constraint, recorded 2026-07-26 after Task 44 shipped a 64-criterion set through S3, AUDIT and FINAL unchallenged because no spec doc, eval or validator carries the cap. S3 must budget against 60 from the start rather than decompose freely and trim at FINAL. When a set runs over, cut criteria that **retire risk** (FINAL Lens 6 Bucket-1 flags, beyond-prompt criteria, diluting owner accept-sets, meta-statements about the agent's own writes) before cutting any that carry coverage, and **never merge two criteria to save a slot** — merging manufactures the F8 NON_ATOMIC_ENUM defect. Never cut a Hardness lever carrier. Any cut that removes a content element named in an OE's `S3 must decompose this into one criterion per content element (…)` directive must be mirrored into that OE in the same pass, or the artifacts drift.

15. **Every phase that reads a platform-pasted input must pin it by content hash before reasoning about it, and re-verify the pin before declaring the phase complete.** `Validators/check_export_freshness.py <task> --pin` at entry, bare at exit. Recorded 2026-07-26 after Task 44 had two consecutive S4 passes silently invalidated by mid-session re-pastes of `8a`/`8b`: pass 3 was superseded at 16:18 and pass 4 at 18:20, the second moving Opus per-run from 28/33/43/31/32/37 to 32/32/44/32/36/46 and shrinking the both-model all-failing set from six criteria to five. Both times `phase_ready.py` and `close_task.py` still reported READY, because nothing recorded WHICH bytes a report described. **Never reconcile a drifted pass by hand, and never carry a per-cell or per-run count forward between passes; re-derive from the export in hand.** Corollary on grading noise: two independent regradings of byte-identical trajectories moved 8.5% and 8.6% of decision cells in opposite net directions, so a single-cell number is not a stable quantity and gate margins are the only durable claim.

16. **A rubric whose title reliably induces the same judge misreading is a rubric defect, not a judge error.** Reclassify Bucket 2 to Bucket 1 once the identical misreading appears on 3+ cells or on both models, and fix the title rather than filing appeals. Threshold and fix pattern live in `Reference/Sessions/S4.md` under Bucket 1b. Recorded 2026-07-26 after Task 44 filed two Moderate Overly Specific defects (criteria 58 and 59) as judge errors because their evidence fields technically disclaimed the requirement the grader kept applying. An appeal cannot fix a title that will mis-grade on every future export, and the Rubrics-Eval severity ladder charges the Rubric Quality sub-dim either way.

17. **S4's trajectory walk is fail-driven and therefore blind to a criterion that passes for the wrong reason. Audit the passing cells too.** `Validators/check_criterion_dependencies.py <task>` reports every cell where a dependent criterion passed in a run where the criterion creating its subject artifact failed. Any hit is an Overly Broad Bucket 1 defect: bind the dependent's subject to the antecedent's artifact in both title and evidence, describing that artifact by content rather than by criterion number so the binding survives renumbering. Recorded 2026-07-26 after Task 44's West-cluster owner criterion passed 6/6 on Gemini while its antecedent passed 2/6, clearing S3, AUDIT, FINAL and four S4 passes before an operator caught it by eye.

18. **A closed council/AUDIT finding must be converted into a standing gate, not recorded in prose.** Any finding closed by a hand-run grep gets a check in `Validators/check_rubric_antipatterns.py` in the same pass. Recorded 2026-07-26 after `AUDIT_rubrics.md` finding F1 classified `FAIL only if` as MODERATE ("made omission a PASS, nullifying the criterion"), fixed it to the additive `FAIL if X, and FAIL if Y`, verified it with a regex run once by hand, and a later edit to that same criterion reintroduced it with `validate.py --phase rubrics` still returning 0 fails / 0 warns. Related: the severity census in council and AUDIT reports is a **self-report by the agent that authored the rubrics**, so it cannot catch that agent's blind spot. Four Task 44 reports asserted "0 Major / 0 Moderate / 0 Minor" while an independent review of the same artifact found two Moderate and one Overly Broad. Treat a council's own census as a claim, and prefer a mechanical check wherever the defect shape is mechanically detectable.

19. **A council may not decline a finding it has itself validated as real, on internal-precedent grounds alone.** If a council writes that a concern "is real" and then declines it, the finding is escalated to the operator, not closed. Recorded 2026-07-26 after `FINAL_council.md` logged MINOR-3 with the observation that "an agent that names Brooke as owner on every item scores full marks on ownership without any per-item reasoning, diluting the discrimination", declined it citing `AUDIT_rubrics.md` Q1, a prior Council B round, Learnings item 12 and Task 41, and concluded "the dilution concern is real but strictly less costly than a false-fail". An independent review of the shipped artifact then flagged that same owner criterion as Overly Broad. In the same lens FINAL asserted "no two accept-sets are nested such that one agent act satisfies two criteria in the same artifact", which was false: an owner named on a comment to a pre-existing record satisfied the owner criterion in runs where the criterion requiring the item to exist failed. **Chains of internal citation are not evidence about the artifact.** A decline must rest on a fact re-read from the universe or the artifact, quoted in the decline, and never on the fact that an earlier phase decided something.

20. **Council prose volume is not evidence of rigour, and long reports that find nothing are a defect in the phase, not a sign of thoroughness.** Task 44 produced 485 KB of council and AUDIT prose across 12 reports for one 60-criterion task. `AUDIT_prompt.md` alone was 92 KB / 804 lines and recorded **zero** severity findings; `S1_A_grounding.md` was 47 KB with zero. Across the four reports that adjudicate findings, **11 findings were declined**, and the defects an independent review later found in the shipped artifact were of exactly the class those reports had examined and cleared. When adding a council, lens or sub-agent, state what defect class it catches that an existing gate cannot, and prefer a deterministic checker whenever the defect shape is mechanically detectable (see rule 18).

21. **For a criterion that fails ALL completed runs, the default is removal, not justification.** `Docs*/9_Common_Error.md`, "Unfair Rubric Criteria": *"If and only if we can vehemently defend the existence of this criterion, should we keep it. Otherwise, we need to remove it."* The pipeline's S4 had the opposite default: it classified all-failing criteria into buckets and then *produced AF justifications* for the legitimate ones, framing Bucket 3 as desired difficulty. Keep-and-justify is the wrong starting posture, and it is the mechanism by which two Moderate defects shipped on Task 44 as "judge errors" rather than being fixed. **Every all-failing criterion must first be argued for removal; it survives only if the defence is one you would state to a reviewer unprompted.** The 5-point pre-write checklist is the test of whether that defence exists, not a formality to clear before writing prose.

22. **Four source docs were never consulted by any phase. Read them where they apply.** Audited 2026-07-26 by grepping every pipeline file for each source filename: `9_Common_Error.md` (0 references), `11_Taxonomy.md` (0), `1_Project_Instructions_Overall.md` (0), `3_Rubrics_V3_One_Pager.md` (0), plus `4_StarPM_SCENARIO STORYLINES.md` (0) and `10_How_To_Load_and_Edit_Universe.md` (0, and it is the injection how-to). `9_Common_Error.md` alone is a 15-error checklist covering prompt, OE and rubric authoring, including the all-failing-criteria rule in item 21 above. A QC pipeline that never opened the project's own Common Errors document is the clearest instance of the pattern in rules 18 to 20: internal machinery substituting for the source.

23. **"Default to zero Process rubrics" never overrides an ordering requirement.** `Docs*/11_Taxonomy.md` and `Docs*/2_Rubrics_V3_Guidelines.md` both name ordering as the **primary** case for a Process rubric, and state that "no Outcome rubric can verify ordering" and that an ordering constraint "can be explicit in the prompt and still require a Process rubric". Rule 8's default-to-zero is a budgeting heuristic derived from four reference tasks; it is not a licence to leave a requirement ungraded. **If the prompt orders actions, one Process rubric per ordering constraint, phrased so any valid path passes.** Enforced by `Validators/check_ordering_coverage.py`. Recorded 2026-07-26 after Task 44 shipped 60 Outcome and 0 Process rubrics while its prompt said "put a slot on my calendar to go back out and re-inspect whatever ends up in that follow-up" and "Then post where this stands in the channel": both deliverables' criteria pass regardless of sequence, so the ordering was never graded at all.

24. **Rubrics carry no Outcome sub-category, and that is why overlap cannot be checked mechanically.** The guidelines define three Outcome sub-categories with distinct rules: 1.1 write-action result, 1.2 action content ("only write 1.2 if it adds a distinct check beyond 1.1"), 2.1 key facts in the final response. `7_Rubrics.json` records only `category: outcome|process`, so the pipeline cannot evaluate "distinct check beyond 1.1", cannot detect two criteria grading the same artifact, and cannot check the guidelines' per-sub-category verb conventions. This is the root cause of the one check that had to be abandoned for noise (nested accept-sets, `check_rubric_antipatterns.py` A4): without knowing which artifact each criterion grades, subject identity is not computable. **Adding a `sub_category` field (1.1 / 1.2 / 2.1 / process) is the single highest-leverage schema change available** and makes the overlap, redundancy and verb-convention checks tractable. Not applied unilaterally: it touches the rubric schema, the validator and all four task templates.

25. **Authority hierarchy, in order: QC Spec Docs > Evals > Rubric Guidelines > pipeline convention.** Where they disagree, the later-dated QC spec entry wins. Recorded 2026-07-26 after a parity pass wrongly relaxed the outcome-to-process ratio on the strength of `Docs*/2_Rubrics_V3_Guidelines.md` dated **May 20, 2026** ("Removed fixed outcome-to-process ratio"), while `Docs*/7_QC_Spec_Doc1.json` reinstates it as a **binary** sub-dimension dated **05/22** ("Pass (5): The number of Outcome Rubrics is greater than Process Rubrics"). The QC spec is both later and higher authority, and Rubric Category Balance has no 3/4 band, so a process-heavy set is an outright FAIL. Never relax a rule against guidelines prose without checking the QC spec for a later, binary restatement.

26. **Ten QC sub-dimensions are BINARY (no 3/4 band). Gate them deterministically, never in council prose.** From `Docs*/7_QC_Spec_Doc1.json`: Prompt / Tool use and Cross-service requirement, Investigation, Coherence, Alignment with Today's Date; Universe / Universe Feasibility, Cross-service Coherence; Rubric / Rubric Category Balance; Trajectory / Tool Call Count, Agent Failure Rate, Error Rate. One defect on any of these is a FAIL with no partial credit, so they are the last place discretionary prose belongs. `Validators/check_qc_binary.py` evaluates nine of the ten deterministically in one report with the spec citation for each. The tenth, Universe / Cross-service Coherence, is genuinely conditional on a contradiction *causing an agent failure*, so it can only be judged against trajectories and is named as human work rather than assumed covered.

27. **Severity taxonomy, current as of QC Spec Doc2 07/16: Overly Specific is MODERATE, Overly Broad is MINOR.** They were swapped on that date (Overly Specific promoted from Minor, Overly Broad demoted from Moderate). This matters because Overall Rubric Quality Pass(5) requires **zero major and zero moderate** issues, so a single Overly Specific criterion costs the 5 while a single Overly Broad one does not (Pass(5) tolerates <5% minor). Percentage bands, denominator = the CB's own criterion count, do not double-count a criterion with multiple issues: Fail at >10% major, >15% moderate-or-major, >20% minor-or-worse.

28. **A criterion that passes on every run is a weak assertion, not a safe one.** Mutation-testing practice treats an assertion holding on every mutant as verifying nothing; the canonical case is asserting non-null instead of asserting the value. The rubric analogue is a criterion passing every cell of every model. `Validators/check_rubric_signal.py` classifies every criterion as DISCRIMINATES / ZERO-SIGNAL / ALL-FAIL and names the cut candidates: existence-only criteria on an artifact whose content a sibling already grades. On Task 44, **11 of 60 criteria (18%) produced zero discrimination and 5 were clean cut candidates** (the ticket-created, plumbing-work-raised, calendar-scheduled, channel-posted and draft-created criteria), on a set that was simultaneously at the 60-criterion ceiling and unable to fit the Process rubric for its ordering requirement. The budget for that coverage already existed. Run this before trimming to the cap, and never cut a lever carrier (rule 14).

29. **Report grader instability as Cohen's kappa, not as percentage of cells moved.** Raw agreement is inflated by chance on an imbalanced Pass/Fail grid, so chance-correct the headline number. **The worked example previously given here was wrong and is corrected: recomputed from the per-run counts in rule 15 (28/33/43/31/32/37 and 32/32/44/32/36/46 of 60), the grid is 57-62% Pass, NOT "mostly-Fail", and at Po=0.914 Cohen's kappa is **+0.822 ("almost perfect")**, not 0.23.** A kappa near 0.23 at ~90% agreement requires single-category prevalence around 5-10%, which this grid does not have. The kappa paradox is real and bites above roughly 60% single-category prevalence, but it was not the active failure mode here. Report Po alongside kappa plus a prevalence index (Byrt) rather than swapping in a friendlier coefficient: Gwet's AC1 is contested as a kappa substitute and the Landis-Koch verbal bands must NOT be applied to it. The pipeline had been reporting Task 44's instability as "8.5% and 8.6% of cells moved", which reads as ~91% reliable and is not. `Validators/check_criterion_stability.py` computes kappa per model across archived gradings and lists the criteria that flip on identical trajectories, which is the actionable output: published rubric-grading work finds agreement high for objective criteria and poor for subjective ones, so a criterion that flips is a **wording** defect. Reword it rather than appealing cells on it. `check_export_freshness.py --pin` now archives every export to `_aux/Verifier_Exports/` so the series exists; before that, each re-paste destroyed the prior grading and made this unmeasurable.

30. **The pipeline's own internal citations are checked, not trusted.** `Validators/check_pipeline_wiring.py` verifies that every path, script, CLI flag and `--phase` value cited in AGENTS.md and `Reference/**` resolves, that every validator imports cleanly, that cross-validator `from X import Y` references exist, and that the validator registry above matches disk. Added 2026-07-27 after an audit of all 35 validators and 26 docs found: `Knowledge_Flow.md` declaring COMPARE's output as `_aux/Compare_Report.md` when `compare_rubrics.py` only printed to stdout, and `make_fill_script.py` performing `sys.argv` indexing and a file read at module level, so it could not be imported and with no argument silently read `./7_Rubrics.json` from the caller's working directory. Both fixed. Run it after editing any runbook or validator; it is cheap and it is the only thing standing between a renamed file and an operator hitting a dead reference mid-phase.

31. **A negatively-framed rubric criterion is a QC failure unless the prompt explicitly mandates a prohibition or non-action.** QC dimension 23 "Rubrics - Negative Criteria", error category `[Fail - Criteria Framing]`, Fail=2 / Pass=5, no partial band. `Docs_harmonygames/8_QC_Spec_Doc2.md:295` prescribes the method exactly: **pre-scan** for `does not`, `must not`, `never`, `no`, `without`, `fails to`, `avoids`, **then review each hit** - a word-presence hard-fail is itself a spec violation. `:302`: a criterion fails "only when it does not correspond to an explicit non-action or prohibition instruction yet is framed negatively". The shipped counter-example that MUST pass: "The Agent reports that PR #438 had no human-submitted review" (affirmative actor+verb; "no ..." only names the content checked). The shipped fail: "The Agent does not omit the ENG-1797 link." Valid negative factual STATES when affirmatively reported: `unresolved`, `unimplemented`, `unconfirmed`, `access denied`. Enforced by `Validators/check_rubric_antipatterns.py` (two-stage: mechanical pre-scan, then prompt-mandate adjudication), and blocking inside `validate.py --phase rubrics` under the `rubric_negative_criteria_gate` / `rubric_vague_exemplar_scope` framework flags, which are true only for `hg` because no other universe's QC spec carries either dimension. **Only a negation on the Agent's own VERB blocks.** `no` and `without` heading a noun phrase name the finding, not the action, and treating all seven indicators alike flagged 10 criteria across two QC_PASSED HarmonyGames tasks, five of them the spec's own valid shape minus its `that` (`The Agent records no submitted review for PR 854`). Those shapes are surfaced for the spec-mandated human review and never block. Anchor `v22 RA-7` is the only thing pinning that split - RA-1 and RA-2 both still pass if it is undone. Related and separately scored: **Vague Exemplar Language** - `such as` / `e.g.` / `for example` in ANY rubric field is one Moderate issue each (`:270`).

32. **Persona ACL read-scoping is a PROMPT FEASIBILITY gate, and a violation is a task defect, not a model miss.** `Docs_harmonygames/14_Persona_ACL.md`: reads are persona-scoped in **seven** services (Gmail, Slack, GCal, GDrive, GDocs, GSheets, GSlides) and unscoped in **six** (`:52` - "contains exactly Contacts, GitHub, Snowflake, Trello, Linear, and Confluence"). Every required read must be validated **from the assigned persona's Agent/Verifier view, not Universe Explorer god-mode** - the explorer shows ALL records by default, including ones the persona cannot see. A prompt requiring evidence the persona cannot access fails `[Fail - Prompt Feasibility with Tools]`. **ACL does not govern writes** (`:17`), and `:134` forbids making an ACL-based write denial necessary to a prompt, Oracle Event or rubric - so never author a task whose difficulty comes from a write the ACL supposedly blocks.

33. **A gate that reads an export-backed universe must be constant-memory, and that bound must be MEASURED, not asserted in prose.** For `base_export_plus_changelog` universes the "universe" is the hydrated base export: **8.1 GB across 316,543 files** as of the 2026-08 drop, including a single `Base_Universe_Complete_Data.json` of **359,094,851 bytes**. Any check that answers a question about the universe must stream it. Measured with the early exit deliberately defeated so every file is read: the chunked presence scan peaks at **160 MiB** on the old 5.0 GB tree and **141 MiB** on the new 8.1 GB one - it is O(atoms), not O(payload), so a bigger universe costs LESS - while `json.load()` of the combined blob alone peaks at **673 MiB** and a full materialisation of the export is what OOM-KILLED the first fix for the phantom-atom bug. Enforced by `Validators/test_memory_bounds.py` at a **384 MiB** peak-RSS ceiling (2.4x over correct behaviour so it cannot flake, 1.75x under the forbidden one so reintroduction trips it), wired into `check_regression.py` alongside `--dead-gate`. Two portability traps are pinned in that file because each silently destroys the measurement: `ru_maxrss` is **bytes on Darwin and kibibytes on Linux** (a 1024x error), and **`RLIMIT_AS` is not settable on macOS**, so a hard address-space cap cannot be the enforcement mechanism. Recorded 2026-08-06. The reason this is a rule and not a comment: before it, `grep -rn "ru_maxrss|getrusage|RUSAGE" Validators/` returned NOTHING, so the only way an O(universe) regression could announce itself was an OOM kill on an operator's machine, after the work was lost.

34. **A labeled ground-truth corpus is a versioned artifact, not a frozen fixture, and a green selftest is not evidence it is current.** `qc_verdict.py selftest` grades the corpus against its own labels, so it stays green while the artifacts underneath go stale - on 2026-08-06 an upstream drop moved **35 of 112** HarmonyGames corpus files (`7_Rubrics.json`, `8_Verifier_Fails.txt`, `6_Oracle_Events.txt`, `9_QC_Feedback.txt` and 12 trajectories) and selftest still reported 10/10 bucket-correct. Nothing caught it: `QC_Tasks/` was absent from `check_source_sync.py`'s `SURFACES` table entirely, and even now that it is listed, that checker needs `--source <extracted drop>` and therefore can never see a **repo-side** edit. `Validators/check_qc_corpus.py` + `qc_corpus_hashes.json` pin all **138 labeled tasks / 1,476 files across 5 corpora** by per-task content hash, wired into `check_regression.py`. Industry practice for golden/ground-truth sets is the same shape: pin the consumed version by content hash, treat modifying a labeled case as production risk rather than housekeeping, and re-baseline only by explicit decision. After ANY intentional corpus sync, re-run `qc_verdict.py selftest` for **every** corpus and only then `check_qc_corpus.py --update`.

## Pipeline Deviations from Eval Specs

Where the 4 evaluator specs (`Evals/1_Prompt_Eval.md` ... `Evals/4_Verifier_Fails_Eval.md`) contain internal contradictions, conditional scoring, or under-specified rules, the pipeline picks one interpretation and documents the choice here. All deviations are conservative — when the spec is ambiguous, the pipeline picks the STRICTER reading.

| Eval spec rule | Spec ambiguity | Pipeline interpretation |
|---|---|---|
| Prompt Eval 2.8 universe-level date alignment is FAIL only if "it caused an agent failure" | Tautology at prompt-writing time (pre-trajectory) | Pipeline scores Prompt 2.8 as NON-FAIL when relative-date phrases are present but resolved windows have universe data; defers the "still-solvable exception" to S4 trajectory evaluation. |
| Prompt Eval 1.3 anti-pattern checks are binary PASS/FAIL but Phase 4.1 scoring uses 1/3/5 | No documented mapping | Pipeline maps each anti-pattern FAIL to a hard 1/5 on its corresponding sub-dim (Command List → Coherence; Bolt-on → Coherence; Pre-Solving → Pre-Solving sub-dim; Tool Mention → Explicit Tool Mention). |
| OE Eval contradicts itself on OE ordering | "OEs are unordered" vs Phase 3.2 dependency-chain checks ordering | Pipeline treats OEs as **unordered for coverage purposes** (Council B-B2 forward/reverse map) but **ordered when lifecycle preconditions apply** (`validate.py` lifecycle precondition check, v10). Both can be true simultaneously — coverage doesn't require order; lifecycle does. |
| Rubrics Eval Severity Taxonomy lists channel-lock-in as Minor; Phase 2.7 escalates to Major-by-default | Two conflicting rules | Pipeline applies Phase 2.7 escalation rule: channel/method lock-in is **Major by default** when a valid alternative path exists; Minor only when no realistic alternative is rejected. The taxonomy table's Minor entry is the FALLBACK, not the primary rule. |
| Rubrics Eval All-Failing Rubrics sub-dim defers to verifier stage | Verifier Fails Eval doesn't explicitly score it | Pipeline scores it at S4: `All-Failing Rubrics sub-dim FAILs if >50% of failing rubrics across the 6 runs are classified as Bucket 1 (Rubric Invalid)`. See `Reference/Sessions/S4.md` for the scoring sub-step. |
| Verifier Fails Eval Phase 3.3 says "this eval does not have access to agent trajectories" | Phase 3.2 requires per-run consistency analysis | Pipeline has full trajectory access via `Agent_Responses/Run*.json`. v10 S4 makes trajectory walk MANDATORY for every bucket classification. Pipeline exceeds the spec here. |
| Rubrics Eval Phase 4.2 threshold math allows dilution | A 100-rubric set with 1 Major (1%) PASSes | Pipeline adds absolute-count gates (Major ≥ 3 = FAIL; documented in `Reference/Rubric_Format.md`). |
| Rubrics Eval Phase 1.1 "0 Outcome = FAIL" but no fail path for missing Process when one is needed | Missing-Process is Non-Fail per spec | Pipeline applies v10 B6 propagation: when a needed Process behavior is identified, it propagates back to S3 as a `PROPAGATE TO S3` flag. Forces rubric expansion or Outcome tightening at the producing phase. |
| Specs reference `[V2] QC_Tasks/` as samples but pipeline uses `QC_Tasks/V3_Tasks/Task11..14/` | V2 samples are on the old Keystone universe | Pipeline reads V3 references directly (Brookfield universe). This is a pipeline-EXCEEDS-spec choice, documented for future spec alignment. |
| Eval specs require "TODO list at Step 0 HARD GATE" + "Phase 0 deep universe exploration" | No mechanism to verify | Pipeline runbooks list required inputs per phase; v11 E1 + E2 add `phase_ready.py` checks for TODO and reference-read logs. Without those, operator discipline is the only enforcement. |
| Tool-name handling differs per artifact (Prompt = FAIL anywhere; OE = MANDATORY; Rubric = NOT in title, OK in evidence) | Specs don't cross-reference each other | Pipeline `validate.py` handles per-phase correctly: prompt phase FAILs any tool-name token; OE phase FAILs only on UNKNOWN tool names; rubric phase FAILs tool names in title only. Per-phase distinction is intentional and stable. |
| MoveOps source zip folder `MCP_Eval_V2.1_Move_Ops/` ships V2.1 framework docs | V2.1 predates V3 — `Docs_moveops/2_Rubrics_V3_Guidelines.md` is filename-labeled V3 but framework-labeled V2.1; some rubric / OE conventions may have minor deltas from V3 Brookfield + V3.1 KeyStone | Pipeline registry tags MoveOps as `V2.1` (see `MoveOps_Base_Universe/` notes and `Validators/universes.py`). Read `Docs_moveops/2_Rubrics_V3_Guidelines.md` before applying validator behavior to MoveOps tasks; per-phase deltas are deferred (validator currently treats MoveOps with the same scoring as Brookfield/KeyStone — flag a deviation here if a real MoveOps task surfaces a divergence). |
| Upstream Brookfield drops (incl. the v21.2-generation `MCP_Eval_V3.zip`) ship `Docs/7_QC_Spec_Doc1.json` + one `Guide/` tree line with KeyStone-mislabeled universe prose ("v3 = Keystone Mortgage", `Mortgage_Base_Universe/` paths, `keystonemortgage.com` example) | Source-template hygiene issue persisting across upstream releases | Repo keeps flavor-corrected copies: ALL scoring rules adopted upstream-verbatim, only the universe-label prose corrected to Brookfield. Divergences are pinned in `Validators/source_sync_deviations.json` and verified by `check_source_sync.py --source <extracted_drop> --universe <name> --expect-deviations`. Everything else (Evals 1-4, Docs 8, templates, base universe) is upstream byte-identical as of the 2026-07 drops. |

When the spec gets a new version, re-check this table against the new spec. If a spec amendment resolves a contradiction differently than the pipeline's interpretation, update both the pipeline AND this table together.

## PIPELINE DISPATCH

> **Supersedes the legacy `command workflow.txt`** (archived to `_archive/` in v21). The 16 PIPELINE triggers below are the only entry points the operator needs. The historical workflow doc is preserved at `_archive/command workflow.txt` for archaeological reference; the runbook contracts it described are now codified in `Reference/Sessions/*.md`.

Each trigger phrase below runs in a **fresh chat with zero prior context**. The runbook bootstraps itself. Find-replace `<TASK_DIR>` per task; everything else is fixed.

| Trigger phrase | Runbook | What it does |
|---|---|---|
| `PIPELINE NEW — <TASK_ID>` (or `PIPELINE NEW REVIEW — <TASK_ID>`) | [Reference/Sessions/NEW.md](Reference/Sessions/NEW.md) | Create fresh task folder + scaffold the input files. CB mode scaffolds 1/2/3 + nudges to S0. Review mode scaffolds 1/2/3/5/6/7/8 + nudges to REVIEW. Accepts `<hex>` (auto-index) or `<index>_<hex>` (explicit). |
| `PIPELINE S0 — Tasks/<TASK_DIR>` | [Reference/Sessions/S0.md](Reference/Sessions/S0.md) | Extract PersonaBrief, split universe, build Universe_Index |
| `PIPELINE HARDNESS — Tasks/<TASK_DIR>` | [Reference/Sessions/HARDNESS.md](Reference/Sessions/HARDNESS.md) | Scan for Opus-4.8 stumping levers, produce Hardness_Plan and Stump Hypothesis |
| `PIPELINE S1 — Tasks/<TASK_DIR>` | [Reference/Sessions/S1.md](Reference/Sessions/S1.md) | Draft `5_Prompt.txt`, validate, two councils |
| `PIPELINE S1.5 — Tasks/<TASK_DIR>` + linter paste | [Reference/Sessions/S1.5.md](Reference/Sessions/S1.5.md) | Handle linter blocker: revise / justify / pivot |
| `PIPELINE S2 — Tasks/<TASK_DIR>` | [Reference/Sessions/S2.md](Reference/Sessions/S2.md) | Draft `6_Oracle_Events.txt`, validate, two councils |
| `PIPELINE S3 — Tasks/<TASK_DIR>` | [Reference/Sessions/S3.md](Reference/Sessions/S3.md) | Draft `7_Rubrics.json`, validate, two councils (heaviest pass) |
| `PIPELINE FINAL — Tasks/<TASK_DIR>` | [Reference/Sessions/FINAL.md](Reference/Sessions/FINAL.md) | Cross-artifact holistic council — answer-leakage scan, entity-drift check, lever-preservation end-to-end. **Required before platform upload.** |
| `PIPELINE S4 — Tasks/<TASK_DIR>` + verifier-fails paste | [Reference/Sessions/S4.md](Reference/Sessions/S4.md) | Classify verifier fails, draft AF justifications |
| `PIPELINE REVIEW — Tasks/<TASK_DIR>` | [Reference/Sessions/REVIEW.md](Reference/Sessions/REVIEW.md) | Review-type task intake: full assessment (validator + Council A + Council B + AUDIT on original + FINAL) + deep trajectory analysis (S4-style bucket classification on original trajectories if present) + initialize `changes.md` with all rows auto-marked Applied. Does NOT materialize 14/15 (v16 split — MATERIALIZE does that). |
| `PIPELINE MATERIALIZE — Tasks/<TASK_DIR>` | [Reference/Sessions/MATERIALIZE.md](Reference/Sessions/MATERIALIZE.md) | Apply Applied rows from `changes.md` to produce `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` / `_aux/REVIEW_prompt_draft.txt`, then re-run full gate set (validator + Council A + Council B + AUDIT + FINAL) on the corrected materialization. Runs AFTER REVIEW, BEFORE FEEDBACK. |
| `PIPELINE REDO — Tasks/<TASK_DIR>` | [Reference/Sessions/REDO.md](Reference/Sessions/REDO.md) | Reviewer redo: REVIEW done + fixes applied but trajectory failed on difficulty (pass@1 > 40%) or density (avg tool calls < 40). Archives candidate originals + rebuilds 5/6/7 from scratch as a full CB build. Also used when a CB's own task came back failing density / difficulty. |
| `PIPELINE COMPARE — Tasks/<TASK_DIR>` | [Reference/Sessions/COMPARE.md](Reference/Sessions/COMPARE.md) | Diff local `7_Rubrics.json` vs platform paste-back `10_Rubrics_Platform.json` to catch silent platform-side mutations |
| `PIPELINE AUDIT — Tasks/<TASK_DIR> --phase {prompt\|oe\|rubrics\|all}` | [Reference/Sessions/AUDIT.md](Reference/Sessions/AUDIT.md) | Veteran QC second-opinion under the STRICTEST possible interpretation (5/5 only, density bar 50+, every "should" read as "must"). **Auto-fires inline from S1/S2/S3 (and S1.5 on prompt revise, REVIEW on corrected materialization)** as the per-phase exit gate. Also available **on-demand** in a fresh chat via this trigger for high-stakes pre-upload sanity checks, post-platform-rejection retros, or post-pipeline-change re-audits. Read-only. Not a substitute for FINAL — complementary. |
| `PIPELINE FEEDBACK — Tasks/<TASK_DIR>` | [Reference/Sessions/FEEDBACK.md](Reference/Sessions/FEEDBACK.md) | **(REVIEW flow only.)** Write `13_Feedback.txt` rating the candidate's ORIGINAL submission against the QC SPEC baseline. Strict input allowlist — reads ONLY originals 5/6/7 + 3 (universe) + QC spec docs; explicitly DENIES `changes.md`, `14_*`, `15_*`, `_aux/Council_Reports/*`, REVIEW draft. Evaluates against spec baseline ONLY (NOT our internal exceeds-spec bar like 50+ density / strictest AUDIT — those are project policy, not spec requirements). Runs AFTER REVIEW, BEFORE CLOSE. Lifted into a separate phase because inline-with-REVIEW feedback consistently drifted to rating the fixed task instead of the original. |
| `PIPELINE CLOSE — Tasks/<TASK_DIR>` | [Reference/Sessions/CLOSE.md](Reference/Sessions/CLOSE.md) | Final read-only sanity check. Audits required artifacts + FINAL verdict + trajectory verdict; refuses to greenlight if anything is missing. Nudges to append cross-task learnings before exit. |

## Knowledge flow + file nomenclature

For the cross-cutting dependency chart (which phase reads / produces what), file-naming conventions (`<phase>_<council>_<purpose>.md`, `AUDIT_<phase>.md`, `S4_<bucket>.md`, etc.), single-source ownership map (Fact_Ledger SSOT, Universe_Split SSOT, etc.), and the cross-phase re-run map (when an artifact changes, what downstream phases must re-run), see [`Reference/Knowledge_Flow.md`](Reference/Knowledge_Flow.md). A fresh-chat agent invoking any phase should read that doc + the phase runbook to know every file path it will touch.

## Project layout

```
MCP_Eval_V3/
├── AGENTS.md                       # this file — entry point
├── Reference/                      # format cards + lever catalog + session runbooks
│   ├── Hardness_Playbook.md
│   ├── Prompt_Format.md
│   ├── OE_Format.md
│   ├── Rubric_Format.md
│   ├── Similarity_Pivot.md
│   ├── Linter_Playbook.md
│   ├── Council_Protocol.md
│   ├── Strict_Convention_Inventory.json
│   ├── OE_Convention_Inventory.json
│   └── Sessions/
│       ├── NEW.md  S0.md  HARDNESS.md  S1.md  S1.5.md  S2.md  S3.md  FINAL.md  S4.md
│       ├── REVIEW.md  MATERIALIZE.md  REDO.md  COMPARE.md  AUDIT.md  FEEDBACK.md  CLOSE.md
├── Validators/
│   ├── universes.py                # multi-universe registry + detect_universe() + FRAMEWORKS profiles (constants SSOT)
│   ├── validate.py                 # phase-aware validator (prompt | oe | rubrics | all | injection | submission_gate)
│   ├── v4_gates.py                 # V4 deterministic gates (Evals_starpm 0 + 5); injection presence-gated for all universes
│   ├── qc_verdict.py               # deterministic QC verdict engine (parse/classify/selftest/audit/feedback), 138/138 across the 5 bucket corpora
│   ├── check_regression.py         # zero-regression gate: anchors + frozen report hashes (7 tasks / 3 v3-family universes)
│   ├── test_regression_anchors.py  # 81 behavior anchors + --dead-gate vacuity self-check
│   ├── test_memory_bounds.py       # 384 MiB peak-RSS ceiling on the export scan + --self-check mutants (rule 33)
│   ├── regression_baseline/        # vendored wave-0 hashes + reports + ROUTING_DECISIONS.md + V4_ENFORCEMENT_AUDIT.md
│   ├── check_source_sync.py        # repo spec surfaces vs extracted upstream drop (catches upstream releases hash pins cannot see)
│   ├── source_sync_deviations.json # documented repo-vs-upstream divergences (flavor corrections)
│   ├── check_eval_hashes.py / eval_file_hashes.json      # eval spec pinning (repo-side drift)
│   ├── check_qc_corpus.py / qc_corpus_hashes.json        # labeled QC ground-truth pinning; a green qc_verdict selftest does NOT prove the corpus is current
│   ├── check_tool_catalog.py / tool_catalog_hashes.json  # tool catalog pinning
│   ├── new_task.py                 # PIPELINE NEW scaffolder (per-universe templates; V4 dual-model shape)
│   ├── parse_trajectories.py       # pass@1 + density (flat + per-model layouts)
│   ├── phase_ready.py              # per-phase input gating (V4-aware: 8a/8b, injection artifacts)
│   ├── close_task.py               # CLOSE audit (V4-aware artifact sets)
│   ├── split_universe.py           # per-task data.py wrapper
│   ├── build_universe_index.py     # per-task summaries (registry tz/today)
│   ├── build_fact_ledger.py        # per-task atom surface (emails, amounts, dates, ids, accounts, personas)
│   ├── build_graph_report.py       # per-task compact density map
│   ├── build_feasible_surface.py   # feasible-action surface for grounding
│   ├── verify_universe_atoms.py    # per-universe claim/atom verification
│   ├── calc_similarity.py          # cross-task similarity gate
│   ├── aggregate_verdicts.py       # council verdict rollup
│   ├── check_justification.py      # linter/AF justification hygiene (+ grading-process meta, em-dash, cross-criterion refs)
│   ├── check_export_freshness.py   # content-hash pin for platform-pasted S4 inputs (rule 15)
│   ├── check_criterion_dependencies.py  # passing-cell audit: dependent passes where antecedent fails (rule 17)
│   ├── check_oe_rubric_sync.py     # OE decompose directives vs rubric carriers (rule 14 mirroring)
│   ├── check_rubric_antipatterns.py # criterion-construction anti-patterns, ex-hand-run greps (rule 18); A5/A6 = rules 31-32
│   ├── check_ordering_coverage.py   # prompt orders actions but no Process rubric grades it (rule 23)
│   ├── check_qc_binary.py           # the 10 binary QC sub-dimensions in one gate (rule 26)
│   ├── check_rubric_signal.py       # per-criterion discrimination; weak-assertion cut list (rule 28)
│   ├── check_criterion_stability.py # Cohen's kappa across gradings; flips = wording defects (rule 29)
│   ├── check_council_yield.py       # findings per KB of council prose (rule 20)
│   ├── check_verification.py       # per-phase verification doc gate
│   ├── compare_rubrics.py          # local vs platform-paste-back rubric diff -> _aux/Compare_Report.md
│   ├── make_fill_script.py         # generates a browser-console rubric form filler from 7_Rubrics.json
│   ├── universe_data_source.py     # contract-aware universe data accessor (per_task_json vs base_export_plus_changelog)
│   ├── test_registry_schema.py     # UNIVERSES entry-shape gate: CORE keys required, OPTIONAL declared, no UNRESOLVED sentinel
│   ├── check_capability_registry.py # KEP-2558-style linter: FRAMEWORKS vs its consumers (C1 consumers, C2 SSOT, C3 flag parity, C4 silent-inherit)
│   ├── test_detect_universe_characterization.py # approval test pinning detect_universe output + raw score vectors
│   ├── test_score_extraction.py    # mutation suite pinning the auditor-form score extractor; bar is never-silently-optimistic
│   ├── check_hydration.py          # gitignored multi-GB payload: present? right service count? sha256 matches? fails loudly, not cryptically
│   ├── check_persona_acl.py        # HarmonyGames persona-ACL gate (ACL-1 roster resolution, ACL-2 catalog-infeasible writes); WIRED into validate.py --phase prompt (rule 32); SKIPs when acl_gate=false
│   ├── test_signal_exclusivity.py  # cross-universe signal collisions + pinned negative/positive detection fixtures
│   ├── universe_data_source.py     # contract-aware universe data accessor (per_task_json vs base_export_plus_changelog)
│   └── check_pipeline_wiring.py    # audits the pipeline's own citations: paths, scripts, flags, phases, imports, orphans (W9), duplicated logic (W10), tool vocab (W11)
├── Brookfield_Base_Universe/       # STALE except 8_Server_Tools_Details.json + 2_Persona_Briefs.md
│   ├── 1_Summary.md ... 7_*.md     # stale reference, do not trust over per-task data
│   ├── 2_Persona_Briefs.md         # stable per-version (personas don't change per task)
│   ├── 8_Server_Tools_Details.json # STABLE — the tool / parameter reference
│   ├── 9_Universe_Schema.json
│   └── Data/                       # stale pre-baked universe split — do NOT use for per-task work
├── Docs/                           # V3 framework specs and guidelines (stable)
├── Evals/                          # phase eval specs (Prompt / OE / Rubrics / Verifier-Fails)
├── Guide/                          # how-to docs and verifier-fails template
├── QC_Tasks/
│   ├── V3_Tasks/                   # on-framework reference tasks (Task11..Task14)
│   ├── V2_Tasks/                   # legacy V2/Keystone — study craft, not framework
│   ├── V3_Buckets/                 # Brookfield labeled QC verdict ground truth (16 tasks, 4 buckets)
│   ├── V3.1_Buckets/               # KeyStone labeled QC verdict ground truth (16 tasks, 4 buckets)
│   ├── V2.1_Buckets/               # MoveOps labeled QC verdict ground truth (80 tasks, 4 buckets)
│   └── V4_Tasks/                   # StarPM labeled QC verdict ground truth (16 tasks, 4 buckets)
│                                   # all five corpora: qc_verdict.py selftest == bucket-correct 138/138 (16+16+80+16+10)
├── Tasks_Template/                 # Brookfield platform-paste template (upstream-synced: 4_Changelog + 9_Universe_inject)
├── Tasks_Template_keystone/        # KeyStone per-universe template (upstream-synced)
├── Tasks_Template_moveops/         # MoveOps per-universe template (upstream-synced)
├── Tasks_Template_starpm/          # StarPM V4 dual-model template (8a/8b, per-model Agent_Responses, dispute placeholders)
├── rubric-json-viewer/             # local rubric JSON viewer utility
├── Tasks/                          # live tasks
│   ├── <TASK_DIR>/                 # per-task work
│   │   ├── 1_Business_Function.txt … 9_Universe_inject.sql  # user-pasted + pipeline-produced (1-9 as before)
│   │   ├── 10_Rubrics_Platform.json   # optional, user pastes for COMPARE
│   │   ├── 13_Feedback.txt            # REVIEW flow only — candidate-facing rating
│   │   ├── 14_Updated_Oracle_Events.txt  # REVIEW flow only, IFF OE fixes Applied
│   │   ├── 15_Updated_Rubrics.json       # REVIEW flow only, IFF rubric fixes Applied
│   │   ├── PersonaBrief.txt
│   │   ├── changes.md              # review-tasks only
│   │   ├── Agent_Responses/        # 6 trajectory JSONs (user-pasted)
│   │   └── _aux/                   # pipeline working directory
│   │       ├── Universe_Split/     # per-task universe split
│   │       ├── Universe_Index/     # service_inventory, entities_personas, key_facts, today_horizon, accounts_per_entity, graph_report
│   │       ├── Fact_Ledger.json    # per-task verifiable atom surface (emails, $, dates, IDs, accounts, personas)
│   │       ├── Hardness_Plan.md
│   │       ├── S0_Setup_Report.md
│   │       ├── Linter_Decision.md
│   │       ├── Linter_Justifications.md
│   │       ├── Council_Reports/
│   │       ├── Validator_Reports/
│   │       └── Reasoning/
│   └── _meta/                      # cross-task learning logs
│       ├── Similarity_Log.md
│       ├── Linter_Justifications.md
│       ├── Hardness_Patterns_Log.md
│       └── Stump_Hypotheses.md
└── data.py                         # smart forwarder — routes per-task input to Validators/split_universe.py
```

## Universe constants (multi-universe — v21)

Pipeline supports **five universes**. Detection is automatic via `detect_universe()` in `Validators/universes.py` (writes `_aux/Universe.txt` at S0). All validators + council prompts + runbooks read constants via the `Validators/universes.py` registry. **Eleven per-universe branches remain in code** (ten `universe == "<name>"` plus one negated `universe != "starpm"` in `v4_gates.py`, which an `==`-only grep cannot see) and are deliberate, not oversights: `build_fact_ledger.py` x2, `build_universe_index.py` x1 and `validate.py` x1 gate QuickBooks/Airtable handling that HarmonyGames has no service for; `build_graph_report.py` x3 are StarPM-shaped report sections every other universe correctly falls through; `verify_universe_atoms.py` x3 dispatch universe-specific claim verifiers (TRID, PHMSA). Everything genuinely shared - timezone, persona tagging, ID pattern sets, identifier shapes, grounding specs, the weekend-comms rule - routes through declared registry keys (`index_tz_from_registry`, `index_internal_by_domain`, `id_pattern_set`, `weekend_comms_rule`). The eleventh is `v4_gates.py`'s `if universe != "starpm": return`, which skips **F7 and F9**. F7 skipping is fine, but **F9 (UNRECONCILED_FUTURE_EVT) is therefore unavailable for HarmonyGames even though HG carries `gcal` in both `services` and `acl_scoped_services`**, so hard rule 13's every-service Calendar sweep is **manual** for HG until F9 is generalised (it reads `gcalendar.gcalendar_events.json` and depends on `entity_vals` that only F7 populates). When adding a universe, prefer a declared registry key over a name comparison, and grep for `!=` as well as `==`.

### Brookfield CPAs & Advisors (default — public accounting / business advisory)

- **Base path:** `Brookfield_Base_Universe/` · Tool catalog: `8_Server_Tools_Details.json` · Persona briefs: `2_Persona_Briefs.md`
- **Universe today:** 2026-06-12 (US/Eastern). Confirm from `_aux/Universe_Index/today_horizon.json`.
- **Three client entities:** `brookfield` (the firm itself), `northstar_legal` (law firm), `acme_cloud` (SaaS).
- **Account-number trap (HARDCODED LANDMINE):** `105000` is Cash-Trust on Brookfield, IOLTA on Northstar, Short-term Investments on Acme. `120000` is Client Cost Advances on Northstar, Deferred Commissions on Acme, absent on Brookfield. Always query `oracle_gl.ogl_accounts WHERE account_number=N AND entity_id=E` — never trust prose role labels.
- **Records Vault retention codes:** `AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, `INDEFINITE`. Never `SOX_7Y` or `SEC_PERMANENT`.
- **Classifications:** `internal` (default), `restricted` (elevated role required), `public` (defined but unused).
- **Slack channels:** C001 #general · C002 #water-cooler · C003 #announcements · C004 #client-onboarding · C005 #monthly-close-coordination · C006 #tax-prep-and-filings · C007 #audit-engagements · C008 #compliance-and-registrations · C009 #cash-management-and-banking · C010 #vendor-bills-and-ap · C012.
- **Parameter traps:** email + messaging use `content` (not `body`). Slack uses `payload` (not `text`). Linear comments use `issueId` + `body`. Records Vault upload uses `content_b64` (not `file`/`data`).
- **JE lifecycle:** `draft → submitted → approved → posted → reversed`. Minimum 300 seconds between transitions. Closed-period posting requires `late_post_authorization_id`.
- **Services:** oracle_gl, sap_subledger, blackline, records_vault, airtable, linear, email, slack, contacts.
- **Docs:** `Docs/` · Evals: `Evals/` · QC ref: `QC_Tasks/V3_Tasks/`.

### Keystone Mortgage Partners (v18 — residential mortgage brokerage)

- **Base path:** `Mortgage_Base_Universe/` · Tool catalog: `6_Server_Tools_Details.json` · Persona briefs: `3_Persona_Briefs.md`
- **Single entity:** `keystone` (30-employee mortgage brokerage in Charlotte, NC).
- **NO account-number trap** (loan-based universe, not GL-based). `mortgage_los.loans` is source of truth for loan-level data; CRM holds the marketing / referral funnel only.
- **TRID timing (HARDCODED LANDMINE):** Loan Estimate must be sent within 3 business days of application; Closing Disclosure must be delivered 3 business days before closing. Query `mortgage_los.disclosures` for actual sent_date vs application_date / closing_date.
- **Departed-employee trap:** Marcus Webb (scenario_7da8f37a — evidence of pre-resignation data exfiltration). Do not author tasks expecting Marcus active.
- **NO Records-Vault-style retention codes / classifications** (mortgage industry uses filesystem PDFs without explicit retention metadata).
- **Slack channels:** C001 #general · C002 #loan-processing · C003 #closings · C004 #compliance-alerts · C005 #rate-watch · C006 #sales-pipeline · C007 #random · C008 #it-support.
- **Loan statuses:** `application → conditional_approval → processing → underwriting → clear_to_close → closed` (or `denied` / `withdrawn`).
- **Condition statuses:** `outstanding` → `cleared`.
- **Parameter traps:** email + messaging use `content` (not `body`). Slack uses `payload` (not `text`). `mortgage_los_add_condition` requires `loan_id`. `stripe_create_charge` requires `amount`.
- **Services:** mortgage_los, stripe, filesystem, crm, quickbooks, email, slack, contacts.
- **Docs:** `Docs_keystone/` · Evals: `Evals_keystone/` · QC ref: `QC_Tasks/V3.1_Tasks/`.

### MoveOps Inc. (v20 — B2B remote-work relocation services, V2.1 framework)

- **Base path:** `MoveOps_Base_Universe/` · Tool catalog: `6_Server_Tools_Details.json` · Persona briefs: `2_Persona_Briefs.md`
- **Universe today:** 2026-04-26 (US/Pacific). Confirm from `_aux/Universe_Index/today_horizon.json`.
- **Single entity:** `moveops` (21-employee B2B relocation startup in San Francisco).
- **NO account-number trap** (operational universe, not GL-based). `airtable.tblRelocations01` is source of truth for relocation state; CRM holds the deal / engagement funnel only.
- **PHMSA DOT hazmat compliance (HARDCODED LANDMINE):** hazmat shipments (cryogenic equipment, Class 3B lasers, chemical samples) require a SIGNED DOT certificate from the freight carrier (Swift / Heartland email thread + Airtable record). Verbal driver confirmation does NOT count. When auditing a hazmat-related claim, verify the Airtable relocation record AND the carrier email thread show actual signed documentation.
- **Marcus Webb identity:** Marcus Webb is a BrightLoop Analytics senior analyst (CLIENT employee at `marcus.webb@brightloopanalytics.com`), DISTINCT from the KeyStone departed-employee Marcus Webb. Same name, different person, different universe — do NOT carry KeyStone's departed-employee logic over.
- **Airtable-vs-CRM source-of-truth trap:** relocation / vendor / coordinator / stipend state lives in Airtable (`tblRelocations01`, `tblStipends00001`, `tblClientAccts01`). CRM holds the deal/engagement funnel. Never trust CRM as source for relocation state.
- **Vendor cross-reference (Heartland Q1 invoice):** the Heartland Q1 2026 invoice has multiple cancelled / reassigned moves billed in error. Any vendor-payment-dispute task must cross-reference invoice line items against `tblRelocations01.vendor + status`, NOT trust the invoice prose.
- **ExpenseBot pilot bugs:** the stipend auto-categorizer has known policy-config bugs for Vectral and Mosaic (exclusion checks, amount validation, duplicate hash detection). When verifying stipend approval correctness, query Airtable stipend records against the policy + Dmitri's audit findings.
- **NO Records-Vault-style retention codes / classifications.**
- **Slack channels:** C001 #general · C002 #customer-engagement · C003 #engineering · C004 #executive · C005 #finance · C006 #operations · C007 #customer-support · C008 #announcements · C009 #root-cause-aws-spike.
- **Parameter traps:** email + messaging use `content` (not `body`). Slack uses `payload` (not `text`). `linear_create_issue` uses `team` (NOT `teamId`! — differs from Brookfield). `linear_create_comment` uses `issueId` + `body`. `crm_create_engagement` requires `engagement_type` + `body`. `airtable_update_records` requires `base_id` + `table_id`. `quickbooks_create_customer` requires `DisplayName` (PascalCase).
- **Services:** airtable, calendar, contacts, crm, email, linear, public, quickbooks, slack.
- **Business functions (5):** Operations 25% · Customer Engagement / Support 30% · Engineering 20% · Finance 15% · Executive 10%.
- **Framework version:** V2.1 (older framework than V3 — some rubric / OE conventions may differ slightly from V3 Brookfield + V3.1 KeyStone; QC sub-dim scoring rules in `Docs_moveops/2_Rubrics_V3_Guidelines.md` may have minor deltas — read it before applying validator behavior to MoveOps tasks).
- **Docs:** `Docs_moveops/` · Evals: `Evals_moveops/` · QC ref: `QC_Tasks/V2.1_Tasks/`.

### Star Property Management (v21 — residential property management, V4 framework)

- **Base path:** `StarPM_Base_Universe/` · Tool catalog: `7_Server_Tools_Details.json` (NOTE: prefix **7**, unlike Brookfield's 8) · Persona briefs: `2_StarPM_PERSONA BRIEFS.md` (space in filename) · Schema: `8_Universe_Schema.json`
- **Universe today:** 2026-07-01 (America/Chicago). Active window 2026-05-01 to 2026-07-01. Confirm from `_aux/Universe_Index/today_horizon.json`. (The stale "Jun 12 US/Eastern" string inside `Docs_starpm/7_QC_Spec_Doc1.json` is superseded by `Docs_starpm/6_Prompt_Relative_Time_Updates.md` and the evals.)
- **Single entity:** `starpm` (Star Property Management, LLC — San Antonio TX multifamily property manager, domain `starpm.com`). 13 authoring personas p_000..p_014 (all `@starpm.com`) + ~47 NPCs.
- **V4 framework deltas (vs V3):** dual-model verification (Opus 4.8 + Gemini): `8a_Verifier_Fails_Opus.txt` + `8b_Verifier_Fails_Gemini.txt` + `Agent_Responses/{Opus,Gemini}/Run1-6_Trajectory.json`; injection is a first-class artifact (`9_Universe_inject.sql` + `4_Changelog.json`) gated by `validate.py --phase injection` (Evals_starpm/0, 7 hard gates + difficulty >= 3.5); pre-upload gate `validate.py --phase submission_gate` (Evals_starpm/5, defect families F1-F6, any single defect = FAIL); QC feedback/dispute artifact chain `9_QC_Feedback.txt` / `10_PT_Dispute_To_QC_Feedback.txt` / `11_Final_QC_Validation_On_PT_Dispute.txt` handled by `Validators/qc_verdict.py` (parse / classify / selftest / audit / feedback).
- **Density:** design target 40+ avg tool calls (Docs_starpm/1: "AVERAGE TOOL CALL COUNT OF ALL AGENT RUNS MUST BE 40+"); QC-spec fail floor is 15. pass@1 <= 40% unchanged.
- **NO account-number trap, NO retention codes, NO classifications** (property-management universe, not GL-based).
- **Near-duplicate decoy files (HARDCODED LANDMINE):** `invoice-2026-419.pdf` vs `invoice-2026-419-287.pdf`; `invoice-BILL-2026-0392.pdf` vs `invoice-BILL-2026-0392-920.pdf`; `agreement-...-tanya-mitchell.pdf` vs `-2.pdf`; `report-laspalmas-8d-qc-inspection.pdf` vs `-2.pdf`. Tasks must cross-check WHICH file is authoritative against Airtable/QuickBooks records, never trust filename prose.
- **Tanya Mitchell contradiction (LANDMINE):** reasonable-accommodation intake documents vs eviction-track make-ready records coexist — tasks touching her unit must reconcile the accommodation-vs-eviction state from the records, not assume either.
- **Cross-property "Unit 14" ambiguity (LANDMINE):** Unit 14 exists at multiple properties (Rio Bend, Sunset Ridge, Tanya Mitchell eviction track) — always disambiguate by property.
- **Airtable is source of record** for make-ready/unit/property state; Linear is secondary (mirror tickets). Never trust Linear over Airtable.
- **Slack channels:** C001 #maintenance · C002 #leasing · C003 #general · C004 #make-ready · C005 #vendors · C006 #owner-relations · C007 #budget-review · C008 #applications.
- **Parameter traps (DIFFER from the other four universes):** Slack `slack_send_message(channel_id, message)` — text param is `message`, NOT `payload`/`text`. Gmail is **draft-only**: `create_draft(to[], subject, body)` — `body`, NOT `content`, and there is NO send tool. Linear upsert `save_issue(..., team, ...)` (NOT `teamId`) / `save_comment(issueId, body)`. Airtable camelCase `baseId`/`tableId`/`records[]`. HubSpot `manage_crm_objects(object_type, action, objects[])`. QuickBooks creates take a single `properties` envelope.
- **Services:** airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack.
- **Business functions (5):** Property Operations 32% · Portfolio Coordination & Owner Relations 20% · Leasing & Applicant Intake 20% · Maintenance & Repairs 18% · QC & Field Services 10%.
- **Framework version:** V4. QC verdict ground truth: `QC_Tasks/V4_Tasks/` (16 labeled tasks in 4 buckets: QC_Passed / QC_True_Fails / QC_Non_Fails / QC_False_Fails_PT_Dispute_Accepted — note their CONTENT is Brookfield-fixture flavored; they are verdict-logic ground truth, not StarPM universe facts). `Docs_starpm/13_QC_Companion.md` is Brookfield-contaminated — do NOT treat as StarPM SSOT (see `Validators/regression_baseline/ROUTING_DECISIONS.md`).
- **Docs:** `Docs_starpm/` · Evals: `Evals_starpm/` (6 evals: adds 0_Injection_Quality + 5_Submission_Gate) · Guide: `Guide_starpm/` · Task template: `Tasks_Template_starpm/` · QC ref: `QC_Tasks/V4_Tasks/`.

### Harmony Games (v22 — mobile game studio, HG framework)

- **Base path:** `HarmonyGames_Base_Universe/` · Tool catalog: `6_Server_Tools_Details.json` (NOTE prefix **6**, **SHARED** with KeyStone/MoveOps: the 2026-08 drop renumbered HG `5_` -> `6_`, so HG no longer has a distinct prefix. Brookfield 8_, StarPM 7_, KeyStone/MoveOps/HarmonyGames 6_) · Persona briefs: `2_Persona_Briefs.md` · Schema: `7_Universe_Schema.json`
- **Universe today:** 2026-02-28 (America/Chicago). Five independent sources agree and, unlike StarPM, the QC-spec JSON is **not** stale. Active injection window 2026-01-01 to 2026-02-28.
- **Single entity:** `harmonygames` (Harmony Games, founder-led remote-first mobile game studio, domain `harmonygames.co`). 17 authoring personas in `4_Persona_ACL_Roster.json` (flat list; `persona_key` / `name` / `email` / `role` / `department`).
- **Framework `hg` — a genuine hybrid, NOT a successor to v4.** Single-model verification like the V3 family (`8_Verifier_Fails.txt`, flat `trajectory-run-{1..6}.json`) PLUS V4's injection + submission_gate phases (`Evals_harmonygames/0` and `/5`). The framework key is deliberately `hg` rather than `v5`, because a version ordinal would imply a successor relationship to v4 that does not exist.
- **Density is THREE distinct thresholds, normatively separated** (`Docs_harmonygames/7_QC_Spec_Doc1.json:14`): authoring target 40+ calls AND 3+ services; prompt-eval hard gate >15 **necessary** calls AND 2+ services AND multiple meaningful writes AND information friction; trajectory QC floor >=15 average. `set_acting_user`, ACL-denied reads and retries against inaccessible records count toward **none** of them.
- **pass@1 <= 40%** (0-2 of 6 completed runs). **Error rate** fails at 3+ of 6 not completing; an empty trajectory file is an errored run, excluded from rubric-fail counts.
- **Injection difficulty floor is 2.5**, not StarPM's 3.5, over seven dimensions with **eight** fail conditions.
- **Rubric balance is a flat 40% Process CAP, binary, and zero Process is valid.** There is **no** Outcome-majority requirement here — that is the older framework's rule and it still governs the other four (see hard rule 8).
- **Rubric `category` is a stored 4-value enum:** `Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, `Process`. This is rule 24's `sub_category` already native to the schema. The text field is `title`, never `criterion`.
- **Severity is the PRE-swap ordering, the reverse of StarPM:** Overly Broad = **Moderate**, Overly Specific = **Minor**. Percentage bands are identical to the other universes.
- **QC spec is 7 dimensions / 38 sub-dimensions, 18 of them BINARY** (Brookfield: 5 / 24 / 10). Two dimensions have no counterpart elsewhere: `Authority and Thresholds` and `Injection`. `Alignment with Today's Date` **left** the binary set here.
- **Model under test is Claude Opus 4.7**, not 4.8 — the one place hard rule 1 is universe-scoped.
- **Working directory is `Generated_Tasks/`**, not `Tasks/`.
- **Gmail is READ-ONLY (LANDMINE):** all 27 `gmail_*` tools read, label or trash. There is NO send, reply, compose or draft tool — weaker even than StarPM, which has `create_draft`. "Email the vendor" is not an available action and a rubric requiring one is ungradeable. Snowflake is query/read-only.
- **Two Slack send tools with DIFFERENT text params (LANDMINE):** `slack_send_message(channel, **text**)` and `slack_conversations_add_message(channel_id, **payload**)`. Both valid. Unique to this universe.
- **Weekend rule vs today (LANDMINE):** routine Slack/Gmail business communication dated on a weekend is a temporal violation, and today (2026-02-28) **is itself a Saturday** and the last day of February. It is also mid-Q1, so "Q1 close" or "Q1 results are final" framing is incoherent.
- **Persona emails are irregular by design (LANDMINE):** `arthur_blake` -> `blake@`, `julia_lawson` -> `jlawson@`, `martin_walsh` -> `martin.walsh@`. Never construct, normalize or infer an email from a name; resolve via `4_Persona_ACL_Roster.json`.
- **Persona ACL is a first-class gate with no analogue in the other four.** Seven services apply persona-scoped read filtering (gmail, gcal, gdrive, gdocs, gsheets, gslides, slack); six are unscoped (contacts, github, snowflake, trello, linear, confluence). **Persona ACL does not govern writes** (`Docs_harmonygames/14_Persona_ACL.md:17`), and `:134` forbids making an ACL-based write denial necessary to a prompt, Oracle Event or rubric. A read under the wrong acting identity is an **Excluded** execution, which is a third trajectory disposition beyond pass/fail and must be subtracted before pass@1 and density are computed.
- **Slack has 985 channels / 218 users** — channel IDs are NOT enumerable against a whitelist, unlike the C001..C0NN sets elsewhere. `slack_channels` is deliberately an empty set in the registry, meaning "do not whitelist-validate".
- **Parameter traps:** `gdocs_create_document` takes `bodyText` (not `body`/`content`); `linear_create_issue` takes `team` (not `teamId`, matching MoveOps); `linear_create_comment` takes `issueId` + `body`.
- **Services (13, ZERO overlap with the other four universes):** confluence, contacts, gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, snowflake, trello. Firebase, BigQuery, App Store Connect, Airtable, QuickBooks and Stripe are business topics only, never directly queryable.
- **Business functions (6):** Engineering & Live-Ops 25% · Product & Design 20% · Growth/UA/Marketing 15% · Founders/Exec/Strategy 15% · Finance/Legal/HR/Ops 15% · Analytics & Data 10%.
- **Payload boundary is INVERTED (architectural).** For the other four, `3_UniverseDataForThisTask.json` carries the data and `*_Base_Universe/Data/` is stale (hard rule 3). Here that per-task file is a 940-byte **contract descriptor** ("Do NOT extract or paste the full universe data") and `Services_Data/` IS the source of truth — 8.1 GB, ~314k files, a 359 MB JSON and four nested git packs. Only `4_Changelog.json` is extracted, and only when the task injects; the query is `SELECT 'public._changelog', to_jsonb(t) FROM public._changelog t`. It is therefore **gitignored behind a hydration pointer** (`HarmonyGames_Base_Universe/Services_Data/README_HYDRATE.md`) rather than vendored. The repo's first `.gitignore` exists for this.
- **Long-horizon class:** a task with at least one run in the 500-1000 tool-call band, governed by `Docs_harmonygames/13_Long_Horizon_Task_Guidelines.md`.
- **QC corpus is 10 tasks in a 4/4/2/0 split** (QC_Passed 4, QC_Non_Fails 4, QC_True_Fails 2, QC_False_Fails_PT_Dispute_Accepted **0**), NOT the 16 that `qc_verdict.py` documents as required. The `_HG` suffix is the discriminator; `Legacy_Other_Universes/` holds other universes' tasks and must never enter an HG corpus count.
- **Docs:** `Docs_harmonygames/` (note: filenames DROP the `V3` infix — `2_Rubrics_Guidelines.md`, `3_Rubrics_One_Pager.md`) · Evals: `Evals_harmonygames/` (6 evals, 0-5) · Guide: `Guide_harmonygames/` · Template: `Tasks_Template_harmonygames/` · QC ref: `QC_Tasks/V5_HG_Buckets/`.

#### Known HarmonyGames deviations (pinned, not bugs to fix silently)

> The HG-U numbering is deliberately **sparse** (U2, U3, U5, U6, U8, U10) because it mirrors the upstream audit's own numbering. The gaps are not missing rows. Do not renumber: existing citations depend on these IDs.

| ID | Deviation |
|---|---|
| HG-U2 | `QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/` is cited by **all six** evals (incl. mandatory conditional pre-reads in `Evals_harmonygames/4` and `/5`, and as the sole BATCH/`BIND[]` exemplar) but **does not exist** anywhere in the drop. The 2026-08 drop dropped the citation from `Docs/README.md` only; the evals still carry it. Pinned deviation, never aliased to another task. |
| HG-U3 | Every shipped task's `3_UniverseDataForThisTask.json` hardcodes a stale `MCP_Eval_V2_HarmonyGames/` base path. The data-contract loader must tolerate it. |
| HG-U5 | Corpus is 10 tasks with one empty bucket, against `qc_verdict.py`'s documented "16/16 required". |
| HG-U6 | The 60-rubric project cap flags `QC_Passed/Task1_..._HG`, which carries 80 criteria and passed upstream QC. Authority for flagging it anyway is an explicit operator ruling, not the upstream spec. |
| HG-U8 | The HG spec carries **no date-stamped amendment markers** (Brookfield's is dense with 05/05, 05/22, 06/09). Hard rule 25's "later-dated entry wins" tiebreaker is therefore **inert** for this universe. |
| HG-U11 | `v4_gates.py`'s `universe != "starpm"` guard skips F9 (UNRECONCILED_FUTURE_EVT) for HarmonyGames despite HG having `gcal`. Hard rule 13's Calendar sweep is therefore MANUAL for HG. Pinned, not silently accepted. |
| HG-U12 | The `v4_gates` persona/address check is silently inert for brookfield, keystone and moveops: their registry `personas` is empty, so `and personas` short-circuits. Only starpm and harmonygames exercise it. Recorded rather than fixed - populating three more persona maps would change three universes' output, which this integration must not do. |
| HG-U10 | All six evals run longer than `Evals_starpm`. (The old "`11_Taxonomy.md` is 159 lines against StarPM's 799" clause is **retired**: the 2026-08 drop rewrote it 7,916 -> 37,588 bytes.) The F1-F6 submission-gate family **names** match V4 but the trigger conditions do **not** transfer; `hg_f1_f6` must be authored from HG's own eval. |


### Universe detection

- Auto-detected per-task by `detect_universe()` in `Validators/universes.py` (signals: service names + persona names + universe data file contents). Highest signal-score wins; ties default to brookfield.
- Cached to `_aux/Universe.txt`. Override by manually editing the file (single word: `brookfield`, `keystone`, `moveops`, `starpm`, or `harmonygames`).
- Every validator / council / AUDIT / FINAL reads `_aux/Universe.txt` and routes constants/paths accordingly.

## Where to start

- **Brand-new task (CB creation):** `PIPELINE NEW — <TASK_ID>` → paste 3 inputs → `PIPELINE S0 — Tasks/<TASK_DIR>`
- **Brand-new task (review-type, deliverables prefilled):** `PIPELINE NEW REVIEW — <TASK_ID>` → paste 7 inputs → `PIPELINE REVIEW — Tasks/<TASK_DIR>`
- **Already-scaffolded task, continuing mid-pipeline:** invoke the next-trigger phrase the previous phase's STOP gate printed
- **Stuck on a linter block:** `PIPELINE S1.5 — Tasks/<TASK_DIR>` + paste the linter output
- **Verifier results came back:** `PIPELINE S4 — Tasks/<TASK_DIR>` + paste verifier fails
- **Wrapping up:** `PIPELINE CLOSE — Tasks/<TASK_DIR>` (read-only final audit)

## Anti-patterns (this project)

- Reading anything in `Brookfield_Base_Universe/` other than `8_Server_Tools_Details.json` or `2_Persona_Briefs.md` and treating it as current per-task truth.
- Writing to the shared `Brookfield_Base_Universe/Data/` directory (corrupts parallel work). Use `data.py` (smart forwarder) or `Validators/split_universe.py` instead — both route output to per-task `_aux/Universe_Split/`.
- Adding process rubrics without applying the three-condition test.
- Using em-dashes or "at least N" without prompt mandate.
- Mentioning guides / specs / frameworks in linter justifications or AF justifications.
- Editing the per-task universe to "make room" for a hardness lever.
- Shipping a deliverable that hasn't cleared both councils.

## Declared-but-unwired capability flags

**`injection_difficulty_floor` is now WIRED**: `v4_gates.py` reads it from the framework profile and prints the universe's own floor (HG 2.5, StarPM 3.5) instead of a hardcoded 3.5. The composite score remains a council judgment; what is wired is the threshold the council is told to apply.

`FRAMEWORKS` declares 28 flags per profile and `check_capability_registry.py` C3 enforces that
all five profiles declare the same set. Declaring a flag is NOT the same as enforcing it, and
C3's "all profiles in parity" can read as though it were. The following are declared and read by
no production consumer today. They are recorded here so the registry stops implying enforcement
that does not exist.

| flag | why it is declared | status |
|---|---|---|
| `density_prompt_gate_calls` | prompt-eval hard gate; needs a human estimate of NECESSARY calls, not a count | descriptive, not enforced |
| `density_prompt_gate_services` | same | descriptive, not enforced |
| `density_target_services` | same | descriptive, not enforced |
| `long_horizon_call_band` | (500,1000); classifies a task, does not gate it | descriptive, not enforced |
| `qc_binary_subdim_count` | 18 vs 10 | descriptive, not enforced |
| `qc_dimension_count` | 7 for HG vs 5 elsewhere; an operator/council reads it | descriptive, not enforced |
| `qc_subdim_count` | 38 vs 24 | descriptive, not enforced |
| `slack_channels_enumerable` | HG has 985 channels so no whitelist is derivable; the check self-disables via an empty slack_channels set | descriptive, not enforced |
| `trajectory_dispositions` | HG adds an `excluded` state; `run_disposition()` reads it and REPORTS `runs_excluded`, but does NOT subtract it from the pass@1 or density denominators | observational; promotion pending a pinned real excluded run |
| `verifier_models` | descriptive; trajectory_layout already drives discovery | descriptive, not enforced |

