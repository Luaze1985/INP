## 2026-06-27T07:24:55Z

You are teamwork_preview_explorer. Your working directory is C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/teamwork_preview_explorer_analysis_1.
Your task is to analyze the target documents:
1. `docs/reference/ipn-samledokument.md`
2. `docs/reference/ipn-hovedokument.md`

Compare their content against the style, clarity, and consistency standards defined in `docs/reference/claude-guardrails.md`.

Specifically:
- Scan the documents and identify occurrences of:
  - AI buzzwords (e.g., AI, kunstig intelligens, agent, maskinlæring, algoritme, llm, gpt, neural, deep learning)
  - Jargon (e.g., synergi, transformasjon, optimalisering, robust, holistisk, digitalisering)
  - Complex sentences and long words
- Check if there are violations of the guardrails, e.g., product status (is MVP presented as finished?), banker/finance terms, partner naming/status (e.g., NorDan LoI status, Tirna Fagskole type), or other rules.
- Draft recommendations for rewriting complex passages or fixing guardrail violations.
- Document all findings in `analysis.md` and write a handoff report at `handoff.md` in your working directory.
- Send a message back to the orchestrator (conversation ID: 518ca07a-8864-409d-b705-b717f827bc42) when completed with a summary of findings.
DO NOT modify any analyzed source documents.
