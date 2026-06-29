## 2026-06-28T18:04:58Z
<USER_REQUEST>
You are the Worker (identity: teamwork_preview_worker).
Your metadata directory is: c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\teamwork_preview_worker_proposal_drafting_1\
Please create this directory and initialize your progress.md and BRIEFING.md inside it.

Your task is to write a comprehensive design and content improvement proposal report at:
`c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\site\mockup\improvements-proposal.md`

Use the findings from the Explorer's handoff report located at:
`c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\teamwork_preview_explorer_design_review_1\handoff.md`
And the design guidelines in:
`c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\site\design-brief.md`

Your generated document `improvements-proposal.md` must be highly professional and must include:
1. Executive Summary: High-level overview of the proposed visual/content audit findings and goals.
2. Visual Layout & Google Stitch / Academic Design Patterns:
   - Explain how to integrate "Google Stitch" visual patterns (modular cards, grid alignment, clean divider borders, high information scent, and search-like knowledge panels) to make the sections look more structured and compact.
   - Explain how to integrate academic and research-focused design patterns (such as from NFR/Norges forskningsråd portals or EU Horizon projects) by detailing recommendations like visual partner logo grids (e.g. for VIBS, SINTEF, Tirna Fagskole) and structured citation/bibliography lists or data verification status tags.
3. Typography & Content Hierarchy: How to improve readability using Geist font weights, line-height adjustments, and clean layouts.
4. Accent Colors & Contrast Ratios (WCAG 2.1 Compliance Audit):
   - Highlight contrast ratios: Cream #F6F0E2 on Dark #1A1A1A (15.35:1 - AAA pass), Gold #E8B23E on Dark (9.05:1 - AAA pass).
   - Explicitly detail contrast failures of opacity-blended text in the current mockup (30% opacity `#menu-disclaimer` is 2.50:1, failing AA; 40% opacity `.source-tag` and `.project-info__title` is 3.49:1, failing AA).
   - Recommend bumping these opacities to at least 50% (`rgba(246, 240, 226, 0.50)`), which blends to `#88857E` and yields a contrast ratio of 4.65:1 (passing WCAG AA for normal text).
5. Sidebar Layout & Responsive Viewports: Analyze desktop static columns (min-width: 1024px) vs. mobile drawer viewports (< 1024px), detailing how styling should ensure clean content flow and suggest wrapping definition lists in card-like styling to match Google Stitch patterns.
6. Direct Links & References: Provide links to reference materials (e.g. Material Design guidelines, Google Search, NFR Portal, EU Horizon frameworks).
7. Alternative Background Image Proposals: Detail the 5 selected Unsplash background image candidates from `site/mockup/bakgrunnsbilder-forslag.md` (Hunter Haley - photo-1507207611509-ec012433ff52, Jeriden Villegas - carrying wood, Clay Banks - photo-1605647540924-852290f6b0d5, Jesper Aggergaard - photo-1504917595217-d4dc5ebe6122, Cullan Smith - photo-1586528116311-ad8dd3c8310d). For each, list direct URL, photographer credit, license, and why it matches the authentic rural craftsmanship ("enkle folk fra bygda") identity.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

STRICT CODE INTEGRITY CONSTRAINT:
You must NOT modify any code files directly. Leave `site/mockup/index.html` and `site/mockup/mockup-styles.css` completely unmodified. Check with git status or other means that they are unmodified after you write the markdown file.

</USER_REQUEST>
