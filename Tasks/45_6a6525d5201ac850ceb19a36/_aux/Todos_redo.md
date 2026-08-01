# REDO Todos — Tasks/45_6a6525d5201ac850ceb19a36 (V4 / StarPM, CB-own task) — COMPLETE

REDO is destructive of in-place 5/6/7. Step 1 (confirm failure) is a HARD GATE.
Gate PASSED: difficulty fail confirmed (Opus pass@1 = 1.00, overall 0.75 > 0.40 ceiling).

- [x] 1. GATE: Confirmed failure from trajectories. Cross-checked _aux/Trajectory_Stats.json vs a
        fresh parse_trajectories.py run (both agree). Opus pass@1 = 1.00 (6/6 all 20 rubrics),
        Gemini 0.50 (3/6), overall 0.75. Verdict REBUILD_CANDIDATE_DIFFICULTY. Density secondary
        (avg 40.2 total; Opus 37.0 under the 40 per-model design target, above the 15 floor).
        -> _aux/REDO_reason.md written (56 lines): computed numbers + root cause + rebuild guidance.
- [x] 2. Archived to _aux/Candidate_Originals/: 5_Prompt.txt, 6_Oracle_Events.txt, 7_Rubrics.json,
        + 8a/8b verifier fails + Trajectory_Stats.json (failure evidence). Byte-verified before clear.
- [x] 3. Cleared in-place 5_Prompt.txt / 6_Oracle_Events.txt / 7_Rubrics.json (confirmed absent).
        _aux/ preserved (Universe_Split, Universe_Index, Fact_Ledger, Feasible_Surface, Hardness_Plan).
- [x] 4. 13_Feedback.txt written: FAIL on difficulty, worst dim overall pass@1 = 0.75 / Opus 1.00.
        Plain narrative, 0 em-dashes, no guide references. Retained universe + persona documented.
- [x] 5. Tasks/_meta/Learnings.md L36 present (singular): "A well-trapped universe contributes zero
        difficulty if the prompt names the traps; difficulty is withheld inference." Root cause =
        prompt leaked every discriminator. Universe atoms reusable; only prompt information content changes.
- [x] 6. STOP gate: response ends here. CB rebuild (HARDNESS -> S1 -> S2 -> S3 -> FINAL) runs in
        FRESH chats, one per phase. Not chained inside this REDO chat.
