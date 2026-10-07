import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# View branches
branches_block = re.search(r'<div[^>]+id=["\']view-branches["\'][^>]*>(.*?)</div>\s*<!--', text, re.DOTALL)
if branches_block:
    print("--- VIEW-BRANCHES ---")
    print(branches_block.group(0)[:1000])

# Users and Audit log details
users_block = re.search(r'<div[^>]+id=["\']view-users["\'][^>]*>(.*?)</main>', text, re.DOTALL)
if users_block:
    print("\n--- VIEW-USERS & LOG FULL ---")
    print(users_block.group(0)[:2000])
