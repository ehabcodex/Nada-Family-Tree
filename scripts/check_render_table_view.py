with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('renderTableView')
print("Position of renderTableView:", pos)
if pos != -1:
    print(text[pos-100:pos+300])
else:
    print("NOT FOUND in index.html!")
