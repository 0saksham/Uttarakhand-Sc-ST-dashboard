import os
import re
import shutil
import json
import pypdf

# Define source and destination paths
source_dir = r"C:\Users\saksh\OneDrive\Desktop\cs\content\events-source"
dest_assets_dir = r"C:\Users\saksh\OneDrive\Desktop\cs\assets\events"
events_json_path = r"C:\Users\saksh\OneDrive\Desktop\cs\content\events.json"

replacements = {
    'Ɵ': 'ti',
    'ﬁ': 'fi',
    'ƫ': 'tti',
    'Ʃ': 'tt',
    '“': '"',
    '”': '"',
    '’': "'",
    '‘': "'"
}

def clean_text(text):
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def parse_date_string(date_line):
    dstr = re.sub(r'^date:\s*', '', date_line, flags=re.IGNORECASE).strip()
    months = {
        'january': '01', 'february': '02', 'march': '03', 'april': '04',
        'may': '05', 'june': '06', 'july': '07', 'august': '08',
        'september': '09', 'october': '10', 'november': '11', 'december': '12',
        'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'jun': '06',
        'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'
    }
    match = re.search(r'(\d+)(?:st|nd|rd|th)?(?:\s*-\s*\d+(?:st|nd|rd|th)?)?\s+([A-Za-z]+),?\s+(\d{4})', dstr)
    if match:
        day_str = match.group(1).zfill(2)
        month_name = match.group(2).lower()
        year_str = match.group(3)
        month_str = months.get(month_name, '01')
        return f"{year_str}-{month_str}-{day_str}"
    match_may = re.search(r'(\d+)(?:st|nd|rd|th)?\s+([A-Za-z]+)\s+(\d{4})', dstr)
    if match_may:
        day_str = match_may.group(1).zfill(2)
        month_name = match_may.group(2).lower()
        year_str = match_may.group(3)
        month_str = months.get(month_name, '01')
        return f"{year_str}-{month_str}-{day_str}"
    return None

def get_slug(title):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug).strip('-')
    return slug

def get_summary(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    summary = " ".join(sentences[:2]).strip()
    if len(summary) > 200:
        summary = summary[:197] + "..."
    return summary

events_data = []

for item in os.listdir(source_dir):
    item_path = os.path.join(source_dir, item)
    if os.path.isdir(item_path):
        pdf_path = os.path.join(item_path, "CONTENT.pdf")
        if os.path.exists(pdf_path):
            print(f"Processing event folder: {item}")
            # Extract text
            reader = pypdf.PdfReader(pdf_path)
            full_text = "\n".join([p.extract_text() for p in reader.pages])
            cleaned = clean_text(full_text)
            
            lines = [l.strip() for l in cleaned.split('\n')]
            
            title_lines = []
            metadata_seen = False
            date_line = ""
            
            for line in lines:
                if not line:
                    continue
                if any(line.startswith(prefix) for prefix in ["Date:", "Location:", "Venue:", "LocaƟon:", "Loca"]):
                    metadata_seen = True
                    if line.startswith("Date:"):
                        date_line = line
                    continue
                if not metadata_seen:
                    title_lines.append(line)
            
            title = " ".join(title_lines).strip().strip('"').strip("'")
            
            # The body is all lines after the metadata block
            # Let's find the index where metadata started
            body_lines = []
            meta_started = False
            for line in lines:
                if not line:
                    continue
                if any(line.startswith(prefix) for prefix in ["Date:", "Location:", "Venue:", "LocaƟon:", "Loca"]):
                    meta_started = True
                    continue
                if meta_started:
                    body_lines.append(line)
            
            detailText = " ".join(body_lines).strip()
            detailText = re.sub(r'\s+', ' ', detailText)
            
            slug = get_slug(title)
            date_val = parse_date_string(date_line) if date_line else None
            summary = get_summary(detailText)
            
            # Copy images
            event_assets_dest = os.path.join(dest_assets_dir, slug)
            os.makedirs(event_assets_dest, exist_ok=True)
            
            images_list = []
            for file_name in sorted(os.listdir(item_path)):
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')) and file_name.lower() != 'content.pdf':
                    src_file = os.path.join(item_path, file_name)
                    dest_file = os.path.join(event_assets_dest, file_name)
                    shutil.copy2(src_file, dest_file)
                    # Store relative path for web
                    images_list.append(f"assets/events/{slug}/{file_name}")
            
            event_entry = {
                "slug": slug,
                "title": title,
                "summary": summary,
                "detailText": detailText,
                "images": images_list
            }
            if date_val:
                event_entry["date"] = date_val
                
            events_data.append(event_entry)

# Sort events descending by date
events_data.sort(key=lambda x: x.get('date', '1970-01-01'), reverse=True)

# Write to events.json
with open(events_json_path, 'w', encoding='utf-8') as f:
    json.dump(events_data, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(events_data)} events. events.json updated.")
