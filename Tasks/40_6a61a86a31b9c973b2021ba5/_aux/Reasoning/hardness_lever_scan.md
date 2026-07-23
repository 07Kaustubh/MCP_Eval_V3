# Hardness Lever Scan -- Working Notes

## Per-scenario grep summary (matches per service, excluding Universe_complete_data.json)

| Scenario | AT | GC | Gmail msg | Gmail thr | Slack msg | HubSpot | QB | Linear iss | Linear com | Contacts | Distinct services |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Mesa Vista (4C makeready) | 11 | 23 | 17 | 9 | 17 | 7 | 7 | 2 | 4 | 0 | 9 |
| Las Palmas (8D makeready) | 63 | 24 | 13 | 6 | 10 | 8 | 2 | 3 | 1 | 0 | 9 |
| Rio Bend (carpet) | 9 | 7 | 7 | 5 | 7 | 1 | 2 | 0 | 0 | 0 | 7 |
| Water heater / Hill Country | 4 | 6 | 3 | 3 | 10 | 0 | 27 | 4 | 5 | 0 | 8 |
| A Plus Carpet / Victor Rios | 6 | 26 | 21 | 3 | 6 | 2 | 18 | 0 | 0 | 1 | 8 |

## Anchoring-scenario pick rationale

**Selected: Water heater leak / Hill Country Plumbing (Cat 1 maintenance escalation).**

Why this over the two make-ready candidates:
- Task 39 (Las Vistas 3C QC closeout) failed density at 35-37 tool calls despite hardness midpoint of 50.5. L31 warns that single-cycle QC / makeready closeout scenarios are structurally density-thin. Mesa Vista 4C and Las Palmas 8D are both makeready closeouts and would hit the same shape trap.
- Water heater emergency escalation is naturally broader: tenant Gmail draft + vendor Gmail draft + owner Gmail draft + Slack #maintenance + Linear ticket lifecycle + Airtable maintenance record + QuickBooks bill scope review + GCalendar install slot. Eight services fire without contrivance.
- QuickBooks depth: 22 Hill Country bill records with line-item descriptions -- perfect L2 (structured-DB skip) surface. Agents skim bill totals and skip line descriptions where the load-bearing scope truth lives.
- Existing resolved incident (Tommy Reyes / Linda Castillo / Unit 14 on 5/15-5/27, closed) provides free L1 (latching) -- no injection required for the decoy. Agent naturally finds it first when searching "water heater" and can misconclude "already resolved."
- Persona fit: Carlos leads `maintenance_escalation_waterheater_leak` (6 actions) per PersonaBrief.

Why not:
- Rio Bend (carpet): thinnest cross-service (7 services), no Linear presence.
- A Plus Carpet invoice: too finance-focused for Onsite PM (Carlos participates but doesn't lead the invoice arc).
- Mesa Vista 4C makeready: L31 density-thin risk.
- Las Palmas 8D makeready: same L31 risk; deep Airtable presence pulls agent into single-service loop.

## Per-lever feasibility grid (water-heater scenario)

| Lever | Feasibility | Evidence anchor | Learnings ref | Selected |
|---|---|---|---|---|
| L1 Latching | STRONG | Resolved Tommy Reyes 5/15 incident is more findable than new active incident I inject | L1 (does not fail alone but multiplies with L9), L13 first-framing | YES |
| L2 Structured-DB skip on QB | STRONG | 22 Hill Country bills; agents skim totals, skip line item descriptions | L10 SAP-subledger invisibility mapped to QB per StarPM adaptation | YES |
| L3 Missing reply | WEAK | Redundant with L5 in this scenario | - | NO |
| L4 Near-miss entity alone | WEAK | Multiple Tommy Reyes / John Smith / Carlos crossovers -- but L4 alone is 0% fail per Learnings | L4 explicitly rejected | NO |
| L5 Thread-reply blindness | STRONG | Slack thread with parent + reply flipping priority is natural for tenant-relay updates | L12 in Learnings, L5 in playbook | YES |
| L6 Near-miss entity confusion | PARTIAL | Available but redundant with L4 rejection above | - | NO |
| L7 Multi-write diversification | STRONG | 5+ writes across 5 services naturally required: Slack + Linear + Airtable + Gmail + GCalendar | L5 in Learnings does not fail alone but needed for density; L7 in playbook | YES |
| L8 Multi-link chain | STRONG | A Slack tenant relay → B Airtable ticket → C Linear issue → D QB bill line description | L11 structured-source vs conversation skip | YES |
| L9 Authority-figure dismissal | STRONG | Tony Reyes (Lead Maint Tech) posts scope-narrowing recommendation ("heat exchanger only") in #maintenance | L9 in Learnings (most effective single mechanism, ~100% fail) | YES |
| L10 Reversal / supersession | PARTIAL | Could layer but not needed | - | NO |
| L11 Net-vs-gross | WEAK | Not applicable to scope decision | - | NO |
| L12 Document cross-reference | PARTIAL | Would need a PDF in StarPM_Base_Universe/Data/Files/ that fits. Skipping unless a Ruud RS75 manual naturally exists; QB line description carries the truth without needing PDF | - | NO |

## Selected: L1 + L2 + L5 + L7 + L8 + L9 (6 levers, exceeds default 4-5 to hit L31 midpoint >= 55)

## Injection anchor unit selection

- Mesa Vista Unit 7B: chosen because
  - Carlos's Mesa Vista portfolio (persona-anchored)
  - Not colliding with Mesa Vista 4C (Carlos's makeready lead scenario) or Unit 14 (Tommy Reyes' resolved incident)
  - Robert Finley portfolio (owner) is confirmed for Mesa Vista per 5/28 Slack from U6480117503
- Tenant: Tanya Mitchell (existing tenant contact, tanya.mitchell@gmail.com) -- designated as Mesa Vista Unit 7B occupant via injection
- Vendor: Hill Country Plumbing (existing vendor id 201, ap@hillcountryplumbing.com)
- Authority figure: Tony Reyes, Lead Maintenance Technician (existing, tony.reyes@starpm.com) -- plausible scope authority for plumbing

## Timezone note

- today_horizon.json says America/New_York; AGENTS.md says StarPM canonical is America/Chicago
- Standardizing on America/Chicago per project policy. All injected timestamps use -05:00 CDT.

## Discovery / write-cost budget

Base discovery (5-8) is TIGHT for StarPM because Airtable requires base_id + table_id resolution (extra 2-3 calls before any record read) and Contacts lookups run 2-3 calls (tenant + vendor + owner). Recommend the write-action row be EXPANDED from playbook default 9-12 (3 writes × 3 reads) to 13-18 (5+ writes × 3 reads) to reflect the actual write anatomy for this scenario. This is what pushes the midpoint from 50 (playbook default) to 55 (L31-safe).

