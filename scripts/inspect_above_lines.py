import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('/* Connector lines')
print(text[pos-1000:pos])
