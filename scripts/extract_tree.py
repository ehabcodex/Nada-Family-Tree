import sys
sys.stdout.reconfigure(encoding='utf-8')
from extract_funcs import extract_function

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- renderTreeView ---")
print(extract_function(text, 'renderTreeView')[:1500])

print("\n--- renderNode ---")
print(extract_function(text, 'renderNode')[:1500])
