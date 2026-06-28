## 2026-06-27T07:06:04Z
You are a Forensic Auditor.
Working directory: C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass
Your metadata directory is C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/auditor_reconciliation

Task:
Perform a forensic integrity audit on the reconciliation task and the newly generated document:
- `docs/reference/vibs-verified-kildedom-2026-06-27.md`

Perform the following verification checks:
1. Integrity Audit: Check the git status and diff (e.g. run `git status` and `git diff`) to confirm that the canonical documents (ipn-kildebibliotek.md, ipn-samledokument.md, ipn-hovedokument.md) are 100% unmodified. If any modifications are detected, it is an INTEGRITY VIOLATION.
2. Authenticity Audit: Inspect `docs/reference/vibs-verified-kildedom-2026-06-27.md` to ensure that it has been authentically and fully generated according to all requirements in C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/ORIGINAL_REQUEST.md. Ensure there are no dummy/facade placeholders or hardcoded bypasses.
3. Audit Verdict: Report a clear, binary verdict: CLEAN or INTEGRITY VIOLATION. Provide full evidence in your report.

Write your audit report to C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/auditor_reconciliation/audit.md.
Also write your handoff.md in your metadata directory. Report back when done.
