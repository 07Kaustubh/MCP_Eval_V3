# Platform Review Diagnosis — Task 39 (Las Palmas 8D make-ready)

**Task:** Tasks/39_6a602c8886ebb06f12354d77  ·  Universe: StarPM (V4)
**Persona / function:** James Bennett — Assistant Maintenance Technician / Maintenance & Repairs
**Platform reviewer verdict:** f3b9ed — **Poor 2/5**, Level of fixes = **full redo**, Parts fixed = **none**
**Attempt id:** 6a614f63de351e29a7249257 (platform id-space; does not map to a local dir hex)

## Trajectory reality (Validators/parse_trajectories.py)
- 12/12 runs completed. Avg total tool calls **38.2** (>= 15 floor OK; below 40 design target). pass@1 = **0.0** (0/6 opus, 0/6 gemini).
- pass@1 = 0.0 is NOT a difficulty pass — it means the 15-rubric set is effectively **unsatisfiable in practice** (no run cleared all 15). This is a VALIDITY failure, not density/difficulty.

## We injected nothing
- `4_Changelog.json` = `[]`; `9_Universe_inject.sql` (73 lines) contains zero Las Palmas/8D/carpet/disposal/make-ready content.
- => Every contradictory row + the carpet calendar event is **base universe**, which V4 forbids editing/deleting. The candidate built a task on top of a messy pre-existing situation without reconciling it.

## Reviewer claims — ALL VERIFIED against ground truth
1. **Three make-ready rows, prompt names none.** tblMakeReady rows for "Las Palmas 8D":
   - `receb057b02f20052` selReady, moveOut/targetReady **2026-05-01**, notes "Turn closed out... carpet cleaned and sealed, deep clean complete, QC punch-list resolved... cleared for leasing."
   - `recf7aecc318b2252` selProg, moveOut **2026-05-01**, notes "three days into in-house make-ready" (contradicts the *closed* row at the SAME move-out).
   - `rec651427ec0d84dd5a` selProg, moveOut **2026-06-18**, targetReady **2026-06-26**, fridge swap 6/25, "critical path (lease signing pending)."
   Prompt says "square up what we've got logged" with no named row. OE 9 + R2/R3/R4 force the **May** row `receb057b02f20052`. Opus (run1) updated it; Gemini (run1) did not — matches reviewer's 5-vs-7 split.
2. **One turn or two.** Two rows moveOut 5/1, one moveOut 6/18/targetReady 6/26 => defensible "two turns" reading (May turn closed 5/29; new turn after 6/18 moveOut). If May turn really finished, flipping receb057 back to In Progress is the WRONG write. Base data; not cleanable.
3. **MT-2026-1271 conflation.** recac236210094352, created 2026-05-01, fldCompletionDate "" (blank), scope = carpet staining + dripping faucet + scuffed walls — all done per Slack. 4 Gemini runs reasonably CLOSED it; no rubric scores that. R14 rewards "still open." One data setup, one rubric rewards X and nothing catches not-X.
4. **PREMISE-KILLER — base-universe calendar event.** gcalendar `7zs34l6s84f23bg7bvwfsc9qie`, **confirmed**, tag "Maintenance / CapEx", "Vendor Walk-Through - A Plus Carpet, Las Palmas 8D", **2026-07-07 13:00 CT**, location Las Palmas 8D, organizer john.smith@starpm.com (accepted), attendee victor.rios@apluscarpetcleaningandrepairs.com. Universe today = 2026-07-01 => confirmed FUTURE carpet-replacement scoping. Carpet is NOT settled. Breaks R15 (carpet complete) and the "disposal is the only open item" spine (R7/R10/R13 + OE 7/11/12). No run found it — luck, not design.
5. **R6 over-reach.** R6 requires the Slack post to say 8D "should not be marketed or shown." Prompt never asks for that (only "post an update so the crew isn't working off old info"). 0/12 runs said it => fails every run. OE 11 invented the clause; the prompt does not.
6. **Non-atomic rubrics.** R15 bundles 5 items (repairs, carpet, deep clean, punch-list, fridge); R11 bundles 3 (approve+order, install, final walk). R3/R4 were split correctly — apply the same rule to R11/R15.
7. **May-1 row temporal impossibility.** receb057 (dated 5/1) reports carpet/deep-clean/QC finished, but Slack (OE 4) shows that work happening 5/15–5/29. A record cannot report work that has not happened yet.

## Root diagnosis
The scenario's central answer ("8D is nearly ready; the disposal is the only open item; correct the one stale record") is FALSE against un-editable base universe: (a) carpet is mid-CapEx-rescope (7/7 A Plus Carpet walk), so there are >= 2 open items; (b) the target record is irreducibly ambiguous (3 rows / two turns, a "closed" and an "in progress" row sharing moveOut 5/1); (c) MT-2026-1271's scope is done, so "keep it open" is not clean. Rubrics compound it (R6 over-reach, R11/R15 bundling, R14 one-sided). No surgical rubric edit can rescue a premise the base universe contradicts.

## Recommended action
FULL REDO (rebuild 5/6/7 as a fresh CB), because the premise is unsalvageable on this universe.
- **Design fork A (recommended):** rebuild on a DIFFERENT clean maintenance scenario for James Bennett where exactly ONE record is the target and every service (incl. Calendar) is consistent. Fastest path to a valid 5/5; avoids irreducible base landmines.
- **Design fork B (faithful, riskier):** rework Las Palmas 8D so the TRUE answer is "two open blockers — seized disposal (OPS-227) AND carpet CapEx (7/7 A Plus walk)" with the exact current-turn record NAMED in the prompt and the stale rows as decoys. Turns the missed-calendar defect into the intended Opus-4.8 stump, but must design around the un-cleanable 3-row/two-turn ambiguity so rubrics don't false-fail.
- Reviewer forward guidance to bake into HARDNESS/S1/S3: before any rubric, confirm only ONE record matches the ask (else name it); search EVERY service incl. Calendar before claiming an "only open item."
