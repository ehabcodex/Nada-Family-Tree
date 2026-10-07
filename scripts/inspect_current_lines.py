import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('.ft-tree')
print("In index.html:")
print(text[pos:pos+1500])
