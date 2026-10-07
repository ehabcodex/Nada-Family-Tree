import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Original length: {len(text)} bytes")

# 1. Update Header Button: Replace Print with Export to PDF
old_hdr_btn = re.search(r'<!-- Print / PDF Export Button -->[\s\S]*?</button>', text)
new_hdr_btn = """<!-- Export to PDF Button -->
        <button class="btn btn-success" onclick="exportToPDF()" id="btn-export-pdf" title="تصدير شجرة العائلة كملف PDF">
          <span>📄</span>
          <span class="t-export-pdf">تصدير PDF</span>
        </button>"""

if old_hdr_btn:
    text = text[:old_hdr_btn.start()] + new_hdr_btn + text[old_hdr_btn.end():]
    print("Replaced header Print button with PDF export button.")
else:
    print("Warning: old header button not matched directly, trying alternative search.")
    text = re.sub(r'<button class="btn btn-success"[^>]*onclick="printOrExportPDF\(\)"[^>]*>[\s\S]*?</button>', new_hdr_btn, text)

# 2. Update Drawer Button: Replace Print with Export to PDF
old_drw_btn = '<button class="drawer-action-btn" onclick="closeMobileDrawer(); printOrExportPDF()">'
new_drw_btn = '<button class="drawer-action-btn" onclick="closeMobileDrawer(); exportToPDF()">'
text = text.replace(old_drw_btn, new_drw_btn)
text = text.replace('<span class="t-print-pdf">طباعة / تصدير PDF</span>', '<span class="t-export-pdf">تصدير كـ ملف PDF</span>')
print("Updated drawer PDF export button.")

# 3. Update I18N and applyTranslations
text = text.replace('printPdf: "طباعة / PDF",', 'exportPdf: "تصدير كـ PDF",\n        printPdf: "تصدير كـ PDF",')
text = text.replace('printPdf: "Print / PDF",', 'exportPdf: "Export to PDF",\n        printPdf: "Export to PDF",')

text = text.replace(
    "document.querySelectorAll('.t-print-pdf').forEach(el => el.textContent = t.printPdf);",
    "document.querySelectorAll('.t-print-pdf').forEach(el => el.textContent = t.exportPdf);\n      document.querySelectorAll('.t-export-pdf').forEach(el => el.textContent = t.exportPdf);"
)
print("Updated translations for PDF export.")

# 4. Replace printOrExportPDF with exportToPDF
old_fn_pos = text.find('function printOrExportPDF() {')
if old_fn_pos != -1:
    old_fn_end = text.find('}', old_fn_pos) + 1
    new_fn = """function exportToPDF() {
      // التأكد من بسط الشجرة بالكامل قبل التصدير
      expandAllNodes();

      const oldTitle = document.title;
      const pdfTitle = currentLanguage === 'ar' ? 'شجرة_عائلة_آل_ندى_توثيق_الأنساب' : 'Al_Nada_Family_Tree_Official_Chart';
      document.title = pdfTitle;

      showToast(currentLanguage === 'ar' ? '📄 جاري فتح تجهيز ملف PDF... اختر حفظ بتنسيق PDF' : '📄 Preparing PDF export... Select (Save as PDF)');

      setTimeout(() => {
        window.print();
        setTimeout(() => {
          document.title = oldTitle;
        }, 1500);
      }, 350);
    }

    function printOrExportPDF() {
      exportToPDF();
    }"""
    text = text[:old_fn_pos] + new_fn + text[old_fn_end:]
    print("Replaced print function with exportToPDF.")

# 5. Add Complete 10 Generations Color Palette to CSS
# Find existing .tree-node.level-0
level_pos = text.find('.tree-node.level-0 {')
if level_pos != -1:
    level_end = text.find('.tree-node.highlighted {', level_pos)
    
    new_levels_css = """/* ==========================================================================
   ألوان الأجيال المميزة والمتناوبة (Distinct Generation Colors: Gen 0 to Gen 10)
   ========================================================================== */

/* الجيل 0: الجد المؤسس الأقدم (الأصل) */
.tree-node.level-0 {
  background: linear-gradient(135deg, #183827 0%, #2F5D46 100%);
  color: #FFFFFF;
  border: 3px solid #142E20;
  padding: 14px 28px;
  border-radius: 24px;
  box-shadow: 0 4px 14px rgba(24, 56, 39, 0.4);
}
.tree-node.level-0 .node-name { color: #FFFFFF; font-size: 1.35rem; font-weight: 800; }
.tree-node.level-0 .node-sub { color: rgba(255, 255, 255, 0.9); }
.tree-node.level-0 .node-badge, .gen-badge-0 { background: #B8893B !important; color: #FFFFFF !important; font-weight: 700; border: 1px solid #D5A34F; }

/* الجيل 1: الجد مصطفى الأول */
.tree-node.level-1 {
  background: linear-gradient(135deg, #8A5E16 0%, #B8893B 100%);
  color: #FFFFFF;
  border: 3px solid #6E490E;
  border-radius: 20px;
  padding: 12px 24px;
  box-shadow: 0 4px 12px rgba(184, 137, 59, 0.4);
}
.tree-node.level-1 .node-name { color: #FFFFFF; font-size: 1.22rem; font-weight: 800; }
.tree-node.level-1 .node-sub { color: rgba(255, 255, 255, 0.9); }
.tree-node.level-1 .node-badge, .gen-badge-1 { background: #2F5D46 !important; color: #FFFFFF !important; font-weight: 700; border: 1px solid #417D5F; }

/* الجيل 2: الجد الجامع أحمد بن مصطفى */
.tree-node.level-2 {
  background: linear-gradient(135deg, #8E3E18 0%, #C45F34 100%);
  color: #FFFFFF;
  border: 3px solid #732E0F;
  border-radius: 18px;
  padding: 11px 20px;
  box-shadow: 0 4px 12px rgba(196, 95, 52, 0.35);
}
.tree-node.level-2 .node-name { color: #FFFFFF; font-size: 1.15rem; font-weight: 800; }
.tree-node.level-2 .node-sub { color: rgba(255, 255, 255, 0.9); }
.tree-node.level-2 .node-badge, .gen-badge-2 { background: #183827 !important; color: #FFFFFF !important; font-weight: 700; border: 1px solid #2F5D46; }

/* الجيل 3: رؤوس الفروع الأولى - أخضر تيل بحري وقور */
.tree-node.level-3 {
  background: var(--node-bg);
  border: 2px solid #165654;
  border-top: 5px solid #165654;
}
.tree-node.level-3 .node-badge, .gen-badge-3 { background: #E0F2F1 !important; color: #004D40 !important; border: 1px solid #80CBC4; font-weight: 700; }
[data-theme="dark"] .tree-node.level-3 { border-color: #4DB6AC; border-top-color: #4DB6AC; }
[data-theme="dark"] .tree-node.level-3 .node-badge, [data-theme="dark"] .gen-badge-3 { background: #00332C !important; color: #80CBC4 !important; border-color: #00695C; }

/* الجيل 4: الفروع السبعة الرئيسية - أزرق ملكي ياقوتي */
.tree-node.level-4 {
  background: var(--node-bg);
  border: 2px solid #1B4E80;
  border-top: 5px solid #1B4E80;
}
.tree-node.level-4 .node-badge, .gen-badge-4 { background: #E1F5FE !important; color: #01579B !important; border: 1px solid #81D4FA; font-weight: 700; }
[data-theme="dark"] .tree-node.level-4 { border-color: #64B5F6; border-top-color: #64B5F6; }
[data-theme="dark"] .tree-node.level-4 .node-badge, [data-theme="dark"] .gen-badge-4 { background: #012A4A !important; color: #90CAF9 !important; border-color: #0D47A1; }

/* الجيل 5: الأجداد - بنفسجي توتي أرجواني فاخر */
.tree-node.level-5 {
  background: var(--node-bg);
  border: 2px solid #632C59;
  border-top: 5px solid #632C59;
}
.tree-node.level-5 .node-badge, .gen-badge-5 { background: #F3E5F5 !important; color: #4A148C !important; border: 1px solid #CE93D8; font-weight: 700; }
[data-theme="dark"] .tree-node.level-5 { border-color: #BA68C8; border-top-color: #BA68C8; }
[data-theme="dark"] .tree-node.level-5 .node-badge, [data-theme="dark"] .gen-badge-5 { background: #2E0854 !important; color: #E1BEE7 !important; border-color: #6A1B9A; }

/* الجيل 6: الآباء الكبار - عنبري زعفراني دافئ */
.tree-node.level-6 {
  background: var(--node-bg);
  border: 2px solid #825412;
  border-top: 5px solid #825412;
}
.tree-node.level-6 .node-badge, .gen-badge-6 { background: #FFF8E1 !important; color: #B75302 !important; border: 1px solid #FFE082; font-weight: 700; }
[data-theme="dark"] .tree-node.level-6 { border-color: #FFD54F; border-top-color: #FFD54F; }
[data-theme="dark"] .tree-node.level-6 .node-badge, [data-theme="dark"] .gen-badge-6 { background: #3E2405 !important; color: #FFE082 !important; border-color: #B75302; }

/* الجيل 7: جيل الآباء المعاصرين - زمردي غض نضر */
.tree-node.level-7 {
  background: var(--node-bg);
  border: 2px solid #1B653F;
  border-top: 5px solid #1B653F;
}
.tree-node.level-7 .node-badge, .gen-badge-7 { background: #E8F5E9 !important; color: #1B5E20 !important; border: 1px solid #A5D6A7; font-weight: 700; }
[data-theme="dark"] .tree-node.level-7 { border-color: #81C784; border-top-color: #81C784; }
[data-theme="dark"] .tree-node.level-7 .node-badge, [data-theme="dark"] .gen-badge-7 { background: #06280E !important; color: #A5D6A7 !important; border-color: #2E7D32; }

/* الجيل 8: جيل الشباب - نيلي فولاذي هادئ */
.tree-node.level-8 {
  background: var(--node-bg);
  border: 2px solid #2F4D66;
  border-top: 5px solid #2F4D66;
}
.tree-node.level-8 .node-badge, .gen-badge-8 { background: #ECEFF1 !important; color: #263238 !important; border: 1px solid #B0BEC5; font-weight: 700; }
[data-theme="dark"] .tree-node.level-8 { border-color: #90A4AE; border-top-color: #90A4AE; }
[data-theme="dark"] .tree-node.level-8 .node-badge, [data-theme="dark"] .gen-badge-8 { background: #1A2733 !important; color: #CFD8DC !important; border-color: #455A64; }

/* الجيل 9: جيل الفتيان والأحفاد - قرمزي رماني حيوي */
.tree-node.level-9 {
  background: var(--node-bg);
  border: 2px solid #913030;
  border-top: 5px solid #913030;
}
.tree-node.level-9 .node-badge, .gen-badge-9 { background: #FFEBEE !important; color: #B71C1C !important; border: 1px solid #FFCDD2; font-weight: 700; }
[data-theme="dark"] .tree-node.level-9 { border-color: #E57373; border-top-color: #E57373; }
[data-theme="dark"] .tree-node.level-9 .node-badge, [data-theme="dark"] .gen-badge-9 { background: #380808 !important; color: #FFCDD2 !important; border-color: #C62828; }

/* الجيل 10: جيل الأطفال والبراعم الواعدة - فيروزي تركوازي مشرق */
.tree-node.level-10 {
  background: var(--node-bg);
  border: 2px solid #146B65;
  border-top: 5px solid #146B65;
}
.tree-node.level-10 .node-badge, .gen-badge-10 { background: #E0F7FA !important; color: #006064 !important; border: 1px solid #80DEEA; font-weight: 700; }
[data-theme="dark"] .tree-node.level-10 { border-color: #4DD0E1; border-top-color: #4DD0E1; }
[data-theme="dark"] .tree-node.level-10 .node-badge, [data-theme="dark"] .gen-badge-10 { background: #002B30 !important; color: #80DEEA !important; border-color: #00838F; }

"""
    text = text[:level_pos] + new_levels_css + text[level_end:]
    print("Added distinctive colors for all 10 generations to CSS.")

# 6. Apply generation badges in Accordion view and Directory Table
# In renderAccordionView():
text = text.replace(
    '<span class="acc-badge gen">${genText}</span>',
    '<span class="acc-badge gen gen-badge-${node.generation}">${genText}</span>'
)

# In filterTable() mobile cards:
text = text.replace(
    '<span class="tag-badge" style="background: rgba(var(--accent-rgb), 0.15); color: var(--accent-dark);">${genLabel}</span>',
    '<span class="tag-badge gen-badge-${m.generation}">${genLabel}</span>'
)

# In filterTable() table rows:
text = text.replace(
    '<td><span class="tag-badge">${m.generation}</span></td>',
    '<td><span class="tag-badge gen-badge-${m.generation}">${m.generation}</span></td>'
)

print("Applied generation color badge classes to Accordion and Table.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Updates successfully applied! File length: {len(text)} bytes")
