# Council B — Adversarial QC — S2 Oracle Events (v4 delta re-review, post-AUDIT)

**Task:** `Tasks/28_6a390e6b331d1ed9022a9f7c`
**Council role:** B (adversarial), delta-only re-review
**Phase:** S2 — Oracle Events
**OE file:** `6_Oracle_Events.txt` (19 OEs, unchanged count from v3)
**Reviewer posture:** read-only; delta-scope only — verify the four AUDIT-named MAJOR/MINOR wording fixes on OE12 / OE14 are cleared, the OE13 polish is cleared, OE8 untouched-and-still-correct, B3 density still clears 50+, Completeness and Hardness Preservation unchanged, no regression on any other OE.
**Prior reports:**
- `_aux/Council_Reports/S2_B_adversarial_v3.md` — v3 verdict was GO (all sub-dims 5/5 / PASS).
- `_aux/Council_Reports/AUDIT_oe.md` — strict veteran AUDIT verdict was REVISE on parameter-overstatement defects in OE12 (entity_id / entry_date / missing description) and OE14 (related_journal_entry_id / corrective_journal_entry_id / resolution_summary), plus a minor OE13 polish (on id → recon_id). Audit explicitly cited this as the same defect-class Council A v2 caught on OE10 but missed on the write-tool OEs.

---

## Delta summary (v4)

| Change | Description |
|---|---|
| **OE12 entity_id overstatement removed** | The required-fields list no longer names `entity_id "brookfield"`. Added explicit guard: "Entity is inferred from the period_id prefix; do not pass a separate entity_id." Matches the OE10 v3 fix pattern exactly. |
| **OE12 entry_date → posting_date** | The date parameter is now correctly named `posting_date`, matching the real tool spec. |
| **OE12 description added** | The required-fields list now includes `description` ("description naming the corrective FX adjustment against the BL recon"). The optional `business_justification` clause is preserved separately. |
| **OE14 unwritable-field overstatement removed** | The "for example by populating related_journal_entry_id or corrective_journal_entry_id" parenthetical is gone. OE14 now names only the writable cross-reference paths: `proposed_resolution` (extend existing text) or `supporting_evidence` (append reference object). |
| **OE14 resolution_summary mention removed** | The "resolution_summary must remain null" line is gone. The disposition-preservation discipline is now carried by "Do NOT pass the state parameter (the existing 'awaiting_approval' state must be preserved so Ryan still owns the disposition). Do NOT call blackline_resolve_exception." |
| **OE13 recon_id polish applied** | OE13 now reads "with recon_id 'BL-516B536953DA'" instead of "on id 'BL-516B536953DA'". Matches the OE10 v3 precision standard. |
| **OE8 untouched** | OE8 names `slack_conversations_replies` with `channel_id "C005"` + `thread_ts "1779891480.000000"`. Both are real parameters on the tool spec. No defect was named in AUDIT; no edit needed; no edit observed. The brief listed OE8 as a sanity-check target only. |
| **No other OE changed** | Verified against the v3 baseline. OE1–OE7, OE9–OE11, OE15–OE19 are byte-identical to v3. All downstream cross-references to OE12 (in OE13, OE14, OE15, OE16, OE17) still resolve correctly. |
| **Delta footprint** | Three OE bodies revised (OE12 + OE13 + OE14); no count change; no cross-reference change; no scope creep. |

---

## (1) OE Accuracy — AUDIT MAJOR/MINOR clear-check

### (1a) AUDIT issue A-OE12-01 — `entity_id` overstatement

**AUDIT finding:** OE12 listed `entity_id "brookfield"` as a required JE field; tool exposes no `entity_id`.

**v4 OE12 verbatim (required-fields clause):**
> "Required parameters: period_id 'brookfield_FP-2026-05', posting_date on or before '2026-06-12' within the period, description naming the corrective FX adjustment against the BL recon, and lines (array). Entity is inferred from the period_id prefix; do not pass a separate entity_id."

**Verified against `8_Server_Tools_Details.json` for `oracle_gl_create_journal_entry`:**

Required params: `period_id`, `posting_date`, `description`, `lines`. ✅
Optional params: `entry_type`, `is_standard_entry`, `source_module`, `business_justification`, `attachments`, `prepared_by`.
**`entity_id` does not exist on the tool.**

OE12's required list now names exactly `period_id`, `posting_date`, `description`, `lines` — a 4-for-4 match with the real required-params set. The "do not pass a separate entity_id" guard is the same negative-instruction pattern OE10 v3 established to prevent the agent from inferring an unwritable parameter from the universe schema.

**Status: CLEARED.**

### (1b) AUDIT issue A-OE12-02 — `entry_date` → `posting_date`

**AUDIT finding:** OE12 named `entry_date` as the date parameter; real param is `posting_date`.

**v4 OE12 verbatim:** "posting_date on or before '2026-06-12' within the period"

**Verified:** `posting_date` is the required date parameter on `oracle_gl_create_journal_entry`.

**Status: CLEARED.**

### (1c) AUDIT issue A-OE12-03 — `description` missing from required-list

**AUDIT finding:** OE12 omitted `description` (required string param) from the required-fields enumeration.

**v4 OE12 verbatim:** "description naming the corrective FX adjustment against the BL recon"

**Verified:** `description` is now in the required-fields enumeration. It is correctly distinguished from the separately-treated optional `business_justification` clause later in the OE body.

**Status: CLEARED.**

### (1d) AUDIT issue A-OE14-01 — unwritable-fields overstatement

**AUDIT finding:** OE14 named `related_journal_entry_id` and `corrective_journal_entry_id` as cross-reference fields populatable via `blackline_update_exception`; neither is a writable parameter.

**v4 OE14 verbatim (cross-reference clause):**
> "to record a cross-reference to the staged JE through the writable parameters the tool exposes. The cross-reference must name the JE id from OE12 in proposed_resolution (extend the existing 'Post a corrective JE in oracle_gl with source_module=manual and reference this exception_id in the business_justification. Re-run recon afterwards.' text to name the staged JE id, or append the JE id via supporting_evidence as a reference object)."

**Verified against `8_Server_Tools_Details.json` for `blackline_update_exception`:**

Writable params: `exception_id`, `root_cause`, `supporting_evidence`, `financial_impact`, `sox_implications`, `proposed_resolution`, `state`, `actor`.

OE14 v4 names only `proposed_resolution` and `supporting_evidence` — both are real writable params. The unwritable `related_journal_entry_id` / `corrective_journal_entry_id` parenthetical is **gone**. The introductory phrase "through the writable parameters the tool exposes" explicitly signals the discipline to the agent.

**Status: CLEARED.**

### (1e) AUDIT issue A-OE14-02 — `resolution_summary` mention

**AUDIT finding:** OE14 said "resolution_summary must remain null"; `resolution_summary` is not a writable param via `blackline_update_exception`.

**v4 OE14 verbatim (disposition-preservation clause):**
> "Do NOT pass the state parameter (the existing 'awaiting_approval' state must be preserved so Ryan still owns the disposition). Do NOT call blackline_resolve_exception. The user explicitly asked not to step on Ryan's disposition."

The `resolution_summary` reference is removed. Disposition-preservation discipline is now carried by:
(a) the `state` param negative-instruction ("Do NOT pass the state parameter"),
(b) the existing-state preservation note ("the existing 'awaiting_approval' state must be preserved"),
(c) the explicit forbid on `blackline_resolve_exception`.

This is a tighter and more accurate articulation than the v3 wording — it instructs the agent on the actual writable param (`state`) it should NOT touch, rather than on a non-writable field name.

**Status: CLEARED.**

### (1f) AUDIT issue A-OE13-01 — `recon_id` polish

**AUDIT finding:** OE13 said "on id 'BL-516B536953DA'"; the tool's identifier param is `recon_id`.

**v4 OE13 verbatim (opener):**
> "Call blackline_update_reconciliation_variances with recon_id 'BL-516B536953DA' and a fresh variance_explanations array (the tool replaces the existing list)."

Now uses `recon_id` explicitly. Matches the OE10 v3 precision standard.

**Status: CLEARED.**

### (1g) OE8 — sanity check (brief listed as a fix target)

**Brief listing:** OE8 was named in the brief's "wording fixes applied to OE8/OE12/OE13/OE14" enumeration.

**AUDIT_oe.md treatment:** OE8 was NOT named in the AUDIT issue table. No defect was identified.

**v4 OE8 verbatim (opener):**
> "Call slack_conversations_replies with channel_id 'C005' and thread_ts '1779891480.000000' to pull the two thread replies."

**Verified against tool spec for `slack_conversations_replies`:** `channel_id` and `thread_ts` are real required params. The string values (`"C005"`, `"1779891480.000000"`) match the universe ground truth (C005 = #monthly-close-coordination; the Ben Arinzo parent thread on 2026-05-27 14:18 UTC). Hannah's reply ts (`1779895920.000000`) and Daniel's reply ts (`1779901680.000000`) are still correctly named in the OE body — verified against the universe split's `slack_messages` table.

OE8 is correct as-is. No edit was needed; none observed. The brief's inclusion of OE8 was a sanity-check ask, not a defect ask.

**Status: NO-OP (correct in v3, correct in v4).**

### (1h) AUDIT defect-class re-sweep — any other write-tool OE with the same flavor?

AUDIT explicitly framed the OE12 / OE14 defects as the same parameter-overstatement defect-class Council A v2 caught on OE10. To be thorough, I re-checked every write-tool OE (OE12 through OE18) against `8_Server_Tools_Details.json`:

| OE | Tool | Params named in OE | All real? |
|---|---|---|---|
| OE12 | `oracle_gl_create_journal_entry` | `period_id`, `posting_date`, `description`, `lines`, `source_module`, `business_justification` | ✅ 6/6 |
| OE13 | `blackline_update_reconciliation_variances` | `recon_id`, `variance_explanations` | ✅ 2/2 |
| OE14 | `blackline_update_exception` | `exception_id`, `proposed_resolution`, `supporting_evidence`, `state` (negative instruction) | ✅ 4/4 |
| OE15 | `email_send_email` | (recipient/cc fields named in agent-voice + the format-card-correct `content` not `body`) | ✅ |
| OE16 | `slack_conversations_add_message` | `channel_id`, `payload` (not `text`, not `content`) | ✅ |
| OE17 | `records_vault_upload_document` | `kind`, `retention_policy_code`, `classification`, `title`, `content_b64` | ✅ 5/5 |
| OE18 | `reminder_delete_reminder` + `reminder_add_reminder` | `reminder_id`; `title`, `description`, `due_datetime` | ✅ |

No remaining parameter-overstatement defect across the write surface. The AUDIT-flagged class is fully resolved.

### Score — OE Accuracy: **5 / 5** (all four AUDIT issues cleared, plus the OE13 minor polish; no remaining overstatements on the write surface)

---

## (2) B3 — Tool-call density re-projection (wording fixes do not change call counts)

The brief's claim to verify: midpoint stays at ~52 (PASS); the AUDIT wording fixes do not change call counts.

### Per-OE delta on the three edited OEs

| OE | v3 mid | v4 mid | Delta | Why |
|---|---:|---:|---:|---|
| **OE12** | 1.5 | 1.5 | 0 | The edit changed the required-fields enumeration and renamed `entry_date`→`posting_date`. The agent still makes exactly one `oracle_gl_create_journal_entry` call (with possible parameter-validation retry on the same call shape). Call count unchanged. |
| **OE13** | 1.5 | 1.5 | 0 | The edit relabeled `on id` → `with recon_id`. The agent still makes exactly one `blackline_update_reconciliation_variances` call (with possible retry). Call count unchanged. |
| **OE14** | 1.5 | 1.5 | 0 | The edit removed the unwritable-fields parenthetical and reframed the disposition-preservation clause around the `state` param. The agent still makes exactly one `blackline_update_exception` call. Call count unchanged. |

### Full density table (unchanged from v3)

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
| OE10 | 4.0 |
| OE11 | 3.5 |
| **OE12** | **1.5** |
| **OE13** | **1.5** |
| **OE14** | **1.5** |
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

**PASS** (midpoint 52, clears 50+ design target). Unchanged from v3. The brief's "midpoint stays at ~52" is **confirmed**. The AUDIT wording fixes are pure parameter-list polish — they correct what the agent should NAME in its tool call payloads but do not change WHICH tool calls it makes or HOW MANY times.

---

## (3) OE Completeness — re-confirmation

Spot-checked the v3 forward-coverage matrix against the v4 OE12 / OE13 / OE14 wording:

| Anchor | v4 coverage | Verdict |
|---|---|---|
| Prompt clause "Stage the entry in the right place" | OE12 still calls `oracle_gl_create_journal_entry` against `period_id "brookfield_FP-2026-05"`. The required-fields cleanup made the OE MORE complete (added `description` which v3 had omitted), not less. | PASS (strengthened) |
| Prompt clause "Update the recon's variance notes" | OE13 still calls `blackline_update_reconciliation_variances`. The `recon_id` parameter polish is precision-only; all variance-explanation content requirements preserved. | PASS |
| Prompt clause "add the same reference into the exception" | OE14 still calls `blackline_update_exception` and still cross-references the JE id from OE12. Only the unwritable-field overstatement is removed; the cross-reference intent is intact via the `proposed_resolution` / `supporting_evidence` realistic paths. | PASS |
| Prompt clause "Don't resolve the exception" | OE14 still forbids `blackline_resolve_exception` and now also forbids passing the `state` param. The disposition-preservation discipline is stronger in v4 than in v3 because it targets the actual writable param (`state`) rather than a non-writable field name (`resolution_summary`). | PASS (strengthened) |
| L1 Latching evidence | The "open classification question" language in OE12's `business_justification` clause is byte-identical to v3. The L1 latching audit trail is intact. | PASS (unchanged) |
| L7 Multi-write diversification | Seven writes across seven services preserved: OE12 (oracle_gl), OE13 (blackline recon), OE14 (blackline exception), OE15 (email), OE16 (slack), OE17 (records vault), OE18 (reminder). No write removed; no write added. | PASS (unchanged) |

No regression on the v3 forward-coverage matrix. Every prompt clause still maps to at least one OE. Two clauses (description completeness, disposition-preservation) are now MORE precisely captured.

### Score — OE Completeness: **5 / 5** (unchanged from v3)

---

## (4) B4 — Hardness Preservation re-confirmation

| Lever | v3 status | v4 delta | Verdict |
|---|---|---|---|
| **L1 Latching** | PASS (strengthened from v1, audit trail intact) | OE12 `business_justification` text byte-identical; OE14 cross-reference intent preserved (proposed_resolution / supporting_evidence still name the JE from OE12); the "open classification question" language is unchanged across OE12 / OE15 / OE17. | PASS (unchanged) |
| **L5 Thread-reply blindness** | PASS | OE7 / OE8 byte-identical to v3. Hannah's reply ts (1779895920.000000) and Daniel's reply ts (1779901680.000000) still named. VEN-441207 evidence trail still surfaced. | PASS (unchanged) |
| **L7 Multi-write diversification** | PASS — 7 writes / 7 services | All seven writes preserved. No new write added; no write removed. | PASS (unchanged) |
| **L8 Multi-link chain** | PASS (strengthened from v2's 4→5 hops) | All five hops preserved (msg OE1 → BL OE3 → Slack OE7/OE8 → SAP OE9 → GL OE10). OE10 unchanged. | PASS (unchanged) |
| **L9 Universe-grounded gotcha (twin)** | PASS | OE4 / OE5 / OE6 / OE17 byte-identical. Vault-phantom zero-match (OE6), FP-2026-06 future-status (OE4), AICPA_SQMS_7Y retention-not-FIRM_INTERNAL (OE17) all preserved. | PASS (unchanged) |

**No lever weakened.** L1 latching, L7 multi-write, L8 multi-link chain, and L9 universe gotcha (twin) are all intact. The AUDIT fixes did not touch any hardness-load-bearing surface — they corrected parameter naming on tool calls that the levers ride through, not the lever conclusions themselves.

### Score — B4 Hardness Preservation: **5 / 5** (unchanged from v3)

---

## (5) No-regression check on every other OE

Diff-checked every OE against the v3 baseline:

| OE | v4 vs v3 | Drift? |
|---|---|---|
| OE1 | byte-identical | none |
| OE2 | byte-identical | none |
| OE3 | byte-identical | none |
| OE4 | byte-identical | none |
| OE5 | byte-identical | none |
| OE6 | byte-identical | none |
| OE7 | byte-identical | none |
| OE8 | byte-identical (brief sanity-check target; no defect; no edit) | none |
| OE9 | byte-identical | none |
| OE10 | byte-identical (already corrected in v3) | none |
| OE11 | byte-identical | none |
| **OE12** | **AUDIT fixes applied (entity_id removed, entry_date → posting_date, description added)** | **intended delta only** |
| **OE13** | **AUDIT polish applied (`on id` → `with recon_id`)** | **intended delta only** |
| **OE14** | **AUDIT fixes applied (unwritable-fields parenthetical removed, resolution_summary mention removed, state-param negative-instruction added)** | **intended delta only** |
| OE15 | byte-identical (cross-references "JE id from OE12" still resolve) | none |
| OE16 | byte-identical (cross-references "staged JE id from OE12" still resolve) | none |
| OE17 | byte-identical (cross-references "staged JE id" still resolve) | none |
| OE18 | byte-identical | none |
| OE19 | byte-identical (final-paragraph posture preserved) | none |

All downstream cross-references to OE12's staged JE id (in OE13, OE14, OE15, OE16, OE17) remain intact and consistent with the revised OE12's create call. No cross-reference dangles. No new tool token introduced anywhere. No tool token removed anywhere.

**No regression on any other OE.**

---

## (6) Issue summary (v4 delta)

| ID | Severity | Issue | Status |
|---|---|---|---|
| B-OE-v1-01 | (Minor, v1) | B3 density mid ~48 (THIN_DENSITY) | RESOLVED in v2 |
| B-OE-v1-02 | (Minor, v1) | OE17/OE18 `reminder_get_all_reminders` parenthetical overstatement | RESOLVED in v2 |
| B-OE-v2-01 | (Minor, v2) | OE10 named `entity_id` / `account_id` as server-side filters | RESOLVED in v3 |
| A-OE12-01 | (MAJOR, AUDIT) | OE12 named `entity_id` as required JE field | **RESOLVED in v4** |
| A-OE12-02 | (MAJOR, AUDIT) | OE12 named `entry_date` as date parameter | **RESOLVED in v4** (now `posting_date`) |
| A-OE12-03 | (MAJOR, AUDIT) | OE12 omitted `description` from required-fields list | **RESOLVED in v4** |
| A-OE14-01 | (MAJOR, AUDIT) | OE14 named `related_journal_entry_id` / `corrective_journal_entry_id` as writable | **RESOLVED in v4** (only `proposed_resolution` / `supporting_evidence` named) |
| A-OE14-02 | (MINOR, AUDIT) | OE14 named `resolution_summary` (non-writable) | **RESOLVED in v4** (replaced by `state`-param negative-instruction) |
| A-OE13-01 | (MINOR, AUDIT) | OE13 said "on id" instead of `recon_id` | **RESOLVED in v4** |

**No new issues.** No Major issues. No outstanding Minors. The AUDIT-named defect-class (parameter overstatement on write-tool OEs) is fully resolved across OE12, OE13, OE14, and re-swept clean on OE15, OE16, OE17, OE18.

---

## Exit verdict

**GO** — All four sub-dim scores are at 5/5 or PASS. All four AUDIT-named MAJOR / MINOR issues on OE12 / OE14 are cleared. The OE13 polish is applied. OE8 is correct as-is (brief sanity-check target only, no defect existed). No regression on any other OE. No new issues introduced by the v4 edits. L1 latching audit trail, L7 multi-write seven-service spread, L8 5-hop multi-link chain, and L9 universe-gotcha twin all remain intact and load-bearing. The OE phase is ready to clear AUDIT (STRICT) and move to S3.

---

## Sub-dim scores

| Sub-dim | v3 | v4 | Delta |
|---|---|---|---|
| OE Completeness | 5 / 5 | **5 / 5** | unchanged (OE12 description-completeness strengthened) |
| OE Accuracy | 5 / 5 (audit later flagged 3 due to overstatements) | **5 / 5 (all AUDIT issues cleared)** | **MAJOR/MINOR issues cleared** |
| B3 Tool-call density | PASS (mid 52) | **PASS (mid 52)** | unchanged (wording fixes do not change call counts) |
| B4 Hardness preservation | 5 / 5 | **5 / 5** | unchanged (L1 + L8 still strengthened) |

**Council B (S2) v4 verdict: GO.**
