# Linter_Justifications

Append-only. One entry per justification sent back to the platform reviewer (Class A pushbacks only).

## Schema

```
## Entry — Tasks/<TASK_DIR> — YYYY-MM-DD

**Linter excerpt:**
> <verbatim linter complaint>

**Justification sent (verbatim):**
> <2 to 5 sentences, no em-dashes, no references to guides / specs / frameworks>

**Reviewer decision:** <Pending / Accepted / Rejected>

**If rejected:** <one line — what the reviewer said, what we will do differently>
```

## Entries

## Entry — Tasks/24_6a36e84723508b4e3f391cfc — 2026-06-21

**Linter excerpt:**
> Lena Park is the Procurement Officer. Her remit is PO issuance, vendor onboarding diligence, and the SOW lifecycle. She is deliberately separated from AP per segregation-of-duties controls and coordinates with Priya Khatri and Tariq Soto on PO-to-invoice matching — she does not own or work the AP queue directly. The prompt describes someone pulling the full pending-approval AP queue across all three entities, triaging root causes on aged payables, cross-checking AP exception tickets, reviewing open partner sign-off threads, and drafting escalation emails to Daniel with Steven on copy. That is squarely Priya Khatri's territory or Daniel Jones's. ... The engagement-scope verification angle (checking the vault for executed engagement records on Acme and Northstar) is also outside Lena's lane.

**Justification sent (verbatim):**
> I tightened the prompt so Lena is explicitly triaging from the procurement seat and handing off to AP, rather than running the queue herself. Vendors call procurement because that is their relationship contact, and Lena's brief names Daniel Jones as her defined escalation when procurement crosses into AP-disposition territory. The Acme engagement evolved through an addendum and at least one change order, which sit under procurement's SOW lifecycle ownership, so the vault scope check is hers to run. Every write now hands off cross-team or escalates upward, and the prompt closes by deferring all disposition to Priya, Daniel, and Steven. Happy to revise further if you see something I missed.

**Reviewer decision:** Pending

**If rejected:** _(placeholder)_

## Entry — Tasks/27_6a39fd19048f9213281ec7b — 2026-06-23

**Linter excerpt:**
> Function mismatch — this is Cat 7 (BlackLine Close-Discipline & Variance), not Cat 2 (Bookkeeping). The task arc — open variance on a cash account, competing causal narratives across threads, feed-history verification, reconciliation attachment review, prior-period precedent check, multi-party disposition correction, reminder before period certifies — is the canonical Cat 7.2 Live Exception Triage pattern. Bookkeeping's lane is pulling transaction context and feeding it to a senior or compliance officer; it does not own the investigation, the narrative adjudication, or the resolution chain.

**Justification sent (verbatim):**
> Ben Arinzo posts the payroll cash entries on this account, and the activity he is seeing on the brookfield_FP-2026-05 period does not line up with the dropped-feed story the close thread is about to accept. The prompt has him asking someone to confirm the picture across the period's feed history, the reconciliation support, and the prior precedent everyone keeps citing, then take what the evidence actually shows back to the close thread and the seat that wrote up the accept-timing recommendation. He is surfacing findings to the people who will decide, not posting the disposition or signing the recon himself. This is the same transaction-context pull he runs for Marina Soko on her AML triage on Northstar accounts 101000 and 105000, just sized to a variance that has been discussed in more than one channel. Happy to revise if you see something I missed.

**Reviewer decision:** Pending

**If rejected:** _(placeholder — fill in reviewer response and follow-up action)_

## Entry — Tasks/27_6a39fd19048f9213281ec7b — 2026-06-23 (Round 2, similarity) — WITHDRAWN

**Linter excerpt:**
> Prompt Similarity. "This prompt is too similar to an existing prompt:" followed by an earlier Brookfield May close-period prompt (named preparer on the external-vendors payables reconciliation for May, duplicate-entry exception with corrective reversal lined up, get ahead of whoever's about to action the reversal, bring in the people who need to weigh in, log the recurring pattern).

**Justification DRAFTED but WITHDRAWN — not sent to platform:**
> I compared this prompt to every prior submission on file and the closest match comes in at 3.8 percent, with the next nine all below 3.5 percent. The records this prompt is built around (the brookfield FP-2026-05 payroll-cash reconciliation BL-333FF9956BC6 and BlackLine exception exc_aade06f6129e43 on account 102000) do not appear in the prior prompt the reviewer cited, which was a vendor-payables duplicate-entry scenario on a different account. The shape overlap is a bookkeeper voice on an open Brookfield close-period reconciliation, which is shared because that seat is the one who does this kind of work, and the scenario, account, dollar figures, and disposition story are otherwise distinct. Happy to revise if you see something specific I missed.

**Reviewer decision:** N/A — withdrawn before submission

**Withdrawal reason:** Class B (similarity ≥ 40%) has no justification path per project rule (AGENTS.md hard rule #9; Reference/Linter_Playbook.md). Kernel-archetype analysis after the draft confirmed real workflow-shape overlap with Tasks/10 (~35-45% on the remaining kernel after stripping shared persona / business-function / Brookfield / FP-2026-05 / today=June 12 / open-recon-pipeline constants). The shared archetype was "owner pushes back on wrong label, route to deciders before action lands, close out" — present in both prompts. Pivoted instead — see `Tasks/27_6a39fd19048f9213281ec7b/_aux/Linter_Decision.md` Round 2 for the pivot levers (L2 reactive→proactive + L3 variance-label dispute→precedent-validation audit + L6 linear→branching) and the Hardness preservation cross-check.

## Entry — Tasks/27_6a39fd19048f9213281ec7b — 2026-06-23 (Round 5, persona role / authority — third re-flag, pushback)

**Linter excerpt:**
> Persona Match Score: Moderate. Role Check FLAG (level of autonomous coordination — vault filing, channel messaging, direct line to a senior — reads slightly above the operational register of a bookkeeper... orchestrating a multi-output workflow). Personality Check FLAG (notably long and structured). **Org Dynamics Check: PASS** (escalation target George McAdam is appropriate; chain is realistic). Blind Spot FLAG (acting more like a senior accountant than a bookkeeper). AI helper notes "this is not a hard role violation. Ben is not approving anything, not making a disposition call, and explicitly says he wants to take it to George. The flag is one of degree rather than kind." Suggested revision strips vault filing + channel drop + DM, leaving only "let me know what you found" reporting back to Ben.

**Justification sent (verbatim):**
> Ben is the named preparer on BL-333FF9956BC6 and authored the variance explanation sitting on it. His standing daily activities include BlackLine close-discipline work, Records Vault filing, and orphan-exception assignments, so the four output surfaces in this prompt are his standing ones, not adopted senior-tier ones. The reviewer noted Org Dynamics passes and the escalation to George is the right chain, so the remaining concern is length and orchestration. The vault drop, channel FYI, direct line to George, and reminder are the natural artifacts a preparer leaves behind when their own recon is queued to lock in on a precedent that does not match the records they prepared. Happy to revise if you see something specific I missed.

**Reviewer decision:** Pending

**If rejected:** _(placeholder — fill in reviewer response and follow-up action)_

## Entry — Tasks/28_6a390e6b331d1ed9022a9f7c — 2026-06-25 (Brookfield Persona check for v3+ tasks)

**Linter excerpt:**
> The prompt is broadly within Anaya Wallace's wheelhouse — she's the standing trainee on the AP escalation family and handles bookkeeping, reconciliations, and basic schedules. AR aging work is also within her described scope. However, several elements push past what a trainee would realistically own unilaterally: filing directly to the Records Vault under firm classification and tagging to the retention policy ... sending the package to Andrea Phil directly over email ... "I am taking this one to Andrea myself" ... The change-order context is also slightly off: the multi-state sales tax scope lines referenced are TX, GA, and NC — but per the v47 SaaS-taxability determination memo authored by Hannah Grant, the confirmed Acme multi-state sales tax states are TX, NY, WA, and AZ.

**Justification sent (verbatim):**
> Anaya is the trainee who already pulled the Q1 Acme AR buckets back in early April; her post in the monthly-close coordination channel on April 4 carries the figures verbatim. John Bartlett's May 11 kickoff message in the same channel opens the Acme change-order workflow with two scope lines, multi-state sales tax work for TX, GA, and NC, and AR-aging bucket cleanup, which is exactly what the prompt names. Daniel Jones's guidance on the point-in-time framing is in the body of the prompt as the senior touchpoint before Anaya brings the package to Andrea. Hannah Grant's April 5 Acme tax determination document is titled for SaaS-taxable jurisdictions only, which is a different category from the cleanup states the change-order workflow opened. Happy to revise if you see something I missed.

**Reviewer decision:** Pending

**If rejected:** _(placeholder — fill in reviewer response and follow-up action)_

## Entry — Tasks/28_6a390e6b331d1ed9022a9f7c — 2026-06-25 (Brookfield Business alignment check for v3+ tasks)

**Linter excerpt:**
> Function Match Score: Weak. ... Systems Check: Flag — The prompt references account 120000 for AR. The canonical AR account in the Brookfield universe is 110000. Account 120000 does not appear in the documented chart of accounts for any entity. ... Write Actions Check: Flag — the prompt does not specify a retention code or classification label ... Scope & Authority Check: Flag — A trainee pulling an AR aging cross-cut for a partner-level change-order package and routing it directly to Andrea Phil is a scope mismatch. ... Universe-Rule Check: Flag — Multiple issues: Wrong AR account: 120000 is cited; the canonical AR account is 110000. Acme SaaS sales-tax nexus error: TX, GA, and NC ... TX, NY, WA, and AZ ... No fiscal period ID on the ledger pull ... Trainee as direct partner-routing seat.

**Justification sent (verbatim):**
> The work in the prompt is a Q1 AR aging cross-cut for Acme, which is normal bookkeeping work for a trainee preparing the cross-cut before it goes up the chain. The account number 120000 in the prompt is taken verbatim from Anaya's own April 4 post in the monthly-close coordination channel where she anchored on that account when she first pulled the buckets; the verification clause asks for the ledger walk-back, which is where the agent is expected to confirm the right Acme AR account against the chart and reconcile against the anchored figures. The multi-state scope lines (TX, GA, NC) and the AR-aging cleanup match John Bartlett's May 11 kickoff message in the close coordination channel word for word. The four writes (vault, close coordination channel post, Andrea over email, self-reminder) sit inside one coherent change-order package situation, and the retention and classification phrasing is the trainee voice the agent is expected to resolve against the dominant codes for working-paper memos. Happy to revise if you see something I missed.

**Reviewer decision:** Pending

**If rejected:** _(placeholder — fill in reviewer response and follow-up action)_

---

## 2026-07-01 — Task 35_6a4421ec8169e23828bb442d — Class A INVALIDATE (Business Function pattern-fit)

**Linter excerpt:** "FALSE — The prompt is not consistent with the Executive & Risk Oversight function as defined in the Brookfield universe. It describes a ransomware incident-response decision at an organization outside the Brookfield scenario entirely, references no Brookfield personas, systems, tools, retention codes, or structural conventions, and maps to none of the nine Executive sub-patterns. The mismatch is categorical, not correctable by minor revision."

**Root cause of linter false positive:** The platform linter ran the Brookfield rulebook against a KeyStone Mortgage Partners universe task. `_aux/Universe.txt` = keystone; persona is Robert Calloway (Owner / Licensed Mortgage Broker at KeyStone); anchoring scenario is `scenario_14b3ffde` (2 BTC ransomware pay-vs-restore on the LOS environment). All flagged "missing" atoms (Brookfield personas Steven Perry / Matthew Li / Andrea Phil / William White, BlackLine / Oracle GL / SAP Subledger tool families, AICPA_SQMS_7Y retention codes, Cat 4.1-4.2 AML patterns, Linda Burns as legal NPC) are Brookfield-universe atoms that categorically do not apply to KeyStone-universe tasks. Council A + Council B + AUDIT (STRICT) all passed the prompt against the correct (KeyStone) rulebook.

**Justification submitted:** see `Tasks/35_6a4421ec8169e23828bb442d/_aux/Linter_Justifications.md`.

**Reviewer response:** [pending platform re-check]

**Cross-task pattern**: this is the 1st recorded instance of the platform linter defaulting to the Brookfield rulebook on a non-Brookfield-universe task. If pattern recurs across ≥ 2 more KeyStone / MoveOps tasks, consider filing a platform issue.

---

## 2026-07-02 — Task 36_6a44224ed5d3b47d6d727cf5 — Class A INVALIDATE (Business alignment — wrong-universe linter)

**Linter excerpt:** "Keystone Business alignment check for v2.2 tasks ... Function Match Score: Weak. Pattern Fit: Flag. Systems Check: Flag (Road Runner, Airtable, Linear cited as absent from function tool matrix). Write Actions Check: Flag (Linear comment, Airtable update, Calendar hold). Scope & Authority Check: Flag (scope more consistent with Operations or Executive than Customer Engagement / Support). ... FALSE — The prompt is not consistent with the Customer Engagement / Support function as defined. The scenario describes a corporate relocation program with housing placement and vehicle transport logistics, operating on systems (Airtable, Road Runner, Linear) that do not exist in the defined business environment."

**Root cause of linter false positive:** The platform linter ran the KeyStone Mortgage rulebook against a MoveOps universe task. `_aux/Universe.txt` = moveops; persona is Julian Brooks (Lead Customer Support Specialist at MoveOps Inc.); anchoring scenario is BrightLoop April cohort service recovery covering Simone Richter (housing / UrbanNest) and Marcus Webb (vehicle / Road Runner). All flagged "missing" atoms are MoveOps-native: Airtable (273 hits, 167 records, 2 bases, 3 tables — source-of-truth for relocation state per AGENTS.md MoveOps hardcoded landmine), Linear (527 hits, 69 issues, 8 projects, 79 comments), Road Runner (36 hits — vehicle carrier vendor), BrightLoop (313 hits — real client), UrbanNest (101 hits — housing partner), Simone Richter (54), Marcus Webb (91, MoveOps person — DISTINCT from KeyStone's departed-employee Marcus Webb per AGENTS.md landmine), Julian Brooks (13), Mina Hashimoto (146 — audit thread owner). Customer Engagement / Support is a defined MoveOps business function at 30% weight.

**Justification submitted:** see `Tasks/36_6a44224ed5d3b47d6d727cf5/_aux/Linter_Justifications.md`.

**Reviewer response:** [pending platform re-check]

**Cross-task pattern update**: this is the 2nd recorded instance of the platform linter running the wrong universe's rulebook (Task 35 KeyStone was flagged against Brookfield; Task 36 MoveOps flagged against KeyStone). Both were categorical wrong-universe classification errors at the linter level, invalidated with clean voice-gate justifications. Threshold noted in Task 35 entry was "≥ 2 more" for platform-issue filing; we are now at 2 total. One more instance (KeyStone or MoveOps universe hit with a non-matching rulebook) crosses the threshold — consider surfacing to the platform on the next occurrence.

---

## 2026-07-22 — Task 38_6a5edd95a6946f6c4d160b5a — Class A INVALIDATE (Persona/scope + Business alignment)

**Linter excerpts (two separate checks, both returned FALSE):**

- **Persona check:** "Persona Match Score: Moderate. Role Check: Flag ... The prompt as written is assigned to Denise Morales, but the scope ... exceeds an Onsite PM's lane and maps cleanly to Brooke Phillips. The persona assignment is the inconsistency; the prompt content itself is well-formed."
- **Business alignment check:** "Function Match Score: Inconsistent ... Sunset Ridge does not exist. Sunset Ridge is explicitly called out in the universe lint rules as an invented property that is NOT part of the managed portfolio. The five populated properties are Mesa Vista, Las Palmas, Las Vistas, Rio Bend, and Ridgeview. 'Sunset Ridge 208B' is a hard flag. Tony Reyes is an NPC ... Tanya Mitchell make-ready record framing ... 'Status' is not a named field in tblMaintenanceTickets."

**Root cause of linter false positives (two distinct bugs on one submission):**

1. **Persona check is stale.** Prior S1.5 iteration (2026-07-22 earlier round, see `_aux/Linter_Decision.md`) already reassigned the prompt from Denise Morales to Brooke Phillips based on the same linter's own suggestion. `2_Persona.txt` + `PersonaBrief.txt` + `5_Prompt.txt` are all Brooke-authored now. The persona check on this round appears to have scored against the earlier Denise submission, not the current Brooke version. Every persona-scope complaint (Aurora briefing, Ridgeview roof CapEx, cross-portfolio brief) maps cleanly onto Brooke's canonical scope: cross-portfolio ops sync, vendor invoice approval, budget oversight, owner reporting, CapEx approval flow with owners. Signature scenario `owner_portfolio_review_midyear` has Brooke coordinating with Aurora Winona directly; 22 calendar events pair them together.

2. **Business alignment check is running against a wrong / stale property allowlist.** `_aux/Universe.txt` = starpm, correct universe. But the linter asserts a five-property portfolio (Mesa Vista / Las Palmas / Las Vistas / Rio Bend / Ridgeview) that OMITS Sunset Ridge. Universe grep shows Sunset Ridge is real and heavily populated: Units 208B / 309C / 104B / Unit 14 all present across Airtable records (MT-2026-063 for Unit 208B in tblMaintenanceTickets), Slack #maintenance threads, Gmail (Alamo HVAC thread), calendar, and Tanya Mitchell's payment plan records are keyed to Sunset Ridge Unit 14. Tony Reyes is `tony.reyes@starpm.com` (present in `slack.slack_users.json` + `contacts.contacts.json`), an internal maintenance tech, not an NPC at a sister property. `$8,400 approved scope from Robert` is real: Ridgeview Roof Section Repair, owner Robert Finley, vendor Pete Donovan. `tblMaintenanceTickets` field schema (`fldPriority`, `fldDescription`, `fldTicketNumber`, `fldCompletionDate`) makes "current status" a natural agent-picks-fldDescription write; the ambiguity claim is a technicality that doesn't survive normal natural-language reading.

**Justification submitted:** see `Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Linter_Justifications.md`. Voice-gate clean (0 forbidden-term hits, 0 em/en dashes).

**Reviewer response:** [pending platform re-check]

**Cross-task pattern update — 3rd instance of platform-linter-wrong-model:**

- Task 35 (2026-07-01): KeyStone universe task linted against Brookfield rulebook (wrong universe rulebook loaded).
- Task 36 (2026-07-02): MoveOps universe task linted against KeyStone rulebook (wrong universe rulebook loaded).
- Task 38 (2026-07-22): StarPM universe task linted against a stale/incomplete StarPM property allowlist (correct-universe-but-outdated-model). This is a slightly different flavor than 35 / 36 — the linter got the universe right but got the property inventory wrong (Sunset Ridge omitted despite 20+ universe references).

Threshold from Task 35 entry was "if pattern recurs across ≥ 2 more KeyStone / MoveOps tasks, consider filing a platform issue." We are now at 3 total wrong-model instances across 3 universes. **Recommendation: surface to the platform on next occurrence** — either the linter's universe-rulebook loader or its property-inventory model is behind the actual per-task universe data, and a spot-check of what property list the platform ships against StarPM tasks would confirm whether this is a stale allowlist bug or per-task-linter-data drift.

---

## 2026-07-23 — Task 40_6a61a86a31b9c973b2021ba5 — Class A INVALIDATE (Property Operations business alignment — persona/entity + lane)

**Linter excerpt (five flagged issues, single Property Operations business alignment check returning FALSE):**

1. "Diane Flores misattributed to Hill Country Plumbing. Universe rules place Diane Flores at Lone Star Maintenance Supply, not Hill Country Plumbing."
2. "Tony Reyes NPC sign-off authority. Tony Reyes is an NPC Lead Maintenance at a sister property with no internal Star PM authority."
3. "QuickBooks bill read outside Property Operations lane. `quickbooks_mock_get_bill` belongs to Portfolio Coordination 2.2, not Property Operations 1.2."
4. "Direct owner communication without Brooke. Drafting a cost heads-up directly to Robert Finley is owner-relations work (Portfolio Coordination 2.3)."
5. "Scope-change escalation gate missing. If the revised scope crosses the vendor-spend threshold, the Onsite PM would need to loop Brooke before confirming with Hill Country."

**Root cause of linter false positives (two independent bugs):**

1. **Diane collision (naive name-match).** Prompt says "Diane, their AP contact at Hill Country" — an anchor added at v4 (AUDIT F2 fix) specifically to disambiguate. Universe evidence: injected Gmail record 7b (`ap@hillcountryplumbing.com`, `internal_date` 2026-06-29 15:12 CDT) is signed "Diane at Hill Country Plumbing" verbatim (base64 body decoded). Diane Flores at Lone Star Maintenance Supply (`diane.flores@lonestarmaintenancesupply.com`, Account Representative) is a different vendor and does not appear anywhere in the Mesa Vista 7B thread. Linter appears to name-match "Diane" without checking the vendor anchor.

2. **Tony Reyes NPC misclassification (universe-model error).** Fact_Ledger + `entities_personas.md` both show `tony.reyes@starpm.com` → "Lead Maintenance Technician", internal Star PM staff. No "sister property" concept in Star PM (single-firm, ~10 apartment properties, one shared `#maintenance` channel C001). Linter's "NPC at sister property" characterization has no universe grounding.

Complaints 3-5 (QB bill lane, owner comms lane, escalation gate) are subjective lane / process interpretations, not universe-rule violations. QB bill read is a designed cross-service verification lever (L2 in Hardness Plan). Direct owner comms on a courtesy heads-up is a normal onsite-manager action. Escalation gate is speculative (linter assumes scope will cross threshold; prompt doesn't commit).

**Justification submitted:** see `Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Linter_Justifications.md`. Three paragraphs, no em-dashes, cites `ap@hillcountryplumbing.com` and `tony.reyes@starpm.com` as concrete records.

**Reviewer response:** [pending platform re-check]

**Cross-task pattern update — 4th instance of platform-linter-wrong-model:**

- Task 35 (2026-07-01): KeyStone universe task linted against Brookfield rulebook.
- Task 36 (2026-07-02): MoveOps universe task linted against KeyStone rulebook.
- Task 38 (2026-07-22): StarPM universe task linted against stale StarPM property allowlist (Sunset Ridge omitted).
- Task 40 (2026-07-23): StarPM universe task linted with (a) naive name-match Diane collision (ignoring vendor anchor) and (b) universe-model error on Tony Reyes NPC classification. Both errors are StarPM-native persona/entity misclassifications.

Pattern signal strengthens: StarPM tasks are drawing 2/2 recorded linter false positives, both with the linter's persona/entity model out of sync with actual universe records. Task 38 was a property-allowlist gap; Task 40 is a two-bug persona/entity misclassification. **Recommendation confirmed: surface to platform on next occurrence** — the StarPM linter model appears to have systemic drift from the actual `3_UniverseDataForThisTask.json` snapshot the CBs ship. Consider requesting the platform expose which universe-model version the linter loads so we can spot per-task drift before submission.
