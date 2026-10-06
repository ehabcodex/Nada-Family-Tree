# -*- coding: utf-8 -*-
"""
Script to inject user management logic and audit trail into index.html
"""
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -----------------------------------------------------------------------------
# 1. Update DEFAULT_ADMIN_USERS & add LS_AUDIT_LOG_KEY
# -----------------------------------------------------------------------------
old_default_users = """    const DEFAULT_ADMIN_USERS = [
      { username: 'ehab', displayName: 'إيهاب ندى', password: '1234' },
      { username: 'admin', displayName: 'إدارة آل ندى', password: '1234' }
    ];"""

new_default_users = """    const DEFAULT_ADMIN_USERS = [
      {
        username: 'ehab',
        displayName: 'إيهاب ندى',
        displayNameEn: 'Ehab Nada',
        password: '1234',
        role: 'super_admin',
        branch: 'ALL',
        createdAt: '2026-10-06',
        status: 'active'
      },
      {
        username: 'admin',
        displayName: 'إدارة آل ندى',
        displayNameEn: 'Al-Nada Admin',
        password: '1234',
        role: 'super_admin',
        branch: 'ALL',
        createdAt: '2026-10-06',
        status: 'active'
      }
    ];
    const LS_AUDIT_LOG_KEY = 'al_nada_audit_log_v2';"""

if old_default_users in content:
    content = content.replace(old_default_users, new_default_users)

# -----------------------------------------------------------------------------
# 2. Update switchTab to render users page
# -----------------------------------------------------------------------------
old_switch_tab = """      if (tabId === 'tree') {
        setTimeout(resetZoom, 50);
      }
    }"""

new_switch_tab = """      if (tabId === 'tree') {
        setTimeout(resetZoom, 50);
      }
      if (tabId === 'users') {
        renderUsersPage();
      }
    }"""

if old_switch_tab in content:
    content = content.replace(old_switch_tab, new_switch_tab)

# -----------------------------------------------------------------------------
# 3. Update renderAllViews to include renderUsersPage
# -----------------------------------------------------------------------------
old_render_all = """      renderStatsView();
      populateParentSelects();
    }"""

new_render_all = """      renderStatsView();
      populateParentSelects();
      if (document.getElementById('view-users')) {
        renderUsersPage();
      }
    }"""

if old_render_all in content:
    content = content.replace(old_render_all, new_render_all)

# -----------------------------------------------------------------------------
# 4. In submitLogin, store role & branch in currentUser session
# -----------------------------------------------------------------------------
old_login_match = """      if (match) {
        currentUser = { username: match.username, displayName: match.displayName };"""

new_login_match = """      if (match) {
        currentUser = {
          username: match.username,
          displayName: match.displayName,
          displayNameEn: match.displayNameEn || match.displayName,
          role: match.role || 'branch_editor',
          branch: match.branch || 'ALL'
        };"""

if old_login_match in content:
    content = content.replace(old_login_match, new_login_match)

# -----------------------------------------------------------------------------
# 5. Add Users Page JS Engine & Audit System
# -----------------------------------------------------------------------------
users_engine_js = """
    // =========================================================================
    // USERS & PERMISSIONS MANAGEMENT ENGINE
    // =========================================================================
    function getUsersList() {
      const stored = localStorage.getItem(LS_ADMIN_CREDS_KEY);
      if (stored) {
        try {
          return JSON.parse(stored);
        } catch(e) {}
      }
      return DEFAULT_ADMIN_USERS;
    }

    function saveUsersList(users) {
      localStorage.setItem(LS_ADMIN_CREDS_KEY, JSON.stringify(users));
    }

    function isSuperAdmin() {
      if (!currentUser) return false;
      const users = getUsersList();
      const u = users.find(x => x.username.toLowerCase() === currentUser.username.toLowerCase());
      return u && u.role === 'super_admin';
    }

    function canUserEditBranch(branchAr) {
      if (!currentUser) return false;
      const users = getUsersList();
      const u = users.find(x => x.username.toLowerCase() === currentUser.username.toLowerCase());
      if (!u) return false;
      if (u.role === 'super_admin') return true;
      if (u.branch === 'ALL') return true;
      return u.branch === branchAr;
    }

    // Render Users Management View
    function renderUsersPage() {
      const users = getUsersList();
      const sessionBanner = document.getElementById('users-session-banner');
      const tbody = document.getElementById('users-table-tbody');
      if (!tbody) return;

      // 1. Session Banner
      if (currentUser) {
        const uObj = users.find(x => x.username.toLowerCase() === currentUser.username.toLowerCase()) || currentUser;
        const roleName = uObj.role === 'super_admin' ? '🛡️ مشرف عام (كامل الصلاحيات)' : (uObj.role === 'auditor' ? '🔍 مدقق أنساب' : '✍️ محرر معتمد');
        const branchScope = uObj.branch === 'ALL' ? 'كافة فروع العائلة' : uObj.branch;
        sessionBanner.innerHTML = `
          <div class="session-banner logged-in">
            <div style="display: flex; align-items: center; gap: 10px;">
              <span style="font-size: 1.3rem;">🟢</span>
              <div>
                <div>أنت مسجل حالياً باسم: <strong>${uObj.displayName}</strong> (@${uObj.username})</div>
                <div style="font-size: 0.82rem; font-weight: normal; margin-top: 2px;">
                  الرتبة: <span style="font-weight: 700;">${roleName}</span> | نطاق التحرير: <span style="font-weight: 700;">${branchScope}</span>
                </div>
              </div>
            </div>
            <button class="btn btn-sm" onclick="logout()" style="background: white; color: #065f46; border: 1px solid #a7f3d0;">تسجيل الخروج</button>
          </div>
        `;
      } else {
        sessionBanner.innerHTML = `
          <div class="session-banner guest">
            <div style="display: flex; align-items: center; gap: 10px;">
              <span style="font-size: 1.3rem;">🔒</span>
              <div>
                <div>أنت تتصفح حالياً بصفة <strong>زائر (قراءة فقط)</strong>.</div>
                <div style="font-size: 0.82rem; font-weight: normal; margin-top: 2px;">
                  لتعديل الأفراد أو إدارة المستخدمين، يرجى تسجيل الدخول بحساب محرر أو مشرف عام.
                </div>
              </div>
            </div>
            <button class="btn btn-sm btn-primary" onclick="openLoginModal()">تسجيل الدخول</button>
          </div>
        `;
      }

      // 2. Metrics
      const totalUsers = users.length;
      const superAdmins = users.filter(u => u.role === 'super_admin').length;
      const editors = users.filter(u => u.role === 'branch_editor').length;
      const auditLogs = getAuditLogs();

      document.getElementById('metric-total-users').textContent = totalUsers;
      document.getElementById('metric-super-admins').textContent = superAdmins;
      document.getElementById('metric-editors').textContent = editors;
      document.getElementById('metric-audit-count').textContent = auditLogs.length;
      document.getElementById('users-count-tag').textContent = `${totalUsers} مستخدم`;

      // 3. Render Users Table
      let html = '';
      users.forEach((u, idx) => {
        const isCurrent = currentUser && currentUser.username.toLowerCase() === u.username.toLowerCase();
        let roleBadgeClass = 'role-editor';
        let roleTitle = '✍️ محرر معتمد';
        if (u.role === 'super_admin') {
          roleBadgeClass = 'role-super';
          roleTitle = '🛡️ مشرف عام';
        } else if (u.role === 'auditor') {
          roleBadgeClass = 'role-auditor';
          roleTitle = '🔍 مدقق أنساب';
        }

        const branchLabel = u.branch === 'ALL' ? '🌐 كافة الفروع' : `<span class="tag-badge">${u.branch}</span>`;
        const dateStr = u.createdAt || '2026-10-06';

        html += `
          <tr>
            <td>${idx + 1}</td>
            <td>
              <div style="display: flex; align-items: center; gap: 8px;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--bg-card-subtle); border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; font-weight: 700; color: var(--primary);">
                  ${u.displayName.charAt(0)}
                </div>
                <div>
                  <strong>${u.displayName}</strong>
                  ${isCurrent ? '<span class="tag-badge" style="background:#dcfce7; color:#166534; margin-inline-start: 4px;">حسابك</span>' : ''}
                  <div style="font-size: 0.78rem; color: var(--text-muted);">@${u.username} ${u.displayNameEn ? `• ${u.displayNameEn}` : ''}</div>
                </div>
              </div>
            </td>
            <td><span class="role-badge ${roleBadgeClass}">${roleTitle}</span></td>
            <td>${branchLabel}</td>
            <td><span class="tag-badge" style="background: #ecfdf5; color: #047857;">🟢 نشط</span></td>
            <td><span style="font-size: 0.8rem; color: var(--text-muted);">${dateStr}</span></td>
            <td>
              <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                <button class="btn btn-sm" onclick="openChangeUserPasswordModal('${u.username}')" title="تغيير كلمة المرور">🔑 الرمز</button>
                <button class="btn btn-sm" onclick="openEditUserModal('${u.username}')" title="تعديل الصلاحية أو الفرع">✏️ تعديل</button>
                ${u.username.toLowerCase() !== 'ehab' ? `
                  <button class="btn btn-sm" style="color: #ef4444; border-color: #ef4444;" onclick="deleteUser('${u.username}')" title="حذف المستخدم">🗑️</button>
                ` : `
                  <button class="btn btn-sm" style="opacity: 0.4; cursor: not-allowed;" title="الحساب الأساسي محمي من الحذف" disabled>🔒</button>
                `}
              </div>
            </td>
          </tr>
        `;
      });
      tbody.innerHTML = html;

      // 4. Render Audit Table
      renderAuditTable();
    }

    // Add / Edit User Modal Handlers
    function openAddUserModal() {
      if (!isAuthorized()) {
        alert(I18N[currentLanguage].authRequired);
        openLoginModal();
        return;
      }
      if (!isSuperAdmin()) {
        alert('تنبيه: إضافة مستخدمين جدد تتطلب صلاحية المشرف العام.');
        return;
      }

      document.getElementById('user-form-modal-title').textContent = '➕ إضافة مستخدم جديد';
      document.getElementById('uf-is-edit').value = '0';
      document.getElementById('uf-username').value = '';
      document.getElementById('uf-username').disabled = false;
      document.getElementById('uf-display-ar').value = '';
      document.getElementById('uf-display-en').value = '';
      document.getElementById('uf-password').value = '';
      document.getElementById('uf-pwd-group').style.display = 'block';
      document.getElementById('uf-role').value = 'branch_editor';
      document.getElementById('uf-branch').value = 'ALL';
      document.getElementById('uf-branch-group').style.display = 'block';

      openModal('user-form-modal');
    }

    function openEditUserModal(username) {
      if (!isAuthorized()) {
        alert(I18N[currentLanguage].authRequired);
        openLoginModal();
        return;
      }
      if (!isSuperAdmin() && (currentUser.username.toLowerCase() !== username.toLowerCase())) {
        alert('تنبيه: تعديل بيانات المستخدمين الآخرين يتطلب صلاحية المشرف العام.');
        return;
      }

      const users = getUsersList();
      const u = users.find(x => x.username.toLowerCase() === username.toLowerCase());
      if (!u) return;

      document.getElementById('user-form-modal-title').textContent = `✏️ تعديل بيانات المستخدم: ${u.displayName}`;
      document.getElementById('uf-is-edit').value = '1';
      document.getElementById('uf-username').value = u.username;
      document.getElementById('uf-username').disabled = true;
      document.getElementById('uf-display-ar').value = u.displayName;
      document.getElementById('uf-display-en').value = u.displayNameEn || '';
      document.getElementById('uf-pwd-group').style.display = 'none';
      document.getElementById('uf-role').value = u.role || 'branch_editor';
      document.getElementById('uf-branch').value = u.branch || 'ALL';

      // Non-super-admins cannot elevate their own role
      document.getElementById('uf-role').disabled = !isSuperAdmin();
      document.getElementById('uf-branch').disabled = !isSuperAdmin();

      openModal('user-form-modal');
    }

    function handleRoleChange(role) {
      const branchGroup = document.getElementById('uf-branch-group');
      if (role === 'super_admin') {
        document.getElementById('uf-branch').value = 'ALL';
      }
    }

    function saveUserForm() {
      const isEdit = document.getElementById('uf-is-edit').value === '1';
      const u = document.getElementById('uf-username').value.trim().toLowerCase();
      const dAr = document.getElementById('uf-display-ar').value.trim();
      const dEn = document.getElementById('uf-display-en').value.trim();
      const pwd = document.getElementById('uf-password').value.trim();
      const role = document.getElementById('uf-role').value;
      const branch = document.getElementById('uf-branch').value;

      if (!u || !dAr) {
        alert('يرجى كتابة اسم المستخدم والاسم الكامل بالعربية.');
        return;
      }

      let users = getUsersList();

      if (!isEdit) {
        if (!pwd) {
          alert('يرجى تحديد كلمة مرور للمستخدم الجديد.');
          return;
        }
        if (users.some(x => x.username.toLowerCase() === u)) {
          alert('اسم المستخدم هذا مسجل مسبقاً، يرجى اختيار اسم آخر.');
          return;
        }

        const today = new Date().toISOString().split('T')[0];
        users.push({
          username: u,
          displayName: dAr,
          displayNameEn: dEn,
          password: pwd,
          role: role,
          branch: branch,
          createdAt: today,
          status: 'active'
        });

        saveUsersList(users);
        closeModal('user-form-modal');
        renderUsersPage();
        logActivity('إضافة مستخدم جديد', `تمت إضافة المحرر (${dAr}) - الرتبة: ${role} - الفرع: ${branch}`);
        showToast(`تمت إضافة المستخدم (${dAr}) بنجاح!`);
      } else {
        const idx = users.findIndex(x => x.username.toLowerCase() === u);
        if (idx !== -1) {
          users[idx].displayName = dAr;
          users[idx].displayNameEn = dEn;
          if (isSuperAdmin()) {
            users[idx].role = role;
            users[idx].branch = branch;
          }
          saveUsersList(users);
          closeModal('user-form-modal');
          renderUsersPage();
          logActivity('تعديل مستخدم', `تم تعديل بيانات المستخدم (${dAr})`);
          showToast('تم حفظ التعديلات بنجاح!');
        }
      }
    }

    // Password Management
    function openChangeUserPasswordModal(username) {
      if (!isAuthorized()) {
        alert(I18N[currentLanguage].authRequired);
        openLoginModal();
        return;
      }
      if (!isSuperAdmin() && (currentUser.username.toLowerCase() !== username.toLowerCase())) {
        alert('تنبيه: تغيير كلمة مرور مستخدم آخر يتطلب صلاحية المشرف العام.');
        return;
      }

      const users = getUsersList();
      const u = users.find(x => x.username.toLowerCase() === username.toLowerCase());
      if (!u) return;

      document.getElementById('pwd-modal-username').value = u.username;
      document.getElementById('pwd-modal-target-name').textContent = `${u.displayName} (@${u.username})`;
      document.getElementById('pwd-modal-new').value = '';

      openModal('user-pwd-modal');
    }

    function saveTargetUserPassword() {
      const uName = document.getElementById('pwd-modal-username').value;
      const newPwd = document.getElementById('pwd-modal-new').value.trim();

      if (!newPwd) {
        alert('يرجى كتابة كلمة المرور الجديدة.');
        return;
      }

      let users = getUsersList();
      const idx = users.findIndex(x => x.username.toLowerCase() === uName.toLowerCase());
      if (idx !== -1) {
        users[idx].password = newPwd;
        saveUsersList(users);
        closeModal('user-pwd-modal');
        logActivity('تغيير كلمة مرور', `تم تحديث كلمة المرور للمستخدم (${users[idx].displayName})`);
        showToast('تم تحديث كلمة المرور بنجاح!');
      }
    }

    function deleteUser(username) {
      if (!isSuperAdmin()) {
        alert('تنبيه: حذف المستخدمين يتطلب صلاحية المشرف العام.');
        return;
      }
      if (username.toLowerCase() === 'ehab') {
        alert('لا يمكن حذف الحساب الرئيسي (ehab).');
        return;
      }
      if (!confirm(`هل أنت متأكد من رغبتك في حذف المستخدم (${username}) وسحب صلاحياته؟`)) {
        return;
      }

      let users = getUsersList();
      const targetUser = users.find(x => x.username.toLowerCase() === username.toLowerCase());
      users = users.filter(x => x.username.toLowerCase() !== username.toLowerCase());
      saveUsersList(users);
      renderUsersPage();
      logActivity('حذف مستخدم', `تم حذف المستخدم (${targetUser ? targetUser.displayName : username}) وسحب الصلاحية`);
      showToast('تم حذف المستخدم بنجاح.');
    }

    // Export & Import Users Backup
    function exportUsersData() {
      const users = getUsersList();
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(users, null, 2));
      const dlAnchor = document.createElement('a');
      dlAnchor.setAttribute("href", dataStr);
      dlAnchor.setAttribute("download", `al_nada_users_backup_${new Date().toISOString().split('T')[0]}.json`);
      document.body.appendChild(dlAnchor);
      dlAnchor.click();
      dlAnchor.remove();
      showToast('تم تصدير ملف نسخة المستخدمين الاحتياطية بنجاح!');
    }

    function importUsersData(event) {
      if (!isSuperAdmin()) {
        alert('تنبيه: استيراد قائمة المستخدمين يتطلب صلاحية المشرف العام.');
        event.target.value = '';
        return;
      }
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const imported = JSON.parse(e.target.result);
          if (Array.isArray(imported) && imported.length > 0 && imported[0].username) {
            saveUsersList(imported);
            renderUsersPage();
            logActivity('استيراد مستخدمين', `تم استيراد قائمة مستخدمين بعدد (${imported.length})`);
            showToast(`تم استيراد ${imported.length} مستخدم بنجاح!`);
          } else {
            alert('صيغة ملف المستخدمين غير صحيحة.');
          }
        } catch(err) {
          alert('حدث خطأ أثناء قراءة ملف JSON: ' + err.message);
        }
      };
      reader.readAsText(file);
      event.target.value = '';
    }

    // =========================================================================
    // AUDIT LOG SYSTEM
    // =========================================================================
    function getAuditLogs() {
      try {
        const stored = localStorage.getItem(LS_AUDIT_LOG_KEY);
        return stored ? JSON.parse(stored) : [];
      } catch(e) {
        return [];
      }
    }

    function logActivity(action, details) {
      const logs = getAuditLogs();
      const now = new Date();
      const timeStr = now.toLocaleDateString('ar-EG', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
      const userLabel = currentUser ? `${currentUser.displayName} (@${currentUser.username})` : 'مستخدم معتمد';

      logs.unshift({
        id: 'log_' + Date.now(),
        time: timeStr,
        user: userLabel,
        action: action,
        details: details
      });

      if (logs.length > 100) logs.pop();
      localStorage.setItem(LS_AUDIT_LOG_KEY, JSON.stringify(logs));
      renderAuditTable();
      const metricEl = document.getElementById('metric-audit-count');
      if (metricEl) metricEl.textContent = logs.length;
    }

    function renderAuditTable() {
      const tbody = document.getElementById('audit-table-tbody');
      if (!tbody) return;
      const logs = getAuditLogs();

      if (logs.length === 0) {
        tbody.innerHTML = `
          <tr>
            <td colspan="5" style="text-align: center; color: var(--text-muted); padding: 24px;">
              لا توجد عمليات مسجلة حتى الآن. سيتم توثيق كل عملية تعديل أو إضافة تلقائياً هنا.
            </td>
          </tr>
        `;
        return;
      }

      let html = '';
      logs.slice(0, 30).forEach((entry, idx) => {
        let actionBadge = '<span class="tag-badge" style="background: #e0f2fe; color: #0369a1;">تعديل</span>';
        if (entry.action.includes('إضافة')) {
          actionBadge = '<span class="tag-badge" style="background: #dcfce7; color: #15803d;">➕ إضافة</span>';
        } else if (entry.action.includes('حذف')) {
          actionBadge = '<span class="tag-badge" style="background: #fee2e2; color: #b91c1c;">🗑️ حذف</span>';
        } else if (entry.action.includes('كلمة مرور')) {
          actionBadge = '<span class="tag-badge" style="background: #fef3c7; color: #b45309;">🔑 أمان</span>';
        }

        html += `
          <tr>
            <td>${idx + 1}</td>
            <td><span style="font-size: 0.8rem; color: var(--text-muted);">${entry.time}</span></td>
            <td><strong>${entry.user}</strong></td>
            <td>${actionBadge}</td>
            <td style="font-size: 0.85rem;">${entry.details}</td>
          </tr>
        `;
      });
      tbody.innerHTML = html;
    }

    function clearAuditLog() {
      if (!isSuperAdmin()) {
        alert('تنبيه: مسح سجل العمليات يتطلب صلاحية المشرف العام.');
        return;
      }
      if (!confirm('هل أنت متأكد من رغبتك في مسح سجل توثيق العمليات؟')) return;
      localStorage.removeItem(LS_AUDIT_LOG_KEY);
      renderAuditTable();
      const metricEl = document.getElementById('metric-audit-count');
      if (metricEl) metricEl.textContent = '0';
      showToast('تم مسح سجل العمليات بنجاح.');
    }
"""

target_engine_anchor = '    // =========================================================================\n    // Manage Authorized Users'
if target_engine_anchor in content and 'function renderUsersPage' not in content:
    content = content.replace(target_engine_anchor, users_engine_js + '\n' + target_engine_anchor)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Step 2: Users engine and audit system injected successfully!')
