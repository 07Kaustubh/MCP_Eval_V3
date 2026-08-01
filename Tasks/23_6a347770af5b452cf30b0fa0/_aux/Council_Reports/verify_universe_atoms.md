# Universe Atom Verification Report

**Atoms checked:** 13
**FAIL:** 1
**WARN:** 0

## FAIL
- STOP: account 119000 (claimed role: Northstar) | claim=oracle_gl.ogl_accounts WHERE account_number=119000 AND entity_id=northstar_legal | universe-row=NO ROW | account 119000 not found on entity northstar_legal

## Per-atom evidence table

| Atom | Query | Row | Verdict | Severity |
|---|---|---|---|---|
| account 119000 (claimed role: Northstar) | `oracle_gl.ogl_accounts WHERE account_number=119000 AND entity_id=northstar_legal` | NO ROW | account 119000 not found on entity northstar_legal | FAIL |
| JE JE-northstar_legal-FP-2026-05-0001 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| JE JE-northstar_legal-FP-2026-05-0020 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| JE JE-northstar_legal-FP-2026-05-0051 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| JE JE-northstar_legal-FP-2026-05-0002 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| vendor VEN-030-A | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| vendor VEN-030 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| vendor VEN-030-736427 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| vendor VEN-030-B | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| vendor VEN-030-353041 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| vendor VEN-030-817856 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email george.mcadam@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email daniel.jones@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |