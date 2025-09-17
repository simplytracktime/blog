#!/usr/bin/env python3

import os
import re
import glob

# Change to content/post directory
os.chdir('content/post/')

# Process all .md files
for file in glob.glob('*.md'):
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract date (yyyy-mm-dd pattern)
        date_match = re.search(r"^date: [^T]*?(\d{4}-\d{2}-\d{2})", content, re.MULTILINE)
        date = date_match.group(1) if date_match else ""
        
        # Extract title
        title_match = re.search(r"^title: '(.*)'", content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
            # Convert to lowercase and replace non-alphanumeric with hyphens
            title = re.sub(r'[^a-z0-9]', '-', title.lower())
            # Remove multiple consecutive hyphens
            title = re.sub(r'-+', '-', title)
            # Remove leading/trailing hyphens
            title = title.strip('-')
        else:
            title = ""
        
        new_name = f"{date}-{title}.md"
        print(new_name)
        
        # Uncomment to actually rename files
        if date and title and file != new_name:
            print(f"Renaming {file} to {new_name}")
            os.rename(file, new_name)