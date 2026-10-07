import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('/* Toast')
if pos != -1:
    print(text[pos:pos+800])
