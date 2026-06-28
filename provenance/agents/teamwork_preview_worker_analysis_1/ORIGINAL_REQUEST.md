## 2026-06-27T07:26:12Z

You are teamwork_preview_worker. Your working directory is C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/teamwork_preview_worker_analysis_1.
Your task is to:
1. Write a Python script using pandas that reads the target documents, tokenizes the text, and calculates the frequencies of:
   - AI/Tech buzzwords (e.g., AI, kunstig intelligens, agent, maskinlæring, algoritme, llm, gpt, neural, deep learning).
   - Complex consulting/academic jargon (e.g., synergi, transformasjon, optimalisering, robust, holistisk, digitalisering, siloer, syntesen, robusthet, operasjonalisert).
   - Complex sentences (e.g., sentences with length > 25 words) or long words (e.g., words with length > 15 characters).
   Save the script to the scratch directory at:
   `C:/Users/larse/.gemini/antigravity-cli/brain/808bc8bb-a252-43c8-843a-e502f888be0a/scratch/word_analysis.py`

2. Run the script to analyze the following files:
   - `docs/reference/ipn-samledokument.md`
   - `docs/reference/ipn-hovedokument.md`

3. Generate a unified report at `docs/reference/vibs-verified-språkanalyse-2026-06-27.md` that contains:
   - A summary table of extracted terms, their category (AI buzzword, jargon, complexity), and frequency.
   - A comparison check against `claude-guardrails.md` rules (read the explorer's analysis report at `C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/.agents/teamwork_preview_explorer_analysis_1/analysis.md` for input).
   - Concrete "Before/After" rewrite recommendations for the complex passages and guardrail violations.

Ensure that NO changes are made to the analyzed source documents.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Document your steps and write a handoff report at `handoff.md` in your working directory.
Send a message back to the orchestrator (conversation ID: 518ca07a-8864-409d-b705-b717f827bc42) when completed with a summary of execution and output paths.
