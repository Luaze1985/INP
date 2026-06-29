# Handoff Report — Design and Content Improvement Proposal

This report summarizes the creation of the design and content improvement proposal report for the VERIFIED scrollytelling mockup, following the Handoff Protocol.

---

## 1. Observation

- **Inputs Read**:
  - Explorer Handoff: `c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\.agents\teamwork_preview_explorer_design_review_1\handoff.md`
  - Design Brief: `c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\site\design-brief.md`
  - Background Images Proposals: `c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\site\mockup\bakgrunnsbilder-forslag.md`
  - CSS Styles: `c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\site\mockup\mockup-styles.css`
  - HTML Template: `c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\site\mockup\index.html`
- **Current Styling and Opacities Observed**:
  - `.side-menu__footer` (line 251) has `color: rgba(246, 240, 226, 0.3);` (30% opacity).
  - `.source-tag` (line 437) has `color: rgba(246, 240, 226, 0.4);` (40% opacity).
  - `.project-info__title` (line 226) has `color: rgba(246, 240, 226, 0.4);` (40% opacity).
  - Base colors: Gold `#E8B23E`, Cream `#F6F0E2`, Dark `#1A1A1A`.
- **Target File Created**:
  - `c:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\site\mockup\improvements-proposal.md`

---

## 2. Logic Chain

1. **Synthesizing Google Stitch and Institutional Design Codes**:
   - Google Stitch emphasizes high information scent, modular card layouts, and search-like knowledge graphs. The definition list `dl` in the sidebar matches the knowledge graph pattern, and the fact cards match modular cards. We proposed grouping the `dl` metadata list inside a modular card and adding grid divider borders to improve structure.
   - Academic portal standards require visual trust anchors and clear citation/verification trails. We proposed replacing plain text partner placeholders with a monochrome logo grid (VIBS, SINTEF, Tirna Fagskole) and implementing verification status tags (e.g. `approved`, `manually_edited`) based on the project's internal database structure.
2. **Typography**:
   - The imported **Geist** font is used. We recommended distinct weights (600/700 for headings, 300/400 for body text) and keeping line-heights at 1.6-1.7 for paragraphs to preserve readability on dark backgrounds.
3. **Contrast Compliance**:
   - Contrast calculations:
     - Cream `#F6F0E2` on Dark `#1A1A1A` yields **15.35:1** (WCAG AAA Pass).
     - Gold `#E8B23E` on Dark `#1A1A1A` yields **9.05:1** (WCAG AAA Pass).
     - 30% opacity cream yields **2.50:1** (WCAG AA Fail).
     - 40% opacity cream yields **3.49:1** (WCAG AA Fail).
   - Remedy: Increase opacities to at least 50% (`rgba(246, 240, 226, 0.50)`), which blends to `#88857E` and yields **4.65:1** (WCAG AA Pass), or 60% (`rgba(246, 240, 226, 0.60)`) yielding **6.18:1**.
4. **Layout & Viewports**:
   - Desktop viewports (min-width: 1024px) utilize a sticky, static sidebar. Mobile viewports (< 1024px) use a slide-out drawer menu. Both display clean content flow. Wrapping the sidebar metadata in card-like styling will match the Google Stitch layout.
5. **Background Images Selection**:
   - Five candidates matching the rustic craftmanship ("enkle folk fra bygda") identity were selected and detailed with photographer credit, license, and direct URLs:
     1. Hunter Haley — photo-1507207611509-ec012433ff52 (Tømrer i støvete verksted)
     2. Jeriden Villegas — carrying wood (Tømrer som bærer planker)
     3. Clay Banks — photo-1605647540924-852290f6b0d5 (Trekonstruksjon og stenderverk)
     4. Jesper Aggergaard — photo-1504917595217-d4dc5ebe6122 (Tømrer på trevegg)
     5. Cullan Smith — photo-1586528116311-ad8dd3c8310d (Takstoler under oppføring)

---

## 3. Caveats

- **No Code Modification**: The code integrity constraint prohibited any direct modifications to `index.html` or `mockup-styles.css`. No code files were modified.
- **Offline Contrast Audits**: Contrast ratios and Unsplash candidate details were validated against local documentation and pre-calculated values, as CODE_ONLY prevents external requests.

---

## 4. Conclusion

The comprehensive report `improvements-proposal.md` has been successfully compiled and written to the `site/mockup/` directory. It satisfies all visual design, typography, accessibility, responsive layout, reference, and background image requirements requested by the user.

---

## 5. Verification Method

- **Inspect File**:
  - Open and review `site/mockup/improvements-proposal.md` to confirm all sections are fully populated.
- **Verify Code Integrity**:
  - Run `git status` to ensure `site/mockup/index.html` and `site/mockup/mockup-styles.css` remain completely unmodified.
