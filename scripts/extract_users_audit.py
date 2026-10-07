import sys
sys.stdout.reconfigure(encoding='utf-8')

from extract_funcs import extract_function

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- renderUsersPage ---")
print(extract_function(text, 'renderUsersPage')[:1000])

print("\n--- renderAuditTable ---")
print(extract_function(text, 'renderAuditTable')[:1000])
