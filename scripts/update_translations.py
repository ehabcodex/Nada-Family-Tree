# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = "document.querySelectorAll('.t-modal-add-title').forEach(el => el.textContent = t.modalAddTitle);"
additions = """      document.querySelectorAll('.t-modal-add-title').forEach(el => el.textContent = t.modalAddTitle);
      if (t.tabUsers) {
        document.querySelectorAll('.t-tab-users').forEach(el => el.textContent = t.tabUsers);
        document.querySelectorAll('.t-users-title').forEach(el => el.textContent = t.usersTitle);
        document.querySelectorAll('.t-users-subtitle').forEach(el => el.textContent = t.usersSubtitle);
        document.querySelectorAll('.t-add-user-btn').forEach(el => el.textContent = t.addUserBtn);
        document.querySelectorAll('.t-export-users-btn').forEach(el => el.textContent = t.exportUsersBtn);
        document.querySelectorAll('.t-import-users-btn').forEach(el => el.textContent = t.importUsersBtn);
      }"""

if target in content and 't.tabUsers' not in content:
    content = content.replace(target, additions)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Translations in applyTranslations updated successfully!')
