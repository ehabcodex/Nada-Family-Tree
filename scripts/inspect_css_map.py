import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

style_start = text.find('<style>')
style_end = text.find('</style>')
css = text[style_start:style_end]

# Find all comments with their line numbers
for m in re.finditer(r'/\*.*?\*/', css, re.DOTALL):
    c = m.group(0)
    if '\n' in c and len(c) > 100:
        continue # skip long blocks
    pos = m.start()
    line_no = css[:pos].count('\n') + 1
    print(f"Line {line_no:4d}: {c.strip()[:65]}")
