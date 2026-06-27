# Council B — Adversarial QC — S2 Oracle Events (v3 delta re-review)

**Task:** `Tasks/28_6a390e6b331d1ed9022a9f7c`
**Council role:** B (adversarial), delta-only re-review
**Phase:** S2 — Oracle Events
**OE file:** `6_Oracle_Events.txt` (19 OEs, unchanged count from v2)
**Reviewer posture:** read-only; delta-scope only (verify the v2 Minor wording note on OE10's parameter list is cleared, re-confirm B3 density still clears 50+, confirm Completeness and Hardness Preservation unchanged, verify no regression on any other OE).
**Prior report:** `_aux/Council_Reports/S2_B_adversarial_v2.md` — v2 verdict was GO with one Minor wording note (B-OE-v2-01) flagging that OE10 named `entity_id` and `account_id` as server-side filters on `oracle_gl_list_journal_entries`, which only exposes `offset`, `limit`, `period_id`, `status`, `prepared_by`, `entry_type`, `min_amount`.

---

## Delta summary (v3)

| Change | Description |
|---|---|
| **OE10 parameter list corrected** | The v2 Minor note B-OE-v2-01 has been addressed. The revised OE10 now names only real server-side filters on `oracle_gl_list_journal_entries` (`period_id` and `min_amount`) and correctly describes the account-210000 hit check as a client-side scan of returned entries' lines via `oracle_gl_get_journal_entry` on any candidates. The 3rd slice (reverses_entry_id chain) was previously named as a separate filter slice; in the revised wording the agent inspects returned entries' lines for any chained relationship, which is the realistic platform-side trajectory. |
| **No other OE changed** | Verified against the v2 OE file. OE1-OE9 and OE11-OE19 are byte-identical to v2. The renumber-pass artifacts (OE12 cross-references) remain intact. |
| **Delta footprint** | Single OE body revised; no count change; no cross-reference change; no field-level data drift; no scope creep. |

---

## (1) OE Accuracy — Minor B-OE-v2-01 clear-check

### (1a) Verified OE10 wording (verbatim)

> "OE10: Call oracle_gl_list_journal_entries with period_id 'brookfield_FP-2026-05' and min_amount 6328.86 (and a second call with period_id 'brookfield_FP-2026-04' and the same min_amount to sweep for any reversal partner), then inspect each returned entry's lines for any hit on account 210000 against the $6,328.86 figure (use oracle_gl_get_journal_entry on any candidate to read its lines). Confirm zero hits on 210000 across both period slices, no existing FX-revaluation JE already booked against the Acme Research subscription line, and no reverses_entry_id chain on 210000 that would make a corrective redundant. Conclude the GL history also does not corroborate either the FX framing or the duplicate framing, reinforcing the OE9 SAP-absence finding and locking the classification question to Ryan Delgado's sign-off path."

### (1b) Parameter accuracy — verified against `8_Server_Tools_Details.json`

`oracle_gl_list_journal_entries` parameter list (verified):
- `offset` — real
- `limit` — real
- `period_id` — real
- `status` — real
- `prepared_by` — real
- `entry_type` — real
- `min_amount` — real

| OE10 named server-side filter | Real param? |
|---|---|
| `period_id "brookfield_FP-2026-05"` | **YES** |
| `period_id "brookfield_FP-2026-04"` | **YES** |
| `min_amount 6328.86` | **YES** |

| OE10 named client-side approach | Tool used | Real? |
|---|---|---|
| "inspect each returned entry's lines for any hit on account 210000" | client-side scan of `lines[]` array on the entry payload | correct posture |
| "use `oracle_gl_get_journal_entry` on any candidate to read its lines" | `oracle_gl_get_journal_entry` | **YES (real tool)** |

The revised OE10 names ONLY real server-side filters (`period_id`, `min_amount`) and correctly frames the account-210000 hit check as client-side line inspection. The previous `entity_id` and `account_id` overstatements are **gone**. The wording now matches the tool's actual parameter list exactly.

### (1c) Universe ground truth — unchanged from v2

The v2 council verified zero hits across:
- brookfield + FP-2026-05 + line on 210000 + amount $6,328.86 → **0**
- brookfield + FP-2026-04 + line on 210000 + amount $6,328.86 → **0**
- brookfield + `reverses_entry_id` set + line on 210000 → **0**

The revised OE10's expected output ("zero hits on 210000 across both period slices, no existing FX-revaluation JE already booked, and no reverses_entry_id chain on 210000") still matches the verified universe ground truth. The narrative slices have been reorganized (3 slices folded into 2 list-calls + client-side reverses_entry_id inspection on returned payloads) but the expected zero result is unchanged.

### (1d) Minor B-OE-v2-01 status

**CLEARED.** The wording polish recommended in the v2 report has been applied verbatim in spirit: server-side filter naming now matches the real parameter list, the client-side account-filter scan is explicit, and the trajectory still lands on the universe-verified zero result.

### Score — OE Accuracy: **5 / 5** (Minor cleared)

---

## (2) B3 — Tool-call density re-projection

The brief's claim to verify: midpoint stays at ~52 (PASS); the edit didn't change the call count meaningfully.

### Revised OE10 call sizing

| Sub-step | Range | Mid |
|---|---:|---:|
| `oracle_gl_list_journal_entries` FP-2026-05 + min_amount 6328.86 | 1 | 1.0 |
| `oracle_gl_list_journal_entries` FP-2026-04 + min_amount 6328.86 | 1 | 1.0 |
| `oracle_gl_get_journal_entry` on candidate entries returned by the two list calls (min_amount 6328.86 may surface a handful of large entries needing line-level inspection for 210000 hits and reverses_entry_id detail) | 1 - 3 | 2.0 |
| **OE10 total** | **3 - 5** | **4.0** |

**OE10 mid: 4.0** — unchanged from v2's projection. The v3 wording reorganized the sub-step structure but kept the same realistic call shape: 2 list calls + ~2 candidate gets.

### Full density table (unchanged from v2 except confirmation)

| OE | Mid |
|---|---:|
| OE1 | 4.0 |
| OE2 | 1.0 |
| OE3 | 2.0 |
| OE4 | 3.0 |
| OE5 | 2.0 |
| OE6 | 4.0 |
| OE7 | 3.0 |
| OE8 | 1.0 |
| OE9 | 4.0 |
| **OE10** | **4.0** |
| OE11 | 3.5 |
| OE12 | 1.5 |
| OE13 | 1.5 |
| OE14 | 1.5 |
| OE15 | 1.5 |
| OE16 | 1.5 |
| OE17 | 2.0 |
| OE18 | 3.0 |
| OE19 | 0.0 |
| Subtotal | 44.0 |
| Cross-service triangulation buffer | 7.5 |
| **Total projection** | **51.5** |

- **Lower bound estimate:** ~35
- **Midpoint estimate:** ~52 (51.5 rounded up)
- **Upper bound estimate:** ~70

### Updated B3 verdict

**PASS** (midpoint 52, clears 50+ design target). Unchanged from v2. The brief's "midpoint stays at ~52" is **confirmed**. The wording correction did not change the realistic call shape — it just relabeled which filters are server-side vs client-side.

---

## (3) OE Completeness — re-confirmation

Spot-checked the v2 forward-coverage matrix against the v3 OE10 wording:

| Anchor | OE10 coverage | Verdict |
|---|---|---|
| Prompt clause 7 (business_justification must spell out what the support shows) | OE10's GL-history-zero finding is still load-bearing for OE12's business_justification, which still explicitly cites "the Oracle GL history on 210000 in FP-2026-05 and FP-2026-04 returned zero matches for the variance figure." | PASS |
| L1 Latching disambiguation | OE10 still confirms neither framing has a corroborating GL trail. The conclusion text ("locking the classification question to Ryan Delgado's sign-off path") is preserved verbatim. | PASS |
| L8 Multi-link chain extension | 5-hop chain (msg → BL → Slack → SAP → GL history) preserved. OE10 is still the explicit 5th hop. | PASS |
| Pre-staging duplicate-prevention | OE10's reverses_entry_id check is preserved ("no reverses_entry_id chain on 210000 that would make a corrective redundant"). | PASS |

No regression on the v2 forward-coverage matrix. Every prompt clause still maps to at least one OE.

### Score — OE Completeness: **5 / 5** (unchanged from v2)

---

## (4) B4 — Hardness Preservation re-confirmation

| Lever | v2 status | v3 delta | Verdict |
|---|---|---|---|
| **L1 Latching** | PASS — strengthened by OE10 GL-zero | OE10 GL-zero finding preserved verbatim in conclusion text. Routing-to-Ryan posture intact. | PASS (unchanged) |
| **L5 Thread-reply blindness** | PASS | No change to OE7/OE8/OE14. | PASS (unchanged) |
| **L7 Multi-write diversification** | PASS — 7 writes / 7 services | Unchanged. | PASS (unchanged) |
| **L8 Multi-link chain** | PASS — strengthened 4→5 hops | 5th hop (OE10 GL history zero) preserved. The hop is structurally identical (still a GL list + inspect) — only the parameter-naming wording was polished. | PASS (unchanged, still strengthened) |
| **L9 Universe-grounded gotcha (twin)** | PASS | No change to OE4/OE5/OE6/OE16/OE18. | PASS (unchanged) |

**No lever weakened.** L1 and L8 remain strengthened relative to v1. L8's 5-hop chain is fully intact because the OE10 hop is preserved — the wording correction was a polish to the filter labels, not a removal of the hop.

### Score — B4 Hardness Preservation: **5 / 5** (unchanged from v2)

---

## (5) No-regression check on every other OE

Diff-checked every OE against the v2 baseline:

| OE | v3 vs v2 | Drift? |
|---|---|---|
| OE1 | byte-identical | none |
| OE2 | byte-identical | none |
| OE3 | byte-identical | none |
| OE4 | byte-identical | none |
| OE5 | byte-identical | none |
| OE6 | byte-identical | none |
| OE7 | byte-identical | none |
| OE8 | byte-identical | none |
| OE9 | byte-identical | none |
| **OE10** | **revised wording (parameter polish)** | **intended delta only** |
| OE11 | byte-identical | none |
| OE12 | byte-identical (business_justification cites OE10 GL-zero — preserved) | none |
| OE13 | byte-identical (cites OE10 GL-zero — preserved) | none |
| OE14 | byte-identical | none |
| OE15 | byte-identical (cites OE10 GL-zero — preserved) | none |
| OE16 | byte-identical | none |
| OE17 | byte-identical (cites OE10 GL-zero — preserved) | none |
| OE18 | byte-identical | none |
| OE19 | byte-identical | none |

All downstream cross-references to OE10's GL-zero finding (in OE12, OE13, OE15, OE17 business_justification / explanation / email / memo bodies) remain intact and consistent with the revised OE10's conclusion. No cross-reference dangles.

**No regression on any other OE.**

---

## (6) Issue summary (v3 delta)

| ID | Severity | Issue | Status |
|---|---|---|---|
| B-OE-v1-01 | (Minor, v1) | B3 density mid ~48 (THIN_DENSITY) | RESOLVED in v2 |
| B-OE-v1-02 | (Minor, v1) | OE17/OE18 `reminder_get_all_reminders` parenthetical overstatement | RESOLVED in v2 |
| B-OE-v2-01 | (Minor, v2) | OE10 named `entity_id` and `account_id` as server-side filters on `oracle_gl_list_journal_entries`, which only exposes `period_id`, `status`, `prepared_by`, `entry_type`, `min_amount`, `offset`, `limit` | **RESOLVED in v3** — OE10 now uses `period_id` + `min_amount` (both real), and the account-210000 filter is correctly framed as client-side line inspection via `oracle_gl_get_journal_entry` |

**No new issues.** No Major issues. No outstanding Minors.

---

## Exit verdict

**GO** — All four sub-dim scores are at 5/5 or PASS. The v2 Minor wording note on OE10 has been resolved. No regression on any other OE. No new issues introduced by the v3 edit. The L1 latching audit trail and the L8 5-hop multi-link chain remain intact and load-bearing.

---

## Sub-dim scores

| Sub-dim | v2 | v3 | Delta |
|---|---|---|---|
| OE Completeness | 5 / 5 | **5 / 5** | unchanged |
| OE Accuracy | 5 / 5 (with Minor B-OE-v2-01) | **5 / 5 (Minor cleared)** | **Minor cleared** |
| B3 Tool-call density | PASS (mid 52) | **PASS (mid 52)** | unchanged |
| B4 Hardness preservation | 5 / 5 | **5 / 5** | unchanged (L8 still strengthened 4→5 hops) |

**Council B (S2) v3 verdict: GO.**
