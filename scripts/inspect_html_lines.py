import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1820, 2450):
    if i < len(lines):
        line = lines[i]
        # print non-empty tags or markers
        if any(k in line for k in ['<header', '</header', '<div class="stats-bar"', '<div class="nav-search-bar"', '<main', '</main', '<div class="modal', 'id="member-modal"', 'id="add-modal"', 'id="login-modal"', 'id="manage-users-modal"']):
            print(f"Line {i+1}: {line.strip()[:90]}")
