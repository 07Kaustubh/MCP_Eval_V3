# Council B — Adversarial QC — S2 Oracle Events (v2 delta re-review)

**Task:** `Tasks/28_6a390e6b331d1ed9022a9f7c`
**Council role:** B (adversarial), delta-only re-review
**Phase:** S2 — Oracle Events
**OE file:** `6_Oracle_Events.txt` (now **19 OEs**; was 18 in v1)
**Reviewer posture:** read-only; delta-scope only (re-grade B3 density; spot-check the new OE10 and the OE18 polish; confirm cross-reference renumbering OE11→OE12; verify no regression elsewhere).
**Prior report:** `_aux/Council_Reports/S2_B_adversarial.md` — v1 verdict was GO with a THIN_DENSITY watch-flag on B3 (midpoint ~48). v2 was produced to address that flag.

---

## Delta summary

| Change | Description |
|---|---|
| **+1 OE inserted (new OE10)** | `oracle_gl_list_journal_entries` discovery step. Three query slices: (a) brookfield/210000/FP-2026-05 for amount $6,328.86, (b) brookfield/210000/FP-2026-04 sweep for any reversal partner, (c) reverses_entry_id chain on 210000. Expected output: zero hits across all three slices. Purpose: extend the L8 multi-link chain from 4 hops to 5 hops; corroborate the L1 latching conflict by showing the GL history does not support either framing; reinforce the OE9 SAP-absence finding. |
| **OE18 wording polished** | The v1 parenthetical "(or filter on title containing 'exc_06b89e3937b04a' or 'BD3 lock')" overstated `reminder_get_all_reminders` (which has no server-side title filter). Revised wording reads "scan the returned list for the title containing..." which correctly frames the operation as a client-side scan. |
| **Downstream renumbering** | Old OE10..18 are now OE11..19. All cross-references inside the OE bodies that named "JE id from OE11" must now read "JE id from OE12". This v2 re-review verifies the renumber landed everywhere. |

---

## (1) B3 — Tool-call density re-projection

| OE | Role | Tool-call range | Mid |
|---|---|---:|---:|
| OE1 | Discovery (msg search variants + list + get) | 3 - 5 | 4.0 |
| OE2 | Single get (BL recon) | 1 - 2 | 1.0 |
| OE3 | Discovery (BL list_exceptions + get_exception) | 1 - 3 | 2.0 |
| OE4 | Discovery (FP list + 2 gets) | 2 - 4 | 3.0 |
| OE5 | Discovery (email search + get) | 1 - 3 | 2.0 |
| OE6 | Discovery (RV 3 list variants + candidate get) | 3 - 5 | 4.0 |
| OE7 | Discovery (Slack search, 3 query variants) | 2 - 4 | 3.0 |
| OE8 | Single replies | 1 - 2 | 1.0 |
| OE9 | Discovery (SAP 3 filter variants) | 3 - 5 | 4.0 |
| **OE10 (NEW)** | **Discovery (GL JE 3 query slices + pagination + client-side filtering)** | **3 - 5** | **4.0** |
| OE11 | Discovery (account + 4 contacts via search or per-name) | 2 - 5 | 3.5 |
| OE12 | Write (oracle_gl_create_journal_entry, possibly a precheck) | 1 - 2 | 1.5 |
| OE13 | Write (BL variance update) | 1 - 2 | 1.5 |
| OE14 | Write (BL exception update) | 1 - 2 | 1.5 |
| OE15 | Write (email_send_email) | 1 - 2 | 1.5 |
| OE16 | Write (slack add_message) | 1 - 2 | 1.5 |
| OE17 | Write (RV upload + possible pre-list to confirm fresh-upload posture) | 1 - 3 | 2.0 |
| OE18 | Multi-step (get_all + delete + add) | 3 - 4 | 3.0 |
| OE19 | Posture summary, no tool call | 0 - 0 | 0.0 |
| **Subtotal** | | **30 - 60** | **44.0** |
| Cross-service triangulation buffer (L1 conflict re-reads, L8 5-hop re-walks, L9 double verification) | | 5 - 10 | 7.5 |
| **Projection** | | **35 - 70** | **51.5** |

- **Lower bound estimate:** ~35
- **Midpoint estimate:** ~52 (51.5 rounded up to the nearest integer)
- **Upper bound estimate:** ~70

**Brief's expected midpoint check.** The brief said: "Total midpoint should rise from ~48 to ~52 (clears the 50+ design target). Confirm or correct." **Confirmed.** v1 midpoint was 47.5 (rounded ~48); inserting OE10 with mid 4.0 plus pagination headroom inside the triangulation buffer takes the new midpoint to 51.5 (rounded ~52). Within the +1 expected granularity, this matches the brief's projection.

**OE10 sizing rationale.** The OE describes three logically distinct query slices. The real `oracle_gl_list_journal_entries` tool exposes only `period_id` (not `entity_id` / `account_id`) as a server-side filter — see (3) Accuracy below — so each slice is realistically a list call followed by client-side filtering on account_id and amount, and at least one slice (the reverses_entry_id chain across periods) is likely two list calls plus inspection because the tool does not filter on `reverses_entry_id` either. Range 3-5 is fair; mid 4.0 is fair. The brief's "new OE10 expected range: 3-5 calls, mid 4.0" is confirmed.

### Updated B3 verdict

**PASS** (midpoint 52, clears 50+ design target). The v1 THIN_DENSITY watch-flag is **cleared**. The L8 5-hop chain materializes inside a single OE (OE10) rather than relying on the cross-service triangulation buffer to absorb it, which is the more defensible posture for downstream platform-side density tracking.

---

## (2) OE Completeness — Forward coverage delta (new OE10)

The brief's claim to verify: "New OE10 maps to prompt clauses (period correctness verification + L1 classification disambiguation) and to L8 multi-link chain (4-hop → 5-hop strength)."

| Anchor | New OE10 coverage | Verdict |
|---|---|---|
| Prompt clause 7 ("Stage the entry in the right place ... referencing the exception ... with the business justification spelling out what the support shows.") | OE10's GL-history-zero finding is load-bearing for OE12's business_justification, which the OE12 text now explicitly cites ("the Oracle GL history on 210000 in FP-2026-05 and FP-2026-04 returned zero matches for the variance figure"). | PASS |
| L1 Latching (FX vs duplicate) disambiguation | OE10 confirms neither framing has a corroborating GL trail. Together with OE9 (SAP zero), this strengthens the agent's posture of routing the classification question to Ryan rather than asserting either framing. | PASS |
| L8 Multi-link chain extension | v1 chain was msg → BL → Slack → SAP (4 hops). v2 chain is msg → BL → Slack → SAP → GL history (5 hops). OE10 is the explicit 5th hop. Lever is strengthened, not weakened. | PASS |
| Pre-staging duplicate-prevention discipline (implicit in any "stage a JE" instruction) | OE10 explicitly checks for "no prior posted or draft entry for $6,328.86 against 210000 that the corrective would duplicate". This is a standard hygiene check ahead of OE12. | PASS |

No regression on the v1 forward-coverage matrix (every prompt clause still maps to at least one OE).

**Score — OE Completeness: 5 / 5** (unchanged from v1).

---

## (3) OE Accuracy — New OE10 fact verification

### (3a) Tool existence

`oracle_gl_list_journal_entries` — verified present in `Brookfield_Base_Universe/8_Server_Tools_Details.json` (line 2789). Description: "List journal entries with optional filters." **Tool exists. ✓**

### (3b) Parameter accuracy — **NEW MINOR ISSUE FLAGGED**

The brief asked: "Parameters `entity_id`, `account_id`, `period_id` are real params for that tool. Verify."

Verified parameter list from `8_Server_Tools_Details.json` (lines 2791-2826):

| OE10 named filter | Real param on tool? |
|---|---|
| `period_id` | **YES** (real, optional, nullable) |
| `entity_id` | **NO** (not in parameter list) |
| `account_id` | **NO** (not in parameter list) |

The full parameter set is `offset`, `limit`, `period_id`, `status`, `prepared_by`, `entry_type`, `min_amount`. The tool does **not** expose `entity_id` or `account_id` as server-side filters.

**Severity: Minor wording issue.** This is analogous to the v1 OE17 (now OE18) parenthetical overstatement of `reminder_get_all_reminders` — the OE intent is correct (verify the GL history doesn't corroborate either framing), the tool selection is correct (`oracle_gl_list_journal_entries`), the trajectory still lands on the correct universe answer (zero hits across all three slices — see (3c) below), and the OE10 expected output is achievable by the agent calling the tool with `period_id` filter and client-side filtering on the line-level `account_id` and amount. The wording "filtered on entity_id, account_id, and period_id" overstates what the tool natively does.

**Recommended polish (not a blocker):** rephrase OE10 to read along the lines of "Call `oracle_gl_list_journal_entries` with `period_id="brookfield_FP-2026-05"` and scan the returned entries' lines for `account_id="210000"` and amount $6,328.86. Repeat with `period_id="brookfield_FP-2026-04"` for any reversal partner. Then scan for any brookfield entry on 210000 with `reverses_entry_id` set." This preserves the three logical slices, the L8 5-hop strengthening, and the expected zero result; it just stops claiming the tool natively filters by entity_id/account_id.

Per the V3 brief's tiered scheme, parameter-overstatement wording issues that do not change the agent's reachable destination (correct answer, correct trajectory shape, correct tool family) are **Minor**, not blocking. Same severity treatment as v1's `reminder_get_all_reminders` overstatement.

### (3c) Universe ground truth — verified via grep on `oracle_gl.ogl_journal_entries.json`

| Slice | Filter applied | Hit count |
|---|---|---:|
| Slice 1 | brookfield + FP-2026-05 + line on 210000 + amount $6,328.86 | **0** |
| Slice 2 | brookfield + FP-2026-04 + line on 210000 + amount $6,328.86 | **0** |
| Slice 3 | brookfield + `reverses_entry_id` set + line on 210000 (any period) | **0** |
| Sanity 1 | brookfield + FP-2026-05 + line on 210000 (any amount) | **0** |
| Sanity 2 | brookfield + FP-2026-04 + line on 210000 (any amount) | **0** |

**All three slices return zero, exactly as OE10 claims.** The sanity rows show there are no brookfield JEs touching 210000 in either close period — meaning the agent's expected zero result is robust across paginated traversal as well. L8 5th-hop lever is intact and correctly anchored to universe data.

### Score — OE Accuracy: 5 / 5

With the Minor wording note in (3b) recorded as a polish recommendation. Trajectory accuracy and universe ground truth are 5/5; tool name is real; the three filter slices map to the correct expected output; the polish is wording, not destination. (Treating this as a 4/5 / BLOCK would mean rejecting an OE that correctly leads the agent to a verified-zero universe result over a parenthetical naming gap — same calibration the v1 council applied to OE17's parenthetical.)

---

## (4) B4 — Hardness preservation

| Lever | v1 status | v2 delta | Verdict |
|---|---|---|---|
| **L1 Latching** | PASS — exercised across OE1 + OE3 + OE11 + OE14 + OE16 + OE18 | OE10's GL-zero finding adds a third corroborating absence (alongside OE6 phantom-doc and OE9 SAP-zero). The classification question routes to Ryan with stronger anchoring. **Strengthened.** | PASS |
| **L5 Thread-reply blindness** | PASS — exercised across OE7 + OE8 + OE14 | No change. Reply pull and downstream content requirement unchanged. | PASS |
| **L7 Multi-write diversification** | PASS — 7 writes / 7 services across OE11..OE17 | After renumber, the 7 writes are now OE12 (oracle_gl) + OE13 (BL recon) + OE14 (BL exception) + OE15 (email) + OE16 (slack) + OE17 (records vault) + OE18 (reminder reset). **Still 7 writes / 7 services. Unchanged.** | PASS |
| **L8 Multi-link chain** | PASS — 4 hops (msg → BL → Slack → SAP) | **STRENGTHENED to 5 hops** (msg → BL → Slack → SAP → GL history). New OE10 is the 5th hop. | PASS (strengthened) |
| **L9 Universe-grounded gotcha (twin)** | PASS — exercised across OE4 + OE5 + OE6 + OE16 + OE18 | No change. | PASS |

**No lever weakened.** L1 and L8 both strengthened. **Score — B4 Lever Preservation: 5 / 5** (unchanged from v1, with L8 strengthened).

---

## (5) Reverse coverage — new OE10 maps to real anchors

| Anchor | OE10 mapping | Verdict |
|---|---|---|
| Prompt clause 7 ("Stage the entry in the right place ... with the business justification spelling out what the support shows") — implicit pre-staging duplicate-prevention | OE10's first slice verifies no prior $6,328.86 entry on 210000 in FP-2026-05; this is standard hygiene any staged JE should clear. The OE12 business_justification text now explicitly cites the GL-zero finding. | PASS |
| Hardness L8 (multi-link chain) | OE10 is the explicit 5th hop. | PASS — load-bearing |
| Hardness L1 (latching disambiguation) | OE10's GL-zero finding corroborates that neither the FX framing nor the duplicate framing has a GL trail, reinforcing the route-to-Ryan posture. | PASS — load-bearing |

**No scope creep.** OE10 services real load-bearing anchors and does not introduce new prompt asks.

---

## (6) Cross-reference renumbering check — OE13/OE14/OE15/OE16 references to JE creation step

The brief asked: "OE13/OE14/OE15/OE16 now reference 'JE id from OE12' (was OE11). Verify the references resolve correctly to the JE creation step."

Verification by direct read of the OE file:

| OE | Reference text | Resolves to OE12 (JE creation)? |
|---|---|---|
| OE12 | Is the JE creation step itself (`oracle_gl_create_journal_entry`) | (target, n/a) |
| OE13 | "the updated explanation must reference the staged journal entry id from OE12" | YES |
| OE14 | "for example by populating related_journal_entry_id or corrective_journal_entry_id with the JE id from OE12, or by appending a note that names the JE id" | YES |
| OE15 | "what the staged entry does (JE id from OE12, draft in brookfield_FP-2026-05 ...)" | YES |
| OE16 | "the staged JE id from OE12 sitting in draft against FP-2026-05" | YES |
| OE17 | "title naming the staged JE id" (not numbered, but contextually references the OE12 JE) | YES (no explicit OE number, but the staged JE referenced is the one OE12 creates) |

All five downstream write OEs that depend on the staged JE id correctly reference OE12. No dangling "OE11" references found.

**Cross-reference check: PASS.**

---

## (7) OE18 wording polish check

The brief asked: "Previously the parenthetical '(or filter on title containing exc_06b89e3937b04a or BD3 lock)' overstated `reminder_get_all_reminders`. The revised text should read 'scan the returned list for the title containing...' Confirm the overstatement is gone."

Verified by direct read of OE18:

> "OE18: Call reminder_get_all_reminders and scan the returned list for the title containing 'exc_06b89e3937b04a' or 'BD3 lock'. Identify reminder_id 'reminder_scen_011_orphan_exception_0000' ..."

The overstatement is **gone**. The revised wording correctly frames the operation as a client-side scan of the returned list. **Polish confirmed.**

---

## (8) No-regression check on every other OE

Spot-checked each pre-existing OE for any unintended drift introduced by the v2 revise:

| OE | Pre-v2 identity | Post-v2 identity | Drift? |
|---|---|---|---|
| OE1 | Messaging conv pull | Messaging conv pull (verbatim) | none |
| OE2 | BL recon get | BL recon get (verbatim) | none |
| OE3 | BL exception list/get | BL exception list/get (verbatim) | none |
| OE4 | FP list | FP list (verbatim) | none |
| OE5 | Email recap pull | Email recap pull (verbatim) | none |
| OE6 | RV phantom-doc verify | RV phantom-doc verify (verbatim) | none |
| OE7 | Slack C005 parent search | Slack C005 parent search (verbatim) | none |
| OE8 | Slack thread replies | Slack thread replies (verbatim) | none |
| OE9 | SAP AP zero on VEN-441207 | SAP AP zero on VEN-441207 (verbatim) | none |
| **OE10 (new)** | — | **GL history zero (3 slices)** | **new insertion** |
| OE11 (was OE10) | Account + contacts discovery | Account + contacts discovery (verbatim) | renumber only |
| OE12 (was OE11) | JE creation (oracle_gl_create_journal_entry) | JE creation (verbatim, body now also cites OE10 GL-zero finding in business_justification) | renumber + business_justification additive note (additive only; no field overwrite) |
| OE13 (was OE12) | BL recon variance update | BL recon variance update (verbatim, body now also names OE10 GL-zero finding) | renumber + additive note |
| OE14 (was OE13) | BL exception update | BL exception update (verbatim) | renumber only |
| OE15 (was OE14) | Email to Ryan | Email to Ryan (verbatim, body now also names OE10 GL-zero finding) | renumber + additive note |
| OE16 (was OE15) | Slack C005 summary | Slack C005 summary (verbatim) | renumber only |
| OE17 (was OE16) | RV memo upload | RV memo upload (verbatim, body now also names OE10 GL-zero finding) | renumber + additive note |
| OE18 (was OE17) | Reminder reset | Reminder reset (verbatim except parenthetical polish — see (7)) | renumber + polish |
| OE19 (was OE18) | Posture summary | Posture summary (verbatim) | renumber only |

**Additive notes assessment.** OE12, OE13, OE15, OE17 now reference the OE10 GL-zero finding in their respective bodies (business_justification, recon variance note, email content, memo body). These are additive — they extend the "SAP AP subledger returned zero matches" language with a parallel "Oracle GL history on 210000 in FP-2026-05 and FP-2026-04 returned zero matches" clause. No prior fact is overwritten; the additive notes strengthen the L8 5-hop chain coverage and the L1 latching audit trail. **No regression.**

---

## Issue summary (v2 delta)

| ID | Severity | Issue | Recommendation | Carry-over from v1? |
|---|---|---|---|---|
| B-OE-v1-01 | (Minor, v1) | B3 density midpoint projected to ~48 (THIN_DENSITY) | **RESOLVED.** v2 midpoint ~52 with new OE10. | Resolved by v2 |
| B-OE-v1-02 | (Minor, v1) | OE17 (now OE18) parenthetical overstated `reminder_get_all_reminders` filter capability | **RESOLVED.** v2 wording reads "scan the returned list for the title containing..." | Resolved by v2 |
| **B-OE-v2-01** | **Minor (new)** | OE10 names `entity_id` and `account_id` as filter parameters on `oracle_gl_list_journal_entries`. Verified parameter list exposes only `period_id` from those three. The tool does support `period_id`, `status`, `prepared_by`, `entry_type`, `min_amount`, `offset`, `limit`. | Wording polish: rephrase to "Call `oracle_gl_list_journal_entries` with `period_id` filter and scan returned lines for account_id 210000 + amount 6328.86" or similar. Trajectory still lands on the correct universe answer (zero hits across all three slices, verified). No functional impact; analogous severity to v1's `reminder_get_all_reminders` parenthetical. | New in v2 (introduced by the insertion itself) |

**No Major issues.** No scope creep. No fact drift. No fabricated universe data. No retention-code violation. No em-dash / en-dash. No softened "Don't resolve" prohibition. No regression on any pre-existing OE. No cross-reference dangle.

---

## Exit verdict

**GO** — All four sub-dim scores are at 5/5 (B3 now PASS, no longer THIN_DENSITY). The v1 watch-flag is cleared. The new OE10 strengthens L1 and L8 levers and the trajectory lands on a universe-verified zero result. One Minor wording polish recommended on OE10's parameter naming (does not block — analogous to the v1 OE17 polish that was applied without blocking shipment in v1).

---

## Sub-dim scores

| Sub-dim | v1 | v2 | Delta |
|---|---|---|---|
| OE Completeness | 5 / 5 | **5 / 5** | unchanged |
| OE Accuracy | 5 / 5 | **5 / 5** | unchanged (with new Minor wording note B-OE-v2-01 on OE10 parameters) |
| B3 Tool-call density | THIN_DENSITY (mid 48) | **PASS (mid 52)** | **upgraded — watch-flag cleared** |
| B4 Hardness preservation | 5 / 5 | **5 / 5** | unchanged (L8 strengthened 4→5 hops; no lever weakened) |

**Council B (S2) v2 verdict: GO.**
