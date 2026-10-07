import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all function definitions in the script
script_match = re.search(r'<script>(.*?)</script>', text, re.DOTALL)
if script_match:
    script_text = script_match.group(1)
    funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', script_text)
    print("Total functions:", len(funcs))
    print("Function names:", funcs[:50])

    # Let's search for functions related to table, tree, users, audit, modals, mobile
    keywords = ['Table', 'Tree', 'Users', 'Audit', 'render', 'Modal', 'filter', 'search', 'mobile', 'touch', 'pinch']
    for kw in keywords:
        matched = [fn for fn in funcs if kw.lower() in fn.lower()]
        print(f"Functions matching '{kw}':", matched)
