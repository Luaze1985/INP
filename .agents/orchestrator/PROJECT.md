# Project: IPN VERIFIED Mockup Improvement Proposal

## Architecture
- This is a documentation and design review task for the VERIFIED IPN application mockup.
- Inputs:
  - `site/mockup/index.html` - The static mockup HTML.
  - `site/mockup/mockup-styles.css` - The mockup stylesheet.
  - Local documentation (e.g. `site/mockup/bakgrunnsbilder-forslag.md`).
- Outputs:
  - `site/mockup/improvements-proposal.md` - A comprehensive improvement proposal in Markdown.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| 1 | Mockup Review & Reference Research | Analyze mockup files and local/external references on Google Stitch & academic portals | None | DONE |
| 2 | Background Image Selection | Find 3-5 carpentry background images matching the target audience identity | 1 | DONE |
| 3 | Draft Proposal Report | Generate `improvements-proposal.md` with layout, typography, color contrast, and sidebar guidelines | 1, 2 | DONE |
| 4 | Verification & Quality Gate | Check code integrity and review proposal content with Reviewer and Auditor | 3 | DONE |

## Interface Contracts
- Mockup files (`index.html`, `mockup-styles.css`) are read-only and MUST NOT be modified.
- Output document `site/mockup/improvements-proposal.md` must be valid Markdown, readable, and structured as per R2 and R3.
