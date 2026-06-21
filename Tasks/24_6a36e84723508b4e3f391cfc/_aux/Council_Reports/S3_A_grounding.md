# Council A — Grounding and Convention (S3 Rubrics)

Task: `24_6a36e84723508b4e3f391cfc` (AP / Vendor Operations — Lena Park, Procurement Officer)
Deliverable: `7_Rubrics.json` (25 rubrics, all outcome, zero process)
Universe today: 2026-06-12 (US/Eastern)
Tool: `explore` sub-agent. Every concrete value re-derived from `_aux/Universe_Split/`.

**VERDICT: GO** (Round 2, after fixes). Round 1 returned BLOCK on two Major atomicity issues (old indices 12 and 14); both are resolved in the current 25-rubric file. Grounding was clean in both rounds.

---

## A1 — Grounding sweep (every concrete value -> FILE:RECORD)

### Dollar amounts
| VALUE | FILE:RECORD |
|---|---|
| $460,556.46 (VaultKey) | `sap_subledger.ap_invoices.json`: `apinv_0f7b328f3be04a9c` (VEN-029-961721) |
| $289,217.86 (CivicSquare) | `sap_subledger.ap_invoices.json`: `apinv_48e7d16bf3814a64` (VEN-024-891664) |
| $108,826.27 (BeaconPay) | `sap_subledger.ap_invoices.json`: `apinv_cfc3542208f14055` (VEN-033-26339) |
| $24,475.25 (TimeLedger) | `sap_subledger.ap_invoices.json`: `apinv_d3019cdcc6ed44b2` (VEN-010-514242) |
| $1,040.63 (Pinecrest) | `sap_subledger.ap_invoices.json`: `apinv_dff20c11abdc495c` (VEN-006-193120) |

### Vendor invoice numbers
| VALUE | FILE:RECORD |
|---|---|
| VEN-029-961721 | `apinv_0f7b328f3be04a9c` |
| VEN-024-891664 | `apinv_48e7d16bf3814a64` |
| VEN-033-26339 | `apinv_cfc3542208f14055` |
| VEN-018-693265 (Clearpoint) | `apinv_99aa0bf007864353` |
| VEN-034-341062 (PensionBridge) | `apinv_3188f63412744768` |
| VEN-005-84026 (AssurePath) | `apinv_7385e55ca9dc4612` |
| VEN-010-514242 | `apinv_d3019cdcc6ed44b2`; also `linear.linear_issues.json`, `email.emails.json`, `messaging.messages.json` |
| VEN-010-693199 (evidence/justification only) | `apinv_9aa666fc03424902`; `issue_0b05ec215a854a439472fb0c6bd3307b`, `issue_08d1ddb3b3c9419faa29e94436004bd8` |
| VEN-006-193120 | `apinv_dff20c11abdc495c` |
| VEN-028-492596 (VerityFile, invoice_date 2026-05-18) | `apinv_4365829f740147af` |
| VEN-012-745157 / -786680 / -730094 (MetroShield, invoice_date 2026-05-31) | `apinv_83e0fb01d65bf324`, `apinv_755ed5b8905d635e`, `apinv_9d60f22d3b80a920` |
| VEN-012-753165 (GraniteRack) | `apinv_6131b7c637aa4b6e`; `issue_e5abbb9af74642eeb10a93426b0bbaa2`, `issue_16b223fecbf14af586d0afa0ce8cc6f4` |

### Document IDs (all classification restricted)
| VALUE | FILE:RECORD |
|---|---|
| doc_eb7cb30c59bd4f03 (acme engagement_letter_addendum) | `records_vault.rv_documents.json` — restricted |
| doc_2d85ac5a698745c5 (acme engagement_change_order) | `records_vault.rv_documents.json` — restricted |
| doc_0036f5b991574808 (northstar engagement_letter) | `records_vault.rv_documents.json` — restricted |

### Linear issue, SOW codes, accounts, channel, emails
| VALUE | FILE:RECORD |
|---|---|
| issue_378874ffeb8f4cb0b0417021f2d3d647 | `linear.linear_issues.json` — "Fix AP routing rule for departed approvers..." |
| SOW-2024-GR-rev3 / SOW-2025-GR-rev1 | `email.emails.json`, `messaging.messages.json`, `linear.linear_issues.json` |
| 210000 (AP - External Vendors) | `oracle_gl.ogl_accounts.json` (all 3 entities); pervasive in AP invoices |
| 219000 (AP - Employee Reimbursements) | `oracle_gl.ogl_accounts.json`; **GraniteRack VEN-012-753165 = `apinv_6131b7c637aa4b6e` is on 219000** |
| C010 / vendor-bills-and-ap | `slack.slack_channels.json` |
| lena.park@ / daniel.jones@ / steven.perry@ / priya.khatri@ brookfieldcpas.com | `contacts.contacts.json` |

### Derived values
| VALUE | DERIVATION |
|---|---|
| ~302 days (CivicSquare) | invoice_date 2025-08-14 -> 2026-06-12 = 302 |
| ~320 days (BeaconPay) | invoice_date 2025-07-27 -> 2026-06-12 = 320 |
| ~338 days (Pinecrest) | invoice_date 2025-07-09 -> 2026-06-12 = 338 |
| 320 / 320 null approver | every `pending_approval` row has `approver: null` |
| 2026-06-19 (reminder) | universe today 2026-06-12 + 7 days |

### Nuance checks
- GraniteRack VEN-012-753165 on account **219000**: CONFIRMED (`apinv_6131b7c637aa4b6e`).
- Three scope docs **restricted** + **zero** access grants for `lena.park@brookfieldcpas.com`: CONFIRMED (no Lena rows in `records_vault.rv_access_grants.json`).

**A1 summary: zero NOT FOUND. Every concrete value in titles and evidence is grounded (directly or via supported derivation).**

---

## A2 — Convention sweep (full 25-rubric pass)

| Check | Result |
|---|---|
| Flat shape `{title, category, justification, evidence}` consistent | PASS (matches sibling live task 23; accepted variant) |
| Agent-centric titles ("The Agent ...") | PASS (all 25) |
| Zero tool function names in titles | PASS |
| No "at least N" in titles | PASS ("at least" appears only in a justification quoting the prompt) |
| `approximately` only on derived ages | PASS (only on ~302 / ~320 / ~338 day counts) |
| `(or similar)` placement (not adjacent to bare id/email/amount) | PASS (Northstar hedge relocated to modify "statement") |
| Outcome > process | PASS (25 / 0) |
| No em / en dashes | PASS |
| Atomicity | PASS (prior Majors cleared, no new violations) |

### Resolution of Round 1 Major issues
- **Issue 1** (old idx 12 — compound bundle VaultKey + BeaconPay): SPLIT into two atomic rubrics (VaultKey largest-dollar-not-most-severe; BeaconPay high-age underweighted by top-dollar). CLEARED.
- **Issue 2** (TimeLedger bundle — credit-memo + VEN-010-693199 disambiguation): de-bundled. Title asserts only the missing-credit-memo / AP classification; VEN-010-693199 disambiguation moved to justification + evidence as judge guidance (the prompt never names VEN-010-693199, so a standalone disambiguation rubric would reach beyond the prompt). CLEARED.

Thematic overlap among the four compound-lens rubrics (method + VaultKey + BeaconPay + CivicSquare) is intentional L1 hardness coverage, not atomicity bundling.

---

## Numbered issue list

**None.**

## VERDICT

**GO.** Grounding clean (zero ungrounded values), convention clean, both Round 1 Major atomicity issues resolved, no new issues introduced.
