# Universe Atom Verification Report

**Atoms checked:** 10
**FAIL:** 2
**WARN:** 0

## FAIL
- STOP: account 105000 (claimed role: IOLTA - Client Trust Account) | claim=oracle_gl.ogl_accounts WHERE account_number=105000 | universe-row=NO ROW | account 105000 not found on entity <any>
- STOP: account 250000 (claimed role: IOLTA Client Trust Liability) | claim=oracle_gl.ogl_accounts WHERE account_number=250000 | universe-row=NO ROW | account 250000 not found on entity <any>

## Per-atom evidence table

| Atom | Query | Row | Verdict | Severity |
|---|---|---|---|---|
| account 105000 (claimed role: IOLTA - Client Trust Account) | `oracle_gl.ogl_accounts WHERE account_number=105000` | NO ROW | account 105000 not found on entity <any> | FAIL |
| account 250000 (claimed role: IOLTA Client Trust Liability) | `oracle_gl.ogl_accounts WHERE account_number=250000` | NO ROW | account 250000 not found on entity <any> | FAIL |
| JE JE-northstar_legal-FP-2026-05-0061 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-7C2A9F4E1B83 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email owen.mercer@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email blue.evans@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email elita.moore@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email daniel.jones@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email edith.banda@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email matthew.li@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |