import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = "let tableCurrentPage = 1;"
replacement = """function renderTableView() {
      const tbody = document.getElementById('table-tbody');
      const branchSelect = document.getElementById('table-branch-filter');
      const genSelect = document.getElementById('table-gen-filter');
      if (!tbody) return;

      const uniqueBranches = Array.from(new Set(flatMembers.map(m => currentLanguage === 'ar' ? m.branch_ar : m.branch_en)));
      const uniqueGens = Array.from(new Set(flatMembers.map(m => m.generation))).sort((a,b)=>a-b);

      const branchHtml = `<option value="ALL">${currentLanguage === 'ar' ? 'جميع الفروع' : 'All Branches'}</option>` +
        uniqueBranches.map(b => `<option value="${b}">${b}</option>`).join('');
      branchSelect.innerHTML = branchHtml;

      const genHtml = `<option value="ALL">${currentLanguage === 'ar' ? 'جميع الأجيال' : 'All Generations'}</option>` +
        uniqueGens.map(g => `<option value="${g}">${currentLanguage === 'ar' ? `الجيل ${g}` : `Gen ${g}`}</option>`).join('');
      genSelect.innerHTML = genHtml;

      const sheetBranch = document.getElementById('sheet-branch-filter');
      const sheetGen = document.getElementById('sheet-gen-filter');
      if (sheetBranch) sheetBranch.innerHTML = branchHtml;
      if (sheetGen) sheetGen.innerHTML = genHtml;

      filterTable();
    }

    let tableCurrentPage = 1;"""

text = text.replace(target, replacement, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added renderTableView() successfully!")
