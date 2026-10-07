import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("filterTable pos:", text.find('filterTable'))
print("tableCurrentPage pos:", text.find('tableCurrentPage'))
print("renderBranchesView pos:", text.find('function renderBranchesView'))
print("renderStatsView pos:", text.find('function renderStatsView'))
