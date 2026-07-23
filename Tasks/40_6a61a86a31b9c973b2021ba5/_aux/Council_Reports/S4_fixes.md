# S4 Fixes — Bucket 1 (Rubric Invalid)

## Summary
**Hard defects: 0.** No rubric fails the 5-point checklist as an unfixable design defect.

**Soft refinement suggestions: 2** (non-blocking; documented so a future rebuild can adopt them for slightly better atomicity).

---

## Refinement 1 (soft, non-blocking) — R5 atomicity

**Current rubric:** "The Agent's update to Airtable ticket rec92f4a1c8e17bd3 revises fldDescription to note the active leak with occupants at home (or similar phrasing)."

**Concern:** the criterion bundles two distinct atoms — (a) active leak, (b) occupants at home. Under the V4 July 2026 atomicity update, single-narrative-claim bundling is defensible when the two atoms travel together as a single safety context, but partial coverage is penalized against the intent.

**Evidence:** all 6 Gemini runs include the leak atom but drop the occupants-at-home atom. Under strict atomicity, Gemini would pass the leak sub-atom and fail the occupants sub-atom (1/2), rather than failing the bundled rubric outright. Opus 5/6 runs pass by including both atoms, showing the bundled criterion is achievable.

**Proposed split (future task template, not required for this rebuild):**
- 5a: "revises fldDescription to note the active leak on the kitchen floor (or similar phrasing)"
- 5b: "revises fldDescription to note that occupants are at home (or similar phrasing)"

**Why non-blocking:** the current rubric is defensible as a single safety-context claim (the "kids-home + water-pooling" scenario travels as one urgency signal). Opus proves it is achievable. Gemini's consistent atom drop is a real coverage gap, not a rubric defect. Bucket 3 classification for the Gemini failures stands.

---

## Refinement 2 (soft, non-blocking) — R21 atomicity

**Current rubric:** "The Agent's comment on Linear issue OPS-231 notes active water pooling with occupants at home (or similar phrasing)."

**Concern:** same bundling as R5 (active pooling + occupants at home).

**Proposed split (future task template):**
- 21a: "notes active water pooling on the kitchen floor (or similar phrasing)"
- 21b: "notes occupants are at home (or similar phrasing)"

**Why non-blocking:** identical reasoning to R5. The current rubric is defensible; Gemini's consistent atom drop is legitimate model failure.

---

## Classifications NOT eligible as Bucket 1

Every failing rubric was tested against the 5-point checklist:

1. Self-contained + atomic + universe-grounded — PASS for all 21 failing rubric × run combinations (R5 and R21 have soft atomicity notes above but are defensible).
2. Flexible enough for valid alternatives — PASS. `(or similar phrasing)` is present on every content rubric.
3. Required by prompt — PASS. Each failing rubric traces back to a specific prompt clause (`"Bring the maintenance ticket current"`, `"Update the operations tracking issue"`, `"drop a note walking through the rationale"`, `"Drop back into the tenant thread"`, `"Draft Diane the revised confirmation"`, `"Robert a heads-up on the cost"`, `"put the install on my calendar"`).
4. Real tool names + valid parameters — PASS. `slack_send_message` (send, not draft), `save_issue`, `save_comment`, `update_records_for_table`, `create_draft`, `create_event` are all real StarPM tools. The R23 rubric explicitly requires the send tool over the draft tool per the V4 StarPM tool-trap warning.
5. Achievable by a capable agent — PASS on all rubrics. The cross-model divergence pattern (Opus AF on R23–R26 but Gemini passes 6/6; Gemini AF on R5 but Opus passes 5/6) is decisive proof that every failing rubric is achievable — a peer model does achieve it.

No Bucket 1 hard-defect fixes required for the shipped 7_Rubrics.json.
