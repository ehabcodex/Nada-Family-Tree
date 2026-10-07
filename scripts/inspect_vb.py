import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="view-branches"')
print("pos of view-branches:", pos)
if pos != -1:
    print(text[pos-300:pos+100])
