## 2026-08-02T21:40:08Z

<USER_REQUEST>
You are the Forensic Auditor for Chapter K3 candidate note.

**Working Directory:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\auditor_k3_integrity_1`
**Project Root:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified`
**Target File to Audit:** `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\docs\reference\prosjektbeskrivelse\k3-forskning-sannhetsserum-v0.5.md`

**Task Description:**
1. Write `progress.md` inside `.agents/auditor_k3_integrity_1/` immediately as your liveness signal.
2. Read `C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\ORIGINAL_REQUEST.md`.
3. Perform a comprehensive forensic integrity audit on `k3-forskning-sannhetsserum-v0.5.md`:
   - **Authenticity check**: Ensure the document contains genuine, fully articulated Norwegian prose and academic citations. Check that there are no hardcoded fake test results, no dummy placeholders (e.g. `[TODO]`, `TBD`, `[insert link]`), and no empty sections.
   - **Structure & File Path check**: Verify that the document is written to `docs/reference/prosjektbeskrivelse/k3-forskning-sannhetsserum-v0.5.md` and follows valid markdown structure.
   - **Citation & Evidence integrity**: Verify that citations correspond accurately to the kildebibliotek and kildedom without fabrication.
   - **Audit Verdict**: Assign explicit verdict `CLEAN` or `INTEGRITY VIOLATION`.
4. Save your full audit evidence report in `.agents/auditor_k3_integrity_1/audit_report.md`.
5. Write your handoff report at `.agents/auditor_k3_integrity_1/handoff.md` with explicit Verdict: `CLEAN` or `INTEGRITY VIOLATION`.
6. Send a message to caller (Recipient: parent, id: fd91f410-8386-467d-b768-e912e84738a6) reporting your audit verdict and findings.
</USER_REQUEST>
