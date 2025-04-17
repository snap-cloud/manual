import json
import os

# Load index entries
try:
    with open('_index_entries.json', 'r') as f:
        index_entries = json.load(f)
except:
    print("No index entries found")
    exit(0)

# Create markdown index file
with open('index-list.qmd', 'w', encoding='utf-8') as f:
    # Write index header
    f.write("""---
title: "Index"
---

""")

    # Sort terms alphabetically
    sorted_terms = sorted(index_entries.keys())

    # Group by first letter
    current_letter = None
    for term in sorted_terms:
        first_letter = term[0].upper()

        # Add letter heading when changing letter
        if first_letter != current_letter:
            current_letter = first_letter
            f.write(f"\n## {current_letter}\n\n")

        # Format term (replace hyphens with commas)
        formatted_term = term.replace('-', ', ')

        # Create links to pages
        page_links = []
        for entry in index_entries[term]:
            file_path = entry.get('file', '')
            page_title = entry.get('title', os.path.basename(file_path))

            if file_path:
                # Create link to the page
                page_links.append(f"[{page_title}]({file_path})")

        # Write the index entry
        f.write(f"**{formatted_term}** — {', '.join(page_links)}\n\n")

print("Index markdown generated successfully")
