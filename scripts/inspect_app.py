import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text), "bytes")

# Find views / tab panes
views = re.findall(r'<div[^>]+id=["\']view-([^"\']+)["\'][^>]*>', text)
print("Views:", views)

# Find modals
modals = re.findall(r'<div[^>]+id=["\']([^"\']*modal[^"\']*)["\'][^>]*>', text, re.IGNORECASE)
print("Modals:", modals)

# Find tree container
tree_m = re.findall(r'<div[^>]+id=["\']([^"\']*tree[^"\']*)["\'][^>]*>', text, re.IGNORECASE)
print("Tree elements:", tree_m)

# Find table elements
table_m = re.findall(r'<table[^>]*>', text)
print("Tables count:", len(table_m))
for m in re.finditer(r'<table[^>]+id=["\']([^"\']+)["\'][^>]*>', text):
    print("Table ID:", m.group(1))

# Check Chart/Stats containers
stats_m = re.findall(r'<div[^>]+id=["\']([^"\']*chart[^"\']*)["\'][^>]*>', text, re.IGNORECASE)
print("Chart containers:", stats_m)
