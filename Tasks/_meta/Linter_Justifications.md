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
