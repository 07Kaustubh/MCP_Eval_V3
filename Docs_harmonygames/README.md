# HarmonyGames Documentation Index

Use this index to choose the smallest authoritative document for the job. The
numbered filenames are stable because the evaluator playbooks link to them
directly.

## Reading paths

### Task authors

1. [`1_Project_Instructions_Overall.md`](1_Project_Instructions_Overall.md)
2. [`../HarmonyGames_Base_Universe/0_Universe_One-Pager.md`](../HarmonyGames_Base_Universe/0_Universe_One-Pager.md)
   through
   [`../HarmonyGames_Base_Universe/4_Reference_Sheet.md`](../HarmonyGames_Base_Universe/4_Reference_Sheet.md)
3. [`15_Persona_ACL.md`](15_Persona_ACL.md), including the exact linked persona
   roster
4. [`0_Tool_Access_Guide.md`](0_Tool_Access_Guide.md), then the exact catalogs
   in [`../HarmonyGames_Base_Universe/Tool_Access/`](../HarmonyGames_Base_Universe/Tool_Access/)
5. [`2_Rubrics_Guidelines.md`](2_Rubrics_Guidelines.md)
6. The prompt and rubric specialist guides listed below
7. [`../Guide/How_To_Use_This_Eval.md`](../Guide/How_To_Use_This_Eval.md) before
   local evaluation

### Evaluators

1. [`../Guide/How_To_Use_This_Eval.md`](../Guide/How_To_Use_This_Eval.md)
2. [`15_Persona_ACL.md`](15_Persona_ACL.md) for the Agent/Verifier identity and
   read-visibility rules
3. Run [`../Evals/0_Injection_Quality_Eval.md`](../Evals/0_Injection_Quality_Eval.md)
   through
   [`../Evals/5_Submission_Gate_Eval.md`](../Evals/5_Submission_Gate_Eval.md)
   in the order specified by the Guide.
4. Use [`7_QC_Spec_Doc1.json`](7_QC_Spec_Doc1.json) as the scored QC
   specification and [`8_QC_Spec_Doc2.md`](8_QC_Spec_Doc2.md) as its human
   explanation.

### Long-horizon tasks

Read [`14_Long_Horizon_Task_Guidelines.md`](14_Long_Horizon_Task_Guidelines.md)
and calibrate against
[`../QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/`](../QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/).
Task5 remains a craft baseline, but its persona artifact is not the current
task template.

### Historical calibration compatibility

Original QC calibration folders may retain a free-text persona artifact or a
non-roster identity. They are craft/history references only, not proof of
current ACL compliance or performance and not a persona format to copy. Every
new or current task must use `2_Persona.txt` with Persona Key, Persona Email,
Name, Role, and Department copied exactly from one
[`Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json)
entry. Do not edit historical QC folders to retrofit this format.

## Document ownership

- [`0_Tool_Access_Guide.md`](0_Tool_Access_Guide.md) — human tool summary;
  `HarmonyGames_Base_Universe/Tool_Access/*.json` remains authoritative.
- [`1_Project_Instructions_Overall.md`](1_Project_Instructions_Overall.md) —
  end-to-end authoring workflow and design targets.
- [`2_Rubrics_Guidelines.md`](2_Rubrics_Guidelines.md) — canonical rubric
  authoring rules.
- [`3_Rubrics_One_Pager.md`](3_Rubrics_One_Pager.md) — quick reference derived
  from document 2.
- [`4_Prompt_Hard_Tips.md`](4_Prompt_Hard_Tips.md) — empirical difficulty and
  search-pattern advice.
- [`5_Prompt_Diversity_Business_Function.md`](5_Prompt_Diversity_Business_Function.md)
  — business-function coverage.
- [`6_Prompt_Relative_Time_Updates.md`](6_Prompt_Relative_Time_Updates.md) —
  relative-time rules.
- [`7_QC_Spec_Doc1.json`](7_QC_Spec_Doc1.json) — machine-readable scored QC
  dimensions.
- [`8_QC_Spec_Doc2.md`](8_QC_Spec_Doc2.md) — QC severity notes and human
  interpretation.
- [`9_Common_Error.md`](9_Common_Error.md) — prompt, OE, and rubric
  anti-patterns.
- [`10_How_To_Load_and_Edit_Universe.md`](10_How_To_Load_and_Edit_Universe.md)
  — platform universe-loading and editing workflow.
- [`11_Taxonomy.md`](11_Taxonomy.md) — platform UI reference; follows the
  question-specific authority order in document 1, including Tool Access,
  Persona ACL/roster, live facts/schema, the requested work, and current
  Evals/QC.
- [`12_Always_Failing_Rubrics.md`](12_Always_Failing_Rubrics.md) — all-failing
  rubric diagnosis.
- [`13_QC_Companion.md`](13_QC_Companion.md) — plain-language QC companion.
- [`14_Long_Horizon_Task_Guidelines.md`](14_Long_Horizon_Task_Guidelines.md) —
  500–1,000-call task supplement.
- [`15_Persona_ACL.md`](15_Persona_ACL.md) — authoritative task-visible
  identity, persona lifecycle, and read-visibility policy; tool catalogs remain
  authoritative for capabilities.

## Rules that commonly appear to conflict

- **Complexity:** 40+ average calls and 3+ services are authoring targets.
  Prompt evaluation requires more than 15 necessary calls; QC's trajectory
  dimension passes at 15 or more average calls. QC cross-service scoring uses a
  2-service floor.
- **Rubric schema:** task JSON stores four fields: `title` (the criterion text),
  `category`, `justification`, and `evidence`.
- **Process rubrics:** all three conditions in the canonical decision test must
  pass. Process rubrics are optional unless omitting one leaves an explicit
  dependency ungraded. Outcome is mandatory and Process may not exceed 40% of
  the set; this cap is not a target ratio, and zero Process is valid.
- **Oracle Events:** OEs are internal planning documents. They cannot override
  the prompt, universe, tool catalogs, or trajectory evidence.
- **Examples:** `QC_Tasks/` is calibration history, not policy. Current Evals
  override legacy wording in an older example.

## Fixed environment

- Today: **2026-02-28**, America/Chicago
- Active injection window: **2026-01-01 through 2026-02-28**
- Enabled MCP services: **13**
- Persona ACL: **17 task-visible personas; scoped reads on Gmail, Slack, GCal,
  and Contacts only**
- Business functions: **6**
- Working tasks: `Generated_Tasks/<task-name>/`
- Completed calibration examples: `QC_Tasks/`
