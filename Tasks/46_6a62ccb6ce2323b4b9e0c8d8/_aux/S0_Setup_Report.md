# S0 Setup Report

**Task:** `Tasks/46_6a62ccb6ce2323b4b9e0c8d8`
**Phase:** S0 (setup only, no deliverables)
**Runbook:** `Reference/Sessions/S0.md`

## Universe

| | |
|---|---|
| Detected universe | `starpm` (Star Property Management, LLC) |
| Framework | V4 (dual-model verification: Opus 4.8 + Gemini) |
| Detection artifact | `_aux/Universe.txt` |
| Base path | `StarPM_Base_Universe/` |
| Tool catalog | `StarPM_Base_Universe/7_Server_Tools_Details.json` (prefix 7, not 8) |
| Services in this task | airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack (8 of 8) |

## Persona

| | |
|---|---|
| Name | Lisa Smith |
| Role | Onsite Property Manager |
| Persona id | `p_002`, email `lisa.smith@starpm.com` |
| Seniority | Mid, Department: Property Operations |
| Scripted footprint | 20 actions across 11 scenarios ("deeply rooted") |
| Signature scenarios | `fair_housing_reasonable_accommodation` (leads, 6 actions), `makeready_turn_lasvistas_9d` (2), `owner_capex_approval_roof` (2), `owner_monthly_report_review` |
| Brief source | `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` lines 13-34, copied verbatim to `PersonaBrief.txt` |

**Business function:** Property Operations (from `1_Business_Function.txt`).

**Alignment check:** the persona brief records Lisa's home Business Function as "1 · Property Operations", which matches the pasted business function exactly. No cross-function mismatch to resolve at S1.

## Per-task data

| | |
|---|---|
| Source | `3_UniverseDataForThisTask.json` (4,431,335 bytes) |
| sha256 | `06f7535a3357ae4900c884fbc76d5e3566f27bf1aef02e47ab6c7ccac8a749a3` |
| Records | **3,892 across 33 sources** |
| Split output | `_aux/Universe_Split/` (33 JSON files) |

Largest sources: `quickbooks.quickbooks_entities` 625, `slack.slack_messages` 580, `gcalendar.gcalendar_events` 565, `gmail.gmail_messages` 484, `hubspot.hubspot_associations` 388, `linear.linear_issues` 230, `hubspot.hubspot_objects` 187, `airtable.airtable_records` 170, `gmail.gmail_threads` 156. Full table in `_aux/Universe_Index/service_inventory.md`.

Airtable system of record (per `_aux/Universe_Index/graph_report.md`): `tblMakeReady` 120 records, `tblMaintenanceTickets` 50.

## Today and horizon

From `_aux/Universe_Index/today_horizon.json`:

| | |
|---|---|
| universe_today | **2026-07-01** |
| universe_timezone | America/Chicago |
| last_event_timestamp_seen | 2026-12-30T12:40:00-05:00 |
| records_dated_after_today | **59** |

**Flag (records_dated_after_today = 59).** Against a universe today of 2026-07-01, 59 records carry timestamps after today and the furthest runs to 2026-12-30, roughly six months past today. The index builder treats post-today records as legitimate when they are future-status or upcoming-due rows, and for this universe that reads as scheduled calendar events plus forward-dated due dates. Two consequences for downstream phases: any "complete" or "only open item" claim must sweep Calendar as well (hard rule 13, a confirmed future event is open work), and S1 must not use a relative-date phrase that resolves into the far-future band where the data thins out (Prompt Eval 2.8). The registry active window for this universe is 2026-05-01 to 2026-07-01.

## Artifacts produced

| Artifact | Result |
|---|---|
| `PersonaBrief.txt` | verbatim Lisa Smith section, source lines 13-34 inclusive, 22 lines |
| `_aux/Universe.txt` | `starpm` |
| `_aux/data_hash.txt` | sha256 above |
| `_aux/Universe_Split/` | 33 files, 3,892 records |
| `_aux/Universe_Index/service_inventory.md` | written |
| `_aux/Universe_Index/entities_personas.md` | written |
| `_aux/Universe_Index/key_facts.md` | written |
| `_aux/Universe_Index/today_horizon.json` | written |
| `_aux/Universe_Index/accounts_per_entity.md` | written |
| `_aux/Universe_Index/graph_report.md` | written |
| `_aux/Fact_Ledger.json` | written, counts below |
| `_aux/Feasible_Surface.json` | 15 tables with enums, 19 enum columns (see note 6: the Airtable source-of-record table is not among them) |
| `_aux/Validator_Reports/injection.md` | SKIP with recorded run (PASS is vacuous, see below) |

**Fact Ledger atom counts:** emails 206, amounts 403, dates 192, personas 61, and 7 id classes under `ids`: airtable_record 170, linear_issue 230, linear_comment 48, hubspot_object 183, slack_channel 8, slack_user 61, invoice 504. `entities` 0 and `fiscal_periods` 0 are correct rather than merely tolerated: `build_fact_ledger.py:189` fills `entities` only from a Brookfield-only `entity_id` field, and `accounts_by_entity` / `fiscal_periods` fill only on `ogl_accounts` / `ogl_fiscal_periods` (lines 192-212), none of which exist in StarPM. Note 5 below covers id classes that are absent and arguably should not be.

## V4 injection gate

`9_Universe_inject.sql` is present (4,065 bytes) but carries **0 executable statements**; it is still the comment-only scaffold header written by `PIPELINE NEW`. `4_Changelog.json` is `[]`. Per hard rule 4 a comment-only header SKIPs the injection gate. `validate.py --phase injection` was run anyway, on the principle that recording a result beats asserting one, and returned PASS with 0 fails, 0 warns and 4 notes deferring the semantic Eval0 checks (P4 fact contradiction, P5 register match, P6 chain depth, P8 difficulty composite) to council.

**That PASS is vacuous and must not be read as validation.** There are no statements in the file to evaluate, so the gate certifies nothing about injection quality; it is recorded here as SKIP-with-recorded-run.

If HARDNESS or S1 decides to inject scenario data, the gate must be re-run against the populated SQL and must clear before levers are built on top of it.

## Notes carried forward to HARDNESS

1. **`p_002` is an authoring-side id and does not appear anywhere in the per-task split.** Lisa resolves through service-native identifiers instead: Slack user `U6480117503`, email `lisa.smith@starpm.com`, present in `slack.slack_users`, `contacts.contacts` and `airtable.airtable_users`. Ground prompts, oracle events and rubrics on the email or the service id, never on `p_002`.
2. **Lisa ranks 11th of 30 by raw artifact density (73 mentions)** while the top of the map is Tony Reyes 862, Brooke Phillips 740, Wesley Tran 641, Isela Juarez 591, Carlos Mendez 525. Her brief calls her deeply rooted on scripted-action count (20 across 11 scenarios), which is a different measure from ambient mention volume. HARDNESS should anchor levers on her four signature scenarios rather than assume a dense ambient surface around her name.
3. **Her Slack record carries `timezone: America/Los_Angeles`** while the universe timezone is America/Chicago and her brief lists active hours 7 AM to 5 PM. Recorded as an observation, not yet classified. It is a candidate lever only if the rest of the data corroborates it; otherwise treat it as data noise and do not build a timing lever on a single field.
4. **Registry landmines to check before lever selection:** near-duplicate decoy files (`invoice-2026-419.pdf` vs `invoice-2026-419-287.pdf` and siblings), the Tanya Mitchell accommodation-versus-eviction contradiction (Tanya appears in this task's data at 28 mentions), and the cross-property "Unit 14" ambiguity. Lisa leads the fair-housing accommodation scenario, so the Tanya Mitchell contradiction sits directly inside her signature surface.
5. **The Fact Ledger has no Calendar, Gmail or QuickBooks id atoms, and Calendar is the one service hard rule 13 names.** `STARPM_ID_PATTERNS` (`build_fact_ledger.py:69-76`) defines six id classes plus field-extracted `invoice`; there is no class for gcalendar events, gmail messages or threads, or quickbooks entities, leaving 565 / 484 / 156 / 625 records respectively with zero id atoms. The builder's stated rationale (lines 67-68) is that bare-hex gmail and contact ids over-collect, which is reasonable, but gcalendar event ids are not bare hex: a real row carries `id` = `whd6zys0hw7zbsh11m9vqv4m4i-b6a1e41c`. Since `Reference/Sessions/S0.md:78` designates the Fact Ledger as the authoritative atom surface for groundedness, and rule 13 requires sweeping every service **including Calendar** before any "complete" or "only open item" claim, S1 and S2 must ground Calendar and Gmail citations directly against `_aux/Universe_Split/gcalendar.gcalendar_events.json` and `gmail.gmail_messages.json` rather than assuming the ledger covers them.
6. **`Feasible_Surface.json` does not contain `airtable.airtable_records`,** which is the 170-row make-ready and maintenance surface (tblMakeReady 120 + tblMaintenanceTickets 50) and StarPM's source of record. Only the Airtable metadata tables (`airtable_fields`, `airtable_pages`, `airtable_views`) made it in. **Exactly one cause, and it is not the hint vocabulary:** `build_feasible_surface.py:73` iterates only top-level `row_data` keys and never descends into `fields`, where StarPM nests its enums. The matcher at line 76 is a substring test and `ENUM_COLUMN_HINTS` leads with `status`, so `fldTurnStatus` (lowercased `fldturnstatus`) **does** match, and that is the field holding `selProg`=56, `selSched`=43, `selReady`=21, corroborated at `_aux/Universe_Index/key_facts.md:15`. **Descending into `fields` alone recovers the make-ready enum with no change to the hint list.** Because `S0.md:90` makes this file the validator's rubric-enum cross-reference at S3, **S3 must check make-ready enum values against `key_facts.md` and the split directly**, or a rubric asserting a wrong status will pass unflagged. That `linear.linear_workflow_states` was captured correctly is evidence for the single-cause reading: its `type` sits at top level, so hint matching demonstrably works and nesting is the whole problem.
7. **`Fact_Ledger.lifecycle.today` is `null`** because `build_fact_ledger.py:314` reads `th.get("today")` while `build_universe_index.py:310` writes the key as `universe_today`. Inert here (StarPM has no fiscal periods, and `today_horizon.json` itself is correct at 2026-07-01), so nothing downstream is affected, but the ledger's whole lifecycle block is dead rather than merely empty. Recorded, not patched: fixing it means editing pipeline code mid-phase. Latent defect for any universe that does carry fiscal periods.

## Exit criteria

- [x] `PersonaBrief.txt` exists and is non-empty
- [x] `_aux/Universe_Split/` contains the per-service JSON files (33)
- [x] `_aux/Universe_Index/` contains all 5 summary files (plus `graph_report.md`)
- [x] `_aux/S0_Setup_Report.md` written (this file)
- [x] `_aux/Verification_s0.md` written (v16 cross-source gate)
- [x] V4 injection gate run and non-blocking (SKIP; the PASS is vacuous on an empty inject file)

**Next trigger:** `PIPELINE HARDNESS — Tasks/46_6a62ccb6ce2323b4b9e0c8d8` in a fresh chat.
