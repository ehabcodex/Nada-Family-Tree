import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Original length:", len(text))

# 1. Fix Tree Canvas & Connector lines in CSS
# Search for tree canvas / ft-tree block in CSS
css_old_tree_start = text.find('.tree-canvas-wrapper {')
css_old_tree_end = text.find('/* بطاقة فرد الشجرة (Tree Node) */')

if css_old_tree_start != -1 and css_old_tree_end != -1:
    new_tree_css = """.tree-canvas-wrapper {
  position: relative;
  overflow: auto;
  min-height: 580px;
  max-height: 75vh;
  background: radial-gradient(circle at 1px 1px, var(--border) 1px, transparent 0);
  background-size: 24px 24px;
  cursor: grab;
  touch-action: pan-x pan-y;
  user-select: none;
}

.tree-canvas-wrapper:active {
  cursor: grabbing;
}

/* NOTE: The geometric graph coordinates use direction: ltr to ensure
   connecting lines never suffer from RTL coordinate reversal bugs,
   while the tree cards themselves preserve RTL Arabic text and badges! */
.tree-canvas {
  direction: ltr !important;
  transform-origin: 0 0;
  padding: 60px;
  display: inline-block;
  min-width: 100%;
  text-align: center;
  transition: transform 0.15s ease-out;
}

.ft-tree, .ft-tree ul {
  margin: 0;
  padding: 0;
  list-style-type: none;
  display: flex;
  justify-content: center;
  position: relative;
  direction: ltr !important;
}

.ft-tree ul {
  padding-top: 28px;
}

.ft-tree li {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  padding: 0 8px;
  direction: ltr !important;
}

/* Connector lines - Rock solid in both Arabic and English */
.ft-tree li::before, .ft-tree li::after {
  content: '';
  position: absolute;
  top: 0;
  right: 50%;
  border-top: 2px solid var(--tree-line);
  width: 50%;
  height: 28px;
}

.ft-tree li::after {
  right: auto;
  left: 50%;
  border-left: 2px solid var(--tree-line);
}

.ft-tree li:only-child::after, .ft-tree li:only-child::before {
  display: none;
}

.ft-tree li:only-child {
  padding-top: 0;
}

.ft-tree li:first-child::before, .ft-tree li:last-child::after {
  border: 0 none;
}

.ft-tree li:last-child::before {
  border-right: 2px solid var(--tree-line);
  border-radius: 0 8px 0 0;
}

.ft-tree li:first-child::after {
  border-radius: 8px 0 0 0;
}

.ft-tree ul::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  border-left: 2px solid var(--tree-line);
  width: 0;
  height: 28px;
}

.ft-tree li.collapsed > ul {
  display: none !important;
}

"""
    text = text[:css_old_tree_start] + new_tree_css + text[css_old_tree_end:]
    print("Fixed Tree Canvas & Connector Lines in CSS.")

# Ensure .tree-node handles direction properly
node_css_marker = ".tree-node {"
pos_node = text.find(node_css_marker)
if pos_node != -1:
    # Check if direction rtl is in tree-node
    node_block = text[pos_node:pos_node+400]
    if 'direction: rtl;' not in node_block:
        text = text[:pos_node + len(node_css_marker)] + "\n  direction: rtl;\n  text-align: center;" + text[pos_node + len(node_css_marker):]
        print("Ensured .tree-node has direction: rtl.")

# 2. Add Toast & Footer CSS
toast_footer_css = """
/* Toast Notification */
.toast {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-inline-start: 4px solid var(--primary);
  box-shadow: var(--shadow-lg);
  padding: 12px 20px;
  border-radius: var(--radius-sm);
  z-index: 200;
  display: none;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text);
}

[dir="rtl"] .toast {
  right: auto;
  left: 24px;
}

.toast.show {
  display: flex !important;
  animation: toastIn 0.3s ease;
}

@keyframes toastIn {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@media (max-width: 639.98px) {
  .toast {
    bottom: calc(var(--bottom-nav-height) + env(safe-area-inset-bottom) + 12px);
    left: 50% !important;
    right: auto !important;
    transform: translateX(-50%);
    width: calc(100% - 32px);
    max-width: 360px;
    justify-content: center;
  }
}

/* Footer - Centered */
footer {
  margin-top: auto;
  background: var(--bg-card);
  border-top: 1px solid var(--border);
  padding: 24px 16px;
  text-align: center;
  font-size: 0.88rem;
  color: var(--text-muted);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  width: 100%;
}

footer p {
  text-align: center;
  margin: 0;
  font-size: 0.92rem;
  color: var(--text-muted);
}

.footer-author {
  font-weight: 700;
  color: var(--primary);
  text-align: center;
  font-family: var(--font-title);
  font-size: 1.1rem;
  margin: 0;
}
"""

# Insert before @media print
print_pos = text.find('@media print {')
if print_pos != -1:
    text = text[:print_pos] + toast_footer_css + "\n" + text[print_pos:]
    print("Added Toast and Centered Footer CSS.")

# 3. Clean up the HTML Toast element so it doesn't show statically
toast_html_old = """  <!-- Toast -->
  <div class="toast" id="toast">
    <span id="toast-icon">✅</span>
    <span id="toast-msg">تمت العملية بنجاح</span>
  </div>"""

toast_html_new = """  <!-- Toast Notification (Hidden by default, shown via showToast) -->
  <div class="toast" id="toast" style="display: none;" aria-live="polite">
    <span id="toast-icon"></span>
    <span id="toast-msg"></span>
  </div>"""

if toast_html_old in text:
    text = text.replace(toast_html_old, toast_html_new)
    print("Removed static '✅ تمت العملية بنجاح' from HTML.")
else:
    # Try regex match
    text = re.sub(r'<div class="toast" id="toast">[\s\S]*?</div>', toast_html_new, text)
    print("Replaced toast HTML with clean hidden element.")

# 4. Center-align footer elements explicitly in HTML
footer_html_old = """  <!-- Footer -->
  <footer>
    <p>شجرة عائلة آل ندى © 2026</p>
    <div class="footer-author">إعداد: إيهاب ندى</div>
  </footer>"""

footer_html_new = """  <!-- Footer -->
  <footer style="text-align: center;">
    <p style="text-align: center; margin: 0;">شجرة عائلة آل ندى © 2026</p>
    <div class="footer-author" style="text-align: center; margin-top: 4px;">إعداد: إيهاب ندى</div>
  </footer>"""

if footer_html_old in text:
    text = text.replace(footer_html_old, footer_html_new)
    print("Centered footer HTML explicitly.")
else:
    text = re.sub(r'<footer>[\s\S]*?</footer>', footer_html_new, text)
    print("Replaced footer with centered HTML.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Updates saved successfully! New length: {len(text)} bytes")
