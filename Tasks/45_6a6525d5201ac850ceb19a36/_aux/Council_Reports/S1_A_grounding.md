# Council A — Grounding & Convention — S1 PROMPT Review

**Task:** `45_6a6525d5201ac850ceb19a36` · **Universe:** starpm (V4) · **Today:** 2026-07-01 America/Chicago
**Deliverable under review:** `5_Prompt.txt` (276 words) · **Mode:** read-only
**Correct answer per Hardness Plan:** KICK-BACK / HOLD (current turn `recbd087a4abd605b` = selProg, deep-clean + interior-repaint still tracking, target 6/30 blown, vendor bills unpaid, 7/15 re-inspection pending).

## VERDICT: BLOCK

One blocking grounding contradiction (A3 + A6, same root): the prompt says the 7/15 re-inspection is on Jaime's ("my") calendar; the universe shows it is NOT on Jaime's calendar. Every other perspective (A1 grounding, A2 convention, A4 action, A7 single-target, A10 business function, A11 solvability) is GO-clean. Fix is low-cost (see Required Fix).

---

## A1 Grounding — VALUE -> FILE:RECORD

All citations are under `_aux/Universe_Split/`.

| Prompt value | FILE : RECORD | Result |
|---|---|---|
| Carlos Mendez (Onsite PM) | `contacts`/index `carlos.mendez@starpm.com` (persona, Onsite Property Manager); `gcalendar` organizer of all 4C events; `slack` C004 "Turn is officially kicked off for Mesa Vista 4C" | FOUND |
| Brooke Phillips (would list/market) | index `brooke.phillips@starpm.com` (persona, Apartment Property Supervisor); `airtable` `reca424761ae15355` "Brooke Phillips has been notified to move forward with listing"; `slack` C004 Carlos "4C is market-ready, Brooke... good to list" | FOUND |
| Jaime Salinas (actor / QC) | index `jaime.salinas@starpm.com` (persona `p_007`, Quality Control Inspector) | FOUND |
| Mesa Vista 4C | `airtable.airtable_records` `recbd087a4abd605b` (tblMakeReady, current) + `recc8534b3fd13954` (tblMakeReady, prior) + `reca424761ae15355` (tblMaintenanceTickets); `gcalendar` 3 event types; `quickbooks` bills | FOUND (exactly 3 Airtable rows) |
| deep-clean scope | `airtable` `recbd087` fldNotes2 "Deep clean ... still tracking"; `gcalendar` "Sunshine Cleaning Deep Clean - Mesa Vista 4C"; `quickbooks` bill `195089456477` | FOUND |
| interior-repaint scope | `airtable` `recbd087` fldNotes2 "interior repaint still tracking"; `gcalendar` "Interior Repaint - Mesa Vista 4C"; `quickbooks` bill `696089964235` | FOUND |
| mid-June move-out (~6/15) | `airtable` `recbd087` fldMoveOut **2026-06-15** | FOUND |
| end-of-June target (~6/30) | `airtable` `recbd087` fldTargetReady **2026-06-30** | FOUND |
| mid-July re-inspection (~7/15) | `gcalendar` "Make-Ready QC Inspection - Mesa Vista 4C" **2026-07-15T10:00**, status confirmed | FOUND (ownership problem — see A3/A6) |
| "wrapped / list it" framing | `slack` C004 Carlos "4C is market-ready ... good to list"; `airtable` `reca424` "market-ready ... Brooke notified to move forward with listing" | FOUND |
| unpaid vendor bills | `quickbooks` `195089456477` (deep clean $387, Balance 387, due 5/31) + `696089964235` (repaint $1,340, Balance 1,340, due 5/31) | FOUND |

Targeted sub-checks:
- **(a) Carlos = Onsite PM tied to 4C turn** — YES. Organizer of every 4C calendar event; `slack` C004 "Turn is officially kicked off for Mesa Vista 4C, tagging Brooke Phillips."
- **(b) Brooke = supervisor who lists/markets** — YES. `airtable reca424` names her for listing; Carlos tags her in C004.
- **(c) recbd087 move-out 6/15, target 6/30, notes "still tracking"** — YES, all three exact (`fldMoveOut 2026-06-15`, `fldTargetReady 2026-06-30`, fldNotes2 "Deep clean and interior repaint still tracking on their respective schedules. Will update status to Ready once all vendor and in-house scopes are signed off").
- **(d) 7/15 4C QC re-inspection exists + ONLY future 4C event** — YES to both. All other 4C calendar events are 2026-05-21 (past). The 7/15 event is the sole future (>= 2026-07-01) 4C event. **Caveat:** it is not on Jaime's calendar (A3/A6).
- **(e) unpaid QB vendor bills for 4C deep-clean/repaint exist** — YES. Both scope bills carry full outstanding balances and are past due.

**A1 result: PASS** — zero NOT FOUND on any core claim.

---

## A2 Convention

| Check | Result |
|---|---|
| 500-word cap | PASS — **276 words** |
| No em/en/figure dash | PASS — byte scan for U+2014/2013/2012/2015/2212 = 0 hits |
| No tool/function names | PASS — regex scan (save_issue, create_draft, list_events, slack_send, manage_crm...) = 0 |
| No MCP-server names | PASS — no airtable/linear/slack/gmail/gcalendar/quickbooks/hubspot tokens; prompt uses "issue tracker", "make-ready channel", "email", "put it on record", "vendor side" |
| No internal IDs | PASS — no rec.../tbl.../C0.../sel.../MR-4C/fld tokens |
| First-person natural voice | PASS — Jaime throughout ("I am not signing off", "my own pass", "I can call this one done") |
| One coherent situation (sentence-removal) | PASS — every sentence advances the single 4C QC scenario |
| Trigger -> Context -> Asks | PASS — line 1 Trigger, line 3 Context, line 5 Asks |
| 3+ writes across 3+ services | PASS — 4-5 writes / 4 services: set QC status (airtable) + open ticket (linear) + channel post (slack) + email Carlos (gmail draft) + notify Brooke |
| No pre-solving | PASS — neutral sign-off-OR-kick-back; states Jaime's "closed" standard but never asserts the answer/state |

Note: the `#XX|` prefixes visible in file reads are harness per-line annotations, not file bytes (JSON parsed cleanly; word/dash/token scans ran on raw bytes). Prompt file is well-formed.

**A2 result: PASS** — zero convention drift.

---

## A3 Narrative-State — STATE CLAIM -> RECORD (CONSISTENT / CONTRADICTING)

- "Carlos has Mesa Vista 4C down as wrapped ... wants it released for listing" -> `slack` C004 Carlos "4C is market-ready ... good to list" + `airtable reca424`. **CONSISTENT**
- "Brooke is ready to put it on the market on his word" -> `airtable reca424` "Brooke ... notified to move forward with listing"; C004 Carlos tags Brooke. **CONSISTENT**
- "moved out in the middle of June" -> `airtable recbd087` fldMoveOut 2026-06-15. **CONSISTENT**
- "target-ready date at the end of the month, which has already come and gone" -> `recbd087` fldTargetReady 2026-06-30; today 2026-07-01 > 6/30 (past-due). **CONSISTENT**
- "the deep clean and the interior repaint ... genuinely closed ... or still tracking" -> `recbd087` fldNotes2 "still tracking". **CONSISTENT**
- "finished with the bill still sitting unpaid, does not count as closed" -> `quickbooks` unpaid deep-clean ($387) + repaint ($1,340). **CONSISTENT**
- **"a re-inspection sitting on my calendar for the middle of this month"** -> `gcalendar` "Make-Ready QC Inspection - Mesa Vista 4C" 2026-07-15 exists on calendar_id **carlos.mendez / wesley.tran / brooke.phillips** only; attendees = Carlos, Brooke, Wesley; **Jaime is not attendee/creator/organizer**. Jaime's own calendar (calendar_id `jaime.salinas@starpm.com`, which does exist) holds only the two **past** 4C events (Deep Clean 5/21, Interior Repaint 5/21), NOT the 7/15 re-inspection. **CONTRADICTING** — the possessive "my calendar" is false.

Required (i)/(ii)/(iii):
- (i) universe supports Carlos reporting/believing 4C wrapped — YES (C004 + `reca424`). CONSISTENT.
- (ii) 6/30 target genuinely past-due as of 7/1 — YES. CONSISTENT.
- (iii) 7/15 re-inspection genuine confirmed future event — YES the event is genuine/confirmed/future; but its ownership contradicts the "my" possessive.

**A3 result: BLOCK** — one narrative-state contradiction ("my calendar").

---

## A4 Action-vs-Universe

Prompt framing is a NEUTRAL QC verification (run my own pass; sign off if ready, hold if not). The only record prescribing a competing action is the DECOY maintenance ticket `reca424` ("market-ready ... move forward with listing") and prior selReady `recc8534` — both contradicted by the authoritative SoR `recbd087` (tblMakeReady, selProg, "still tracking") + unpaid bills + pending 7/15 re-inspection. The universe genuinely makes "not ready / hold" the correct outcome, so the divergence from the decoys is the intended latching bait, not an unexplained divergence. Jaime (QC Inspector) has sign-off/kick-back authority (`PersonaBrief`: "signs off on marketing-ready status or kicks work back").

**A4 result: PASS** — no ACTION_DIVERGENCE, no AUTHORITY_GAP.

---

## A6 Persona Scope

Mesa Vista 4C QC IS within Jaime's scope: `PersonaBrief` lists her in scenario `makeready_turn_carlos` (this turn) as the QC anchor, with core systems Airtable (Make-Ready QC status) / Slack `#make-ready` / Linear (QC issues) / Gmail (Onsite-PM notifications) — exactly the prompt's write surfaces. "my own pass" / "I can call this one done" are in scope.

**Exception — SCOPE_DRIFT:** "a re-inspection sitting on **my** calendar" — the 7/15 QC re-inspection is NOT on Jaime's calendar (only Carlos/Brooke/Wesley), and gcalendar is not even in Jaime's core system footprint (Carlos organizes the 4C events). The one 4C event the QC Inspector would own is the one event the universe did not put on her calendar or invite list.

**A6 result: BLOCK** — persona-scope drift on the calendar claim (same root as A3).

---

## A7 Clarity & Specificity — single-target uniqueness (rule 13 / F7)

"Mesa Vista 4C ... its June turn ... moved out in the middle of June with a target-ready date at the end of the month" resolves to exactly ONE record:

| Candidate | move-out / target | Matches "mid-June move-out + end-of-month target"? |
|---|---|---|
| `recbd087` (selProg, current) | 6/15 / 6/30 | YES — unique match |
| `recc8534` (selReady, prior) | 6/01 / 6/14 | NO — 6/01 is start not middle; 6/14 is mid not end |
| `reca424` (maint ticket) | none / none | NO — no move-out/target dates |

The date content uniquely pins `recbd087`. The prior turn is excluded by content. A "latest-created record" heuristic would wrongly grab `recc8534` (created 5/29 > `recbd087` 5/22) — but that is the intended Opus-selective supersession trap, and the prompt's explicit dates resolve the ambiguity correctly. The 7/15 re-inspection reference further pins the current turn (the prior turn is closed). No second reading changes the write-action set.

**A7 result: PASS** — single target uniquely identified; no MAJOR clarity gap; no CLARITY_GAP BLOCK.

---

## A10 Business Function

- Assigned (`1_Business_Function.txt`): **Quality Control & Field Services**.
- Prompt primary: QC sign-off / kick-back on a make-ready turn.
- **match = TRUE.**

Minor label note (non-issue): this council prompt calls it "category 5"; `PersonaBrief` and `3_StarPM_TASK CATEGORIES.md` number QC as "Cat 3" (C004 #make-ready = Cat 1 turnover + Cat 3 QC). The function NAME matches exactly; the number is a labeling quirk in the council prompt, not a prompt defect.

**A10 result: PASS.**

---

## A11 Solvability (Hardness_Plan trajectory walk)

| Step | Required row | Materialized? |
|---|---|---|
| Find 4C current turn | `airtable recbd087` (selProg) | YES |
| Read selProg + notes | fldNotes2 "still tracking" | YES |
| Find "done" maint ticket | `airtable reca424` (MR-4C-2026-08) | YES |
| Find prior completed turn | `airtable recc8534` (selReady) | YES |
| QB vendor bills for 4C | `195089456477` ($387 unpaid) + `696089964235` ($1,340 unpaid) | YES |
| 7/15 calendar event | `gcalendar` 2026-07-15 QC inspection | YES (on Carlos/Brooke/Wesley) |
| Resolve Carlos + Brooke | personas exist (`@starpm.com`) | YES |
| Write targets | Airtable `recbd087` update · Slack C004 `#make-ready` · Linear team Operations (OPS) / project "Summer Make-Ready Program" · Gmail draft to Carlos | YES (all 4) |

The core kick-back decision is fully solvable from the Airtable SoR (`recbd087` selProg / "still tracking") + the two unpaid bills, independent of the calendar event, so there is **no hard SOLVABILITY_BREAK**. Caveat folded into A3/A6: because the 7/15 event is not on Jaime's calendar and `list_events` defaults to the current user's calendar, an agent following the literal "my calendar" pointer returns only the two PAST 4C events and misses the re-inspection unless it cross-searches other calendars (`list_calendars` + per-calendar `list_events`, or `fullText` across calendars). This can undercut lever L9 and/or misdirect the agent.

**A11 result: PASS (with caveat).**

---

## Blocking Findings

1. **[A3 + A6] "on my calendar" contradiction (BLOCK).** Prompt line 3: "a re-inspection sitting on **my** calendar for the middle of this month." Universe: `gcalendar` "Make-Ready QC Inspection - Mesa Vista 4C" 2026-07-15 is on calendar_id carlos.mendez / wesley.tran / brooke.phillips (attendees Carlos/Brooke/Wesley); Jaime is not attendee/organizer; Jaime's own calendar holds only the 5/21 past 4C events. The first-person possessive is factually false and can misdirect a Jaime-scoped calendar search.

## Required Fix (pick one)

- **Fix 1 — prompt-side, minimal (recommended for S1 now):** drop the possessive, e.g. "There is also a re-inspection on the calendar for the middle of this month" or "Carlos has a re-inspection on the calendar for the middle of this month." Keeps the (true) fact that a 7/15 re-inspection is scheduled without claiming it is on Jaime's calendar. Re-run `validate.py --phase prompt` (word count unaffected).
- **Fix 2 — universe-side, most faithful (V4 injection; flag to HARDNESS/S2):** via `9_Universe_inject.sql` ADD a Jaime-calendar copy of / add Jaime as attendee to the 7/15 event (ADD only — do NOT modify the existing base rows, per hard-rule 4). Makes "my calendar" literally true and repairs the universe oddity of a QC inspection that excludes the QC inspector. Heavier; must clear `validate.py --phase injection`.

If Fix 1 is taken, S2/HARDNESS should note the 7/15 event lives on Carlos/Brooke/Wesley calendars so OE/rubric discovery accounts for cross-calendar lookup.

## Non-blocking Observations

- **OBS1 (chronology noise).** Deep-clean/repaint calendar events (2026-05-21) and their QB bills (TxnDate 2026-05-01) predate the current turn's 6/15 move-out. Universe-internal noise; does not break prompt grounding (the "still tracking" fact lives on `recbd087` + the unpaid balances). S2/S3 should ground "still tracking / not closed" on the Airtable record + unpaid bills, not on calendar-event dates.
- **OBS2 (repaint vendor).** Calendar "Interior Repaint" event names Pete Donovan; the QB repaint bill `696089964235` is billed to **Permian Make-Ready Crew**. Prompt names no vendor (fine), but S2 OEs should reference the actual QB vendor (Permian) for the repaint balance.
- **OBS3 (category numbering).** Council prompt "category 5" vs PersonaBrief/doc "Cat 3" for QC — name matches; numbering quirk only.
- **OBS4 (for S2/HARDNESS).** The 7/15 QC inspection excludes Jaime (the QC inspector) from attendees. If a calendar reference is retained, ensure discovery/OEs account for the event living on colleagues' calendars.

---

## VERDICT: BLOCK

---

## Re-review (delta)

**Change reviewed:** line-3 clause "a re-inspection **sitting on my** calendar for the middle of this month" -> "a re-inspection **on the** calendar for the middle of this month" (removed the false first-person possessive; nothing else changed).

1. **A3 + A6 blocker RESOLVED.** "a re-inspection on the calendar for the middle of this month" is truthful: the confirmed 2026-07-15 "Make-Ready QC Inspection - Mesa Vista 4C" exists (`gcalendar`, on Carlos/Wesley/Brooke calendars). The sentence no longer asserts Jaime owns it, makes no "only open item" over-claim (F9-clean), and carries no first-person calendar-ownership claim anywhere in the file. No new contradiction introduced.
2. **Ripple check — clean.** Removing the possessive adds no grounding issue, narrative-state contradiction, persona-scope drift, or clarity gap. Re-verified delta mechanics: 275 words (<= 500), zero em/en dashes, zero tool/server/internal-id tokens. Lines 1 and 5 unchanged; A1/A2/A4/A7/A10/A11 untouched and remain PASS. The A11 note (7/15 event lives on colleagues' calendars, so discovery needs a cross-calendar search rather than Jaime's default calendar) persists as a downstream S2/discovery consideration only — it is no longer a false claim and is not a blocker.

## DELTA VERDICT: GO
Sole blocker (A3/A6 "on my calendar") resolved by removing the false possessive; no ripple defects; all other perspectives remain clean.
