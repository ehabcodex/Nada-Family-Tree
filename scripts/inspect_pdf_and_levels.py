import sys
sys.stdout.reconfigure(encoding='utf-8')
from extract_funcs import extract_function

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- printOrExportPDF ---")
print(extract_function(text, 'printOrExportPDF'))

print("\n--- Level styling in CSS ---")
import re
levels = re.findall(r'\.tree-node\.level-\d+[^{]*\{[^}]*\}', text)
for l in levels:
    print(l)
