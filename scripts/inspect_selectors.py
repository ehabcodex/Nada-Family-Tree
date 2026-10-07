import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

style_start = text.find('<style>')
style_end = text.find('</style>')
css = text[style_start:style_end]

# Find all selectors
selectors = set()
for line in css.split('\n'):
    line = line.strip()
    if line.endswith('{') and not line.startswith('@') and not line.startswith('/*'):
        sel = line[:-1].strip()
        selectors.add(sel)

print(f"Total CSS rule blocks: {len(selectors)}")
sample = sorted(list(selectors))[:50]
for s in sample:
    print("  ", s)
