# S4 Bucket 3 (Legitimate Model Failure) findings — model-tagged trajectory walks

Task: Tasks/41_6a61a86a3453b3714bdc72ef · V4 dual-model (Opus 4.8 + Gemini). Rubric indices are internal (1-20 in `7_Rubrics.json` order).

Every failing criterion below was walked in the failing run's trajectory BEFORE classification, and its ground truth re-confirmed in `Universe_Split/`. All land in Bucket 3 (correct rubric, genuine agent failure). No Bucket 1, no Bucket 2.

---

## AF cluster — balance trap (BOTH models, all 6 runs each)

**Rubrics 1 (net ~$1,832), 2 (charges ~$1,982), 16 (owner-draft ~$1,832).**

**Trajectory walk (representative, all 12 runs identical in outcome):**
- Relevant tool calls: each run listed / read Tanya Mitchell customer entities and landed on AR invoice 7214 (CustomerRef "Tanya Mitchell", proj-2e48c594aab7).
- Parameter/values reported: `$2,287.50` = $1,125 + $975 + $187.50 (invoice 7214 charge lines). Present verbatim in every run's final response, Airtable note, OPS-32 comment, Slack post, and owner draft (grep: "2287" 7-23 hits/run across 12/12 runs).
- Authoritative value: bill QR-2026-0441 (id 232176553533, VendorRef "Alamo HVAC Services", **no CustomerRef**) lines $847 + $925 + $210 = **$1,982**; less the $150 payment-plan credit (line 4) = **$1,832** net. Stored Balance $2,132 adds the credit as a positive.
- Criterion comparison: "approximately $1,832" / "$1,982 comprising 847/925/210" not met on any run. $1,832 never appears as a reported answer (grep: absent 11/12; a single incidental token in Opus run 3, not the reported figure).
- **Opus asymmetry note:** `QR-2026-0441` appears in Opus trajectories only as a PDF filename inside a `workspace/company_files/invoices` directory listing — the bill entity was never opened/read. Both models effectively skipped the vendor-linked bill (lever L2, structured-DB skip); neither disposed the $150 credit (lever L11).

**5-point checklist:** (1) grounded — YES, values re-confirmed in QB entities; (2) flexible — YES, "approximately" tolerates rounding, accepts any walk-back to the three components; (3) prompt-required — YES ("what she genuinely owes", "walk it back to the underlying charges", "not double-counting any credit", owner email covers "the balance"); (4) real tools/params — YES (final-response + draft-body checks, no phantom tools); (5) capable agent could pass — YES, the bill is queryable; hard (0/12) but achievable. → Bucket 3. AF justifications written.

---

## Opus partial fails — owner-entity latching (Harris vs Castillo)

**Rubric 4 (confirm owner auth = Linda Castillo) — Opus runs 2, 3, 5 fail (3/6).**
- Trajectory: runs 2/3/5 identify Harry Harris as owner (from Linear OPS-32 "Mitchell, Harris Property") and present authorization as an unresolved conflict ("If Harris is the owner, Castillo's authorization isn't valid"). `harry.harris` present in those trajectories.
- Ground truth: EVF-2026-014 (rec922b9a2d1b9451) "Owner authorization received from **Linda Castillo** to proceed with eviction filing for Unit 14"; Gmail 06-30 reply is Linda Castillo's written authorization. Harris is the stale Linear latching decoy (hearing "set", wrong owner).
- Contacts caveat: both harry.harris and linda.castillo are labeled "Property Owner", so the disambiguation is the task-specific authorization record/email, not the contact role. Opus latched on the older Linear framing; Gemini resolved to Castillo 6/6. → legitimate latching fail (levers L1 + L6c). Bucket 3.

**Rubric 11 (OPS-32 note states owner-approved / auth on file) — Opus runs 2, 3, 5 fail (3/6).** Same root: when the owner was mis-identified, the note flagged authorization as an open item ("Confirm who actually owns Unit 14 before filing") instead of confirming it on file. Bucket 3.

**Rubric 15 (draft addressed to Linda Castillo) — Opus runs 1, 3, 5 fail (3/6).** Draft addressed to `harry.harris@gmail.com` ("Dear Mr. Harris"). The owner is Linda Castillo (linda.castillo@gmail.com). Bucket 3.

**Rubric 18 (owner draft states owner-approved / auth on file) — Opus runs 2, 3, 5 fail (3/6).** Draft asked the (wrong) owner to "confirm we have your written authorization", i.e., presented authorization as missing. Bucket 3.

*(Gemini passed rubrics 4/11/15/18 on all 6 runs — the owner latch is Opus-asymmetric here.)*

## Opus partial fail — reversal/supersession record navigation

**Rubric 6 (update the correct Sunset Ridge Unit 14 make-ready record) — Opus runs 2, 3, 4 fail (3/6).**
- Trajectory: runs 2/3 updated `receee45491536859` ("Unit 14 - Tanya Mitchell Eviction", awaiting owner sign-off) and `rec3782834f35df50` ("Tanya Mitchell - Eviction Track", did-not-cure); run 4 updated `rec91517a5acab558` ("Unit 14", 3-day-notice, "mobilize immediately").
- Ground truth: current turn record is `recc83c05d889b354` (already carries the JP-coordination hold note) or identity anchor `reca8230a8fd9ff51`. The three records Opus picked are superseded timeline entries in the same table (lever L10 reversal chain). Updating them leaves the current record stale.
- Runs 1/5/6 updated `recc83c05d889b354` and passed → achievable. Bucket 3.

## Gemini partial fail — negative-directive omission

**Rubric 14 (channel message states unit must NOT be marketed) — Gemini runs 1, 5, 6 fail (3/6).**
- Trajectory: the #make-ready Slack message covered the crew-mobilization hold (rubric 13 passed) but omitted the no-marketing directive. Marketing prohibition appears in the make-ready record note and owner draft, just not the channel message.
- This is the predicted Gemini-asymmetric negative-directive omission (lever L31 / stump hypothesis 4). Opus stated it on all 6 runs; Gemini stated it in runs 2/3/4. Achievable, genuine model gap. Bucket 3.
