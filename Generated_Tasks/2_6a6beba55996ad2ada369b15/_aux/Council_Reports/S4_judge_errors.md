# S4 judge errors — Bucket 2

Task `2_6a6beba55996ad2ada369b15` · universe **harmonygames** · model **Claude Opus 4.8** · pass 2.
Export pinned at entry: `8_Verifier_Fails.txt` `ad0260ca6682ad47…` 55,564 B, per-run [17, 19, 21, 20, 19, 22]; `7_Rubrics.json` `bf26e5373d7fbab6…` 13,703 B.

Tool-call numbers in this file count the Nth `tool_use` block in that run's trajectory, in order. Pass 1 used a different numbering; the two are not comparable.

## Count: 2 — one wrong FAIL, one wrong PASS

---

## 1. Criterion 17 — #winddown message, continuing spend. **Run 5. Wrong FAIL. Appeal this cell.**

**Grader wrote:** "The posted Slack message does not include the ~$8,447 post-Feb-10 continuing spend figure. The three points in the message cover DAU/engagement, total acquisition spend, and data proceeds — the continuing UA spend figure after the stop decision is absent."

**Trajectory citation.** Run 5, tool call 58: `slack_send_message`, `channel: "C0ADGSZKR3R"`, text point 2 reads:

> *We are still bleeding cash that the cancellation list missed.* Paid UA on all three apps has been charging every day from 10 Feb through today — *$8,447 since the 9th* (~$445/day, still live): Domino $5,574, Combo Fighter $2,441, ZM3D $432.

The tool returned `{"ok": true, "ts": "1786042237.560055", "channel": "C0ADGSZKR3R"}` and echoed that text back. The figure the grader called absent is the second of the three points it enumerated, with the per-title split beside it. The criterion asks for approximately 8,447 charged across the studio's titles over the 19 days from 2026-02-10 and explicitly rejects only the 2,441 Combo Fighter subtotal in its place; Run 5 gives the studio figure first and the subtotal as a component.

**Not a rubric defect.** The same criterion passed Run 6 on materially the same sentence ("across all three titles it's $8,447 over 19 days"), and the same run's written account and tracking item both passed on the same figure. One cell, one model, no repeated misreading, so this is below the rule 16 reclassification threshold. The criterion is correct as written and the reading of this one cell is wrong.

**Effect if upheld.** Run 5 moves 19/28 to 20/28. It does not become a passing run, so pass@1 is unchanged at 0.0.

---

## 2. Criterion 7 — written account, ad-account owner. **Run 6. Wrong PASS. Do not appeal; recorded from the passing-cell audit.**

This is the step 1b finding. It runs in the lenient direction, so there is nothing to file with the platform, but it is the only cell in the export whose grading is structurally impossible and it must not be carried into any later count as a genuine pass.

**Grader wrote:** "The document names Leonard Hayes as the owner of the ad accounts, specifically stating he 'runs the Meta/FB ad account — set up the Combo Fighter FB app.'"

**Trajectory citation.** That string exists in Run 6, tool call 58, `linear_create_issue`, in the `description` field of issue DES-2438. It does not exist anywhere in Run 6, tool call 56, `gdocs_create_document`, which is the written account the criterion grades. The document's 7,104-character body names Leonard three times: once in its header line "For Leonard's angel conversations", once as joint owner of "GitHub, Deel, Gusto, Intuit, Linear", and once as owner of Carta. Its paid-UA section says "nobody went back and killed the ad accounts" and attaches no owner to them at all.

**Why the checker missed it.** `check_criterion_dependencies.py` exits 0 and correctly finds no cell where a dependent passed while its antecedent failed. This is not a dependency violation. It is an artifact-scope leak between two criteria that grade the same fact on two different surfaces: criterion 7 on the written account, criterion 21 on the tracking item. Run 6 satisfied the tracking-item one and was credited for both.

**Consequence for the classification.** Criterion 7 fails 5/6 in the export and 6/6 on the trajectories. It is classified Bucket 3 on the five cells the export actually fails, and it is flagged in `S4_verdict.md` as the criterion most likely to become all-failing on the next export. The AF justification for it is drafted in `S4_fixes.md` section B rather than in the submitted batch, so it is ready if that happens.

**Cheap defence, cell-neutral.** Criterion 7's evidence field currently reads "Inspect the created page or document for the named owner attached to the continuing spend." Naming the surface it excludes would have prevented this. The suggested wording is in `S4_fixes.md` section B; it changes no cell in this export under a correct reading and is offered as a hardening, not as a fix to a defect.

---

## Considered and not filed

- **Criteria 12, 16 and 24, the coverage conclusion.** Runs 1, 5 and 6 fail all three; runs 2, 3 and 4 pass all three. The split is perfectly correlated across the three surfaces within every run, and it is identical to the split in the previous export on the same trajectories. A grader that was guessing would not reproduce the same six-run pattern across three criteria twice. The failing runs are also substantively wrong rather than merely hedged: each of them nets Unity and Singular to zero on an insolvency waiver that the record shows is requested and unanswered, which is what lets them write "roughly cash-neutral". Legitimate fails.
- **Criterion 5, runs 4 and 6.** Both wrote "~800" for a peak of 801. Run 6 had the exact value in hand at tool call 33, which returned `["2026-02-07", "801"]` as its top row, and softened it on the way to the page. Run 4 never computed it; it pulled the raw per-date, per-platform series at tool call 25 and eyeballed the total. The grader applied the criterion the same way on both, and on the three runs that reported the wrong day's figure. Consistent, so not a judge error. The over-specificity question is argued in `S4_fixes.md` section A and resolved against changing the criterion.
- **Criterion 25, runs 2 and 3.** Both state 10,800 and 2,500 separately and neither sums them. The criterion asks for the funds available figure of 13,300. Correctly graded.
