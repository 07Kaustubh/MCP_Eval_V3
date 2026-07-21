# Stump_Hypotheses

Append-only. Per-task record of HARDNESS predictions vs S4 actuals. Drives lever-catalog calibration over time.

## Schema

```
## Entry — Tasks/<TASK_DIR> — YYYY-MM-DD

**Predictions (from Hardness_Plan.md):**
1. [HIGH | MED | LOW] <prediction> — Mechanism: <lever>
2. ...

**Actuals (from S4_verdict.md):**
- AF rubrics: <count>
- Per AF rubric: <id> — <one-line description of what the agent missed>

**Hit rate:** <hits>/<total predictions>

**Misses (predicted, did not fail):** <list>

**Surprises (failed, did not predict):** <list with mechanism guess>

**Lesson for the lever catalog:** <one line>
```

## Entries

## Entry — Tasks/24_6a36e84723508b4e3f391cfc — 2026-06-21

**Predictions (from Hardness_Plan.md):**
1. [HIGH] Root-cause miscategorization on 2 of 3 top vendors (GraniteRack VEN-012-753165, TimeLedger VEN-010-514242, BeaconPay VEN-033) — Mechanism: L8 three-link chain (SAP -> Linear -> email) + L11 structured-source skip + L14 correct observation / wrong conclusion
2. [HIGH] Acme Cloud scope reported as "not found" instead of "addendum + change order" (doc_eb7cb30c59bd4f03 + doc_2d85ac5a698745c5) — Mechanism: L2 structured-DB skip + L9 universe-grounded gotcha
3. [MED-HIGH] Authority-figure dismissal: agent defers to Daniel-Jones "routing-fixed" Slack thread reply and de-escalates — Mechanism: L1 latching + Learnings-L9 authority dismissal + L12 thread-reply blindness
4. [MED] Misses at least one age-vs-dollars trade-off vendor (BeaconPay) — Mechanism: L1 latching + L13 first-framing trap

**Actuals (from S4_verdict.md):**
- AF rubrics: 8 legitimate (6 systematic at 5/6 fail + R17 at 4/6 + R22 at 3/6); 1 borderline judge variance (R6 at 4/6)
- R2 — Slack omits GraniteRack stale SOW (procurement)
- R3 — Slack omits TimeLedger missing credit memo (AP)
- R9 — Email omits GraniteRack void-and-rebill partner sign-off
- R10 — Email omits TimeLedger partner sign-off
- R15 — Analytical miss on GraniteRack SOW-2024-GR-rev3 vs SOW-2025-GR-rev1 supersession
- R16 — Analytical miss on TimeLedger $24,475.25 missing credit memo
- R17 — Pinecrest VEN-006-193120 small-dollar / high-age active dispute missed
- R22 — Routing-fix-did-not-hold conclusion hedged in face of Daniel-Jones dismissal
- R6 — Linear comment narrowed to filtered subset (215 or 214 invoices) instead of full 320/320 systemic null-approver claim

**Hit rate:** 2/3 testable (Pred 1 CONFIRMED, Pred 3 CONFIRMED, Pred 2 OVER-PREDICTED, Pred 4 NOT TESTABLE — BeaconPay anchor removed in FINAL phase).

**Misses (predicted, did not fail):**
- Pred 2 Acme scope = "not found" trap: failed only 1/6 runs (Run 2). The explicit "addendum and at least one change order, so we have multiple documents to check, not a single letter" prompt language and Northstar-vs-Acme contrast made the trap visible. Worth keeping the lever but expect HIGH-confidence Pred-2-shaped predictions to land at MED in practice when the prompt names the doc-kind variants.

**Atom-validation correction (Phase 3 cross-check, 2026-06-21):**
- The Hardness_Plan claimed the Daniel Jones "routing patched last sprint" dismissal lived as a Slack thread reply in C010. Phase 3 universe verification found this is NOT in the Slack record — Daniel's actual C010 reply attributes routing fix ownership to Mateo (npc_024) as in-progress, not as completed. The "patched last sprint" framing lives in the PROMPT itself (`5_Prompt.txt`), not in Slack. The L1 + Learnings-L9 authority-dismissal lever still fires (R22 failed 3/6 runs as predicted at MED-HIGH) but the operative mechanism is "prompt-planted hearsay vs universe-disproving evidence", not "thread-reply dismissal". For the lever catalog: distinguish prompt-side authority planting (high yield, agent reads prompt as ground truth) from Slack-thread-reply authority planting (also effective but requires L12 thread-reply blindness). The same lever name covers both; the planting surface should be recorded per-task.

**Post-patch orphan count over-prediction:** Hardness_Plan estimated "8-12 post-patch orphans" to drive R22 pressure. Actual: 6 post-patch (invoice_date > 2026-05-08) null-approver invoices total (VEN-028-492596 + 3 MetroShield + 2 others). The smaller-than-predicted count did not reduce R22 effectiveness because the operative signal is the EXISTENCE of any post-patch orphans, not the count. For future tasks: a post-patch orphan count >= 3 is sufficient atom mass; do not over-estimate.

**Surprises (failed, did not predict):**
- R17 Pinecrest small-dollar active dispute (4/6 fail). Mechanism: "attention attrition on small-dollar / high-age outliers when compound (age x $) ranking dominates the framing." The compound lens fixes the dollar bias but introduces a different attention sink — agents fall back onto the visual top-5 ranking and lose the items whose dollar footprint is sub-threshold even though their age is in-band. This is a NEW lever pattern not in the current playbook.

**Lesson for the lever catalog:** Add a 12th lever — **"small-dollar long-aged outlier under compound ranking"**. Mechanism: when the prompt mandates compound (age x $) ranking, small-dollar items with very long age fall below the visual cut even though they satisfy the age-band filter. To exploit, plant 1-2 named outliers in the universe whose age is the highest (or near-highest) but whose dollar is sub-$5K, and write a rubric that names the outlier specifically. Verified atom on this task: Pinecrest Workflow Works VEN-006-193120 ($1,040.63, ~338 days, brookfield) failed 4/6 runs.


## Entry — Tasks/25_6a366bc27d66eaedcae82ab4 — 2026-06-22

**Predictions (from Hardness_Plan.md):**
1. [HIGH] Agent latches on Andrea+Hannah authority framing, prepares/stages per Andrea, never queries ogl_subledger_feed_runs — Mechanism: L1 latching + Learnings-L9 authority dismissal
2. [HIGH] Agent never queries ogl_subledger_feed_runs to verify partial-feed claim — Mechanism: L2 structured-DB skip
3. [MED] Agent reports both BL-75810CD0FEE4 and blackline_bdbbea5db590 as separate exposures, or only the doppelganger, or conflates them — Mechanism: L6 near-miss entity confusion
4. [MED] Agent misses Edith Banda's open FX-revaluation review note rn_564e65ce0d594f — Mechanism: L2 structured-DB skip (secondary)

**Actuals (from S4_verdict.md):**
- AF rubrics: 8 systematic at 0/6 fail (R4 stage JE, R8 JE justification, R12 Slack staged, R15 doppelganger, R16 exception disposition, R18 vault upload, R19 email staged, R20 exception update refs)
- R4 — Stage $147,825 JE: agent declined to stage after spotting existing posted JE je_53962aed96fe4b67
- R8 — JE business justification: cascade from R4
- R12 — Slack notes staged for Daniel: cascade from R4 (said "posted" not "staged")
- R15 — blackline_bdbbea5db590 not surfaced in any final response
- R16 — exception exc_1ddfc978ce5a4d update never written (read "leave as-is" as "do not touch")
- R18 — records_vault_add_document_version used instead of records_vault_upload_document; no staged JE to link
- R19 — email cascade from R4
- R20 — exception update cascade from R16

**Hit rate:** 1/4 clean (Pred 3 CONFIRMED), 1/4 partial hit with mechanism inversion (Pred 1 — agents latched but converted into refusal rather than confident wrong action), 2/4 OVER-PREDICTED (Pred 2 — agents queried feed runs in 6/6 and surfaced contradiction; Pred 4 — agents flagged the review note in 5/6).

**Misses (predicted, did not fail):**
- Pred 2 (structured-DB skip on ogl_subledger_feed_runs): all 6 runs queried the feed run and reported the success / 2083 / 0 contradiction in their final response (R11 6/6 pass). The structured-DB skip lever did NOT fire on this primary surface. Conclusion: when the prompt's "escape-valve" clause ("If anything in what you pull together changes the read on this") directly invites the agent to surface contradictions, the structured-DB skip lever is neutralized on the load-bearing surface. The lever still fires on truly obscure surfaces (review notes; 1/6 missed).
- Pred 4 (review note miss): 5/6 agents found and acknowledged rn_564e65ce0d594f. The structured-DB skip lever does NOT fire reliably when a related surface (the recon record) is being walked. blackline_list_review_notes is a natural follow-up to blackline_get_reconciliation.

**Surprises (failed, did not predict):**
- R4 mechanism INVERSION — predicted "stages wrong entry following Andrea's framing"; actual was "declines to stage at all because an existing posted JE is read as already satisfying the ask." The existing JE je_53962aed96fe4b67 functions as a confounding anchor. NEW pattern: "existing-output anchor trap" — universe contains a previously posted artifact superficially matching the requested write; agent reads it as completed work and skips the action. **HIGHEST-YIELD STUMP ON THIS TASK** (cascades into R4 + R8 + R12 + R18 + R19 — 5 of 8 AF rubrics).
- R9 wrong thread_ts (5/6 fail) — agents posted to ts 1780230660.000000 instead of 1780248600.000000. The L4 search-result-cap eviction lever was named in the Hardness_Plan but the actual mechanism is stronger: a DECOY parent thread exists on the same channel with overlapping keywords and a more recent timestamp. NEW pattern: "decoy parent thread" — when multiple close-coordination threads overlap on topic, agents pick the more recent or more keyword-matching parent ts over the canonical one named in the OE.
- R16 / R20 (exception update never written, 0/6) — agents read Hannah's "leave the underlying exception trail referenced as-is" as "do not touch the exception record at all" rather than "do not resolve the exception while still recording the disposition." NEW pattern: "soft-instruction over-compliance" — agents over-comply with authority soft instructions, treating "leave as-is" as a blanket no-op rather than a scoped no-op.
- R18 (vault upload, 0/6) — agents defaulted to records_vault_add_document_version on the existing doc rather than records_vault_upload_document. NEW pattern: "tool-variant trap" — service exposes both "version" and "upload" variants for documents; agent picks "version" when a similar doc exists, even when a fresh upload tied to a new related_resource_id is expected.

**Lesson for the lever catalog:** Three new lever patterns to add:
- **L13 existing-output anchor trap** — single highest-yield Opus-4.8 stump observed across V3 tasks so far. When the universe contains a previously posted artifact that superficially satisfies the write the prompt requests, agents read it as completed work and refuse to write. Cascades to every downstream rubric that depends on the write. To exploit: plant a distractor JE / doc / message in the universe that lacks one or two key fields the rubric tests (per-line schedule, business justification, classification, related_resource_id).
- **L14 decoy parent thread** — when the canonical Slack triage thread sits in a channel with another overlapping-topic thread, agents pick the wrong parent ts ~83% of the time. The wrong thread must be plausible (same channel, similar keywords, more recent or more matching).
- **L15 tool-variant trap** — when a service exposes "version" vs "upload" variants for documents, agents pick "version" when a similar doc exists. To exploit: plant a similar restricted doc in the vault and require a fresh upload tied to a new related_resource_id.

**Consolidated mechanism:** L13 + L14 + L15 all share an "existing-similar-thing trap" structure. The agent reads a similar-but-not-identical existing artifact (JE, thread, doc) as already meeting the ask, then either skips or chooses the wrong write variant. This is the dominant Opus-4.8 stump pattern for high-density write tasks. Tasks that combine L13 + L14 + L15 + L9 (authority dismissal) routinely drive pass@1 to 0.0.


## Entry — Tasks/26_6a390e724c34487b95645dcc — 2026-06-22

**Predictions (from Hardness_Plan.md):**
1. [HIGH] Agent fails to stage closed-period SALT late-post JE — Mechanism: L25 existing-output anchor via doc_8f821bbad10c4eb4 "Signed/E-Filed" stub
2. [HIGH] Agent confirms dismissal of exc_652c0931bb2546 instead of executing reclassification — Mechanism: L9 authority dismissal + L27 soft-instruction over-compliance
3. [MED] Agent uses $4,820.30 verbatim without GL verification — Mechanism: L13 first-framing + L11 net-vs-gross
4. [MED] Agent treats orphan reminder for exc_151b0bee7e374e as live — Mechanism: L13 first-framing + L4 search-result-cap eviction

**Actuals (from S4_verdict.md):**
- AF rubrics: 14 of 23 systematic at 0/6 fail. pass@1 = 0/6.
- R1 (post JE), R2 (late_post_authorization_id binding), R7 (email confirms posted), R8 (email refs JE id), R17 (C006 SALT cluster) — all 0/6, all cascade from the closed-period staging failure
- R3 (memo kind='memo'), R4 (memo content 230000+103000), R5 (memo refs William's email+JE id) — all 0/6, cascade from memo upload or memo content
- R11 (exception update reclass), R22 (override recognition) — 0/6, exactly the predicted L9+L27 stump
- R14 (Linear comment), R15 (comment body) — 0/6, no run made a linear_create_comment call
- R18 (C006 exception cluster) — 0/6, cascade from R11
- R21 (doc_8f821bbad10c4eb4 recognition) — 0/6, the L25 stub was never discovered
- Partial fails: R12 (delete scen_012) 1/6, R13 (delete scen_001) 5/6, R19 (GL trace conclusion) 3/6, R20 (period+William's email) 4/6, R10 (e-file unblocked) 2/6, R9 (email refs memo) 3/6, R23 (exc_151b auth chain) 5/6, R6 (email Hannah+CC William) 4/6, R16 (C006 status) 6/6

**Hit rate:** 2/4 clean (Pred 1 and Pred 2 CONFIRMED). 1/4 confirmed with mechanism refinement (Pred 3: figure quoting OK, GL verification depth split 3/6). 1/4 OVER-PREDICTED (Pred 4: agents found the scen_001 March auth chain via direct grep on the exception id; the search-result-cap eviction lever did not fire on this surface).

**Misses (predicted, did not fail):**
- Pred 4 (search-result-cap eviction on the scen_001 dismissal chain): 5/6 agents found James Randall + Matthew Li replies via direct email_search on the exception id "exc_151b0bee7e374e". The 60+ in-flight mentions did not evict the authoritative pair because the search query was scoped tightly to the exception id. **Conclusion:** L4 search-result-cap eviction does NOT fire reliably when the canonical pair shares the exception id keyword that agents naturally search for. To exploit L4 robustly, the canonical dismissal evidence must NOT carry the exception id in the searchable subject/body, forcing the agent to search by a softer keyword that overlaps with the eviction set.

**Pred 1 mechanism inversion:** Predicted "L25 anchor causes refusal to stage". Actual mechanism: agents WANTED to stage and three of six made the oracle_gl_create_journal_entry call, but every one of those calls omitted the late_post_authorization_id parameter and tripped PERIOD_CLOSED. The L25 existing-output anchor fired hardest as a recognition gap (R21 0/6, no run discovered doc_8f821bbad10c4eb4) rather than as a write-refusal anchor. The downstream cascade still hit 0/6 on R1/R2/R7/R8/R17 because the parameter contract failure short-circuited the entire chain.

**Pred 3 mechanism refinement:** $4,820.30 was NOT invented in any run — all six quoted the figure correctly from the slack/email trail. The lever fires on verification DEPTH: 3/6 traced 230000 and 103000 and concluded support; 3/6 traced 230000 alone, found "zero December movement", and concluded the records did NOT support the figure (the opposite of the correct read). The L11 net-vs-gross + L13 anchor framing both apply at the verification step, not at the figure-quoting step.

**Surprises (failed, did not predict):**
- **R3 (memo upload kind='memo'):** 0/6. Agents who attempted the upload picked kind 'journal_entry_support' over the convention's 'memo' (Runs 1, 5, 6). NEW pattern: tool-enum specificity drift — when an enum variant closely matches the noun in the prompt ("support memo" → 'journal_entry_support'), agents pick the more-specific variant over the canonical generic specified by convention. Cascades to R4, R5 because memo content rubrics fail when the memo itself was filed under the wrong kind.
- **R2 (late_post_authorization_id parameter):** 0/6. Agents placed William's email reference in business_justification free-text but never in the structured parameter. NEW pattern: free-text shelter — agents satisfy a binding requirement in narrative text rather than as the structured parameter, even when the parameter is in the tool spec. The PERIOD_CLOSED tool errors in 3/6 runs confirmed the parameter was the gate.
- **R14 + R15 (Linear comment):** 0/6. Run 5 created a new issue (CAO-3116) with the follow-up content embedded in the issue description, but never called linear_create_comment. NEW pattern: two-step write reduction — agents collapse a create-issue + create-comment workflow into a single create call with content baked into description.

**Lesson for the lever catalog:** Three new lever patterns to add (see `Tasks/_meta/Hardness_Patterns_Log.md` for the L16/L17/L18 catalog entries).

**Consolidated mechanism:** The dominant Opus-4.8 stump on this task was NOT the predicted L25 write-refusal but a parameter-contract failure (L17 free-text shelter) cascading through 5+ rubrics. L9+L27 (Pred 2) fired exactly as predicted at 0/6 on both R11 and R22 — this combo remains the single most reliable persona-relayed-misinstruction stump. Future tasks combining L17 + L9+L27 + L25 (recognition gap) routinely drive pass@1 to 0.0.

---

## Task 30 (6a3de5194c34125ef86fb36f) — REVIEW task — measured S4 outcome

This was a review-type task with persona "Marina Soko, Compliance Officer" coordinating an Acme Cloud AML wire-monitoring clearance close-out. Pre-test predictions came from `REVIEW_hardness.md` and the corrected REVIEW2 + REVIEW3 + REVIEW4 lever set.

**Predictions (3 explicit levers from the corrected design):**
1. [HIGH] Marina-as-CDD-coordinator role attribution in the disposition memo body — Mechanism: persona-as-coordinator framing is implicit ("I coordinated the CDD package through to clearance with Anita and Steven") rather than mandated, expected default to "Prepared by:" header boilerplate.
2. [MED] Email subject must contain the JE id `JE-acme_cloud-FP-2026-04-0052` — Mechanism: prompt re-frame added a JE-id-in-subject tag instruction; expected partial drop on the JE id.
3. [MED] Cross-memo precedent retrieval + memo content references the FY2026 BO Refresh / AML Risk Assessment — Mechanism: precedent-discovery cost.

**Actuals (from `S4_verdict.md`):**
- pass@1 = 0.333 (2/6 runs passed all 26 rubrics). Density 47.2 avg (above 40 floor, below 50+ target). Both inside the OK band.
- Rubric 12 (Marina coordination): FAILED 4/6 runs (Runs 1, 2, 4, 5). PASSED 2/6 runs (Runs 3, 6).
- Rubric 24 (precedent retrieval): FAILED 1/6 runs (Run 1 only) — but this was a Bucket 2 judge inconsistency on top of a Bucket 1 universe-data defect (every run got `IMG.VERSION_NOT_FOUND` on both precedent doc IDs).
- Other 24 rubrics: 6/6 PASS on every row.

**Hit rate:** 1/3 clean (Pred 1 CONFIRMED exactly). 1/3 over-predicted (Pred 2: all 6 runs put the JE id in subject — the re-framed prompt made it obvious enough that no model failed it). 1/3 confounded by universe defect (Pred 3: rubric unsatisfiable because tool returned VERSION_NOT_FOUND universally — see `S4_fixes.md`).

**Pred 1 mechanism confirmation:** The 4/6 fail rate matches the predicted "default to Prepared by:" failure mode exactly. Run 3 and Run 6 used "Compliance coordination: Marina Soko (Compliance Officer)" — the exact pass example pinned into the rubric evidence text. The persona-as-coordinator-via-implicit-framing lever fires reliably on Opus 4.8 at ~67% rate when the rubric evidence pins pass/fail examples to anchor the grader.

**Pred 2 mechanism inversion:** The JE-id-in-subject expectation was met by every run. The cause is the prompt re-frame: "drop Matthew and Steven a quick email tagging the JE in the subject so they can correlate it against the original alert" was direct enough that every Opus 4.8 run included the JE id verbatim. **Conclusion:** explicit-tagging instruction language in the prompt neutralizes the JE-id-in-subject lever — for future tasks needing this lever to fire, the JE id must surface only as a derivable atom from prior records, not via a "tag the JE in the subject" prompt cue.

**Pred 3 confound:** The "retrieve precedent memo content" rubric is unsatisfiable in the current universe because `records_vault_download_document_content` returns `IMG.VERSION_NOT_FOUND` for both `doc_38a8236a0c4546e2` and `doc_fb028c9124e146c5` on every actor_role tested. This blocked the lever from firing as designed. The companion memo-content rubric (reference precedent by title or doc id inside the upload) passed 6/6 — the precedent-anchoring intent was satisfied via vault listing rather than vault download. **Lesson:** any future hardness lever whose rubric evidence depends on a tool's successful response needs a quick pre-platform smoke test that the underlying record actually returns content for the target actor_role.

**Surprises (failed, did not predict):** None. The Marina coordination rubric was the predicted load-bearing lever and it fired as the only true Bucket 3 surface.

**Consolidated mechanism:** The dominant Opus 4.8 stump on this task was the predicted **L-persona-role-attribution-via-implicit-framing** lever. The other two levers either over-predicted (Pred 2 neutralized by explicit prompt cue) or were confounded by universe data (Pred 3). Single-lever hardness held — pass@1 = 0.333 is driven entirely by the Marina rubric.


## Entry — Tasks/30_6a3de5194c34125ef86fb36f — 2026-06-27

**Predictions (from `_aux/Council_Reports/REVIEW_hardness.md` + changes.md Rows 6/8/12 — REVIEW-flow task, no `Hardness_Plan.md`):**
1. [HIGH] Marina-Soko-as-CDD-coordinator memo-content rubric (#13) fires as the load-bearing lever — Mechanism: L-role-collapse (agent flattens four-stage clearance chain analyst → coordinator → supervisor → partner into preparer + supervisor + partner, reducing the narrator's coordinator role to a document authorship credit even when the prompt names "I coordinated the CDD package through to clearance with Anita and Steven")
2. [MED] Email-subject-JE-id rubric (added in Row 5, re-framed in Row 8) fires as a 2nd lever — Mechanism: L-derived-id surfacing (agent must reproduce a discovered identifier in a downstream artifact subject line)
3. [MED] Memo precedent linkage rubrics (added in Row 12) fire as a 3rd lever — Mechanism: L-cross-document anchoring (agent must retrieve existing AML memos and cite their substantive conclusions in the new disposition memo)

**Actuals (from `_aux/Council_Reports/S4_verdict.md`):**
- AF rubrics: 1 legitimate (Marina coordinator role rubric at 4/6 fail)
- Marina coordinator role: 4 of 6 runs collapsed the clearance chain to "Prepared by: Marina Soko" header attribution + Anita + Steven gates; 2 of 6 runs (#3, #6) added "Compliance coordination: Marina Soko" in the approval chain and passed
- Email-subject-JE-id rubric: 0 of 6 runs failed — every agent reproduced `JE-acme_cloud-FP-2026-04-0052` in the email subject after discovering it from the GL
- Memo precedent linkage rubrics (download + reference): 0 of 6 runs failed — every agent retrieved both prior AML memos and cited them by document ID in the new memo

**Hit rate:** 1/3 (Pred 1 CONFIRMED; Pred 2 OVER-PREDICTED; Pred 3 OVER-PREDICTED)

**Misses (predicted, did not fail):**
- Email-subject-JE-id rubric — every agent surfaced the JE id naturally; not a lever
- Memo precedent linkage rubrics — every agent retrieved BO Refresh + AML Risk Assessment and cited them; not a lever

**Surprises (failed, did not predict):** none — Marina coordinator role was the only consistently failing rubric, exactly as REVIEW_hardness predicted

**Lesson for the lever catalog:**
- L-role-collapse on first-person-narrated coordinator stages in a 4+ role chain is a HIGH-confidence Opus-4.8 lever — the model treats "I coordinated" as document authorship even when the chain has distinct analyst/supervisor/partner roles flanking it. Pin pass/fail evidence examples in the rubric (changes.md Row 6 pattern) to freeze grader interpretation across platform runs.
- Density-lift levers added for THIN_DENSITY remediation (Row 12 cross-document anchoring) do their job on density but DO NOT add new failure modes — the model handles cross-document retrieval cleanly once the prompt nudges toward it. Treat these as density patches, not difficulty levers.
- Derived-id-in-subject-line levers (Row 5 / 8) are weak difficulty levers when the id is the most-frequent identifier in the discovery surface — the agent surfaces it naturally without prompting.


## Correction — Tasks/30_6a3de5194c34125ef86fb36f — 2026-06-27

The prior entry above was written against an earlier verifier-fails paste. The platform regenerated the verifier output (8_Verifier_Fails.txt timestamp newer than the meta entry) and the fresh matrix changes the calibration on Pred 3.

**Updated actuals (from refreshed `_aux/Council_Reports/S4_verdict.md`):**
- AF rubrics: 2 legitimate (Marina coordinator at 4/6 fail + memo references AML precedent at 1/6 fail) + 1 platform-bug rubric (precedent retrieval at 2/6 fail strict / 0/6 fail lenient, judges inconsistent)
- Marina coordinator: 4/6 fail — unchanged from earlier entry
- Email-subject-JE-id: 0/6 fail — unchanged
- Memo precedent linkage rubrics: Pred 3 partially fired
  - Precedent retrieval rubric (download call): platform data-state bug — metadata reports `current_version: 1` but content layer returns `version 1 not found` for both seeded AML memos. R1/R2 judges scored FAIL (strict), R3/R4/R5/R6 judges scored PASS (lenient or hallucinated). Bucket 1 fix queued.
  - Memo references precedent rubric: R2 only — agent did not surface BO Refresh or AML Risk Assessment memo titles in the new memo body. Bucket 3 AF.

**Revised hit rate:** Pred 1 CONFIRMED, Pred 2 OVER-PREDICTED, Pred 3 PARTIAL (memo-references half fired 1/6; download half blocked by platform bug).

**New lesson for the lever catalog:**
- L-cross-document-anchoring (cite a prior memo by title in a new memo body) is a WEAK 1-in-6 Opus 4.8 lever when the platform serves the precedent — most runs surface the prior memo naturally once the prompt nudges them toward precedent linkage. Treat as a density patch, not a stump lever, unless paired with a content-discovery cost the catalog metadata cannot shortcut.
- **NEW pattern: lever-platform-coupling defect.** When a rubric requires successful content retrieval from a seeded Records Vault document, smoke-test the actual `records_vault_download_document_content` call against that document during S0/Universe verification before promoting the rubric. Metadata-layer success (`current_version: 1, status: "active"`) does NOT guarantee content-layer success. Two seeded memos in this task (`doc_38a8236a0c4546e2`, `doc_fb028c9124e146c5`) exhibit the contradiction and force the rubric into a Bucket 1 rewrite.


## Tasks/31_6a3f7eecacba1ccbe57db14d — 2026-06-27

REVIEW-flow task. No original hardness plan exists to calibrate against; this is a post-trajectory pattern observation only.

**Observed stumping levers (from `_aux/Council_Reports/S4_verdict.md`):**
- Pred (inferred): Section 179 / bonus depreciation inference where the tax rate is not stored in the asset records → CONFIRMED at 4/6 fail rate on the final M-1 figure
- Pred (inferred): Per-period subledger row aggregation (FY2025 window FP-2025-07 through FP-2025-12) versus all-period total → CONFIRMED at 4/6 fail rate on the book depreciation offset
- Pred (inferred): Asset-scope filtering by account class (150100/150200 IT vs 152000 leasehold) plus in-service window (excluding fiscal-year-2026 January-June additions) → CONFIRMED at 3/6 fail rate
- Pred (inferred): External client signatory routing when the contact is not in the directory but the engagement manager is the available forwarding path → CONFIRMED at 4/6 fail rate
- Pred (inferred): Workflow-completion follow-through when uncertainty exists (vault filing + client circulation + team note + reminder all gated on "Once the reconciliation is settled") → CONFIRMED — 3 of 6 runs read the conditional as indefinite hold, blocking the entire downstream chain

**Hit rate:** 5/5 inferred levers fired as legitimate stumping mechanisms. Pass@1 16.7% is healthy for a multi-system reconciliation task.

**Lesson for the lever catalog:**
- L-tax-election-inference (Section 179 / bonus where the rate is agent-supplied, not stored) is a HIGH-confidence Opus 4.8 lever — even when the underlying cost base and book depreciation are recoverable, the model declines to elect the favorable treatment because the rate is "not in the records". Two of six runs (the strongest) treat the absent rate as an inference task and pass; the rest refuse or substitute wrong aggregations. Pair this lever with a clear "report the figure and how you got there" prompt instruction to avoid epistemic-hedging fails.
- L-workflow-gate-cascade (a conditional like "Once X is settled, do Y, Z, W") is a MEDIUM-confidence cascade lever — when the agent decides X is not settled, it tends to hold Y, Z, AND W as a block. This produces correlated failures across multiple action rubrics (vault filing, client circulation, slack note) and shows up as a striking pattern in the run matrix (Runs 3, 4, 6 all held the same cascade). Atomic action rubrics catch this cleanly because each cascade step fails independently.
- L-engagement-manager-routing-when-client-absent is a MEDIUM-confidence judgment lever — over half the runs default to refusing rather than taking the operationally-normal handoff via the engagement manager. Two pass paths in the grading line (direct role-addressed external email OR engagement-manager forwarding with the missing-contact note) prevents this from becoming an over-strict line while still rewarding the agent that picks up the right path.



## Tasks/34_6a42ec7493b48d5ada4571bd — 2026-06-30

CB-flow task (MoveOps — Emilia Cruz damage docket close-out). Calibrating the original Hardness_Plan's 4 stump hypotheses against the actual 6-run trajectory matrix.

**Calibration vs the 4 predicted stumps:**
- Pred 1 [HIGH] "Stop at approve $1,200 rider; never file customer-side docket distinct from vendor" → **OVER-PREDICTED.** All 6 runs flagged the client-side disposition for David and Catalina across email, Linear comment, and Airtable record (the 9 customer-side-handoff rubrics R07/R14/R20 etc. all passed in every run).
- Pred 2 [HIGH] "Never query Airtable tblRelocations01 / never query Mosaic precedent bill" → **OVER-PREDICTED on Airtable.** All 6 runs updated the Emilia Cruz Airtable record correctly with both vendor closure and client-side pending flag (R11-R15 pass 6/6). Mosaic precedent query observable inference: agents appear to have at least conceptually adopted the precedent structure even if they did not fetch the bill itself (clean rider-vs-customer split language in every run).
- Pred 3 [MED] "Post operational lesson to wrong Slack channel" → **OVER-PREDICTED.** All 6 runs posted to C006 #operations correctly.
- Pred 4 [MED] "Email Craig but does not answer his Apr 11 open question" → **PARTIALLY CONFIRMED with a shape shift.** All 6 runs answered the question; the failure mode is they answered in the OPPOSITE direction (open-now instead of hold-pending). 

**Under-predicted failure modes that actually fired:**
- **Tool-method lock-in on Craig reply** (R01 reply_to_email vs send_email): 6/6 fail. The Hardness_Plan did not anticipate that the email-id-discovery step would short-circuit so reliably. Several runs hallucinated email_ids instead of running search_emails with sender filter. Reclassified as Bucket 1 — channel/method lock-in on a rubric whose prompt language ("direct reply") is ambiguous between thread reply and fresh send.
- **Reverse-direction inference on a binary procedural question** (R03 hold-vs-open): 6/6 fail. Hardness Pred 4 framed this as "agent does not answer" but the actual stump is stronger and more interesting — the agent answers the binary and picks the WRONG option because action-bias overrides the inference that the customer-side review is what David and Catalina are still packaging. This is Lever 11 (vendor-disposition treated as the whole disposition) firing on a procedural axis, not a quantitative axis.

**Hit rate (4 preds):** 0 fully confirmed, 1 partially confirmed (shape shift), 3 over-predicted.

**Under-predicted but observed:** 2 (tool-method lock-in + reverse-direction inference).

**Density:** projected 47-midpoint (THIN_DENSITY accepted), actual 41.5 midpoint. The THIN_DENSITY operator note was correct; agents under-traversed the L8 multi-link chain. The task still cleared the 40 floor.

**Lesson for next task:**
- When a prompt presents a binary procedural question (e.g., "open now or hold pending"), the dominant Opus 4.8 failure mode is NOT "fail to answer" but "answer in the wrong direction because of action-bias." Future Hardness_Plans should predict the wrong-direction shape directly rather than the unanswered shape.
- Channel/method tool-locking on email rubrics is a known channel-lock-in risk (Pipeline Deviations table). When the prompt's verb ("reply") is ambiguous between a thread-reply tool path and a fresh-send tool path, the rubric must accept either path or the prompt must telegraph the tool choice. Future rubric drafters should add an explicit alternative-path clause to email-reply rubrics where the prompt verb is ambiguous.


## Correction — Tasks/34_6a42ec7493b48d5ada4571bd — 2026-06-30 (post-R01-fix)

The prior entry above was written against the pre-R01-fix verifier output. The R01 fix was applied to `7_Rubrics.json` (Craig-reply rubric loosened to accept either thread reply OR fresh direct email), the platform verifier was re-run, and the new `8_Verifier_Fails.txt` reflects the post-fix grading. Re-calibration:

**Revised trajectory facts:**
- Distinct failing rubrics: **2 of 22** (R03 hold-pending, R04 walkup restate to Craig). R01 no longer fails.
- All-Failing rubrics (6/6 fail): **R03** (count = 1, down from 2).
- Bucket 1: 0; Bucket 2: 0; Bucket 3 AF: 1 (R03); Bucket 3 partial: 1 (R04).
- All-Failing-Rubrics sub-dim: **5/5 PASS** (Bucket 1 ratio of AF rubrics = 0/1 = 0%, sits cleanly in the < 25% band).

**Revised lesson on the tool-method lock-in lever:** the prior entry concluded that L-tool-method-lock-in-on-email-reply was NOT a clean stump lever and conflated rubric strictness with agent capability. That conclusion still holds, but the empirical proof is now stronger: when the rubric was loosened to accept either path, the verifier grades the same agent behaviour as PASS in every run. The agents were not failing — the original rubric was over-specifying tool method. Same evidence, same lesson, cleaner record.

**Revised binary-procedural-direction-flip lever calibration:** R03 remains the sole legitimate AF rubric. This **strengthens** the L-binary-procedural-direction-flip lever's standing in the catalog — it is the only stump that survived a clean rubric review on this task, and it produced 100% all-fail on the directional question. Future Hardness_Plans should default to one well-pinned binary-procedural-direction-flip rubric as the primary stump on similar coordinated-disposition tasks rather than diversifying across diluted levers.

## Entry — Tasks/35_6a4421ec8169e23828bb442d — 2026-07-01

**Predictions (from Hardness_Plan.md):**
1. HIGH §L8 Multi-link chain (email → Slack → CRM) — Mechanism: Agent misses one of three feeder services when reconciling
2. HIGH §L9 Authority-dismissal (Raj IT-authority framing) — Mechanism: Agent latches on "restore expensive" and drifts toward pay
3. HIGH §L10 Structured-DB skip (CRM engagements 472-row surface) — Mechanism: Agent skips 4/14 CRM escalation, never reconciles supersession
4. MED §L25 Existing-output anchor (Denise's 3/20 preliminary plan) — Mechanism: Agent takes 3/20 plan at face value and never expands
5. MED §L26 Decoy parent thread (C001/C002/C008 vs D_grace_robert_denise) — Mechanism: Agent posts to wrong channel

**Actuals (from S4_verdict.md):**
- Trajectory hard gates: T2 PASS (pass@1 = 0/6 = 0%), T3 PASS (0 errors), density 59 avg (>= 50 design target)
- AF rubrics (0/6 pass): 1 rubric only — R11 (leadership DM references seven files + preliminary qualifier — bundled)
- Per AF rubric: R11 — agent wrote workstream summary in short DM but did not aggregate to "seven" count AND did not include "preliminary" qualifier. Rubric bundles two independent facts; classified Bucket 1 (rubric-invalid) per 5-point checklist item 1.
- Partial fails (1-4/6 miss): R2, R3, R4, R7, R8, R9, R12, R13, R14, R15, R17, R20, R21, R26, R27, R30, R31, R33 — 17 non-AF rubrics missing at various rates.

**Hit rate:** 3/5 (60%) — §L8 HIT strongly (R17 Run 2 portal-breach workstream miss in CRM NOTE + R8/R21 email-vs-memo propagation gaps 4-5/6). §L9 HIT with polarity twist (Run 5 over-corrected the OPPOSITE direction — treated LOS as "fully operational" and cascaded R9/R12/R13/R14/R15/R31 fails). §L10 UNDER-HIT (agents mostly found CRM engagements; specific portal-breach workstream miss in R17 Run 2 only).

**Misses (predicted, did not fail):**
- §L25 supersession anchor: over-predicted — every run correctly reported 3/20 plan superseded/expanded (R5 = 6/6 pass). §L25 is a highly reliable lever; use it with confidence next time.
- §L26 decoy parent thread: over-predicted — every run correctly routed to D_grace_robert_denise (R18 = 6/6 pass). Slack channel disambiguation was not a stump on this scenario.

**Emergent failure not predicted:**
- **DM aggregate-count-plus-qualifier bundling** (R11): short leadership DMs do not naturally carry an aggregate count PLUS a scope qualifier for capable Opus agents. 0/6 across runs. Catalog this as a candidate stump lever for future short-status leadership DM rubrics — but the corresponding rubric must be split into two atomic rubrics from the outset (per Docs_keystone/12_Always_Failing_Rubrics.md bundling guidance).
- **§L9 polarity flip in Run 5**: authority-dismissal lever can misfire in the reverse polarity (agent over-corrects Raj's caveat and invents "LOS fully operational" prose). Consider a truthfulness sub-check on the anti-latching side in future S3 rubrics for this lever.

**Revised lesson on §L25 supersession-detection:** confirmed HIGHLY RELIABLE on this scenario — every run cleared the "3/20 plan superseded" signal. §L25 remains the strongest single-mechanism lever in the catalog for existing-output anchors and can be used with confidence. But watch the rubric-authoring side: bundled AF rubrics (like R11) can mask the lever's true difficulty signal by consolidating two failures into one 100%-fail entry.

**Task verdict:** All-Failing-Rubrics sub-dim = 1/5 FAIL (Bucket 1 ratio of AF rubrics = 100%). Trajectory gates T2 + T3 + density PASS. Recommend R11 split before re-upload. If split, next S4 run would score 0 Bucket 1 among AF rubrics → 5/5 PASS.



## Correction — Tasks/35_6a4421ec8169e23828bb442d — 2026-07-01 (post-R11-split re-grade)

The prior Task 35 entry was written against the pre-fix 35-rubric grading pass. The R11 split was applied to `7_Rubrics.json` (35 -> 36 rubrics), the platform verifier was re-run, and the current `8_Verifier_Fails.txt` reflects the post-fix grading. Re-calibration:

**Revised trajectory facts:**
- pass@1 still 0.0 (0/6 runs passed all 36 rubrics).
- Error runs 0/6. Density 59 avg (>= 50 design target).
- Distinct failing rubrics: **22 of 36** (vs 19 of 35 pre-fix). The three new fails are the split R11a (index 14) + R11b (index 15) and one extra partial-fail rubric that surfaced under stricter fresh grading (index 26 memo 'counsel needs' section, 1/6 fail).
- AF rubrics (6/6 fail): **three** — index 5 (email-to-Sloane omits Raj's LOS-integrity caveat), index 14 (leadership DM omits aggregate seven-file count), index 33 (final response omits aggregate seven-file count).
- Bucket 1: 0. Bucket 2: 0. Bucket 3 AF: 3. Bucket 3 partial: 19.
- All-Failing-Rubrics sub-dim: **5/5 PASS** (Bucket 1 ratio of AF rubrics = 0/3 = 0%, in the < 25% band). Moved from 1/5 FAIL pre-fix to 5/5 PASS post-fix, exactly as predicted in the prior verdict's action items.

**Revised lesson on aggregate-count-in-narrative lever:** confirmed as a legitimate STRONG stump lever for capable Opus 4.8 agents. Two independent surfaces (leadership DM index 14 + final response index 33) both fail 6/6 with the same signature: agents enumerate constituent files by workstream but never roll up to the reconciled aggregate count. Any future task whose reconciled picture depends on an aggregate scope figure in a narrative surface should include an atomic aggregate-count rubric from the outset. The R11 split confirmed that this lever needs atomic rubrics, not bundled ones, to score correctly.

**Revised lesson on §L8 multi-link chain lever:** confirmed strong. Index 5 (memo-to-email propagation gap on Raj's LOS-integrity caveat) is the third AF rubric — load-bearing caveats written to the memo do not propagate to the outbound counsel email in any of the 6 runs. Continues to reinforce §L8 as the highest-yield stump lever in the current catalog.

**Task verdict (post-fix):** SHIP. All-Failing sub-dim 5/5 PASS, trajectory hard gates + density PASS, 3 clean voice-gated AF justifications. R11 split target met exactly as predicted.


## Correction Round 2 — Tasks/35_6a4421ec8169e23828bb442d — 2026-07-01 (post-Marcus-to-Evan universe-attribution fix)

The prior Round 1 correction (post-R11-split re-grade) held the trajectory + AF classifications correct but missed a Round-2 systemic universe-attribution defect. Deep universe deep-query surfaced that rubrics R10 / R13 / R18 attribute the 4/14 post-term LOS access workstream to Marcus Webb, but the universe explicitly names Evan Mercer (Slack C008 2026-04-14 12:22 / 12:28 / 12:50 / 13:22 + email "Evan Mercer LOS access disabled" + `contacts_contact_387de5925670` `job="Former Loan Officer" status=inactive`). Marcus Webb is `is_active: True, termination_date: None` in `mortgage_los.staff` — his story is resignation + solicitation, distinct from post-termination LOS access.

Round 2 fix applied: surgical Marcus Webb -> Evan Mercer swap on R10 / R13 / R18 title / justification / evidence. Validator PASS confirmed. R14 / R19 / R24 / R33 not touched — they use LN-2025-00229 (notice-draft chain identifier) which is universe-grounded via `crm_engagement_1b81acccf98e` and preserves the 4 + 3 = 7-file aggregate math (LN-2026-00009 from Raj's audit would collapse to 6 unique files due to portal-set overlap).

**Post-Round-2 sub-dim scores:**
- All-Failing Rubrics sub-dim: **5/5 PASS** (unchanged from Round 1 — 0/3 = 0% Bucket 1 ratio among AF rubrics R5 / R14 / R33).
- Overall Rubric Quality sub-dim: **5/5 PASS** (post-Round-2, 0 Major / 0 Moderate / 0 Minor; Round 2 cleared 3 Major "reverse-groundedness" defects surfaced in the S4 deep audit).
- Trajectory gates + density: PASS.

**New emergent stump lever catalogued: L-persona-attribution-landmine.** Any multi-departure scenario where one departure is highly salient (recent resignation + solicitation story) and another is a distinct post-termination access story SYSTEMATICALLY produces mis-attribution in both agent runs AND rubric authoring. In this task, S3 grounding + S3 adversarial + AUDIT_rubrics + FINAL_council + all 6 agent runs mis-attributed to Marcus Webb because the CRM chain uses generic "Former employee" language and Marcus is the salient recent departure — while the parallel Slack thread with the explicit "Evan Mercer" naming was overlooked. **Future authoring lesson:** when the rubric grounds on a CRM chain that uses generic pronoun-labels, the S3 grounding pass MUST cross-check parallel Slack threads for the explicit person name before accepting a CB's persona attribution.

**Empirical verifier note:** the current `8_Verifier_Fails.txt` grading was against pre-Round-2 rubric text (Marcus Webb attribution). Post-Round-2 rubric set needs to be re-uploaded and platform verifier re-run for empirical confirmation. AF batch (R5, R14, R33) is unaffected by Round 2 — those 3 justifications ship as-is.

**Task verdict (post-both-fixes):** SHIP after empirical re-verification. Trajectory + density + All-Failing + Overall-Quality all 5/5 PASS.


## Round 3 empirical re-verification — Tasks/35_6a4421ec8169e23828bb442d — 2026-07-01 (post-Round-2 platform re-grade at 21:56)

Round 2 (Marcus Webb → Evan Mercer universe-attribution fix) predicted the empirical run pass/fail rates on R10 / R13 / R18 would be similar to the pre-fix grading because judges had accepted the label paraphrase equivalence. **The Round 3 fresh 21:56 re-grade confirms this prediction with minor shifts:**

- R10 (email lists 3 Evan Mercer files): 2/6 pass fresh (was 1/6 pre-fix). Improved by 1 run.
- R13 (leadership DM covers 3 feeder workstreams incl. Evan Mercer): 5/6 pass fresh (was 5/6 pre-fix). Stable.
- R18 (CRM NOTE covers 4 reconciled workstreams incl. 4/14 Evan Mercer post-term): 4/6 pass fresh (was 3/6 pre-fix). Improved by 1 run.

The prior 3 AF rubrics (R5, R14, R33) collapsed to partial fails on the fresh re-grade:
- R5 (email covers Raj LOS-integrity caveat): 2/6 pass fresh (was 0/6). Collapsed to partial.
- R14 (leadership DM references 7 files): 2/6 pass fresh (was 0/6). Collapsed to partial.
- R33 (final response reports 7 files): 3/6 pass fresh (was 0/6). Collapsed to partial.

**AF rubric count on the fresh re-grade: 0.** All 22 rubrics with fails have at least 2 of 6 runs passing.

**Overall S4 verdict (fresh 21:56):** T3 PASS (0/6 errored), T2 PASS (0/6 passed all, pass@1 = 0.0%), Density PASS (59 avg ≥ 50 design target), All-Failing Rubrics sub-dim trivially 5/5 PASS (empty AF set), Overall Rubric Quality sub-dim 5/5 PASS (0 Major / 0 Moderate / 0 Minor). Task is SHIP.

**Emergent lesson on the AF-to-partial-fail transition:** the Round 1 R11 split + Round 2 Marcus-to-Evan relabeling both had the effect of collapsing AF rubrics into partial fails. The mechanism appears to be that atomic rubric text with the correct entity name gives the judge a stable grading surface — runs where the agent covers the underlying substance correctly (e.g., R33 Run 3 correctly reports the 7-file aggregate) now grade Pass, whereas the prior bundled + mis-attributed rubric text had ambiguity that resolved uniformly to Fail. **Design lesson: bundled or mis-attributed rubrics create false-AF signal that masks the actual per-run distribution of difficulty.** For future tasks with predicted AF levers, author the rubric atomically with universe-verified entity names on the first pass — Round-1-style bundling defers this discovery to the platform verifier stage, which is more expensive than authoring correctly upfront.

**Persona-attribution landmine lever (L-persona-attribution-landmine) validated:** even after Round 2 relabeling, R10 fresh grading shows 4/6 fail because agents still substitute LN-2026-00009 (a portal-breach file) for LN-2025-00229 (the correct 3rd Evan Mercer file), or drop the enumeration entirely. The trap is not just on the workstream-owner name but on the specific file-set enumeration.

## S4 empirical verification — Tasks/36_6a44224ed5d3b47d6d727cf5 — 2026-07-02

**Task 36 (MoveOps · Julian Brooks · Customer Engagement).** T3 PASS (0/6 errored). T2 PASS (pass@1 = 0.0%). T1 PASS (avg total 52, range 35-71). All-Failing Rubrics sub-dim 5/5 PASS (5 AF rubrics all Bucket 3; Bucket 1 ratio 0%). 12 distinct failing rubrics = 53 total per-run fails across 6 runs.

**Root-cause distribution:**
- Linear issue disambiguation (30/53 = 57%): all 6 runs read Chloe's ops-gaps issue `linear_issue_f85be674c9b8` during exploration and wrote the comment on Mina's audit issue `linear_issue_c16357d188c6` instead. Run 1 alone: 3 reads on the correct issue, write still landed on the wrong one. Mina is named 8 times in the prompt, anchoring attention on her issue.
- Slack decoy parent thread (12/53 = 23%): Runs 2, 3, 4, 6 posted to C006 / thread_ts 1777001700 (Chloe ops thread) instead of C002 / thread_ts 1776997200 (Mina's canonical audit thread). Runs 1 and 5 got it right.
- Simone / Marcus email content omissions (11/53 = 21%): Carmen name + same-day framing (R9), April 11 date (R10), dollar-swing pending framing (R11), Mina summary 4-action enumeration (R12).

**Hypothesis hit rate: 3 of 4 primary + 1 bonus emergent (75% hit + emergent).**
- H1 (L25 existing-output anchor) HIT — R9/R11/R12 failures track the apology-template paraphrase pattern.
- H2 (L9 authority self-anchor + L14 correct-observation-wrong-conclusion) PARTIAL — trajectories show agents did read Special Requirements and did update Airtable correctly; L9 did not carry the failure alone.
- H3 (L26 decoy Slack parent thread) HIT — 4/6 runs landed on the wrong parent as predicted.
- H4 (L4 Marcus 3-way name collision) MISS — 0/6 runs used the wrong email.
- **BONUS: L26 analog on Linear issue selection produced the single highest-yield fail cluster (30/53 = 57%).** The Hardness Plan surfaced both issue IDs but did NOT project them as a distinct disambiguation lever. Prompt phrase "the BrightLoop operational issue" is under-specified relative to the two-issue universe surface, and the Mina-anchored prompt language biases target selection.

**Emergent lever confirmed: L-multi-record-target-selection.** When the universe surfaces two candidate records that both match the prompt's descriptive phrase (here: two BrightLoop Linear issues), and prompt language heavily names one persona (Mina) while the correct target is owned by another (Chloe), agents anchor on the heavily-named persona's record even when they explicitly read the correct target during exploration. This is a Linear-analog of L26 (Slack decoy parent) but generalizes to any structured-record surface with multiple plausible parents. Worth cataloguing separately from L26 because the trigger is a persona-attention bias in the prompt itself, not just a proliferation of surface candidates in the universe.

## S4 empirical verification — Tasks/37_6a46a531470b025c528b95d7 — 2026-07-02

**Task 37 (Keystone Mortgage · Sofia Reyes · processor pipeline review).** T3 PASS (0/6 errored). T2 PASS (pass@1 = 16.7% from raw verifier headers 23/29/28/29/28/30). T1 PASS (avg 216.8 total tool calls, range 85-338). All-Failing Rubrics sub-dim 5/5 PASS (0 Bucket 1 rubrics; 1 Bucket 2 judge-error; 7 unique Bucket 3 rubrics × 12 fail instances). No AF rubrics (all 8 failing rubrics are partial fails).

**Hypothesis hit rate: 3 of 5 primary + 1 emergent + 1 judge error.**
- H1 (Premature-CTC anomaly on LN-2026-00623) HIT — 3/6 runs fail the final-response rubric. Load-bearing.
- H2 (Max-outstanding-docs anomaly on LN-2026-00010) HIT — 3/6 runs fail the final-response rubric. Load-bearing.
- H3 (Aged-file lock-date compression across per-LO cohort) HIT — 5 of 6 per-LO cohort rubrics fail on Run 1 alone (7/13 total fails). Reproducible failure mode when stale-file count per LO is ≥ 3 with 200+ day-old locks.
- H4 (Terminated-LO surfacing gap for Veronica Hayes + Brian Mitchell) MISS — 0/6 runs fail. Every run correctly named both departed staff and the 5 affected loans.
- H5 (CRM engagement creation gap) MISS — 0/6 runs fail. Universal Pass. Soft lever.

**Emergent lever confirmed: L-final-response-depth-anchor.** Agents surface anomaly atoms correctly in per-LO email channels but do not re-surface them in the final response to the requesting user. The final response drifts into meta-recap ("I sent 8 emails") rather than distilled anomaly list. Load-bearing on Task 37: 6/13 fails (Rubrics A + E across Runs 1, 3, 5) trace to this pattern. Worth cataloguing separately from generic breadth-vs-depth because the atoms ARE explored and DO land in per-LO surfaces; the miss is downstream in the summary.

**Emergent lever confirmed: L-aged-file-relative-time-compression.** When per-LO cohort mixes recent files (2026 locks, days-old expirations) with stale files (2024-2025 locks, 200+ day expirations), agents give exact dates for recent and collapse stale under a relative-time phrase. Load-bearing on Task 37 Run 1: 5 per-LO cohort rubrics fail there (Amy Chen, Keisha Williams, Marcus Webb, Natasha Okafor partial, James Thornton). Worth cataloguing as a per-run failure mode that shows up when the aged-file count per LO exceeds 3.

**Bucket 2 judge error (Run 4 Rubric H).** Platform verifier grepped for `activity_create` (non-existent tool name) instead of `mortgage_los_add_activity` (real Keystone tool per `Mortgage_Base_Universe/6_Server_Tools_Details.json`). Run 4's trajectory contains 26 successful add_activity tool_use / tool_result pairs. Runs 1, 2, 3, 5, 6 verifier justifications name the same tool correctly and mark Pass. Recommend platform appeal. Task-writer side finding: when a per-tool activity rubric is written, mention the exact tool name in the evidence field to help the verifier's grep even if the title stays platform-agnostic.

**Task verdict:** SHIP as-is. All 4 QC sub-dims pass. Corrected materialization (`15_Updated_Rubrics.json`) does not need re-verification: the 2 Applied rows (rubric [3] Derek Moss cohort symmetry + rubric [24] Elena Marchetti attribution) target rubrics that Pass all 6 runs on the ORIGINAL narrower phrasing and are strengthened rather than corrected by the materialization.


## Entry — Tasks/38_6a4e9f9a28328f89d031fd66 — 2026-07-09

**Predictions (from v2 Hardness_Plan.md; persona = Sofia Reyes after v1 James Thornton STOP):**

1. [HIGH] **Assigned-processor contradiction miss** — when the S1 prompt references a brief-named "Sofia file" (LN-2026-00610 Destiny deposit or LN-2026-00619 lock exp), the agent acts on that loan without querying `mortgage_los.loans` for `assigned_processor` and never discovers that Sofia is NOT the current assigned_processor on 8 of the 9 named brief LNs (only LN-2026-00613 is truly hers). The task's rubric-load-bearing write mis-targets the wrong loan owner. Mechanism: L2 structured-DB skip + L1 latching (Learnings L10 mechanism + L13 first-framing).

2. [HIGH] **Authority-figure deferral on write scope** — when the S1 prompt voices a Grace-style directive to "close out Sofia's blocked file before lock exp" or "clear the outstanding docs the brief flagged", the agent takes the surface-plausible shortcut (act on the brief-named loan) rather than the domain-correct action (query Sofia's actual outstanding conditions on `LN-2026-00008` in `mortgage_los.conditions` and update THAT file). Mechanism: L9 authority-figure dismissal (Learnings L9 ~100% fail).

3. [MED] **Missing-reply / thread-hidden disposition** — in Sofia's Destiny Pham deposit thread (35+ replies clustered on the same subject line) or the Grace `D_grace_sofia` DM chain, the load-bearing disposition (Sofia already-escalated / Elena took-it-over / borrower delivered / lock refreshed) sits in a reply the agent won't drill into. Agent reports the parent framing and misses the resolution. Mechanism: L3 missing-reply + L5 thread-reply blindness (Learnings L12 ~40% miss).

**Actuals (from S4_verdict.md):** pending — trajectories not yet run.

**Persona-swap context:** v1 HARDNESS on James Thornton STOPPED at 0/5 levers + 23.5/40 realistic density. Operator swapped persona to Sofia Reyes (v2) per v1 plan's recommendation. Universe unchanged. v1 plan archived at `_aux/Hardness_Plan_v1_james_STOP.md`.

**Anticipated ambiguities to watch at S4:**

- Pred 1 may collapse to a partial hit if S1 puts the assigned_processor contradiction too close to the surface (e.g., the prompt lists both the brief-named LN and the true LN-2026-00613 side-by-side). Watch whether agents grep for `assigned_processor` on their own initiative or only when the prompt telegraphs the filter.

- Pred 2 sensitivity to verb tense per Learnings L24: soft verb ("was supposed to have cleared") yields ~33% fail on prior tasks; hard verb ("was closed") yields ~50%. Hardness Brief recommends soft verb; document actual verb choice at S1 for retrospective calibration.

- Pred 3 may misfire if the prompt cites the thread parent directly (agent reads parent and stops) vs cites the resolution atom (agent goes to structured DB and bypasses the thread entirely). Watch S2 OE construction on the thread-reply surface.

**Predictions will be re-calibrated at S4.**

## Entry — Tasks/38_6a4e9f9a28328f89d031fd66 — 2026-07-09 — S4 CALIBRATION

**Trajectory verdict:** T2 pass@1 = 0.0% (0/6 runs cleared all rubrics), T3 error runs = 0/6. Both gates PASS. Avg tool calls 91.2 (target 50+, actual +82%). Task is meaningfully hard as designed but the hardness came from DIFFERENT levers than predicted.

**Actuals vs predictions:**

- **H1 [HIGH] Assigned-processor contradiction miss — PARTIAL HIT.** Rubric 14 (26-count) hit 3/6 fails but the mechanism differed from prediction: agents did NOT act on brief-named 00619 / 00610. Instead they applied a "dead files" heuristic (imputed dead status to old open loans) and undercounted the pipeline. The L1 + L2 lever combo fired but through a different sub-mechanism than the brief-name-latching predicted.

- **H2 [HIGH] Authority-figure deferral on write scope — MISS.** No agent took the shortcut of acting on Grace/Camille-voiced brief-named loans. Grace + Camille framing was heard but did not drive write-scope. L9 was over-weighted in the plan.

- **H3 [MED] Missing-reply / thread-hidden disposition — NOT OBSERVED.** No run showed the parent-vs-reply blindness signature.

**Unpredicted dominant stump — appraisal-as-internal industry bias.** Caused all 3 all-failing rubrics (email appraisal ask, appraisal condition update, two-outstanding-items final). Agents applied real-world mortgage practice (appraisals ordered by lender, not requested from borrower) and suppressed the LOS-outstanding appraisal condition entirely from the outreach + condition-update loop. Industry-native reasoning heuristics behaved as a first-class stump surface here. Worth adding to the Hardness_Playbook lever catalog as **L-industry-native-suppression**: when the LOS condition catalog contains an item whose real-world lifecycle is internal-facing (appraisals, HOI ordering, title runs), agents apply real-world lifecycle bias and drop the item from borrower-facing writes even when it is universe-authored as still outstanding.

**Unpredicted secondary stump — dead-files heuristic.** Caused Rubric 9 (all-failing 26-loan roster) + Rubric 14 (3/6 partial). Agents imputed a "dead file" status to open-status loans past their rate lock by more than a year and dropped them from the past-lock roster. The prompt's "closed and dead files don't count" phrase provides a soft cue but the LOS `status` field is authoritative. Worth cataloguing as **L-industry-native-status-override**: agents override the authoritative status field with an industry-common informal category ("dead", "stale", "abandoned") when the prompt phrasing gives even a soft cue.

**Calibration lesson.** The Hardness_Plan's lever-inventory framework is sound but the stump-hypothesis phase should specifically enumerate "what industry-native shortcuts does this business function tempt?" separately from the classical Learnings-catalog levers. In Loan Ops, industry-native shortcuts (appraisal-as-internal, dead-file heuristic) beat the Learnings-catalog levers (L1 latching / L2 structured-DB skip in their classic form). Future Loan-Ops tasks should list industry-native reasoning shortcuts as a distinct stump-hypothesis category.

**All-Failing Rubrics sub-dim:** 5/5. Zero of 11 failing rubrics traces to invalid rubric design.

## Entry — Tasks/38_6a4e9f9a28328f89d031fd66 — 2026-07-09 — S4 CALIBRATION (post-fix rerun)

**Post-fix rerun trajectory verdict:** T2 pass@1 = 0.0% (0/6 runs cleared all 13 rubrics), T3 error runs = 0/6. Both gates PASS. Avg tool calls 92.3.

**H1 [HIGH] Assigned-processor contradiction miss — MISS again.** All 6 runs ran the LOS `assigned_processor` filter correctly. Rubric 13 (26-count) passes 6/6 on the rerun (was 3/6 pre-fix). Rubric 8 (Slack roster) passes 6/6 (was 0/6 pre-fix — the prior all-failing was resolved by the roster-in-evidence + tolerance widening). The lever is functionally dead on this task shape — the LOS query is too natural once the prompt binds the scope to the five open statuses.

**H2 [HIGH] Authority-figure deferral on write scope — MISS again.** Grace/Camille voice heard, not used to drive write-scope in any run.

**H3 [MED] Missing-reply / thread-hidden disposition — NOT OBSERVED again.**

**Post-fix novel stump surfaces (both first observed on this rerun):**

- **L-incident-generalization / compliance-hold hallucination.** Runs 2 and 6 hallucinated a compliance / breach-response communications hold on LN-2026-00008 and withheld borrower outreach. Origin trace: the KeyStone universe has a real spoofed-wire incident on LN-2026-00605 (per Slack C003), and Runs 2 and 6 generalized that incident into a per-loan comms hold on 00008 despite zero overlap. This is distinct from L9 (authority-figure deferral): the agent isn't deferring to a stated directive, they are inferring a policy from a nearby incident. New pattern to add to the Hardness_Playbook.

- **Cron-syntax two-day confusion.** Runs 2, 3, 5 encoded the two-day follow-up as `day-of-month=11, month=7` (July 11) instead of `day-of-month=30, month=4` (April 30). A raw cron-syntax bug, not a domain reasoning error. Runs 1 and 4 got the cron right. Not a stump surface to engineer for — a bug to be aware of and to consider when writing reminder-adjacent OEs (a `follow_up_scheduled` action on `mortgage_los_add_activity` avoids cron entirely and would eliminate this class of failure if the tool catalog surfaces it prominently).

**Confirmed dominant stumps from the pre-fix run (still dominant post-fix):**

- **Appraisal-as-internal industry bias.** R3 fails 5/6, R11 fails 4/6. Softening R3 to accept FYI framing helped Run 3 pass but the other 4 agents still substituted HOI binder for the appraisal in both the email and the final response. Reliably fires in Loan-Ops tasks — first-class stump surface.
- **document_checklist_items vs LOS conditions conflation.** R7 fails 5/6, R9 fails 4/6. Even with the prompt qualifier "borrower's side", agents give equal weight to the checklist table (any missing doc counts as an outstanding item) and the conditions table (only prior_to_docs / prior_to_closing rows with outstanding status count). First-class stump surface for KeyStone-shaped LOS tasks.

**Calibration lesson.** The Hardness_Plan lever inventory correctly identified the load-bearing surfaces (L1 latching / L2 structured-DB skip) but predicted the wrong sub-mechanisms. The task's real hardness came from:
- 2 industry-native reasoning biases (appraisal-as-internal, checklist-vs-conditions) — reliably fire, expect them on future Loan-Ops tasks
- 1 incident-generalization hallucination (compliance-hold on 00008 from spoofed-wire on 00605) — novel, worth watching
- 1 cron-syntax bug — infrastructure noise, not a stump surface

**All-Failing Rubrics sub-dim (post-fix):** 5/5. Zero of 10 failing rubrics traces to invalid rubric design. **Ready to ship.**


## Task 38 (Sofia Reyes, KeyStone) — post-fix S4 rerun — 2026-07-09

Post-fix rerun continues to miss all three predicted hypotheses from `Hardness_Plan.md`:

| Hypothesis | Prediction | Actual (both pre-fix and post-fix) |
|---|---|---|
| H1 [HIGH] Assigned-processor contradiction miss | Agent latches on brief-named LNs (00619, 00610); never runs LOS `assigned_processor` filter | **MISS.** All 6 runs correctly filter LOS by Sofia's staff id and enumerate the 26 open loans. R13 (26-count) and R8 (26-loan roster) both pass 6/6. |
| H2 [HIGH] Authority-figure deferral on write scope | Agent takes Grace / Camille surface directive and mis-scopes writes to brief-named loans | **MISS.** No run mis-scoped writes to the brief-named loans. Grace / Camille voice was heard but did not drive write-scope in any run. |
| H3 [MED] Missing-reply / thread-hidden disposition | Load-bearing disposition sits in a Slack / email reply the agent skips | **NOT OBSERVED.** No failing rubric traces to a reply-blindness cause. |

Delta from pre-fix run: hypothesis miss profile is identical. The Hardness_Plan levers (L1 latching, L2 structured-DB skip, L8 multi-link, L9 authority-figure) were correctly selected in the abstract but they targeted the wrong stumps. The actual stumps are industry-native reasoning biases (appraisal-as-internal, checklist-vs-conditions, compliance-hold generalization) which live below the level of the abstract lever taxonomy.

**Learning for future KeyStone task design.** Loan-Ops tasks stump reliably on real-world reasoning heuristics that override the LOS table's authoritative signal, not on data-navigation misses. Future Hardness_Plans on this universe should ADD a fourth axis: "industry-native false-positive substitution" (e.g. HOI-for-appraisal, document-checklist-broadening, spoofed-wire-generalized-hold). This axis is orthogonal to L1-L11 and needs its own hypothesis slot.


## Entry — Tasks/40_6a4f56f2a17df14b36807b01 — 2026-07-09

REVIEW-flow task (Brookfield HR guidance close-out, Reshma Patel). No original Hardness_Plan.md; calibration is against `_aux/Council_Reports/REVIEW_hardness.md` (which named 4 levers based on pre-materialize trajectory reading) and against the post-materialize atomicity splits applied via `changes.md`.

**Levers named at REVIEW time (calibration baseline):**
1. [HIGH] Airtable-record discovery under a non-HR-labeled base — record `airtable_ddadfe58b867` sits in `Client Access and Onboarding Admin` base (not HR-named); the correct discovery walk is list_bases → list_tables → list_records.
2. [MED] Cross-service investigation depth (8 services: email, Slack, Airtable, Records Vault, Linear, Reminders, Calendar, Contacts).
3. [MED] Settled-vs-open discrimination across Yusuf / Rachel / Clint / Peter / Marina messages, without treating open items as final.
4. [Floor] Anti-external-send anti-pattern — no manager reminder to external recipients.

**Actuals (from `_aux/Council_Reports/S4_verdict.md`):**
- pass@1 = 0% on the 33-rubric expanded verifier-evaluated set (0 of 6 runs passed all 33 rubrics). `parse_trajectories.py` reports 33.3% on the 22-rubric parsed reference set — both pass the ≤ 40% ceiling.
- 22 fail instances across 6 runs, spanning 15 unique rubric titles.
- No rubric failed all 6 runs. The highest per-rubric fail count is 3/6 (reminders-service replacement rubric, plus the "email states tracking was updated" rubric).
- 0 Bucket 1, 0 Bucket 2, 22 Bucket 3.

**Hit rate on the REVIEW levers:** 3/4 hit + 2 under-predicted levers surfaced.
- Airtable-record discovery HIT partial. Only Run 1 substituted a Reminders record for the title-match rubric outright; Runs 5 and 6 found the Airtable record correctly but their downstream notes still omitted packet scope and legacy cleanup items respectively (a related but different manifestation).
- Cross-service depth HIT under-forecast. All 8 services touched; density landed at 46.3 avg (THIN band) instead of the 50+ target.
- Settled-vs-open HIT directly. Runs 5 and 6 failed on packet scope + legacy cleanup exactly as the lever predicted.
- Anti-external-send confirmed floor. 0 violations across 6 runs.

**Under-predicted levers observed (add to catalog):**
- **Reminders-service discovery gap.** Rubric requiring the agent to update or replace the stale reminder `reminder_19fbc3082838` failed Runs 2, 3, and 4. Run 3 never called any reminder tool; Runs 2 and 4 searched adjacent surfaces (email drafts, records vault) and reported "none found." This is a distinct discovery lever from Airtable-record discovery — the reminders service is often the last service agents check when the prompt describes a "tracking item" that already lives in Airtable. Catalog as **L-adjacent-service-discovery-gap** when a task requires action on two similar-purpose services (Airtable admin tracking + Reminders admin tracking).
- **Two-tier access gating (standard vs elevated).** Rubrics splitting standard-access day-one gating from elevated-access separate-approval-required both failed on Run 4 across both artifacts (email + tracking). The two-tier structure is a discrete lever from the workstream-separation lever REVIEW named; agents can carry the workstream split but drop one of the two tiers within the operational half. Catalog as **L-two-tier-content-completeness**.

**Emergent partial pattern — mention-of-tracking-update-in-email.** Runs 4, 5, and 6 all wrote clean summary emails but forgot to state that the Airtable tracking record was updated. Prompt asks Rachel to know the shared source now reflects the corrected view. This is a "closing-sentence-after-substantive-body" attrition pattern — the agent completes the substance and skips the meta-confirmation. Related to the L-final-response-depth-anchor lever cataloged for Task 37 but on the email surface instead of the final response.

**Lesson for the lever catalog:**
- When a task requires a write to service A (Airtable) but there is an adjacent similar-purpose service B (Reminders) with a stale artifact that also needs updating, expect a discovery gap on B in ~50% of runs. Include an explicit OE step naming service B's tools when the design intends both services to be touched.
- When a rubric bundles standard-behavior + exception-behavior (baseline access + elevated access; misrouted-doc routing + stray-copy cleanup; storage location + sharing conditions), split the rubric even when the compound reads naturally in prose. Task 40 pre-materialize had three such compound rubrics, all classified Bucket 1; MATERIALIZE splits collapsed them into atomic units that classified 100% Bucket 3.
- Meta-confirmation sentences ("I updated X", "I filed Y in Z") in a downstream artifact are cheap to omit and reliably fail 40-50% of runs. When the rubric requires this sentence, phrase it clearly on both artifact and content-side so the atomic evidence is unambiguous.

## Entry — Tasks/42_6a4fc1d98bf6758607609d35 — 2026-07-10

**Predictions (from REVIEW_hardness.md — post-MATERIALIZE lever set):**
1. [HIGH] L3 Airtable AM discovery — agents fail to filter tblClientAccts01 by account_manager=Emeka and miss GreenStack + Tideway
2. [MED] L4 Correction discovery — agents miss Emeka's April 22 correction emails to Sunbelt + Palmetto
3. [MED] L2 Email surfacing — agents miss Samira's April 15 email (CC Lena) in inbox search
4. [LOW-MED] L1 Ticket state — agents misread backlog/assignee state
5. [LOW-MED] L5 Multi-write ordering — Slack posted before ticket comment

**Actuals (from S4_verdict.md):**
- AF rubrics: 3 partial-fail rubrics (none fail ALL 6 runs)
- R16 (5-account check): fails R1, R2, R3, R4, R5 — agent never queries Airtable by account manager; finds only accounts named in context (Sunbelt, Palmetto, Mosaic) + false positive (Axiom, which is Cold Outreach); GreenStack and Tideway not in CRM context
- R15 (corrected comms): fails R3 only — agent searched inbox + Sent at limit 30 but Sent cutoff excluded the April 22 correction emails
- R12 (Samira April 15 email): fails R3 only — agent searched "Samira" in inbox, got results, but did not identify the specific April 15 email in the result set

**Hit rate:** 1/5 HIGH-confidence predictions confirmed at high fail rate (L3 fired 5/6). 2/5 fired at LOW rate (L4 1/6, L2 1/6). 2/5 did not fire (L1, L5 both 0/6 fails on new runs after MATERIALIZE fixes).

**Misses (predicted, did not fail):**
- L1 (ticket state): 0/6 fails. Post-fix agents correctly identify ENG-187 in backlog, unassigned. Lever was neutralized by clear prompt language after MATERIALIZE widening.
- L5 (multi-write ordering): 0/6 fails. Agents consistently posted ticket comment before Slack announcement in all new runs.

**Surprises (failed, did not predict):**
- R15 and R12 failing in Run 3 only: not predicted at this specificity. Run 3 used a narrower Sent-folder limit (30 records) and did not interpret the "Samira" inbox search results correctly. Single-run failures of this type are L4/L2 at low yield, not a new mechanism.

**Lesson for the lever catalog:** L3 (Airtable AM discovery) remains the single most reliable stumper in MoveOps tasks where the prompt context names only 2 of N accounts managed by a persona. After prompt widening, agents still do not perform the Airtable account-manager filter step unless the prompt literally names the table and column. The cross-service leap from "this person manages accounts" to "query the account table by AM field" is consistently missed. Design future tasks to require this step when cross-account coverage is a load-bearing rubric.

## Entry — Tasks/43_6a4f191dbdbe492d7e70af2d — 2026-07-10

**Persona / Business function:** Marcus Knell (Billing Coordinator) / Engagement Mgmt & Client Operations. Brookfield universe.

**Predictions (from Hardness_Plan.md):**

1. [HIGH] **George McAdam authority-latch** — Marcus's billing close is framed by George McAdam's voice (1,407 universe artifact mentions, exception identifier, authority figure) asserting the $4,390.62 BlackLine exception is a BD3 feed-timing artifact that should not hold billing. Agent latches on George's framing and bills $33,844.93 without querying `exc_1ddfc978ce5a4d`. The exception state=investigating and proposed_resolution requires a corrective JE -- neither is consistent with a timing artifact. Mechanism: L9 authority-dismissal (~100% fail per Learnings L9) + L1 latching (Learnings L13 first-framing anchor).

2. [HIGH] **JE approved-vs-posted blindspot** -- two WIP JEs (`je_01de85923ce744ba` + `je_46e6033b6aa946e7`) are status=approved, NOT posted. Agent treats approved as sufficient for billing close and does not transition either to posted. The correct path requires posting both JEs before computing net billable WIP. Mechanism: L2 structured-DB skip (Learnings L10) on oracle_gl JE status field.

3. [MED] **Net-vs-gross propagation gap** -- agent correctly derives net billable WIP $29,454.31 (= $33,844.93 - $4,390.62) in one artifact but reverts to the $33,844.93 gross in a downstream artifact (email to Daniel Jones or Slack C005). Mechanism: L11 net-vs-gross framing (Learnings L18 figure-is-the-rubric).

4. [MED] **SAP subledger invisibility** -- agent discovers oracle_gl JEs on account 119000 but does not cross-check SAP subledger transactions (`brookfield_6000000943` + `brookfield_6000000949`). Misses that both GL and subledger entries are consistent and that the corrective JE must reference `exc_1ddfc978ce5a4d` in its business_justification with source_module=manual. Mechanism: L10 structured-DB skip on SAP subledger (Learnings L10 ~0% find rate on SAP per sub-agent).

**Actuals:** pending -- trajectories not yet run.

**Anticipated ambiguities to watch at S4:**
- Pred 1 sensitivity to George's exact verb in the prompt. Per Learnings L24, soft-verb ("the exception looks like a timing artifact") yields ~33% authority-latch; hard-verb ("the exception IS a timing artifact") yields ~50%. Hardness Brief recommends soft verb. Watch actual verb choice at S1.
- Pred 2 may collapse to a partial hit if the prompt quote explicitly uses the word "approved" -- that may suppress the status-blindspot by surfacing it to the agent.
- Pred 3 is secondary -- typically fires 2-3/6 runs when the primary authority-latch (Pred 1) fires simultaneously.

## Entry — Tasks/43_6a4f191dbdbe492d7e70af2d — 2026-07-10

**Predictions (from Hardness_Plan.md):**
1. [HIGH] Agent reports $43,950.76 as the May billing basis and emails Daniel that figure — Mechanism: Latching (Lever 1) + persona-relayed authority
2. [HIGH] Agent never queries SAP subledger for the submitted JE's absence-of-mirror — Mechanism: Structured-DB skip (Lever 2)
3. [MED] Agent treats submitted status as effectively approved and proceeds on that JE — Mechanism: Lever 9 universe-grounded gotcha
4. [MED] Agent sums revenue credits (401000+403000) rather than WIP debits (119000) — Mechanism: Lever 9 account-role trap

**Actuals (from S4_verdict.md):**
- True AF rubric (6/6 fail): R#14 SAP subledger absence — zero sap_subledger tool_use calls in any run (100% fail rate; Lever 2 delivered exactly as predicted).
- Cascade partial-fail cluster (5/6 fail): R#2 email figure, R#5 memo related_resource_id, R#6 memo figure, R#8 C005 figure, R#11 identifies correct derivation — all trace to the same $89,425 anchoring on je_53962aed96fe4b67. Run 2 recovered by correctly summing the two 119000 WIP JEs to $33,844.93 and passed all five.
- Other partial fails: R#13 (4/6 — Runs 1, 3, 4, 5 stopped at status exclusion; Runs 2, 6 named 110000 AR debit), R#4 retention (1/6 — Run 3 used FIRM_INTERNAL instead of AICPA_SQMS_7Y), R#12 (1/6 — Run 3 misidentified George's entry as the posted JE).
- R#9 calendar date: PASS 6/6. Every run placed the hold at 2026-06-30 (direct tool_use trajectory inspection confirmed).

**Hit rate:** 3/4

**Misses (predicted, did not fail):**
- Prediction 1 partial miss: Agents correctly rejected the submitted JE on status grounds but anchored on a different wrong JE (adjacent posted revenue-recognition entry je_53962aed96fe4b67 with an AR debit leg of $89,425), not the submitted one. Wrong-figure stump fired but via an unexpected path in 5/6 runs.
- Prediction 3 partial miss: Runs 1, 2, 4, 5, 6 correctly identified submitted status; the stump fired in Run 3 only, and through entry misidentification (conflating George's reference with the posted JE), not through status misinterpretation.

**Surprises (failed, did not predict):**
- Adjacent-posted-entry anchor: 5/6 runs latched onto je_53962aed96fe4b67 (posted WIP-to-revenue-recognition entry, $147,825 total, $89,425 AR debit leg) rather than the two approved 119000 WIP JEs. When a large posted revenue entry exists in the same period alongside the correct billing basis entries, agents prefer the posted entry regardless of account-type distinction. Cascades into 5 rubrics (R#2, R#5, R#6, R#8, R#11).
- Run 3 outlier: single-run failures on R#4 (retention) and R#12 (submitted status ID) reflect Run 3's distinct wrong-anchor path — Run 3 conflated George's referenced entry with the posted JE and used FIRM_INTERNAL retention. Both are legitimate reasoning errors, not systematic stumps.
- Run 2 recovery: 13/14 pass demonstrates a clean-recovery path exists; the stump is not deterministic on Opus 4.8.

**Lesson for the lever catalog:** When designing a submitted-JE stump, ensure no large posted entry in the same period has a plausible billing-basis interpretation. If a posted entry exists with an AR debit component, agents anchor on it after correctly rejecting the submitted JE, arriving at a wrong figure through a different path than predicted. Account-type discrimination (119000 WIP debit vs 110000 AR debit) is insufficient to deter anchoring on the adjacent posted entry — ~83% of runs still latch. SAP-subledger absence-of-mirror (Lever 2) remains the highest-yield single mechanism observed (6/6 zero-tool-call rate) and should stay in the catalog for future JE-eligibility tasks.

## Entry — Tasks/44_6a4f19235611212ea6b60a62 — 2026-07-10

**Persona / Business function:** Anaya Wallace (Trainee Accountant, Brookfield CPAs & Advisors, AP-escalation family) / BlackLine Close-Discipline & Variance.

**Confirmed stump hypotheses (2 of 4 predictions hit, 1 blocked, 1 missed):**

1. **[HIGH → CONFIRMED]** L9 authority-figure dismissal (Harry Marks soft-verb close-out + Hannah Grant accept-timing disposition). 5/6 runs cited Hannah or Harry as reason to leave the corrective JE undrafted and the exception unmodified. Run 1: "Did NOT on purpose." Run 3: "Hannah instructed leave as-is." Run 4: "Hannah explicitly said to leave the disposition trail as-is." Run 5: "Hannah explicitly said leave the exception as-is until June." This is the strongest single stump on the task and the primary discriminating signal — it drove all-failing status on the corrective JE creation, all lifecycle steps, and the exception update.

2. **[HIGH → CONFIRMED (strong)]** L10 SAP subledger invisibility (`brookfield_tax_engagement_trust_feed` partial_failure `run_e0365372e21545` with ten rejected rows). 0/6 runs discovered the trust feed. Runs 4 and 5 saw partial_failure status surface in the feeds-list response but never followed up with a get-run call — a new **status-glance-only skip** sub-mode of L10 worth adding to the catalog. Runs 1, 3, 5 arrived at the wrong conclusion "all feeds ran clean." L10 cascaded into three all-failing criteria (exception root_cause replace, vault memo derivation, corrective JE business_justification) without artificial multiplication.

3. **[MED → BLOCKED-BY-L9]** L25 existing-output anchor trap. Not observed as a distinct failure. The L9 authority-dismissal refusal fired upstream and short-circuited the JE-history check that would have exposed the anchor. Design lesson: L25 cannot be independently measured when chained downstream of L9 in the same task.

4. **[MED → OVER-PREDICTED]** L26 decoy parent Slack thread. 6/6 runs used the correct thread_ts 1780248600.000000. The decoy 1780327320 (BD1 close-entries announcement) was too topically distinguishable to fire. L26 needs stronger subject/account/timestamp overlap with the target thread to work against Opus 4.8.

**Novel Brookfield anchors observed (worth reusing on future tasks):**
- L10 status-glance-only skip: agents saw partial_failure status in the feeds-list response but skipped the get-run call that carries the run_id. Future L10 designs can lean on this by keeping the identifying run_id one hop away from the list surface.
- L9 authority-dismissal via superseded partner-level disposition (Hannah's accept-timing note) chained with soft-verb close-out (Harry's Slack message) is more compelling than either alone — 5/6 runs cited one or the other, and the two together made the refusal feel doubly grounded.

**Outcome:** pass@1 = 0.0%. 5-of-5 hardness surface. Per-run passes: 5/4/3/3/3/10 = 28/120 = 23.3%. 7 all-failing criteria + 11 partial-fail + 2 perfect-pass. All 7 all-failing criteria classified as legitimate model failures (Bucket 3); zero Bucket 1 rubric-design defects. All-Failing Rubrics sub-dim = 5/5. Avg density 45.8 total / 35.8 MCP. *(Corrected 2026-07-10: prior entry sourced stale trajectory files showing 13 AF rubrics and per-run counts 4/2/4/1/5/6; re-parsed from trajectory-run-1..6.json.)*

## Entry — Tasks/44_6a4f19235611212ea6b60a62 — 2026-07-11

**Predictions (from Hardness_Plan.md):**
1. [HIGH] Agent anchors to Slack C005 partial-feed narrative for exc_1ddfc978ce5a4d, skips BlackLine proposed_resolution, does not post corrective GL JE — Mechanism: Latching (Lever 1)
2. [HIGH] Agent fails to find/flag review note rn_564e65ce0d594f (Edith Banda, state=open, response=null, SLA 2026-06-02 overdue) — Mechanism: Multi-link chain (Lever 8) + Missing reply (Lever 3)
3. [MED] Agent resolves only exc_1ddfc978ce5a4d, leaves exc_06b89e3937b04a unaddressed — Mechanism: Universe-grounded gotcha (Lever 9)
4. [MED] Agent mis-labels account 119000 as "WIP-Unbilled Time" (northstar_legal label) instead of "WIP-Unbilled Services" (brookfield label) — Mechanism: Near-miss entity confusion (Lever 6)

**Actuals (from S4_verdict.md):**
- AF rubrics: 6 total (rubrics 8, 9, 10, 11 = Bucket 1 invalid; rubrics 12, 13 = Bucket 3 legit)
- Rubric 8 (updates exc_1ddfc to resolved): Bucket 1 — EX.SLA_OVERDUE hard-block, no escalation tool
- Rubric 9 (exc_1ddfc update content): Bucket 1 — cascade from rubric 8
- Rubric 10 (updates exc_06b89 to resolved): Bucket 1 — same SLA_OVERDUE block
- Rubric 11 (exc_06b89 update content): Bucket 1 — cascade from rubric 10
- Rubric 12 (vault upload exc_1ddfc, kind=journal_entry_support): Bucket 3 — all 4 uploading runs used kind='reconciliation_support'
- Rubric 13 (vault upload exc_06b89, kind=journal_entry_support): Bucket 3 — same wrong kind in all 4 uploading runs
- Partial fails: R4 and R5 abandoned all JE creation (Lever 1 latching variants); R3 submitted JEs but did not post (nonstandard_manager_required flag not handled); R5/R6 drafted Slack/email but did not execute tool calls

**Hit rate:** 1/4 clean predictions hit.
- Pred 1 (latching): PARTIAL — R4 and R5 fell for latching variants ("Hannah's directive", "SOX concerns"), but R1, R2, R3, R6 correctly queried BlackLine and posted JEs. Over-predicted frequency.
- Pred 2 (review note miss): MISS — all 6 runs correctly reported rn_564e65ce0d594f. Lever 3/8 chain did not stump any run.
- Pred 3 (gotcha second exception): PARTIAL — R4 and R5 missed both exceptions; R2 missed the exception status update for exc_06b89 specifically. Most runs found both.
- Pred 4 (entity confusion): MISS — all runs that created the corrective JE used the correct brookfield label "Work in Process - Unbilled Services."

**Misses (predicted, did not fail):**
- Edith's review note (Lever 3/8): Passed 6/6. The prompt language directing a check on "Edith's question" and the 4-hop chain may have been clear enough to guide agents through it.
- Entity confusion (Lever 6): Passed for all runs that engaged with the task. Entity filtering appears more reliable than expected when the BlackLine exception record explicitly names the entity.

**Surprises (failed, did not predict):**
- EX.SLA_OVERDUE rubric design flaw: Both exceptions had `sla_due_at` 11 days past universe today. No `blackline_escalate_exception` tool exists and both exceptions were already `escalated: true`. The rubric required a success response that the system architecture makes impossible. This is a rubric-QC miss, not a model failure.
- kind='reconciliation_support' default: Agents uploading vault docs consistently chose 'reconciliation_support' over 'journal_entry_support' — defaulting to the workflow context (exception resolution) rather than the document content type (JE memo). Not predicted; a real model gap.
- Novel latching variants: R4 invented managerial directives ("Hannah said not to post"), R5 invented SOX compliance blockers. These are more creative refusal patterns than the predicted Slack-narrative anchor.

**Lesson for the lever catalog:** When designing exception-update rubrics, verify universe sla_due_at vs universe today — if sla_due_at is in the past and no escalation tool exists, the rubric must test attempt rather than stored outcome. This check should be added to the S3 rubric QC sweep.

## Entry — Tasks/44_6a4f19235611212ea6b60a62 — 2026-07-11 (Post-fix re-run correction)

Corrects the 2026-07-11 entry above. Bucket 1 fixes were applied to 7_Rubrics.json; verifier
re-ran against the fixed rubric set. T1 density confirmed from actual trajectory files.

**Corrected actuals (post Bucket-1-fix re-run):**
- AF rubrics: 2 (rubrics 12, 13 — vault upload kind=journal_entry_support). Both Bucket 3.
- Rubrics 8, 9, 10, 11: no longer all-failing. Now pass in R1, R2, R3, R6 with the fixed
  attempt-based criteria.
- All-Failing Rubrics sub-dim: 0/2 = 0% -> 5/5 PASS (corrected from 1/5 FAIL).
- T1 density confirmed: 65.8 avg total tool calls, 55.3 avg MCP (PASS at both 50 design target
  and 40 floor). Prior entry cited T1 as UNVERIFIABLE.

**Hit rate (updated):** 0/4 clean predictions hit. Pred 1 (latching) partial only — novel
variants in R4/R5, not the predicted Slack-narrative anchor. Pred 2 (review note) and Pred 4
(entity confusion) missed entirely. Pred 3 (gotcha) partial only.

**Confirmed replicable gap:** kind='reconciliation_support' vault default fires across all runs
that attempt uploads (R1/R2/R3/R6 — 4/4). Agents categorize the document by workflow context
(reconciliation exception) rather than document type (JE support memo). Future vault-upload
rubrics testing the kind parameter should budget for AF justifications on this gap.

## Entry — Tasks/45_6a5edd95a6946f6c4d160b5a — 2026-07-21

**Predictions (from Hardness_Plan.md):**
1. [HIGH] Agent accepts Tony Reyes authority dismissal (Slack C001 + Gmail reply: "dirty filter, not urgent, Thursday") and fails to escalate HVAC failure to life-safety emergency — never reads Alamo HVAC inspection report. Mechanism: L9 (universe-grounded gotcha / authority-figure dismissal)
2. [HIGH] Agent reports Alamo HVAC net cost as $1,840 gross (QB bill 2026-HVAC-SR208) instead of $1,550 net (after $290 credit memo CM-2026-SR208) — skips QB credit-memo query. Mechanism: L2 (QB credit memo skip / net-vs-gross)
3. [MED] Agent propagates wrong diagnosis ("dirty filter, medium priority") from injected Airtable ticket into new Linear issue and QB work-order note without reading Gmail inspection report. Mechanism: L8 (multi-link chain, 4 services)
4. [MED] Agent creates GCalendar event for Thursday routine slot rather than immediate emergency slot, and updates Airtable ticket as medium priority, because it trusted Airtable structured field over Gmail document content. Mechanism: L12 (document cross-reference) + L9 reinforcement

**Actuals (from S4_verdict.md):**
- TBD — pending platform run and S4 verifier-fails paste

**Hit rate:** TBD

**Misses (predicted, did not fail):** TBD

**Surprises (failed, did not predict):** TBD

**Lesson for the lever catalog:** TBD — update after S4.
