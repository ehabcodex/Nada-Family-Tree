import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find TRANSLATIONS dictionary
m = re.search(r'const\s+TRANSLATIONS\s*=\s*(\{.*?\});\s*(?:let|var|const|function)', text, re.DOTALL)
if m:
    print("Found TRANSLATIONS:")
    print(m.group(1)[:1200])
else:
    # search where translations are defined
    m2 = re.search(r'TRANSLATIONS', text)
    if m2:
        print("TRANSLATIONS at:", m2.start())
        print(text[m2.start():m2.start()+1000])
