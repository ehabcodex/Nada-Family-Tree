import sys, re
sys.stdout.reconfigure(encoding='utf-8')
from extract_funcs import extract_function

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

funcs = ['initPanZoom', 'switchTab', 'updateAuthUI', 'filterTable', 'handleSearch']
for fn in funcs:
    code = extract_function(text, fn)
    print(f"Function {fn}: {len(code)} chars, start: {text.find('function ' + fn)}")
