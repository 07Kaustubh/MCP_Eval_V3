# REVIEW Dismissed Findings

Findings raised by Council A / B / FINAL that did NOT survive per-task universe verification, and therefore were NOT added to `changes.md`.

## Dismissed

1. **"Lena Park is not a valid persona for AP triage."**
 - Source: persona-fit lens, Council B.
 - Check: `_aux/Universe_Index/entities_personas.md` confirms Lena Park exists with email `lena.park@brookfieldcpas.com`, role `Procurement Officer`. Procurement Officer is adjacent to AP / vendor relationships and the prompt's "PO side to unblock things" line frames the persona accurately.
 - Disposition: dismissed. Persona fit scores 4, not 1-2.

2. **"Records Vault retention code mismatch - prompt assumes long-term retention."**
 - Source: groundedness lens, Council A.
 - Check: the prompt does not mention retention codes. The check was speculative.
 - Disposition: dismissed.

3. **"Tool name 'SAP' in prompt is a hard linter block."**
 - Source: strict-language lens, Council B.
 - Check: `Reference/Linter_Playbook.md` flags **tool names** (per `8_Server_Tools_Details.json`) and explicit tool / service IDs. "SAP" is a generic system name, not a tool name. Validator did not flag it. Soft demerit, not a blocker.
 - Disposition: dismissed as a fail; noted as a soft style miss in the prompt scoresheet (scored 4, not 1).

4. **"Daniel Jones / Steven Perry references in prompt may be hallucinated."**
 - Source: groundedness lens.
 - Check: Both exist in `entities_personas.md`. Daniel Jones is Accounts Manager, Steven Perry is Managing Partner. Approval-tier framing matches.
 - Disposition: dismissed.
