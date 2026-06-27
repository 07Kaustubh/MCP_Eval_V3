# Council A (Grounding) — S2 OE re-review (v3, delta on OE10 parameter fix)

**Task:** `Tasks/28_6a390e6b331d1ed9022a9f7c`
**Phase:** S2 OE grounding (delta-only, third pass)
**Scope:** Verify that the OE10 rewrite resolves the v2 BLOCK (parameter overstatement of `entity_id` / `account_id` on `oracle_gl_list_journal_entries`), re-confirm the zero-hit GL ground truth under the corrected call shape, and confirm no other OE drifted.

---

## (1) OE10 parameter list re-verified against tool spec

**Tool:** `oracle_gl_list_journal_entries` (from `Brookfield_Base_Universe/8_Server_Tools_Details.json`).
**Declared parameter set:** `offset, limit, period_id, status, prepared_by, entry_type, min_amount`.

**OE10 revised call signature:**

> "Call `oracle_gl_list_journal_entries` with `period_id "brookfield_FP-2026-05"` and `min_amount 6328.86` (and a second call with `period_id "brookfield_FP-2026-04"` and the same `min_amount` to sweep for any reversal partner), then inspect each returned entry's lines for any hit on account 210000 against the $6,328.86 figure (use `oracle_gl_get_journal_entry` on any candidate to read its lines)."

- `period_id` → ✓ supported parameter, string, nullable.
- `min_amount` → ✓ supported parameter, number, nullable.
- `entity_id` → no longer named as a filter parameter. ✓ defect cleared. (Entity scoping is achieved by the `brookfield_` prefix on the period_id, which is the project-accepted pattern.)
- `account_id` → no longer named as a filter parameter. ✓ defect cleared. (Per-line account scoping is now correctly stated as a client-side scan of returned entries' lines.)

**Tool:** `oracle_gl_get_journal_entry`.
**Declared parameter set:** `entry_id` (required, string).

OE10 says "use `oracle_gl_get_journal_entry` on any candidate to read its lines" — the implied parameter is the entry id, matching the tool's `entry_id` field. ✓ no overstatement; the OE leaves the param name implicit and points the agent at the JE id, which is the only way to read lines.

**Net:** v2 BLOCK item is resolved. Both tools are called with declared parameters only. The call-then-scan pattern now matches the OE18 reminder-list pattern.

---

## (2) Zero-hit ground truth re-confirmed under the corrected query shape

Scanned `Tasks/28_6a390e6b331d1ed9022a9f7c/_aux/Universe_Split/oracle_gl.ogl_journal_entries.json` (2,388 entries total).

Counts under the revised call shape (server returns by `period_id` + `min_amount`; client scans returned lines for `account_id == "210000"` and `$6,328.86`; client also inspects `reverses_entry_id`):

| Slice | Brookfield JEs touching 210000 | Brookfield JEs with any $6,328.86 line | Brookfield JEs with line on 210000 AND $6,328.86 | Brookfield JEs with `reverses_entry_id` set |
|---|---|---|---|---|
| `brookfield_FP-2026-05` | **0** | **0** | **0** | **0** |
| `brookfield_FP-2026-04` | **0** | **0** | **0** | **0** |

OE10's three independent absence claims all hold:
- No existing JE on 210000 in either period — ✓ ZERO hits.
- No $6,328.86 amount on 210000 in either period — ✓ ZERO hits.
- No `reverses_entry_id` chain on 210000 in April that would partner a May corrective — ✓ ZERO hits (no brookfield reversal in either period at all).

L8 chain-extension claim (5-hop absence trail: messaging FX framing → BL exception duplicate classification → C005 thread VEN-441207 → SAP AP zero hits → GL history zero hits) is preserved and remains grounded.

---

## (3) No collateral disturbance to other OEs from the OE10 edit

Re-scanned the full OE file:

- OE1–OE9 wording unchanged from v2; renumbering is stable (the new OE10 sits at the same numeric slot as in v2, no further +1 shift).
- OE11 (account / contacts) wording unchanged.
- OE12 (JE create / staging) wording unchanged. Downstream "OE12" references in OE13 / OE14 / OE15 / OE16 still point cleanly at the JE create step. ✓
- OE12 business-justification language still names "the Oracle GL history on 210000 in FP-2026-05 and FP-2026-04 returned zero matches for the variance figure" — which is the OE10 finding being relayed. ✓ self-consistent with the corrected OE10.
- OE13 still names "the SAP-absence and GL-absence findings from OE9 and OE10" — ✓ self-consistent.
- OE17 retention discipline (`AICPA_SQMS_7Y`, "NOT FIRM_INTERNAL") unchanged.
- OE18 reminder polish unchanged.
- OE19 final posture unchanged.

No stray edits, no off-by-one, no broken cross-reference.

---

## (4) A1 / A2 / A3 re-confirmation

- **A1 — Retention discipline on OE17.** `retention_policy_code "AICPA_SQMS_7Y"` (in per-task allowlist), classification `"internal"`, no `SOX_7Y` / `SEC_PERMANENT` anywhere in the OE file. ✓ PASS.
- **A2 — JE lifecycle on OE12.** Only `oracle_gl_create_journal_entry` is called; submit / approve / post explicitly forbidden, with reason ("staging only ahead of Ryan's sign-off"). ✓ PASS.
- **A3 — BL exception scope-write on OE14.** `blackline_update_exception` writes a cross-reference only, state stays `awaiting_approval`, `resolution_summary` stays null, `blackline_resolve_exception` explicitly forbidden. ✓ PASS.

All three carry-overs hold.

---

## (5) Cross-cutting checks unchanged

Em-dash absence, parameter-trap conventions (`content` for email, `payload` for Slack, `body` for Linear, etc. on the touched OEs), account-number entity scoping on 210000 → all re-verified, all PASS.

---

## Exit verdict

**GO** — OE10 parameter overstatement is resolved on the supported parameter set; zero-hit ground truth re-confirmed under the corrected call shape; no collateral edits elsewhere; A1 / A2 / A3 still PASS.

No further iteration required from Council A.
