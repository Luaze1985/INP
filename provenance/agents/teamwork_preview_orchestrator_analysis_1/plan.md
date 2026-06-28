# Execution Plan - Språkanalyse (Word and Semantic Analysis)

This plan coordinates the text and semantic analysis of Vibs IPN application documents.

## Scope & Requirements
- **R1**: Write Python/Pandas analysis script at `C:/Users/larse/.gemini/antigravity-cli/brain/808bc8bb-a252-43c8-843a-e502f888be0a/scratch/word_analysis.py`
- **R2**: Analyze target documents: `docs/reference/ipn-samledokument.md` and `docs/reference/ipn-hovedokument.md`
- **R3**: Compare against style, clarity, and consistency standards in `docs/reference/claude-guardrails.md`
- **R4**: Generate a unified report at `docs/reference/vibs-verified-språkanalyse-2026-06-27.md`
- **R5**: No modifications to the analyzed source documents.

## Milestones & Workflow
We will use a direct Project Pattern cycle: Explorer -> Worker -> Reviewer -> Auditor.

### Milestone 1: Exploration
- **Role**: `teamwork_preview_explorer`
- **Tasks**:
  - Scan the target files (`ipn-samledokument.md`, `ipn-hovedokument.md`) and guardrails (`claude-guardrails.md`) to identify specific occurrences of AI buzzwords, jargon, and complex structures.
  - Draft lists of keywords to extract.
  - Formulate initial rewrite recommendations.
- **Deliverable**: `analysis.md` in explorer's folder.

### Milestone 2: Implementation
- **Role**: `teamwork_preview_worker`
- **Tasks**:
  - Write `word_analysis.py` to the designated path.
  - Execute the script to count frequency of buzzwords, jargon, and long sentences/words.
  - Draft the final report `docs/reference/vibs-verified-språkanalyse-2026-06-27.md` with:
    - Summary frequency table
    - Comparison with `claude-guardrails.md`
    - Before/After recommendations
- **Deliverable**: `changes.md` and `handoff.md` in worker's folder.

### Milestone 3: Review
- **Role**: `teamwork_preview_reviewer`
- **Tasks**:
  - Verify script functionality and review the quality of the report.
  - Check alignment with all R1-R4 requirements.
- **Deliverable**: `review.md` in reviewer's folder.

### Milestone 4: Forensic Audit
- **Role**: `teamwork_preview_auditor`
- **Tasks**:
  - Perform static analysis and run the python script.
  - Run `git status` check to verify that no source documents were modified.
- **Deliverable**: `audit.md` in auditor's folder.

### Milestone 5: Synthesis & Handover
- **Role**: Orchestrator (self)
- **Tasks**:
  - Compile the final results.
  - Report completion to Sentinel.
