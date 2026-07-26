# Reads log — PIPELINE S3 (Rubrics) — Tasks/44_6a62ccba8cad60844b8364b9

Universe: `starpm` (V4). Every doc below was read in full unless noted.

## Framework / spec docs

- `Reference/Rubric_Format.md` :: FLAT 4-field schema confirmed (`title`, `category`, `justification`, `evidence`); no `id`, no `annotations`. Confirmed hard rules: agent-centric titles, no tool names in title, no "at least N" without prompt mandate, atomic per item, single-target uniqueness, threshold math with absolute-count gates (Major >= 3 = FAIL; activates below 30 rubrics).
- `Docs_starpm/2_Rubrics_V3_Guidelines.md` :: two categories only (Outcome mandatory / Process optional-rare); Outcome sub-types 1.1 write result, 1.2 action content, 2.1 key facts to user; five phrasing rules; three-condition Process test; bundling exception (same tool call / same data point); Mistake 12 method-agnostic rule; Rule 4 approximately only for calculated values, never counts/IDs/dates; service metadata requirements (Email: recipient + content items listed individually; Slack: channel + content items; Linear: title + relevant fields).
- `Docs_starpm/12_Always_Failing_Rubrics.md` :: valid-AF patterns. Two legitimate sources of all-fail: over-strict Outcome (rounding/equivalents) and bundled Outcome. Process rubrics that punish a valid path must be deleted, never made "flexible" by enumerating tools.
- `Evals_starpm/3_Rubrics_Eval.md` (all 1079 lines) :: the grading spec this rubric set will be scored against. Extracted: 5 scored sub-dims; severity taxonomy (Major = missing criteria / not self-contained / not atomic / incorrect; Moderate = overlapping, mislabeled category, overly specific; Minor = overly broad); hard gates: Blank Fields, Forward Coverage, Atomicity Split-Completely, Act-vs-Defer (T9), Impossible Derivation (T10), Imported Constraint (T10), Write-as-Deliverable Preservation (T12), Prompt-vs-Rubric Action Alignment (Gap 6), Deliverable Destination Consistency, Final-Response Coverage (Gap 3), OE-to-Rubric Cross-Reference (Gap 4), Exclusion/Decoy Coverage, Under-Strict/Overly-Broad, Pre-Submission All-Fail Prediction. Phase 2.7 anti-rationalization rule on channel/method lock-in (Major by default when a valid alt path exists). Phase 2.11 date alignment resolves relative time from 2026-07-01.
- `Docs_starpm/7_QC_Spec_Doc1.json` (Rubric dimension) :: 5 sub-dims + pass bands; Overall Rubric Quality PASS requires zero Major AND zero Moderate and <5% Minor.
- `Docs_starpm/8_QC_Spec_Doc2.md` :: V3 severity taxonomy definitions + worked examples behind the eval's severity table.
- `AGENTS.md` :: hard rules 6 (no "at least N"), 7 (no tool names in rubric titles), 8 (Outcome > Process, default zero), 11 (V4 density 40+ per model), 13 (single-target uniqueness / every-service sweep incl. Calendar / naive-agent simulation). Deviations table: channel lock-in is Major by default (Phase 2.7 escalation is primary, taxonomy Minor entry is fallback).

## Reference corpus (voice / structure) — read every one

- `QC_Tasks/V4_Tasks/QC_Passed/Task1_6a26c29d5f5b7cf1ea90c0cc/7_Rubrics.json` :: 32 rubrics, 0 process. Pattern: one 1.1 per write, then one 1.2 per content element of the same write, then a parallel 2.1 block for the same facts in the final response. Confirms per-content-element decomposition is the passing house style, and that the same fact in two different deliverables is two rubrics, not a redundancy.
- `QC_Tasks/V4_Tasks/QC_Passed/Task2_6a27b70a80b7729ca5d6d88d/7_Rubrics.json` :: 14 rubrics, 0 process. Confirms method-agnostic tracking-item phrasing ("may use a reminder, calendar event, Linear issue, or Airtable record") when the prompt leaves the destination open.
- `QC_Tasks/V4_Tasks/QC_Passed/Task3_6a2b528b5612fb11a6502d7a/7_Rubrics.json` :: 14 rubrics, 1 process. The one passing Process rubric in the corpus: independent verification of a balance against a primary source where the Outcome content could be mirrored from the secondary source. Its justification explicitly argues all three conditions. Also the strongest example of `evidence` fields carrying explicit FAIL clauses (naming the wrong answers that must not pass).
- `QC_Tasks/V4_Tasks/QC_Passed/Task4_6a30fe7ec1d692ab3ccad616/7_Rubrics.json` :: 23 rubrics, 0 process. Confirms notify-style 1.1 split one-per-recipient, and the same content element graded separately in the notification and in the written record.
- `Reference/Strict_Convention_Inventory.json` :: allowed phrasings + evidence-field shapes; checked "(or similar)", "approximately", "must be one of", "including but not limited to" usage bands against the above.

## Task inputs

- `Tasks/44_.../5_Prompt.txt` :: the 11 asks this rubric set must cover, no more.
- `Tasks/44_.../6_Oracle_Events.txt` :: OE1-38. OE28-38 are the write actions; OE29-33 and OE35, OE37, OE38 carry explicit "S3 must decompose this into ..." instructions that this phase treats as binding.
- `Tasks/44_.../_aux/Hardness_Plan.md` :: 5 selected levers + the 10 pre-registered S3 constraints (esp. 7a: scope the state claim to Jaime's three QC issues, never the whole push; 6: no rubric on OPS-91; 7: no rubric on an absence).
- `Tasks/44_.../_aux/Verification_s2.md` :: prior-phase cross-source verification; corrections appended to the Hardness Plan (37 thread parents not 15; 18 HVAC ticket rows not 20+; Lisa's ask is 7 days after Elias's wrap not 5).
- `Tasks/44_.../_aux/Universe_Split/*` + `_aux/Fact_Ledger.json` :: ground truth for every value embedded in a rubric title. Per-value greps recorded in `_aux/Verification_s3.md`.
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: write-tool parameter shapes confirmed for the six write surfaces (Airtable `create_records_for_table`, Linear `save_issue` / `save_comment`, Gmail `create_draft`, Slack `slack_send_message`, GCalendar `create_event`) — used only to keep evidence fields honest; no tool name appears in any criterion.
