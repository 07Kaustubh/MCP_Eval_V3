# Universe Atom Verification Report

**Atoms checked:** 9
**FAIL:** 2
**WARN:** 0

## FAIL
- STOP: account 101000 (claimed role: Cash - Operating) | claim=oracle_gl.ogl_accounts WHERE account_number=101000 | universe-row=NO ROW | account 101000 not found on entity <any>
- STOP: account 110000 (claimed role: Accounts Receivable - Trade) | claim=oracle_gl.ogl_accounts WHERE account_number=110000 | universe-row=NO ROW | account 110000 not found on entity <any>

## Per-atom evidence table

| Atom | Query | Row | Verdict | Severity |
|---|---|---|---|---|
| account 101000 (claimed role: Cash - Operating) | `oracle_gl.ogl_accounts WHERE account_number=101000` | NO ROW | account 101000 not found on entity <any> | FAIL |
| account 110000 (claimed role: Accounts Receivable - Trade) | `oracle_gl.ogl_accounts WHERE account_number=110000` | NO ROW | account 110000 not found on entity <any> | FAIL |
| JE JE-acme_cloud-FP-2026-04-0052 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email steven.perry@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email matthew.li@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email farah.dlamini@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email peter.sanchez@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email marina.soko@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email anita.knowles@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |