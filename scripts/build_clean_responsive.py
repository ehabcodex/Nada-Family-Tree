import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# Read original pristine backup
with open('index.html.bak', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Loaded pristine backup: {len(html)} bytes")

# Read new CSS
with open('scripts/new_styles.css', 'r', encoding='utf-8') as f:
    new_css = f.read()

# =========================================================================
# Step 1: Head updates (Amiri font and viewport)
# =========================================================================
font_pattern = r'<link href="https://fonts\.googleapis\.com/css2\?family=Cairo[^"]+" rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400;1,700&family=Cairo:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
html = re.sub(font_pattern, new_fonts, html)

viewport_pattern = r'<meta name="viewport" content="[^"]+">'
new_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">'
html = re.sub(viewport_pattern, new_viewport, html)

# =========================================================================
# Step 2: CSS Replacement
# =========================================================================
style_start = html.find('<style>')
style_end = html.find('</style>')
if style_start != -1 and style_end != -1:
    html = html[:style_start + 7] + "\n" + new_css + "\n  " + html[style_end:]
    print("CSS replaced successfully.")

# =========================================================================
# Step 3: Header Hamburger Button
# =========================================================================
drawer_btn_markup = """
        <!-- Mobile Drawer Toggle -->
        <button class="btn btn-icon mobile-only-btn" id="mobile-drawer-toggle" onclick="toggleMobileDrawer()" aria-label="قائمة الخيارات والتعديل" title="القائمة">
          <span>☰</span>
        </button>"""

actions_marker = '<button class="btn btn-accent" onclick="toggleLanguage()"'
pos_actions = html.find(actions_marker)
if pos_actions != -1:
    btn_close = html.find('</button>', pos_actions) + 9
    html = html[:btn_close] + drawer_btn_markup + html[btn_close:]
    print("Added hamburger button to header.")

# =========================================================================
# Step 4: Add Mobile Drawer right after </header>
# =========================================================================
drawer_markup = """
  <!-- Mobile Navigation Drawer (Off-canvas) -->
  <div id="mobile-drawer-overlay" class="drawer-overlay" onclick="closeMobileDrawer()"></div>
  <aside id="mobile-nav-drawer" class="nav-drawer" aria-hidden="true" role="dialog" aria-label="قائمة الخيارات">
    <div class="drawer-header">
      <div class="brand-mini">
        <div class="brand-logo sm">ن</div>
        <div>
          <strong style="font-family: var(--font-title); font-size: 1.15rem; color: var(--primary);" class="t-app-title">شجرة عائلة آل ندى</strong>
          <div style="font-size: 0.72rem; color: var(--text-muted);" class="t-drawer-subtitle">خيارات وإجراءات الموقع</div>
        </div>
      </div>
      <button class="btn btn-icon btn-sm" onclick="closeMobileDrawer()" aria-label="إغلاق">✕</button>
    </div>
    <div class="drawer-body">
      <div id="drawer-auth-container"></div>
      <div class="drawer-actions-list">
        <button class="drawer-action-btn" onclick="closeMobileDrawer(); handleProtectedAction(openAddMemberModal)">
          <span>➕</span> <span class="t-add-member">إضافة فرد جديد</span>
        </button>
        <button class="drawer-action-btn" onclick="closeMobileDrawer(); printOrExportPDF()">
          <span>🖨️</span> <span class="t-print-pdf">طباعة / تصدير PDF</span>
        </button>
        <button class="drawer-action-btn" onclick="closeMobileDrawer(); exportData()">
          <span>💾</span> <span class="t-export">تصدير JSON</span>
        </button>
        <label class="drawer-action-btn" style="cursor: pointer; margin: 0;">
          <span>📥</span> <span class="t-import">استيراد JSON</span>
          <input type="file" accept=".json" style="display: none;" onchange="closeMobileDrawer(); handleProtectedImport(event)">
        </label>
      </div>
    </div>
    <div class="drawer-footer">
      <div style="font-size: 0.76rem; color: var(--text-muted); text-align: center;">
        توثيق شامل ومفصل لفروع ونسب العائلة الكريمة • 449 فرداً
      </div>
    </div>
  </aside>
"""
header_end = html.find('</header>')
if header_end != -1:
    html = html[:header_end + 9] + "\n" + drawer_markup + html[header_end + 9:]
    print("Added Mobile Drawer markup.")

# =========================================================================
# Step 5: view-tree: Add Tree Mode Bar & Accordion Container
# =========================================================================
viewport_marker = '<div class="tree-viewport-container">'
pos_viewport = html.find(viewport_marker)
if pos_viewport != -1:
    mode_bar_markup = """
      <!-- Mobile / Responsive View Mode Switcher -->
      <div class="tree-mode-bar" id="tree-mode-bar">
        <div class="segmented-control" role="group" aria-label="طريقة عرض الشجرة">
          <button class="seg-btn active" id="btn-mode-tree" onclick="setTreeMobileMode('tree')">
            <span>🌳</span> <span class="t-mode-tree">عرض الشجرة</span>
          </button>
          <button class="seg-btn" id="btn-mode-accordion" onclick="setTreeMobileMode('accordion')">
            <span>📑</span> <span class="t-mode-accordion">قائمة متداخلة (Accordion)</span>
          </button>
        </div>
      </div>
"""
    html = html[:pos_viewport + len(viewport_marker)] + mode_bar_markup + html[pos_viewport + len(viewport_marker):]

# Add Accordion wrapper right after canvas-wrapper
canvas_wrap_marker = '<div class="tree-canvas-wrapper" id="canvas-wrapper">'
pos_cw = html.find(canvas_wrap_marker)
if pos_cw != -1:
    # Find the closing tag of canvas-wrapper
    cw_close = html.find('</div>\n      </div>\n    </div>', pos_cw)
    if cw_close != -1:
        # cw_close points to the closing of canvas-wrapper
        cw_end = cw_close + 6 # length of </div>
        accordion_markup = """

        <!-- Mobile Accordion Tree View -->
        <div id="tree-accordion-wrapper" class="tree-accordion-wrapper" style="display: none;">
          <div class="accordion-toolbar">
            <div style="display: flex; gap: 8px;">
              <button class="btn btn-sm" onclick="expandAllAccordion()">📂 <span class="t-expand-all">بسط الكل</span></button>
              <button class="btn btn-sm" onclick="collapseAllAccordion()">📁 <span class="t-collapse-branches">طي الكل</span></button>
            </div>
            <div style="font-size: 0.8rem; color: var(--text-muted);">
              <span>10 أجيال موثقة • تصفح متسلسل</span>
            </div>
          </div>
          <div id="tree-accordion-container" class="tree-accordion-list"></div>
        </div>"""
        html = html[:cw_end] + accordion_markup + html[cw_end:]
        print("Added tree mode bar and accordion container successfully.")

# =========================================================================
# Step 6: view-table: Add mobile filter button, cards container, pagination
# =========================================================================
table_toolbar_marker = '<div class="table-toolbar">'
pos_tt = html.find(table_toolbar_marker)
if pos_tt != -1:
    filter_btn_markup = """
          <!-- Mobile Filter Button (Opens Bottom Sheet) -->
          <button class="btn btn-primary mobile-filter-btn" id="btn-open-filter-sheet" onclick="openFilterSheet()">
            <span>🔍</span> <span class="t-filter-btn">تصفية الفروع والأجيال</span>
            <span class="active-filter-badge" id="active-filter-count" style="display: none;">0</span>
          </button>
"""
    html = html[:pos_tt + len(table_toolbar_marker)] + filter_btn_markup + html[pos_tt + len(table_toolbar_marker):]

# Add mobile member cards and pagination after data-table-wrapper
table_close_marker = '</table>\n        </div>'
pos_tc = html.find(table_close_marker)
if pos_tc != -1:
    pos_tc_end = pos_tc + len(table_close_marker)
    mobile_table_markup = """
        <!-- Mobile Member Cards List -->
        <div id="table-cards-container" class="table-cards-container"></div>

        <!-- Table Pagination Controls -->
        <div id="table-pagination" class="table-pagination"></div>"""
    html = html[:pos_tc_end] + mobile_table_markup + html[pos_tc_end:]
    print("Added mobile filter button, cards container and pagination to table.")

# =========================================================================
# Step 7: Filter Bottom Sheet modal markup
# =========================================================================
filter_sheet_markup = """
  <!-- Filter Bottom Sheet for Mobile -->
  <div class="modal-backdrop" id="filter-bottom-sheet" onclick="if(event.target===this) closeFilterSheet()">
    <div class="modal-window">
      <div class="modal-header">
        <h3 class="modal-title t-filter-sheet-title">🔍 تصفية الفروع والأجيال</h3>
        <button class="modal-close" onclick="closeFilterSheet()" aria-label="إغلاق">✕</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label t-filter-branch">الفرع الرئيسي:</label>
          <select class="form-select" id="sheet-branch-filter"></select>
        </div>
        <div class="form-group">
          <label class="form-label t-filter-gen">الجيل:</label>
          <select class="form-select" id="sheet-gen-filter"></select>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn" onclick="resetFiltersFromSheet()">🔄 <span class="t-reset-filters">إعادة ضبط</span></button>
        <button class="btn btn-primary" onclick="applyFiltersFromSheet()">✓ <span class="t-apply-filters">تطبيق</span></button>
      </div>
    </div>
  </div>
"""
login_modal_pos = html.find('<div class="modal-backdrop" id="login-modal">')
if login_modal_pos != -1:
    html = html[:login_modal_pos] + filter_sheet_markup + "\n  " + html[login_modal_pos:]
    print("Added Filter Bottom Sheet modal.")

# =========================================================================
# Step 8: Add Mobile Bottom Navigation Bar before </body>
# =========================================================================
bottom_nav_markup = """
  <!-- Fixed Mobile Bottom Navigation Bar -->
  <nav id="mobile-bottom-nav" class="mobile-bottom-nav" aria-label="التنقل السفلي">
    <button class="bottom-nav-item active" data-tab="tree" onclick="switchTab('tree')">
      <span class="bottom-nav-icon">🌳</span>
      <span class="bottom-nav-label t-tab-tree">الشجرة</span>
    </button>
    <button class="bottom-nav-item" data-tab="branches" onclick="switchTab('branches')">
      <span class="bottom-nav-icon">🗂️</span>
      <span class="bottom-nav-label t-tab-branches">الفروع</span>
    </button>
    <button class="bottom-nav-item" data-tab="table" onclick="switchTab('table')">
      <span class="bottom-nav-icon">📋</span>
      <span class="bottom-nav-label t-tab-table">الدليل</span>
    </button>
    <button class="bottom-nav-item" data-tab="stats" onclick="switchTab('stats')">
      <span class="bottom-nav-icon">📊</span>
      <span class="bottom-nav-label t-tab-stats">الإحصاء</span>
    </button>
    <button class="bottom-nav-item" id="mobile-bottom-users" data-tab="users" onclick="switchTab('users')" style="display: none;">
      <span class="bottom-nav-icon">👥</span>
      <span class="bottom-nav-label t-tab-users">الصلاحيات</span>
    </button>
  </nav>
"""
body_end = html.rfind('</body>')
if body_end != -1:
    html = html[:body_end] + bottom_nav_markup + "\n" + html[body_end:]
    print("Added Mobile Bottom Navigation Bar.")

# =========================================================================
# Step 9: Surgical JavaScript Replacements
# =========================================================================

def replace_function(source, fn_name, new_code):
    pos = source.find(f"function {fn_name}")
    if pos == -1:
        raise ValueError(f"Function {fn_name} not found in source!")
    brace_open = source.find("{", pos)
    count = 1
    i = brace_open + 1
    while i < len(source) and count > 0:
        if source[i] == '{': count += 1
        elif source[i] == '}': count -= 1
        i += 1
    return source[:pos] + new_code + source[i:]

# 9.1 I18N dictionary updates
ar_marker = 'statHNotes: "📜 الملاحظات والوفيات الموثقة بالرسمة",'
ar_new = """statHNotes: "📜 الملاحظات والوفيات الموثقة بالرسمة",
        modeTree: "عرض الشجرة",
        modeAccordion: "قائمة متداخلة (Accordion)",
        filterBtn: "تصفية الفروع والأجيال",
        filterSheetTitle: "🔍 تصفية الفروع والأجيال",
        applyFilters: "تطبيق التصفية",
        resetFilters: "إعادة ضبط",
        drawerSubtitle: "خيارات وإجراءات الموقع","""
html = html.replace(ar_marker, ar_new, 1)

en_marker = 'statHNotes: "📜 Notes and deceased records documented on the chart",'
en_new = """statHNotes: "📜 Notes and deceased records documented on the chart",
        modeTree: "Tree View",
        modeAccordion: "Accordion List",
        filterBtn: "Filter Branches & Generations",
        filterSheetTitle: "🔍 Filter Directory",
        applyFilters: "Apply Filters",
        resetFilters: "Reset Filters",
        drawerSubtitle: "Site actions and tools","""
html = html.replace(en_marker, en_new, 1)

# applyTranslations updates
trans_marker = "document.querySelectorAll('.t-stat-h-notes').forEach(el => el.textContent = t.statHNotes);"
trans_new = """document.querySelectorAll('.t-stat-h-notes').forEach(el => el.textContent = t.statHNotes);
      document.querySelectorAll('.t-mode-tree').forEach(el => el.textContent = t.modeTree);
      document.querySelectorAll('.t-mode-accordion').forEach(el => el.textContent = t.modeAccordion);
      document.querySelectorAll('.t-filter-btn').forEach(el => el.textContent = t.filterBtn);
      document.querySelectorAll('.t-filter-sheet-title').forEach(el => el.textContent = t.filterSheetTitle);
      document.querySelectorAll('.t-apply-filters').forEach(el => el.textContent = t.applyFilters);
      document.querySelectorAll('.t-reset-filters').forEach(el => el.textContent = t.resetFilters);
      document.querySelectorAll('.t-drawer-subtitle').forEach(el => el.textContent = t.drawerSubtitle);"""
html = html.replace(trans_marker, trans_new, 1)

# 9.2 updateAuthUI
new_update_auth = """function updateAuthUI() {
      const container = document.getElementById('auth-status-container');
      const t = I18N[currentLanguage];

      if (currentUser) {
        if (container) {
          container.innerHTML = `
            <div class="auth-badge">
              <span>🟢</span>
              <span>${t.editorBadge} ${currentUser.displayName}</span>
              <button class="btn btn-sm" onclick="openManageUsersModal()" style="margin-inline-start: 6px; padding: 2px 6px; font-size: 0.75rem;" title="إدارة المحررين وتغيير الرمز السري">⚙️ ${currentLanguage === 'ar' ? 'إدارة الصلاحيات' : 'Manage Editors'}</button>
              <button class="btn btn-sm" onclick="logout()" style="margin-inline-start: 6px; padding: 2px 6px;">${t.logout}</button>
            </div>
          `;
        }
      } else {
        if (container) {
          container.innerHTML = `
            <button class="btn btn-sm" onclick="openLoginModal()" id="btn-login" title="تسجيل الدخول لتفعيل صلاحية التعديل">
              <span>🔒</span>
              <span class="t-login">${t.login}</span>
            </button>
          `;
        }
      }

      updateDrawerAuthUI();

      // تبويب إدارة المستخدمين يظهر للمحررين فقط
      const tabUsers = document.getElementById('tab-btn-users');
      const mobileTabUsers = document.getElementById('mobile-bottom-users');
      const showUsers = isAuthorized();
      if (tabUsers) tabUsers.style.display = showUsers ? 'inline-flex' : 'none';
      if (mobileTabUsers) mobileTabUsers.style.display = showUsers ? 'flex' : 'none';
    }

    function updateDrawerAuthUI() {
      const container = document.getElementById('drawer-auth-container');
      if (!container) return;
      const t = I18N[currentLanguage];

      if (currentUser) {
        container.innerHTML = `
          <div class="auth-badge" style="width: 100%; justify-content: space-between; padding: 10px 12px; margin-bottom: 8px;">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span>🟢</span>
              <div>
                <div style="font-weight: 700;">${currentUser.displayName}</div>
                <div style="font-size: 0.72rem; color: var(--text-muted);">${t.editorBadge} (@${currentUser.username})</div>
              </div>
            </div>
            <button class="btn btn-sm btn-danger" onclick="closeMobileDrawer(); logout();" style="padding: 4px 10px;">${t.logout}</button>
          </div>
        `;
      } else {
        container.innerHTML = `
          <button class="btn btn-primary" onclick="closeMobileDrawer(); openLoginModal();" style="width: 100%; justify-content: center; margin-bottom: 8px;">
            <span>🔒</span>
            <span>${t.login}</span>
          </button>
        `;
      }
    }

    function toggleMobileDrawer() {
      const drawer = document.getElementById('mobile-nav-drawer');
      if (!drawer) return;
      if (drawer.classList.contains('open')) {
        closeMobileDrawer();
      } else {
        openMobileDrawer();
      }
    }

    function openMobileDrawer() {
      const drawer = document.getElementById('mobile-nav-drawer');
      const overlay = document.getElementById('mobile-drawer-overlay');
      if (drawer) {
        drawer.classList.add('open');
        drawer.setAttribute('aria-hidden', 'false');
      }
      if (overlay) overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
      updateDrawerAuthUI();
    }

    function closeMobileDrawer() {
      const drawer = document.getElementById('mobile-nav-drawer');
      const overlay = document.getElementById('mobile-drawer-overlay');
      if (drawer) {
        drawer.classList.remove('open');
        drawer.setAttribute('aria-hidden', 'true');
      }
      if (overlay) overlay.classList.remove('open');
      document.body.style.overflow = '';
    }"""
html = replace_function(html, 'updateAuthUI', new_update_auth)
print("Replaced updateAuthUI with drawer support.")

# 9.3 initPanZoom (with touch pan, pinch zoom, and accordion view functions)
new_init_pan_zoom = """function initPanZoom() {
      const wrapper = document.getElementById('canvas-wrapper');
      if (!wrapper) return;
      let isDown = false;
      let startX, startY, scrollLeft, scrollTop;

      // سحب الفأرة (Mouse Pan)
      wrapper.addEventListener('mousedown', (e) => {
        if (e.target.closest('.tree-node') || e.target.closest('.node-toggle') || e.target.closest('.mobile-float-btn')) return;
        isDown = true;
        startX = e.pageX - wrapper.offsetLeft;
        startY = e.pageY - wrapper.offsetTop;
        scrollLeft = wrapper.scrollLeft;
        scrollTop = wrapper.scrollTop;
      });

      wrapper.addEventListener('mouseleave', () => isDown = false);
      wrapper.addEventListener('mouseup', () => isDown = false);

      wrapper.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - wrapper.offsetLeft;
        const y = e.pageY - wrapper.offsetTop;
        const walkX = (x - startX) * 1.4;
        const walkY = (y - startY) * 1.4;
        wrapper.scrollLeft = scrollLeft - walkX;
        wrapper.scrollTop = scrollTop - walkY;
      });

      // تكبير وتصغير بالعجلة (Wheel Zoom)
      wrapper.addEventListener('wheel', (e) => {
        if (e.ctrlKey) {
          e.preventDefault();
          zoomTree(e.deltaY < 0 ? 0.1 : -0.1);
        }
      });

      // إيماءات اللمس على الموبايل: سحب بإصبع + تكبير بإصبعين (Touch Pan & Pinch Zoom)
      let touchStartX = 0, touchStartY = 0;
      let touchScrollLeft = 0, touchScrollTop = 0;
      let initialPinchDistance = null;
      let isTouchPanning = false;

      wrapper.addEventListener('touchstart', (e) => {
        if (e.target.closest('.tree-node') || e.target.closest('.node-toggle') || e.target.closest('.mobile-float-btn')) return;
        if (e.touches.length === 1) {
          isTouchPanning = true;
          touchStartX = e.touches[0].pageX - wrapper.offsetLeft;
          touchStartY = e.touches[0].pageY - wrapper.offsetTop;
          touchScrollLeft = wrapper.scrollLeft;
          touchScrollTop = wrapper.scrollTop;
        } else if (e.touches.length === 2) {
          isTouchPanning = false;
          initialPinchDistance = Math.hypot(
            e.touches[0].pageX - e.touches[1].pageX,
            e.touches[0].pageY - e.touches[1].pageY
          );
        }
      }, { passive: false });

      wrapper.addEventListener('touchmove', (e) => {
        if (e.touches.length === 1 && isTouchPanning) {
          const x = e.touches[0].pageX - wrapper.offsetLeft;
          const y = e.touches[0].pageY - wrapper.offsetTop;
          wrapper.scrollLeft = touchScrollLeft - (x - touchStartX);
          wrapper.scrollTop = touchScrollTop - (y - touchStartY);
        } else if (e.touches.length === 2 && initialPinchDistance) {
          e.preventDefault();
          const currentDistance = Math.hypot(
            e.touches[0].pageX - e.touches[1].pageX,
            e.touches[0].pageY - e.touches[1].pageY
          );
          const delta = (currentDistance - initialPinchDistance) / 180;
          if (Math.abs(delta) > 0.03) {
            zoomTree(delta > 0 ? 0.08 : -0.08);
            initialPinchDistance = currentDistance;
          }
        }
      }, { passive: false });

      wrapper.addEventListener('touchend', (e) => {
        if (e.touches.length < 2) initialPinchDistance = null;
        if (e.touches.length === 0) isTouchPanning = false;
      });
    }

    // تبديل عرض الشجرة وقائمة الأكورديون المتداخلة على الموبايل
    let currentTreeMobileMode = 'tree';
    let expandedAccordionNodes = new Set();

    function setTreeMobileMode(mode) {
      currentTreeMobileMode = mode;
      const btnTree = document.getElementById('btn-mode-tree');
      const btnAcc = document.getElementById('btn-mode-accordion');
      const canvasWrap = document.getElementById('canvas-wrapper');
      const treeToolbar = document.querySelector('.tree-toolbar');
      const accWrap = document.getElementById('tree-accordion-wrapper');
      const floatingControls = document.getElementById('mobile-floating-zoom');

      if (mode === 'tree') {
        if (btnTree) btnTree.classList.add('active');
        if (btnAcc) btnAcc.classList.remove('active');
        if (canvasWrap) canvasWrap.style.display = 'block';
        if (floatingControls) floatingControls.style.display = 'flex';
        if (treeToolbar && window.innerWidth >= 640) treeToolbar.style.display = 'flex';
        if (accWrap) accWrap.style.display = 'none';
        setTimeout(resetZoom, 50);
      } else {
        if (btnTree) btnTree.classList.remove('active');
        if (btnAcc) btnAcc.classList.add('active');
        if (canvasWrap) canvasWrap.style.display = 'none';
        if (floatingControls) floatingControls.style.display = 'none';
        if (treeToolbar) treeToolbar.style.display = 'none';
        if (accWrap) accWrap.style.display = 'block';
        renderAccordionView();
      }
    }

    function renderAccordionView() {
      const container = document.getElementById('tree-accordion-container');
      if (!container || !treeData) return;

      if (expandedAccordionNodes.size === 0) {
        flatMembers.filter(m => m.generation <= 2).forEach(m => expandedAccordionNodes.add(m.id));
      }

      function buildNodeHtml(node) {
        const hasChildren = node.children && node.children.length > 0;
        const isExpanded = expandedAccordionNodes.has(node.id);
        const name = currentLanguage === 'ar' ? node.name_ar : node.name_en;
        const branch = currentLanguage === 'ar' ? node.branch_ar : node.branch_en;
        const genText = currentLanguage === 'ar' ? `الجيل ${node.generation}` : `Gen ${node.generation}`;
        const kidsText = currentLanguage === 'ar' ? `${node.children ? node.children.length : 0} أبناء` : `${node.children ? node.children.length : 0} children`;

        let html = `<div class="acc-node ${isExpanded ? 'expanded' : ''}" id="acc-node-${node.id}">`;
        html += `
          <div class="acc-row" onclick="toggleAccordionNode('${node.id}')">
            ${hasChildren ? `<div class="acc-chevron">▸</div>` : `<div style="width: 28px;"></div>`}
            <div class="acc-info">
              <div class="acc-name">${name}</div>
              <div class="acc-meta">
                <span class="acc-badge branch">${branch}</span>
                <span class="acc-badge gen">${genText}</span>
                ${hasChildren ? `<span class="acc-badge kids">${kidsText}</span>` : ''}
                ${node.notes ? `<span style="font-size: 0.72rem; color: #b8893b;">📌 ${node.notes}</span>` : ''}
              </div>
            </div>
            <button class="btn btn-sm acc-btn-view" onclick="event.stopPropagation(); inspectMember('${node.id}')">
              ✏️ ${isAuthorized() ? (currentLanguage === 'ar' ? 'تعديل' : 'Edit') : (currentLanguage === 'ar' ? 'عرض' : 'View')}
            </button>
          </div>
        `;

        if (hasChildren) {
          html += `<div class="acc-children">`;
          node.children.forEach(child => {
            html += buildNodeHtml(child);
          });
          html += `</div>`;
        }

        html += `</div>`;
        return html;
      }

      container.innerHTML = buildNodeHtml(treeData);
    }

    function toggleAccordionNode(id) {
      if (expandedAccordionNodes.has(id)) {
        expandedAccordionNodes.delete(id);
      } else {
        expandedAccordionNodes.add(id);
      }
      const el = document.getElementById(`acc-node-${id}`);
      if (el) {
        el.classList.toggle('expanded');
      }
    }

    function expandAllAccordion() {
      flatMembers.forEach(m => expandedAccordionNodes.add(m.id));
      renderAccordionView();
    }

    function collapseAllAccordion() {
      expandedAccordionNodes.clear();
      if (treeData) expandedAccordionNodes.add(treeData.id);
      renderAccordionView();
    }"""
html = replace_function(html, 'initPanZoom', new_init_pan_zoom)
print("Replaced initPanZoom with mobile gestures and accordion view.")

# 9.4 renderTableView: update to also sync sheet selectors
new_render_table_view = """function renderTableView() {
      const tbody = document.getElementById('table-tbody');
      const branchSelect = document.getElementById('table-branch-filter');
      const genSelect = document.getElementById('table-gen-filter');
      if (!tbody) return;

      const uniqueBranches = Array.from(new Set(flatMembers.map(m => currentLanguage === 'ar' ? m.branch_ar : m.branch_en)));
      const uniqueGens = Array.from(new Set(flatMembers.map(m => m.generation))).sort((a,b)=>a-b);

      const branchHtml = `<option value="ALL">${currentLanguage === 'ar' ? 'جميع الفروع' : 'All Branches'}</option>` +
        uniqueBranches.map(b => `<option value="${b}">${b}</option>`).join('');
      if (branchSelect) branchSelect.innerHTML = branchHtml;

      const genHtml = `<option value="ALL">${currentLanguage === 'ar' ? 'جميع الأجيال' : 'All Generations'}</option>` +
        uniqueGens.map(g => `<option value="${g}">${currentLanguage === 'ar' ? `الجيل ${g}` : `Gen ${g}`}</option>`).join('');
      if (genSelect) genSelect.innerHTML = genHtml;

      const sheetBranch = document.getElementById('sheet-branch-filter');
      const sheetGen = document.getElementById('sheet-gen-filter');
      if (sheetBranch) sheetBranch.innerHTML = branchHtml;
      if (sheetGen) sheetGen.innerHTML = genHtml;

      filterTable();
    }"""
html = replace_function(html, 'renderTableView', new_render_table_view)
print("Replaced renderTableView.")

# 9.5 filterTable: replace with cards + pagination + filter sheet support
new_filter_table = """function filterTable() {
      const tbody = document.getElementById('table-tbody');
      const cardsContainer = document.getElementById('table-cards-container');
      const paginationContainer = document.getElementById('table-pagination');
      const branchSelect = document.getElementById('table-branch-filter');
      const genSelect = document.getElementById('table-gen-filter');
      const searchInput = document.getElementById('main-search');

      const branchVal = branchSelect ? branchSelect.value : 'ALL';
      const genVal = genSelect ? genSelect.value : 'ALL';
      const searchVal = searchInput ? searchInput.value.trim().toLowerCase() : '';

      // شارة عدد الفلاتر المفعلة على الموبايل
      let activeFilterCount = 0;
      if (branchVal !== 'ALL') activeFilterCount++;
      if (genVal !== 'ALL') activeFilterCount++;
      const badgeEl = document.getElementById('active-filter-count');
      if (badgeEl) {
        if (activeFilterCount > 0) {
          badgeEl.textContent = activeFilterCount;
          badgeEl.style.display = 'inline-flex';
        } else {
          badgeEl.style.display = 'none';
        }
      }

      let filtered = flatMembers.filter(m => {
        const b = currentLanguage === 'ar' ? m.branch_ar : m.branch_en;
        const matchesBranch = branchVal === 'ALL' || b === branchVal;
        const matchesGen = genVal === 'ALL' || m.generation.toString() === genVal;
        
        let matchesSearch = true;
        if (searchVal) {
          const nameAr = m.name_ar.toLowerCase();
          const nameEn = m.name_en.toLowerCase();
          const lineageAr = (m.lineage_ar || '').toLowerCase();
          const lineageEn = (m.lineage_en || '').toLowerCase();
          matchesSearch = nameAr.includes(searchVal) || nameEn.includes(searchVal) || lineageAr.includes(searchVal) || lineageEn.includes(searchVal);
        }
        return matchesBranch && matchesGen && matchesSearch;
      });

      const countBadge = document.getElementById('table-count-badge');
      if (countBadge) countBadge.textContent = filtered.length;

      // 1. عرض جدول الكمبيوتر والتابلت
      if (tbody) {
        if (filtered.length === 0) {
          tbody.innerHTML = `<tr><td colspan="8" style="text-align: center; padding: 32px; color: var(--text-muted);">${currentLanguage === 'ar' ? 'لا توجد نتائج مطابقة لبحثك' : 'No matching results'}</td></tr>`;
        } else {
          let html = '';
          filtered.forEach((m, idx) => {
            const name = currentLanguage === 'ar' ? m.name_ar : m.name_en;
            const lineage = currentLanguage === 'ar' ? m.lineage_ar : m.lineage_en;
            const branch = currentLanguage === 'ar' ? m.branch_ar : m.branch_en;
            const father = currentLanguage === 'ar' ? (m.parent_name_ar || '-') : (m.parent_name_en || '-');

            html += `
              <tr>
                <td>${idx + 1}</td>
                <td>
                  <strong>${name}</strong>
                  <div style="font-size: 0.78rem; color: var(--text-muted);">${lineage}</div>
                </td>
                <td><span class="tag-badge">${branch}</span></td>
                <td>${father}</td>
                <td><span class="tag-badge">${m.generation}</span></td>
                <td>${m.children_count}</td>
                <td class="col-notes">${m.notes || '-'}</td>
                <td>
                  <button class="btn btn-sm" onclick="inspectMember('${m.id}')">✏️ ${isAuthorized() ? (currentLanguage === 'ar' ? 'تعديل' : 'Edit') : (currentLanguage === 'ar' ? 'عرض' : 'View')}</button>
                </td>
              </tr>
            `;
          });
          tbody.innerHTML = html;
        }
      }

      // 2. عرض بطاقات الموبايل مع التصفح والتحميل السريع
      if (cardsContainer) {
        if (filtered.length === 0) {
          cardsContainer.innerHTML = `<div style="text-align: center; padding: 36px 16px; color: var(--text-muted); background: var(--bg-card); border-radius: var(--radius-sm); border: 1px dashed var(--border);"><div style="font-size: 2rem; margin-bottom: 8px;">🔍</div><div>${currentLanguage === 'ar' ? 'لا توجد نتائج مطابقة لبحثك' : 'No matching results found'}</div></div>`;
          if (paginationContainer) paginationContainer.style.display = 'none';
          return;
        }

        const totalPages = Math.ceil(filtered.length / tablePageSize);
        if (tableCurrentPage > totalPages) tableCurrentPage = totalPages;
        if (tableCurrentPage < 1) tableCurrentPage = 1;

        const startIndex = (tableCurrentPage - 1) * tablePageSize;
        const pageItems = filtered.slice(startIndex, startIndex + tablePageSize);

        let cardsHtml = '';
        pageItems.forEach((m) => {
          const name = currentLanguage === 'ar' ? m.name_ar : m.name_en;
          const lineage = currentLanguage === 'ar' ? m.lineage_ar : m.lineage_en;
          const branch = currentLanguage === 'ar' ? m.branch_ar : m.branch_en;
          const father = currentLanguage === 'ar' ? (m.parent_name_ar || '-') : (m.parent_name_en || '-');
          const genLabel = currentLanguage === 'ar' ? `الجيل ${m.generation}` : `Gen ${m.generation}`;
          const kidsLabel = currentLanguage === 'ar' ? `${m.children_count} أبناء` : `${m.children_count} kids`;

          cardsHtml += `
            <div class="member-card">
              <div class="member-card-header">
                <div>
                  <div class="member-card-name">${name}</div>
                  <div class="member-card-lineage">${lineage}</div>
                </div>
                <span class="tag-badge" style="background: rgba(var(--accent-rgb), 0.15); color: var(--accent-dark);">${genLabel}</span>
              </div>
              <div class="member-card-meta">
                <span class="tag-badge" style="background: rgba(var(--primary-rgb), 0.1); color: var(--primary);">${branch}</span>
                <span>👨 الأب: <strong>${father}</strong></span>
                <span>👶 ${kidsLabel}</span>
                ${m.notes ? `<span style="color: #b8893b; width: 100%;">📌 ${m.notes}</span>` : ''}
              </div>
              <div class="member-card-actions">
                <button class="btn btn-sm btn-primary" onclick="inspectMember('${m.id}')">
                  ✏️ ${isAuthorized() ? (currentLanguage === 'ar' ? 'تعديل الفرد' : 'Edit Member') : (currentLanguage === 'ar' ? 'عرض التفاصيل' : 'View Details')}
                </button>
              </div>
            </div>
          `;
        });
        cardsContainer.innerHTML = cardsHtml;

        // شريط التصفح بين الصفحات
        if (paginationContainer) {
          if (totalPages <= 1) {
            paginationContainer.style.display = 'none';
          } else {
            paginationContainer.style.display = 'flex';
            paginationContainer.innerHTML = `
              <button class="btn btn-sm" onclick="setTablePage(${tableCurrentPage - 1})" ${tableCurrentPage === 1 ? 'disabled style="opacity: 0.5;"' : ''}>
                ${currentLanguage === 'ar' ? '← السابق' : '← Prev'}
              </button>
              <span style="font-weight: 600; color: var(--text);">
                ${currentLanguage === 'ar' ? `صفحة ${tableCurrentPage} من ${totalPages}` : `Page ${tableCurrentPage} of ${totalPages}`}
              </span>
              <button class="btn btn-sm" onclick="setTablePage(${tableCurrentPage + 1})" ${tableCurrentPage === totalPages ? 'disabled style="opacity: 0.5;"' : ''}>
                ${currentLanguage === 'ar' ? 'التالي →' : 'Next →'}
              </button>
            `;
          }
        }
      }
    }

    let tableCurrentPage = 1;
    const tablePageSize = 25;

    function setTablePage(page) {
      tableCurrentPage = page;
      filterTable();
      const target = document.getElementById('table-cards-container');
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    // دوال اللوحة السفلية لتصفية الفروع والأجيال على الموبايل
    function openFilterSheet() {
      const branchSelect = document.getElementById('sheet-branch-filter');
      const genSelect = document.getElementById('sheet-gen-filter');
      const mainBranchSelect = document.getElementById('table-branch-filter');
      const mainGenSelect = document.getElementById('table-gen-filter');

      if (branchSelect && mainBranchSelect) {
        branchSelect.innerHTML = mainBranchSelect.innerHTML;
        branchSelect.value = mainBranchSelect.value;
      }
      if (genSelect && mainGenSelect) {
        genSelect.innerHTML = mainGenSelect.innerHTML;
        genSelect.value = mainGenSelect.value;
      }
      openModal('filter-bottom-sheet');
    }

    function closeFilterSheet() {
      closeModal('filter-bottom-sheet');
    }

    function applyFiltersFromSheet() {
      const branchVal = document.getElementById('sheet-branch-filter').value;
      const genVal = document.getElementById('sheet-gen-filter').value;
      if (document.getElementById('table-branch-filter')) {
        document.getElementById('table-branch-filter').value = branchVal;
      }
      if (document.getElementById('table-gen-filter')) {
        document.getElementById('table-gen-filter').value = genVal;
      }
      tableCurrentPage = 1;
      filterTable();
      closeFilterSheet();
    }

    function resetFiltersFromSheet() {
      if (document.getElementById('sheet-branch-filter')) {
        document.getElementById('sheet-branch-filter').value = 'ALL';
      }
      if (document.getElementById('sheet-gen-filter')) {
        document.getElementById('sheet-gen-filter').value = 'ALL';
      }
      applyFiltersFromSheet();
    }"""
html = replace_function(html, 'filterTable', new_filter_table)
print("Replaced filterTable with card list & pagination.")

# 9.6 switchTab: update to sync both desktop tabs and mobile bottom nav
new_switch_tab = """function switchTab(tabId) {
      // تحديث تبويبات الكمبيوتر
      document.querySelectorAll('.tab-btn').forEach(btn => {
        const isMatch = btn.getAttribute('data-tab') === tabId || 
                        (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(`'${tabId}'`));
        if (isMatch) {
          btn.classList.add('active');
          btn.setAttribute('aria-selected', 'true');
          try {
            btn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
          } catch(e) {}
        } else {
          btn.classList.remove('active');
          btn.setAttribute('aria-selected', 'false');
        }
      });

      // تحديث شريط التنقل السفلي للموبايل
      document.querySelectorAll('.bottom-nav-item').forEach(btn => {
        if (btn.getAttribute('data-tab') === tabId) {
          btn.classList.add('active');
          btn.setAttribute('aria-selected', 'true');
        } else {
          btn.classList.remove('active');
          btn.setAttribute('aria-selected', 'false');
        }
      });

      // تفعيل اللوحة المناسبة
      document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
      const targetPanel = document.getElementById(`view-${tabId}`);
      if (targetPanel) targetPanel.classList.add('active');

      if (tabId === 'tree') {
        if (currentTreeMobileMode === 'tree') {
          setTimeout(resetZoom, 50);
        } else {
          renderAccordionView();
        }
      }
      if (tabId === 'table') {
        filterTable();
      }
      if (tabId === 'users') {
        renderUsersPage();
      }

      if (window.innerWidth < 640) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }"""
html = replace_function(html, 'switchTab', new_switch_tab)
print("Replaced switchTab with bottom nav syncing.")

# 9.7 handleSearch: debounced search and tree auto-centering
new_handle_search = """function handleSearch(val) {
      clearTimeout(searchDebounceTimer);
      const clearBtn = document.getElementById('search-clear-btn');
      if (clearBtn) {
        clearBtn.style.display = val.trim() ? 'flex' : 'none';
      }
      searchDebounceTimer = setTimeout(() => {
        executeSearch(val);
      }, 250);
    }

    let searchDebounceTimer = null;

    function executeSearch(val) {
      const query = val.trim().toLowerCase();
      tableCurrentPage = 1;
      filterTable();

      document.querySelectorAll('.tree-node').forEach(node => {
        node.classList.remove('highlighted');
      });

      if (!query) return;

      const matchedMembers = flatMembers.filter(m => {
        return m.name_ar.toLowerCase().includes(query) ||
               m.name_en.toLowerCase().includes(query) ||
               (m.lineage_ar && m.lineage_ar.toLowerCase().includes(query)) ||
               (m.notes && m.notes.toLowerCase().includes(query));
      });

      // في عرض الأكورديون، فتح مسارات البحث
      if (currentTreeMobileMode === 'accordion') {
        matchedMembers.forEach(m => {
          let curr = m;
          while (curr && curr.parent_id) {
            expandedAccordionNodes.add(curr.parent_id);
            curr = flatMembers.find(f => f.id === curr.parent_id);
          }
        });
        renderAccordionView();
      } else {
        // في عرض الشجرة: بسط الأجداد والتركيز التلقائي على الفرد
        matchedMembers.forEach(m => {
          let curr = m;
          while (curr && curr.parent_id) {
            collapsedNodes.delete(curr.parent_id);
            curr = flatMembers.find(f => f.id === curr.parent_id);
          }
        });

        if (matchedMembers.length > 0) {
          renderTreeView();
          matchedMembers.forEach(m => {
            const el = document.getElementById(`node-${m.id}`);
            if (el) el.classList.add('highlighted');
          });

          // تمركز الشجرة تلقائياً على الشخص الأول المطابق
          setTimeout(() => {
            const firstNode = document.getElementById(`node-${matchedMembers[0].id}`);
            if (firstNode) {
              firstNode.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });
            }
          }, 150);
        }
      }
    }"""
html = replace_function(html, 'handleSearch', new_handle_search)
print("Replaced handleSearch with debouncing and tree centering.")

# Save updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Build completed successfully! Final size: {len(html)} bytes")
