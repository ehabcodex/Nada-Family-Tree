import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

body_part = text[42001:47729]
print("--- BODY TO MAIN ---")
print(body_part)
