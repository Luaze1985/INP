# Plan - Mockup Analysis and Improvements Proposal

This plan coordinates the tasks outlined in the original request to review the VERIFIED research status mockup, perform design code research, propose background images, and document them in an improvement proposal.

## Steps and Subtasks

### 1. Planning & Setup
- [x] Create `BRIEFING.md`
- [x] Create `progress.md`
- [x] Create `plan.md`
- [x] Create `PROJECT.md`
- [ ] Start heartbeat cron for progress updates

### 2. Mockup Review & Design Reference Investigation
- [ ] Spawn **Explorer (teamwork_preview_explorer)** to:
  - Inspect `site/mockup/index.html` and `site/mockup/mockup-styles.css` (read-only).
  - Search the codebase and existing documents for any reference material on "Google Stitch", NFR, EU Horizon portals, etc.
  - Review `site/mockup/bakgrunnsbilder-forslag.md` and other scripts for existing background image lists.
  - Produce a structured research report detailing visual layouts, design codes, typography, accent colors, contrast ratios (WCAG), and sidebar viewport handling.
- [ ] Verify the explorer's report.

### 3. Alternative Background Images Selection
- [ ] Analyze the explorer's findings regarding local craftsmanship background images.
- [ ] Verify selection of 3-5 images with direct links, photographer credits, license info, and rationale matching "enkle folk fra bygda".

### 4. Draft Improvement Proposal
- [ ] Spawn **Worker (teamwork_preview_worker)** to:
  - Write `site/mockup/improvements-proposal.md` based on explorer findings and image recommendations.
  - Verify WCAG compliance recommendations, Google Stitch layout details, and NFR/Horizon portal structures.
  - Ensure absolutely NO modifications are made to `site/mockup/index.html` or `site/mockup/mockup-styles.css`.
- [ ] Spawn **Reviewer (teamwork_preview_reviewer)** to:
  - Review the proposed markdown document.
  - Run git checks to ensure code integrity (no modifications to html/css).
- [ ] Spawn **Forensic Auditor (teamwork_preview_auditor)** to:
  - Validate code integrity (strict check that no HTML/CSS files were modified).

### 5. Finalize & Handoff
- [ ] Write `handoff.md` summarizing the outcomes.
- [ ] Send final message to the Sentinel.
