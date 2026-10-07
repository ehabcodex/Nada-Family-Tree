import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

users_block = re.search(r'<div[^>]+id=["\']view-users["\'].*?</main>', text, re.DOTALL)
if users_block:
    for m in re.finditer(r'<table[^>]*id=["\']([^"\']+)["\'][^>]*>', users_block.group(0)):
        print('Table in users:', m.group(1))

    # Also let's see tbody IDs
    for m in re.finditer(r'<tbody[^>]*id=["\']([^"\']+)["\'][^>]*>', users_block.group(0)):
        print('Tbody in users:', m.group(1))

# Check table headers for users and audit log
for m in re.finditer(r'<h3[^>]*>(.*?)</h3>', users_block.group(0) if users_block else ""):
    print('H3 in users:', m.group(1))
