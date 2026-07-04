# Prompt: Rebuild the UCOST SC/ST Cell Portal Page in an Advanced, Professional Format

## Context to give the AI/design tool

You are redesigning a government informational webpage for the **SC/ST Cell**, a project under the **Uttarakhand State Council for Science & Technology (UCOST)**, Dehradun. The original page is a bare content dump with no visual hierarchy. Rebuild it as a **single, self-contained page** (no long endless scroll — think dense, premium, bento-grid composition rather than sparse stacked sections) that is modern, professional, and GIGW 3.0–compliant. Keep every piece of content from the source page, but because vertical real estate is limited, prioritize **information density through layout craft**: overlapping cards, compact stat badges, a tight image mosaic, and collapsible/tabbed sub-content rather than long paragraphs. Creativity in composition matters more here than in a typical multi-page portal — this single page has to do the work of five.

---

## 0. Image Asset Manifest (use these exact files, exact placements)

The following local image files are available at `C:\Users\saksh\OneDrive\Desktop\cs\` — reference them by filename and place each in the specified slot. (Note: these were listed from a folder screenshot; if any file isn't yet downloaded/synced locally, re-export or re-save it before build so the path resolves.)

| Filename | Assigned Placement | Treatment |
|---|---|---|
| `logo-UCOST.png` | Header, top-left, primary org logo | Fixed height ~48px, transparent background, anchors to Home |
| `logo UK.png` | Top utility bar, left of "Government of Uttarakhand" text | Small emblem, ~32px, paired with Devanagari/English toggle |
| `ucost campus.png` | Hero banner background (behind the page-title band) | Full-bleed, dark gradient overlay (UCOST blue → transparent) so white title text stays legible on top |
| `chopta temple.png` | Cultural-context mosaic strip (see Section 2B) | Cropped square/portrait tile |
| `temple 1.png` | Cultural-context mosaic strip | Cropped square/portrait tile |
| `culture.png` | Cultural-context mosaic strip | Cropped square/portrait tile |
| `culture 1.png` | Cultural-context mosaic strip | Cropped square/portrait tile |
| `nanital.png` (Nainital) | Cultural-context mosaic strip | Cropped square/portrait tile |
| `moountains.png` | Cultural-context mosaic strip **and** as a subtle full-width divider background between Methodology and Deliverables sections, at 10–15% opacity behind a solid color overlay | Wide/landscape crop |

All six mosaic images (`chopta temple`, `temple 1`, `culture`, `culture 1`, `nanital`, `moountains`) form a single **"Communities & Landscapes of Uttarakhand" strip** — see Section 2B for exact layout. This strip is the emotional/human anchor of the page: it ties the SC/ST hill-community livelihood narrative to real regional imagery instead of leaving the page as pure text/data.

---

## 1. Global Page Structure (must include ALL of these)

1. **Top Utility Bar** (thin strip above header)
   - Government of Uttarakhand emblem/text on the left
   - "Government of India" / "Skip to Main Content" link
   - Font size toggle (A- A A+), high-contrast/accessibility toggle, language switch (English/Hindi)
   - Screen reader access link

2. **Header Band**
   - UCOST logo (left) + "Uttarakhand State Council for Science & Technology" full name and tagline
   - National emblem / DST logo (right, since this is a DST SEED-funded project)
   - Search bar (icon + expandable input)

3. **Primary Navigation Menu** (horizontal, sticky on scroll)
   - Home | About Us | Divisions | Projects | SC/ST Cell (active/highlighted) | Publications | Media | RTI | Contact Us
   - Dropdown/mega-menu support for nested pages

4. **Breadcrumb Trail**
   - Home > Divisions > SC/ST Cell

5. **Page Title Banner**
   - Large heading: "SC/ST Cell"
   - Subheading: "Establishment of Scheduled Caste (SC)/Scheduled Tribe (ST) Cell in UCOST, Dehradun"
   - Optional hero background image (community/fieldwork/Himalayan-region imagery relevant to SC/ST livelihood programs)

---

## 1B. Single-Page Compression Strategy

Since everything must fit on one page without feeling cramped or turning into a wall of text, use these techniques:

- **12-column CSS grid**, max-width 1280px, 24px gutters, section vertical padding capped at 48px (not the usual 80–120px government-portal padding)
- **Tabbed content switcher** for Sections E–G (Objectives / Methodology / Deliverables) — one shared card frame with a 3-tab horizontal switcher at the top, so only one tab's content is visible at a time, saving ~2/3 of the vertical space those three sections would otherwise take. Default open tab: Objectives.
- **Two-column split** for Project Coordinators + Project Team: coordinators as 2 large cards on the left (40% width), team as a compact 6-avatar grid on the right (60% width) — sit side by side, not stacked
- **Inline stat badges** instead of a separate chart section: the 18.76% SC / 2.89% ST figures render as two large circular progress-ring badges (SVG), sitting directly beside the Project Overview paragraph in a 2-column split (text left, stat rings right), not as a separate full-width section
- **Sticky right-rail sidebar** (not a stacked section) — Quick Links, Related Projects, Contact widget all live in a slim 280px sticky column running alongside main content, reclaiming footer-adjacent space
- **Compact footer** — 4-column footer capped at ~160px height, small type (13px), icon-only social row

Target: entire page fits in **2.5–3.5 viewport heights** on desktop at 1440px width, versus the 6–8 viewport heights a naive stacked-section build would produce.

---

## 2. Main Content Sections (in order, with exact content to preserve)

### A. Project Identity Card (info box / summary card at top)
Present as a bordered "Project Fact Sheet" card with icon-labeled rows:
- **Project Title:** Establishment of Scheduled Caste (SC)/Scheduled Tribe (ST) Cell in Uttarakhand State Council for Science and Technology (UCOST), Dehradun
- **Funded By:** Science for Equity Empowerment and Development (SEED) Division, Department of Science & Technology (DST), New Delhi
- **Coverage:** All 13 Districts of Uttarakhand

### A2. "Communities & Landscapes of Uttarakhand" Mosaic Strip
Immediately below the Fact Sheet card, insert a **full-width, fixed-height (~180–220px) image mosaic** using the six regional photos — this replaces what would otherwise be a wasted whitespace gap and gives the page its emotional anchor without costing extra vertical space:
- Layout: 6 tiles in an uneven bento pattern — e.g., 1 wide tile (`moountains.png`, spanning 2 columns) + 5 standard tiles (`chopta temple`, `temple 1`, `culture`, `culture 1`, `nanital`), all with 4px gutters and consistent 8px corner radius
- On hover: tile scales to 1.03x with a soft shadow lift and a small caption overlay fades in (e.g., "Nainital", "Chopta Temple") — subtle micro-interaction, not intrusive
- On mobile: collapses to a horizontally scrollable snap-carousel instead of a grid, so it stays a single row and doesn't eat vertical space
- Purpose: signals *this project is about real hill communities and living heritage*, not just a policy document

### B. Project Coordinators (table or two-column card grid)
| Name | Role |
|---|---|
| Dr. D.P. Uniyal | Joint Director, UCOST (Project Co-PI) |
| Dr. M.S. Rawat | Scientific Officer (Project Co-PI) |

### C. Project Team (card grid or table, 6 members)
| Name | Designation |
|---|---|
| Mr. Santosh Rawat | Principal Project Associate |
| Mr. Sunil Tewari | Principal Project Associate |
| Mr. Punit Singh | Project Associate |
| Mr. Gaurav Chamoli | Project Associate |
| Mr. Paras Upadhayay | Project Assistant |
| Ms. Urmila Ghildiyal | Project Assistant |

### D. Project Overview
Full narrative paragraph (verbatim, reflowed into readable justified body text with a highlighted stat callout):
> UCOST is implementing this SEED-DST funded project targeting the SC/ST community in Uttarakhand's hilly regions — **18.76% SC population** and **2.89% ST population** (Census 2011) — with focus on sustainable livelihood planning, traditional/indigenous knowledge capture, skill upgrades, technology database creation, and spatial mapping. SC/ST Cells are being established across all 13 districts of Uttarakhand to coordinate technology adoption for socioeconomic development, scale successful interventions, and build institutional and human capacity.

Use two **stat callout badges/infographics** for the 18.76% (SC) and 2.89% (ST) figures — a pattern used often in government dashboards (donut chart or big-number stat cards).

### E. Objectives (icon list, 4 items)
Present as a 2x2 or 4-column icon-card grid:
1. Assess the livelihood system for sustainable livelihood planning through science, know-how, and practices
2. Capture traditional and indigenous knowledge and upgrade skills, building on local innovation and knowledge systems
3. Establish a database of promising technologies for widespread adaptation
4. Map data and resources on the spatial domain

### F. Methodology
Body paragraph, verbatim meaning preserved, organized as a **process/workflow diagram** with these components as connected nodes:
- Food Preservation Unit (Horticulture & Agriculture Products)
- Artisan & Handicrafts Unit
- Scientific Gazettes Preparation Unit (incl. indigenous/traditional knowledge testing, product quality validation, market linkage)
- Mapping through Remote Sensing (RS) & Geographical Information System (GIS)

### G. Project Deliverables (numbered list / checklist styled cards)
1. Human Resource Development of SC/ST Community
2. Establishment of Site-based Skill Development Centre
3. Identification of Gaps in Existing Government/Non-Government Schemes
4. Formulation, Strengthening, Coordination & Documentation of Programmes/Projects for filling gaps through S&T interventions
5. Replicable Model Development through S&T Intervention in SC/ST Areas

---

## 3. Sidebar (right column, sticky)
- "Quick Links" widget: RTI, Tenders, Downloads, Related Schemes
- "Related Projects/Divisions" widget
- Contact widget: UCOST address, phone, email
- Social media icons (X/Twitter, Facebook, YouTube)

## 4. Footer (full width)
- Four-column layout: About UCOST | Important Links | Related Portals (DST, MeitY, Digital India, MyGov) | Contact & Social
- Last updated date, Visitor counter
- Copyright line, Web Information Manager credit
- Compliance badges: GIGW 3.0, WCAG 2.1 AA, valid HTML/CSS
- Hyperlinks to Sitemap, Privacy Policy, Terms of Use, Disclaimer, Hyperlinking Policy, Copyright Policy

---

## 5. Design System Requirements

- **Color palette (exact tokens):**
  - `--ucost-blue: #0B3D6E` (primary — header, nav active state, buttons)
  - `--ucost-blue-light: #1E6FB5` (hover states, links)
  - `--saffron-accent: #FF9933` (small accent only — badges, active tab underline)
  - `--green-accent: #128807` (success/stat indicators)
  - `--bg-base: #F7F8FA`, `--bg-card: #FFFFFF`
  - `--text-primary: #1A1A1A`, `--text-secondary: #5A5A5A`
  - Use saffron/green sparingly (5–10% of visual weight) — this is a professional S&T portal, not a festive banner
- **Typography:**
  - Font stack: `'Inter', 'Noto Sans', 'Noto Sans Devanagari', sans-serif`
  - H1 (page title): 32px/40px, weight 700
  - H2 (section titles): 20px/28px, weight 600, `--ucost-blue`
  - H3 (card titles): 16px/22px, weight 600
  - Body: 14px/22px, weight 400, `--text-secondary`
  - Stat numbers (18.76%, 2.89%): 28px, weight 800, tabular-nums
- **Cards & shadows:** `border-radius: 10px`, `box-shadow: 0 1px 3px rgba(0,0,0,0.08)` resting, `0 4px 12px rgba(0,0,0,0.12)` on hover; 1px `#E5E7EB` border
- **Icons:** Consistent 20px line-icon set (Lucide or Feather style) for objectives, deliverables, and contact info — never mix icon styles
- **Responsive breakpoints:** Desktop ≥1280px (full grid), Tablet 768–1279px (mosaic drops to 4 tiles, sidebar moves below content), Mobile <768px (single column, hamburger nav, mosaic becomes carousel, tabs become accordion)
- **Accessibility:** GIGW 3.0 and WCAG 2.1 AA compliant — skip-to-content link, descriptive alt text on all 9 images (e.g., alt="Chopta Temple, Rudraprayag district" not "image1"), full keyboard navigation, minimum 4.5:1 contrast ratio on all text, semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`)
- **Data visualization:** SVG circular progress rings for the SC (18.76%) / ST (2.89%) stats — animate ring fill on scroll-into-view (once, not looping)
- **Micro-interactions:** 150ms ease-out transitions on all hover states; sticky nav condenses (reduces height by ~30%) after 80px scroll; mosaic tile hover lift as described in Section A2

---

## 6. Deliverable Format
Build as a **single responsive HTML/CSS(/JS) file** (or single React component if specified), structured with semantic tags (`<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`), ready to preview in-browser, styled to look like a polished, modern Government-of-India department portal rather than a plain content page.

- Reference all 9 images via a local `assets/` folder using their exact filenames from Section 0 (e.g., `assets/logo-UCOST.png`, `assets/ucost campus.png`) — copy the actual files from `C:\Users\saksh\OneDrive\Desktop\cs\` into that `assets/` folder before build so paths resolve
- If any image is missing/not yet downloaded at build time, use a clearly labeled grey placeholder box of the correct aspect ratio (not a broken-image icon) so layout doesn't shift once the real file is dropped in
- Total page weight target: keep all 9 images compressed/optimized (WebP preferred, PNG fallback) so combined page load stays under ~1.5MB
