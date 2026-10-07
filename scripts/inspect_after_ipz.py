import sys
sys.stdout.reconfigure(encoding='utf-8')
from extract_funcs import extract_function

with open('index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function initPanZoom()')
print("In bak, initPanZoom is at:", pos)
fn = extract_function(text, 'initPanZoom')
print("Length of initPanZoom:", len(fn))
after = text[pos + len(fn):pos + len(fn) + 500]
print("Right after initPanZoom in bak:")
print(after)
