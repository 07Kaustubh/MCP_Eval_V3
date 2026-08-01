# Universe Atom Verification Report

**Atoms checked:** 14
**FAIL:** 2
**WARN:** 1

## FAIL
- STOP: account 230000 (claimed role: Confirm) | claim=oracle_gl.ogl_accounts WHERE account_number=230000 | universe-row=NO ROW | account 230000 not found on entity <any>
- STOP: account 103000 (claimed role: Cash) | claim=oracle_gl.ogl_accounts WHERE account_number=103000 | universe-row=NO ROW | account 103000 not found on entity <any>

## WARN
- 'Confirm Daniel never responded' | 'Confirm Daniel' has no sent emails to walk a thread from — cannot verify the no-response claim. Re-check the actual claim or rename the persona.

## Per-atom evidence table

| Atom | Query | Row | Verdict | Severity |
|---|---|---|---|---|
| account 230000 (claimed role: Confirm) | `oracle_gl.ogl_accounts WHERE account_number=230000` | NO ROW | account 230000 not found on entity <any> | FAIL |
| account 103000 (claimed role: Cash) | `oracle_gl.ogl_accounts WHERE account_number=103000` | NO ROW | account 103000 not found on entity <any> | FAIL |
| 'Confirm Daniel never responded' | `email.emails WHERE from contains 'Confirm Daniel'` | NO SENT EMAILS | 'Confirm Daniel' has no sent emails to walk a thread from — cannot verify the no-response claim. Re-check the actual claim or rename the persona. | WARN |
| exception exc_652c0931bb2546 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| exception exc_151b0bee7e374e | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-2E691B2E18FA | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| recon BL-1F548113B049 | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email tom.chang@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email julia.vance@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email daniel.jones@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email james.randall@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email hannah.grant@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email william.white@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |
| email matthew.li@brookfieldcpas.com | `presence search in 3_UniverseDataForThisTask.json` | found | present in universe | PASS |