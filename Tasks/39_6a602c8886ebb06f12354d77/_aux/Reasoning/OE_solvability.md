# S2 OE Solvability + Coverage — Tasks/39_6a602c8886ebb06f12354d77 (StarPM V4)

## OE-to-prompt coverage (forward + reverse, both clean)
| Prompt ask | OE step(s) |
|---|---|
| figure out where 8D really stands / confirm each piece actually landed | OE1-7 (discovery + reconciliation) |
| run down whatever it is waiting on and get it moving so it can genuinely close | OE7 (identify blocker) + OE8 (advance) |
| square up what we have logged so it matches reality | OE9 (correct stale make-ready row) |
| post an update in the make-ready channel | OE11 (Slack C004) |
| draft John an email (where it stands / outstanding / what it takes) | OE10 (resolve John) + OE12 (Gmail draft) |

Reverse map clean: every OE traces to a real prompt ask. No scope creep.

## OE-to-rubric mapping preview (for S3)
- OE8 (save_comment OPS-227) -> Outcome 1.1: agent advanced the disposal blocker (requested John Smith's parts approval for the full disposal replacement). [F1: phrase channel-agnostic. Linear comment on OPS-227 OR Slack-to-John are both valid; do NOT lock the method.]
- OE9 (update_records_for_table tblMakeReady) -> Outcome 1.1: make-ready record corrected so no 8D row still reads Ready / cleared-for-leasing. [F2: target the OUTCOME, not record id receb057b02f20052.] Guard: MT-2026-1271 stays OPEN. Do NOT write a rubric that rewards marking the ticket complete while the disposal is unresolved.
- OE11 (slack_send_message C004) -> Outcome 1.1 (posted true 8D status in #make-ready) + Outcome 1.2 content (not-ready + disposal-awaiting-parts-approval).
- OE12 (create_draft to john.smith@starpm.com) -> Outcome 1.1 (draft created) + Outcome 1.2 content (where 8D stands / what is outstanding = the disposal / what it takes to finish = approve + install + final walk). Gmail is draft-only.
- 2.1 (tell-me facts): the prompt routes the "straight story" to John via the email + Slack (not a chat reply to the requester). So the reportable facts live in the OE11/OE12 content rubrics (1.2). S3 to confirm whether a standalone 2.1 is warranted.
- OE1-7, OE10: pure discovery / dependency lookups -> no rubric (the Outcome rubrics prove the reads happened).
- Optional (Council B + AUDIT note): a correct-unit-isolation rubric guarding against 204B / Rio Bend 214 (MT-2026-1325) confusion.

## Density
Per-model midpoint ~44 (Hardness Plan 48.5, Council B 40-48, AUDIT 44). StarPM V4 band (40 design / 15 floor, per model) -> PASS. Lean-correct floor ~20; watch platform runs (F6) but never < 15 for a correct solve.

## Gate results
- validate.py --phase oe: PASS (0 fails, 0 warns, 3 benign notes)
- verify_universe_atoms.py: 7/7 PASS
- Council A grounding: GO
- Council B adversarial: GO (OE Completeness 5/5, OE Accuracy 5/5)
- AUDIT (strict): PASS (STRICT) — 62/62 regression anchors, all 5 levers trace prompt+OE+atom, density 44/model

## S3 carry-forward (from Council B + AUDIT findings register)
- F1: advance-blocker rubric channel-agnostic (Linear comment or Slack-to-John).
- F2: record-correction rubric outcome-focused, not record-id-locked.
- Guard: MT-2026-1271 must remain OPEN (no false-completion reward).
- Optional: correct-unit-isolation rubric (204B swarm + Rio Bend 214 twin).
