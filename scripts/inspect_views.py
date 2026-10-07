import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check tables with their parents or IDs
for m in re.finditer(r'<table[^>]*id=["\']?([^"\'\s>]+)?["\']?[^>]*>', text):
    print("Table tag:", m.group(0))

# Check view-stats content
stats_block = re.search(r'<div[^>]+id=["\']view-stats["\'][^>]*>(.*?)</div>\s*<!--', text, re.DOTALL)
if stats_block:
    print("\n--- VIEW-STATS PREVIEW ---")
    print(stats_block.group(0)[:1500])

# Check view-table content
table_block = re.search(r'<div[^>]+id=["\']view-table["\'][^>]*>(.*?)</div>\s*<!--', text, re.DOTALL)
if table_block:
    print("\n--- VIEW-TABLE PREVIEW ---")
    print(table_block.group(0)[:1500])

# Check view-users content
users_block = re.search(r'<div[^>]+id=["\']view-users["\'][^>]*>(.*?)</div>\s*<!--', text, re.DOTALL)
if users_block:
    print("\n--- VIEW-USERS PREVIEW ---")
    print(users_block.group(0)[:1500])

# Check view-tree controls and toolbar
tree_block = re.search(r'<div[^>]+id=["\']view-tree["\'][^>]*>(.*?)<div[^>]+id=["\']tree-canvas["\']', text, re.DOTALL)
if tree_block:
    print("\n--- VIEW-TREE CONTROLS ---")
    print(tree_block.group(0)[:1500])
