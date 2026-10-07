# -*- coding: utf-8 -*-
"""
Script to set 'Collapse to Ancestors' active by default on initial page load
"""
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update toolbar buttons to give IDs and initial primary style to collapse button
old_buttons = """          <div style="display: flex; gap: 8px; align-items: center;">
            <button class="btn btn-sm" onclick="expandAllNodes()">📂 <span class="t-expand-all">بسط الكل</span></button>
            <button class="btn btn-sm" onclick="collapseToGen(4)">📁 <span class="t-collapse-branches">طي للأجداد</span></button>
          </div>"""

new_buttons = """          <div style="display: flex; gap: 8px; align-items: center;">
            <button class="btn btn-sm" onclick="expandAllNodes()" id="btn-expand-all">📂 <span class="t-expand-all">بسط الكل</span></button>
            <button class="btn btn-sm btn-primary" onclick="collapseToGen(4)" id="btn-collapse-ancestors">📁 <span class="t-collapse-branches">طي للأجداد</span></button>
          </div>"""

if old_buttons in content:
    content = content.replace(old_buttons, new_buttons)

# 2. Update mobile floating controls to include both collapse and expand with proper titles
old_mobile_float = """          <!-- Floating Mobile Controls for Touch Navigation -->
          <div class="mobile-tree-floating-controls" id="mobile-floating-zoom">
            <button class="mobile-float-btn" onclick="zoomTree(0.15)" title="تكبير">➕</button>
            <button class="mobile-float-btn" onclick="zoomTree(-0.15)" title="تصغير">➖</button>
            <button class="mobile-float-btn" onclick="resetZoom()" title="إعادة ضبط">🎯</button>
            <button class="mobile-float-btn" onclick="expandAllNodes()" title="بسط الفروع">📂</button>
          </div>"""

new_mobile_float = """          <!-- Floating Mobile Controls for Touch Navigation -->
          <div class="mobile-tree-floating-controls" id="mobile-floating-zoom">
            <button class="mobile-float-btn" onclick="zoomTree(0.15)" title="تكبير">➕</button>
            <button class="mobile-float-btn" onclick="zoomTree(-0.15)" title="تصغير">➖</button>
            <button class="mobile-float-btn" onclick="resetZoom()" title="إعادة ضبط">🎯</button>
            <button class="mobile-float-btn" onclick="collapseToGen(4)" id="mobile-float-collapse" title="طي للأجداد">📁</button>
            <button class="mobile-float-btn" onclick="expandAllNodes()" id="mobile-float-expand" title="بسط الفروع">📂</button>
          </div>"""

if old_mobile_float in content:
    content = content.replace(old_mobile_float, new_mobile_float)

# 3. Update expandAllNodes and collapseToGen functions with button highlights and centering
old_collapse_funcs = """    function expandAllNodes() {
      collapsedNodes.clear();
      renderTreeView();
    }

    function collapseToGen(genLimit) {
      collapsedNodes.clear();
      flatMembers.forEach(m => {
        if (m.generation >= genLimit && m.children_count > 0) {
          collapsedNodes.add(m.id);
        }
      });
      renderTreeView();
    }"""

new_collapse_funcs = """    function updateTreeToggleButtons(isCollapsed) {
      const btnCollapse = document.getElementById('btn-collapse-ancestors');
      const btnExpand = document.getElementById('btn-expand-all');
      const floatCollapse = document.getElementById('mobile-float-collapse');
      const floatExpand = document.getElementById('mobile-float-expand');

      if (btnCollapse && btnExpand) {
        if (isCollapsed) {
          btnCollapse.classList.add('btn-primary');
          btnExpand.classList.remove('btn-primary');
        } else {
          btnExpand.classList.add('btn-primary');
          btnCollapse.classList.remove('btn-primary');
        }
      }
      if (floatCollapse && floatExpand) {
        if (isCollapsed) {
          floatCollapse.style.borderColor = 'var(--primary)';
          floatExpand.style.borderColor = 'var(--border)';
        } else {
          floatExpand.style.borderColor = 'var(--primary)';
          floatCollapse.style.borderColor = 'var(--border)';
        }
      }
    }

    function expandAllNodes() {
      collapsedNodes.clear();
      renderTreeView();
      updateTreeToggleButtons(false);
      setTimeout(() => {
        const wrapper = document.getElementById('canvas-wrapper');
        if (wrapper) {
          wrapper.scrollLeft = (wrapper.scrollWidth - wrapper.clientWidth) / 2;
        }
      }, 50);
    }

    function collapseToGen(genLimit = 4) {
      collapsedNodes.clear();
      flatMembers.forEach(m => {
        if (m.generation >= genLimit && m.children_count > 0) {
          collapsedNodes.add(m.id);
        }
      });
      renderTreeView();
      updateTreeToggleButtons(true);
      setTimeout(() => {
        const wrapper = document.getElementById('canvas-wrapper');
        if (wrapper) {
          wrapper.scrollLeft = (wrapper.scrollWidth - wrapper.clientWidth) / 2;
          wrapper.scrollTop = 0;
        }
      }, 50);
    }"""

if old_collapse_funcs in content:
    content = content.replace(old_collapse_funcs, new_collapse_funcs)

# 4. Trigger collapseToGen(4) and center scroll in DOMContentLoaded
old_init = """    // Initialization
    window.addEventListener('DOMContentLoaded', () => {
      loadSavedState();
      initAuth();
      initTheme();
      initLanguage();
      renderAllViews();
      initPanZoom();
    });"""

new_init = """    // Initialization
    window.addEventListener('DOMContentLoaded', () => {
      loadSavedState();
      initAuth();
      initTheme();
      initLanguage();
      renderAllViews();
      // Collapse to ancestors by default on initial page load
      collapseToGen(4);
      initPanZoom();
      setTimeout(() => {
        const wrapper = document.getElementById('canvas-wrapper');
        if (wrapper) {
          wrapper.scrollLeft = (wrapper.scrollWidth - wrapper.clientWidth) / 2;
          wrapper.scrollTop = 0;
        }
      }, 120);
    });"""

if old_init in content:
    content = content.replace(old_init, new_init)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Default collapse to ancestors configured successfully in index.html!')
