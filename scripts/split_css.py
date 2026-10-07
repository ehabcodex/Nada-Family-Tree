import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

style_start = text.find('<style>')
style_end = text.find('</style>')
css = text[style_start+7:style_end]

# Split css into sections based on comments
sections = re.split(r'/\*\s*([^/*\n]+)\s*\*/', css)
print("Sections count:", len(sections))
for i in range(1, len(sections), 2):
    title = sections[i].strip()
    content = sections[i+1].strip()
    print(f"Section '{title}': {len(content)} chars")
