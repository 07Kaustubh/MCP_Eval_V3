# Bucket 1 — Rubric Invalid (fixes)

## R01 — Reply to Craig via `email_reply_to_email` (channel/method lock-in)

### Failure pattern (6/6 runs)
- Run 1, tool call: `email_send_email` to craig.nguyen@keymove-specialty.com (fresh email, not threaded)
- Run 2, tool call: `email_send_email` to craig.nguyen@keymove-specialty.com; agent noted "there's no inbound email to reply to so I sent him a fresh direct email rather than threading one"
- Run 3, tool call: `email_send_email` with subject "Re: Emilia Cruz Steinway damage photos and extraction notes" but no `email_id` thread parameter
- Run 4, tool call: `email_send_email`; agent noted "couldn't find his original email in our store, so sent fresh to his address on file"
- Run 5, tool call: agent tried `get_email_by_id` with fabricated id `email_keymove_craig_steinway_damage` → `email_not_found`, then sent fresh via `email_send_email`
- Run 6, tool call: `email_send_email`; no `email_id` parameter

### Why this is Bucket 1, not Bucket 3

The 5-point checklist (v15) gives:

1. Atomic / grounded? YES. The email `email_email_1f1459bff84c` is confirmed at row_data index 927 of the universe and `reply_to_email` is a valid MoveOps tool.
2. **Flexible enough? NO.** A valid alternative path exists: a fresh email from blessing.okafor@moveops.com to craig.nguyen@keymove-specialty.com fulfills "Blessing owes him a direct reply" with identical operational content and identical KeyMove file landing (Craig's inbox). The rubric's "must be a thread reply" requirement comes from the rubric author's inference about "KeyMove file continuity," not from any explicit prompt instruction.
3. Required by prompt? "I owe him a direct reply" is the prompt language. "Direct reply" is ambiguous between "reply to thread" and "direct fresh email to him personally." The prompt does NOT say "reply on the existing thread."
4. Real tool names? YES.
5. Capable agent realistically passes? NO. 0/6 with Opus 4.8. Multiple runs ran searches and could not surface the email_id from the mailbox store (the Craig email is in folder=SENT from Craig's side, requiring `search_emails` with sender filter rather than the default INBOX search the agents reached for).

Per the Pipeline Deviations table in `AGENTS.md`: "channel/method lock-in is Major by default when a valid alternative path exists." R01 locks in `email_reply_to_email` when `email_send_email` to Craig's address is a valid alternative.

### Suggested fix

Reframe R01 to test the substance (Blessing sends a direct reply to Craig from her own address with the operational content) rather than the tool-method.

**Before:**
> The Agent replies to Craig Nguyen's April 11 damage email (email_email_1f1459bff84c) from blessing.okafor@moveops.com.

**After:**
> The Agent sends an email to craig.nguyen@keymove-specialty.com from blessing.okafor@moveops.com, either as a thread reply on email_email_1f1459bff84c (via reply_to_email) or as a fresh direct email (via send_email).

This keeps R02 (rider-processed acknowledgement), R03 (hold-vs-open direction), and R04 (walkup-assessment restate) intact as the substantive content tests on the Craig email and removes the tool-method lock-in.

---

Bucket 1 count: **1**
Total failing rubrics: **3** (R01, R03, R04)
Bucket 1 ratio: 1/3 = 33.3%
All-Failing rubrics (failed 6/6): R01, R03
Bucket 1 ratio of All-Failing rubrics: 1/2 = **50%**
All-Failing Rubrics sub-dim: 50% falls in 25-50% band → **3/5 (NON-FAIL)**

---

## R01 — RESOLVED — 2026-06-30

Fix applied to `7_Rubrics.json`. The Craig-reply rubric now reads:

> "The Agent replies to Craig Nguyen on his April 11 damage email (email_email_1f1459bff84c) from blessing.okafor@moveops.com, either as a thread reply on the existing email or as a fresh direct email to craig.nguyen@keymove-specialty.com."

Platform verifier re-run against the loosened rubric. Result: R01 PASS in all 6 runs. Verifier text per run cites the fresh `email_send_email` call as satisfying the "either path" criterion.

No remaining Bucket 1 fixes. The post-fix All-Failing Rubrics sub-dim is **5/5 (PASS)** because R03 — the sole remaining all-failing rubric — is Bucket 3 (the intended cross-service inference stump on the hold-vs-open direction). See the appended `## Re-classification` section in `S4_verdict.md` for the corrected sub-dim score.
