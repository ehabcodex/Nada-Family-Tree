import sys
sys.stdout.reconfigure(encoding='utf-8')
from extract_funcs import extract_function

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- openModal ---")
print(extract_function(text, 'openModal'))
print("--- closeModal ---")
print(extract_function(text, 'closeModal'))
