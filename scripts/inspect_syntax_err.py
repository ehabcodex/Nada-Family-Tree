import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('}, 300);')
print("pos of }, 300);:", pos)
if pos != -1:
    print(text[pos-200:pos+200])
