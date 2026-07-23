# Rubric Coverage Matrix — S3

**Task:** 40_6a61a86a31b9c973b2021ba5 (StarPM V4, Mesa Vista 7B water heater scope correction)
**AUDIT verdict:** PASS (STRICT) — see `_aux/Council_Reports/AUDIT_rubrics.md`
**Council A:** GO — see `_aux/Council_Reports/S3_A_grounding.md`
**Council B:** GO — see `_aux/Council_Reports/S3_B_adversarial.md`
**Density:** THIN carry inherited from S1/S2 (~38-40 midpoint under strict accounting; ~56 midpoint under generous accounting). HARD FLAG for FINAL / platform monitoring: 6-run avg < 40 → `PIPELINE REDO`.

## Prompt sentence → OE step(s) → rubric(s)

| Prompt line(s) | Ask | OE step(s) | Rubric(s) |
|---|---|---|---|
| L2-4 (backstory) | context, no ask | OE 3 (Slack authority read) | (no rubric — read-only) |
| L5 (tenant call escalation) | context, no ask | OE 4 (Slack thread reply) | (no rubric — read-only; downstream 2, 3, 7, 9 depend) |
| L7 "Before I confirm... check whether the detail she has captured lines up with the summary" | derive correct scope from QB bill vs Gmail/Slack summary | OE 5 (Gmail read), OE 9-10 (QB read + line description) | (derivation covered downstream via content rubrics 3, 5, 7, 11, 15) |
| L7 "Whatever the diagnostic actually points to is the scope I want to move on." | corrected scope must drive all writes | OE 10 (Conclude: full replacement ~$1,850) | (drives content rubrics 3, 5, 7, 9, 11, 13, 15) |
| L8 "Bring the maintenance ticket current with the priority from last night's call and the scope we're actually going with." | Airtable ticket update + priority + scope | OE 7 (find ticket), OE 12 (update) | **1** (write existence), **2** (fldPriority selHigh), **3** (fldDescription bundle) |
| L8 "Update the operations tracking issue so the team sees where it landed" | Linear issue update | OE 8 (find issue), OE 13 (update) | **4** (write existence), **5** (description scope + Thursday) |
| L8 "drop a note walking through the rationale" | Linear rationale comment | OE 14 (save_comment) | **6** (write existence), **7** (comment body bundle: diagnostic + escalation + Thursday) |
| L8 "Drop back into the tenant thread with the same rationale so anyone following sees the call before Hill Country goes ahead" | Slack in-thread post (send, not draft) | OE 15 (slack_send_message) | **8** (write existence: C001 thread 1782824160.000302, send not draft), **9** (message bundle: scope + High + Thursday) |
| L9 "Draft Diane the revised confirmation so she can pull the right parts" | Gmail draft to Diane at Hill Country | OE 16 (create_draft) | **10** (write existence: ap@hillcountryplumbing.com), **11** (body: full-replacement RS75 ~$1,850 Thursday) |
| L9 "Tanya an update on the timing for the week" | Gmail draft to Tanya | OE 17 (create_draft) | **12** (write existence: tanya.mitchell@gmail.com), **13** (body: full-replacement + Thursday + no internal $ figures) |
| L9 "Robert a heads-up on the cost" | Gmail draft to Robert | OE 18 (create_draft) | **14** (write existence: robert.finley@gmail.com), **15** (body: $310 → $1,850 + diagnostic reason + Thursday) |
| L9 "put the install on my calendar for Thursday morning so I'm blocked out to be onsite when the crew shows up" | Carlos GCalendar event | OE 19 (create_event) | **16** (compound: 2026-07-02 morning, Mesa Vista 7B, Carlos's calendar) |
| L11 "Parts need pulling today so Hill Country's ready for Thursday morning" | urgency framing on Diane draft | OE 16 (create_draft body) | (drives content 11 — install slot Thursday morning) |

## Coverage checks

- **Every OE 12-19 write step has ≥1 Outcome 1.1 rubric.** ✓
- **Every OE 12-19 write step with content requirements has an Outcome 1.2 rubric.** ✓
- **Every prompt ask maps to at least one rubric.** ✓
- **No rubric goes beyond the prompt.** ✓ (verified in Council B B5 + AUDIT Lens 2 reverse coverage)
- **Zero explicit prompt tell-me cues → zero Outcome 2.1 rubrics.** ✓ (correct: all content assertions embedded in write artifacts)
- **Zero Process rubrics.** ✓ (matches V3 references Task 11-14)

## Hardness lever → rubric enforcement

| Lever | Enforcing rubric(s) | Pass IFF traversed? |
|---|---|:---:|
| L1 Latching | 1 (exact record ID `rec92f4a1c8e17bd3`) | ✓ |
| L2 QB structured-DB skip | 3, 5, 7, 11, 15 (all require $1,850 scope, only surfaced in QB Line[0].Description) | ✓ |
| L5 Thread-reply blindness | 2 (selHigh), 3(a), 7(b), 9(b) (all require escalation content) | ✓ |
| L7 Multi-write diversification | 1, 4, 6, 8, 10, 12, 14, 16 (8 writes × 5 services) | ✓ |
| L8 Multi-link chain | 3 → 5 → 7 → 9 → 11 → 15 (scope value propagates end-to-end) | ✓ |
| L9 Authority dismissal | 5, 7, 11, 15 (all require $1,850 override; 15 sharpest via $310 → $1,850 cost-delta narrative) | ✓ |

All 6 selected levers enforced with lock-and-key rubric coverage. Agent that skips any lever surface fails ≥1 rubric.
