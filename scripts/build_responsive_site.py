import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

# Read original index.html
with open('index.html.bak', 'r', encoding='utf-8') as f:
    orig_html = f.read()

print(f"Loaded index.html.bak ({len(orig_html)} characters)")
