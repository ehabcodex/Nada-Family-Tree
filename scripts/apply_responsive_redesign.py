import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# Read original backup
with open('index.html.bak', 'r', encoding='utf-8') as f:
    html = f.read()

# Read new CSS
with open('scripts/new_styles.css', 'r', encoding='utf-8') as f:
    new_css = f.read()

print("Original length:", len(html))

# 1. Update Google Fonts in <head>
font_pattern = r'<link href="https://fonts\.googleapis\.com/css2\?family=Cairo[^"]+" rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400;1,700&family=Cairo:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
html = re.sub(font_pattern, new_fonts, html)

# 2. Update meta viewport
viewport_pattern = r'<meta name="viewport" content="[^"]+">'
new_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">'
html = re.sub(viewport_pattern, new_viewport, html)

# 3. Replace <style>...</style>
style_start = html.find('<style>')
style_end = html.find('</style>')
if style_start != -1 and style_end != -1:
    html = html[:style_start + 7] + "\n" + new_css + "\n  " + html[style_end:]
    print("Replaced CSS style block successfully.")

# 4. Update Header actions: add hamburger button
header_actions_pos = html.find('<div class="header-actions">')
if header_actions_pos != -1:
    # Insert mobile drawer toggle button at end of header actions
    end_actions_pos = html.find('</div>\n    </div>\n  </header>')
    if end_actions_pos == -1:
        end_actions_pos = html.find('</div>', header_actions_pos)
    
    drawer_btn_markup = """
        <!-- Mobile Drawer Toggle -->
        <button class="btn btn-icon mobile-only-btn" id="mobile-drawer-toggle" onclick="toggleMobileDrawer()" aria-label="قائمة الخيارات والتعديل" title="القائمة">
          <span>☰</span>
        </button>
      </div>"""
    html = html[:end_actions_pos] + drawer_btn_markup + html[end_actions_pos + 6:]
    print("Added mobile drawer toggle button.")

# 5. Add Mobile Nav Drawer markup right after </header>
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
        توثيق شامل ومفصل لفروع ونسب العائلة الكريمة
      </div>
    </div>
  </aside>
"""

header_end = html.find('</header>')
if header_end != -1:
    html = html[:header_end + 9] + "\n" + drawer_markup + html[header_end + 9:]
    print("Added Mobile Drawer markup.")

# 6. In view-tree: Add mode switcher bar and Accordion wrapper
tree_view_pos = html.find('<div id="view-tree" class="view-panel active">')
if tree_view_pos != -1:
    viewport_pos = html.find('<div class="tree-viewport-container">', tree_view_pos)
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
    html = html[:viewport_pos + 37] + "\n" + mode_bar_markup + html[viewport_pos + 37:]
    print("Added tree mode bar.")

    # Add tree accordion wrapper after canvas-wrapper
    canvas_wrap_end = html.find('</div>\n      </div>\n    </div>\n\n    <!-- Branches View -->')
    if canvas_wrap_end == -1:
        canvas_wrap_end = html.find('</div>\n      </div>\n    </div>', tree_view_pos)
    
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
        </div>
"""
    # Insert before the closing of tree-viewport-container
    insert_before = html.find('</div>\n    </div>\n\n    <!-- Branches View -->')
    if insert_before == -1:
        insert_before = html.find('</div>\n    </div>\n', tree_view_pos)
    html = html[:insert_before] + accordion_markup + html[insert_before:]
    print("Added tree accordion wrapper.")

# 7. In view-table: Add mobile filter button, cards container, and pagination
table_view_pos = html.find('<div id="view-table" class="view-panel">')
if table_view_pos != -1:
    # In table-toolbar, add mobile filter button
    toolbar_pos = html.find('<div class="table-toolbar">', table_view_pos)
    filter_btn_markup = """
          <!-- Mobile Filter Button (Opens Bottom Sheet) -->
          <button class="btn btn-primary mobile-filter-btn" id="btn-open-filter-sheet" onclick="openFilterSheet()">
            <span>🔍</span> <span class="t-filter-btn">تصفية الفروع والأجيال</span>
            <span class="active-filter-badge" id="active-filter-count" style="display: none;">0</span>
          </button>
"""
    html = html[:toolbar_pos + 27] + "\n" + filter_btn_markup + html[toolbar_pos + 27:]
    
    # Add mobile member cards and pagination after data-table-wrapper
    table_wrap_end = html.find('</table>\n        </div>', table_view_pos)
    if table_wrap_end != -1:
        table_wrap_close = table_wrap_end + len('</table>\n        </div>')
        mobile_table_markup = """
        <!-- Mobile Member Cards List -->
        <div id="table-cards-container" class="table-cards-container"></div>

        <!-- Table Pagination Controls -->
        <div id="table-pagination" class="table-pagination"></div>
"""
        html = html[:table_wrap_close] + "\n" + mobile_table_markup + html[table_wrap_close:]
        print("Added table cards container and pagination.")

# 8. Add Filter Bottom Sheet modal markup
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

# 9. Add Mobile Bottom Navigation Bar before </body>
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
    print("Added Mobile Bottom Navigation markup.")

# Write updated file to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html HTML and CSS successfully. Length:", len(html))
