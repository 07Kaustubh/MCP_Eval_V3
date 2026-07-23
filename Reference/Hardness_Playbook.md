# Hardness Playbook — Stumping Opus 4.8

The single biggest lever for QC pass rates is **hardness without contrivance**. Opus 4.8 is the model under test. The patterns below are the ones that empirically defeat it on Brookfield tasks. Each lever maps to a hard-tip observation in `Docs/4_Prompt_Hard_Tips.md`. **No universe edits** in this pipeline — every lever must be found in the per-task `_aux/Universe_Split/` before being engineered into the prompt.

## Opus 4.8 failure modes (the levers)

| # | Lever | Failure mode it triggers | Hard-tip source | Tool-call cost |
|---|---|---|---|---:|
| 1 | **Latching** | Same incident in 2+ services with different counts/scope; the more-findable source is incomplete. Agent reports the first framing. | "Agents latch onto the first framing they encounter" | 5-8 |
| 2 | **Structured-DB skip** | Load-bearing fact lives only in Oracle GL / SAP / BlackLine / Records Vault / Airtable / Linear, not mirrored in email or Slack. Agent reads secondhand chatter and stops. | "Agents skip structured databases" | 4-7 |
| 3 | **Missing reply** | A dispute / question has a buried reply that flips the conclusion. Agent finds the dispute, reports it, never searches for the response. | "Agents don't search for responses to things they find" | 3-5 |
| 4 | **Search-result-cap eviction** | The load-bearing message is buried under high-traffic keywords or in an older thread. It gets pushed out of the top results. | "Data past search result limits is invisible" | 3-5 |
| 5 | **Thread-reply blindness** | The resolution sits in a Slack thread reply, not the top-level message. Agent reads the question, never the answer. | "Slack thread replies are also hard for agents to find" | 2-4 |
| 6 | **Near-miss entity confusion** | Two similar IDs / names / account numbers plausibly confused (`105000` differs per entity; two Noahs; two vendors with the same prefix). | Hard tips + universe account-trap rule | 3-5 |
| 7 | **Multi-write diversification** | Most agents default to one email. 3+ writes across 3+ services (Records Vault upload, Linear comment, Airtable update, Slack post, reminder) forces breadth. | "Diversify your write actions" | 9-12 |
| 8 | **Multi-link chain** | A→B→C where A is easy (Slack mention), B requires a follow-up search (vendor reply, SAP credit memo), C is the actual disposition. | "Three-link chains are harder" | 6-9 |
| 9 | **Universe-grounded gotcha** | Force a check that punishes assumed knowledge (account-role per entity, retention code that doesn't exist, unused `public` classification, open period past lock target, exception in `awaiting_approval` past SLA). | Universe summary anti-patterns | 3-5 |
| 10 | **Reversal / supersession** | A JE has `status="reversed"` and a `reverses_entry_id` partner; an SOW / W-9 / engagement letter has been superseded. Agent uses the gross figure or the old reference. | Task 11 / 12 worked examples | 4-6 |
| 11 | **Net-vs-gross framing** | An aggregate of "wire activity" or "AP spend" depends on which adjustments to apply. Agent uses the gross. | Task 11 worked example | 4-7 |

## Tool-call density projection (HARD GATE)

`PIPELINE HARDNESS` MUST project tool-call density before greenlighting S1. The projection sums:

**Density formula version:** `density_formula_version: 2` (recalibrated 2026-07-23 for StarPM realities — see the StarPM lever-cost recalibration subsection at the end of this file). `[PROJECT POLICY — cites §4.9 spec floor 15; project internal target 40+]` The 50+ midpoint design target and the density formula that produces it sit above the §4.9 (Trajectory → Tool Call Count) spec floor of avg ≥ 15 tool calls; recalibration adjusts coefficients only and does not modify §4.9.

| Component | Tool-call cost |
|---|---:|
| Base discovery (contact lookups, channel resolution, period lookup) | 5-8 |
| Sum of selected levers (from the table above) | ~ sum of ranges |
| Write actions (target 3+ writes × ~3 supporting reads each) | 9-12 |
| Cross-service triangulation buffer | 5-8 |

**Design target: average projected tool-call count must be ≥ 50 to greenlight S1 cleanly.** Three bands: midpoint ≥ 50 = PASS; midpoint 40-49 = `THIN_DENSITY` (operator can continue with per-task justification but task is at risk of underflow on real platform runs); midpoint < 40 = `INSUFFICIENT_DENSITY` (STOP — must add levers, expand write-action mix, or both). The 50+ midpoint design target produces ~40+ tool calls in real platform runs, which is the empirical floor below which tasks come back failing density.

## Composition rules

- **4-to-5 levers per task is the design default.** 3 is acceptable only if the chosen 3 include high-cost levers (L7 multi-write 9-12, L8 multi-link 6-9, L11 net-vs-gross 4-7 — sum 19-28) AND the operator documents in `Hardness_Plan.md` why expanding wasn't possible (universe constraint). To hit the 50+ midpoint design target consistently, default to 4-5 levers — 3 levers will frequently land in the THIN band (40-49) or below.
- **Levers must be discoverable, not buried.** Difficulty comes from connecting evidence, not hiding it. The first link of every chain must be findable through a normal broad search.
- **Each lever must be grounded in this task's `_aux/Universe_Split/`.** If a lever doesn't have backing data, drop it.
- **Stack with discipline.** Pair structured-DB-skip with multi-write so the agent has to query the source AND act on it. Pair missing-reply with latching so the agent has to override its first read.
- **3+ writes across 3+ services minimum.** Mix of: email, Slack channel post, Linear comment / update, Records Vault upload, Airtable update, reminder, calendar event, JE lifecycle, AP invoice approval / void, reconciliation lifecycle.

## Stump Hypothesis output (what HARDNESS phase emits)

Per task, HARDNESS produces `_aux/Hardness_Plan.md` containing:

1. **Levers Available** — which of the 11 the per-task data supports, with a one-line evidence pointer per lever (`<file>:<row_id>` or `<file>:<index>`).
2. **Selected Levers** — the 3 to 5 chosen, with rationale + projected tool-call cost per lever.
3. **Tool-Call Density Projection** — sum of base discovery + selected lever costs + write-action cost + buffer. PASS at ≥ 50 (design target), THIN_DENSITY at 40-49 (continue with per-task justification), INSUFFICIENT_DENSITY at < 40 (STOP).
4. **Stump Hypothesis** — the 2 to 4 specific rubric outcomes most likely to fail across the 6 Opus runs, with confidence (high / med / low) and reasoning citing the levers.
5. **Hardness Score** — `selected / 5`. If fewer than 3 levers are available, output `INSUFFICIENT_LEVERS`.
6. **Hardness Brief for the Prompt Writer** — a tight paragraph the S1 runbook hands directly to the prompt-drafting sub-agent.

## What hardness is NOT

- Not arbitrary precision ("the email at 3:47 PM"). That is contrived difficulty, fails the QC `Contrived / Unnatural Prompts` dimension.
- Not over-stacking unrelated asks. That fails Coherence.
- Not pre-solving the puzzle in the prompt. That fails Investigation.
- Not naming tools or IDs the agent is supposed to discover. That fails Explicit Tool Mention.

---

## Persona-attribution landmine (rubric-authoring and AUDIT failure pattern)

**Pattern:** When a scenario contains multiple departed-employee narratives or multiple persons associated with similar workstreams, rubric authors, AUDIT reviewers, and agents all default-attach the most salient name to a workstream even when a less-salient person is the correct attribution. The salient name typically has a richer backstory (resignation letter, solicitation, conflict); the correct name belongs to a quieter, single-thread narrative.

**Detection signal:** Universe CRM chains or email threads that use generic pronoun-labels ("Former employee post-term access under review", "Former LO account review") without naming the specific person. When the named-person field is absent in the workstream's primary service record, rubric authors fill it from memory, defaulting to the salient name.

**Why this persists through the pipeline:** S3 grounding verifies atom existence (does this CRM engagement body match?) but not attribution (does the named person appear IN the communications for this workstream?). AUDIT reads "correct role" through cognitive salience without grepping the Slack thread that names someone else. FINAL answer-leakage scan checks prompt-vs-rubric leakage, not rubric-vs-universe factual grounding.

**Canonical example — Task 35 (Keystone):** Rubrics R10/R13/R18 attributed the 04-14 post-termination LOS access workstream to Marcus Webb. The universe Slack thread at 04-14 12:22/12:28/12:50/13:22 explicitly names Evan Mercer ("Evan Mercer LOS access disabled") — a single-thread, low-salience departure. Marcus Webb had a high-salience story (resignation + solicitation + spouse-agent conflict) but `mortgage_los.staff` showed `termination_date: None, is_active: True` on 04-14. All 6 platform agent runs replicated the wrong attribution. The defect was caught only at S4 via universe deep-query. See `Tasks/_meta/Pipeline_Improvement_Notes.md` (2026-07-01 entry) for the full root-cause analysis.

**Pipeline countermeasures added 2026-07-01:**
- **S3 grounding (O1):** Persona-attribution co-occurrence check — person name must co-occur with workstream keywords in at least one universe communication before the grounding sub-agent marks the attribution as verified.
- **S3 adversarial council (O4):** Entity-swap check — for every person-named rubric, ask whether a different person in the universe could plausibly be attributed to the same workstream. If yes and both persons appear in adjacent universe atoms, the attribution is ambiguous and must be anchored explicitly.
- **AUDIT KS-9 (O2):** Persona-attribution reverse-groundedness — for every named person in every rubric, confirm at least one universe communication co-occurring their name with the rubric's workstream keywords. Zero co-occurrence = Major.
- **FINAL named-entity reverse-groundedness (O3):** Enumerate all unique person names across rubric titles/evidences; for each, confirm at least one universe atom grounds the attribution to the assigned workstream.

---

## StarPM Adaptation (V4 — ML-confirmed July 2026)

The 11-lever catalog above was built on Brookfield tasks. All 11 levers apply to StarPM tasks with the substitutions below. Read this section whenever `_aux/Universe.txt` = `starpm`.

### Service substitutions

Wherever the Brookfield lever catalog names a Brookfield-specific service, substitute the StarPM equivalent:

| Brookfield service | StarPM equivalent | Notes |
|---|---|---|
| oracle_gl / SAP subledger | QuickBooks | Primary accounting surface |
| BlackLine reconciliations | Airtable (Make-Ready Turns, Stipends) | Operational SSOT for unit state |
| Records Vault | Gmail / HubSpot note attachments | No standalone vault; docs surface via email/CRM |
| Linear (issues) | Linear (maintenance tickets MT-YYYY-NNNN) | Same service, different ticket taxonomy |
| Email | Gmail (`gmail_create_draft` — NO send action) | Gmail only drafts; send is not available |
| Slack | Slack (8 channels C001-C008) | Same service |
| Contacts | Contacts | Same service |
| Calendar | GCalendar | Same service |

### Write-action mix for StarPM (target 3+ writes across 3+ services)

Standard StarPM write-action menu (use 3-5 from this list per task):

| Write action | Service | Tool hint |
|---|---|---|
| Draft email to tenant / vendor / owner | Gmail | `gmail_create_draft` |
| Post to Slack channel | Slack | channel must be C001-C008 |
| Create / update Linear maintenance ticket | Linear | `linear_create_issue` / `linear_update_issue` |
| Update Airtable Make-Ready record | Airtable | `airtable_update_records` |
| Create / update QuickBooks bill or payment | QuickBooks | `quickbooks_create_bill` |
| Create / update HubSpot deal or note | HubSpot | `hubspot_create_deal` / note endpoint |
| Schedule GCalendar event (inspection, walkthrough) | GCalendar | `gcalendar_create_event` |

### L12 — Document cross-reference (StarPM-specific lever)

**Failure mode:** A lease agreement, vendor invoice, or maintenance report in `StarPM_Base_Universe/Data/Files/` is the authoritative source for a key fact (charge amount, lease clause, inspection finding). The live service record (QuickBooks bill, Airtable status, Linear ticket) shows a different or incomplete value. Opus 4.8 trusts the live database field and skips reading the attached document.

**How to engineer it:** Prompt references a specific document by natural context ("per the lease signed last month", "check the original invoice", "the QC inspection report"). Agent must trace the document reference through the service that holds the attachment (Gmail thread attachment, HubSpot note attachment, or Airtable attachment field) and read the PDF content. The stumping fact is only in the document, not mirrored in the live service record.

**Tool-call cost:** 2-4 (find the email/record that references the doc + read attachment + cross-reference against live data + flag or act on the discrepancy). `[PROJECT POLICY — cites §4.9 spec floor 15; project internal target 40+]` Recalibrated from 4-8 to 2-4 under `density_formula_version: 2` because the attachment surfaces through a single service-tool call on StarPM (Gmail thread / HubSpot note / Airtable field), one call shorter than the initial estimate; cross-service requirement still holds at ≥ 2 service touches per §4.1 (Prompt → Tool use and Cross-service requirement).

**Composition rule:** Pair L12 with L1 (Latching) — the live service record is the more-findable source and will latch the agent. Pair with L8 (Multi-link chain) — document reference is the second link (A = live record shows X → B = attached PDF shows Y → C = agent must act on the discrepancy).

**Read-only constraint (hard):** Prompts using L12 MUST NOT ask the agent to modify, upload, or replace the PDF. The Files/ directory is read-only. The agent reads the document and acts on what it finds (email the finding, update a Linear ticket, flag the discrepancy to the owner) — it never writes back to the file.

### StarPM lever-cost recalibration (`density_formula_version: 2`)

`[PROJECT POLICY — cites §4.9 spec floor 15; project internal target 40+]` The base 11-lever cost ranges above assume Brookfield tool surfaces (email send with get-thread reply loop, Records Vault upload with metadata retrieval roundtrip); StarPM tool surfaces are leaner, so the coefficient adjustments below preserve the density formula's truthfulness on StarPM realities without changing any QC spec rule, and the §4.9 spec floor of avg ≥ 15 tool calls is unchanged.

| Adjustment | Brookfield baseline | StarPM recalibrated | Spec / policy tag |
|---|---:|---:|---|
| Gmail write cost per action | send + reply-loop follow-up ≈ 2 calls | `gmail_create_draft` = 1 call (no send tool exists in StarPM) | `[PROJECT POLICY — cites §4.9]` The draft-only surface reduces write cost by ~1 call per Gmail write, and the write still counts as a service touch under §4.1 (Prompt → Tool use and Cross-service requirement). |
| Document / attachment retrieval | Records Vault upload + metadata roundtrip ≈ 2 calls | Gmail thread / HubSpot note / Airtable attachment field = 1 call | `[PROJECT POLICY — cites §4.9]` StarPM has no Records Vault; the doc surfaces through a service tool that already returns the attachment, and cross-service coherence between attachment and live data is preserved under §4.7 (Universe → Cross-service Coherence). |
| Slack write cost per action | `slack_send_message` = 1 call | `slack_send_message` = 1 call (sends) OR `slack_send_message_draft` = 1 call (drafts only, does NOT send) | `[PROJECT POLICY — cites §4.9]` HARDNESS density projection assumes send unless the prompt scope calls for a draft, and a rubric requiring a send fails if the agent uses the draft tool, so tight-identifier truthfulness under §4.5 (Prompt → Truthfulness) requires the tool the prompt implies to match the tool the rubric grades. |
| L12 Document cross-reference | not applicable (Brookfield lever set stops at L11) | 2-4 calls (down from initial draft of 4-8) | `[PROJECT POLICY — cites §4.9]` Attachment surfaces through 1 service-tool call plus 1 live-record cross-reference call plus 1 flag/act call, and the cross-service requirement still holds at ≥ 2 service touches under §4.1. |

**Composition-rule impact:** the base `Write actions (target 3+ writes × ~3 supporting reads each) | 9-12` row still applies to StarPM as an upper band, and recalibration confirms no supporting-read multiplier needs raising on StarPM to keep the 50+ midpoint design target achievable per §4.9 (Trajectory → Tool Call Count) — 3+ writes forces ≥ 3 service touches under §4.1 (Prompt → Tool use and Cross-service requirement) and the resulting midpoint remains above the §4.9 spec floor.
