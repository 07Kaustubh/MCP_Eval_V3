# Changes Tracker — Task 10_6a2d9411aa26e656b0eff46b

**Task:** FY26 Q1 partner sign-off control test re-verification
**Persona:** Peter Sanchez (Head of Compliance)
**Business Function:** Compliance & Internal Controls
**Reviewer:** QC second-look (auditor)
**Date opened:** 2026-06-13

---

## Baseline QC Snapshot (before any fixes)

| Dimension | Sub-Dimension | Initial Rating | Notes |
|---|---|---|---|
| Prompt | All 12 sub-dimensions | 5 | Clean |
| Universe | Data exists + Cross-service coherence | 5 | Clean |
| Oracle Events | OE Completeness + Accuracy | 5 | Clean |
| Rubric | Overall Rubric Quality | **4** | Rubric #13 title carried a leaked `` `json\n` `` markdown code-fence prefix (minor wording error) |
| Rubric | All-Failing Rubrics | 5 (auto) | No rubric failed all 6 completed runs |
| Rubric | Category Balance | 5 | 15 Outcome / 0 Process |
| Rubric | Process Rubrics | 5 | None present; Outcome covers all OE work |
| Rubric | Agent Centric Phrasing | 5 | All begin "The Agent…"; no tool names |
| Trajectory | Tool Call Count | 5 | ≥15 average comfortably exceeded |
| Trajectory | Agent Failure Rate | 5 | pass@1 = 1/6 = 16.7% (≤40% required) |
| Trajectory | Error Rate | 5 | 0 errored runs |

**Initial overall (grade-to-lowest):** **4 (Non-Fail)**, capped by Rubric → Overall Rubric Quality.

---

## Universe Verification Performed

Verified directly against `3_UniverseDataForThisTask.json` (25,937 rows across 42 sources):

- **5 sampled reconciliations** — all present, with the entity / preparer / reviewer / certifier identities matching OE 4 exactly.
- **Email IDs** — `email_scen_042_audit_compliance_0001`, `_0005`, `_0006`, `email_scen_043_audit_compliance_0001`, `_0009` — all present with the expected senders, subjects, timestamps, and content (Marina kickoff; Marina CLEAR memo; Steven clearance + Q2 direction; Julia Northstar planning; Julia Northstar materiality).
- **Calendar event** — `event_scen_042_audit_compliance_0007` exists, titled "FY26 Q2 partner-sign-off control test", start `2026-08-04T18:00:00+00:00`, `attendees=[]` (so adding Peter + Julia is genuinely required).
- **Slack channel** — `C008` = `compliance-and-registrations` (matches OE 11 and rubric #7).
- **Contacts** — Marina Soko (Compliance Officer), Farah Dlamini (AML Analyst), Julia Vance (Audit Partner), Peter Sanchez (Head of Compliance), Steven Perry (Managing Partner) — all `@brookfieldcpas.com`.
- **Rubric #13 ground truth (firm-internal distractors)** — verified via authoritative `job` field and `@brookfieldcpas.com` email domain:
  - Rakesh Ambani → `job = "Chief Executive Officer"`, firm employee.
  - Margaret Sullivan → `job = "Controller"`, firm employee.
  - Ryan Delgado → `job = "Audit Senior"`, firm employee.
  - George McAdam → `job = "Accounts Senior"`, firm employee.
  - Steven Perry → `job = "Managing Partner"`, firm employee.

  Note: the contact `description` field is written in George McAdam's narrative voice ("That's me — accounts senior"), so Rakesh's description colloquially reads as "Client-side CEO" and Margaret's as "Client controller". The authoritative org facts (`job` + `@brookfieldcpas.com` email domain) place both inside the firm. This is *natural difficulty* — an agent that anchors on the narrative description rather than the structured fields will over-apply the methodology and fail rubric #13. The rubric's ground truth is correct.

- **`4_Changelog.json`** — empty (no CB universe edits), consistent with rubric/OE assumptions.

---

## Findings & Fixes

### Finding F-001 — Rubric #13 title contained leaked `` `json\n` `` markdown code-fence prefix [FIXED]

- **File:** `7_Rubrics.json`
- **Rubric index:** #13 (0-based 12), category `outcome`
- **Field:** `title`
- **Before (repr):** `'json\nThe Agent concludes that BL-EA01CF363E1E is the only one of the five sampled reconciliations… a rotation-boundary observation only).\n'`
- **After (repr):** `'The Agent concludes that BL-EA01CF363E1E is the only one of the five sampled reconciliations… a rotation-boundary observation only).'`
- **Issue type:** Minor Wording Error per `Docs/8_QC_Spec_Doc2.md` → "Purely Non-Failing Issues > Rubric Wording Errors" — borderline, but visible as part of the criterion text the judge reads.
- **QC sub-dimension impacted:** Rubric → Overall Rubric Quality (only sub-dimension below 5 in the baseline).
- **Fix applied:** Stripped the leading `json\n` and trailing `\n`. Criterion text and category unchanged. All 15 titles verified clean (no `\n`, no leading `json`, no leading/trailing whitespace).
- **Status:** ✅ Done.

### No other findings

A second-pass deep audit using `Evals/1_Prompt_Eval.md`, `Evals/2_OE_Eval.md`, and `Evals/3_Rubrics_Eval.md` produced no additional Major / Moderate / Minor issues:

- **Prompt** — passes all 12 sub-dimensions cleanly. Persona voice matches Head of Compliance; cross-service investigation required (BlackLine + Email + Calendar + Slack + Contacts); no tool names; no command-list shape; coherent single scenario; no bolt-ons; investigation drives the action; date references resolve cleanly against the universe.
- **OEs** — all 12 OEs are tool-grounded, accurate, and complete; tool names match `8_Server_Tools_Details.json`; expected data values match the universe verification above; covers discovery → contacts lookup → 4 write actions (BlackLine review note, email Marina/Farah, Slack post, calendar edit).
- **Rubrics** — every rubric is atomic, self-contained (specific recon IDs / emails / channel embedded), agent-centric ("The Agent …"), and names no tool. Rubric #3 and #5 explicitly write the channel-agnostic notification path ("any direct notification path is valid") — correctly avoids method lock-in. Rubric #9 allows either edit-existing or create-equivalent — correctly avoids path lock-in. 15 Outcome / 0 Process is appropriate here because every key behavior the prompt asks for is a write action or a final-response claim that Outcomes can verify with embedded ground-truth values; no Process rubric passes the three-condition test.
- **Trajectory** — pass@1 = 1/6 = 16.7%, 0 errored runs, ≥15 tool calls per run (the trajectory log items reach ~260). Rubric #13 is the discriminating rubric (5/6 runs fail by over-flagging firm-internal distractors as exceptions; Run 6 passes by correctly reading the org structure).

---

## Post-Fix QC Snapshot

| Dimension | Sub-Dimension | Final Rating |
|---|---|---|
| Prompt | All 12 sub-dimensions | 5 |
| Universe | Data exists + Cross-service coherence | 5 |
| Oracle Events | OE Completeness + Accuracy | 5 |
| Rubric | Overall Rubric Quality | **5** ← was 4 |
| Rubric | All-Failing Rubrics | 5 |
| Rubric | Category Balance | 5 |
| Rubric | Process Rubrics | 5 |
| Rubric | Agent Centric Phrasing | 5 |
| Trajectory | Tool Call Count | 5 |
| Trajectory | Agent Failure Rate | 5 |
| Trajectory | Error Rate | 5 |

**Final overall (grade-to-lowest):** **5 (Pass) across every dimension.**

---

## Change Log

| # | Date | File | Change | Reason | QC Dim Affected |
|---|------|------|--------|--------|-----------------|
| 1 | 2026-06-13 | `7_Rubrics.json` | Rubric #13 `title`: stripped leading `json\n` and trailing `\n`. | Leaked markdown code-fence prefix in the title (minor wording error per `8_QC_Spec_Doc2.md`). | Rubric → Overall Rubric Quality (4 → 5). |

---

## Candidate Feedback Notes (for the rating)

**Strengths**

- Strong end-to-end scenario design. Pass@1 = 16.7% is squarely inside the target band, and the discriminating rubric (#13) catches a *meaningful* failure mode — over-applying the independence methodology to firm-internal certifiers — rather than a trivia gap.
- Cross-service investigation is genuine: solving requires correlating BlackLine certifier identity → Northstar audit-engagement emails. The agent cannot lean on Marina's CLEAR memo alone; it has to go to the source records, which is exactly what the prompt asks for.
- Rubric framing is method-agnostic where the prompt named a goal (e.g., "get it in front of Marina") and method-specific only where the prompt named a channel (e.g., `#compliance-and-registrations`). That's the correct V3 calibration.
- Rubrics are all self-contained, atomic, agent-centric, and tool-name-free. No over-specification, no fabricated literals, no reward-hackable "at least N" patterns.

**One thing to clean up next time**

- Rubric #13's title carried a leftover `` `json\n` `` markdown code-fence — looks like the rubric was authored in a chat / code-block context and the fence header got captured inside the JSON string when it was pasted. Worth a quick visual scan of all `title` fields for stray newlines or markdown markers before submitting. Score impact was small (Minor wording error) but it was the *only* thing keeping the task off a clean 5/5.
