# Council A (Grounding) — S2 OE re-review (v2, delta)

**Task:** `Tasks/28_6a390e6b331d1ed9022a9f7c`
**Phase:** S2 OE grounding (delta-only)
**Scope:** Verify the S2 revision did not introduce any grounding regression. The OE file grew from 18 → 19 OEs: one new discovery OE inserted at OE10 (oracle_gl JE-history sweep on 210000), OE18 wording polished (reminder-list scanning), all other content unchanged but renumbered (+1 from old OE10 onward).

---

## Delta items audited

### (1) NEW OE10 — oracle_gl JE-history sweep on 210000

**Tool-name check:** `oracle_gl_list_journal_entries` is defined in `Brookfield_Base_Universe/8_Server_Tools_Details.json` at line 2789. ✓ PRESENT.

**Parameter check (BLOCKING DEFECT):** OE10 specifies the call as "filtered on entity_id 'brookfield', account_id '210000', and period_id 'brookfield_FP-2026-05'". The tool's declared parameter list is `offset, limit, period_id, status, prepared_by, entry_type, min_amount` (8_Server_Tools_Details.json lines 2789–2837). **`entity_id` and `account_id` are NOT real parameters on this tool.** Only `period_id` is. This is a tool-capability overstatement equivalent to the OE18-pre-revision defect that triggered this re-review.

**Universe-content claim ("zero hits"):** verified TRUE.
- Loaded `Tasks/28_6a390e6b331d1ed9022a9f7c/_aux/Universe_Split/oracle_gl.ogl_journal_entries.json` (2388 total entries).
- brookfield JEs with `period_id in {brookfield_FP-2026-05, brookfield_FP-2026-04}`: **0 hits**.
- Substring occurrences of `6328.86` or `6,328.86` anywhere in the JE corpus: **0 hits**.
- brookfield JEs with non-null `reverses_entry_id`: **0 hits** (so no reversal partner on 210000 in either April or May).
- The "zero hits across all three slices" outcome is correctly grounded; the absence finding is real and useful.

**L8 chain-extension claim (4-hop → 5-hop):** consistent with what the universe contains. Old chain was Hop A messaging (Anaya FX framing) → Hop B blackline exception (duplicate classification) → Hop C C005 Slack thread (Hannah's VEN-441207 reply) → Hop D SAP AP zero hits on VEN-441207 / Acme Research Ltd UK. New OE10 extends to Hop E Oracle GL history zero hits on 210000 for FP-2026-05 + FP-2026-04 + $6,328.86 + reversal partner. The fifth hop is a legitimate independent absence signal: neither the structured AP subledger nor the GL ledger corroborates either branch of the classification dispute, reinforcing the routing of the disposition to Ryan Delgado. The Hardness Plan's L8 lever count is preserved and tightened.

**Net OE10 verdict:** GROUNDING REGRESSION on parameter list. Universe content and chain logic are sound.

**Fix required (minimal, in-place):** rewrite the call specification on OE10 from "filtered on entity_id 'brookfield', account_id '210000', and period_id 'brookfield_FP-2026-05'" to filter on the supported parameters only — e.g. `period_id="brookfield_FP-2026-05"` (the brookfield prefix on the period_id already scopes the call to the brookfield entity by construction), optionally setting `min_amount=6328.86` to narrow results, then **scanning the returned list** for line-level account_id "210000" and the $6,328.86 amount or a reversal-partner link. Repeat with `period_id="brookfield_FP-2026-04"` for the reversal-sweep slice. This matches the same "call then scan" pattern OE18 was polished to.

---

### (2) "OE12" cross-references in OE13 / OE14 / OE15 / OE16

Renumbering check. Previously these OEs referenced "OE11" (the staging step). After the +1 shift, the staging step is OE12.

- **OE13** "The updated explanation must reference the staged journal entry id from OE12" → ✓ correctly points to the JE create step.
- **OE14** "to record a cross-reference to the staged JE (… JE id from OE12 …)" → ✓.
- **OE15** "what the staged entry does (JE id from OE12 …)" → ✓.
- **OE16** "the staged JE id from OE12 sitting in draft …" → ✓.

All four downstream references point cleanly at the new OE12 (JE create). No stray "OE11" reference to the staging step survives in the revised file. ✓ PASS.

---

### (3) OE18 wording polish — `reminder_get_all_reminders` capability

Revised OE18 reads: "Call `reminder_get_all_reminders` and scan the returned list for the title containing 'exc_06b89e3937b04a' or 'BD3 lock'. Identify reminder_id 'reminder_scen_011_orphan_exception_0000' …". This phrasing makes the scan an explicit client-side step on the returned list, not a server-side filter. No false capability is implied on the tool. ✓ PASS.

(Note: this is the exact pattern OE10 should also adopt for the JE-history sweep — see fix-item (1).)

---

### (4) A1 / A2 / A3 re-confirmation after renumbering

- **A1 — Retention discipline on OE17 (was OE16).** OE17 specifies `retention_policy_code "AICPA_SQMS_7Y"`, explicitly noting "NOT FIRM_INTERNAL despite Anaya's claim about the workings file". `AICPA_SQMS_7Y` is in the per-task retention allowlist. No `SOX_7Y` / `SEC_PERMANENT` anywhere in the OE file. ✓ PASS.
- **A2 — JE lifecycle on OE12 (was OE11).** OE12 calls `oracle_gl_create_journal_entry` only and explicitly states "Do NOT call `oracle_gl_submit_journal_entry`, `oracle_gl_approve_journal_entry`, or `oracle_gl_post_journal_entry`. The user asked for staging only ahead of Ryan's sign-off." No submit/approve/post call elsewhere in the chain. ✓ PASS.
- **A3 — BL exception scope-write on OE14 (was OE13).** OE14 updates reference fields only (`related_journal_entry_id` or `corrective_journal_entry_id` or an appended note), explicitly preserves `state="awaiting_approval"` and `resolution_summary=null`, and explicitly forbids `blackline_resolve_exception`. ✓ PASS.

---

### (5) Renumbering spot-check — no inadvertent breakage elsewhere

Scanned the OE file for any surviving "OE11" / "OE10" reference that should have been bumped:
- No reference in OE13/14/15/16/17/18/19 to "OE11" pointing at the JE-create step. All updated to OE12. ✓
- No reference in OE11/12 to a numerically earlier OE that would have shifted past it. The new OE10 sits between OE9 (SAP absence) and the old OE10 (account / contacts) cleanly; both internal flow ("reinforcing the OE9 SAP-absence finding" inside OE10's body) and reading order (discovery before staging) hold. ✓
- OE19 (final user-facing posture, was OE18) still restates the disciplines imposed by OE6, OE12, OE14, OE9 — all valid numbers after the shift. ✓ (One nit: OE19's body does not explicitly mention OE10's GL-absence finding in its restated discipline, but the prior report did not require that and the omission is not a regression.)

No stray off-by-one. ✓ PASS.

---

## Cross-cutting checks unchanged from v1

A1 retention discipline, A2 JE lifecycle discipline, A3 BL exception scope-write discipline, parameter-trap conventions on `content` / `payload` / messaging, em-dash absence, account-number entity scoping on 210000 → all carry over from v1 unchanged. Re-verified against the renumbered targets above.

---

## Exit verdict

**BLOCK** — one grounding regression introduced by the new OE10.

**Defect list:**

1. **OE10 parameter overstatement.** OE10 specifies `entity_id` and `account_id` as filters on `oracle_gl_list_journal_entries`, but the tool's parameter schema in `8_Server_Tools_Details.json` only supports `offset, limit, period_id, status, prepared_by, entry_type, min_amount`. Rewrite OE10 to call the tool with `period_id="brookfield_FP-2026-05"` (and a second call with `period_id="brookfield_FP-2026-04"`), optionally `min_amount=6328.86`, then **scan the returned list** for line-level account 210000, the $6,328.86 amount, and any `reverses_entry_id` chain. This mirrors the call-then-scan pattern OE18 was polished to. Universe-content "zero hits" claim and the L8 chain-extension claim are correct as written and need no change once the call signature is fixed.

All other deltas (OE12 cross-references in OE13–16; OE18 wording polish; A1/A2/A3 re-confirmation; renumbering spot-check) PASS without further action.

After OE10 is rewritten on the supported parameter set, re-submit for a one-item delta re-review.
