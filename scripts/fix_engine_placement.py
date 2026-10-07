# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Read users_engine_js from inject_users_js.py
with open('inject_users_js.py', 'r', encoding='utf-8') as f:
    code_text = f.read()

import re
m = re.search(r'users_engine_js = """([\s\S]*?)"""', code_text)
assert m, 'users_engine_js not found'
users_engine_js = m.group(1)

target = '    // =========================================================================\n    // Theme Management'
assert target in content, 'target theme management not found'

content = content.replace(target, users_engine_js + '\n' + target)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Users engine successfully injected right above Theme Management!')
