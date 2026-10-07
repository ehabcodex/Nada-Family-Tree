const fs = require('fs');

const content = fs.readFileSync('index.html', 'utf8');

console.log("File size:", content.length, "bytes");

// 1. Check <script> syntax
const scriptMatch = content.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
  try {
    new Function(scriptMatch[1]);
    console.log("JavaScript syntax check: PASSED (No syntax errors)");
  } catch (err) {
    console.error("JavaScript syntax check FAILED:", err.message);
    process.exit(1);
  }
} else {
  console.error("No script tag found!");
  process.exit(1);
}

// 2. Check essential IDs
const essentialIds = [
  'main-tabs', 'main-search', 'view-tree', 'tree-canvas',
  'tree-mode-bar', 'btn-mode-tree', 'btn-mode-accordion',
  'tree-accordion-wrapper', 'tree-accordion-container',
  'canvas-wrapper', 'mobile-floating-zoom',
  'view-table', 'table-tbody', 'table-cards-container', 'table-pagination',
  'btn-open-filter-sheet', 'filter-bottom-sheet', 'sheet-branch-filter', 'sheet-gen-filter',
  'view-branches', 'view-stats', 'view-users',
  'mobile-bottom-nav', 'mobile-nav-drawer', 'mobile-drawer-toggle',
  'member-modal', 'add-modal', 'login-modal', 'theme-btn', 'lang-btn'
];

let missingIds = [];
essentialIds.forEach(id => {
  if (!content.includes(`id="${id}"`)) {
    missingIds.push(id);
  }
});

if (missingIds.length > 0) {
  console.warn("Missing IDs:", missingIds);
} else {
  console.log("All essential HTML element IDs present:", essentialIds.length);
}

// 3. Check CSS variables
const requiredVars = [
  '--bg', '--bg-card', '--primary', '--accent', '--text',
  '--font-title', '--font-ar', '--tree-line'
];

requiredVars.forEach(v => {
  if (content.includes(v)) {
    console.log(`CSS Variable ${v}: OK`);
  } else {
    console.warn(`Missing CSS Variable ${v}`);
  }
});
