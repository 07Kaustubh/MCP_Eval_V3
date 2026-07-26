# Bucket 2: Judge Error

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Basis:** `8a_Verifier_Fails_Opus.txt` + `8b_Verifier_Fails_Gemini.txt` as re-exported 2026-07-26 12:04, cross-walked against `Agent_Responses/{Opus,Gemini}/`.

> **Supersedes** `_superseded/S4_judge_errors.md` (written against an earlier, non-matching `8a` export).

**6 criteria of 52 failing criteria are Bucket 2.** They account for **16 disputed run-cells** out of 403 fail cells across the two models (4.0%). A further **5 disputed cells** sit under criteria whose overall bucket is 3 and are listed at the end, so the pattern is visible without inflating the Bucket 2 count. That is **21 judge-error cells** in this report; one further contested cell (the first-person self-reference on Opus run 2) is a rubric-phrasing false fail and is documented in `S4_fixes.md` instead, for **22 contested cells in total, 20 of them on Gemini**. Every entry below carries the exact artifact text the judge said was absent.

---

## B2-1: Draft states the earlier QC sign-off does not hold (idx 49)

**Fail record.** Opus 0/6 · Gemini 2/6 (runs 1, 2). Both Gemini cells are disputed.

- `Gemini Run 1, tool call 79 (create_draft)`, body: "My earlier QC spot-check sign-off from late May applied only to the initial HVAC run and **DOES NOT HOLD** for the overall Preventive Maintenance Push. On the Quality Control side, this push is NOT a pass, and it should NOT be treated as closeable yet."
  Judge: "The draft email does not plainly state that Jaime Salinas's earlier QC sign-off does not hold. The agent's summary describes itself as containing this statement, but the actual draft content as described marks records as Done and does not retract the sign-off."
  The judge graded the agent's Linear writes rather than the draft body. The criterion's evidence scopes it to the draft body.

- `Gemini Run 2, tool call 72 (create_draft)`, body: "To be direct and unequivocal: **MY EARLIER MAY SIGN-OFF DOES NOT HOLD FOR CLOSING OUT THIS INITIATIVE**, AND THE PREVENTIVE MAINTENANCE PUSH CANNOT BE TREATED AS CLOSEABLE YET."
  Judge: "framing the QC side as a pass rather than a retraction."

**Verdict.** Both cells are false fails. The retraction is the first substantive sentence of each draft, in capitals in both.

---

## B2-2: Draft states the push should not be treated as closeable yet (idx 50)

**Fail record.** Opus 0/6 · Gemini 2/6 (runs 1, 2). Both disputed. Same two drafts, same sentences: run 1 "it should NOT be treated as closeable yet"; run 2 "THE PREVENTIVE MAINTENANCE PUSH CANNOT BE TREATED AS CLOSEABLE YET". Judge for run 2: "The agent's summary and email treated the push as substantially closeable with only plumbing and minor West cluster work remaining." The draft's own prerequisite list requires South plumbing execution, West cluster completion and a QC re-inspection before close, which is the opposite of closeable.

**Verdict.** Both cells are false fails.

---

## B2-3: Channel update reports the plumbing findings including the two water heaters as still open (idx 36)

**Fail record.** Opus 0/6 · Gemini 3/6 (runs 2, 4, 5). All three disputed.

- `Gemini Run 2, tool call 71 (slack_send_message, C001)`: "*3. South Cluster - STATUS: IN PROGRESS / OPEN ITEMS* ... **Plumbing (OPEN):** Field inspections flagged items requiring tech work onsite. **2 Water Heater Replacements** (past serviceable life) - Logged in maintenance ticket log as *MT-2026-1327*".
- `Gemini Run 4, tool call 90 (slack_send_message, C001)`: "`MT-2026-1327`: Replace 2 aging water heaters past serviceable life (High Priority)" plus "**Overall Status**: The PM Push remains **OPEN** until West Cluster PM scope is finished and South Cluster plumbing repairs are completed."
- `Gemini Run 5, tool call 59 (slack_send_message, C001)`: "**South Cluster**: **HVAC & Electrical Complete; Plumbing Field Follow-Up Open**. Field items flagged during Carlos's plumbing walk (2 water heater replacements, hose bib repairs) ... require tech dispatch."

**Verdict.** All three cells are false fails. Each post names the two water heater replacements and states they are open.

---

## B2-4: Final response reports the plumbing findings including the two water heaters as still open (idx 56)

**Fail record.** Opus 0/6 · Gemini 2/6 (runs 2, 5). Both disputed.

- `Gemini Run 5, final response`: "**South Cluster**: **HVAC & Electrical Complete; Field Follow-Up Open** ... Plumbing audit flagged 2 water heater replacements and exterior hose bib repairs, plus 2 condensate drain flushes requiring on-site tech work."
- `Gemini Run 2, final response`: "**New Tracking Items Raised for Open Work**: `OPS-1000`: *South Cluster Plumbing Follow-up: Water Heater Replacements & Hose Bib Repairs* - Assigned/Owned by **Carlos Mendez**" and "Created `MT-2026-1327` (South Cluster Water Heater Replacements) ... so technicians can execute the required onsite work."

**Verdict.** Both are false fails. The run 5 cell is unambiguous. The run 2 cell is the weakest entry in this report: the water heaters are named under a heading that reads "Open Work" and the response says technicians still have to execute, which satisfies the criterion, but the response never uses the word open in a sentence of its own about them.

---

## B2-5: Draft names the person holding the West cluster work (idx 47)

**Fail record.** Opus 2/6 (runs 2, 5, both genuine) · Gemini 3/6 (runs 2, 5, 6, all three disputed).

- `Gemini Run 2, tool call 72 (create_draft)`: "Open Work & Owner: **Lisa Smith** owns the remaining West Cluster PM scope (plumbing, electrical checks, and property-level walkthroughs). Tracked in Linear as OPS-1001."
- `Gemini Run 5, tool call 60 (create_draft)`: "#### 4. West Cluster ... Who is Holding It: **Lisa Smith** (Onsite Lead)."
- `Gemini Run 6, tool call 91 (create_draft)`: "#### **4. West Cluster** ... Who is Holding It: **Lisa Smith** (Onsite Cluster Lead) / **Brooke Phillips** (Project Lead)."

The run 6 justification is visibly defective on its face: it reads "The draft presents North cluster as fully closed and does not discuss outstanding tenant access work or name an owner for it. No one from Carlos Mendez, Elias Navarro, or Tony Reyes is named as holding tenant access work." That is the tenant-access criterion's accept-set applied to the West cluster criterion.

**Verdict.** Three false fails. The two Opus cells are genuine: neither draft contains a West cluster section at all.

---

## B2-6: Final response reports the South electrical panel inspections as recorded finished (idx 58)

**Fail record.** Opus 4/6 (runs 1, 2, 3, 5) · Gemini 4/6 (runs 1, 2, 4, 5). Four cells disputed.

- `Opus Run 1, final response`, cluster table: "| **South** | Electrical done; plumbing open | ... | **OPS-186 -> Done**; ticket **MT-2026-1328** |". Judge: "this is about the electrical being done generally, and does not reference OPS-186 recording the electrical panel inspections as complete." OPS-186 is named in the same table row.
- `Gemini Run 1, final response`: "**South Cluster**: **HVAC & Electrical Complete; Plumbing Field Repairs Open**. Electrical panel inspections (Patricia) and HVAC run (Elias) are finished."
- `Gemini Run 4, final response`: "**South Cluster Electrical**: Updated `OPS-186` to `Done` with a comment confirming Patricia Nguyen's completion of electrical panel inspections."
- `Gemini Run 5, final response`: "HVAC service (`OPS-43`) and electrical panel inspections (`OPS-186`) are complete and marked `Done`."

The criterion's evidence already states that naming the record identifier is acceptable but not required and that a response reporting the inspections as recorded finished satisfies it. The judge instead required a meta-framing that separates the record's claim from the work. Two runs on each model passed the same criterion, so the bar is reachable as written.

**Verdict.** Four false fails. The other four cells are genuine: Opus run 2 never retrieved OPS-186, Opus runs 3 and 5 reported electrical as only partially complete or as North panel notes only, and Gemini run 2 folded OPS-186 into an undifferentiated list of records advanced to Done. **No rubric fix is proposed**, because the only wording change that would help would drop the recorded-as hedge and thereby assert as verified fact a completion that lives in a record still sitting in Todo.

---

## Disputed cells under Bucket 3 criteria

Logged for appeal, not counted in the Bucket 2 total.

| Criterion | Cell | Artifact text the judge said was absent |
|---|---|---|
| Crew recorded East HVAC service complete (idx 59) | Gemini run 1 | Final response: "**East Cluster**: **Complete**. Coil cleanings and filter swaps finished by Elias Navarro". The evidence says naming the coil cleaning alone satisfies the criterion. |
| Crew recorded East HVAC service complete (idx 59) | Gemini run 6 | Final response: "**East Cluster (Status: CLOSED - Fully Complete & Passed QC)** ... 100% complete across all assigned properties". The judge conceded the completion is stated and failed it for not separating crew record from QC confirmation, which the criterion does not ask for. Weaker than the run 1 cell. |
| Draft names the East QC holder (idx 48) | Gemini run 5 | Draft: "#### 3. East Cluster ... Who is Holding It: **Jaime Salinas** (QC Inspector)." |
| Draft states East QC must be confirmed before close (idx 43) | Gemini run 5 | Draft: "Action Needed to Close: Jaime Salinas conducts final QC spot-check walk and logs passing verification on `OPS-1002`", under a section headed "Cluster-by-Cluster Status & Closeout Requirements". |
| Final response reports East QC unconfirmed rather than complete (idx 55) | Gemini run 5 | Final response: "**East Cluster**: **HVAC Complete; Final QC Pending** ... `OPS-1002` (Assigned to Jaime Salinas for final QC spot-check verification)." |
| Channel update reports the end-of-June target passed with work open (idx 28) | none | Listed only to record that this criterion's single Gemini fail was checked and is genuine: run 2's post never mentions the end-of-June target. |

---

## Judge-consistency observation (not a bucket entry)

The West cluster tracking-item criterion (idx 3) passed `Gemini Run 1` on an item titled "West Cluster - Preventive Maintenance Push Completion & Final Scope" whose description ends "before final QC sign-off", and failed `Gemini Run 2` on an item titled "West Cluster PM Push - Complete Plumbing, Electrical & Final PM Scope" with no QC wording. The distinction rests on four words. It is recorded here because it runs in the pass direction, so it is not a false fail and needs no appeal, but it shows the same criterion being graded at two different strictness levels within one model's run set.
