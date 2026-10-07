import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function renderTableView')
print('In bak:', pos)
print(text[pos:pos+800])
