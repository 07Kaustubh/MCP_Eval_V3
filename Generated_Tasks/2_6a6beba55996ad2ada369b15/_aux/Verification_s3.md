# Verification — S3 (`2_6a6beba55996ad2ada369b15`)

Universe **harmonygames** (framework `hg`) · persona **Robert** · business function **Executive** · universe today **2026-02-28** America/Chicago · model under test **Claude Opus 4.7** · deliverable `7_Rubrics.json`, **25 criteria**

Set shape: Outcome 1.1 = 3, Outcome 1.2 = 18, Outcome 2.1 = 3, Process = 1. Process share 4 percent against the HarmonyGames flat cap of 40 percent. 25 of the 60-criterion project ceiling.

## Data sources consulted

### Per-task data

- `_aux/Universe_Split/snowflake.snowflake.tables.json` (159 MB) :: streamed, never loaded. Council A re-derived every Snowflake figure at a 230 MiB peak confirmed externally by `/usr/bin/time -v`, and AUDIT re-derived them independently at 231.0 MiB. Both under the 384 MiB ceiling of hard rule 33. Combo Fighter measured window 2026-01-05 to 2026-02-09 (72 rows / 36 dates), lifetime revenue 0.00 with `REVENUE_DAILY_V2` carrying zero combo rows, lifetime acquisition spend 7,483.42 over 330 rows, peak daily active users 801, 845 new users, 55,101 sessions, D1 simple mean 44.0, post-2026-02-09 spend 8,452.64 over 280 rows, cash 2,500 at month_end_date 2026-02-28.
- `_aux/Universe_Split/slack.2026-02.json` and `slack.2026-01.json` :: the 22,500 gross offer and 11,700 counterparty charge at ts 1770911000.728559, the approximately 15,000 Sunset wind-down cost at ts 1770850852.708789, and the campaign-control trail establishing Leonard Hayes as the only person who starts or stops a campaign. All quoted verbatim by both Council A and AUDIT.
- `_aux/Fact_Ledger.json` :: 5,750 amounts and 23,928 emails indexed; the validator's groundedness sweep runs against it.
- `_aux/Verification_s2.md` and `_aux/Reasoning/OE_solvability.md` :: prior-phase verification reviewed. All 13 S2 directives (numbered 1 to 9 and 11 to 13; the source doc skips 10) carried into the criterion set and confirmed honoured one by one in both `S3_B_adversarial.md` and `AUDIT_rubrics.md`.
- `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json` and `Docs_harmonygames/14_Persona_ACL.md` :: Robert's read scope confirmed by authorship, 19 text-bearing messages in #winddown and 691 in the founder channel. No criterion depends on evidence outside his scope.

### Eval spec

`Evals_harmonygames/3_Rubrics_Eval.md`

Read in full before drafting, not after. HarmonyGames severity ordering applied throughout, which is the reverse of the newer StarPM one: **Overly Broad = Moderate, Overly Specific = Minor**, with an over-specification that would false-fail a correct agent escalating to Incorrect (Major) under Phase 2.7.

- Overall Rubric Quality :: **5**. Zero Major, zero Moderate, zero Minor after the round-2 fix.
- Rubric Category Balance :: **5**. Binary. Outcome present at 24 of 25; Process at 1 of 25 is 4 percent against the 40 percent cap.
- Process Rubrics :: **5**. One Process criterion, all three conditions pass.
- Agent-Centric Phrasing :: **5**. See the adjudicated tension below.
- Negative Criteria :: **5**. Binary. Pre-scan hits on "exceeds" and "fall short" are all affirmative actor plus verb naming a reported factual state.
- All-Failing Rubrics :: not assessable at S3, no verifier export. Zero predicted AF.

### QC spec

`Docs_harmonygames/7_QC_Spec_Doc1.json`

All twelve applicable Rubric sub-dims scored **5** under AUDIT's strictest reading, with the per-atom evidence table filled from source rather than inherited. `check_qc_binary.py` independently returns PASS on all 6 measurable binary sub-dimensions.

### Reference docs

- `Docs_harmonygames/2_Rubrics_Guidelines.md` :: four stored fields, the 4-value category enum, the three-condition Process test, the flat 40 percent Process cap with zero Process valid, and the ban on `such as` / `e.g.` / `for example` across every field.
- `Docs_harmonygames/3_Rubrics_One_Pager.md` :: ordering named as the primary Process case; an explicit prompt ordering still requires a Process rubric because no Outcome verifies sequence. This is the authority for criterion 25.
- `Docs_harmonygames/9_Common_Error.md` :: read BEFORE drafting. Drove five decisions, listed in `Reads_s3.md`.
- `Docs_harmonygames/12_Always_Failing_Rubrics.md` :: its affirmative-exclusion pattern is why the R&D credit is kept out of the criterion set entirely rather than expressed as a prohibition.
- `QC_Tasks/V5_HG_Buckets/QC_Passed/Task1..Task4/7_Rubrics.json` :: craft reference, 80 / 50 / 50 / 57 criteria.

## Verification statements

- [x] `validate.py --phase rubrics` PASS, 0 fails, 0 warns, 6 notes.
- [x] `check_rubric_antipatterns.py` OK, 0 findings across 25 criteria x 3 fields.
- [x] `check_ordering_coverage.py` OK. 1 ordering construction in the prompt, 1 Process criterion grading it.
- [x] `check_oe_rubric_sync.py` OK, after mirroring two OE decompose lists under rule 14.
- [x] `check_qc_binary.py` all 6 measurable binary sub-dims PASS.
- [x] `test_regression_anchors.py` 89 passed, 0 failed of 89.
- [x] `validate.py --phase oe` re-run after the OE edit, still PASS 0 fails / 0 warns at 25 steps.
- [x] Council A **GO**. Every concrete value re-derived from source, zero mismatches, zero ungrounded values, no value outside Robert's read scope.
- [x] Council B **GO** on round 2. One Major raised and fixed in place; all six scored sub-dims at 5; zero Major, Moderate and Minor at close.
- [x] AUDIT **PASS (STRICT)** on the first round, with all twelve applicable Rubric sub-dims at 5 and its per-atom evidence table self-derived rather than inherited from Council A.
- [x] Outcome outnumbers Process; Outcome 1.1 for every OE write action; Outcome 2.1 for every prompt tell-me cue.
- [x] Density midpoint 40 to 43 across 5 services on the HarmonyGames bands, clearing the 40+ authoring target, the >15 necessary-call prompt gate and the >=15 trajectory floor. The V3-family 50/40 bands were explicitly excluded from both council briefs and the AUDIT brief.
- [x] All five hardness levers trace end-to-end.
- [x] No criterion names a tool, uses an em-dash, uses "at least N" without a prompt mandate, or dates a communications write to 2026-02-28.

## Discrepancies surfaced

1. **One Major, raised by Council B and fixed in place.** The final-response lead-figure criterion shipped as a closed six-figure financial set. That set omitted the grounded engagement figures (801 peak daily active users, 845 new users, 55,101 sessions, 44.0 percent D1) which criterion 5 itself accepts and which OE 23's "any two or three of the grounded figures" authorizes, so an agent leading with peak DAU would have been false-failed. Reworded to an objective open semantic rule naming five accepted record domains. Council B confirmed on re-check that the Major is retired and the criterion still discriminates: the 24,275 R&D credit presented as inbound cash traces to none of the five domains and fails, as does any fabricated figure.

2. **Two OE decompose element lists edited this pass, mirrored under rule 14.** Both relaxations removed defects the OE was seeding into the rubric set rather than bending criteria to fit a weaker OE. OE 20 asked for the engagement peak to be "reported without softening", which seeds a negatively framed criterion and HG QC dimension 23 makes that an outright FAIL absent a prompt-mandated prohibition; replaced with an affirmative closed set of engagement figures plus an explicit instruction never to grade it as a criterion about softening. OE 21 asked for "at least the coverage verdict and the still-running spend figure restated", which is exactly the non-atomic quantifier bundling the guidelines ban; split into two elements. AUDIT judged both mirrors faithful.

3. **The validator is stricter than the guidelines on Process phrasing.** The canonical HG guidelines give "The Agent posts the ENG-2230 briefing in #season-pass before updating ENG-2230" as the model valid Process criterion, but `validate.py` fails any Process title starting with a write verb, `posts` included. The ordering criterion is therefore phrased "The Agent completes the written account before it posts to the #winddown channel", which satisfies both. Worth knowing before a future task hits the same wall and assumes the guideline example is safe to copy.

4. **The shipped HG QC_Passed corpus stores `category` in a form the spec does not list.** All four passed tasks use lowercase `outcome` / `process`, while `Docs_harmonygames/2_Rubrics_Guidelines.md:319` and `Evals_harmonygames/3_Rubrics_Eval.md:7` both specify the 4-value enum `Outcome 1.1` / `Outcome 1.2` / `Outcome 2.1` / `Process`. The registry enum accepts both. This set ships the spec-conformant 4-value form, which is also project rule 24's `sub_category` already native to the schema, so the validator reports sub-category counts for free.

5. **Agent-Centric Phrasing carries a real spec tension, adjudicated rather than waved.** 18 of 25 titles use the possessive form. `7_QC_Spec_Doc1.json`'s Non-Fail (3/4) row literally names "a valid possessive construction", so a maximally literal reader could dock the sub-dim to 4. AUDIT declined the dock on authority-document text rather than internal precedent: Doc1's own Authority Order sub-dim states the evals supply repository-level policy overrides, and `Evals_harmonygames/3_Rubrics_Eval.md` lines 767, 782 and 788 mark possessive Agent forms valid with "no fix needed" under the 06/09 update.

6. **Two deterministic gates are unmeasurable at S3, and are recorded as unmeasured rather than passed.** `check_criterion_dependencies.py` and `check_rubric_signal.py` both SKIP with no verifier export. Rule 17's passing-cell audit and rule 28's per-criterion discrimination check must both run at S4, before any all-failing criterion is classified and before any trim on signal grounds.

7. **Three watch-items carried to S4, none blocking.** The engagement criterion's 801 branch is a cross-platform per-day sum (single-row max is 426) and its 44.0 branch is a simple mean where the new-user-weighted mean is 43.78; both carry mild derivation ambiguity, but the criterion is any-one-of-four and its 845 and 55,101 branches are unambiguous single-column sums, so it cannot false-fail a correct agent. The superseded Helpshift 1,500 could in principle slip past the lead-figure provenance rule if a judge reads "vendor obligations" loosely. Council A recorded the two competing readings of the continuing-spend figure as distinct: 8,922.12 including 2026-02-09 and 2,444.08 for Combo Fighter alone, against the graded 8,452.64.

## Verdict

PASS.

- `7_Rubrics.json` is 25 criteria in the flat four-field schema, validator clean at 0 fails and 0 warns, every construction and coverage gate green, 89/89 regression anchors.
- Council A **GO**, Council B **GO**, AUDIT **PASS (STRICT)**. One REVISE round consumed against a cap of 3.
- Every prompt ask is graded and no criterion grades a requirement that exists only in the Oracle Events. Coverage matrix at `_aux/Reasoning/Rubric_Coverage_Matrix.md`.
- The set's sharpest discriminator is the net-versus-gross wedge: the managed wind-down service at approximately 15,000 sits above the 10,800 the deal nets and below the 22,500 it grosses, so Leonard's own "the data will likely cover our costs" is true against the gross and false against the net. Criterion 11 grades that comparison directly.
- Ready for `PIPELINE FINAL`.
