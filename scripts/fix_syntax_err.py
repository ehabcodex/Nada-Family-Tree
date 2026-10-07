import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

bad_snippet = """    function printOrExportPDF() {
      exportToPDF();
    }, 300);
    }"""

good_snippet = """    function printOrExportPDF() {
      exportToPDF();
    }"""

if bad_snippet in text:
    text = text.replace(bad_snippet, good_snippet)
    print("Fixed bad syntax snippet successfully!")
else:
    # Try finding the bad part
    pos = text.find('}, 300);\n    }')
    if pos != -1:
        text = text[:pos] + text[pos+15:]
        print("Removed leftover 300ms timer.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved fixed index.html.")
