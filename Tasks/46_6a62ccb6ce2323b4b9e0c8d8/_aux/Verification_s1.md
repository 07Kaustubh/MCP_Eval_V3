# Verification — S1 (cross-source check)

Prompt at revision 4. Universe `starpm`, framework V4, universe today **2026-07-01** America/Chicago.

## Sources consulted

**Per-task data**
- `_aux/Universe_Split/` :: grounded the four atoms the prompt names. Harry Harris + Robert Finley
  as Lisa's two owners via `linear.linear_comments:comment_248a843fe7db59e8afaf8d5b6c71c387`
  (author_id `user_0aa171072660514bb4e76ed0fae5bdb9` = Brooke Phillips), corroborated by
  `slack.slack_messages:297f14105d465ce1b7e66a59f1ad3ecb`. End-of-June owner-delivery deadline via
  the OPS-10 description ("ready for owner delivery before end of June"). `brooke.phillips@starpm.com`
  = "Apartment Property Supervisor" via `contacts.contacts`. `#owner-relations` = C006, not archived,
  with Lisa `U6480117503` in `members_json`.
- `_aux/Fact_Ledger.json` :: consulted. **`lifecycle.today` is null**, which is what exposes the
  validator defect below. No atom coverage for this prompt (see the caveat under Verification).
- `_aux/Hardness_Plan.md` :: five levers (L2, L10, L11, L1, L7) and the governing L36 withholding
  table. The prompt was written to the plan's "Safe prompt shape": name the two owners and the
  missed deadline, name no figure, property, discrepancy, record state or service.

**Eval spec** :: `Evals_starpm/1_Prompt_Eval.md`, all 12 Prompt sub-dims, verdicts below.
**QC spec** :: `Docs_starpm/7_QC_Spec_Doc1.json` Prompt dimension + `Docs_starpm/8_QC_Spec_Doc2.md`
severity ladder; binary dims respected per the scheme map in `Reference/Council_Protocol.md`.
**Reference cards** :: `Reference/Prompt_Format.md`, `Reference/Council_Protocol.md`,
`Reference/Sessions/S1.md`, `Reference/Hardness_Playbook.md`.
**Common errors** :: `Docs_starpm/9_Common_Error.md` Part 1, all 7 prompt-writing error classes.
**Date SSOT** :: `Docs_starpm/6_Prompt_Relative_Time_Updates.md` (universe today 2026-07-01).
**Reference corpus** :: `QC_Tasks/V4_Tasks/QC_Passed/Task1..Task4/5_Prompt.txt`.

## Eval spec sub-dim verdicts (Evals_starpm/1_Prompt_Eval.md)
- 1.1 Unique Ground Truth :: **PASS at rev 4.** Was FAIL at rev 3 (Council B blocker, see below).
- 1.2 Feasibility :: PASS. Gmail is draft-only in StarPM (`create_draft`, no send tool), so the
  prompt says "Put an email together for Brooke", which a draft satisfies. Calendar and Airtable
  write tools confirmed present in the catalog by Council B.
- 1.3 Explicit Tool Mention :: PASS (binary). Zero tool names, zero MCP-server names. The three
  service references are natural-language deliverable surfaces (email / issue tracker / owner
  relations channel).
- 1.4 Prompt Clarity and Specificity :: PASS at rev 4 (both councils 5/5 after the fix; Council B
  scored it 3/5 at rev 3).
- 1.5 Contrived / Unnatural :: PASS. Mid-thought entry, persona states what she already believes.
- 1.6 Truthfulness :: PASS. 10/10 concrete claims grounded by Council A, 5 on two independent paths.
- 1.7 Tool use and Cross-service :: PASS (binary). 3 distinct services named, 6 writes across 5.
- 1.8 Investigation :: PASS (binary). No pre-solving; every discriminator withheld as inference.
- 1.9 Coherence :: PASS (binary). Sentence-removal test passed on all sentences; one situation.
- 1.10 Persona :: PASS. Lisa Smith 1/13, role exact, register matches brief (formality 0.60).
- 1.11 Business Function :: PASS. Both councils 5/5 at iteration 2 (Council A revised 3 -> 5).
  Flagged for FINAL adjudication anyway, see Discrepancies.
- 1.12 Alignment with Today's Date :: PASS. "It is now July" resolves correctly against 2026-07-01;
  the end-of-June deadline is genuinely one day past and OPS-10 is still in Backlog.

## QC spec sub-dims (Docs_starpm/7_QC_Spec_Doc1.json, Prompt dimension)
All 12 scored by Council B-B1 per the scheme map in `Reference/Council_Protocol.md`, binary dims
respected. At iteration 2 Council B reports all 12 at 5.

## Reference docs consulted
- `Reference/Prompt_Format.md` :: 500-word cap, no em-dash, no tool names, no internal IDs, no
  pre-solving, one coherent situation. All re-checked at rev 4 (262 words, 0 dashes).
- `Docs_starpm/9_Common_Error.md` Part 1 :: read before drafting per the S1 runbook, checked against
  all 7 prompt-writing error classes.
- `QC_Tasks/V4_Tasks/QC_Passed/Task1..Task4/5_Prompt.txt` :: voice and structure corpus.

## Verification statements
- [x] Validator (`validate.py --phase prompt`) exit 0. PASS, 0 fails, 0 warns, 262 words, 3 services.
- [x] Council A grounding + convention clean. GO at iteration 2, zero ungrounded claims.
- [x] Council B QC scoring. GO at iteration 2, all 12 applicable sub-dims at 5, no NON-FAIL bands invoked.
- [x] Similarity gate composite < 40. Max composite **27.8** at rev 5 (27.5 at rev 3). Nearest prior task is Task 40 at 27.1
      with multiplier **1.000**, meaning no contextual-differentiator credit was applied (same persona,
      same business function), so that figure is pure lexical distinctness rather than a weighted pass.
- [x] AUDIT verdict = **PASS (STRICT)** at its iteration 2, after returning REVISE at iteration 1 and
      finding a MAJOR defect (F1) that BOTH councils had examined and cleared. Mandatory here on two
      grounds: AGENTS.md rule 12, and S1.md step 8 auto-fire condition (e).
- [x] Density projection re-validated per model. Opus 63.5 / Gemini 66.0 against the V4 design target
      of 40 (floor 15). Council B initially projected the fix would cost 2-4 calls and then corrected
      itself: the Hardness Plan's component table already projected the read-only QuickBooks
      trajectory, so nothing was subtracted. Margins +23.5 and +26.0.
- [x] Rule 23 (ordering -> Process rubric). All 6 `ORDERING` patterns in
      `check_ordering_coverage.py` return zero hits, so zero Process rubrics remains valid at S3.

## Discrepancies surfaced

### 1. Validator defect (pipeline, NOT this deliverable) — surfaced with measured scope, not patched
**Upgraded after Oracle verification.** I had asserted this was blocked by frozen regression hashes
without testing the claim. Measured: the root cause is a one-line key mismatch at
`build_fact_ledger.py:314` (`th.get("today")` vs the `"universe_today"` key written by
`build_universe_index.py:310`), it affects **3 of 4 universes** (all but Brookfield, where the
fallback is right by coincidence), and the frozen baseline **enshrines the wrong date** for 4 of its
7 dated reports (keystone 33/35 should be 2026-04-28, moveops 34/36 should be 2026-04-26). Fixing it
changes 4 of 21 pinned reports and needs `build_fact_ledger.py` re-pinned in `code_hashes.txt`.
Full table in `Handoff_S2_S3.md` item 17. Operator decision.

`Validators/validate.py:472` reads `ledger.get("lifecycle", {}).get("today") or "2026-06-12"`. That
fallback is a **Brookfield** date, and it is universe-blind: the same function branches on
`universe == "starpm"` two lines earlier to select the internal-ID regex, then hardcodes a Brookfield
date regardless. This task's `Fact_Ledger.lifecycle.today` is null (StarPM has no fiscal_periods
table), so every StarPM prompt report resolves relative dates against 2026-06-12 instead of the
correct 2026-07-01. Confirmed independently by Council A three ways.

Consequence if trusted: this prompt's "It is now July" would read as a FUTURE reference and the
task would look date-misaligned on the binary "Alignment with Today's Date" sub-dim, when it is
correct. Not patched here because `validate.py` is covered by frozen report hashes in
`Validators/regression_baseline/`; a fix belongs in its own change with `check_regression.py` re-run.

### 2. The atom verifier gave no signal on this prompt
`verify_universe_atoms.py` returned PASS with **0 atoms checked**. That is a consequence of the
design, not evidence of correctness: the prompt deliberately contains no figures, IDs, amounts or
record states, so there was nothing for it to verify. All grounding here rests on Council A's manual
sweep plus my four hand-verified atoms. Recorded so no downstream phase mistakes that PASS for
mechanical confirmation.

### 3. Two S3-phase checkers crash rather than reporting N/A
`check_qc_binary.py` and `check_ordering_coverage.py` both raise an unhandled `JSONDecodeError` when
`7_Rubrics.json` is still the scaffold placeholder. They are legitimately N/A at S1, but they should
degrade rather than traceback. Minor robustness gap, logged for whoever next touches Validators.

### 4. Open cross-council item for FINAL
Business Function. Council A scored 3/5 (ambiguous) at iteration 1, citing
`owner_portfolio_review_midyear` as a documented Cat 2 scenario and #owner-relations as a Cat 2
channel, then revised to 5/5 agreeing with Council B. Both now agree it is not a FAIL under any
read. Recorded for FINAL because a revision toward agreement is where groupthink hides, and AUDIT
was asked to give an independent read.

## Verdict

**PASS.**

All S1 exit criteria met against the deliverable at revision 5 (sha256 `885750ecef51acc5...`,
261 words, 0 em-dashes):

- `validate.py --phase prompt` PASS, 0 fails, 0 warns, 3 distinct services.
- Council A **GO** (iteration 3), zero ungrounded claims, 10/10 concrete claims grounded.
- Council B **GO** (iteration 3), all 12 applicable Prompt sub-dims at 5, no NON-FAIL band invoked.
- AUDIT **PASS (STRICT)** (its iteration 2), after returning REVISE at iteration 1.
- Similarity max composite 27.8 against a ceiling of 40.
- Density Opus 63.5 / Gemini 66.0 against the V4 per-model design target of 40.
- Hardness levers 5 of 5 preserved (L2 recorded as attenuated, knowingly, and escalated to FINAL).
- Rule 23: all 6 `ORDERING` patterns return zero hits, so zero Process rubrics is valid at S3.

The prompt reached this state through two justified blocks, both of which changed the artifact:
Council B blocked revision 3 on Unique Ground Truth (the correction mandate reached QuickBooks by
anaphora), and AUDIT returned REVISE on revision 4 (the phrase "the scheduling side" denoted Airtable
rather than Calendar). Neither was a false alarm and both are recorded in `Todos_s1.md`.

Not certified by this document: anything downstream of S1. The eleven carry-forwards in
`Handoff_S2_S3.md` are obligations on S2/S3, not claims about the prompt.
