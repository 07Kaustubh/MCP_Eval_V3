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

## Entry — Tasks/38_6a5edd96beaa98710363ebb2 — 2026-07-21 (predicted)

1. [HIGH] Wrong balance on 3-day notice / filing package (gross figure, decoy CustomerRef sums, or $0 from paid-off 8,173.44). Mechanism S1+S3 (L10+L14). Expect 5-6/6 fail.
2. [HIGH] Wrong unit/property (4B / Las Palmas 4B / Hartwell / Rio Bend / renewal Unit 14 instead of Sunset Ridge Unit 14). Mechanism S4+latching (L4+L13). Expect 4-5/6 fail.
3. [MED] Eviction hedged/blocked citing approved ESA accommodation. Mechanism S5 (L14). Expect 2-4/6 fail.
4. [MED] Cascade into owner summary / court prep + over-action (sends instead of drafts, files before owner sign-off). Mechanism L19+L9/L21. Expect 3-5/6 fail.
Actual AF rubrics + calibration delta: pending S4.


## Entry - Tasks/38_6a5edd954557325b498168d1 - 2026-07-22

Universe: StarPM. Persona: Carlos Mendez (Onsite PM, p_009), Property Operations. HARDNESS predictions (actuals filled at S4):

1. [HIGH] Opus reports/marks Las Palmas 8D as ready, or updates the wrong tblMakeReady record, missing the active June turn ([selProg] ready 2026-06-26) + open garbage-disposal Linear issue + MT-2026-1271 Vacant. Mechanism: L8 latching + L25 existing-output anchor + L10 supersession.
2. [HIGH] With Carlos relaying a soft "Brooke already signed off" dismissal, Opus defers to the supervisor and skips the required 8D rework write even after seeing the open disposal issue. Mechanism: L9 authority dismissal.
3. [MED-HIGH] Opus reports the wrong carpet cost ($285 Unit 4B, or $2,680 gross of the two 412 Mesquite bills) instead of the $385 Rio Bend owner pass-through. Mechanism: L4 search-cap eviction + L28 near-dup + L11 net-vs-gross.
4. [MED] Given "Unit 14 carpet", Opus touches the Tanya Mitchell eviction Unit 14 / Sunset Ridge Unit 14 instead of Rio Bend Unit 14. Mechanism: L28/L4 cross-property entity confusion (paired with a write rubric so it is not standalone L4).

Actual AF rubrics + calibration delta: TBD at S4.

### Follow-up - Tasks/38_6a5edd954557325b498168d1 - 2026-07-22 (post-Oracle-review)

Added a 5th predicted stump after the post-Oracle-review density fix introduced the water-heater lever (6th lever, 3rd scenario cluster):

5. [MED-HIGH] Opus closes or marks Tommy Reyes's water-heater ticket (MT-2026-1256) resolved on seeing "replacement done in-house", missing that the flooring damage still requires the external vendor escalation and the $1,340 flooring-vendor work must be recorded before the ticket can close. Mechanism: L14 correct-observation / wrong-conclusion + L8 multi-link (leak -> in-house fix -> flooring escalation).