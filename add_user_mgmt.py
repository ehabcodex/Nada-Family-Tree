# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update table action button text
old_btn = '✏️ ${isAuthorized() ? \'تعديل\' : \'عرض\'}'
new_btn = '✏️ ${isAuthorized() ? (currentLanguage === \'ar\' ? \'تعديل\' : \'Edit\') : (currentLanguage === \'ar\' ? \'عرض\' : \'View\')}'
if old_btn in content:
    content = content.replace(old_btn, new_btn)

# 2. Update updateAuthUI to add Manage Editors button
old_auth_ui = """        container.innerHTML = `
          <div class="auth-badge">
            <span>🟢</span>
            <span>${t.editorBadge} ${currentUser.displayName}</span>
            <button class="btn btn-sm" onclick="logout()" style="margin-inline-start: 6px; padding: 2px 6px;">${t.logout}</button>
          </div>
        `;"""

new_auth_ui = """        container.innerHTML = `
          <div class="auth-badge">
            <span>🟢</span>
            <span>${t.editorBadge} ${currentUser.displayName}</span>
            <button class="btn btn-sm" onclick="openManageUsersModal()" style="margin-inline-start: 6px; padding: 2px 6px; font-size: 0.75rem;" title="إدارة المحررين وتغيير الرمز السري">⚙️ ${currentLanguage === 'ar' ? 'إدارة الصلاحيات' : 'Manage Editors'}</button>
            <button class="btn btn-sm" onclick="logout()" style="margin-inline-start: 6px; padding: 2px 6px;">${t.logout}</button>
          </div>
        `;"""

if old_auth_ui in content:
    content = content.replace(old_auth_ui, new_auth_ui)

# 3. Add Manage Users modal right after login-modal
manage_modal_html = """
  <!-- MANAGE USERS MODAL -->
  <div class="modal-backdrop" id="manage-users-modal">
    <div class="modal-window" style="max-width: 480px;">
      <div class="modal-header">
        <h3>⚙️ إدارة صلاحيات المحررين</h3>
        <button class="modal-close" onclick="closeModal('manage-users-modal')">&times;</button>
      </div>
      <div class="modal-body">
        <div style="background: var(--bg-card-subtle); padding: 12px; border-radius: 8px; margin-bottom: 16px; border: 1px solid var(--border);">
          <h4 style="font-size: 0.9rem; margin-bottom: 8px; color: var(--primary);">🔑 تغيير كلمة المرور لحسابك (<span id="my-username-display"></span>)</h4>
          <div class="form-group" style="margin-bottom: 8px;">
            <input type="password" id="new-password-input" class="form-input" placeholder="أدخل كلمة المرور الجديدة">
          </div>
          <button class="btn btn-sm btn-primary" onclick="changeMyPassword()">حفظ كلمة المرور الجديدة</button>
        </div>

        <div>
          <h4 style="font-size: 0.9rem; margin-bottom: 8px; color: var(--primary);">👥 قائمة المحررين المعتمدين</h4>
          <div id="editors-list-container" style="margin-bottom: 14px;"></div>

          <details style="background: var(--bg-card-subtle); padding: 10px; border-radius: 8px; border: 1px solid var(--border);">
            <summary style="font-weight: 600; cursor: pointer; color: var(--text);">➕ إضافة محرر معتمد جديد</summary>
            <div style="margin-top: 10px; display: flex; flex-direction: column; gap: 8px;">
              <input type="text" id="new-editor-username" class="form-input" placeholder="اسم المستخدم بالإنجليزية (مثال: ahmad)">
              <input type="text" id="new-editor-display" class="form-input" placeholder="الاسم الظاهر (مثال: أحمد ندى)">
              <input type="password" id="new-editor-pwd" class="form-input" placeholder="كلمة المرور">
              <button class="btn btn-sm btn-primary" onclick="addNewEditor()">إضافة المحرر لقائمة المصرح لهم</button>
            </div>
          </details>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn" onclick="closeModal('manage-users-modal')">إغلاق</button>
      </div>
    </div>
  </div>
"""

target_after_login_modal = '  </div>\n\n  <!-- Toast -->'
if target_after_login_modal in content and 'id="manage-users-modal"' not in content:
    content = content.replace(target_after_login_modal, '  </div>\n' + manage_modal_html + '\n  <!-- Toast -->')

# 4. Add manage editors JS functions
manage_funcs_js = """
    // =========================================================================
    // Manage Authorized Users
    // =========================================================================
    function openManageUsersModal() {
      if (!currentUser) return;
      document.getElementById('my-username-display').textContent = currentUser.displayName || currentUser.username;
      document.getElementById('new-password-input').value = '';
      renderManageUsersList();
      openModal('manage-users-modal');
    }

    function renderManageUsersList() {
      const container = document.getElementById('editors-list-container');
      const creds = JSON.parse(localStorage.getItem(LS_ADMIN_CREDS_KEY)) || DEFAULT_ADMIN_USERS;
      let html = '<ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px;">';
      creds.forEach(u => {
        const isCurrent = currentUser && currentUser.username.toLowerCase() === u.username.toLowerCase();
        html += `
          <li style="display: flex; justify-content: space-between; align-items: center; padding: 8px 10px; background: var(--bg-card); border: 1px solid var(--border); border-radius: 6px; font-size: 0.85rem;">
            <div>
              <strong>${u.displayName}</strong> <span style="color: var(--text-muted);">(@${u.username})</span>
              ${isCurrent ? '<span class="tag-badge" style="margin-inline-start: 4px; background: #dcfce7; color: #166534;">حسابك الحالي</span>' : ''}
            </div>
            ${u.username.toLowerCase() !== 'ehab' && !isCurrent ? `<button class="btn btn-sm" style="color: #ef4444; border-color: #ef4444; padding: 2px 6px;" onclick="removeEditor('${u.username}')">إزالة</button>` : ''}
          </li>
        `;
      });
      html += '</ul>';
      container.innerHTML = html;
    }

    function changeMyPassword() {
      const newPwd = document.getElementById('new-password-input').value.trim();
      if (!newPwd) {
        alert(currentLanguage === 'ar' ? 'يرجى كتابة كلمة مرور جديدة.' : 'Please enter a new password.');
        return;
      }
      let creds = JSON.parse(localStorage.getItem(LS_ADMIN_CREDS_KEY)) || DEFAULT_ADMIN_USERS;
      const idx = creds.findIndex(u => u.username.toLowerCase() === currentUser.username.toLowerCase());
      if (idx !== -1) {
        creds[idx].password = newPwd;
      } else {
        creds.push({ username: currentUser.username, displayName: currentUser.displayName, password: newPwd });
      }
      localStorage.setItem(LS_ADMIN_CREDS_KEY, JSON.stringify(creds));
      document.getElementById('new-password-input').value = '';
      showToast(currentLanguage === 'ar' ? 'تم تحديث كلمة المرور بنجاح!' : 'Password updated successfully!');
    }

    function addNewEditor() {
      const u = document.getElementById('new-editor-username').value.trim().toLowerCase();
      const d = document.getElementById('new-editor-display').value.trim();
      const p = document.getElementById('new-editor-pwd').value.trim();

      if (!u || !d || !p) {
        alert(currentLanguage === 'ar' ? 'يرجى ملء جميع الحقول لإضافة محرر جديد.' : 'Please fill all fields.');
        return;
      }

      let creds = JSON.parse(localStorage.getItem(LS_ADMIN_CREDS_KEY)) || DEFAULT_ADMIN_USERS;
      if (creds.some(item => item.username.toLowerCase() === u)) {
        alert(currentLanguage === 'ar' ? 'اسم المستخدم هذا مسجل مسبقاً.' : 'Username already exists.');
        return;
      }

      creds.push({ username: u, displayName: d, password: p });
      localStorage.setItem(LS_ADMIN_CREDS_KEY, JSON.stringify(creds));
      document.getElementById('new-editor-username').value = '';
      document.getElementById('new-editor-display').value = '';
      document.getElementById('new-editor-pwd').value = '';
      renderManageUsersList();
      showToast(currentLanguage === 'ar' ? `تمت إضافة المحرر (${d}) بنجاح!` : `Editor added successfully!`);
    }

    function removeEditor(uname) {
      if (!confirm(currentLanguage === 'ar' ? `هل أنت متأكد من إزالة صلاحية المحرر (${uname})؟` : `Remove editor ${uname}?`)) return;
      let creds = JSON.parse(localStorage.getItem(LS_ADMIN_CREDS_KEY)) || DEFAULT_ADMIN_USERS;
      creds = creds.filter(u => u.username.toLowerCase() !== uname.toLowerCase());
      localStorage.setItem(LS_ADMIN_CREDS_KEY, JSON.stringify(creds));
      renderManageUsersList();
      showToast(currentLanguage === 'ar' ? 'تم حذف المحرر من الصلاحيات' : 'Editor removed');
    }
"""

target_before_theme = '    // =========================================================================\n    // Theme Management'
if target_before_theme in content and 'openManageUsersModal' not in content:
    content = content.replace(target_before_theme, manage_funcs_js + '\n    // =========================================================================\n    // Theme Management')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html successfully with editor management features!')
