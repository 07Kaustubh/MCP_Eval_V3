# Reads — S3 (`2_6a6beba55996ad2ada369b15`)

Universe **harmonygames** (framework `hg`) · persona **Robert** · today **2026-02-28** · model under test **Claude Opus 4.7**

## QC spec / framework docs

- `Docs_harmonygames/2_Rubrics_Guidelines.md` :: canonical authoring rules. Confirmed the stored 4-value `category` enum (`Outcome 1.1` / `1.2` / `2.1` / `Process`), the four stored fields, the three-condition Process test, the flat 40 percent Process CAP with zero Process valid (no Outcome-majority rule here), agent-centric affirmative phrasing with its six rules, the `such as` / `e.g.` / `for example` ban across every field, and the atomic-per-item rule that forbids "at least N" bundling.
- `Docs_harmonygames/3_Rubrics_One_Pager.md` :: quick reference. Confirmed ordering is the named primary Process case and that an explicit prompt ordering can still require a Process rubric because no Outcome verifies sequence. This is the authority for criterion 25.
- `Docs_harmonygames/9_Common_Error.md` :: read BEFORE drafting, per the runbook. Its rubric section drove five drafting decisions: missing criteria 9/12 (built the coverage matrix from the prompt sentence by sentence), over-specified criterion 8/12 (no surface pinned for the account or the tracker), undefined acceptance 7/12 (every figure embedded in `title`), atomicity 6/12 (split the OE 21 "coverage verdict and still-running spend" element into two), and vague exemplar language.
- `Docs_harmonygames/12_Always_Failing_Rubrics.md` :: AF diagnosis patterns. Read for the affirmative-exclusion example, which is what kept the R&D credit out of the criterion set entirely rather than expressed as a prohibition.
- `Evals_harmonygames/3_Rubrics_Eval.md` :: the evaluation authority. Extracted the severity taxonomy, the mandatory placeholder-acceptance pre-scan, the atomicity decomposition gate, the over-specificity decision rule (channel lock-in is Major by default when a valid alternative path exists), the two scored phrasing sub-dimensions (2.8 Agent-Centric, 2.8A Negative Criteria), the Final-Response Coverage hard gate, and the requirement-provenance gate that forbids an OE-only requirement from becoming a criterion.

## Reference corpus

- `QC_Tasks/V5_HG_Buckets/QC_Passed/Task1..Task4/7_Rubrics.json` :: 80 / 50 / 50 / 57 criteria, all four flat with exactly `title` / `category` / `justification` / `evidence`. Only Task2 carries Process, at 2 of 50. Studied Task1's craft for how a closed accepted set is stated inside `title` and how a content element is bound to its artifact rather than to a sibling criterion.
- Deviation noted: all four shipped corpora store `category` as lowercase `outcome` / `process`, while `Docs_harmonygames/2_Rubrics_Guidelines.md:319` and `Evals_harmonygames/3_Rubrics_Eval.md:7` both specify the 4-value enum. The eval is the evaluation authority and the registry enum accepts both, so this set ships the spec-conformant 4-value form, which also carries the sub-category signal for free.

## Reference cards

- `Reference/Sessions/S3.md` :: phase contract, exit criteria, the 3-round REVISE cap.
- `Reference/Rubric_Format.md` and `Reference/Strict_Convention_Inventory.json` :: consulted, but both are Brookfield-derived. HarmonyGames phrasing is taken from the HG passed corpus and `Docs_harmonygames/2_Rubrics_Guidelines.md` instead, per the runbook's own note on per-universe phrasing SSOT.

## Upstream task artifacts

- `5_Prompt.txt` :: decomposed sentence by sentence into the forward coverage matrix.
- `6_Oracle_Events.txt` :: 25 steps. The four `S3 must decompose this into one criterion per content element` directives in OE 20, OE 21, OE 22 and OE 23 are the carrier list, plus the ordering clause at the foot.
- `_aux/Reasoning/OE_solvability.md` :: the 13 S3 directives. All carried; see `Verification_s3.md` for the per-directive disposition.
- `_aux/Council_Reports/AUDIT_oe.md` :: every OE figure re-derived from source with zero mismatches, across all 20 channels Robert can reach. Its NOTE on the 24,275 negative-criterion trap is honoured: no criterion names the R&D credit.
- `_aux/Verification_s2.md` :: prior-phase verification, including the two non-load-bearing cross-table disagreements that directives 9 and 13 keep off the criterion set.
