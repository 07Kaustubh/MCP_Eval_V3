# Learnings — Opus 4.8 Failure Modes (append-only)

Empirical findings about what reliably stumps Opus 4.8 on Brookfield tasks, distilled from cross-task iteration evidence. **Read this before PIPELINE HARDNESS on every new task.** Append new findings here after every S4 verifier-fails analysis so future tasks compound on prior learnings.

Each entry: numbered finding → empirical evidence → design rule.

---

## What does not reliably fail Opus 4.8 (DO NOT rely on these alone)

### L1. Confirm-already-done tasks (100% pass)
If the answer already exists in a system of record and the agent just looks it up + reports, Opus 4.8 passes every time. Even with misleading conversational chatter ("it is still in the queue"), the agent checks the GL and correctly concludes "already posted."

**Rule:** The correct answer must require DERIVING something the agent can get wrong, not merely confirming a posted state.

### L2. Single-hop reductions (~80% pass)
One reduction (e.g. "the $24,000 was collected, so write off $9,500 not $33,500") is reliably found — the GL JE surfaces in the first period query, and a buried Slack reply usually states the answer explicitly anyway.

**Rule:** A single hop from "wrong number" to "right number" is too discoverable. Multiple hops where each system holds a different piece are needed.

### L3. Two reductions with both keyword-searchable (~60% pass)
Adding a second reduction buried in the subledger (e.g., a $1,500 credit memo not in GL) helps, but if the memo is findable via simple keyword search ("Larkspur" in subledger descriptions), determined agents still find it.

**Rule:** Two layers are better than one — especially across services the agent might skip — but a competent agent's keyword search still cracks it.

### L4. Near-miss entity confusion alone (~0% fail)
All Brookfield runs handled Larkspur Retail vs Larkspur Realty correctly. Two-name traps are not enough on their own.

**Rule:** Near-miss entities are a flavor lever, not a difficulty lever. Combine with structural difficulty.

### L5. Action-incompleteness traps alone (~0% fail)
All runs reliably did the email + Slack + reminder. Agents are thorough on writes.

**Rule:** Asking for many write actions does not produce failures. Diversify writes for tool-call density (40+), not for stumping.

### L6. Correction emails that state the right answer (100% pass)
Adding a correction email that explicitly says "the correct figure is $X, not $Y" is useless — agents read full email threads to every depth and find it.

**Rule (HARD):** NEVER put the correct answer in any email, Slack message, messaging DM, or document body. If the correct answer appears as text in any searchable artifact, Opus 4.8 will find it. The answer must be DERIVED from raw data, not stated.

### L7. Binary "is it posted?" traps (100% pass)
Tasks where the correct answer is "the JE is not there" pass every time. The agent's first move on any financial-readiness question is `oracle_gl_list_journal_entries` or `oracle_gl_get_account`. A missing JE is trivially detected.

**Rule (HARD):** Never design a task where the correct answer is "it is not there." Put WRONG data in the GL that looks right, so the agent finds something and stops investigating.

---

## What reliably fails Opus 4.8 (use these as the hardness levers)

### L8. Three reductions across three different services (~40% pass — the target)
Stacking reductions across structurally different systems produces the target failure rate:
- Layer 1: Oracle GL (the agent usually finds this)
- Layer 2: SAP subledger (the agent almost never finds this — see L10)
- Layer 3: SAP subledger different account + email + Records Vault (sometimes found)

Agents fail in diverse ways: some skip the GL, some skip the subledger, some find-but-misapply.

**Rule:** Stack reductions across DIFFERENT structured systems, each requiring a different search strategy. Three layers is the ceiling — a 4th crosses into precision-stacking contrivance.

### L9. Authority-figure dismissal (~100% fail, most effective single mechanism)
After planting reductions, add a PLAUSIBLE but WRONG dismissal from an authority figure (the person who originally calculated the number, or a senior reviewer) explaining why the reductions "do not matter" using domain-correct-sounding reasoning. Opus 4.8 defers to the authority and dismisses the reductions it found.

Example pattern (from a real Brookfield task): "those items are settlement activity against the payable balance, not provision adjustments — they move cash position on 230000 but do not change the SALT provision calculation."

**Rule:** Plant the dismissal AFTER planting the reductions. The frame must be plausible to an accounting-literate reader but wrong for the specific situation. The agent must have enough domain reasoning to reject the frame, which Opus 4.8 does not.

### L10. SAP subledger invisibility (~0% find rate)
Across 6 trajectories on one task, 0/6 agents ever called `sap_subledger_list_subledger_transactions` or any SAP tool. Agents check Oracle GL and conversational surfaces (email, Slack, messaging) but almost never query the subledger unless explicitly told to. Even an in-task Slack hint mentioning "a credit posted to 230000" did not trigger a subledger query.

**Rule:** Place at least one critical reduction in the SAP subledger with no corresponding GL entry. This is the single most reliable "service skip" in the Brookfield universe.

### L11. Structured-source vs conversation skip
Agents skip either Oracle GL OR SAP subledger but not both. If the conversational chatter is rich, the agent uses it as a substitute for one of the structured queries.

**Rule:** The strongest traps put the load-bearing answer in a system the agent has no conversational reason to query.

### L12. Thread-reply invisibility (~40% miss rate)
Agents find parent messages easily; thread REPLIES are missed ~40% of the time. A reply that flips the conclusion of the parent is a strong lever — but not as strong as L9 + L10.

**Rule:** Bury the resolution in a thread reply, not the top message. Stack with L9 / L10 — alone it's only moderate.

### L13. First-framing trap (consistent leverage)
The first explicit figure the agent reads anchors strongly. Subsequent reductions need explicit, structured evidence to override the anchor.

**Rule:** Anchor the wrong number in 3+ conversational places (email + Slack + GL JE). Agents must traverse the full evidence chain to override it.

### L14. Correct-observation / wrong-conclusion
Agents find the evidence but reason incorrectly about its effect. E.g., finds a $1,500 credit memo, reasons "this resolved the dispute" rather than "subtract this from the figure."

**Rule:** Design situations where the right reasoning step requires domain knowledge (right-of-setoff, ASC 606 deferred revenue release, IOLTA segregation). Add an explicit instruction from a credible source to collapse ambiguity if needed.

---

## Prompt design rules (empirically validated)

### L15. Implicit prompts only
An explicit hint ("I have a feeling something moved, do not just trust the number") gives agents a head-start and they find the reduction. An implicit prompt ("figure out the write-off, get George set up to book it") with NO hint that the circulating number is wrong forces self-initiated discovery, which many fail.

**Rule (HARD):** Never hint that the answer is wrong. The persona should believe the number and ask the agent to execute, not investigate.

### L16. Persona believes the wrong number
Frame the prompt from the perspective of the person anchored on the wrong figure. The agent's job is to execute on the figure; the agent must self-discover the discrepancy.

### L17. Wrong-answer catalog in the design notes
Document every possible intermediate wrong answer and which reduction(s) were missed to produce it. Useful for rubric design (which intermediate values must be flagged as wrong) and verifier-fails classification.

---

## Rubric design rules

### L18. The figure IS the rubric
The single most discriminating rubric on derived-figure tasks: "Agent reports the correct figure as approximately $X" with the wrong intermediate values explicitly listed (`not $A`, `not $B`, `not $C`). Every failed run failed this rubric; agents who passed got the figure right.

**Rule:** Build the highest-discrimination rubric around the derived figure. Enumerate the intermediate wrong answers in the criterion itself.

### L19. Cascade rubrics
If the figure is wrong, cascade rubrics on email / Slack content also fail. This gives clear per-run fail counts without redundancy.

**Rule:** Content-of-deliverable rubrics that reference the correct figure will cascade-fail when the figure is wrong. This is desired — do not consider it bundling.

### L20. Channel-agnostic 1.1 rubrics
"Sends George a written message (email or DM)" avoids false negatives on equivalent communication paths. Lock in the figure, not the channel.

**Rule:** Use method-agnostic phrasing when the prompt names a goal not a channel. See L9 in Rubric_Format.md.

### L21. Negative guards
Add a rubric like "Agent does NOT post the JE itself" to catch over-action failure modes that no run hits but are latent risks.

**Rule:** One negative guard per task is a reasonable insurance policy. More than that becomes noise.

---

## DR/CR direction gotcha (verify manually before running trajectories)

### L22. DR/CR direction matters more than amount
A DR to a credit-normal liability INCREASES it. A CR to a credit-normal liability REDUCES it. A real Brookfield task had this bug — a JE was DR 101000 / CR 230000, which INCREASED the payable. All 6 agents correctly read the accounting direction and treated it as +$X instead of -$X. The "correct" answer became the wrong target.

**Rule (HARD):** Before pasting `3_UniverseDataForThisTask.json` to the platform, manually verify every injected JE's DR/CR direction. The agent gets accounting direction right — if you get it wrong, the math will be "correct" for the wrong data and the rubric will fail for the wrong reason.

---

## Calibration data

Iteration counts to reach pass@1 ≤ 40% from the Archive's two grounded tasks:
- Task01 (write-off): 3 iterations to reach 40% pass (3 reductions across 3 services + implicit prompt).
- Task02 (SALT shortfall): 4 iterations. Iter 1 (100% pass — confirm-already-done), Iter 2 (100% pass — correction email stated answer), Iter 3 (0% pass — bug + too hard), Iter 3b (0% pass with L9 authority dismissal + L10 subledger reduction).

The iteration count IS the problem these learnings exist to prevent. Use this file to skip the failed iterations.

---

## Pipeline implications

1. **HARDNESS phase reads this file first.** Every lever picked must cite a Learnings entry that justifies it works (or document a new finding if a novel lever is tried).
2. **The correct answer NEVER appears verbatim in any artifact.** Test by string-searching the prompt + per-task universe JSON for the correct figure — should return zero matches outside the GL line items the agent must aggregate.
3. **Default to 3 reductions across 3 services + L9 authority dismissal.** This is the anatomy that reliably reaches pass@1 ≤ 40%.
4. **HARDNESS density projection must hit 40+ tool calls** (see `Reference/Hardness_Playbook.md`). The 3-service / 3-reduction anatomy naturally produces 45-60.
5. **PIPELINE FINAL holistic council runs after S3** — see `Reference/Sessions/FINAL.md`. It catches answer-leakage that per-phase councils miss.
6. **After S4 verifier-fails analysis, append a new finding here** if you learn something new about how Opus 4.8 fails (or stops failing) on a lever pattern. Reference the task by `<TASK_DIR>`.

---

## Append template

```markdown
### L<n>. <One-line finding>
<2-4 sentences of empirical evidence: which task, which trajectories, what the agent did.>

**Rule:** <The design rule this implies, in one line.>

**Source:** Tasks/<TASK_DIR>/Agent_Responses/ verifier-fails analysis on <date>.
```

Number monotonically — never rewrite or delete old entries.

---

### L23. Dollar-threshold filter blindness on email surface (NEW pattern, structural stump)
Task 24 (AP triage REDO). Across 12 trajectory runs (6 in cycle 1 + 6 in cycle 2), every agent scoped the email to Daniel by an implicit ~$50K dollar threshold and dropped sub-threshold items the prompt named as needing partner sign-off. GraniteRack VEN-012-753165 ($39,090.56) and TimeLedger Nexus VEN-010-514242 ($24,475.25) both went from 1/6 failure in cycle 1 to 0/6 failure in cycle 2. The partner-sign-off requirement lived in the cross-service trail (Owen Mercer escalation email + Linear void-and-rebill issue for GraniteRack; Daniel Jones "conditioned release" email + Linear AP-escalation issue for TimeLedger), not in the invoice amount. Agents anchored on dollar magnitude and never consulted the trail.

**Rule:** When the email-write rubric requires the agent to surface sub-threshold dollar items, design the prompt and OE chain so the partner-sign-off determination comes from an authoritative trail (Linear ticket + escalation email) rather than a dollar filter. Expect 100% failure on the email surface for any sub-$50K named item unless the prompt explicitly says "dollar amount is not the filter."

**Source:** Tasks/24_6a36e84723508b4e3f391cfc/trajectory-runs/ verifier-fails analysis on 2026-06-21 (two cycles).

### L24. Prompt-side L9 yield is verb-tense sensitive
Task 24, rubric R22 (routing-fix-did-not-land). Fail rate moved from 3/6 (50%) to 2/6 (33%) after the prompt verb was softened from "was patched last sprint" to "was supposed to land last sprint" with cascading consistency updates ("whether that held" -> "whether it actually landed", "after that patch" -> "after that target"). The soft verb preserves the L9 authority-dismissal lever (agent still has to triangulate Linear ticket status past due + post-target null-approver invoices) while clearing QC Truthfulness 5 under both strict-literalist and design-intent readings. The hard verb yields ~17pp more difficulty but carries Truthfulness risk because "was patched" is a completed-action assertion the universe contradicts.

**Rule:** Default to soft verbs ("was supposed to land", "should have shipped") for prompt-side L9 authority-dismissal anchors. Reserve hard verbs ("was patched", "shipped last sprint") only when difficulty headroom is needed AND the QC reviewer is known to be permissive on persona-relayed assertions.

**Source:** Tasks/24_6a36e84723508b4e3f391cfc/trajectory-runs/ verifier-fails analysis on 2026-06-21 (cycle 1 hard verb 50% fail rate; cycle 2 soft verb 33% fail rate; same agent population, same universe).
