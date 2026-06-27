# PIPELINE FEEDBACK — Candidate Feedback (Review Flow)

**Trigger:** `PIPELINE FEEDBACK — Tasks/<TASK_DIR>`

**When to run:** AFTER `PIPELINE REVIEW` completes. BEFORE `PIPELINE CLOSE`. This is the dedicated phase that writes `13_Feedback.txt` — the candidate-facing rating on their ORIGINAL submission.

## Why a separate phase

REVIEW does a lot of work — validators, councils, AUDIT, FINAL, fix proposals, materialization. By the time the agent reaches the feedback step inside REVIEW, the chat context is saturated with "the fixed work" and the feedback consistently drifts to rating what we fixed instead of what the candidate submitted. Lifting this into a fresh-chat phase with a clean context AND a strict input allowlist solves the drift.

Two strict rules drive this phase:

1. **Read ONLY the candidate's originals** — `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` (the untouched originals at task root). Do NOT read `changes.md`. Do NOT read `14_Updated_*`. Do NOT read `15_Updated_*`. Do NOT read `_aux/REVIEW_prompt_draft.txt`. Do NOT read `_aux/Council_Reports/*`. Do NOT read `_aux/REVIEW_*`. None of those are the candidate's work; they're OUR review work.

2. **Evaluate ONLY against the QC spec doc** — `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md`. We exceed this bar internally (50+ density target, strictest AUDIT, 5 gates per phase, B6 propagation, multi-dim similarity, etc.) but the CANDIDATE is rated against the BASELINE the QC spec defines, NOT against our internal exceeds-spec bar. Do NOT downgrade the candidate for missing our internal-only standards.

## Required inputs (the allowlist)

| File | Source | Why required |
|---|---|---|
| `Tasks/<TASK_DIR>/5_Prompt.txt` | candidate-original | the prompt being rated |
| `Tasks/<TASK_DIR>/6_Oracle_Events.txt` | candidate-original | the OEs being rated |
| `Tasks/<TASK_DIR>/7_Rubrics.json` | candidate-original | the rubrics being rated |
| `Tasks/<TASK_DIR>/3_UniverseDataForThisTask.json` | user-pasted | for spot-checking truthfulness / feasibility against the per-task universe |
| `Docs/7_QC_Spec_Doc1.json` | repo | QC dim scoring source |
| `Docs/8_QC_Spec_Doc2.md` | repo | QC dim scoring source |
| `Reference/Linter_Playbook.md` | repo | voice rules (no internal terminology, no em-dashes, plain humanlike) |

## Forbidden inputs (the denylist — DO NOT read)

| File | Why forbidden |
|---|---|
| `Tasks/<TASK_DIR>/changes.md` | Internal change log — **ALLOWED ONLY for fields 3 + 4 mechanical metadata** (count Applied rows for Level-of-Fixes, map section headings to Parts-of-Task-Fixed). NOT allowed to inform fields 1 + 2 (score + qualitative feedback rating the original). |
| `Tasks/<TASK_DIR>/14_Updated_Oracle_Events.txt` | OUR fix to the OEs — not the candidate's work |
| `Tasks/<TASK_DIR>/15_Updated_Rubrics.json` | OUR fix to the rubrics — not the candidate's work |
| `Tasks/<TASK_DIR>/_aux/REVIEW_prompt_draft.txt` | OUR scratch fix to the prompt — not the candidate's work |
| `Tasks/<TASK_DIR>/_aux/Council_Reports/*` | OUR internal review process artifacts |
| `Tasks/<TASK_DIR>/_aux/REVIEW_*` | OUR internal review process artifacts |
| `Tasks/<TASK_DIR>/_aux/Validator_Reports/*` | OUR internal validator output — informs scoring, but not directly read into the feedback voice |

If your tools surface these (because they're in the same directory tree), explicitly suppress them from informing the feedback body. The candidate is rated on what they delivered, full stop.

## Procedure

1. **Confirm originals are intact.** `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` must exist at task root and be non-empty. If any is missing, STOP — the operator needs to invoke `PIPELINE REVIEW` first.

2. **Read ONLY the allowed inputs.** Originals 5 / 6 / 7 + user-pasted 3 + QC spec docs + Linter_Playbook (for voice rules). Do not open anything in the denylist.

3. **Walk every applicable QC spec dimension.** For each applicable dim in `Docs/7_QC_Spec_Doc1.json` (across prompt, OE, rubrics, universe sections), score the candidate's work 1-5 against the SPEC's BASELINE criteria. Use `Docs/8_QC_Spec_Doc2.md` for the prose definition. Do NOT apply our internal exceeds-bar (50+ density, strictest AUDIT, B6 propagation, etc.) — those are project policy, not spec requirements. A candidate prompt that projects to 42 tool calls passes the spec's "investigation breadth" dim even though our internal HARDNESS phase would flag THIN.

4. **Spot-check truthfulness against the per-task universe.** For 2-3 concrete claims in the candidate's prompt / OE / rubrics (dollar amounts, IDs, account numbers, named persons), verify against `3_UniverseDataForThisTask.json`. Feasibility and Truthfulness are spec dims — the candidate's work either grounds or it doesn't, and a quick spot-check is enough; do NOT replicate the full Fact_Ledger grounding sweep that REVIEW already ran.

5. **Plain-language QC dim mapping.** Translate any sub-dim < 5 into plain language for the feedback body. Mapping table (loose, not hard-named — preserves senior-reviewer voice):

   | Internal QC dim | Plain-language description for the candidate |
   |---|---|
   | Atomicity | "rubrics that combine multiple checks into a single line" |
   | Self-Containment | "rubrics that require the judge to look up data outside the criterion text" |
   | Feasibility | "asks the agent cannot satisfy with the available tools and data" |
   | Truthfulness | "factual claims about the universe that do not match the records" |
   | Atomic-for-multi-write | "splitting one-rubric-per-item instead of using at-least-N thresholds" |
   | Outcome-vs-Process category balance | "process-style rubrics that an outcome could already prove" |
   | Tool-leak in rubric titles | "rubrics that name a specific tool the agent had to use" |
   | Coverage gap | "asks in the prompt that no rubric checked" |
   | Investigation pre-solved | "prompt sentences that tell the agent the answer" |
   | Persona-business-function mismatch | "scenario that does not read naturally from this persona's seat" |
   | Internal IDs in prompt | "ID-like strings the persona would not say out loud" |
   | Coherence / contrived difficulty | "asks bolted on that do not read like a single coherent request" |

6. **Derive the mechanical metadata from `changes.md` (v15 — fields 3 + 4 only).** This is the ONE exception to the "do not read changes.md" rule. The candidate-facing form has 4 fields, and 2 of them are mechanical scope metadata that comes directly from what we fixed:

   Read `Tasks/<TASK_DIR>/changes.md`. Count Applied rows per section heading. Use only the counts + section names — do NOT use the change content to inform the qualitative rating (fields 1 + 2 are still rated from the ORIGINAL).

   Map counts to **Level of Fixes** (Field 3):
   | Total Applied rows | Level of Fixes |
   |---|---|
   | 0 | `No edits / Approved as is` |
   | 1-3 | `Minor Fixes` |
   | 4-10 | `Major Fixes` |
   | 11+ OR full rewrite | `Full Redo` |

   Map section headings to **Parts of Task Fixed** (Field 4, multi-select):
   | changes.md section | Form option |
   |---|---|
   | Prompt / Persona | `Prompt` |
   | Oracle Events / OE | `Oracle Events` |
   | Rubrics / Rubric | `Rubrics` |
   | Tool / Universe / Engineering | `Eng. Issues/Taxonomy Issues` |
   | (zero Applied rows) | `None` |

7. **Write `Tasks/<TASK_DIR>/13_Feedback.txt`** matching the candidate-facing form (4 fields):

   ```
   ## Quality: Overall Task

   Score: <1 | 2 | 3 | 4 | 5>

   ## Overall Task Feedback

   <2-5 sentences in plain humanlike voice rating the ORIGINAL submission against the QC spec.>
   <Direct, specific, actionable. Cite what worked and what needs work in the candidate's own words / artifacts.>
   <No internal terminology, no em-dashes, no guide references.>

   ## Level of Fixes

   <Full Redo | Major Fixes | Minor Fixes | No edits / Approved as is>

   ## Parts of Task Fixed

   <comma-separated subset of: Prompt, Oracle Events, Rubrics, Eng. Issues/Taxonomy Issues, None>
   ```

   Hard rules on the Overall Task Feedback body (Field 2):
   - Concise. Senior reviewer voice — direct, professional, not preachy. A FEW sentences, not a full report.
   - No em-dashes.
   - No internal terminology: no QC dim names ("Atomicity", "Self-Containment"), no council references, no script names, no `_aux/` paths, no rubric numbers like "rubric 7", no phase names like "S2 / FINAL / AUDIT".
   - Rate against the QC SPEC baseline only. Do NOT downgrade for missing our internal exceeds-spec bar.
   - Do NOT reference our fixes or `changes.md` content even obliquely. The feedback rates the ORIGINAL; fields 3 + 4 are mechanical scope metadata only.
   - Per the QC docs scoring rule: overall score can only be as high as the lowest scoring rubric. If any single sub-dim in the QC spec scores a 2, the overall is a 2, even if other dims score 5. Reflect this in the Score field.

8. **Voice gate.** Run:
   ```
   python Validators/check_justification.py Tasks/<TASK_DIR>/13_Feedback.txt
   ```
   Exit 0 required. If non-zero, strip every forbidden term per the per-hit report and re-save. Loop until clean.

## Exit criteria

- `Tasks/<TASK_DIR>/13_Feedback.txt` exists with the structured plain-language rating.
- `python Validators/check_justification.py Tasks/<TASK_DIR>/13_Feedback.txt` exits 0.
- The feedback rates ONLY the originals — no leakage from `changes.md` / `14_*` / `15_*` / draft / council reports.
- The feedback uses ONLY plain-language descriptions, no hard-named QC dims or internal terminology.

## STOP gate

This phase ends here after `13_Feedback.txt` is saved and voice-gated. End your response. The user proceeds to `PIPELINE CLOSE — Tasks/<TASK_DIR>` in a fresh chat to wrap up the task.

**If the user pastes follow-up content in this chat** (the next phase's work, additional rating requests, fix attempts, or an unrelated question), do NOT process it. Reply: "This chat is single-shot for the FEEDBACK phase. Please open a fresh chat and invoke the appropriate next trigger from the dispatch table." Chaining inside one chat defeats the entire pipeline.

Do NOT proceed to CLOSE in this chat.

## Bootstrap

Read root `AGENTS.md` first. The candidate is rated on their ORIGINAL submission against the QC SPEC BASELINE — not on our internal exceeds-spec bar. We hold ourselves to a higher standard internally; the rating is fair only when measured against the publicly-defined criteria the candidate had access to.
