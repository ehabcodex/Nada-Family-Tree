import sys
sys.stdout.reconfigure(encoding='utf-8')

def extract_function(text, fn_name):
    pos = text.find(f"function {fn_name}")
    if pos == -1:
        return f"Function {fn_name} not found"
    brace_open = text.find("{", pos)
    count = 1
    i = brace_open + 1
    while i < len(text) and count > 0:
        if text[i] == '{':
            count += 1
        elif text[i] == '}':
            count -= 1
        i += 1
    return text[pos:i]

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- filterTable ---")
print(extract_function(text, 'filterTable'))
