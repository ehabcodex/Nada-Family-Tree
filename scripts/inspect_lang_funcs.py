import sys, re
sys.stdout.reconfigure(encoding='utf-8')
from extract_funcs import extract_function

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- toggleLanguage ---")
print(extract_function(text, 'toggleLanguage'))

print("--- setLanguage ---")
print(extract_function(text, 'setLanguage'))

print("--- applyTranslations ---")
print(extract_function(text, 'applyTranslations'))
