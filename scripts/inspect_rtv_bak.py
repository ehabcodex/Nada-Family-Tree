import sys
sys.stdout.reconfigure(encoding='utf-8')
from extract_funcs import extract_function

with open('index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

print(extract_function(text, 'renderTreeView'))
