import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'تمت العملية بنجاح', text))
print("Occurrences of 'تمت العملية بنجاح':", len(matches))
for m in matches:
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 100)
    print("Match at pos:", m.start())
    print(text[start:end])
    print("-" * 50)
