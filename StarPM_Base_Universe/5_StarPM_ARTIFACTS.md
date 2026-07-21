# Star Property Management — Artifacts

The systems catalog. What each service holds, what its object shapes look like, and how they thread across scenarios. Read this when you need to know *where* a piece of ground truth lives.

> **Naming convention.** Service display names below drop the "Mock" suffix (e.g., "Airtable" not "Airtable Mock"). Tool identifiers in code / prompts retain the underscore form (e.g., `airtable_mock_list_records`).

---

## The 8 services

| Service | Role | Heaviest surface |
|---|---|---|
| **QuickBooks** | Accounting system of record | Bills (360), invoices (318), credit memos (296), estimates (334), payments (129) |
| **Airtable** | Workflow tracking | Make-Ready Turns (167) + Maintenance Tickets (231) |
| **HubSpot** | Leasing CRM | Deals (103), contacts (61), companies (7), notes, tickets |
| **Linear** | Maintenance ticket system | Issues (223) across 3 projects |
| **Gmail** | External + internal correspondence | Threads (151) / messages (479) |
| **Slack** | Internal coordination | 8 channels, message volume varies |
| **Google Calendar** | Scheduling | Events (113) — tours, vendor visits, court dates, syncs |
| **Contacts** | Directory | 61 entries — every persona + NPC |

There is **no filesystem MCP service** in the universe. Documents that would normally live on disk (application docs, inspection reports, screening reports, filing packets) travel as Gmail attachments, HubSpot notes, or Airtable record fields. The `Data/Files/` folder contains **read-only reference PDFs** (contracts, invoices, reports) the agent can read directly during task execution — these are universe data, not an editable filesystem. CBs never modify them.

---

## Airtable

Airtable holds two tables — the operational workflow trackers.

### Table: `Make-Ready Turns` (`tblMakeReady`, 167 records)

Tracks a unit's turn from move-out through market-ready.

**Fields:**

| Field ID | Name | Type | Meaning |
|---|---|---|---|
| `fldUnit` | Unit | Single-line text | Property + unit identifier (e.g., "Las Palmas 8D", "Mesa Vista 4C") |
| `fldTurnStatus` | Status | Single-select | Turn stage (`selSched`, `selProg`, `selReady` — schedule → in progress → ready) |
| `fldMoveOut` | Move-Out Date | Date | When the outgoing tenant vacated |
| `fldTargetReady` | Target Ready | Date | The date the unit should be marketing-ready |
| `fldNotes2` | Notes | Multiline text | Free-text notes including owner references, contractor names, punch-list highlights |

**Property distribution across the 167 records:** Las Palmas (heaviest — 87 mentions), Las Vistas (40), Mesa Vista (16), Rio Bend (14), Ridgeview (2). A minority of records use unit-only naming without an explicit property prefix.

### Table: `Maintenance Tickets` (`tblMaintenanceTickets`, 231 records)

Property-visible maintenance ticket tracking. Complements Linear (which is the primary maintenance system of record — see below).

**Fields:**

| Field ID | Name | Type | Meaning |
|---|---|---|---|
| `fldTicketNumber` | Ticket Number | Single-line text | Format `MT-2026-XXXX` |
| `fldDescription` | Description | Multiline text | Free-text description of the issue |
| `fldPriority` | Priority | Single-select | Priority level (`selHigh`, etc.) |
| `fldCompletionDate` | Completion Date | Date | When the ticket was closed |

**Note on cross-reference with Linear.** Airtable Maintenance Tickets (`MT-2026-XXXX`) and Linear issues (`OPS-N`) are parallel systems with **no cross-references between them**. This is a known coherence gap flagged in the v3 audit; treat Airtable Maintenance Tickets as a property-facing view and Linear as the maintenance-team's execution system.

---

## HubSpot

The leasing CRM. Deals thread the applicant lifecycle; associations link deals to contacts and companies; notes carry screening detail; tickets carry non-leasing service items (like fair-housing accommodation requests).

### Object types

| Type | Count | Role |
|---|---:|---|
| Deals | 103 | Leasing pipeline records; ~20 are legitimate Star PM applicant/tenant flows, the rest are noise |
| Contacts | 61 | Everyone in the universe (personas + NPCs) has a HubSpot contact |
| Companies | 7 | Property-owner LLCs and select vendor companies (Lone Star Capital Partners, Mesa Verde Investments, Rio Grande Holdings, A Plus Carpet Cleaning & Repairs, Sunshine Cleaning, Lone Star Maintenance Supply, Apartment Locator Central) |
| Tickets | 12 | Non-leasing service items (e.g., fair-housing accommodation cases) |
| Notes | 4 | Engagement notes and screening records attached to deals |

### Deal stages (leasing pipeline)

Applicant deals move through these stages in order:

`appointmentscheduled` → `presentationscheduled` → `qualifiedtobuy` → `decisionmakerboughtin` → `contractsent` → `closedwon` (or `closedlost` on decline / non-renewal)

### Associations

| Association | Coverage |
|---|---|
| Deal → Contact | 18 / 103 deals (all legitimate applicant/tenant flows have contact links; the ~85 noise deals do not) |
| Deal → Company | 103 / 103 |
| Contact → Company | 61 / 61 |
| Ticket → Contact | 12 / 12 |

### Signature applicant pipelines

| Applicant | Deals in pipeline | Referral source |
|---|---:|---|
| Priya Nambiar | 6 (appointmentscheduled → closedwon) | Jerome Okafor / Apartment Locator Central |
| Marcus Delgado | 5 (Las Palmas 2BR lifecycle) | Tasha Wentworth (referral partner) |
| Angela Carter | 3 (application → move-in) | Direct |
| Connor Beaumont | 2 (Mesa Vista renewal + non-renewal) | Existing tenant |
| Tommy Reyes | 2 (renewal appointmentscheduled → contractsent) | Existing tenant |

### Deal owners (leasing agents on the deal)

| Owner | Deals | Notes |
|---|---:|---|
| Sandra Allen | 14 | Owns the intake pipelines (Priya, Marcus Delgado, Angela Carter) |
| Kevin Okafor | 2 | Owns Connor Beaumont's Mesa Vista renewal + non-renewal |
| Alicia Vega (NPC) | 2 | Owns the Tommy Reyes standard-renewal scenario |
| Brooke Phillips | 85 | Catch-all owner for noise deals (mass email / HOA / fake-portfolio) |

---

## Linear

The maintenance ticket system of record. Linear is where every repair, PM cycle, and HVAC escalation lives.

### Projects (3)

| Project | Role |
|---|---|
| **Property Ops** (`proj_001`) | General property-operations issues that don't fit a specific initiative |
| **Summer Make-Ready Program** (`proj_002`) | Anchors the make-ready surge work |
| **Preventive Maintenance Push** (`proj_003`) | Anchors the HVAC / plumbing / electrical PM cycles |

### Issue counts

- 223 issues total across the three projects
- 44 comments across those issues
- Zero attachments and zero documents (attachment/document surfaces are empty in this universe)

### Team & workflow

- One Linear team; 61 users (every persona + NPC has a Linear user)
- 5 workflow states (open → in progress → in review → done → closed)

### Where Linear lives across scenarios

Linear is heavily used in:
- `maintenance_hvac_elias` (Elias creates cluster-level Linear issues + threads comments)
- `preventive_maintenance_push_routine` (Brooke opens PM issues; techs execute)
- `owner_capex_approval_roof` (the originating maintenance ticket that escalates to CapEx)
- `eviction_court_coordination` (a Linear issue tracks case prep — cross-domain use)
- `budget_review_makeready_q2` (a Linear issue tracks the budget reconciliation)

---

## QuickBooks

The heaviest surface in the universe. Cash cycles, vendor bills, tenant rent invoices, owner distributions.

### Object counts

| Object | Count |
|---|---:|
| Bills (vendor invoices Star PM pays) | 360 |
| Invoices (tenants pay Star PM, or Star PM bills owners) | 318 |
| Estimates | 334 |
| Credit memos | 296 |
| Payments | 129 |
| Vendors | 8 |
| Customers | 40 (mixed — owner LLCs, individual owners, tenants, some applicants/referral partners as intended noise) |
| Accounts | 7 |

### Vendor list

| Vendor | Type |
|---|---|
| Alamo HVAC Services | HVAC service and repairs |
| Hill Country Plumbing | Plumbing service and repairs |
| Lone Star Electric | Electrical service |
| Big Bend Restoration | Structural / restoration |
| Permian Make-Ready Crew | Make-ready labor |
| Lone Star Maintenance Supply | Parts and supplies |
| A Plus Carpet Cleaning & Repairs | Carpet cleaning, repair, replacement |
| Sunshine Cleaning | Move-out and turnover cleaning |

### Bill structure

A vendor bill (`Bill`) has:
- `DocNumber` (vendor's invoice reference)
- `TxnDate` (when the bill was issued)
- `DueDate` (when Star PM owes payment)
- `VendorRef` (name + id)
- `Line[]` (line items with `AccountBasedExpenseLineDetail.AccountRef` and descriptions)
- `PrivateNote` (internal note — often carries property attribution and approver context)
- `TotalAmt`, `Balance`

**Property attribution.** ~150 of 167 Airtable Make-Ready Turns name a property, but only ~11 of 360 QB bills name a property explicitly in a text field. Property attribution on bills sits in `PrivateNote` and `Line.Description` when present; many overhead bills legitimately don't reference a property.

### Invoice structure

An invoice (`Invoice`) has similar fields to a bill but flows the other direction (money owed **to** Star PM). Recipient types include:
- Property owners (invoiced for management fees or pass-through repair charges)
- Tenants (rent invoices)
- A small tail of intended-noise recipients (applicants, referral partners) — the universe carries these as noise on purpose

### Forward-looking obligations

At the 2026-07-01 anchor date:
- 166 bills have `DueDate` > 07-01 (unpaid, coming due)
- 144 invoices have `DueDate` > 07-01 (open A/R, coming due)

---

## Gmail

External and internal correspondence. 151 threads across 479 messages. Every message falls inside the 2026-05-01 → 2026-07-01 window.

### Common flows

- **Tenant maintenance report** → Onsite PM (Tommy Reyes / Tanya Mitchell → Carlos Mendez)
- **Vendor invoice submission** → Brooke Phillips (Gary Hoffman, Victor Rios)
- **Referral partner introduction** → Sandra Allen (Tasha Wentworth, Jerome Okafor)
- **Applicant document submission** → Sandra Allen (Priya Nambiar attaches pay stubs)
- **Owner report transmittal** → Robert Finley / Linda Castillo / David Shea / Harry Harris (from Brooke)
- **Court communication** → Patricia Lowe (from Patricia Nguyen, for evictions)
- **Rent notices** → Tenants (Patricia Nguyen sends late notices, payment plans, 3-day pay-or-quits)

### Attachments

Application documents (pay stubs, IDs, prior-residence letters) arrive as Gmail attachments in leasing threads. No separate filesystem — Gmail carries the document layer for the leasing lifecycle.

---

## Slack

8 channels aligned to workflows. Messages carry internal team coordination.

| Channel | ID | Volume | Primary use |
|---|---|---:|---|
| `#make-ready` | C004 | high | Unit turnover coordination |
| `#general` | C003 | high | Cross-cutting announcements, escalation broadcasts |
| `#maintenance` | C001 | high | Ticket dispatch, diagnostic threads |
| `#leasing` | C002 | medium | Leasing pipeline handoffs |
| `#applications` | C008 | medium | Applicant handoff and screening |
| `#owner-relations` | C006 | medium | Owner-facing coordination |
| `#budget-review` | C007 | medium | Budget variance discussion, invoice approval |
| `#vendors` | C005 | low | Vendor dispatch and coordination |

### Users

61 Slack users — every persona + NPC. Notable: Star PM staff use `@starpm.com` emails; tenants, applicants, and external vendors use gmail.com or vendor-specific domains.

---

## Google Calendar

121 events on the primary calendar. Events span 2026-05-01 → 2026-07-23, giving roughly 3 weeks of forward visibility from the anchor (2026-07-01).

### Event distribution vs anchor

| Bucket | Events |
|---|---:|
| Before 2026-07-01 | 112 |
| On 2026-07-01 | 1 |
| After 2026-07-01 | 8 |

### Event types

- Tour appointments (leasing pipeline)
- Vendor visits and walk-throughs (maintenance dispatch, A Plus Carpet, Alamo HVAC, Ridgeview roof follow-up)
- QC walk-throughs (make-ready sign-off — e.g., Mesa Vista 4C on 2026-07-15)
- Move-in walkthroughs
- Owner meetings (mid-year reviews, monthly reports, CapEx approval calls)
- Ops sync meetings (weekly Property Ops sync, Q3 planning)
- Statutory deadlines (rent-notice windows, court dates)
- Renewal appointments (Tommy Reyes on 2026-07-06)
- PM appointment blocks (preventive maintenance cycles)

---

## Contacts

61 contact records — every persona + NPC has an entry. Each contact has:
- `contact_id` (opaque hash)
- `first_name` / `last_name`
- `email`
- `job` (role description matching the persona/NPC role)
- `is_user` (boolean — whether they're a Star PM staff user or external)

Contacts is a directory service, not a workflow surface. Personas and NPCs reference it for looking up someone's email, role, or contact identity.

---

## Cross-service threading — how a typical workflow moves

**A make-ready turn:**
1. Onsite PM creates a Make-Ready Turn record in **Airtable**
2. Posts kickoff in **Slack** `#make-ready`
3. Emails vendors via **Gmail** to schedule work
4. Vendor visits appear on **Google Calendar**
5. Vendor invoices arrive via **Gmail**; Brooke approves in **QuickBooks**
6. Internal repairs may be tracked as **Linear** tickets
7. Jaime does QC and updates **Airtable** status to Approved
8. Onsite PM emails leasing team via **Gmail**; hands off in **Slack** `#leasing`

**A rent-collection lifecycle:**
1. Delinquency identified from **QuickBooks** rent invoice
2. **Airtable** Maintenance Ticket record opened for the delinquency
3. First notice email via **Gmail**
4. Follow-up event set on **Google Calendar**
5. Payment plan negotiated by **Gmail**; **QuickBooks** invoice updated
6. If plan fails: 3-day pay-or-quit **Gmail**; **Airtable** status updated
7. Eviction packet assembled from **QuickBooks** ledger + prior **Gmail** notices
8. Court filing coordinated with Patricia Lowe via **Gmail**; **Linear** issue tracks case prep

**A leasing application:**
1. Inbound inquiry / referral via **Gmail**
2. **HubSpot** contact created; deal opened
3. **Slack** `#applications` handoff
4. Airtable unit availability check
5. Tour scheduled on **Google Calendar**
6. Applicant emails documents as **Gmail** attachments
7. **HubSpot** notes carry screening detail; deal advances through stages
8. On approval: **QuickBooks** invoice for first month + deposit; **Airtable** unit status flipped to Leased

---

## What a "good" task-artifact anchor looks like

When authoring a Star PM task, verify these anchors against the live data before committing:

- **Property + unit** matches an entry in Airtable Make-Ready Turns (e.g., Las Palmas 8D, Mesa Vista 4C, Las Vistas 9D)
- **Tenant name** matches a Contacts record and shows up in relevant Airtable/QuickBooks rows
- **Vendor name** matches a QuickBooks vendor and has HubSpot company representation when applicable
- **Owner name** matches an NPC in the Property Owner role
- **Ticket ID** exists in Linear (`OPS-N`) or Airtable (`MT-2026-XXXX`)
- **Deal reference** exists as a HubSpot deal with the applicant contact associated
- **Any statutory date** (rent-notice window, 3-day pay-or-quit deadline) is consistent with the universe's 2026-05-01 → 2026-07-01 window
