# Universe Atom Verification Report

**Atoms checked:** 11
**FAIL:** 1
**WARN:** 0

## FAIL
- STOP: account 131000 (claimed role: FP-2026-05) | claim=oracle_gl.ogl_accounts WHERE account_number=131000 | universe-row=NO ROW | account 131000 not found on entity <any>

## Per-atom evidence table

| Atom | Query | Row | Verdict | Severity |
|---|---|---|---|---|
| account 131000 (claimed role: FP-2026-05) | `oracle_gl.ogl_accounts WHERE account_number=131000` | NO ROW | account 131000 not found on entity <any> | FAIL |
| exception exc_4d5d3582698946 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| exception exc_a0f77f2a19104e | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-0DEC7D2FD9E6 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-516B536953DA | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-7085321B04EA | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email ben.arinzo@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email daniel.jones@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email emily.adekole@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email andrea.phil@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email jones.harrison@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |