# Universe Atom Verification Report

**Atoms checked:** 10
**FAIL:** 1
**WARN:** 0

## FAIL
- STOP: account 102000 (claimed role: Payroll) | claim=oracle_gl.ogl_accounts WHERE account_number=102000 | universe-row=NO ROW | account 102000 not found on entity <any>

## Per-atom evidence table

| Atom | Query | Row | Verdict | Severity |
|---|---|---|---|---|
| account 102000 (claimed role: Payroll) | `oracle_gl.ogl_accounts WHERE account_number=102000` | NO ROW | account 102000 not found on entity <any> | FAIL |
| exception exc_af7274fb658844 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-9FA5DE86AE36 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-FF2DDBF1F0E0 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-72E451657112 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-02C970AEFA7B | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-3F60ED1C7107 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email daniel.jones@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email matthew.li@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email sean.williams@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |