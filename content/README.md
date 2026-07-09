# Content Data Layer — SC/ST Cell Portal

This directory contains all structured content for the SC/ST Cell Portal. The site uses a **content-driven architecture**: the UI reads these JSON files at runtime, so adding or editing content requires **no code changes** — just edit the relevant JSON file.

---

## Architecture Overview

```
content/
├── photos.json        # Photo gallery entries (80 photos)
├── quick-links.json   # External quick-link portals with logos
├── team.json          # Team roster (PI, Co-PI, Staff)
├── events.json        # Upcoming/past events
├── whats-new.json     # Announcements & news items
├── portals.json       # Government portal links (ticker bar)
└── README.md          # This file

assets/
├── photos/            # 80 photo images referenced by photos.json
└── links/             # Logo images referenced by quick-links.json
```

---

## JSON File Schemas

### `photos.json`

Array of photo objects for the gallery section.

| Field       | Type    | Description                                                       |
|-------------|---------|-------------------------------------------------------------------|
| `filename`  | string  | Exact image filename in `assets/photos/` (case-sensitive)         |
| `caption`   | string  | Display caption derived from the filename (without extension)     |
| `highlight` | boolean | `true` = featured in the hero/highlights carousel; `false` = gallery only |

**Example:**
```json
{ "filename": "AIPAN.jpg", "caption": "AIPAN", "highlight": true }
```

---

### `quick-links.json`

Array of external portal links shown in the Quick Links section.

| Field  | Type   | Description                                            |
|--------|--------|--------------------------------------------------------|
| `name` | string | Display name of the portal                             |
| `url`  | string | Full URL to the external portal                        |
| `logo` | string | Logo image filename in `assets/links/` (case-sensitive)|

**Example:**
```json
{ "name": "Government of Uttarakhand", "url": "https://uk.gov.in/", "logo": "Government of Uttarakhand.png" }
```

---

### `team.json`

Array of team members grouped by tier.

| Field  | Type   | Description                                                   |
|--------|--------|---------------------------------------------------------------|
| `tier` | string | One of `"PI"`, `"Co-PI"`, or `"Staff"`                        |
| `name` | string | Full name with title (e.g., "Prof. (Dr.) Durgesh Pant")       |
| `role` | string | Designation / job title                                       |
| `org`  | string | *(optional)* Organization & address — present for PI/Co-PI only |

**Example:**
```json
{ "tier": "Staff", "name": "Mr. Ankit Kandiyal", "role": "Senior Project Associate" }
```

---

### `events.json`

Array of event objects. Currently empty — add entries as events are scheduled.

| Field       | Type   | Description                            |
|-------------|--------|----------------------------------------|
| `title`     | string | Event title                            |
| `date`      | string | ISO 8601 date (`YYYY-MM-DD`)           |
| `location`  | string | Venue / location                       |
| `summary`   | string | Short description of the event         |

**Example:**
```json
{ "title": "Workshop on Tribal Welfare", "date": "2024-03-15", "location": "UCOST, Dehradun", "summary": "One-day workshop on..." }
```

---

### `whats-new.json`

Array of announcement / news items shown in the "What's New" section.

| Field        | Type     | Description                                         |
|--------------|----------|-----------------------------------------------------|
| `slug`       | string   | URL-friendly identifier (kebab-case)                |
| `title`      | string   | Headline of the announcement                        |
| `date`       | string   | ISO 8601 date (`YYYY-MM-DD`)                        |
| `summary`    | string   | Short summary for list/card views                   |
| `detailText` | string   | Full announcement text (supports `\n` for newlines) |
| `images`     | string[] | Array of image filenames (can be empty)              |

**Example:**
```json
{
  "slug": "scst-cell-recruitment-2023",
  "title": "SC/ST Cell Project Staff Recruitment — Walk-in Interview",
  "date": "2023-08-10",
  "summary": "Principal Project Associate walk-in interview at UCOST...",
  "detailText": "Full text here...",
  "images": []
}
```

---

### `portals.json`

Array of government portal links shown in the scrolling ticker / footer bar.

| Field  | Type   | Description                         |
|--------|--------|-------------------------------------|
| `name` | string | Full portal name                    |
| `url`  | string | Full URL to the portal              |
| `abbr` | string | Short abbreviation for compact views|

**Example:**
```json
{ "name": "Digital India", "url": "https://www.digitalindia.gov.in/", "abbr": "Digital India" }
```

---

## How to Add New Entries

1. **Open** the relevant JSON file in any text editor.
2. **Add** a new object to the array following the schema above.
3. **Save** the file — the site will pick up changes automatically (no rebuild needed).

### Adding a new photo:
1. Place the image file in `assets/photos/`.
2. Add an entry to `photos.json`:
   ```json
   { "filename": "NEW_PHOTO.jpg", "caption": "New Photo Caption", "highlight": false }
   ```

### Adding a new quick link:
1. Place the logo image in `assets/links/`.
2. Add an entry to `quick-links.json`:
   ```json
   { "name": "Portal Name", "url": "https://example.gov.in/", "logo": "logo-filename.png" }
   ```

### Adding a new team member:
Add an entry to `team.json`:
```json
{ "tier": "Staff", "name": "Ms. New Member", "role": "Project Associate" }
```

### Adding a new announcement:
Add an entry to `whats-new.json` with all required fields.

### Adding a new event:
Add an entry to `events.json` following the schema.

---

## File Organization

| Directory        | Contents                                    |
|------------------|---------------------------------------------|
| `assets/photos/` | 80 photo images referenced by `photos.json` |
| `assets/links/`  | Logo images referenced by `quick-links.json`|
| `content/`       | All JSON data files + this README           |
