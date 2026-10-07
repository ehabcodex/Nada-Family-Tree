import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'\.toast\b[^{]*\{[^}]*\}', text))
print("Occurrences of .toast CSS:", len(matches))
for m in matches:
    print(m.group(0))

if len(matches) == 0:
    print("NO .toast CSS found in stylesheet! That is why the toast is visible by default!")
