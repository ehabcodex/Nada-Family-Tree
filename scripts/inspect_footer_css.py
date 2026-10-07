import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'footer\b[^{]*\{[^}]*\}', text))
print("Footer CSS matches:")
for m in matches:
    print(m.group(0))
