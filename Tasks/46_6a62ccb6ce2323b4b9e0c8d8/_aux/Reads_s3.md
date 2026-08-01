# S3 Reads - Tasks/46_6a62ccb6ce2323b4b9e0c8d8

v11 E2 compliance log. One line per spec doc / Reference card / Eval spec consulted, with what was confirmed.
Universe: starpm (V4), read from `_aux/Universe.txt`.

## Read directly by the orchestrating agent

- `Reference/Sessions/S3.md` :: phase contract - required inputs, 10-step procedure, exit criteria, STOP gate. Confirmed AUDIT auto-fire is unconditional for S3 (not conditional as in S1/S2).
- `AGENTS.md` (root) :: 30 hard rules. Load-bearing for this phase: rule 8 (outcome > process), 13 (single-target uniqueness / every-service sweep), 14 (60-criterion ceiling, never cut a lever carrier, mirror cuts into OE decompose directives), 21 (all-failing defaults to REMOVAL), 23 (ordering requires a Process rubric regardless of default-to-zero), 25 (authority order: QC Spec > Evals > Guidelines > convention), 26 (10 binary QC sub-dims), 27 (Overly Specific = MODERATE, Overly Broad = MINOR since 07/16), 28 (zero-signal criteria are weak assertions).
- `Tasks/46_6a62ccb6ce2323b4b9e0c8d8/5_Prompt.txt` :: 4 paragraphs. Asks read cold for the tell-me set and the write set.
- `Tasks/46_6a62ccb6ce2323b4b9e0c8d8/6_Oracle_Events.txt` :: 36 OE steps. Four embedded `S3 must decompose this into one criterion per content element` directives at OE 30, 31, 33, 36; one `S3 must write this as a single criterion whose accept-set covers ...` directive at OE 35.
- `Tasks/46_6a62ccb6ce2323b4b9e0c8d8/_aux/Handoff_S2_S3.md` :: 426 lines. The binding obligation list. Carries 6 BLOCKING obligations, 4 pinning cautions, the graded write set with cardinality already pinned, 4 deliberate accept-set breadths, and 7 closing-review cautions.
- `Reference/Rubric_Format.md` :: flat 4-field schema `{title, category, justification, evidence}`; hard rules table; 1.1/1.2/2.1 sub-type shapes; flexibility patterns; threshold math with the pipeline's absolute-count gates (active only below 30 criteria).
- `Docs_starpm/9_Common_Error.md` :: Part 3 rubric errors read BEFORE drafting per the runbook. Ten error classes: process-duplicating-outcome, process-phrased-as-tool-call, single-channel lock-in, bundling across calls, external-knowledge dependence, values not matching universe data, requiring actions the prompt never asked for, reasoning mixed into the criterion field, "approximately" on fixed values, and unfair (all-failing) criteria. The last one is the source of AGENTS.md rule 21: *"If and only if we can vehemently defend the existence of this criterion, should we keep it. Otherwise, we need to remove it."*
- `Docs_starpm/2_Rubrics_V3_Guidelines.md` :: framework rules. Two categories only; outcome-first workflow (Steps 1-6); three-condition Process test; verb cheat sheet per sub-category; service metadata requirements (email needs recipient + CC + itemised content, Slack needs channel + itemised content, Linear needs title + fields); bundling exception limited to same-tool-call parameters or a single inseparable data record; "approximately" barred from counts, IDs and dates; atomic-per-item rule for multi-item write actions with "at least N" reward-hackable and allowed only where GT is genuinely indeterminate.

## Delegated reads (sub-agent extractions, logged on return)

- `QC_Tasks/V4_Tasks/QC_Passed/Task*/7_Rubrics.json` :: V4 phrasing/structure SSOT - delegated (bg_4dfaa616).
- `Tasks/46_6a62ccb6ce2323b4b9e0c8d8/_aux/Hardness_Plan.md` :: lever inventory for the B4 coverage gate - delegated (bg_108db32c).
- `Evals_starpm/3_Rubrics_Eval.md` + `Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/12_Always_Failing_Rubrics.md` :: scoring sub-dims, severity taxonomy, threshold math, AF patterns - delegated (bg_41fcc173).

## Notes carried into drafting

- Authority order (rule 25) matters here: `2_Rubrics_V3_Guidelines.md` is dated Jun 3 2026 and its May 20 entry says "Removed fixed outcome-to-process ratio", but `7_QC_Spec_Doc1.json` reinstates Rubric Category Balance as a BINARY sub-dim on 05/22. The QC spec is later and higher authority, so outcome > process is enforced as a hard gate, not a preference.
- The guidelines' "When to Write Rubrics" section assumes rubrics are drafted during/after a live agent run. This pipeline drafts pre-run from the universe split and the OE chain, then reconciles at S4 against real trajectories. Recorded so the difference is deliberate rather than an oversight.
