# Verification — AUDIT_prompt (S1.5 iter-2, Step 0.5 cross-source check)

**Task:** Tasks/38_6a5edd95a6946f6c4d160b5a
**Phase audited:** prompt (S1.5 iter-2, POST F1 Airtable retarget)
**Universe:** starpm (per `_aux/Universe.txt`)
**Verifier:** Veteran QC (STRICTEST) · Audit date: 2026-07-22

## Strictest interpretation re-applied

- Every "should" in QC spec read as "must".
- Every NON-FAIL middle band collapsed to REVISE.
- StarPM V4 density floor: 40+ midpoint (per `Docs_starpm/1`, NOT Brookfield 50+).
- Every soft convention treated as binding.
- Every validator WARN listed as worth-mentioning.
- Every hardness lever must trace end-to-end with cited evidence.
- Every write action must name (a) a tool that exists in the StarPM catalog AND (b) a specific target that exists in the universe.
- Any answer-leakage hit on a derived figure = BLOCKER.

## Data sources consulted (re-verified from source — NOT trusting prior phase outputs)

- `_aux/Universe_Split/airtable.airtable_records.json` :: re-queried tblMaintenanceTickets (51 rows) + tblMakeReady rows for Ridgeview / Finley / Sunset Ridge 208B / Tanya. Confirmed MT-2026-047 (`recb4aeaed326f156`) exists with Finley-portfolio-roof description; MT-2026-063 (`rec7f6e5d4c3b2a1e`) exists for SR 208B AC; `rec8b679d92f30753` exists as tblMakeReady "Ridgeview - Roof Section" with $8,400 owner sign-off note. Tanya multi-row set (`rec769c9f03f0b85f` Las Palmas 4B, `rec91517a5acab558` + `recc83c05d889b354` Unit 14) confirmed.
- `_aux/Universe_Split/slack.slack_channels.json` :: C001 = #maintenance, is_private=False, confirmed.
- `_aux/Universe_Split/slack.slack_messages.json` :: Tony's C001 post ts=1782914700 confirmed (via prior Council A grounding evidence + cross-check).
- `_aux/Universe_Split/contacts.contacts.json` :: aurora.winona@starpm.com, brooke.phillips@starpm.com, tony.reyes@starpm.com, robert.finley@gmail.com, tanya.mitchell@gmail.com all confirmed.
- `_aux/Universe_Split/linear.linear_issues.json` :: **re-verified iter-1's specific escape** — searched for Ridgeview / roof / Finley / Big Bend / Pete Donovan Linear issues. Confirmed non-existence (iter-1 Council A's original finding stands). Iter-2 retarget removed the Item 2 Linear write dependency, closing this escape.
- `_aux/Fact_Ledger.json` :: amounts "8400.00" and "640.00" present.

## Tool catalog verified (universe-aware per `_aux/Universe.txt` = starpm)

`StarPM_Base_Universe/7_Server_Tools_Details.json` — the following tools cited in write-action verification:
- `airtable_update_records(base_id, table_id, records[])` — CONFIRMED (camelCase param names)
- `slack_send_message(channel_id, message)` — CONFIRMED (StarPM-specific: `message` param, NOT `payload` / `text`)
- `create_draft(to[], subject, body)` — CONFIRMED (StarPM Gmail is draft-only; `body` param NOT `content`)

## Eval spec verified for prompt phase

`Evals_starpm/1_Prompt_Eval.md` — strictest reading applied. `Docs_starpm/6_Prompt_Relative_Time_Updates.md` used for today = 2026-07-01 America/Chicago (supersedes stale Jun-12 string in `Docs_starpm/7_QC_Spec_Doc1.json`).

## QC spec re-verified (StarPM Docs, 5 dims / 24 sub-dims)

- `Docs_starpm/7_QC_Spec_Doc1.json` :: all 12 applicable prompt sub-dims re-scored under strict interpretation (12/12 at 5/5).
- `Docs_starpm/8_QC_Spec_Doc2.md` :: appendix taxonomy re-applied to bolt-on WARN triage.
- Caveat honored: `Docs_starpm/13_QC_Companion.md` is Brookfield-contaminated per `Validators/regression_baseline/ROUTING_DECISIONS.md` — NOT used.

## All 8 lenses status (Lens 6 + 9 retired in v18/v21)

- Lens 1 strict QC scoring :: **PASS** (12/12 at 5/5; per-atom evidence table completed including NEW MT-2026-047 row-existence proof)
- Lens 2 answer-leakage sweep :: **PASS** (0 BLOCKER hits on prompt or agent-facing surfaces)
- Lens 3 hardness end-to-end + per-write-target verification :: **PASS** (5/5 levers preserved; 4/4 write actions have verified tool + verified target; **iter-1 Linear-issue escape closed**)
- Lens 4 strict density :: **PASS** (midpoint ~50.5, above StarPM V4 40+ floor; L11+L2+L8 chain forcing-function IMPROVED by retarget)
- Lens 5 adversarial review :: **PASS** (7 checks including new Item-1-vs-Item-2 write-ask ambiguity — resolved via paragraph topic-sentence disambiguation)
- Lens 6 :: RETIRED (merged into Lens 1)
- Lens 7 anti-rationalization :: **PASS** (5 concerns explicitly evaluated; zero talked-out; 3 promoted to WATCH-OUT with deterministic evidence)
- Lens 8 regression-anchor verification :: **61/61 PASS**
- Lens 9 :: RETIRED (merged into Lens 1 + Lens 5)

## Verification statements

- [x] Validator (`validate.py --phase prompt`) already run pre-audit; 0 FAIL, 2 WARN (both bolt-on false positives per Lens 1 Coherence remove-sentence test); results incorporated.
- [x] Regression-anchor suite executed during audit; 61/61 anchors PASS.
- [x] Per-write-target universe grounding executed for all 4 write actions (W1 SR 208B Airtable, W2 #maintenance Slack, W3 Ridgeview roof Airtable retarget, W4 Aurora Gmail draft). Iter-1's specific escape (Linear-issue write with no target) is closed by the retarget AND independently re-verified during this audit.
- [x] Anti-rationalization output check passed; every "considered but decided fine" line traced to deterministic evidence, not convenience.
- [x] Verdict `PASS (STRICT)` recorded in `AUDIT_prompt.md` with explicit per-issue trail and 5 WATCH-OUT notes for downstream phases.

## Discrepancies surfaced (this pass)

- **Iter-1 → iter-2 delta:** iter-1 Lens 3 accepted "L11 TRIGGERED" and "L8 TRIGGERED" without verifying the Linear write target existed. Iter-2 Lens 3 adds the per-write-target row-existence table as a hard gate. This is a permanent methodology fix; future prompt-phase AUDITs on any task should apply the same table.
- **Two Airtable candidate records for Item 2** (MT-2026-047 tblMaintenanceTickets + rec8b679d92f30753 tblMakeReady): both exist and are semantically valid targets for "update the maintenance record" on Ridgeview roof. Hardness_Plan L8 designates MT-2026-047. Downstream OE must NAME the specific record; WATCH-OUT #3 raised.
- **MT-2026-047 desc says "Finley portfolio property" not "Ridgeview" literally**: agent must derive Finley → Ridgeview via contacts / tblMakeReady MR. Intentional per L2 structured-DB skip. WATCH-OUT #5 raised (S3 rubric should not require literal "Ridgeview" text on the ticket record).
- **Density lower bound 40 at floor**: not a fail (midpoint 50.5 well above), but S4 must flag any individual run below 40. WATCH-OUT #1 raised.
