# -*- coding: utf-8 -*-
"""
Script to make index.html 100% mobile-friendly, responsive, and touch-optimized
"""
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -----------------------------------------------------------------------------
# 1. Add Comprehensive Mobile CSS
# -----------------------------------------------------------------------------
mobile_css = """
    /* =========================================================================
       MOBILE & TABLET RESPONSIVE STYLES
       ========================================================================= */
    /* Floating Mobile Controls for Tree */
    .mobile-tree-floating-controls {
      display: none;
      position: absolute;
      bottom: 16px;
      left: 16px;
      z-index: 10;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 30px;
      padding: 4px 8px;
      box-shadow: var(--shadow-lg);
      gap: 6px;
      align-items: center;
    }

    [dir="rtl"] .mobile-tree-floating-controls {
      left: auto;
      right: 16px;
    }

    .mobile-float-btn {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      border: 1px solid var(--border);
      background: var(--bg-card-subtle);
      color: var(--text);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      cursor: pointer;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      transition: all 0.2s ease;
    }

    .mobile-float-btn:active {
      transform: scale(0.92);
      background: var(--primary);
      color: white;
    }

    @media (max-width: 900px) {
      .mobile-tree-floating-controls {
        display: flex;
      }
    }

    @media (max-width: 768px) {
      /* General layout */
      body {
        font-size: 14px;
      }

      main {
        padding: 12px 10px;
      }

      /* Header */
      header {
        padding: 10px 12px;
        position: relative !important;
        top: auto !important;
      }

      .header-container {
        flex-direction: column;
        align-items: stretch;
        gap: 12px;
      }

      .brand {
        justify-content: center;
        text-align: center;
      }

      .brand-logo {
        width: 38px;
        height: 38px;
        font-size: 1.15rem;
      }

      .brand-titles h1 {
        font-size: 1.2rem;
      }

      .brand-titles p {
        font-size: 0.78rem;
      }

      .header-actions {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 6px;
      }

      .header-actions .btn {
        padding: 6px 10px;
        font-size: 0.78rem;
        flex-grow: 1;
        justify-content: center;
      }

      .header-actions .btn.btn-icon {
        flex-grow: 0;
      }

      #auth-status-container {
        width: 100%;
        display: flex;
        justify-content: center;
        margin-bottom: 2px;
      }

      #auth-status-container .btn,
      #auth-status-container .auth-badge {
        width: 100%;
        justify-content: center;
        text-align: center;
        font-size: 0.8rem;
      }

      /* Stats Bar */
      .stats-bar {
        padding: 8px 10px;
      }

      .stats-container {
        flex-direction: column;
        gap: 8px;
        align-items: stretch;
      }

      .stat-items {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 6px;
        width: 100%;
      }

      .stat-item {
        font-size: 0.78rem;
        background: var(--bg-card);
        padding: 6px 8px;
        border-radius: var(--radius-sm);
        border: 1px solid var(--border);
        justify-content: space-between;
      }

      /* Navigation Tabs & Search - Mobile Responsive & Touch Optimized */
      .nav-search-bar {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        padding: 8px 10px;
        margin: 0;
        position: sticky;
        top: 0;
        z-index: 60;
        background: rgba(248, 250, 252, 0.94);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-bottom: 1px solid var(--border);
        box-shadow: 0 4px 14px -2px rgba(0, 0, 0, 0.06);
      }

      [data-theme="dark"] .nav-search-bar {
        background: rgba(17, 24, 39, 0.94);
        box-shadow: 0 4px 16px -2px rgba(0, 0, 0, 0.4);
      }

      .tabs-nav-wrapper {
        width: 100%;
        display: flex;
        align-items: center;
        gap: 6px;
        position: relative;
      }

      /* Pill Slider Mode (Default on Mobile) */
      .tabs {
        display: flex;
        overflow-x: auto;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
        scroll-snap-type: x mandatory;
        scrollbar-width: none;
        -ms-overflow-style: none;
        padding: 4px 6px;
        gap: 6px;
        width: 100%;
        border-radius: 14px;
        background: var(--bg-card-subtle);
        border: 1px solid var(--border);
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.04);
      }

      .tabs::-webkit-scrollbar {
        display: none;
      }

      .tab-btn {
        padding: 9px 15px;
        font-size: 0.82rem;
        font-weight: 700;
        flex-shrink: 0;
        scroll-snap-align: center;
        border-radius: 10px;
        background: var(--bg-card);
        color: var(--text-muted);
        border: 1px solid var(--border);
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
        touch-action: manipulation;
        -webkit-tap-highlight-color: transparent;
      }

      .tab-btn:active {
        transform: scale(0.94);
      }

      .tab-btn.active {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%) !important;
        color: #ffffff !important;
        border-color: rgba(255, 255, 255, 0.25) !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35), 0 2px 4px rgba(0, 0, 0, 0.08) !important;
      }

      [data-theme="dark"] .tab-btn.active {
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%) !important;
        color: #ffffff !important;
        border-color: rgba(147, 197, 253, 0.35) !important;
        box-shadow: 0 4px 16px rgba(59, 130, 246, 0.45) !important;
      }

      .tabs-layout-toggle-btn {
        display: inline-flex;
        width: 38px;
        height: 38px;
        border-radius: 10px;
      }

      /* 2-Row / Grid Layout Mode when user toggles grid view */
      .tabs.layout-grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 6px;
        overflow-x: visible;
        white-space: normal;
        padding: 6px;
      }

      .tabs.layout-grid .tab-btn {
        padding: 8px 4px;
        font-size: 0.74rem;
        flex-direction: column;
        gap: 4px;
        text-align: center;
        width: 100%;
        border-radius: 10px;
        scroll-snap-align: none;
      }

      .tabs.layout-grid .tab-btn:nth-child(1),
      .tabs.layout-grid .tab-btn:nth-child(2),
      .tabs.layout-grid .tab-btn:nth-child(3) {
        grid-column: span 2;
      }

      .tabs.layout-grid .tab-btn:nth-child(4),
      .tabs.layout-grid .tab-btn:nth-child(5) {
        grid-column: span 3;
      }

      .tabs.layout-grid .tab-btn-icon {
        font-size: 1.25rem;
      }

      .search-box {
        width: 100%;
        max-width: 100%;
      }

      .search-input {
        width: 100%;
        padding: 8px 34px 8px 32px;
        font-size: 16px !important; /* Prevents auto-zoom on iOS Safari */
        border-radius: 9999px;
      }

      /* Interactive Tree View */
      .tree-viewport-container {
        height: 72vh;
        border-radius: var(--radius-sm);
      }

      .tree-toolbar {
        flex-direction: column;
        align-items: stretch;
        gap: 6px;
        padding: 6px 10px;
      }

      .tree-toolbar > div {
        justify-content: space-between;
        width: 100%;
      }

      .tree-toolbar .btn {
        padding: 4px 8px;
        font-size: 0.75rem;
      }

      .tree-canvas-wrapper {
        touch-action: pan-x pan-y pinch-zoom;
        cursor: grab;
      }

      .tree-canvas-wrapper:active {
        cursor: grabbing;
      }

      .tree-node {
        min-width: 95px;
        padding: 6px 10px;
        border-radius: 10px;
      }

      .node-name {
        font-size: 0.9rem;
      }

      .node-sub {
        font-size: 0.68rem;
      }

      .node-badge {
        font-size: 0.6rem;
        padding: 1px 5px;
      }

      /* Branches View */
      .branches-grid {
        grid-template-columns: 1fr;
        gap: 14px;
      }

      .branch-card {
        border-radius: var(--radius-sm);
      }

      .branch-header {
        padding: 12px 14px;
      }

      .branch-body {
        padding: 12px 14px;
      }

      /* Directory & Tables */
      .table-container {
        border-radius: var(--radius-sm);
        margin-bottom: 16px;
      }

      .table-header {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        padding: 12px 14px;
      }

      .table-filters {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        width: 100%;
      }

      .table-filters .form-select {
        width: 100%;
        font-size: 16px !important;
      }

      .data-table th, .data-table td {
        padding: 8px 10px;
        font-size: 0.8rem;
      }

      .data-table-wrapper {
        -webkit-overflow-scrolling: touch;
      }

      /* Users Management View */
      .users-header-bar {
        flex-direction: column;
        align-items: stretch;
        padding: 14px;
      }

      .users-header-bar > div:last-child {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6px;
        width: 100%;
      }

      .users-header-bar > div:last-child .btn,
      .users-header-bar > div:last-child label.btn {
        width: 100%;
        justify-content: center;
        text-align: center;
      }

      .users-stats-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 8px;
      }

      .user-metric-card {
        padding: 10px 12px;
        gap: 10px;
      }

      .metric-icon {
        width: 38px;
        height: 38px;
        font-size: 1.15rem;
      }

      .metric-val {
        font-size: 1.2rem;
      }

      .metric-lbl {
        font-size: 0.72rem;
      }

      .session-banner {
        flex-direction: column;
        align-items: stretch;
        text-align: center;
        gap: 10px;
        padding: 12px 14px;
      }

      .session-banner button {
        width: 100%;
      }

      /* Modals on Mobile */
      .modal-window {
        width: 95% !important;
        max-width: 95% !important;
        max-height: 90vh;
        overflow-y: auto;
        margin: auto;
        border-radius: var(--radius);
      }

      .modal-header {
        padding: 12px 16px;
      }

      .modal-header h3 {
        font-size: 1.05rem;
      }

      .modal-body {
        padding: 14px 16px;
      }

      .modal-footer {
        padding: 12px 16px;
        flex-wrap: wrap;
        gap: 8px;
      }

      .modal-footer .btn {
        flex: 1;
        justify-content: center;
      }

      /* Form Controls iOS Optimization */
      .form-input, .form-select, .form-textarea {
        font-size: 16px !important; /* Critical to prevent iOS Safari auto zoom */
        padding: 9px 12px;
      }

      /* Footer */
      footer {
        padding: 16px 12px;
        font-size: 0.85rem;
      }

      .footer-author {
        font-size: 0.9rem;
        padding: 3px 12px;
      }
    }

    @media (max-width: 420px) {
      .stat-items {
        grid-template-columns: 1fr;
      }

      .users-stats-grid {
        grid-template-columns: 1fr;
      }
    }
"""

if '/* MOBILE & TABLET RESPONSIVE STYLES */' not in content:
    target_css_end = '  </style>'
    content = content.replace(target_css_end, mobile_css + '\n  </style>')

# -----------------------------------------------------------------------------
# 2. Add Floating Mobile Controls inside tree-viewport-container
# -----------------------------------------------------------------------------
mobile_floating_html = """
          <!-- Floating Mobile Controls for Touch Navigation -->
          <div class="mobile-tree-floating-controls" id="mobile-floating-zoom">
            <button class="mobile-float-btn" onclick="zoomTree(0.15)" title="تكبير">➕</button>
            <button class="mobile-float-btn" onclick="zoomTree(-0.15)" title="تصغير">➖</button>
            <button class="mobile-float-btn" onclick="resetZoom()" title="إعادة ضبط">🎯</button>
            <button class="mobile-float-btn" onclick="expandAllNodes()" title="بسط الفروع">📂</button>
          </div>
"""

target_canvas_end = '          </div>\n        </div>\n      </div>'
if 'id="mobile-floating-zoom"' not in content:
    content = content.replace('<div class="tree-canvas-wrapper" id="canvas-wrapper">',
                            '<div class="tree-canvas-wrapper" id="canvas-wrapper">\n' + mobile_floating_html)

# -----------------------------------------------------------------------------
# 3. Add Touch Dragging & Pinch-to-Zoom in initPanZoom
# -----------------------------------------------------------------------------
old_pan_zoom = """    function initPanZoom() {
      const wrapper = document.getElementById('canvas-wrapper');
      if (!wrapper) return;

      let isDown = false;
      let startX, startY, scrollLeft, scrollTop;

      wrapper.addEventListener('mousedown', (e) => {
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

      wrapper.addEventListener('wheel', (e) => {
        if (e.ctrlKey) {
          e.preventDefault();
          zoomTree(e.deltaY < 0 ? 0.1 : -0.1);
        }
      });
    }"""

new_pan_zoom = """    function initPanZoom() {
      const wrapper = document.getElementById('canvas-wrapper');
      if (!wrapper) return;

      let isDown = false;
      let startX, startY, scrollLeft, scrollTop;

      // Desktop Mouse Pan
      wrapper.addEventListener('mousedown', (e) => {
        if (e.target.closest('.tree-node') || e.target.closest('.mobile-float-btn')) return;
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

      // Desktop Ctrl + Wheel Zoom
      wrapper.addEventListener('wheel', (e) => {
        if (e.ctrlKey) {
          e.preventDefault();
          zoomTree(e.deltaY < 0 ? 0.1 : -0.1);
        }
      }, { passive: false });

      // Mobile Touch Pan & Pinch-to-Zoom
      let touchStartX = 0, touchStartY = 0;
      let touchScrollLeft = 0, touchScrollTop = 0;
      let isTouching = false;
      let initialPinchDistance = null;
      let initialZoomOnPinch = 1;

      wrapper.addEventListener('touchstart', (e) => {
        if (e.target.closest('.mobile-float-btn')) return;

        if (e.touches.length === 1) {
          isTouching = true;
          touchStartX = e.touches[0].pageX - wrapper.offsetLeft;
          touchStartY = e.touches[0].pageY - wrapper.offsetTop;
          touchScrollLeft = wrapper.scrollLeft;
          touchScrollTop = wrapper.scrollTop;
          initialPinchDistance = null;
        } else if (e.touches.length === 2) {
          isTouching = false;
          initialPinchDistance = Math.hypot(
            e.touches[0].pageX - e.touches[1].pageX,
            e.touches[0].pageY - e.touches[1].pageY
          );
          initialZoomOnPinch = treeZoom;
        }
      }, { passive: true });

      wrapper.addEventListener('touchmove', (e) => {
        if (e.touches.length === 1 && isTouching) {
          const currentX = e.touches[0].pageX - wrapper.offsetLeft;
          const currentY = e.touches[0].pageY - wrapper.offsetTop;
          const deltaX = (currentX - touchStartX) * 1.2;
          const deltaY = (currentY - touchStartY) * 1.2;
          wrapper.scrollLeft = touchScrollLeft - deltaX;
          wrapper.scrollTop = touchScrollTop - deltaY;
        } else if (e.touches.length === 2 && initialPinchDistance) {
          e.preventDefault(); // Prevent standard page zooming
          const currentDistance = Math.hypot(
            e.touches[0].pageX - e.touches[1].pageX,
            e.touches[0].pageY - e.touches[1].pageY
          );
          const factor = currentDistance / initialPinchDistance;
          let newZoom = initialZoomOnPinch * factor;
          newZoom = Math.min(Math.max(newZoom, 0.25), 2.0);
          treeZoom = Math.round(newZoom * 100) / 100;
          updateCanvasTransform();
        }
      }, { passive: false });

      wrapper.addEventListener('touchend', (e) => {
        if (e.touches.length === 0) {
          isTouching = false;
          initialPinchDistance = null;
        } else if (e.touches.length === 1) {
          touchStartX = e.touches[0].pageX - wrapper.offsetLeft;
          touchStartY = e.touches[0].pageY - wrapper.offsetTop;
          touchScrollLeft = wrapper.scrollLeft;
          touchScrollTop = wrapper.scrollTop;
          isTouching = true;
          initialPinchDistance = null;
        }
      }, { passive: true });

      // Adaptive initial zoom on mobile screens
      if (window.innerWidth <= 768 && treeZoom === 1.0) {
        treeZoom = 0.65;
        updateCanvasTransform();
      }
    }"""

if old_pan_zoom in content:
    content = content.replace(old_pan_zoom, new_pan_zoom)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Mobile responsiveness and touch engine added successfully!')
