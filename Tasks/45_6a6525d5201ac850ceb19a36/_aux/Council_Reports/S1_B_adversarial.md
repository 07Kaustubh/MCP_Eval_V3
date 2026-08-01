# Council B — Adversarial QC + Density + Hardness Preservation — S1 PROMPT

**Task:** 45_6a6525d5201ac850ceb19a36 · **Universe:** starpm (V4, dual-model) · **Today:** 2026-07-01 America/Chicago
**Deliverable:** `5_Prompt.txt` (Jaime Salinas QC pass on Mesa Vista 4C mid-June make-ready turn)
**Intended correct answer:** KICK-BACK / HOLD · **Density scheme:** StarPM per-model (target 40+, floor 15)
**Mode:** READ-ONLY. Five role lenses (Architect, Implementer, Red-team, Ground-truth, Integration); verdict = union.

---

## Ground-truth anchor (re-verified against `_aux/Universe_Split/`, not the Hardness Plan's claims)

| Record | Table | Status | Distinguishing content | Role |
|---|---|---|---|---|
| `recbd087a4abd605b` | tblMakeReady | **selProg** | fldMoveOut **2026-06-15**, fldTargetReady **2026-06-30**, fldNotes2 "Deep clean and interior repaint **still tracking**… Will update status to Ready once all vendor and in-house scopes are signed off" | **TRUTH — current turn, NOT ready** |
| `recc8534b3fd13954` | tblMakeReady | selReady | fldMoveOut 2026-06-01, fldTargetReady 2026-06-14, "Unit confirmed ready for leasing" (created 2026-05-29, LATER) | DECOY — prior completed turn |
| `reca424761ae15355` | tblMaintenanceTickets | selHigh | MR-4C-2026-08, "All make-ready work… complete… market-ready… Brooke Phillips notified", fldCompletionDate **2026-05-01** | DECOY — "done" ticket |
| `rec12969a3fdb0852` | tblMaintenanceTickets | selHigh | MT-2026-084, "Make-ready turn opened… full unit turnover scope initiated", fldCompletionDate 2026-05-01 | DECOY — turn-open ticket (**Hardness Plan missed this row**) |

**Corroborators verified:** deep-clean bill `195089456477` (Sunshine Cleaning) `type=bill` **balance 387.0** UNPAID · interior-repaint bill `696089964235` (Permian Make-Ready Crew) `type=bill` **balance 1340.0** UNPAID · future event `0hjw400xgjb3j7ay7ynuaqbnpi` **2026-07-15** "Make-Ready QC Inspection - Mesa Vista 4C" · Carlos Mendez (Onsite PM, carlos.mendez@starpm.com) · Brooke Phillips (Apartment Property Supervisor, brooke.phillips@starpm.com) · Jaime Salinas (`p_007`, QC Inspector) · #make-ready = C004.

**Record-census correction:** Mesa Vista 4C has **4 records (2 make-ready + 2 maintenance tickets)**, not the "3" the Hardness Plan states. Immaterial to the answer and to F7 (the extra row is a maintenance ticket, not a competing make-ready turn), but it means **two** "done"-flavored maintenance tickets bait latching, not one. Carry to S3 (non-blocking advisory, B6 below).

---

## [B1] QC sub-dimension scoring (`Docs_starpm/7_QC_Spec_Doc1.json`) — bar is 5 on every dim

- **SUB-DIM Unique Ground Truth -> 5/(1|5) -> REASON:** Single end-state = HOLD. The prompt hands the sign-off/hold branch to the investigation; the universe resolves it decisively (selProg + "still tracking" + past-due 6/30 target + two unpaid vendor bills + 7/15 re-inspection pending). No literal-text-vs-universe split (the persona explicitly defers to her own pass), so the 06/09 file-vs-defer failure shape does not apply. Sign-off is a latching/wrong-turn error, not a second valid reading. PASS.
- **SUB-DIM Feasibility -> 5/(1|3|5) -> REASON:** Every ask maps to a tool (Airtable update, Linear issue+comment, Slack post, Gmail draft) and every load-bearing fact exists and is retrievable (verified above). No per-X breakdown requested → no dimensional-feasibility gate. PASS.
- **SUB-DIM Explicit Tool Mention -> 5/(1|5 binary) -> REASON:** No MCP tool-function names. "issue tracker", "make-ready channel", "get an email together", "set the QC status" are natural artifact/service references — not "the Linear tool" / "the X MCP server" phrasing, so not even the non-fail band is triggered. PASS.
- **SUB-DIM Prompt Clarity & Specificity -> 5/(1|3|5) -> REASON:** One coherent ask: investigate the pinned turn, set QC status to the correct call, open a ticket of what's left, post to the channel, draft Carlos an email, loop Brooke if holding. No Action-Decision-Ambiguity: the sign-off/hold conditional is resolved by data to a single write action (hold), not left to two unresolved readings. Delegation is unambiguous — all imperatives are directed at the agent. PASS.
- **SUB-DIM Contrived / Unnatural -> 5/(1|3|5) -> REASON:** Natural QC scenario in Jaime's voice; difficulty is conflicting data across services (ticket/prior-turn/chatter say done vs. structured selProg), not arbitrary constraints or a command list. PASS.
- **SUB-DIM Alignment with Today's Date -> 5/(1|3|5) -> REASON:** Today 2026-07-01. "mid-June move-out" (6/15, past), "end-of-month target… come and gone" (6/30, one day past — accurate), "re-inspection… middle of this month" (7/15, future event — permitted). The decoy tickets' 5/01 completion dates are internally messy but sit in DECOY data and, if anything, reinforce the correct answer (a turn that moved out 6/15 cannot have completed 5/01) — no push toward a wrong end-state. PASS.
- **SUB-DIM Truthfulness -> 5/(1|3|5) -> REASON:** All tight identifiers verified: Carlos (Onsite PM), Brooke (Apt Property Supervisor), the two scopes = deep clean + interior repaint (both with live unpaid vendor bills), mid-June move-out / end-of-month target / mid-month re-inspection all match universe records. No phantom, no factual error. PASS.
- **SUB-DIM Tool Use & Cross-service -> 5/(1|5 binary) -> REASON:** Requires reconciliation across Airtable + QuickBooks + GCalendar + Contacts + Slack + Linear + Gmail (7 services) — far beyond the 2-service floor; facts are scattered and must be reconciled. PASS.
- **SUB-DIM Investigation + Action -> 5/(1|5 binary) -> REASON:** Heavy investigation (reconcile 2 make-ready rows + 2 tickets + QB bills + calendar) feeds 4 writes; cannot act without investigating. PASS.
- **SUB-DIM Coherence / Bolt-on -> 5/(1|5 binary) -> REASON:** Remove-a-sentence test: every ask (set status, open ticket, post channel, email Carlos, notify Brooke) causally flows from the single QC-decision situation. No bolt-on. PASS.
- **SUB-DIM Persona -> 5/(1|3|5) -> REASON:** Jaime Salinas is the impartial QC sign-off anchor who walks units after maintenance declares complete and signs off or kicks back — exactly this task. Voice (short, factual, observation-first) matches. PASS.
- **SUB-DIM Business Function -> 5/(3|5) -> REASON:** BF3 Quality Control & Field Services — a QC sign-off/kick-back on a make-ready turn is squarely in-function. PASS.

**B1 result: 12/12 sub-dims = 5. No dimension below bar.**

---

## [B2] Adversarial alt-path / second reading

**(a) Intended stump exists — CONFIRMED (desirable difficulty, not a defect).** Three findable "done" signals bait a latching agent into SIGN OFF: (1) Carlos's "wrapped, list it" report (prompt line 1); (2) maintenance ticket MR-4C-2026-08 "All make-ready work… complete… market-ready… QC walkthrough by Jaime… Brooke notified"; (3) the prior selReady turn `recc8534`. An agent that trusts any of these signs off wrongly.

**(b) Kick-back is UNIQUELY correct — CONFIRMED.** Sign-off is NOT defensible from the actual data, only from latching:
- The **current** turn `recbd087` (the one the prompt pins) is `fldTurnStatus=selProg`, notes "deep clean and interior repaint **still tracking**." Airtable is SoR for make-ready state (StarPM rule) → this structured field is authoritative.
- Target-ready **6/30 is past-due** as of 2026-07-01.
- Both named scopes have **unpaid vendor bills** (deep clean 387 / repaint 1340, balance>0) — and the prompt's own rule ("finished with the bill still unpaid does not count as closed") makes unpaid → not closed.
- The **7/15 QC re-inspection has not yet occurred**.
- The "complete" ticket's fldCompletionDate **5/01 is impossible** for a turn that moved out 6/15 → it describes the *prior* turn, not this one; its "market-ready in the make-ready record" claim maps to `recc8534` (selReady), not `recbd087`.
Every decisive signal points to HOLD. **No genuine second end-state → Unique Ground Truth holds.**

**(c) Target disambiguation holds — CONFIRMED.** "mid-June move-out" (6/15) + "end-of-month target" (6/30) uniquely select `recbd087` among the two make-ready rows; the prior turn is 6/1 move-out / 6/14 target (neither "mid-June" nor "end-of-month"). Robust, non-fragile pin. **F7 clears.** (One divergence from the plan: 4 records exist, not 3 — see census correction; does not affect uniqueness of the make-ready-turn target.)

---

## [B3] Tool-call density projection (per model — StarPM band: ≥40 PASS)

Competent trajectory (both models same discovery sweep): resolve Carlos → Airtable tables/get records tblMakeReady (2 rows) → tblMaintenanceTickets (2 tickets) → reconcile → QuickBooks bills for 4C (deep-clean + repaint balances) → GCalendar 7/15 event → resolve Brooke → Slack #make-ready context, then 4-5 writes (Airtable QC-status update on `recbd087` · Linear issue + comment · Slack C004 post · Gmail draft to Carlos) + post-write verification + cross-service param-trap retries (slack `message`, gmail draft-only `body`, linear `team`).

| Component | Range | Mid |
|---|---|---|
| Discovery sweep (7 services) | 12-20 | 16 |
| Reconcile 2 make-ready rows + 2 tickets + QB balances (L2/L1/L10) | 6-10 | 8 |
| L9 future-event + past-due target reasoning | 3-5 | 4 |
| Writes (4-5) + post-write verify | 7-11 | 9 |
| Cross-service param-trap buffer | 3-6 | 4 |
| **TOTAL** | **31-52** | **~41** |

**Per-model midpoint: Opus ≈ 43, Gemini ≈ 41. Both ≥ 40 → PASS (thin margin).** Well above the 15 floor. **NOTE (non-blocking):** the margin is genuinely thin and rests on the 4-5-write mix + post-write verification being preserved downstream — the Hardness Plan's own L33 note records StarPM runs landing 33-38 per run. S2/S3 must hold 4-5 writes across Airtable/Linear/Slack/Gmail (not collapse to 3) or real runs risk dipping under 40. Even read pessimistically as THIN (~38), it is "acceptable with documented per-task justification," which the Hardness Plan supplies. Not a blocker at prompt phase; flag for S4 density confirmation.

---

## [B4] Hardness preservation

- **L2 structured-DB skip (SYMMETRIC) — PRESERVED.** "before anyone lists it I need the real state of that turn" + "whether both are genuinely closed and signed off or still tracking" forces the agent to the make-ready row's own status/notes; every easier signal (ticket, chatter, prior turn) says done. Both models fail if they stop at chatter.
- **L1 latching (OPUS-SEL) — PRESERVED.** Baited explicitly in line 1: "Carlos has Mesa Vista 4C down as wrapped… Brooke is ready to put it on the market on his word."
- **L10 supersession (OPUS-SEL) — PARTIALLY PRESERVED, acceptable.** The "complete" ticket + prior selReady still bait "trust the done record," but rule-13 disambiguation ("mid-June move-out") narrows *which row to inspect*, softening the pure pick-latest-row variant. Per the council's own note, **rule-13 F7 disambiguation legitimately takes priority over L10**; the latching-on-ticket variant of the Opus stump survives intact. **No HARDNESS_REGRESSION.**
- **L31 explicit negative directive (GEMINI-SEL) — PRESERVED + GROUNDED.** The prompt explicitly asks for the sign-off-OR-kick-back call and the do-not-market hold: "if it is not, say so plainly and hold it, because it does not go to listing until every outstanding scope is closed and signed off… If I am holding it back, Brooke needs to hear it from us before she markets it." The negative is an **explicitly requested output** → avoids the Task-39 "phrase never asked" defect. (b) satisfied.
- **L7 multi-write — PRESERVED.** Four writes (Airtable QC status, Linear ticket, Slack #make-ready post, Gmail draft to Carlos) + Brooke notification.
- **L9 future-event — PRESERVED + F9-clean.** "re-inspection… middle of this month" (7/15) and "target… already come and gone" (6/30 past-due). The prompt does **not** claim the re-inspection is the "only open item," and the 7/15 event is the task's own forward action → no F9 unreconciled-future-event trap.

**No lever lost or neutralized. rule-13 disambiguation vs L10 tension resolved in rule-13's favor as designed.**

---

## [B6] Upstream propagation

**No BLOCKING PROPAGATE flags.** One **non-blocking advisory** (does not change lever selection or ground truth): the Hardness Plan record census (`_aux/Hardness_Plan.md`, lines 12 and 89) states Mesa Vista 4C has "3 records"; the universe actually holds **4** (adds `rec12969a3fdb0852` MT-2026-084 turn-open ticket in tblMaintenanceTickets). Fix: correct the census to "2 make-ready + 2 maintenance tickets" and carry "two decoy 'done' tickets" into S3 so the QC-status write-action rubric binds to the current in-progress turn (mid-June move-out / end-of-month target, `recbd087`) and is not satisfied by either maintenance ticket. This strengthens (not weakens) the latching bait.

---

## Summary

All 12 prompt sub-dims score 5. The intended stump (latch → sign off) is present and strong, while kick-back/HOLD is the uniquely correct end-state, decisively grounded in the current turn's selProg status, past-due target, two unpaid vendor bills, and pending 7/15 re-inspection — sign-off is unreachable except by latching or wrong-turn conflation. Target disambiguation is robust (F7 clears). Every hardness lever still fires (L31 grounded; L10 correctly subordinated to rule-13). Per-model density projects ~41-43 (≥40, thin margin, documented). Only issues: one non-blocking census correction to carry into S3, and a design-margin note to preserve 4-5 writes downstream.

VERDICT: GO

---

## Re-review (delta)

**Change under review:** line 3 "a re-inspection **sitting on my** calendar for the middle of this month" → "a re-inspection **on the** calendar for the middle of this month" (Council A's sole grounding BLOCK: the 2026-07-15 QC re-inspection is on Carlos/Wesley/Brooke calendars, not Jaime's; false possessive removed). Lines 1 and 5 verified byte-identical to prior review. Delta-only assessment below.

1. **QC sub-dims — no regression.** Only the re-inspection clause is touched. **Truthfulness: same-or-better** — the false calendar-ownership claim is gone; "on the calendar" is neutrally true (the 7/15 event exists on the shared/colleagues' calendars). **Alignment with Today's Date: unchanged** (still resolves to future 2026-07-15 from 2026-07-01). Persona voice remains natural (arguably more fitting for an impartial QC). Remaining 10 sub-dims untouched. **12/12 = 5 holds.**
2. **Density (B3) — no drop.** Removing "my" means the L9 event no longer sits on Jaime's own calendar, so the agent must search across calendars / by keyword to surface "Make-Ready QC Inspection - Mesa Vista 4C" (7/15). That **adds** (or at worst holds) discovery calls. Per-model midpoint stays **~41-43, ≥40**.
3. **Hardness (B4) — all levers still fire.** L9 unchanged/strengthened (event still present and load-bearing; now requires broader cross-calendar discovery; F9-clean preserved). L1 latching / L2 structured-DB skip / L10 supersession / L31 grounded negative directive / L7 multi-write all live in untouched clauses. No HARDNESS_REGRESSION.
4. **Adversarial (B2) — no new reading.** "on the calendar" still uniquely resolves to the only *future* 4C event (7/15; other 4C events are 5/21, past). No new second reading, no change to write actions or end-state. UGT single end-state (HOLD) intact; the edit also removes an agent-confusion vector (searching only Jaime's calendar → empty result).

The edit is strictly same-or-better on all four axes. Prior GO stands.

DELTA VERDICT: GO
