import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Find line numbers of key tags
markers = [
    '<!DOCTYPE', '<head', '<link', '<style', '</style>',
    '<body', '<header', '</header>', '<div class="stats-bar"',
    '<div class="nav-search-bar"', '<main', '<div id="view-tree"',
    '<div id="view-branches"', '<div id="view-table"', '<div id="view-stats"',
    '<div id="view-users"', '</main>', '<div class="modal-backdrop"',
    'id="member-modal"', 'id="add-modal"', 'id="login-modal"',
    'id="manage-users-modal"', 'id="user-form-modal"', 'id="user-pwd-modal"',
    '<script', 'function loadSavedState', 'function renderTableView',
    'function renderTreeView', 'function initPanZoom', 'function printOrExportPDF',
    '</script>', '</body>', '</html>'
]

for marker in markers:
    for i, line in enumerate(lines):
        if marker in line:
            print(f"{i+1:5d}: {line.strip()[:70]}")
            break
