# Todos — S1.5 (Linter Blocker)

- [x] Run phase-readiness gate (`phase_ready.py --phase s1.5`) — OK, 1/1 upstream artifact present
- [x] Create `_aux/Todos_s1.5.md` (this file)
- [x] Create `_aux/Reads_s1.5.md`
- [x] Detect mode — **CB-mode** (`_aux/Universe_Split/` present; `6_Oracle_Events.txt` and `7_Rubrics.json` are unfilled placeholders, so no candidate-prefilled artifacts). Fixes, if any, land in `5_Prompt.txt` in place.
- [x] Classify the block — **Class A** (business-function / persona-authority / universe-rule misalignment). No similarity finding, so no Class B leg.
- [x] Re-grep each cited finding against `_aux/Universe_Split/` + base-universe docs
  - [x] F1 owner identity (Linda Castillo vs Robert Finley on Mesa Vista 4C)
  - [x] F2 QuickBooks in the Onsite PM lane (reads on AP bills + owner-invoice correction)
  - [x] F3 "invented Airtable field" for final owner cost
  - [x] F4 owner-billing authority at the Onsite PM tier
- [x] Classify the linter per finding — all four **clearly wrong** (universe evidence contradicts each)
- [x] Decision: **INVALIDATE, prompt unchanged**
- [x] Write `_aux/Linter_Justifications.md` (Class A template, reviewer voice)
- [x] Run `check_justification.py` — exit 0 required
- [x] Append entry to `Tasks/_meta/Linter_Justifications.md`
- [x] Write `_aux/Linter_Decision.md`
- [x] AUDIT — **skipped, correctly**: justification-only resolution, no prompt edit, so there is no new artifact to audit (S1.5 step 8)
- [x] STOP gate — end response, no OE drafting in this chat
