# Verifier Fails — S4 verdict

## Trajectory T3 — Error Rate
Erroneous runs: 0/6. Verdict: **PASS** (< 3).

## Trajectory T2 — Agent Failure Rate
Runs passing all rubrics: 0/6. pass@1: **0.0%**. Verdict: **PASS** (≤ 40%).

## Trajectory density
Average tool calls (total): 41.5. Density verdict: **PASS** at the 40 floor. The midpoint sits inside the THIN_DENSITY 40-49 band that the Hardness Plan flagged as the expected projection given the L9-anchored stump shape; the task held the line on real runs at the lower end of its projected 40-58 range.

## Run matrix (22 rubrics × 6 runs; only failing rubrics shown)

| Rubric # | Criterion shorthand                                              | R1  | R2  | R3  | R4  | R5  | R6  | Fail count |
|---------:|-----------------------------------------------------------------|-----|-----|-----|-----|-----|-----|-----------:|
| R01      | Reply to Craig via reply_to_email with email_id 1f1459bff84c    | F   | F   | F   | F   | F   | F   | 6/6        |
| R03      | Direct Craig to HOLD pending client-side disposition            | F   | F   | F   | F   | F   | F   | 6/6        |
| R04      | Craig email restates walkup-assessment / stairwell turn radius  | P   | P   | P   | P   | F   | F   | 2/6        |

Pass-all-runs rubrics (19 of 22, not shown): R02, R05, R06, R07, R08, R09, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22.

## Trajectory walks per failing rubric

### R01 — Reply via reply_to_email (6/6 fail)

- **Run 1**: `email_send_email` to craig.nguyen@keymove-specialty.com; no `email_id` parameter.
- **Run 2**: `email_send_email` (fresh); agent's reasoning: "there's no inbound email to reply to so I sent him a fresh direct email rather than threading one."
- **Run 3**: `email_send_email` with subject "Re: Emilia Cruz Steinway damage photos and extraction notes"; still a fresh send, no thread.
- **Run 4**: `email_send_email`; agent noted "couldn't find his original email in our store, so sent fresh to his address on file."
- **Run 5**: agent attempted `get_email_by_id` with fabricated id `email_keymove_craig_steinway_damage` → `email_not_found`; fell back to `email_send_email`.
- **Run 6**: `email_send_email` direct; no `email_id` parameter.

Universe check: the Craig email is confirmed present at row_data index 927 of the universe split, sender `craig.nguyen@keymove-specialty.com`, folder SENT (from Craig's side). The `reply_to_email` tool exists in the MoveOps catalog with an `email_id` parameter.

**Classification: Bucket 1 — Rubric Invalid.** A valid alternative path (fresh `email_send_email` to craig.nguyen@keymove-specialty.com) fulfills the prompt's "I owe him a direct reply" language with identical operational substance. The rubric locks in tool-method when the prompt does not. See `S4_fixes.md`.

### R03 — Direct Craig to HOLD pending client-side (6/6 fail)

- **Run 1**: Craig email said "open the formal claim on KeyMove's side now. Don't hold pending our client's review." Opposite direction.
- **Run 2**: "go ahead and open it now on your side."
- **Run 3**: "go ahead and open the formal insurance claim on KeyMove's side now. You do not need to hold pending our client's review."
- **Run 4**: "go ahead and open the formal claim now."
- **Run 5**: "go ahead and open the formal claim on KeyMove's side now — don't hold pending our client's review."
- **Run 6**: "please go ahead and open the formal claim on your side now — no need to hold pending our client's review."

All 6 runs gave the same opposite direction. The prompt's "hold pending our client's review" phrasing names the operational reason for the hold (client review), and the prompt elsewhere references the Mosaic precedent (carrier piece and client-facing piece as coordinated dispositions) plus Catalina packaging the NorthWind side. The inference chain "client-side review is what David and Catalina are packaging, that package is still open, therefore tell Craig to hold" is supported by the prompt. Agents missed it via action-bias.

**Classification: Bucket 3 — Legitimate Model Failure (All-Failing).** AF justification drafted in `S4_AF_justifications.md`.

### R04 — Craig email restates walkup-assessment (2/6 fail)

- **Runs 1-4**: Craig email named the walkup assessment underestimating the stairwell turn radius. Pass.
- **Run 5**: Craig email said "Our field report corroborates your extraction notes" but did not name walkup assessment or stairwell turn radius. Fail.
- **Run 6**: Craig email had no mention of walkup assessment, stairwell turn radius, or extraction route. Fail.

The criterion is achievable (4/6 runs pass) and the flexibility clause ("or similar statement that the walkup assessment was insufficient for the stairwell extraction") is genuinely flexible. Runs 5 and 6 simply omitted the operational facts from the Craig email and put them only in the David/Catalina email and Linear comment.

**Classification: Bucket 3 — Legitimate Model Failure (Partial-Fail, NOT All-Failing).** No AF justification required because the rubric does not flag as always-failing on the platform.

## Classifications summary

- Bucket 1 (rubric invalid): **1** rubric (R01) → see `S4_fixes.md`
- Bucket 2 (judge error): **0** rubrics → see `S4_judge_errors.md`
- Bucket 3 (legitimate failure): **2** rubrics (R03 All-Failing + R04 Partial-Fail) → R03 in `S4_AF_justifications.md`

## All-Failing Rubrics sub-dim

All-Failing rubrics (failed in every completed run): **R01, R03** (count = 2)
Of these, Bucket 1 (rubric invalid): **R01** (count = 1)
Bucket 1 ratio of All-Failing rubrics: 1 / 2 = **50%**

Per scoring table: 50% sits in the **25-50% NON-FAIL** band. **Score: 3/5 (NON-FAIL).**

Justification: half of the always-failing rubrics traces to a tool-method lock-in on the Craig reply rather than to a genuine task difficulty. Loosening R01 to accept either a thread reply or a fresh send to Craig's address would drop the ratio to 0%. The remaining always-failing rubric (R03 hold-vs-open direction) is a real, defensible reasoning challenge supported by the Mosaic precedent reference in the prompt.

## Hardness calibration

Stump hypothesis hit rate vs. the four predictions:

| # | Predicted stump | Predicted strength | Actual | Status |
|---|----|----|----|----|
| H1 | Stop at "approve the $1,200 rider"; never file customer-side docket distinct from vendor | HIGH | All 6 runs flagged the client-side disposition for David and Catalina across the email, Linear comment, and Airtable record | **OVER-PREDICTED** |
| H2 | Never query Airtable tblRelocations01 / never query the Mosaic precedent bill | HIGH | All 6 runs updated the Emilia Cruz Airtable record correctly (R11-R15 pass) | **OVER-PREDICTED** on Airtable; Mosaic precedent query is not directly observable from the rubric set |
| H3 | Post operational lesson to wrong Slack channel (#customer-engagement or #finance) | MED | All 6 runs posted to C006 #operations correctly | **OVER-PREDICTED** |
| H4 | Email Craig but do not answer his Apr 11 open question | MED | All 6 runs answered the question, but in the opposite direction (open-now instead of hold-pending) | **PARTIALLY CONFIRMED** — failure mode shifted from "unanswered" to "answered wrong direction" |

Under-predicted failure modes that actually fired:

1. **Tool-method lock-in on the Craig reply.** R01 (reply_to_email vs. send_email) fails 6/6. The Hardness Plan did not anticipate that the email-id-discovery step would short-circuit so reliably across runs. Several runs hallucinated email_ids instead of searching by sender, suggesting search-strategy fragility on inbound emails in folder SENT (from sender's side).
2. **Reverse-direction inference on Craig's binary question.** Hardness Plan H4 framed the stump as "agent does not answer" but the actual failure was "agent answers in the opposite direction." This is a stronger and more interesting failure mode: the agent reads the binary, picks an option, picks the wrong one because of action-bias. Lever 11 (vendor disposition treated as the whole disposition) is what drives the wrong pick.

Density observation: projected midpoint 47, actual midpoint 41.5. The THIN_DENSITY operator note in the Hardness Plan was right; agents under-traversed the L8 multi-link chain. The task still cleared the 40 floor but did not reach the 50+ design target.

## Action items

- **Apply R01 fix** to `7_Rubrics.json` per `S4_fixes.md` (reframe to accept either tool path on the Craig reply). After the fix, the All-Failing Rubrics sub-dim moves from 3/5 to 5/5.
- **Keep R03 as-is** and ship the AF justification to the platform reviewer. This rubric is the intended failure mode and tests a real cross-service inference.
- **No fix needed for R04.** Partial-fail at 2/6 is acceptable; the criterion is achievable in 4/6 runs.
- **No judge-error appeals** required.
- Re-run platform verifier after R01 fix if the operator wants the All-Failing sub-dim to clear at 5/5.

---

## Re-classification after R01 fix applied — 2026-06-30

The R01 fix was applied to `7_Rubrics.json` (rubric loosened to "either a thread reply on the existing email or a fresh direct email") and the platform verifier was re-run. The current `8_Verifier_Fails.txt` reflects the post-fix grading: R01 passes 6/6 because every run sent a fresh direct email to `craig.nguyen@keymove-specialty.com`, which the loosened rubric accepts. This section supersedes the matrix above for go-or-no-go reading. The pre-fix analysis is preserved for the audit trail.

### Run matrix (post-fix) — only failing rubrics shown

| Rubric  | Criterion shorthand                                              | R1  | R2  | R3  | R4  | R5  | R6  | Fail count |
|---------|-----------------------------------------------------------------|-----|-----|-----|-----|-----|-----|-----------:|
| R03     | Direct Craig to HOLD pending client-side disposition            | F   | F   | F   | F   | F   | F   | 6/6        |
| R04     | Craig email restates walkup-assessment / stairwell turn radius  | P   | P   | P   | P   | F   | F   | 2/6        |

R01 status: PASS in every run (verifier cites "fresh direct email to Craig's address, which satisfies the criterion"). 20 other rubrics: pass all six runs.

### Classifications summary (post-fix)

- Bucket 1 (rubric invalid): **0** rubrics
- Bucket 2 (judge error): **0** rubrics
- Bucket 3 (legitimate failure): **2** rubrics
  - R03 — All-Failing — AF justification in `S4_AF_justifications.md`
  - R04 — Partial-Fail (2/6) — no AF justification needed because the rubric does not always-fail

### All-Failing Rubrics sub-dim (post-fix)

- All-Failing rubrics: **R03** (count = 1)
- Of these, Bucket 1: **0**
- Bucket 1 ratio of All-Failing rubrics: 0 / 1 = **0%**
- Per scoring table: 0% sits in the **< 25% PASS** band → **Score: 5/5 (PASS).**

Justification: the single always-failing rubric (R03) is Bucket 3, the intended hold-vs-open direction stump that tests a real cross-service inference (the Mosaic precedent + the open client-side review packaging Catalina is doing). No rubric defect drives the always-fail behaviour.

### Action items (post-fix)

- R01 fix already applied. No further rubric changes required.
- R03 ships to the platform reviewer as a legitimate AF rubric with the justification in `S4_AF_justifications.md`.
- R04 partial-fail (2/6) is acceptable; the criterion is achievable in 4/6 runs and the flexibility tail clause is genuinely flexible.
- No judge-error appeals required.
- Task verdict: **SHIP.**
