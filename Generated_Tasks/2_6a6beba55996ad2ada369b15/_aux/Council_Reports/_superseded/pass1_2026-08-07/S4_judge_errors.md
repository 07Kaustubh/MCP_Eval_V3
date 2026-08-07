# S4 judge errors — Bucket 2

Task `2_6a6beba55996ad2ada369b15` · 6 runs · 14 failing criteria walked.

## Count: 0

No failing cell in this export is a judge error. Every judge justification checked was consistent with what the trajectory actually shows, including the four criteria whose target value the environment cannot serve. On criteria 4, 6, 17 and 20 the graders correctly reported that the agent's figure was not the figure the criterion named; the fault is in the criterion, not the reading.

## Considered and reclassified rather than filed

### Criterion 10 — the wind-down service cost, runs 1, 3 and 6

On its face this is the strongest judge-error candidate in the export. Run 2 wrote "Legal / managed wind-down … ~$13,000 in February alone" and passed. Runs 1, 3 and 6 wrote the same 13,000 from the same `FINANCE.EXPENSES.MONTHLY_BURN` row (Run 1: "Wind-down legal | ~$13K | Booked in Feb burn"; Run 3: "Feb wind-down legal | $13,000 | Already paid from cash"; Run 6: "Wind-down legal: ~$13,000 booked in February") and failed. Under `Evals_harmonygames/4_Verifier_Fails_Eval.md` Phase 3.3 cross-run comparison, three failing runs that did what the passing run did reads as judge inconsistency.

It is filed as a rubric defect instead, per `AGENTS.md` rule 16. The criterion accepts "approximately 13,000 to 15,000" and the universe carries an unrelated February legal line of exactly 13,000 on a table every run queried, so the accepted band cannot discriminate the intended discovery from the collision. Four cells turn on which words the agent put next to the same number. An appeal would win three cells and leave the band intact for every future run; the fix in `S4_fixes.md` section B binds the figure to its subject and closes it permanently. Note that the correct direction of the inconsistency is the reverse of the usual one: the outlier is run 2's PASS, not the three FAILs, and the rewrite makes the criterion 6/6 failing.

### Criterion 5 — peak daily active users, run 6

Run 6 retrieved the exact answer. Tool call 81, `SELECT date, SUM(dau) dau … GROUP BY date ORDER BY dau DESC LIMIT 5`, returned `["2026-02-07", "801"]` as its first row. The agent then wrote "Peak ~800 daily active users" in the document. The criterion names 801 and OE 24 makes 801 the graded engagement figure, so the fail stands: the agent had the value in hand and softened it on the way to the page. This is a legitimate model failure, not a judge error.

### Criterion 27 — licensing rather than sale, run 4

The written account used "Data-licensing deal" correctly, so the fail looks harsh until the evidence field is read. That field scopes the criterion to the written account and the final response together, and Run 4's final response says "the data sale lets us close roughly cash-neutral". The grading is correct as the criterion is scoped.
