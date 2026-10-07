import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect renderTableView
m = re.search(r'function renderTableView\b.*?\n\}', text, re.DOTALL)
if m:
    print("--- renderTableView ---")
    print(m.group(0)[:1500])

# Let's inspect initPanZoom
m2 = re.search(r'function initPanZoom\b.*?\n\}', text, re.DOTALL)
if m2:
    print("\n--- initPanZoom ---")
    print(m2.group(0)[:1500])
