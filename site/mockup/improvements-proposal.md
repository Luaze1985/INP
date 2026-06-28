# Design and Content Improvement Proposal Report: VERIFIED Scrollytelling Mockup

**Project Reference**: IPN-VERIFIED (Norges forskningsråd - NFR IPN Application)  
**Document Status**: Proposal Report  
**Author**: Visual Design & Quality Assurance Specialist (teamwork_preview_worker)  
**Date**: June 28, 2026  

---

## 1. Executive Summary

The **VERIFIED** project is a research-focused initiative aiming to establish an objective, simple, and verifier-backed methodology for documenting the actual environmental and sustainability impacts of material choices in the private residential building market. Developed primarily for small-and-medium-sized (SMB) regional builders and craftspeople ("enkle folk fra bygda"), the project seeks to bridge the gap between complex life-cycle assessments (LCA/EPD) and the everyday reality of local construction sites.

This report presents a comprehensive visual design and content audit of the current scrollytelling mockup. The audit evaluates the mockup's alignment with:
1. **The Core Brand Identity**: An authentic, honest, and competent representation of rural manual craftsmanship.
2. **Institutional Standards**: The rigor, transparency, and trust anchors required by public funding bodies like the Research Council of Norway (NFR) and EU Horizon Europe.
3. **Usability and Accessibility**: Complete compliance with Web Content Accessibility Guidelines (WCAG 2.1) AA and AAA standards.

The proposal outlines concrete recommendations to transition the mockup into a highly polished, professional, and accessible portal, while strictly adhering to the code freeze (leaving existing files unaltered).

---

## 2. Visual Layout & Google Stitch / Academic Design Patterns

To balance the down-to-earth craftsmanship of the project with the academic authority of its research partners, we propose integrating two distinct design patterns into the mockup's layout.

### A. Google Stitch Design Patterns
"Google Stitch" focuses on high information scent, modular card layouts, search-engine-style knowledge panels, and crisp grid alignments. Applying these principles will make the layout more structured and compact:
- **Modular Cards**: The glassmorphic fact cards (`.fact-card`) should be treated as structured, self-contained data modules. We recommend adding defined grid boundaries rather than leaving cards floating loosely in open space. Section divisions should employ thin, high-contrast borders (e.g., solid `rgba(246, 240, 226, 0.08)` or `rgba(232, 178, 62, 0.15)` lines) to divide content chunks.
- **Search-Like Knowledge Panels**: In the sidebar navigation panel, the key-value project metadata (`.project-info dl`) closely mirrors a search engine’s knowledge graph panel. We recommend wrapping this definition list in a distinct card-like container (matching the fact card style) with subtle glassmorphic blur and borders. This separates project data from navigational links and increases its "information scent."

### B. Academic and Research-Focused Design Patterns
To meet NFR and institutional expectations, the design must project high scientific transparency:
- **Visual Partner Logo Grid**: Replace the text-based placeholder `[placeholder - SINTEF Community og Tirna Fagskole]` with a visual, high-contrast monochrome logo grid displaying the partners behind the project: **VIBS**, **SINTEF Community**, and **Tirna Fagskole**. Placing these logos in a structured row in the sidebar footer or at the bottom of the intro section immediately establishes a "trust anchor."
- **Data Verification Status Tags**: Standardize references by replacing informal `.source-tag` text with structured data status badges. Drawing from the project's internal database schema (`sources`, `claims`), claims can display verification tags such as `approved` (🟢), `suggested` (🟡), or `manually_edited`. This reinforces the core thesis of VERIFIED—making data quality and source verifiability explicitly visible.

---

## 3. Typography & Content Hierarchy

Typography is the cornerstone of readability, particularly in high-density factual documents. The mockup imports the **Geist** font family, which is modern, clean, and highly legible.

### Typography Improvements & Hierarchy
1. **Font Weights**: Geist's multiple weights should be leveraged to differentiate structural hierarchy. We recommend using **Geist SemiBold (600)** or **Geist Bold (700)** exclusively for headings (`h1`, `h2`, `.section-badge`) and key metrics (`.fact-card__number`). For body copy (`.section-paragraph` and `.hero-subtitle`), **Geist Light (300)** or **Geist Regular (400)** should be used to maintain a clean, readable text texture.
2. **Line-Height Adjustments**: 
   - Body paragraph text (`.section-paragraph`) should maintain a line-height of **1.6 to 1.7** (currently set to 1.7) to allow comfortable reading on dark backgrounds.
   - Large headings (`h1` and `h2`) should have a tighter line-height (**1.1 to 1.2**) to ensure they remain cohesive and do not break awkwardly on smaller viewports.
3. **Layout Spacing**: Ensure substantial vertical margin and padding ("lufterom" or breathing room) between content blocks to prevent visual fatigue. A minimum of `2.5rem` to `3rem` spacing is recommended between section headings and paragraphs on desktop displays.

---

## 4. Accent Colors & Contrast Ratios (WCAG 2.1 Compliance Audit)

An audit of the color palette reveals that while the primary colors possess excellent contrast against the dark background, secondary elements utilizing low opacities fail accessibility compliance.

### A. Compliant Colors (WCAG 2.1 AAA Pass)
*   **Cream `#F6F0E2` on Dark `#1A1A1A`**
    *   **Contrast Ratio**: **15.35:1** (Passes WCAG AA and AAA for all text sizes).
    *   *Usage*: Highly legible for main body paragraphs, titles, and card descriptions.
*   **Gold `#E8B23E` on Dark `#1A1A1A`**
    *   **Contrast Ratio**: **9.05:1** (Passes WCAG AA and AAA for all text sizes).
    *   *Usage*: Perfect for draw-in accent details, buttons, and big data numbers.

### B. Opacity-Blended Contrast Failures (WCAG 2.1 AA Failures)
To achieve a "dempet" (muted) gray look, the mockup uses transparency opacities of the cream text color on the dark background. The audit reveals the following violations:
*   **30% Opacity Cream text (`rgba(246, 240, 226, 0.30)`) on Dark `#1A1A1A`**
    *   *Equivalent Blended Solid Color*: `#5B5955`
    *   **Contrast Ratio**: **2.50:1** (FAIL - fails both AA and AAA standards).
    *   *Affected Element*: `.menu-disclaimer` (`FoU-utkast til NFR-søknad` in the sidebar footer).
*   **40% Opacity Cream text (`rgba(246, 240, 226, 0.40)`) on Dark `#1A1A1A`**
    *   *Equivalent Blended Solid Color*: `#72706A`
    *   **Contrast Ratio**: **3.49:1** (FAIL - fails WCAG AA Normal text requirement of 4.5:1).
    *   *Affected Elements*: `.source-tag` (fact card footer citation) and `.project-info__title` (`FoU-prosjektinfo` section heading in sidebar).

### C. Recommended Remediation
To resolve these accessibility failures without sacrificing the muted visual hierarchy, we recommend the following:
*   **Increase opacity to at least 50% (`rgba(246, 240, 226, 0.50)`)**:
    *   *Equivalent Blended Solid Color*: `#88857E`
    *   **Contrast Ratio**: **4.65:1** (PASS - passes WCAG AA Normal text standard of 4.5:1).
    *   *Application*: Bump `.source-tag`, `.project-info__title`, and `.menu-disclaimer` to this opacity.
*   **Alternative (Preferred for AAA compliance)**: Bump opacity to **60% (`rgba(246, 240, 226, 0.60)`)**, which blends to `#9E9A92` and provides a contrast ratio of **6.18:1** (comfortably exceeding the AA threshold).

---

## 5. Sidebar Layout & Responsive Viewports

The mockup uses a responsive design that handles desktop and mobile layouts differently:

### A. Desktop Viewport (min-width: 1024px)
*   **Layout**: A dual-column grid system where the sidebar (`.side-menu`) acts as a static, sticky left-hand column (`position: sticky`, width `320px`), while the main container scrolls vertically.
*   **Content Flow**: Clean and logical. The sticky menu ensures that project info and navigation are constantly available, acting as an anchor.
*   **Improvement**: The definition list (`dl`) currently flows loosely. Wrapping this list in card-like container styling matching the `.fact-card` will align the sidebar with the Google Stitch card motif and define clear content boundaries.

### B. Mobile Viewport (< 1024px)
*   **Layout**: A top-bar header (`.mobile-header`) is fixed at the top of the viewport. The sidebar shifts to an off-canvas drawer (`transform: translateX(-100%)`) that slides in from the left when the burger menu is toggled.
*   **Content Flow**: Responsive and clear. The drawer overlay is dismissible via the close button (`&times;`) or by clicking any navigation link.
*   **Improvement**: On very narrow mobile screens (< 360px), padding inside the side-menu navigation can cause wrapping of the logo text. Adjusting padding to `1rem` on narrow screens prevents layout breakage.

---

## 6. Direct Links & References

To align the implementation details with established visual design frameworks and portals, the following guidelines and systems are referenced:
*   **Google Material Design 3 Guidelines**: Refer to [Material Design 3 Documentation](https://m3.material.io) for modular grid systems, card designs, and modern dark-theme elevation overlays.
*   **Google Search Knowledge Panels**: See [Google Search Visual Elements](https://developers.google.com/search/docs/appearance/visual-elements/knowledge-panel) for guidelines on displaying highly structured data in compact panels.
*   **Norges forskningsråd (NFR) Portal**: Visit [Forskningsrådet Official Website](https://www.forskningsradet.no) for structural guidelines on project descriptions, institutional layout expectations, and public dissemination.
*   **EU Horizon Funding Frameworks**: See [EU Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home) for academic and consortium-backed layout standards.

---

## 7. Alternative Background Image Proposals

To represent the authentic, rustic craftsmanship of rural Norwegian contractors and SMB carpenters, we have selected five high-quality background images from Unsplash. All are licensed under the Unsplash License (free commercial and non-commercial use) and are optimized for readability when dimmed to 30% brightness and 45% saturation.

### Candidate 1: Carpenter in a Dusty Workshop (`kandidat-1.jpg`)
*   **Direct URL**: [Unsplash Photo 5i0nGc1k3LY](https://images.unsplash.com/photo-1507207611509-ec012433ff52)
*   **Photographer Credit**: Hunter Haley
*   **License**: Unsplash License
*   **Rural Craftsmanship Rationale**: Depicts a craftsman in physical work attire inside a rustic workshop surrounded by sawdust, raw wood, and traditional tools. It captures honest labor, tactile materials, and the professional pride (*yrkesstolthet*) of manual builders, completely free of corporate gloss.

### Candidate 2: Carpenter Carrying Planks (`kandidat-3.jpg`)
*   **Direct URL**: [Unsplash Photo](https://images.unsplash.com/photo-1590674899484-d5640e854abe)
*   **Photographer Credit**: Jeriden Villegas
*   **License**: Unsplash License
*   **Rural Craftsmanship Rationale**: Shows an active worker in standard overalls carrying heavy framing timber on an outdoor site. This image visualizes physical grit, daily manual operations, and the real-world conditions under which rural SMB carpenters work.

### Candidate 3: Residential Wood Framing (`kandidat-5.jpg`)
*   **Direct URL**: [Unsplash Photo F1VfW8fS66M](https://images.unsplash.com/photo-1605647540924-852290f6b0d5)
*   **Photographer Credit**: Clay Banks
*   **License**: Unsplash License
*   **Rural Craftsmanship Rationale**: Captures the timber skeleton (*stenderverk*) and roof trusses of a traditional family home under construction. It immediately defines the physical research object of the VERIFIED project (residential timber structures) and highlights wood craftsmanship.

### Candidate 4: Carpenter Nailing Cladding (`kandidat-9.jpg`)
*   **Direct URL**: [Unsplash Photo](https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122)
*   **Photographer Credit**: Jesper Aggergaard
*   **License**: Unsplash License
*   **Rural Craftsmanship Rationale**: Displays a contractor nailing exterior wooden cladding on a house wall. It highlights details of carpentry execution and represents the practical focus of regional builders.

### Candidate 5: Roof Trusses Under Construction (`kandidat-10.jpg`)
*   **Direct URL**: [Unsplash Photo](https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d)
*   **Photographer Credit**: Cullan Smith
*   **License**: Unsplash License
*   **Rural Craftsmanship Rationale**: A structural shot of wooden roof trusses framing the sky. It represents traditional Norwegian construction engineering, emphasizing robust structures, simple materials, and precise woodworking.
