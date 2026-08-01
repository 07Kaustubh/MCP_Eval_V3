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

### L25. Existing-output anchor trap (NEW pattern, HIGHEST-yield novel stump on Brookfield)
Task 25 (May WIP recognition). All 6 trajectory runs found the previously posted JE je_53962aed96fe4b67 sitting in brookfield_FP-2026-05 and refused to stage the required new $147,825 entry on double-booking grounds. The existing JE was a distractor: it lacked the per-service-line schedule, the business justification tying it to Andrea Phil's stage-completion review, and routing to Daniel Jones for review. The refusal cascaded into 5 of 8 always-failing rubrics (stage JE, JE justification, Slack notes staged, vault upload linked to staged JE, email confirms staged). This is the strongest single-mechanism stump observed across V3 tasks to date — the agent's "do not double-book" instinct overrides every rubric that requires the staged write.

**Rule:** When you need a high-confidence AF stump, plant a previously posted artifact (JE / doc / message / thread) in the universe that superficially matches the requested write but lacks one or two rubric-tested fields (per-line schedule, business justification, classification, related_resource_id, routing target). Write the rubrics around the gap between the distractor and the spec'd write. Expect 100% failure on the staging rubric and 80-100% failure on every downstream rubric that depends on it.

**Source:** Tasks/25_6a366bc27d66eaedcae82ab4/trajectory-runs/ verifier-fails analysis on 2026-06-22.

### L26. Decoy parent thread (NEW pattern, reliable Slack-write stump)
Task 25 (May WIP recognition). 5 of 6 runs posted to Slack thread_ts 1780230660.000000 instead of the canonical 1780248600.000000. Both threads live in the same #monthly-close-coordination channel (C005), both touch the same incident keywords (WIP / BL-75810CD0FEE4 / exc_1ddfc978ce5a4d / partial-feed), and the wrong one is roughly 5 hours more recent. Agents that did pull the thread list still picked the more recent or more keyword-matching parent ts. Stronger than the L4 search-result-cap eviction lever predicted — the wrong thread doesn't need to be evicted, it just needs to look more plausible.

**Rule:** For any Slack-write rubric anchored to a specific thread_ts, plant a decoy parent in the same channel on an overlapping topic with a more-recent timestamp. The canonical thread must be named only in the OE (or in a less-recent Slack search result). Expect 80%+ failure on the thread_ts check.

**Source:** Tasks/25_6a366bc27d66eaedcae82ab4/trajectory-runs/ verifier-fails analysis on 2026-06-22.

### L27. Soft-instruction over-compliance (NEW pattern)
Task 25 (May WIP recognition). All 6 runs skipped the blackline_update_exception write on exc_1ddfc978ce5a4d entirely, reading Hannah Grant's "leave the underlying exception trail referenced as-is for now" as a blanket no-op on the exception record. The correct scoped read was "do not resolve the exception, but record the accept-timing disposition while keeping state as investigating." No agent reached the scoped read. Cascaded into two AF rubrics (exception update + exception update refs Hannah/BD3).

**Rule:** When the prompt requires the agent to take a scoped write under a soft authority instruction ("leave X as-is", "do not touch Y", "park Z"), make the scope explicit ("update X with the disposition but do not resolve it") OR add a second authority sentence that endorses the scoped write. Otherwise expect 0/6 on the write rubric.

**Source:** Tasks/25_6a366bc27d66eaedcae82ab4/trajectory-runs/ verifier-fails analysis on 2026-06-22.

### L28. Tool-variant trap (NEW pattern, reliable Records Vault stump)
Task 25 (May WIP recognition). All 6 runs chose records_vault_add_document_version on the existing doc_42c851aed8fb40ab over records_vault_upload_document for a fresh memo. The "similar doc already exists" signal triggered the version-bump path 100% of the time even though the OE expected a fresh upload tied to a new related_resource_id (the staged JE).

**Rule:** For Records Vault rubrics that require a fresh upload, plant a similar restricted doc in the vault with overlapping title scope and require classification + retention + related_resource_id on the new upload to differ from the existing one. The agent will default to version-bump and miss the related_resource_id requirement, which is the rubric-tested field.

**Source:** Tasks/25_6a366bc27d66eaedcae82ab4/trajectory-runs/ verifier-fails analysis on 2026-06-22.

### L29. Escape-valve prompt clauses neutralize L2 structured-DB skip
Task 25 (May WIP recognition). The Hardness_Plan predicted [HIGH] that agents would skip ogl_subledger_feed_runs and never surface the partial-feed contradiction. All 6 runs queried the feed run, found run_e33ed2561f2c46 (success / 2083 / 0 rejected), and surfaced the contradiction in their final response (R11 6/6 pass; R17 in S4 matrix). The reason: the prompt's escape-valve sentence "If anything in what you pull together changes the read on this before I take it to Daniel, say so plainly. I would rather hear it from you before the package moves than from Andrea after." directly invites the agent to look for and surface contradictions. The lever still fired on the SECONDARY structured-DB surface (blackline_review_notes — Edith Banda's open note) but only 1/6.

**Rule:** If your hardness anatomy depends on L2 structured-DB skip on a load-bearing surface, do NOT include an escape-valve clause in the prompt that invites contradiction-surfacing. The escape-valve is useful for Truthfulness 5 and for keeping the persona's voice realistic, but it neutralizes L2 on the surface it points at. Reserve escape-valves for tasks where L2 fires on a different (truly obscure) surface than the load-bearing one.

**Source:** Tasks/25_6a366bc27d66eaedcae82ab4/trajectory-runs/ verifier-fails analysis on 2026-06-22.

### L30. REVIEW REBUILD triage from rubric-binding cascade (NEW pattern)
Task 26 (April close controls review REDO). Raw 6-trajectory metrics looked clean: avg tool calls 59.3, pass@1 0/6, both inside the difficulty and density windows. But the 0/6 was entirely driven by two rubrics checking for a clean-branch note "to Andrea" when the prompt explicitly named Peter Sanchez as the addressee. Rebinding those two rubrics to Peter raises projected effective pass@1 to ~3/6 (50%), above the 40% ceiling. Combined with two more rubrics naming the wrong persona (Daniel vs Matthew Li), 6 of 8 titles starting with "If" instead of "The Agent" (platform-linter block), and zero coverage of the prompt's five closing deliverables (timeline, ranking, evidence, classification, clean-branch memo), the deliverable set was past patchable.

**Rule:** Apparent 0/6 difficulty is suspect when one or more rubrics name a person the prompt does not. Before greenlighting a low-pass-rate task, sanity-check every rubric's named recipients against the prompt's explicit recipients. If the named-recipient mismatch is in the load-bearing write-action rubric, the 0/6 is artefactual and the task must be triaged REBUILD rather than approved on raw pass@1. Also extend the check to persona names (rubric "Daniel" vs prompt persona "Matthew Li") and to title format (titles starting with "If" rather than "The Agent" block the platform linter).

**Source:** Tasks/26_6a390b7b8e3ad2bcdcfa90b3/_aux/Candidate_Originals/changes.md (row 18) + Tasks/26_6a390b7b8e3ad2bcdcfa90b3/_aux/REDO_reason.md on 2026-06-22.


### L31. Gemini omits explicit NEGATIVE directives (dual-model V4 differentiator)
Task 39 (StarPM V4, Las Palmas 8D make-ready). A rubric requiring the agent to state the unit is "not ready and should not be marketed or shown" failed ALL 6 Gemini runs and passed ALL 6 Opus runs. Every Gemini channel post named the open blocker but framed the unit positively ("will be 100% rent-ready once approved") and never issued the prohibition (stop showing / do not market). Opus issued the walk-back in every run ("please don't treat as fully ready yet"). Verified: full C004 bodies scanned, zero "not ready / don't show / don't market" hits across all 6 Gemini runs.

**Rule:** In dual-model (V4) tasks, a rubric that demands an explicit negative directive — walk back a prior go-ahead, "do not", "not yet", "stop" — is a cheap, near-100% Gemini stump and trivial for Opus. Plant a "must explicitly retract a prior it-is-ready signal" beat when you need a reliable per-model difficulty differentiator; do not rely on it to stump Opus. When such a rubric fails every run of ONE model but passes the other, it is a legitimate model gap (Bucket 3), not an invalid all-fail — the cross-model asymmetry is the proof of achievability.

**Source:** Tasks/39_6a602c8886ebb06f12354d77/8b_Verifier_Fails_Gemini.txt (R6 6/6 fail) + _aux/S4_bucket3.md, 2026-07-23.
## 2026-07-23 - S4 on Task 40 (StarPM V4 dual-model): tooling + verification gotchas
1. parse_trajectories.py could not read Gemini's flat trajectory format. Gemini exports tool calls as TOP-LEVEL events (`{"type":"tool_use","tool_name":...}`), not nested in `message.content[]` like Claude-Code/Opus. count_tool_calls only handled the nested shape, so it scored EVERY Gemini run as 0 tool calls -> false REBUILD_CANDIDATE_DENSITY on what is actually a 40.0-avg run set. This affected ALL StarPM/V4 dual-model tasks silently. Fix is additive (also count top-level type==tool_use, mcp_ prefix), mutually exclusive with the nested branch, regression-clean (anchors 62/62, reports 21/21, verdicts 7/7). Always sanity-check a "0 tool calls" model against the raw file before trusting a density REDO.
2. check_verification.py section regexes match header TOKENS anywhere in the file, not just line-start. Writing a literal "## Verdict" (or any "## Section") inside verification PROSE creates a second match and the Verdict/section capture breaks (captured PASS-less text). Never embed "## <Header>" literals in verification-doc prose; refer to them without the "##".
3. StarPM stores tenant rent arrears as a QuickBooks AP BILL (QR-2026-0441), not an AR invoice. Agents that only search invoices/payments find the zero-balance decoy 7214 and miss the real figure. This is the single most robust stump on the task (0/12 both models). Worth reusing: place the authoritative number in the object type the agent is least likely to query.

## 2026-07-23 - S4 Task 40 correction pass (skeptical re-verification found 3 real defects)
A second pass (full read of 8a/8b + per-rubric tool_use/tool_result walk) overturned three first-pass calls. Lessons:
4. AF justifications MUST be grounded in the tool WALK, not inferred from the verifier text. First pass wrote "agent never opened the bill" (R10 Opus) and "did not query the accommodation record" (R13 Gemini). The walk proved BOTH agents reached the source: Opus surfaced QR-2026-0441 in an invoice result (never called the bills tool, still had the value in runs 1,3); Gemini retrieved the approved ESA in CRM/thread results in all 6 runs. The real stump is CARRY-THROUGH (fact in context, omitted from the email), a stronger and more accurate failure story than "never found it". Never write an AF justification from the judge's text alone.
5. Non-atomic rubrics hide until the trajectories split them. R12 ("owner-approved (EVF-2026-014) but still in JP coordination") passed S3 + AUDIT + FINAL, but across runs the two halves failed independently (EVF-id vs JP-status) AND the judge graded the same EVF-id-absent state as pass (Gemini 4,5) and fail (Gemini 1,2,6). A parenthetical id that looks like grounding but gets graded as a token is the tell. S3 atomicity decomposition should split any email-content rubric whose two facts come from different records (EVF from the maintenance ticket, JP from the make-ready note/Slack) - "same email" is NOT sufficient for atomicity when the facts are independently verifiable and sourced differently.
6. Verify tool REACHABILITY before ruling an always-failing rubric legit: a 0/12 arrears rubric is only Bucket 3 because search_bills/get-bill exist in the catalog and OE 9 uses them. If the bill had been unreachable it would have been an impossible-derivation (Bucket 1). Always check the tool catalog for the OE's canonical path.


## 2026-07-23 - S4 Task 40 post-split re-verify (the R12 split fix, empirically validated)
7. The remedy in item 5 was re-run on the platform (Opus only) and it WORKS - documenting the closed loop. After splitting R12 into R12a (owner-approved) + R12b (JP-coordination/not-closed) and demoting the "(EVF-2026-014)" parenthetical to optional grounding, the fresh Opus 8a (17 criteria) graded both halves consistently: R12a 6/6 pass, R12b fails only run 1 (a genuine JP-coordination omission). The proof the id-token was the defect, not real difficulty: under the OLD combined rubric Opus failed runs 1 AND 5; under the split, run 5 passes both halves because the EVF-id it had omitted is no longer graded. Splitting a bundled Outcome rubric and demoting an id-that-looks-like-grounding raises measured grading accuracy WITHOUT changing task difficulty (pass@1 stayed 0%). Operational gotcha for S4 re-runs: when the platform re-verifies after a rubric fix, the new verifier file can carry a DIFFERENT criterion count than the pre-fix file for the other model (here 8a=17 post-split, 8b=16 pre-split) - always reconcile criteria-per-run before trusting a prior matrix, and flag the un-re-run model (Gemini) as a pending platform re-verify rather than assuming symmetry.

## 2026-07-23 - S4 Task 40 Gemini re-verify (dual-model closed loop)
8. The v3 pending action (Gemini platform re-verify on the 17-rubric split) arrived and closes the loop symmetrically. The Gemini 8b was re-graded on the same six trajectories (tool-call counts 47/45/37/38/33/40 unchanged) against the split rubrics: R12a 6/6 pass, R12b 6/6 pass - exactly the Opus result. This confirms the "(EVF-2026-014)" parenthetical, not task difficulty, drove the pre-split flip-flop (Gemini combined runs 4,5 pass vs 1,2,6 fail in the same id-absent state); the atomic split eliminates it on BOTH models with pass@1 unchanged at 0%. Two operational notes: (a) a rubric-fix re-verify is a re-GRADE of the existing trajectories, not a fresh agent run - confirm the tool-call counts are unchanged before trusting it as a like-for-like validation; (b) reconciling the new file against the prior matrix caught a transcription error in the v3 verdict (Opus runs 5,6 were 12/17 each, not the recorded 10/11) - recompute pass/run from the fail lines rather than trusting a hand-carried matrix.
## 2026-07-24 - S4 Task 41 (StarPM V4 dual-model): a displaced lever + the clean dual-model 0/6 recipe
9. **A downstream lever can be "displaced" (never observed) because an upstream lever fires first.** Task 41 selected L2 (arrears hidden in a vendor-linked AP bill) AND L11 (the $150 credit stored as a positive → $2,132 vs $1,832 net) as independent levers. In practice L11 was NEVER observable: no run across 12 opened the bill at all, so the credit-disposition step never ran — every run reported $2,287.50 from the paid customer invoice 7214 and stopped. L11 is a real lever but it lives one hop PAST L2's discovery gate. Design rule: if you want a net-vs-gross/sign lever to produce its own observable fail, do not stack it behind a discovery lever that already sweeps 0/12 — pair it with an EASY path to the figure so agents reach the disposition step. Otherwise the two levers collapse into one measured stump and you cannot tell them apart at S4.
10. **Verify "reached the source" by the tool WALK, not a string grep (reinforces item 4).** grep showed "QR-2026-0441" in all 6 Opus trajectories, which naively reads as "Opus found the bill". The walk showed every hit was the PDF filename `QR-2026-0441.pdf` in a `workspace/company_files/invoices` directory LISTING — the bill entity was never opened. Both models effectively skipped it. A filename in a dir listing is a breadcrumb the agent didn't pull, not evidence of retrieval. Always characterize AF failures from what the agent OPENED/USED, not what appeared in its context.
11. **The clean dual-model 0/6 recipe: one symmetric stump + two complementary asymmetric stumps.** Task 41 landed 0/6 on BOTH models via (a) L2 vendor-linked-bill arrears = symmetric (0/12), (b) L1 owner-latching + L10 reversal-record-pick = Opus-selective, (c) L31 negative-directive omission = Gemini-selective. The symmetric stump guarantees neither model sweeps; the two asymmetric stumps deepen the margin on whichever model would otherwise be strong. This is the second StarPM task to confirm structured-store-skip = symmetric, near-miss/reversal-record = Opus-selective, negative-directive = Gemini-selective. Bank this triad as the default StarPM dual-model difficulty mix.

## 2026-07-24 - S4 Task 41 post-fix re-grade (correcting item 11's L10 claim)
12. **A rubric fix that removes a false-fail is not a lever lost — re-run and confirm pass@1 before crediting removed fails as difficulty.** Task 41's prior S4 logged an "L10 reversal/supersession make-ready-record pick" as an Opus 3/6 stump. It was not: R6 whitelisted an exact-ID accept-set that contradicted OE 14 ("grade on tenant + property, not the exact record id") and false-failed correct writes (right tenant, right Unit 14, right hold content). After R6 was reconciled to grade on content, the post-fix re-grade shows R6 passing 6/6 Opus and pass@1 UNCHANGED at 0/6 both models. Correction to item 11: the dual-model 0/6 recipe rests on L2 (symmetric arrears) + L1 owner-latching (Opus-selective) + L31 negative-directive (Gemini-selective); L10's genuine role is the eviction-state supersession READ (handled correctly, rubrics 3/10/17 passed 12/12), not a make-ready-record write stump. Operator rule: after an S4 rubric fix, re-classify the re-graded run from scratch and confirm the difficulty verdict independently; a removed false-fail must be struck from the lever ledger, not counted as a weakened lever.

## 2026-07-25 - Task 39 (StarPM V4, Las Palmas 8D) shipped a QC-fail-capable fault: the gates ran and mis-scored
13. **Five green human-judgment gates can still ship a QC fail when they reason backward from the answer.** Task 39 got a platform Poor 2/5 "full redo". S0/HARDNESS/S1/S2/S3/S4/4xAUDIT/FINAL all ran and returned GO. The faults were not missed by omission - they were SEEN and mis-scored: FINAL LENS 6 called R6/R11/R15 "MINOR / ship-as-is / acceptable as-is"; FINAL Red-Team #3 "confirmed" the target record unambiguous because it was "the only selReady row" (the prompt said square up what is LOGGED, not "find the ready row"); Red-Team #4 "confirmed" the disposal was the sole blocker without ever sweeping Calendar; AUDIT scored Atomicity 5/5 with a definition that only caught cross-action bundling; S4 scored Bucket-1 = 0/11 while the 12 trajectories showed the false-fails. Root cause: answer-anchored review with no deterministic backstop.
14. **Three fault classes are now deterministic V4 submission-gate defects (F7/F8/F9), because judgment alone let them ship.** F7 AMBIGUOUS_TARGET: a rubric pins one record id while >=2 universe rows share its entity and the prompt names none (Task 39 R2/R3/R4 on three "Las Palmas 8D" rows; also caught Task 40 on five "Unit 14" rows). F8 NON_ATOMIC_ENUM: one criterion enumerates >=3 conjunctive items under a completeness/step predicate (R11 3 items, R15 5). F9 UNRECONCILED_FUTURE_EVT: a confirmed calendar event dated >= universe today references the task entity, its date is uncited in the OEs, and the deliverables assert completeness (the 2026-07-07 "A Plus Carpet" walk that broke "disposal is the only open item"). RED->GREEN: Task 39 flips PASS->FAIL (6 defects); 41/43 stay PASS; regression 62/62 + 21/21 + 7/7 unchanged.
15. **A future confirmed calendar event on the task entity is open work - Calendar was the one service no lens swept.** When a task's thesis is "the unit is done except for X", grep every service for the entity, Calendar included, before writing the "only X open" rubric. The contradiction that sank Task 39 sat in the single service the whole council skipped.
16. **When 0/12 runs pass a rubric, treat it as a rubric-validity question first, not a difficulty win.** R6 required "should not be marketed or shown" - a phrase the prompt never asks for - so it failed 6/6 and got justified as a model failure. pass@1 = 0.0 with a specific rubric all-failing is the exact signature of an ungrounded/false-fail rubric; run the naive-agent + prompt-grounding check before crediting it as hardness.

## 2026-07-25 - S4 Task 43 (StarPM V4 dual-model): the base64 body trap, and a 0/12 rubric that survived the validity check
17. **On StarPM, a Gmail message body is base64 and agents do not decode it. Never let a rubric's only corroborating evidence live in one.** OE 7 prescribed `search_threads` then `get_thread(threadId: "66132537181ecbe1")` to reach the owner summary whose body settles the task's central classification ("Pete Donovan finished the interior repaint (including a touch-up on the bedroom closet trim...), and Tony's team handled all internal repairs in-house"). **9 of 12 runs made exactly that call and 0 of 12 decoded the payload**, which `get_thread` returns as base64 in `payload.body.data`. The StarPM gmail surface has no `get_message`/`read_message` that returns plaintext, so `get_thread` is the only path and it always returns encoded. One run (Gemini 2) had already used base64 decoding on other content earlier in the same run and still left this payload encoded. Design rule: treat an email body as **flavour, never as the load-bearing discriminator**. Put the resolving fact in a structured field (`VendorRef`, an account ref, a status enum) and let the email corroborate. Verification rule: when an OE cites an email body, walk a trajectory and confirm the body was actually decoded before crediting it as reachable evidence.
18. **Item 16's rule (0/12 = suspect the rubric first) applied and CLEARED a rubric for the first time. Record what "clears" looks like.** The closet-trim rubric failed 12/12 across two model families, with both families converging on the *same* wrong answer ($1,727) rather than scattering - the exact signature item 16 says to distrust. It survived because three independent discriminators are reachable and one is structured: `VendorRef.name` = the outside vendor on the same record, an operative "Pass-through to owner" clause two sentences later in the same note, and the prompt's exclusion narrowed to "an internal walk or a condition check" (a repaint touch-up is neither). Contrast with Task 39 R6, which failed 6/6 on a phrase the prompt never asked for. **The test that separates them: can you name a reachable, non-prose source that resolves the question, and does the prompt's own language pick that side?** If yes it is a lever; if no it is a false-fail. Unanimous convergence on one wrong answer is evidence of a well-built trap OR a broken rubric - the discriminator is reachability, not the fail count.
19. **Check judge consistency ACROSS runs of the same rubric, not just judge correctness within a run - and check the passes, not only the fails.** Two distinct judge errors surfaced only by cross-run comparison. (a) On the closet-trim-amount rubric the judge enforced an evidence-field vendor attribution on Opus runs 2 and 3 and waived it on runs 1, 4 and 6 for materially identical text. (b) More importantly, **two runs were passed on the Airtable rubrics for doing exactly what a third run was failed for**: Opus 2 and Opus 4 wrote only to the stale In Progress row (which the evidence field explicitly says does not satisfy), while Gemini 3 did the same and was failed. Opus 2's own response says it treated the live Ready row as "a stray duplicate". Wrong-PASS cells are not appealable and are easy to skip, but they corrupt the lever ledger: the dual-row lever really fired 3/12, not the 1/12 the raw matrix shows. **Always reconstruct write targets from the trajectory for every run of a record-pick rubric, including the runs that passed.**
20. **A lever that is "masked" in one task can be the engine in the next, and the escape-valve sentence is what unmasks it.** Task 41 item 9 concluded L11 net-vs-gross was unobservable because it sat one hop past L2's discovery gate. Task 43 carried an L29 escape-valve sentence in the prompt ("go back to what each vendor charged us and set it against the line items I sent her") that the FINAL council flagged as blunting L2. It did exactly that - and by opening the discovery gate it let L11 become the sole engine, 12/12 symmetric, 9 of 15 failing rubrics. **The pairing rule is confirmed from both directions: stack net-vs-gross behind a discovery gate and you measure one stump; open the gate and you measure two.** Also worth banking: the FINAL council's pre-registered re-attribution ("if runs reach the AP bills but land on $1,897 or $1,727, score that as L6/L11 firing, not L2 failing") was correct to the dollar. A pre-registered prediction of *which* lever will fire is cheap to write at FINAL and makes the S4 calibration honest instead of retrofitted.
21. **When a criterion is replaced or restored mid-iteration, re-derive every accommodation clause attached to it AND its siblings - and re-read the prior round's rationale before signing off.** Task 44's S3 AUDIT found two Moderates that both per-phase councils missed, and both were the *same* defect: an accommodation added in round N survived a round-N+1 criterion swap without being re-derived. (a) Council A asked for a one-directional `FAIL only if ...` guard on a condensate-drain criterion so a correct agent would not be penalised for the defensible reading. That criterion was later deleted outright and replaced with a different positive-completion criterion - and the `FAIL only if` clause was carried across verbatim. On the replacement it inverted the meaning: silence became a PASS, nullifying the exact criterion added to close a completeness Major. It was the only exclusive-fail clause in a 64-rubric set. (b) An East-owner criterion's accept-set was widened to include the supervisor draft in round 2 *because* the draft-specific criterion had just been deleted; round 3 restored the draft criterion without re-narrowing the first, leaving `pass(B) => pass(A)` so one omission failed two criteria. **The councils could not catch either, because each re-reviewed the current text against the spec and neither re-read why the clause was written.** The cheap fix that would have caught both: when you delete or replace a criterion, grep the set for every clause that was introduced to accommodate it. AUDIT found (b) by reading `_aux/Todos_s3.md`'s own iteration log - which is an argument for keeping that log narrative, not just a checkbox list.
22. **A grounding council that sweeps for falsifiers beats one that only sweeps for sources - and the falsifier is often a message no Oracle Event mentions.** Twice on Task 44 the load-bearing defect was not an ungrounded value but a *grounded* value contradicted by a record nobody had looked at. Three rubrics asserted a second round of tenant access notices was "never confirmed"; a top-level Slack post six days after the ask (Carlos Mendez, "48-hour notice letters are out to all affected tenants") falsifies it, appears in zero OEs and zero prior council reports, and sits in a channel the OEs *require* the agent to page in full - so a compliant agent finds it and correctly refuses to write the claim. Separately, a positive-completion criterion built on an issue comment ("all good now") was falsified by the same author's portfolio wrap six days later flagging that item for recurring follow-up. **Both are the absence-shaped-claim trap wearing a positive disguise: "X is still pending" and "X requires no further work" are both universally-quantified over time, so both are refuted by a single later record.** Give the grounding council an explicit falsifier mandate: for every time-quantified claim, sweep the full channel history and the full comment corpus *after* the cited source date, not just for the source itself.

### L32. 60 is the hard rubric-count ceiling, and nothing in the pipeline enforces it

**Evidence:** Task 44 shipped a 64-criterion `7_Rubrics.json` through S3 (Council A + Council B + AUDIT `PASS (STRICT)`) and the full FINAL cross-artifact council without a single gate objecting. The cap appears in no spec doc, no eval, no Reference card and no validator — `validate.py --phase rubrics` and `v4_gates.py` both count criteria and report the census (`64 outcome / 0 process`) without bounding it. It surfaced only because the operator stated it after FINAL had already returned PASS.

**Rule:** Budget against 60 at S3, before decomposition. The OE-side `S3 must decompose this into one criterion per content element` directives are what drive the count up — when the OE list of content elements across all write actions exceeds the budget, the decision to drop an element belongs at S2/S3 where it can be reasoned about, not at FINAL as a trim.

**When a set does run over, cut to retire risk, not to trim coverage.** Task 44's four cuts were all things the FINAL council had already flagged: two Lens 6 Bucket-1 risks (a location-pinned duplicate of a claim graded elsewhere at wider scope; a beyond-prompt assignee audit), the weakest owner accept-set (which was also the subject of a fragile nesting adjudication that had consumed a whole AUDIT round), and a criterion grading a meta-statement about the agent's own writes rather than a finding. Bucket_1_Risk went **6.3% -> 0%** and the soft NOT_ATOMIC warn count **3 -> 2** while every lever carrier and every prompt ask survived. A count cap is an opportunity to delete the criteria you were already uneasy about.

**Three hard constraints on any count-driven cut:**
1. **Never merge two criteria to save a slot.** Merging is how you manufacture the F8 NON_ATOMIC_ENUM defect. Only whole-criterion removal.
2. **Never cut a lever carrier.** Check the AUDIT report's lever-trace table first; string-match each carrier in the reduced set afterward.
3. **Mirror the cut into the OE.** Every dropped element that an OE named in an `S3 must decompose…` directive leaves a stale instruction pointing at a criterion that no longer exists. Narrow the directive to the surviving elements and re-state the dropped one as description content that carries no criterion, with the reason. Leave the agent-facing expected-discovery prose alone so the oracle path is unchanged.

**Density is unaffected by a well-chosen cut** — verify this rather than assume it. None of Task 44's four forced a unique tool call: the underlying records were still forced by the surviving criteria in the same group.

### L33. Platform grading is non-deterministic at ~8.5% of cells; design difficulty for margin, not for a number

**Evidence:** Task 44 was graded three times. The third and second gradings ran against **byte-identical trajectories** (`Agent_Responses/` unchanged; `parse_trajectories.py` reproduces every per-run tool-call count to the unit) and differed on **67 of 720 decision cells (9.3%)**. Only 6 of those 67 fall on the six criteria whose evidence text was edited between the exports. **61 cells (8.5% of all cells) are decision changes on criterion text that did not move by a character.** The drift is model-asymmetric: Gemini gained 20 criteria-passed across its six runs, Opus lost 3, with a single-run swing as large as 9 points. Three cells in the newest export carry judge justifications that the write payload refutes verbatim, and all three had passed under the previous export.

**Rule 1 — design for margin.** Every hard gate held under all three gradings because the margins were wide: pass@1 0/6 against a 40% ceiling, density 62.5 and 79.8 against a 40 floor, 0 error runs against a ceiling of 2. A task whose projected difficulty lands *just* inside a threshold is not actually inside it, because the grader can move ~8.5% of cells on a re-run. This is a second, independent argument for the 50+ density design target and it applies to difficulty the same way.

**Rule 2 — do not rebuild an S4 analysis on a per-cell delta.** When a regrade arrives, re-derive the matrix from the export in hand rather than patching the previous one. Task 44's South-electrical criterion had its per-cell count restated three times across three exports, and each restatement of a stale number cost a review round.

**Rule 3 — the trajectory walk is load-bearing, not confirmatory.** Classifying from verifier text alone would have produced AF justifications blaming the model for three failures whose artifacts contain the exact text the judge said was missing. The walk is the only thing separating a false fail from a justification that ships.

**Rule 4 — criterion shape predicts stability, so choose the shape.** Criteria grading **a created artifact and its contents** moved 0 of 96 cells across two gradings. Criteria grading **the agent's characterisation of a pre-existing record's claim** ("X is recorded as finished", "the latest dated status says Y") absorbed most of the movement and produced 6 of 10 contested cells. When a lever can be carried either way, carry it on the artifact.

**Rule 5 — filed appeals should clear a verbatim-decisive bar.** Pass 2 filed 22 contested cells against one export; the next regrade vacated 11 of them with no rubric change at all. Filing only the cells whose artifact text is word-for-word decisive costs nothing and keeps the appeal credible.

**Corollary for evidence fields:** the three amendments applied between exports (identifier-form latitude, paraphrase latitude, first-person self-reference) each flipped the specific cell they targeted, so evidence-field clarification does work as intended. It just does not account for most of the movement, and it should not be credited with movement it did not cause.

### L34

**Widening a criterion's accept-set recovers real agent work, and the gain is measurable within one regrade.** Task 44, three gradings of twelve byte-identical trajectories. Thirteen criteria were widened between the second and third grading, every edit adding an acceptable location or reason rather than relaxing the substance. Two moved decisively in the agent's favour: the note-on-a-QC-record criterion went from 0 of 6 to 4 of 6 on Opus once any correct reason was accepted instead of one named reason, and three filter-run criteria each gained their first Opus pass once a comment on an existing open record was accepted alongside a new tracking item. No lever was weakened and no gate moved.

**Why this matters at S3 rather than S4.** In every one of those cases the agent had done the work and put it somewhere the criterion did not list. The criterion was measuring destination compliance, not the reasoning the lever was built to test. The cheap discipline is to ask, for every write criterion at authoring time, "what are all the places a competent agent could reasonably put this?" and enumerate them in the evidence field then. Discovering it at S4 costs a full reclassification pass and leaves a grading of record that understates the model.

**The limit of the technique.** Widening cannot help a criterion whose content was never produced anywhere. The two East duplicate-record criteria were widened to accept any deliverable as the location and stayed at 0 of 12, because no run in either model ever stated the finding. Widening fixes destination mismatches; it does nothing for genuine misses, and that is exactly the separation you want.

### L35

**Grader non-determinism is symmetric in magnitude and unstable in direction.** Task 44 now has three independent gradings of the same twelve trajectories. Second to third: 9.3% of cells moved, net 42 Fail-to-Pass against 25 Pass-to-Fail. Third to fourth: 10.3% moved, net 46 Pass-to-Fail against 28 Fail-to-Pass. Restricting to criteria whose text did not change between exports, the rates are 8.5% and 8.6%, which is a stable noise floor of roughly one cell in twelve. The direction, however, reversed completely.

**Consequences.** Per-run scores are not a stable quantity on this task family: the best Opus run reported 47, then 46, then 43 across three exports of the same trajectory. Never restate a per-cell or per-run count without re-deriving it from the export in hand. Gate margins, by contrast, are safe: pass@1 was 0 of 6 on both models under all three gradings, error runs 0 of 6 under all three, and density is a trajectory property grading cannot touch. Design for margin, not for a number.

**Confirmation of the criterion-shape rule (L33 Rule 4), now across three gradings.** Criteria that grade a created artifact and its contents moved **0 of 120 cells** from the third grading to the fourth, having moved 0 of 96 from the second to the third. The four criteria carrying the persona's own undispositioned field note are **6 of 6 pass on Opus and 6 of 6 fail on Gemini under all three gradings, with 0 of 48 cells moved in the latest pair**. The rule is no longer a single-pass observation. When a lever can be carried on a created artifact or on the agent's characterisation of a pre-existing record's claim, carry it on the artifact.


### L36. A well-trapped universe contributes zero difficulty if the prompt names the traps; difficulty is withheld inference, not universe trap density

**Evidence:** Task 45 (StarPM V4, Mesa Vista 4C QC hold) shipped a genuinely strong universe — the live selProg turn `recbd087a4abd605b` vs a decoy selReady row `recc8534` created LATER (5/29 vs 5/22), two "done"-flavored maintenance tickets, unpaid QuickBooks bills ($387 + $1,340), a past-due 6/30 target, and a real future 2026-07-15 QC re-inspection. The Hardness_Plan selected the banked StarPM dual-model triad (L2 symmetric structured-DB skip + L1/L10 Opus-selective supersession + L31 Gemini-selective negative directive). It came back **Opus pass@1 = 100% (6/6 all 20 rubrics), Gemini 50%, overall 75%** — a T2 difficulty FAIL on both models, routed to REDO. Zero all-failing rubrics; the only fails were Gemini occasionally skipping the Airtable write or a dollar figure, at 1-2 of 6.

**Mechanism — the prompt spent every trap by naming it.** Each engineered lever maps to a prompt sentence that pre-solves it: L2 ("finished with the bill still sitting unpaid, does not count as closed to me" hands over the exact billed-but-unpaid trap), L10 ("moved out in the middle of June with a target-ready date at the end of the month" IS recbd087's distinguishing content, so no row disambiguation remains), L31 ("if it is not, say so plainly and hold it" pre-scaffolds the negative), L9 ("a re-inspection on the calendar for the middle of this month ... factors into whether I can call this one done" names the gating event). Every rubric discriminator traces to an explicit prompt clause, so inference load is near zero and a capable agent cannot fail.

**Rule — audit the prompt against the rubric discriminators before shipping, not after.** For each rubric criterion, find the sentence in the prompt that would let an agent satisfy it WITHOUT discovering anything. If every criterion has one, the task is too easy regardless of how hard the universe is. This is the "escape-valve clause neutralizes the lever" pattern (Stump_Hypotheses Task 25) at its maximum — the whole prompt was one escape valve. A stump lever only fires on the delta between what the agent must conclude and what the prompt already told it.

**Corollary for StarPM QC-hold scenarios specifically:** the prompt must ask for the QC determination WITHOUT defining billed-but-unpaid, WITHOUT enumerating the scopes, WITHOUT pinning the turn by its move-out/target dates, and WITHOUT naming the re-inspection as a gate. Force the agent to discover which make-ready row is live, to reconcile QuickBooks itself, and to surface the future event on its own. The universe atoms are all reusable for the rebuild; only the prompt's information content must change.

**Density corroborated the call:** Opus averaged 37.0 tool calls (below the 40 design target, above the 15 floor) — the THIN_DENSITY the S1 AUDIT had already accepted with a mandatory sub-40 REDO gate. Difficulty was the decisive trigger; sub-40 Opus density was an independent second reason to rebuild.