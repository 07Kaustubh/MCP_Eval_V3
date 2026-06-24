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
