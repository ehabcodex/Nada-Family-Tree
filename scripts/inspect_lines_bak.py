import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('/* Connector lines')
if pos != -1:
    print(text[pos:pos+2500])
else:
    print("Not found, searching for .ft-tree...")
    pos2 = text.find('.ft-tree')
    print(text[pos2:pos2+1500])
