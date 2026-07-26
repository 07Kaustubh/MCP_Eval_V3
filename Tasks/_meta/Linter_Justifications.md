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

## 2026-07-22 — Task 39_6a602c8886ebb06f12354d77 — Class A INVALIDATE (StarPM Persona + Business alignment, within-universe seat misjudgment)

**Linter excerpt (two findings, both returned FALSE):**
> [Persona check] James Bennett is a junior assistant maintenance technician who executes assigned tickets under John's or Elias's direction; "close out" authority, cross-workstream coordination, record reconciliation, crew-facing channel posts, and a status email to John read like a PM or Lead Tech. Suggested reauthoring from Carlos Mendez (Onsite PM).
> [Business alignment] Authoring seat, write actions, and accountability belong to Property Operations (Cat 1.1 Unit Turnover Coordination), not Maintenance & Repairs. "John Smith is a Lead Tech; he doesn't draft status emails to himself."

**Decision: INVALIDATE both, prompt unchanged.** Correct universe (StarPM rulebook on a StarPM task, NOT a wrong-universe error like Tasks 35/36). The linter made a within-universe persona-seat misjudgment:
> (1) Persona is a fixed input, so "reauthor from Carlos Mendez" swaps a given, not a fixable prompt defect. The StarPM persona-anchor rule authors tasks from the persona's HOME function (James = Cat 4 Maintenance & Repairs), not participant appearances; the PersonaBrief authoring line instantiates it ("executes assigned tickets, follows Lead's routing, reports back on completion").
> (2) The load-bearing open item is James's OWN maintenance ticket (OPS-227 / MT-2026-1271, seized 8D disposal he flagged: "routing back to you for parts approval before I swap it"), canonical Cat 4 work.
> (3) Every decision routes to his direct lead John Smith (Lead Maintenance Technician); James never declares ready, approves spend, or directs anyone.
> (4) The business-alignment finding has a factual error: James authors the email, John receives it; different people.
Council A (A4 authority + A10 business function), Council B (Persona 5/5, Business Function 5/5), and AUDIT all passed the prompt; an independent oracle re-adjudication confirmed INVALIDATE on both. Two justifications submitted, one per finding.

**Residual pushback-risk (watch-item, not a defect):** the #make-ready crew-post, since the universe shows John posting the daily progress updates on this turn (recf7aecc318b2252). Rated yellow (pushback-risk), not red. If the platform rejects the pushback, the cheapest surgical concession is folding that crew status into the email to John (triggers full re-gate; do NOT do preemptively; do NOT concede the two flagged voice phrases, they are the strongest ground).

**Justifications submitted:** see `Tasks/39_6a602c8886ebb06f12354d77/_aux/Linter_Justifications.md` (Persona check + Business alignment check).

**Reviewer response:** [pending platform re-check]

**Cross-task pattern:** distinct from the Tasks 35/36 wrong-universe pattern; the linter used the CORRECT StarPM rulebook here and made a within-universe persona-seat misjudgment. First recorded StarPM persona/BF within-universe false-positive. Pattern to watch: the linter under-weighting the persona-anchor rule (home-function authoring) when a maintenance persona participates in a turn that also has a coordinator (Onsite PM) seat.

---

## 2026-07-22 — Task 39_6a602c8886ebb06f12354d77 — Class A INVALIDATE (StarPM Persona + Business alignment, within-universe seat misjudgment)

**Linter excerpt (two findings, both returned FALSE):**
> [Persona check] James Bennett is a junior assistant maintenance technician who executes assigned tickets under John's or Elias's direction. Calling it done to John, squaring up logged records, and posting crew-facing channel updates are above his station... reads like a PM or Lead Tech. Suggested reauthoring from Carlos Mendez (Onsite PM).
> [Business alignment check] The authoring seat, write actions, and accountability posture all belong to Property Operations (Cat 1.1 Unit Turnover Coordination), not Maintenance & Repairs. "John Smith is a Lead Tech; he doesn't draft status emails to himself."

**Root cause of linter false positive:** Correct universe this time (StarPM rulebook on a StarPM task — NOT a wrong-universe error like Tasks 35/36). The linter misjudged the persona seat on the merits: (1) the persona is a fixed platform input, so "reauthor from Carlos Mendez" swaps a given, not a fixable prompt defect; the StarPM persona-anchor rule authors tasks from the persona's HOME function (James = Cat 4 Maintenance & Repairs), not from participant appearances in a turn. (2) The load-bearing open item is James's OWN maintenance ticket (OPS-227 / MT-2026-1271, seized 8D disposal he flagged himself: "routing back to you for parts approval before I swap it. — James"), which is canonical Cat 4.1 work, not turnover coordination. (3) Every decision routes to his direct lead John Smith (Lead Maintenance Technician); James never declares the unit ready, approves spend, or directs anyone. (4) The business-alignment finding contains a factual error — James authors the email, John receives it; they are different people, so nobody emails themselves. Council A (A4 authority + A10 business function), Council B (Persona 5/5, Business Function 5/5), and the S1 AUDIT all passed the prompt; an independent oracle re-adjudication (15m) confirmed INVALIDATE on both findings and advised leading the pushback with the structural argument (authority routes to John + it is his own ticket) rather than the "plausible junior readings" of the two flagged phrases.

**Residual pushback-risk (watch-item, NOT a defect, prompt left unchanged):** the #make-ready crew-post clause — the universe shows John posting the daily progress updates on this exact turn (airtable recf7aecc318b2252). Rated yellow (pushback-risk), not red. IF the platform rejects the pushback, the single cheapest surgical concession is folding that crew status into the email to John (that edit triggers the full re-gate, so do NOT apply preemptively; and do NOT concede the two flagged phrases — they are the strongest ground).

**Justification submitted:** see `Tasks/39_6a602c8886ebb06f12354d77/_aux/Linter_Justifications.md` (voice gate clean, 0 hits).

**Reviewer response:** [pending platform re-check]

**Cross-task pattern:** distinct from the Tasks 35/36 wrong-universe pattern — the linter used the CORRECT StarPM rulebook and made a within-universe persona-seat misjudgment. First recorded StarPM persona/BF within-universe false-positive; the pattern to watch is the linter under-weighting the persona-anchor rule (home-function authoring) when a maintenance persona legitimately participates in a make-ready turn that ALSO has a coordinator seat (Onsite PM). The wrong-universe counter (Tasks 35/36) stays at 2; this task does NOT increment it.

---

## Entry — Tasks/42_6a62ccac9492f2a60e456c1c — 2026-07-25

**Linter excerpt:**
> [Business alignment check] Invented vendor — "Pete Donovan's crew." The Star PM universe has exactly eight approved vendors ... "Pete Donovan's crew" does not correspond to any of them ... Prompts inventing vendors outside the approved list are a universe-rule flag. Return: FALSE.

**Justification sent (verbatim):**
> The prompt names Pete Donovan as the crew on the Ridgeview roof, and he is in the data as a contact listed as an exterior painter at pete.donovan@gmail.com and as a QuickBooks customer record. The Ridgeview roof bill carries a note that Pete Donovan's quote was accepted at 8,400 dollars, and the owner pass-through invoice to Robert Finley describes the job as Pete Donovan Roofing, so the name is taken straight from the records rather than invented. The bill of record for that roof is actually entered under a different vendor, and sorting out which name the payable really sits against before any money moves is exactly what Brooke is asking for here. Naming Pete Donovan the way the existing emails and Slack posts already do is faithful to what she believes going in. Happy to revise if you see something I missed.

**Reviewer decision:** Pending

**Root cause of linter false positive:** Correct universe (StarPM rulebook on a StarPM task). The linter's premise is factually wrong: Pete Donovan is present 40+ times as a contact (Exterior Painter, pete.donovan@gmail.com) and a QuickBooks customer (`proj-f6f9edfeae5c`), and the roof records name him directly (bill 2026-481 note "Pete Donovan quote accepted at $8,400"; owner invoice 2026-494 "Pete Donovan Roofing"). The linter's "approved vendor" rule conflates a conversationally-named crew with the AP vendor of record. The conflict between the named crew ("Pete Donovan / Donovan Roofing") and the booked vendor (Big Bend Restoration, VendorRef 203) is the intended central trap; the suggested revision (name Big Bend in the prompt) would leak the vendor-of-record answer and gut the task. Prompt left unchanged; no additional defects on re-check.

**If rejected:** minimal surgical option is to soften "Pete Donovan's crew is confirmed" to a first-name-only reference ("Pete's crew") without naming a vendor, preserving the trap; do NOT name Big Bend. Any such edit triggers a full re-gate, so do not apply preemptively.

**Cross-task pattern:** Second recorded StarPM within-universe false positive (after Task 39's persona/BF misjudgment). Pattern to watch: the linter applying the eight-vendor "approved list" rule to a conversationally-named crew without checking whether the name is a real contact/customer in the data. Does not increment the wrong-universe counter (stays at 2, Tasks 35/36).

---

## Entry — Tasks/43_6a62ccaf5853030245ac9d53 — 2026-07-25

**Linter excerpt (Business alignment check, Return: FALSE on four grounds):**
> Owner misattribution (Linda Castillo assigned to Mesa Vista, a Robert Finley property), QuickBooks reconciliation and invoice-correction actions outside the Property Operations authority and tool matrix, and an invented Airtable cost field not present in the defined schema. Suggested revision reassigns the owner to Robert Finley and recommends re-labelling the prompt as Portfolio Coordination.

**Justification sent (verbatim):**
> Mesa Vista 4C is Carlos's own turn, and Linda Castillo is the owner on it: the owner invoice for that unit, 2026-534, is made out to her for $1,622 covering the deep clean, the repaint, and the closet trim, and Carlos's email to her titled Mesa Vista 4C Make-Ready Complete is sitting in his sent mail. No 4C invoice exists under any other owner name, so pointing this at a different owner would leave the agent nothing to check the charges against. Carlos also entered and logged the 4C vendor bills in QuickBooks himself, one of them noted as entered by him and another as routed and logged by him, so going back to those same bills to confirm what Linda was actually charged is part of the work he already does on this unit. The make-ready record for 4C already carries its cost and scope detail in a notes field, so the confirmed owner figure has a place to land alongside the status change. Happy to revise if you see something I missed.

**Reviewer decision:** Pending

**Root cause of linter false positive:** Correct universe (StarPM rulebook on a StarPM task). All four findings are contradicted by the records. (1) Owner: AR invoice `445653930748` / Doc 2026-534 carries CustomerRef Linda Castillo against "Mesa Vista Unit 4C" at $1,622; belief email `5101c5a41dffa90a` opens "Hi Linda"; ticket `rec12969a3fdb0852` flags Linda on the 4C turn; the `makeready_turn_carlos` storyline states "an owner invoice gets issued to Linda Castillo." The linter's source is the summary owner table, whose column is headed "Owns / touches" and which states each owner holds one or more properties; Robert Finley's "Mesa Vista (monthly reports)" entry traces to `owner_monthly_report_review`, a Brooke and Lisa reporting scenario, not unit-level 4C billing. (2) QuickBooks: Cat 1 lists QuickBooks among Onsite PM primary systems and 1.4 lists `quickbooks_mock_update_invoice` as a Cat 1 write; the Cat 2.2 write the linter describes is `quickbooks_mock_update_bill`, which the prompt never asks for. Bill notes on `195089456477` ("entered into QB by Carlos") and `546359391323` ("Routed and logged by Carlos Mendez") put the persona in this ledger already. (3) Airtable: the prompt names no field; `tblMakeReady.fldNotes2` is multilineText and both live 4C rows already hold cost and scope narrative there. The linter's own revision resolves to the same field, conceding the mechanism. (4) Authority: pass-through owner invoicing is a defined universe motion and the 4C owner invoice originates in Carlos's own scenario. Prompt left unchanged; re-check surfaced no new defects.

**If rejected:** lead the re-submission with the documentary F1 evidence (invoice 2026-534 plus the sent email). Do NOT concede the owner swap, which is factually wrong and would leave the correction ask with no target. The only cheap surgical concession available is softening the self-attribution of the original bill ("I billed her" to "the bill went out on my turn"), which costs nothing in the levers; never concede the QuickBooks reconciliation, which is the entire spine.

**Cross-task pattern:** Third recorded StarPM within-universe false positive (after Task 39 persona seat, Task 42 vendor list). Same shape all three: the linter treats a summary-doc roster or category shorthand as an exclusive rule and does not cross-check the live records that the authoring guidance names as the anchor of record. Does not increment the wrong-universe counter (stays at 2, Tasks 35 and 36).
