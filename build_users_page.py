# -*- coding: utf-8 -*-
"""
Script to build and inject the Users & Permissions Management Page into index.html
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -----------------------------------------------------------------------------
# 1. Add CSS for Users Page
# -----------------------------------------------------------------------------
users_css = """
    /* =========================================================================
       USERS MANAGEMENT PAGE STYLES
       ========================================================================= */
    .users-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 20px;
      background: var(--bg-card);
      padding: 16px 20px;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }

    .users-stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }

    .user-metric-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      display: flex;
      align-items: center;
      gap: 14px;
      box-shadow: var(--shadow);
    }

    .metric-icon {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      flex-shrink: 0;
    }

    .metric-val {
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--text);
      line-height: 1.2;
    }

    .metric-lbl {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    .role-badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 700;
    }

    .role-super {
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fde68a;
    }

    .role-editor {
      background: #dbeafe;
      color: #1e40af;
      border: 1px solid #bfdbfe;
    }

    .role-auditor {
      background: #ccfbf1;
      color: #115e59;
      border: 1px solid #99f6e4;
    }

    .session-banner {
      padding: 14px 18px;
      border-radius: var(--radius);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      font-size: 0.9rem;
      font-weight: 600;
      margin-bottom: 20px;
    }

    .session-banner.logged-in {
      background: #ecfdf5;
      color: #065f46;
      border: 1px solid #a7f3d0;
    }

    .session-banner.guest {
      background: #fffbeb;
      color: #92400e;
      border: 1px solid #fde68a;
    }
"""

if '.users-header-bar' not in content:
    content = content.replace('/* =========================================================================\n       MODALS', users_css + '\n    /* =========================================================================\n       MODALS')

# -----------------------------------------------------------------------------
# 2. Add Tab in Navbar
# -----------------------------------------------------------------------------
old_tab_stats = """      <button class="tab-btn" onclick="switchTab('stats')">
        <span>📊</span>
        <span class="t-tab-stats">الإحصائيات والتحليل</span>
      </button>"""

new_tab_stats_and_users = """      <button class="tab-btn" onclick="switchTab('stats')">
        <span>📊</span>
        <span class="t-tab-stats">الإحصائيات والتحليل</span>
      </button>
      <button class="tab-btn" onclick="switchTab('users')" id="tab-btn-users">
        <span>👥</span>
        <span class="t-tab-users">إدارة المستخدمين والصلاحيات</span>
      </button>"""

if 'id="tab-btn-users"' not in content and old_tab_stats in content:
    content = content.replace(old_tab_stats, new_tab_stats_and_users)

# -----------------------------------------------------------------------------
# 3. Add VIEW 5 (Users & Permissions Management) in <main>
# -----------------------------------------------------------------------------
view_users_html = """
    <!-- VIEW 5: USERS & PERMISSIONS MANAGEMENT -->
    <div id="view-users" class="view-panel">
      <!-- Users Header Bar -->
      <div class="users-header-bar">
        <div>
          <h2 style="font-size: 1.25rem; font-weight: 800; color: var(--primary); display: flex; align-items: center; gap: 8px; margin: 0;">
            <span>👥</span> <span class="t-users-title">إدارة المستخدمين وصلاحيات التعديل</span>
          </h2>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin: 4px 0 0 0;" class="t-users-subtitle">
            توزيع وضبط صلاحيات الإضافة والتعديل بين أفراد العائلة لضمان دقة نسب العائلة وحفظه من التغيير العشوائي.
          </p>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <button class="btn btn-primary" onclick="openAddUserModal()">
            <span>➕</span> <span class="t-add-user-btn">إضافة مستخدم جديد</span>
          </button>
          <button class="btn" onclick="exportUsersData()" title="تصدير نسخة احتياطية من قائمة المستخدمين">
            <span>💾</span> <span class="t-export-users-btn">نسخة احتياطية</span>
          </button>
          <label class="btn" style="cursor: pointer; margin: 0;" title="استيراد نسخة مستخدمين">
            <span>📥</span> <span class="t-import-users-btn">استعادة</span>
            <input type="file" accept=".json" style="display: none;" onchange="importUsersData(event)">
          </label>
        </div>
      </div>

      <!-- Current Session Status Banner -->
      <div id="users-session-banner"></div>

      <!-- Metrics Cards -->
      <div class="users-stats-grid">
        <div class="user-metric-card">
          <div class="metric-icon" style="background: rgba(30,58,138,0.1); color: var(--primary);">👥</div>
          <div>
            <div class="metric-val" id="metric-total-users">0</div>
            <div class="metric-lbl">إجمالي المستخدمين المسجلين</div>
          </div>
        </div>
        <div class="user-metric-card">
          <div class="metric-icon" style="background: rgba(217,119,6,0.1); color: var(--accent);">🛡️</div>
          <div>
            <div class="metric-val" id="metric-super-admins">0</div>
            <div class="metric-lbl">المشرفون العامون (تحكم كامل)</div>
          </div>
        </div>
        <div class="user-metric-card">
          <div class="metric-icon" style="background: rgba(16,185,129,0.1); color: #10b981);">✍️</div>
          <div>
            <div class="metric-val" id="metric-editors">0</div>
            <div class="metric-lbl">محررو الفروع المعتمدون</div>
          </div>
        </div>
        <div class="user-metric-card">
          <div class="metric-icon" style="background: rgba(99,102,241,0.1); color: #6366f1);">📜</div>
          <div>
            <div class="metric-val" id="metric-audit-count">0</div>
            <div class="metric-lbl">سجلات التعديل الموثقة</div>
          </div>
        </div>
      </div>

      <!-- Users Table -->
      <div class="table-container" style="margin-bottom: 28px;">
        <div class="table-header" style="justify-content: space-between;">
          <h3 style="font-size: 1.05rem; font-weight: 700; display: flex; align-items: center; gap: 8px; margin: 0;">
            <span>📋</span> <span>المستخدمون والمحررون المصرح لهم</span>
          </h3>
          <span class="tag-badge" id="users-count-tag">0 مستخدم</span>
        </div>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th style="width: 45px;">#</th>
                <th>المستخدم والاسم الكامل</th>
                <th>الرتبة والصلاحية</th>
                <th>نطاق التحرير المخول به</th>
                <th>الحالة</th>
                <th>تاريخ الإنشاء</th>
                <th style="width: 190px;">الإجراءات</th>
              </tr>
            </thead>
            <tbody id="users-table-tbody">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tree Audit Trail / History -->
      <div class="table-container">
        <div class="table-header" style="justify-content: space-between; flex-wrap: wrap; gap: 8px;">
          <div>
            <h3 style="font-size: 1.05rem; font-weight: 700; display: flex; align-items: center; gap: 8px; margin: 0;">
              <span>📜</span> <span>سجل توثيق التعديلات (تتبع الإضافات والتغييرات بالاسم والوقت)</span>
            </h3>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin: 4px 0 0 0;">
              يتم هنا تسجيل كل إضافة أو تعديل أو حذف لأفراد الشجرة تلقائياً باسم المحرر المسؤول وتاريخ العملية لضمان الحفاظ على صحة التوثيق.
            </p>
          </div>
          <div>
            <button class="btn btn-sm" onclick="clearAuditLog()" id="btn-clear-audit" title="مسح السجل (يتطلب صلاحية المشرف العام)">🗑️ مسح السجل</button>
          </div>
        </div>
        <div class="data-table-wrapper" style="max-height: 380px;">
          <table class="data-table">
            <thead>
              <tr>
                <th style="width: 50px;">#</th>
                <th style="width: 170px;">التاريخ والوقت</th>
                <th>المحرر المسؤول</th>
                <th>نوع العملية</th>
                <th>تفاصيل الإجراء</th>
              </tr>
            </thead>
            <tbody id="audit-table-tbody">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
"""

if 'id="view-users"' not in content:
    target_end_main = '    </div>\n  </main>'
    content = content.replace(target_end_main, '    </div>\n' + view_users_html + '\n  </main>')

# -----------------------------------------------------------------------------
# 4. Add User Modals (Add/Edit User, Change Password)
# -----------------------------------------------------------------------------
user_modals_html = """
  <!-- ADD / EDIT USER MODAL -->
  <div class="modal-backdrop" id="user-form-modal">
    <div class="modal-window" style="max-width: 500px;">
      <div class="modal-header">
        <h3 id="user-form-modal-title">➕ إضافة مستخدم جديد</h3>
        <button class="modal-close" onclick="closeModal('user-form-modal')">&times;</button>
      </div>
      <div class="modal-body">
        <input type="hidden" id="uf-is-edit" value="0">
        
        <div class="form-group">
          <label class="form-label">اسم المستخدم بالإنجليزية (Username):</label>
          <input type="text" id="uf-username" class="form-input" placeholder="e.g. mohammad_nada">
        </div>

        <div class="form-group">
          <label class="form-label">الاسم الكامل بالعربية (Display Name):</label>
          <input type="text" id="uf-display-ar" class="form-input" placeholder="مثال: محمد ندى">
        </div>

        <div class="form-group">
          <label class="form-label">الاسم بالإنجليزية (اختياري):</label>
          <input type="text" id="uf-display-en" class="form-input" placeholder="e.g. Mohammad Nada">
        </div>

        <div class="form-group" id="uf-pwd-group">
          <label class="form-label">كلمة المرور / الرمز السري:</label>
          <input type="password" id="uf-password" class="form-input" placeholder="••••••••">
        </div>

        <div class="form-group">
          <label class="form-label">الصلاحية والرتبة:</label>
          <select id="uf-role" class="form-select form-input" onchange="handleRoleChange(this.value)">
            <option value="super_admin">🛡️ مشرف عام (كامل الصلاحيات + إدارة المستخدمين)</option>
            <option value="branch_editor" selected>✍️ محرر معتمد (إضافة وتعديل أفراد العائلة)</option>
            <option value="auditor">🔍 مدقق أنساب (مراجعة وتوثيق ملاحظات فقط)</option>
          </select>
        </div>

        <div class="form-group" id="uf-branch-group">
          <label class="form-label">نطاق التحرير المخول به (الفرع):</label>
          <select id="uf-branch" class="form-select form-input">
            <option value="ALL">🌐 كافة فروع العائلة دون قيود</option>
            <option value="فرع محمود بن مصطفى">فرع محمود بن مصطفى</option>
            <option value="فرع سالم بن حمد">فرع سالم بن حمد</option>
            <option value="فرع احمد بن حمد">فرع احمد بن حمد</option>
            <option value="فرع محمد بن حمد">فرع محمد بن حمد</option>
            <option value="فرع عبد الله بن حمد">فرع عبد الله بن حمد</option>
            <option value="فرع خليل بن حمد">فرع خليل بن حمد</option>
            <option value="فرع ابراهيم بن حمد">فرع ابراهيم بن حمد</option>
          </select>
          <small style="color: var(--text-muted); font-size: 0.78rem; display: block; margin-top: 4px;">
            تحديد الفرع يمنع هذا المحرر من تعديل أي فرع آخر لضمان الدقة وتفادي التداخلات.
          </small>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn" onclick="closeModal('user-form-modal')">إلغاء</button>
        <button class="btn btn-primary" onclick="saveUserForm()">حفظ المستخدم</button>
      </div>
    </div>
  </div>

  <!-- CHANGE USER PASSWORD MODAL -->
  <div class="modal-backdrop" id="user-pwd-modal">
    <div class="modal-window" style="max-width: 420px;">
      <div class="modal-header">
        <h3>🔑 تغيير كلمة المرور للمستخدم</h3>
        <button class="modal-close" onclick="closeModal('user-pwd-modal')">&times;</button>
      </div>
      <div class="modal-body">
        <input type="hidden" id="pwd-modal-username">
        <p style="font-size: 0.88rem; margin-bottom: 12px; color: var(--text-muted);">
          تعيين كلمة مرور جديدة للمستخدم: <strong id="pwd-modal-target-name" style="color: var(--primary);"></strong>
        </p>
        <div class="form-group">
          <label class="form-label">كلمة المرور الجديدة:</label>
          <input type="password" id="pwd-modal-new" class="form-input" placeholder="أدخل كلمة المرور الجديدة">
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn" onclick="closeModal('user-pwd-modal')">إلغاء</button>
        <button class="btn btn-primary" onclick="saveTargetUserPassword()">تحديث كلمة المرور</button>
      </div>
    </div>
  </div>
"""

if 'id="user-form-modal"' not in content:
    target_modal_anchor = '  <!-- Toast -->'
    content = content.replace(target_modal_anchor, user_modals_html + '\n  <!-- Toast -->')

# -----------------------------------------------------------------------------
# 5. Add Translations to I18N
# -----------------------------------------------------------------------------
ar_additions = """        tabUsers: "إدارة المستخدمين والصلاحيات",
        usersTitle: "إدارة المستخدمين وصلاحيات التعديل",
        usersSubtitle: "توزيع وضبط صلاحيات الإضافة والتعديل بين أفراد العائلة لضمان دقة نسب العائلة وحفظه من التغيير العشوائي.",
        addUserBtn: "إضافة مستخدم جديد",
        exportUsersBtn: "نسخة احتياطية",
        importUsersBtn: "استعادة","""

en_additions = """        tabUsers: "User & Role Management",
        usersTitle: "User & Permission Management",
        usersSubtitle: "Distribute and manage editing rights among family members to ensure accuracy of genealogy.",
        addUserBtn: "Add New User",
        exportUsersBtn: "Export Users",
        importUsersBtn: "Import Users","""

if 'tabUsers:' not in content:
    content = content.replace('authRequired: "تنبيه: التعديل والإضافة محصوران بالمحررين المعتمدين فقط. يرجى تسجيل الدخول أولاً."',
                            'authRequired: "تنبيه: التعديل والإضافة محصوران بالمحررين المعتمدين فقط. يرجى تسجيل الدخول أولاً.",\n' + ar_additions)
    content = content.replace('authRequired: "Notice: Editing and adding members is restricted to authorized editors. Please login first."',
                            'authRequired: "Notice: Editing and adding members is restricted to authorized editors. Please login first.",\n' + en_additions)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Step 1: HTML structure and CSS injected successfully!')
