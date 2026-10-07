import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('<!-- Branches View -->')
print("pos of Branches View:", pos)
if pos != -1:
    print(text[pos-250:pos])
