# MASTER PROMPT — SC/ST Cell Portal Rebuild (Antigravity Build Instructions)

**Repository:** https://github.com/0saksham/Uttarakhand-Sc-ST-dashboard
**Live site:** https://uttarakhand-sc-st-dashboard.vercel.app/
**Current stack:** Single `index.html` (100% HTML/CSS/JS), `assets/` folder, deployed via Vercel. A prior rebuild prompt (`UCOST_SCST_Cell_Portal_Rebuild_Prompt.md`) already exists in the repo root — read it first for the established design system (color tokens, typography, spacing, component patterns) and keep that visual language consistent unless a specific instruction below overrides it.

---

## HOW TO WORK — LOOP PROMPTING (read this before starting)

Do not treat this as a single one-shot build. Work in iterative passes:

1. **Pass 1 — Build.** Implement every section below as completely as you can from the data provided.
2. **Pass 2 — Self-review.** Go through the **Final QA Checklist** at the bottom of this document item by item. For each item, mark it Pass / Fail / Partial and note exactly why.
3. **Pass 3 — Fix.** Fix every Fail/Partial item found in Pass 2.
4. **Pass 4 — Re-review.** Re-run the full checklist again from scratch (not just the previously-failed items — a fix can break something else).
5. **Repeat Passes 3–4** until a full checklist pass comes back 100% clean with zero Fail/Partial items.
6. **Final output:** a short changelog summarizing what was fixed in each loop iteration, plus confirmation of the final clean checklist pass.

Do not stop at "looks done" — stop only when the checklist is clean. If something in this document is ambiguous or a required data file/asset is missing, flag it explicitly in your output rather than guessing silently.

---

## 1. Header & Accessibility Bar
- Fix the top Uttarakhand/UCOST logo rendering — correct aspect ratio, alignment, consistent sizing at all breakpoints.
- Make the **Screen Reader** toggle functional: real ARIA live-region announcements and enhanced labeling on activation, not decorative.
- Make **A- / A / A+** functional: scales a root font-size variable site-wide, state held in component state (no localStorage).

## 2. Branding Row
- Remove the UK state logo and the full council name/address block currently shown there (the "Uttarakhand State Council for Science & Technology / उत्तराखंड राज्य विज्ञान एवं प्रौद्योगिकी परिषद / UCOST, Vigyan Dham, Jhajra, Dehradun – 248 007" text and the UK logo next to it).
- Also remove the search bar from this row.
- Replace the freed space with a compact, styled **"SC / ST Cell"** wordmark/badge — this becomes the page's primary visual identity mark. Give it real design treatment (custom type, small icon/emblem, or two-tone badge) — not a plain text swap.

## 3. Navigation
Reduce nav to exactly **three items: Home | About Us | Contact Us**.
- **Home** → external link to `https://ucost.uk.gov.in/`
- **About Us** → expands to exactly two sub-items, each opening its own detail page sharing the global header/footer theme (see Section 6 for full text):
  - **UCOST**
  - **SC/ST Cell**
- **Contact Us** → routes to the Contact Us page/section (Section 9)
- Remove entirely: Divisions, Projects, Publications, Media, RTI.

## 4. Hero Section
- Replace the current background video with `hero.mp4`, located at `C:\Users\saksh\OneDrive\Desktop\cs\hero.mp4`. Maintain autoplay/muted/loop, optimize for web.
- Implement a **scroll-driven signature interaction** rather than a static hero: as the user scrolls past the hero, the video should smoothly shrink and dock into a small corner frame (picture-in-picture style) while the Project Fact Sheet / stats rise up and take over the main viewport. This should be the one deliberate motion moment on the page — keep everything else calm around it, don't stack additional scroll effects on top of it.

## 5. Photos Section
- Replace the current photo strip with the 80 images located at `C:\Users\saksh\OneDrive\Desktop\cs\1\UCOST`.
- Each image's filename becomes its caption/alt text.
- Build as a responsive grid; visually highlight a subset (larger tile / featured border) — use your judgment for which if no explicit highlight list is provided, or flag this as needing a decision.
- Add an **"Explore All Media"** control that opens a full gallery (modal or dedicated page) showing all 80 images with lightbox/zoom navigation.

## 6. About Us (2 sub-pages)
About Us has exactly two clickable entries. Each opens its own detail page (same global header/footer theme as the rest of the site) showing the full text below verbatim — no summarizing:

**UCOST page — full text:**
> Uttarakhand State Council for Science and Technology is an autonomous body of the Government of Uttarakhand, Department of Information & Science Technology. UCOST started its activities from last quarter of year 2005, However it was registered under the Registration of Societies Act, 1860 in November 2002. The apex body of the Council is the General Body which is chaired by the Hon'ble Chief Secretary. This body comprises of the Principal Secretary & Secretaries from various departments, Vice Chancellors, eminent scientists, representatives from Industries and NGO's. The day to day business is held by the Director General. The Secretary of the department is the chairman of its executive committee. The Council plays a catalytic role for the promotion of S&T in the state and supplement/complement the developmental programmes of the state in different sectors. The overall incharge of the Council is the Director General.

**SC/ST Cell page — full text:**
> The SC/ST Cell of the Uttarakhand State Council for Science & Technology (UCOST) has been established under the project "Establishment of SC/ST Cell in Uttarakhand State Council for Science & Technology," funded by the Science for Equity, Empowerment and Development (SEED) Division, Department of Science and Technology (DST), Government of India. The project has been implemented in two phases to promote the socio-economic development and technological empowerment of the Scheduled Caste (SC) and Scheduled Tribe (ST) communities residing in the hilly regions of Uttarakhand. The initiative primarily covers districts including Dehradun, Champawat, Chamoli, Nainital, Pithoragarh, Udham Singh Nagar, and Uttarkashi, while establishing a coordinated network across all 13 districts of the state. According to the Census 2011, SCs constitute 18.76% and STs 2.89% of Uttarakhand's total population, making focused interventions essential for inclusive development. The SC/ST Cell serves as a coordination and facilitation platform for identifying, promoting, adapting, and scaling up appropriate science and technology-based solutions that enhance sustainable livelihoods and improve the quality of life of target communities. It works towards strengthening human and institutional capacities through skill development, technology deployment, and capacity-building programmes. The Cell also assesses local livelihood systems, documents and promotes traditional and indigenous knowledge, supports local innovations, develops databases of promising technologies for wider adoption, and undertakes spatial mapping of resources to facilitate evidence-based planning. In its second phase, the project further emphasizes human resource development, establishment of site-based skill development centres, replication of successful technology interventions, and identification of gaps in existing government and non-government schemes to ensure effective delivery of developmental benefits to SC/ST communities.

At the end of the About Us section (not on every sub-page — just the main About Us area), include a social media row with **only** these four, correctly linked:
- Facebook: https://www.facebook.com/ucostpage
- X: https://x.com/ucostdehradun
- YouTube: https://www.youtube.com/@ucostdehradun
- LinkedIn: https://www.linkedin.com/in/ucostdehradun/

If any other social platform icon currently exists on the page with no real/confirmed account, remove it — do not leave placeholder/dead social links.

## 7. Quick Links — Auto-Scrolling Logo Carousel
Rebuild Quick Links as a vertical auto-scrolling carousel of clickable logos:
- Images scroll automatically (slow, continuous auto-scroll).
- Manual **up/down arrow controls** let the user override — pause auto-scroll on manual interaction, resume after a few seconds idle.
- Each logo is clickable and opens its respective link in a new tab.
- Logo image source: use the folder at `C:\Users\saksh\OneDrive\Desktop\cs\link images` if present; if that folder is missing or incomplete, the same logos are also embedded as images inside `QUICK_LINKS.docx` (already provided) — extract from there as a fallback.

**Data — 8 entries:**
| # | Name | Link |
|---|---|---|
| 1 | National Portal of India | https://www.india.gov.in/ |
| 2 | Department of Science & Technology, Govt. of India | https://dst.gov.in/ |
| 3 | India Science, Technology & Innovation Portal | https://www.indiascienceandtechnology.gov.in/ |
| 4 | Council of Scientific & Industrial Research (CSIR) | http://www.csir.res.in/ |
| 5 | Government of Uttarakhand | https://uk.gov.in/ |
| 6 | Dept. of IT, Good Governance and Science Technology, Govt. of Uttarakhand | https://it.uk.gov.in/ |
| 7 | Uttarakhand State Council for Science and Technology | https://ucost.uk.gov.in/ |
| 8 | Directorate of Tribal Welfare, Government of Uttarakhand | https://tribalwelfare.uk.gov.in/ |

## 8. What's New (replaces "Related Divisions")
Remove the "Related Divisions" block. Add a **What's New** block in its place. Source content from the folder at `C:\Users\saksh\OneDrive\Desktop\cs\what's new`. One confirmed item so far — the SC/ST Cell Project Staff recruitment advertisement (Principal Project Associate walk-in interview, dated 10th August 2023, UCOST Vigyan Dham Jhajra Dehradun, full eligibility/terms & conditions as per the source PDF). Each What's New item opens its own detail page using the shared template (Section 11).

Also **swap the display position** of the Quick Links block and the What's New block relative to their current layout (whichever one is currently on which side, reverse it) so the two sit side by side in switched positions.

## 9. Contact Us
**Main nav "Contact Us"** routes to a full Contact page with:
- **PI:** Prof. (Dr.) Durgesh Pant, Director General, UCOST, Vigyan Sadan Block, Vigyan Dham, Dehradun – 248007 | Tel: +91-0135-2976266 | dg@ucost.in
- **Co-PI:** Dr. Devi Prashad Uniyal, Joint Director, UCOST | Mobile: +91-9837862069 | dpuniyal.ucost@gmail.com
- **Co-PI:** Dr. Manmohan Singh Rawat, Scientific Officer, UCOST | Tel: +91-9368399447 | manmohansinghrwt@gmail.com
- **Project Staff:** Mr. Nalin Sharma (Principal Project Associate), Mr. Devendra Singh (Principal Project Associate), Mr. Ankit Kandiyal (Senior Project Associate), Mr. Kumar Roshan (Project Associate), Ms. Rukhsar (Project Associate), Mr. Shailender Rautela (Project Assistant)

**Sidebar Contact widget** (smaller, persistent) — update with the same correct address/phone/email as above (use the PI's primary line as the headline contact, others below in smaller text). Additional source folder: `C:\Users\saksh\OneDrive\Desktop\cs\contact us` — use it if it contains anything beyond the above (e.g. a confirmed map embed).

## 10. Events & Activity (replaces "Latest News & Events")
Rename the section and change the content model from news-article style to event/activity style: date, title, short description, optional thumbnail, link to its own detail page (Section 11). Search functionality must work the same way the current News & Events search does — filter the list live. Event data (folder per event, each with title/detail/images) will be provided separately/shortly — build the section and template now so it's ready to receive that data without further code changes (see Section 12, content-driven architecture).

## 11. Shared Detail-Page Template
Build one reusable detail-page template (shares the global header/footer) used by: each About Us entry, each What's New item, and each Events & Activity item. Renders: title, full detail text body, associated photo set. Routes dynamically per item (e.g. `/about/[slug]`, `/whats-new/[slug]`, `/events/[slug]`).

## 12. Content-Driven Architecture (apply this as the underlying build pattern, not an afterthought)
So future updates (new photos, new events, new links, new team members) require **editing a data file only — never touching component code**:

1. Create a `/content` directory at the project root with one JSON file per dynamic section:
   - `content/photos.json` — `{ filename, caption, highlight }[]`. Images live in `/assets/photos/`.
   - `content/events.json` — `{ slug, title, date, summary, detailText, images[] }[]`. Auto-generates detail pages via dynamic routing.
   - `content/whats-new.json` — same shape as events.
   - `content/quick-links.json` — `{ name, url, logo }[]`.
   - `content/team.json` — `{ tier: 'PI'|'Co-PI'|'Staff', name, role, photo? }[]`.
   - `content/portals.json` — `{ name, url, logo }[]` for Related Portals.
2. All components read from these JSON files rather than hardcoding arrays/JSX per item.
3. New JSON entries must produce new live pages/tiles automatically — zero additional code per new item.
4. Write a short `content/README.md` explaining the exact JSON shape per file and confirming no code changes are needed for routine content updates.
5. Use plain JSON + the existing routing/rendering approach already in this repo (it's currently plain HTML/CSS/JS) — don't introduce a new framework or CMS just for this.

## 13. Project Leadership & Team — full replacement
Remove the entire old roster (Project Coordinators Dr. D.P. Uniyal & Dr. M.S. Rawat + 6-person Project Team of Santosh Rawat, Sunil Tewari, Punit Singh, Gaurav Chamoli, Paras Upadhayay, Urmila Ghildiyal with initials-avatar cards DU/MR/SR/ST/PS/GC/PU/UG).

Build the new roster, grouped in three tiers, keeping the existing initials-avatar card layout style:
- **PI:** Prof. (Dr.) Durgesh Pant — Director General, Uttarakhand State Council for Science & Technology (UCOST), Government of Uttarakhand, Vigyan Dham, Jhajra, Dehradun
- **Co-PI:** Dr. D. P. Uniyal — Joint Director, UCOST, Government of Uttarakhand, Vigyan Dham, Jhajra, Dehradun
- **Co-PI:** Dr. M. S. Rawat — Scientific Officer, UCOST, Government of Uttarakhand, Vigyan Dham, Jhajra, Dehradun
- **Project Staff:**
  - Mr. Devendra Singh — Principal Project Associate
  - Mr. Nalin Sharma — Principal Project Associate
  - Mr. Ankit Kandiyal — Senior Project Associate
  - Ms. Rukhsar — Project Associate
  - Mr. Kumar Roshan — Project Associate
  - Mr. Shalinder Rautela — Project Assistant

Cross-reference `Final_SC_ST_Cell_UCOST.pptx` and `Nalin_Sharma_SC-St_Cell_Project_Progress.pptx` (both provided in the project) for any additional detail, photos, or supporting context on these individuals or the project — treat both decks as supplementary reference material only; the roster above is authoritative and must not be altered based on the decks.

## 14. Objectives, Methodology & Deliverables
Update the existing tabbed structure with this content verbatim:

**Objectives (10):**
1. To assess the livelihood system for sustainable livelihood planning through science, know-how and practices.
2. To capture traditional and indigenous knowledge and upgrade the skill, building on local innovation and local knowledge system.
3. Establishment of database of promising technologies that can be taken up for widespread adaption.
4. Mapping of the above data and resources of spatial domain.
5. To act as coordination cell to promote adaption of appropriate and relevant technologies for socio-economic development of target development.
6. Promotion, replication and scaling up of successful technologies leading to socio-economic employment of capacity building.
7. Development of programs and projects for strengthening human & institutional capacities and technology development.
8. Human Resource development of SC/ST Community.
9. Establishment of site-based skill development centre.
10. Identification of gaps in existing government/non-government schemes.

**Methodology:**
> Site-specific priority areas across Uttarakhand's varying geography, with need-based interventions for socio-economic upliftment via: Food Preservation Unit (Horticulture & Agriculture Products), Artisan & Handicrafts Unit, Scientific Gazettes Preparation Unit (including indigenous/traditional knowledge testing, product quality validation and market linkage), and Mapping through Remote Sensing (RS) & Geographical Information System (GIS).

**Deliverables:**
1. Human Resource Development of SC/ST Community.
2. Establishment of Site-based Skill Development Centre.
3. Identification of Gaps in Existing Government/Non-Government Schemes.
4. Formulation, Strengthening, Coordination & Documentation of programmes/Projects for filling gaps through S&T interventions.
5. The proposed model, developed through S&T intervention in SC/ST areas, is designed to be replicable elsewhere.

## 15. Important Links → UCOST Map
Remove the "Important Links" block entirely. Replace with an embedded map showing the UCOST office location: `https://maps.app.goo.gl/Jug9zk8YkKdKFj947`. Embed as an interactive map (Google Maps iframe) with a "Get Directions" link out to the same URL.

## 16. Related Portals
Update and correctly hyperlink the Related Portals block. Current placeholder set (confirm/replace if you have a more current list): DST, MeitY, Digital India, MyGov, SEED — link each to its respective official domain.

## 17. Mobile View
Full responsive audit and fix pass across every section above — header controls, branding row, nav collapse, hero (including the scroll-dock interaction — degrade gracefully on mobile, e.g. skip the dock effect and just autoplay normally), photo grid, Quick Links carousel (touch-swipe friendly), sidebar blocks, About Us / What's New / Events detail pages, map embed, and footer. Do this last, after all other sections are rebuilt, since it depends on final layouts.

---

## FINAL QA CHECKLIST (run this repeatedly per the Loop Prompting instructions above)

- [ ] Top logo renders correctly at all breakpoints
- [ ] Screen reader toggle is functional, not decorative
- [ ] A-/A/A+ functionally resizes all site text
- [ ] UK logo, search bar, and old council-name block removed from branding row; "SC / ST Cell" wordmark in place and styled
- [ ] Nav shows exactly Home | About Us | Contact Us
- [ ] Home links externally to ucost.uk.gov.in
- [ ] About Us has exactly 2 sub-pages (UCOST, SC/ST Cell), each with full verbatim text on its own themed page
- [ ] Social media row shows only FB/X/YT/LI with correct links; no dead/placeholder icons
- [ ] Hero video is the new file, autoplays, loops, muted
- [ ] Hero scroll-dock interaction works on desktop and degrades gracefully on mobile
- [ ] Photo section shows all 80 images, captioned, with highlighted subset and working "Explore All Media"
- [ ] Quick Links carousel auto-scrolls, has functional up/down arrows, pauses on manual interaction, all 8 logos link out correctly in new tabs
- [ ] Quick Links and What's New blocks are swapped in position from their original layout
- [ ] What's New shows at least the recruitment-ad item with its own detail page
- [ ] Contact Us (main page) shows all PI/Co-PI/Staff details correctly
- [ ] Contact Us (sidebar widget) shows correct condensed info
- [ ] Events & Activity section renamed and restructured, search works, template ready even if event data is still pending
- [ ] Shared detail-page template used consistently across About Us / What's New / Events, matching global theme
- [ ] `/content` JSON files exist for photos, events, whats-new, quick-links, team, portals — with a README explaining the no-code update workflow
- [ ] Leadership & Team shows the full new 9-person roster with old roster completely removed
- [ ] Objectives (10), Methodology, and Deliverables (5) all present verbatim
- [ ] Important Links block replaced with working UCOST map embed + directions link
- [ ] Related Portals correctly linked
- [ ] Full mobile responsive pass complete across every section
- [ ] No console errors, no broken links, no missing-image icons anywhere on the site

If any checklist item cannot be completed because required data/assets are missing (e.g. Events & Activity folder not yet provided, Related Portals final list unconfirmed), mark it explicitly as **Blocked — awaiting [X]** in your final output rather than leaving it silently incomplete.
