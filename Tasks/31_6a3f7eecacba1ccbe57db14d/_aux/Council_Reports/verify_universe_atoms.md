# Universe Atom Verification Report

**Atoms checked:** 8
**FAIL:** 5
**WARN:** 0

## FAIL
- STOP: account 153000 (claimed role: ROU) | claim=oracle_gl.ogl_accounts WHERE account_number=153000 | universe-row=NO ROW | account 153000 not found on entity <any>
- STOP: account 230000 (claimed role: Income Tax Payable) | claim=oracle_gl.ogl_accounts WHERE account_number=230000 | universe-row=NO ROW | account 230000 not found on entity <any>
- STOP: account 230000 (claimed role: Income Tax Payable) | claim=oracle_gl.ogl_accounts WHERE account_number=230000 AND entity_id=northstar_legal | universe-row=NO ROW | account 230000 not found on entity northstar_legal
- STOP: account 230000 (claimed role: Income Tax Payable) | claim=oracle_gl.ogl_accounts WHERE account_number=230000 | universe-row=NO ROW | account 230000 not found on entity <any>
- STOP: account 230000 (claimed role: Income Tax Payable) | claim=oracle_gl.ogl_accounts WHERE account_number=230000 AND entity_id=northstar_legal | universe-row=NO ROW | account 230000 not found on entity northstar_legal

## Per-atom evidence table

| Atom | Query | Row | Verdict | Severity |
|---|---|---|---|---|
| account 153000 (claimed role: ROU) | `oracle_gl.ogl_accounts WHERE account_number=153000` | NO ROW | account 153000 not found on entity <any> | FAIL |
| account 230000 (claimed role: Income Tax Payable) | `oracle_gl.ogl_accounts WHERE account_number=230000` | NO ROW | account 230000 not found on entity <any> | FAIL |
| account 230000 (claimed role: Income Tax Payable) | `oracle_gl.ogl_accounts WHERE account_number=230000 AND entity_id=northstar_legal` | NO ROW | account 230000 not found on entity northstar_legal | FAIL |
| account 230000 (claimed role: Income Tax Payable) | `oracle_gl.ogl_accounts WHERE account_number=230000` | NO ROW | account 230000 not found on entity <any> | FAIL |
| account 230000 (claimed role: Income Tax Payable) | `oracle_gl.ogl_accounts WHERE account_number=230000 AND entity_id=northstar_legal` | NO ROW | account 230000 not found on entity northstar_legal | FAIL |
| email julia.vance@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email william.white@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email hannah.grant@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |