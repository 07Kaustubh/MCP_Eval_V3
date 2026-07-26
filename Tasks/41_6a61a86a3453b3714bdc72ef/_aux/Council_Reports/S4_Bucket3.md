# S4 Bucket 3 (Legitimate Model Failure) findings — model-tagged trajectory walks

Task: Tasks/41_6a61a86a3453b3714bdc72ef · V4 dual-model (Opus 4.8 + Gemini) · **post-fix re-grade** (8a/8b 2026-07-24 22:41-42). Rubric indices are internal (1-20 in `7_Rubrics.json` order).

Every failing criterion below was walked in the failing run's trajectory (raw tool-call extraction) BEFORE classification, and its ground truth re-confirmed in `_aux/Universe_Split/`. All land in Bucket 3 (correct rubric, genuine agent failure). Zero Bucket 1, zero Bucket 2 this run. **R6 (make-ready record) is no longer a failing rubric — it passes 6/6 after the OE-14 reconciliation fix; it is dropped from this file.**

---

## AF cluster — balance trap (BOTH models, all 6 runs each)

**Rubrics 1 (net ~$1,832), 2 (charges ~$1,982), 16 (owner-draft ~$1,832).**

**Trajectory walk (raw extraction, all 12 runs identical in outcome):**
- Relevant tool calls: each run listed/read Tanya Mitchell customer entities and landed on AR invoice 7214 (CustomerRef "Tanya Mitchell", proj-2e48c594aab7); no run called `search_bills` / opened bill QR-2026-0441.
- Parameter/values reported: **$2,287.50** = $1,125 + $975 + $187.50 (invoice 7214 charge lines). Raw-extracted from each Opus run's final result (`final_money=['$2,287.50']` on all 6). Present in the OPS-32 note, Slack post, and owner draft across runs.
- Authoritative value (re-confirmed in raw universe): bill QR-2026-0441 (id 232176553533, VendorRef "Alamo HVAC Services", **no CustomerRef**) lines $847 + $925 + $210 = **$1,982**; less the $150 payment-plan credit (line 4) = **$1,832** net. Stored Balance $2,132 adds the credit as a positive.
- Criterion comparison: "approximately $1,832" / "$1,982 comprising 847/925/210" not met on any run. $1,832 never appears as a reported answer (Opus grep: `1832` absent as a reported figure in 5/6, one incidental token in run 3, never the answer).

**5-point checklist:** (1) grounded — YES, values re-confirmed in raw QB entities; (2) flexible — YES, "approximately" tolerates rounding, accepts any walk-back to the three components; (3) prompt-required — YES ("what she genuinely owes", "walk it back to the underlying charges", "not double-counting any credit", owner email covers "the balance"); (4) real tools/params — YES (final-response + draft-body checks; `search_bills`/`get-bill` exist, no phantom tools); (5) capable agent could pass — YES, the bill is queryable (1 of 113 bills; line descriptions contain "Tanya Mitchell, Unit 14"); hard (0/12) but achievable. → Bucket 3. AF justifications written (`S4_AF_justifications.md`).

---

## Opus partial fails — owner-entity latching (Harris vs Castillo)

Ground truth: EVF-2026-014 (`rec922b9a2d1b9451`) "Owner authorization received from **Linda Castillo** to proceed with eviction filing for Unit 14"; Gmail 06-30 reply is Linda Castillo's written authorization. Contacts label BOTH `linda.castillo` and `harry.harris` as "Property Owner", so the disambiguation is the task-specific authorization record/email, not the contact role. Harris is the stale Linear latching decoy (OPS-32 "Mitchell, Harris Property", hearing "set"). Gemini resolved to Castillo 6/6 (all drafts to `linda.castillo@gmail.com`, raw-confirmed) — the owner latch is Opus-asymmetric.

**Rubric 4 (confirm owner auth = Linda Castillo) — Opus runs 1, 3, 5 fail (3/6).**
- Trajectory: runs 1/3/5 name Harry Harris as owner (run 3/5 explicitly call Linda "internal accounting liaison, not the owner"; run 1 confirms Linda's auth on file but treats ownership as open and directs the owner email to Harris). `harry.harris` present in those trajectories (grep 7/13/13 hits).
- → legitimate latching fail (levers L1 + L6c). Bucket 3.

**Rubric 11 (OPS-32 note states owner-approved / auth on file) — Opus runs 3, 5 fail (2/6).** When the owner was mis-identified, the note flagged authorization as an open item ("owner authorization is not properly on file / must fix before filing") instead of confirming it on file. (Run 1 passed R11 — it did confirm Castillo's auth on file in the note even while flagging the Harris conflict; the R4 fail there is driven by the mis-directed draft.) Bucket 3.

**Rubric 15 (draft addressed to Linda Castillo) — Opus runs 1, 3, 5 fail (3/6).** Raw `create_draft` recipient extraction: runs 1/3/5 → `harry.harris@gmail.com`; runs 2/4/6 → `linda.castillo@gmail.com`. The owner is Linda Castillo. Bucket 3.

**Rubric 18 (owner draft states owner-approved / auth on file) — Opus runs 2, 3, 5 fail (3/6).** Runs 3/5 asked the (wrong) owner to "confirm we have your written authorization", i.e., presented authorization as missing. Run 2 identified the owner correctly (drafted to Linda) but the draft body never stated the authorization-on-file fact — a distinct completeness gap, not an identity error. Both are genuine deliverable-content failures. Bucket 3.

*(Gemini passed rubrics 4/11/15/18 on all 6 runs — the owner latch is Opus-asymmetric here.)*

---

## Gemini partial fail — negative-directive omission

**Rubric 14 (channel message states unit must NOT be marketed) — Gemini runs 1, 5, 6 fail (3/6).**
- Trajectory (raw extraction of the C004 `slack_send_message` body): runs 1/5/6 cover the crew-mobilization hold (rubric 13 passed) but the message body contains no "market" token (raw flag `market_in_msg=False`); the marketing prohibition appears only in the make-ready record note and owner draft, not the channel message. Runs 2/3 include it (`market_in_msg=True`); run 4 posts via `slack_send_message_draft` and also includes "Do not list or market the unit."
- Ground truth: OE 16 requires the channel post to state "the crew must not mobilize and the unit must not be marketed until possession is formally returned"; the prompt states "us marketing something we can't deliver." Rubric R20 checks the same prohibition in the owner draft (passed 6/6 Gemini), so R14 is a valid per-deliverable atomic check, not a duplicate. Opus stated it on all 6 runs → achievable.
- This is the predicted Gemini-asymmetric negative-directive omission (lever L31 / stump hypothesis H4). Genuine model gap. Bucket 3.

## 5-point checklist for the partials (summary)

Rubrics 4/11/15/18 and 14 all pass the 5-point pre-write checklist: grounded (values/owner/OE re-confirmed in universe), flexible (owner rubrics accept flagging the Harris discrepancy as long as the deliverable lands on Castillo; R14 accepts any phrasing of the marketing hold), prompt-required (owner authorization + no-marketing are explicit asks), real tools/params (`create_draft` to-param, `slack_send_message` message-param), and achievable (each passed on the majority of runs / on the other model). None reclassify to Bucket 1.
