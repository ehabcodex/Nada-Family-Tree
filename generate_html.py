# -*- coding: utf-8 -*-
"""
Generate complete standalone bilingual interactive HTML page for Al-Nada Family Tree
"""
import json
import os

out_dir = r"C:\Users\user\.gemini\antigravity\scratch\al_nada_family_tree"
with open(os.path.join(out_dir, "family_tree.json"), "r", encoding="utf-8") as f:
    tree_data = json.load(f)

with open(os.path.join(out_dir, "family_members_flat.json"), "r", encoding="utf-8") as f:
    flat_data = json.load(f)

tree_json_str = json.dumps(tree_data, ensure_ascii=False)
flat_json_str = json.dumps(flat_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>شجرة عائلة آل ندى | Al-Nada Family Tree</title>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #1e3a8a;
      --primary-light: #3b82f6;
      --primary-dark: #172554;
      --accent: #d97706;
      --accent-light: #f59e0b;
      --bg: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-subtle: #f1f5f9;
      --border: #e2e8f0;
      --border-strong: #cbd5e1;
      --text: #0f172a;
      --text-muted: #64748b;
      --text-light: #94a3b8;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --radius: 12px;
      --radius-sm: 8px;
      --font-ar: 'Cairo', system-ui, sans-serif;
      --font-en: 'Inter', system-ui, sans-serif;
      --tree-line: #94a3b8;
      --node-bg: #ffffff;
      --node-border: #cbd5e1;
      --node-hover: #eff6ff;
    }}

    [data-theme="dark"] {{
      --primary: #3b82f6;
      --primary-light: #60a5fa;
      --primary-dark: #1d4ed8;
      --accent: #fbbf24;
      --accent-light: #fcd34d;
      --bg: #090d16;
      --bg-card: #111827;
      --bg-card-subtle: #1f2937;
      --border: #283548;
      --border-strong: #374151;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --text-light: #64748b;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.5);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.6);
      --tree-line: #475569;
      --node-bg: #1e293b;
      --node-border: #334155;
      --node-hover: #1e3a5f;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    }}

    body {{
      font-family: var(--font-ar);
      background-color: var(--bg);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.6;
    }}

    body.lang-en {{
      font-family: var(--font-en);
    }}

    /* Header */
    header {{
      background: var(--bg-card);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(12px);
    }}

    .header-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 12px 20px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .brand-logo {{
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 20px;
      box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);
    }}

    .brand-titles h1 {{
      font-size: 1.35rem;
      font-weight: 800;
      line-height: 1.2;
      color: var(--text);
    }}

    .brand-titles p {{
      font-size: 0.82rem;
      color: var(--text-muted);
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border);
      background: var(--bg-card);
      color: var(--text);
      text-decoration: none;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }}

    .btn:hover {{
      background: var(--bg-card-subtle);
      border-color: var(--border-strong);
    }}

    .btn-primary {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    .btn-primary:hover {{
      background: var(--primary-dark);
      border-color: var(--primary-dark);
      color: white;
    }}

    .btn-accent {{
      background: var(--accent);
      color: white;
      border-color: var(--accent);
    }}

    .btn-accent:hover {{
      background: var(--accent-light);
      border-color: var(--accent-light);
      color: white;
    }}

    .btn-sm {{
      padding: 4px 8px;
      font-size: 0.78rem;
    }}

    .btn-icon {{
      width: 38px;
      height: 38px;
      padding: 0;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: var(--radius-sm);
    }}

    /* Stats Bar */
    .stats-bar {{
      background: var(--bg-card-subtle);
      border-bottom: 1px solid var(--border);
      padding: 10px 20px;
    }}

    .stats-container {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      align-items: center;
      justify-content: space-between;
    }}

    .stat-items {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .stat-item {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.85rem;
    }}

    .stat-badge {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      padding: 2px 8px;
      border-radius: 20px;
      font-weight: 700;
      color: var(--primary);
    }}

    /* Search and Nav Tabs */
    .nav-search-bar {{
      max-width: 1440px;
      margin: 16px auto 0;
      padding: 0 20px;
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      justify-content: space-between;
      align-items: center;
    }}

    .tabs {{
      display: flex;
      background: var(--bg-card-subtle);
      padding: 4px;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      gap: 4px;
    }}

    .tab-btn {{
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      border: none;
      background: transparent;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .tab-btn.active {{
      background: var(--bg-card);
      color: var(--text);
      box-shadow: 0 2px 4px rgba(0,0,0,0.06);
    }}

    .search-box {{
      position: relative;
      flex: 1;
      max-width: 380px;
    }}

    .search-input {{
      width: 100%;
      padding: 9px 14px 9px 36px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border);
      background: var(--bg-card);
      color: var(--text);
      font-size: 0.9rem;
      outline: none;
    }}

    [dir="rtl"] .search-input {{
      padding: 9px 36px 9px 14px;
    }}

    .search-icon {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
      font-size: 14px;
    }}

    [dir="rtl"] .search-icon {{
      right: 12px;
    }}

    [dir="ltr"] .search-icon {{
      left: 12px;
    }}

    /* Main Content Area */
    main {{
      flex: 1;
      max-width: 1440px;
      width: 100%;
      margin: 0 auto;
      padding: 16px 20px 40px;
      position: relative;
    }}

    .view-panel {{
      display: none;
    }}

    .view-panel.active {{
      display: block;
    }}

    /* =========================================================================
       TREE VIEW
       ========================================================================= */
    .tree-viewport-container {{
      position: relative;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      overflow: hidden;
      height: 78vh;
      display: flex;
      flex-direction: column;
    }}

    .tree-toolbar {{
      padding: 10px 16px;
      background: var(--bg-card-subtle);
      border-bottom: 1px solid var(--border);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      z-index: 10;
    }}

    .tree-canvas-wrapper {{
      flex: 1;
      overflow: auto;
      position: relative;
      cursor: grab;
      user-select: none;
      background: 
        radial-gradient(circle, var(--border) 1px, transparent 1px);
      background-size: 24px 24px;
    }}

    .tree-canvas-wrapper:active {{
      cursor: grabbing;
    }}

    .tree-canvas {{
      transform-origin: 0 0;
      padding: 60px;
      display: inline-block;
      min-width: 100%;
    }}

    /* CSS Hierarchical Family Tree Diagram */
    .ft-tree, .ft-tree ul {{
      margin: 0;
      padding: 0;
      list-style-type: none;
      display: flex;
      justify-content: center;
      position: relative;
    }}

    .ft-tree ul {{
      padding-top: 28px;
    }}

    .ft-tree li {{
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      padding: 0 8px;
    }}

    /* Connector lines */
    .ft-tree li::before, .ft-tree li::after {{
      content: '';
      position: absolute;
      top: 0;
      right: 50%;
      border-top: 2px solid var(--tree-line);
      width: 50%;
      height: 28px;
    }}

    .ft-tree li::after {{
      right: auto;
      left: 50%;
      border-left: 2px solid var(--tree-line);
    }}

    .ft-tree li:only-child::after, .ft-tree li:only-child::before {{
      display: none;
    }}

    .ft-tree li:only-child {{
      padding-top: 0;
    }}

    .ft-tree li:first-child::before, .ft-tree li:last-child::after {{
      border: 0 none;
    }}

    .ft-tree li:last-child::before {{
      border-right: 2px solid var(--tree-line);
      border-radius: 0 8px 0 0;
    }}

    .ft-tree li:first-child::after {{
      border-radius: 8px 0 0 0;
    }}

    .ft-tree ul::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 50%;
      border-left: 2px solid var(--tree-line);
      width: 0;
      height: 28px;
    }}

    /* Tree Node Card */
    .tree-node {{
      background: var(--node-bg);
      border: 2px solid var(--node-border);
      border-radius: 12px;
      padding: 8px 12px;
      min-width: 110px;
      text-align: center;
      position: relative;
      box-shadow: 0 2px 5px rgba(0,0,0,0.06);
      cursor: pointer;
      z-index: 2;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .tree-node:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-lg);
      border-color: var(--primary);
    }}

    .tree-node.highlighted {{
      border-color: var(--accent);
      box-shadow: 0 0 0 4px rgba(245, 158, 11, 0.4);
      animation: pulse 1.5s infinite;
    }}

    @keyframes pulse {{
      0% {{ transform: scale(1); }}
      50% {{ transform: scale(1.04); }}
      100% {{ transform: scale(1); }}
    }}

    .tree-node.level-0 {{
      background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
      color: white;
      border-color: #1e3a8a;
      padding: 12px 24px;
      font-size: 1.25rem;
      border-radius: 24px;
    }}

    .tree-node.level-1 {{
      background: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%);
      color: white;
      border-color: #0f766e;
      border-radius: 20px;
    }}

    .tree-node.level-2 {{
      background: linear-gradient(135deg, #c2410c 0%, #f97316 100%);
      color: white;
      border-color: #c2410c;
      border-radius: 18px;
    }}

    .tree-node.level-3 {{
      background: linear-gradient(135deg, #7e22ce 0%, #a855f7 100%);
      color: white;
      border-color: #7e22ce;
      border-radius: 16px;
    }}

    .tree-node.level-4 {{
      border-color: var(--primary);
      border-width: 2px;
      font-weight: 700;
    }}

    .node-name {{
      font-weight: 700;
      font-size: 0.95rem;
    }}

    .node-sub {{
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .tree-node.level-0 .node-sub,
    .tree-node.level-1 .node-sub,
    .tree-node.level-2 .node-sub,
    .tree-node.level-3 .node-sub {{
      color: rgba(255, 255, 255, 0.85);
    }}

    .node-badge {{
      display: inline-block;
      font-size: 0.65rem;
      padding: 1px 6px;
      border-radius: 10px;
      background: var(--bg-card-subtle);
      color: var(--text-muted);
      margin-top: 4px;
    }}

    .node-toggle {{
      position: absolute;
      bottom: -11px;
      left: 50%;
      transform: translateX(-50%);
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: var(--primary);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: bold;
      border: 2px solid var(--bg-card);
      cursor: pointer;
      box-shadow: 0 2px 4px rgba(0,0,0,0.15);
      z-index: 5;
    }}

    .node-toggle:hover {{
      background: var(--accent);
    }}

    .ft-tree li.collapsed > ul {{
      display: none;
    }}

    /* =========================================================================
       BRANCHES VIEW
       ========================================================================= */
    .branches-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 20px;
    }}

    .branch-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .branch-header {{
      padding: 14px 18px;
      background: var(--bg-card-subtle);
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .branch-title {{
      font-weight: 800;
      font-size: 1.1rem;
      color: var(--primary);
    }}

    .branch-count {{
      font-size: 0.78rem;
      padding: 2px 8px;
      border-radius: 12px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      font-weight: 700;
    }}

    .branch-body {{
      padding: 16px;
      flex: 1;
      max-height: 480px;
      overflow-y: auto;
    }}

    .branch-tree-list {{
      list-style: none;
      padding-inline-start: 14px;
      border-inline-start: 2px solid var(--border);
    }}

    .branch-tree-item {{
      margin-bottom: 8px;
      position: relative;
    }}

    .branch-tree-item::before {{
      content: '';
      position: absolute;
      top: 12px;
      right: -16px;
      width: 12px;
      height: 2px;
      background: var(--border);
    }}

    [dir="ltr"] .branch-tree-item::before {{
      right: auto;
      left: -16px;
    }}

    .branch-node-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      background: var(--bg-card);
      border: 1px solid var(--border);
      font-size: 0.86rem;
      font-weight: 600;
      cursor: pointer;
      text-align: start;
    }}

    .branch-node-btn:hover {{
      border-color: var(--primary);
      background: var(--bg-card-subtle);
    }}

    /* =========================================================================
       TABLE / DIRECTORY VIEW
       ========================================================================= */
    .table-container {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      overflow: hidden;
    }}

    .table-toolbar {{
      padding: 12px 18px;
      background: var(--bg-card-subtle);
      border-bottom: 1px solid var(--border);
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      justify-content: space-between;
      align-items: center;
    }}

    .filter-group {{
      display: flex;
      gap: 8px;
      align-items: center;
    }}

    select.form-select {{
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border);
      background: var(--bg-card);
      color: var(--text);
      font-size: 0.85rem;
      outline: none;
    }}

    .data-table-wrapper {{
      max-height: 65vh;
      overflow: auto;
    }}

    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: start;
      font-size: 0.88rem;
    }}

    table.data-table th {{
      position: sticky;
      top: 0;
      background: var(--bg-card-subtle);
      padding: 10px 14px;
      font-weight: 700;
      border-bottom: 2px solid var(--border);
      color: var(--text-muted);
      z-index: 5;
    }}

    table.data-table td {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border);
    }}

    table.data-table tr:hover td {{
      background: var(--bg-card-subtle);
    }}

    /* =========================================================================
       STATISTICS VIEW
       ========================================================================= */
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 20px;
    }}

    .stat-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--shadow);
    }}

    .stat-card h3 {{
      font-size: 1.05rem;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--primary);
    }}

    .freq-list {{
      list-style: none;
    }}

    .freq-item {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 0;
      border-bottom: 1px dashed var(--border);
      font-size: 0.9rem;
    }}

    .freq-bar-bg {{
      flex: 1;
      height: 8px;
      background: var(--bg-card-subtle);
      border-radius: 4px;
      margin: 0 12px;
      overflow: hidden;
    }}

    .freq-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--primary) 0%, var(--primary-light) 100%);
      border-radius: 4px;
    }}

    /* =========================================================================
       MODALS
       ========================================================================= */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(4px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .modal-backdrop.open {{
      display: flex;
    }}

    .modal-window {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      width: 100%;
      max-width: 540px;
      box-shadow: var(--shadow-lg);
      overflow: hidden;
      animation: modalFadeIn 0.25s ease;
    }}

    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.95); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .modal-header {{
      padding: 16px 20px;
      background: var(--bg-card-subtle);
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-header h3 {{
      font-size: 1.15rem;
      font-weight: 700;
    }}

    .modal-close {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 1.4rem;
      line-height: 1;
    }}

    .modal-body {{
      padding: 20px;
      max-height: 70vh;
      overflow-y: auto;
    }}

    .modal-footer {{
      padding: 12px 20px;
      background: var(--bg-card-subtle);
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: flex-end;
      gap: 10px;
    }}

    .form-group {{
      margin-bottom: 16px;
    }}

    .form-label {{
      display: block;
      margin-bottom: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
    }}

    .form-input, .form-textarea {{
      width: 100%;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border);
      background: var(--bg-card);
      color: var(--text);
      font-size: 0.9rem;
      outline: none;
    }}

    .form-input:focus, .form-textarea:focus {{
      border-color: var(--primary);
    }}

    .lineage-banner {{
      background: var(--bg-card-subtle);
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border-inline-start: 4px solid var(--primary);
      margin-bottom: 16px;
      font-size: 0.85rem;
    }}

    .tag-badge {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
      background: var(--bg-card-subtle);
      color: var(--text);
      border: 1px solid var(--border);
    }}

    /* Toast Notification */
    .toast {{
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
    }}

    [dir="rtl"] .toast {{
      right: auto;
      left: 24px;
    }}

    .toast.show {{
      display: flex;
      animation: toastIn 0.3s ease;
    }}

    @keyframes toastIn {{
      from {{ transform: translateY(20px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    /* Footer */
    footer {{
      margin-top: auto;
      background: var(--bg-card);
      border-top: 1px solid var(--border);
      padding: 16px 20px;
      text-align: center;
      font-size: 0.82rem;
      color: var(--text-muted);
    }}
  </style>
</head>
<body data-theme="light" class="lang-ar">

  <!-- Header -->
  <header>
    <div class="header-container">
      <div class="brand">
        <div class="brand-logo">ن</div>
        <div class="brand-titles">
          <h1 id="app-title">شجرة عائلة آل ندى</h1>
          <p id="app-subtitle">توثيق شامل ومفصل لفروع ونسب العائلة الكريمة</p>
        </div>
      </div>

      <div class="header-actions">
        <!-- New Member -->
        <button class="btn btn-primary" onclick="openAddMemberModal()" title="إضافة فرد جديد">
          <span>➕</span>
          <span class="t-add-member">إضافة فرد</span>
        </button>

        <!-- Export JSON -->
        <button class="btn" onclick="exportData()" title="تصدير شجرة العائلة">
          <span>💾</span>
          <span class="t-export">تصدير</span>
        </button>

        <!-- Import JSON -->
        <label class="btn" style="margin: 0; cursor: pointer;" title="استيراد ملف JSON">
          <span>📥</span>
          <span class="t-import">استيراد</span>
          <input type="file" id="import-file" accept=".json" style="display: none;" onchange="importData(event)">
        </label>

        <!-- Reset Button -->
        <button class="btn" onclick="resetData()" title="استعادة الشجرة الأصلية">
          <span>🔄</span>
          <span class="t-reset">إعادة ضبط</span>
        </button>

        <!-- Theme Toggle -->
        <button class="btn btn-icon" onclick="toggleTheme()" id="theme-btn" title="تغيير المظهر (فاتح / داكن)">
          <span id="theme-icon">🌙</span>
        </button>

        <!-- Language Toggle -->
        <button class="btn btn-accent" onclick="toggleLanguage()" id="lang-btn" title="Switch Language / تغيير اللغة">
          🌐 <span>English</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Quick Stats Bar -->
  <div class="stats-bar">
    <div class="stats-container">
      <div class="stat-items">
        <div class="stat-item">
          <span class="t-stat-total">إجمالي الأفراد:</span>
          <span class="stat-badge" id="stat-total-count">448</span>
        </div>
        <div class="stat-item">
          <span class="t-stat-gens">أقصى عمق للأجيال:</span>
          <span class="stat-badge" id="stat-max-gen">10</span>
        </div>
        <div class="stat-item">
          <span class="t-stat-branches">الفروع الرئيسية:</span>
          <span class="stat-badge">7</span>
        </div>
        <div class="stat-item">
          <span class="t-stat-ancestor">الجد الجامع:</span>
          <strong id="stat-ancestor-name">مصطفى بن حمد آل ندى</strong>
        </div>
      </div>
      <div style="font-size: 0.8rem; color: var(--text-muted);">
        <span class="t-stat-source">مستخرجة ومطابقة 100% من الوثيقة المرفقة</span>
      </div>
    </div>
  </div>

  <!-- Navigation Tabs & Search -->
  <div class="nav-search-bar">
    <div class="tabs">
      <button class="tab-btn active" onclick="switchTab('tree')">
        <span>🌳</span>
        <span class="t-tab-tree">الشجرة الهيكلية</span>
      </button>
      <button class="tab-btn" onclick="switchTab('branches')">
        <span>🗂️</span>
        <span class="t-tab-branches">مستكشف الفروع</span>
      </button>
      <button class="tab-btn" onclick="switchTab('table')">
        <span>📋</span>
        <span class="t-tab-table">دليل الأسماء والبحث</span>
      </button>
      <button class="tab-btn" onclick="switchTab('stats')">
        <span>📊</span>
        <span class="t-tab-stats">الإحصائيات والتحليل</span>
      </button>
    </div>

    <div class="search-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="main-search" class="search-input" placeholder="ابحث عن اسم، جيل، أو فرع..." oninput="handleSearch(this.value)">
    </div>
  </div>

  <!-- Main Views -->
  <main>
    <!-- VIEW 1: INTERACTIVE HIERARCHICAL TREE -->
    <div id="view-tree" class="view-panel active">
      <div class="tree-viewport-container">
        <div class="tree-toolbar">
          <div style="display: flex; gap: 8px; align-items: center;">
            <button class="btn btn-sm" onclick="zoomTree(0.15)">➕ <span class="t-zoom-in">تكبير</span></button>
            <button class="btn btn-sm" onclick="zoomTree(-0.15)">➖ <span class="t-zoom-out">تصغير</span></button>
            <button class="btn btn-sm" onclick="resetZoom()">🎯 <span class="t-zoom-fit">إعادة ضبط</span></button>
            <span style="font-size: 0.8rem; color: var(--text-muted); margin-inline-start: 8px;" id="zoom-level-text">100%</span>
          </div>
          <div style="display: flex; gap: 8px; align-items: center;">
            <button class="btn btn-sm" onclick="expandAllNodes()">📂 <span class="t-expand-all">بسط الكل</span></button>
            <button class="btn btn-sm" onclick="collapseToGen(4)">📁 <span class="t-collapse-branches">طي للأجداد</span></button>
          </div>
        </div>

        <div class="tree-canvas-wrapper" id="canvas-wrapper">
          <div class="tree-canvas" id="tree-canvas">
            <!-- Tree HTML injected by JavaScript -->
          </div>
        </div>
      </div>
    </div>

    <!-- VIEW 2: BRANCHES EXPLORER -->
    <div id="view-branches" class="view-panel">
      <div class="branches-grid" id="branches-grid">
        <!-- Branch Cards injected here -->
      </div>
    </div>

    <!-- VIEW 3: SEARCHABLE DIRECTORY / TABLE -->
    <div id="view-table" class="view-panel">
      <div class="table-container">
        <div class="table-toolbar">
          <div class="filter-group">
            <label class="form-label" style="margin: 0;" class="t-filter-branch">الفرع:</label>
            <select class="form-select" id="table-branch-filter" onchange="filterTable()">
              <option value="ALL">جميع الفروع (All Branches)</option>
            </select>
          </div>
          <div class="filter-group">
            <label class="form-label" style="margin: 0;" class="t-filter-gen">الجيل:</label>
            <select class="form-select" id="table-gen-filter" onchange="filterTable()">
              <option value="ALL">جميع الأجيال (All Generations)</option>
            </select>
          </div>
          <div style="font-size: 0.85rem; color: var(--text-muted);">
            <span class="t-showing-rows">المعروض:</span> <strong id="table-count-badge">0</strong>
          </div>
        </div>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>#</th>
                <th class="t-th-name">الاسم الكامل والنسب</th>
                <th class="t-th-branch">الفرع الرئيسي</th>
                <th class="t-th-father">الأب</th>
                <th class="t-th-gen">الجيل</th>
                <th class="t-th-children">الأبناء</th>
                <th class="t-th-notes">ملاحظات</th>
                <th class="t-th-actions">إجراءات</th>
              </tr>
            </thead>
            <tbody id="table-tbody">
              <!-- Rows injected here -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- VIEW 4: STATISTICS & ANALYSIS -->
    <div id="view-stats" class="view-panel">
      <div class="stats-grid">
        <div class="stat-card">
          <h3 class="t-stat-h-names">📊 الأسماء الأكثر تكراراً في العائلة</h3>
          <ul class="freq-list" id="stats-freq-names"></ul>
        </div>
        <div class="stat-card">
          <h3 class="t-stat-h-gens">📈 التوزيع العددي للأجيال</h3>
          <ul class="freq-list" id="stats-freq-gens"></ul>
        </div>
        <div class="stat-card">
          <h3 class="t-stat-h-branches">🌳 توزيع أفراد العائلة حسب الفروع</h3>
          <ul class="freq-list" id="stats-freq-branches"></ul>
        </div>
        <div class="stat-card">
          <h3 class="t-stat-h-notes">📜 الملاحظات والوفيات الموثقة بالرسمة</h3>
          <div style="font-size: 0.88rem; line-height: 1.8;">
            <p><strong>1. مسلم بن زكي:</strong> مسجل في الرسمة: "وفاة 19/2/2016 الجمعة"</p>
            <p><strong>2. فهمي بن زكي:</strong> مسجل في الرسمة: "وفاة 5/1/1982"</p>
            <p><strong>3. ماجد بن ايهاب بن ماجد بن حسين بن شاكر:</strong> مسجل معه قيد بالخط: "رامي الحمد الله"</p>
          </div>
        </div>
      </div>
    </div>
  </main>

  <!-- MEMBER INSPECT / EDIT MODAL -->
  <div class="modal-backdrop" id="member-modal">
    <div class="modal-window">
      <div class="modal-header">
        <h3 id="modal-title">بطاقة الفرد</h3>
        <button class="modal-close" onclick="closeModal('member-modal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="lineage-banner" id="modal-lineage"></div>

        <input type="hidden" id="edit-id">
        <div class="form-group">
          <label class="form-label t-lbl-name-ar">الاسم (بالعربية):</label>
          <input type="text" id="edit-name-ar" class="form-input">
        </div>

        <div class="form-group">
          <label class="form-label t-lbl-name-en">Name (in English):</label>
          <input type="text" id="edit-name-en" class="form-input">
        </div>

        <div class="form-group">
          <label class="form-label t-lbl-parent">الأب / الأصل:</label>
          <select id="edit-parent-id" class="form-select form-input"></select>
        </div>

        <div class="form-group">
          <label class="form-label t-lbl-notes">ملاحظات / تاريخ ميلاد أو وفاة:</label>
          <input type="text" id="edit-notes" class="form-input">
        </div>

        <div style="display: flex; gap: 8px; margin-top: 10px;">
          <button class="btn btn-primary" onclick="openAddChildFromModal()">
            <span>➕</span> <span class="t-btn-add-son">إضافة ابن لهذا الشخص</span>
          </button>
          <button class="btn" style="color: #ef4444; border-color: #ef4444;" onclick="deleteCurrentMember()">
            <span>🗑️</span> <span class="t-btn-delete">حذف</span>
          </button>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn" onclick="closeModal('member-modal')" class="t-btn-cancel">إلغاء</button>
        <button class="btn btn-primary" onclick="saveMemberEdit()" class="t-btn-save">حفظ التعديلات</button>
      </div>
    </div>
  </div>

  <!-- ADD NEW MEMBER MODAL -->
  <div class="modal-backdrop" id="add-modal">
    <div class="modal-window">
      <div class="modal-header">
        <h3 class="t-modal-add-title">إضافة فرد جديد إلى شجرة العائلة</h3>
        <button class="modal-close" onclick="closeModal('add-modal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label t-lbl-name-ar">اسم الفرد (بالعربية):</label>
          <input type="text" id="add-name-ar" class="form-input" placeholder="مثال: يوسف">
        </div>

        <div class="form-group">
          <label class="form-label t-lbl-name-en">Name (English):</label>
          <input type="text" id="add-name-en" class="form-input" placeholder="e.g. Youssef">
        </div>

        <div class="form-group">
          <label class="form-label t-lbl-father-sel">اختر الأب:</label>
          <select id="add-parent-id" class="form-select form-input"></select>
        </div>

        <div class="form-group">
          <label class="form-label t-lbl-notes">ملاحظات إضافية:</label>
          <input type="text" id="add-notes" class="form-input" placeholder="سنة الميلاد، إقامة، إلخ...">
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn" onclick="closeModal('add-modal')">إلغاء</button>
        <button class="btn btn-primary" onclick="confirmAddMember()">إضافة</button>
      </div>
    </div>
  </div>

  <!-- Toast -->
  <div class="toast" id="toast">
    <span id="toast-icon">✅</span>
    <span id="toast-msg">تمت العملية بنجاح</span>
  </div>

  <!-- Footer -->
  <footer>
    <p>شجرة عائلة آل ندى © 2026 | نظام توثيق وتعديل شجرة الأنساب التفاعلي | مستخرج بدقة كاملة من وثيقة شجرة عائلة آل ندى</p>
  </footer>

  <!-- SCRIPT -->
  <script>
    // Embedded Master Dataset
    const ORIGINAL_TREE_DATA = {tree_json_str};
    const ORIGINAL_FLAT_DATA = {flat_json_str};

    // State
    let currentLanguage = 'ar';
    let currentTheme = 'light';
    let zoomScale = 1.0;
    let treeData = null;
    let flatMembers = [];
    let collapsedNodes = new Set();

    // LocalStorage Keys
    const LS_DATA_KEY = 'al_nada_family_tree_v1';
    const LS_THEME_KEY = 'al_nada_theme_mode';
    const LS_LANG_KEY = 'al_nada_lang_mode';

    // Translations Dictionary
    const I18N = {{
      ar: {{
        appTitle: "شجرة عائلة آل ندى",
        appSubtitle: "توثيق شامل ومفصل لفروع ونسب العائلة الكريمة",
        addMember: "إضافة فرد",
        export: "تصدير",
        import: "استيراد",
        reset: "إعادة ضبط",
        statTotal: "إجمالي الأفراد:",
        statGens: "أقصى عمق للأجيال:",
        statBranches: "الفروع الرئيسية:",
        statAncestor: "الجد الجامع:",
        tabTree: "الشجرة الهيكلية",
        tabBranches: "مستكشف الفروع",
        tabTable: "دليل الأسماء والبحث",
        tabStats: "الإحصائيات والتحليل",
        zoomIn: "تكبير",
        zoomOut: "تصغير",
        zoomFit: "إعادة ضبط",
        expandAll: "بسط الكل",
        collapseBranches: "طي للأجداد",
        filterBranch: "الفرع:",
        filterGen: "الجيل:",
        showingRows: "المعروض:",
        thName: "الاسم الكامل والنسب",
        thBranch: "الفرع الرئيسي",
        thFather: "الأب",
        thGen: "الجيل",
        thChildren: "الأبناء",
        thNotes: "ملاحظات",
        thActions: "إجراءات",
        statHNames: "📊 الأسماء الأكثر تكراراً في العائلة",
        statHGens: "📈 التوزيع العددي للأجيال",
        statHBranches: "🌳 توزيع أفراد العائلة حسب الفروع",
        statHNotes: "📜 الملاحظات والوفيات الموثقة بالرسمة",
        modalCardTitle: "بطاقة الفرد",
        modalAddTitle: "إضافة فرد جديد إلى شجرة العائلة",
        lblNameAr: "الاسم (بالعربية):",
        lblNameEn: "Name (in English):",
        lblParent: "الأب / الأصل:",
        lblNotes: "ملاحظات / تاريخ ميلاد أو وفاة:",
        btnAddSon: "إضافة ابن لهذا الشخص",
        btnDelete: "حذف",
        btnCancel: "إلغاء",
        btnSave: "حفظ التعديلات",
        searchPlaceholder: "ابحث عن اسم، جيل، أو فرع...",
        deleteConfirm: "هل أنت متأكد من رغبتك في حذف هذا الفرد؟ إذا كان لديه أبناء فسيتم حذفهم أيضاً.",
        resetConfirm: "هل أنت متأكد من إعادة ضبط الشجرة للبيانات الأصلية من ملف PDF؟ ستفقد التعديلات المحلية غير المصدرة."
      }},
      en: {{
        appTitle: "Al-Nada Family Tree",
        appSubtitle: "Comprehensive and Detailed Documentation of the Family Lineage",
        addMember: "Add Member",
        export: "Export",
        import: "Import",
        reset: "Reset Data",
        statTotal: "Total Members:",
        statGens: "Max Generations:",
        statBranches: "Main Branches:",
        statAncestor: "Common Ancestor:",
        tabTree: "Interactive Tree",
        tabBranches: "Branches Explorer",
        tabTable: "Directory & Search",
        tabStats: "Statistics & Insights",
        zoomIn: "Zoom In",
        zoomOut: "Zoom Out",
        zoomFit: "Reset Zoom",
        expandAll: "Expand All",
        collapseBranches: "Collapse to Ancestors",
        filterBranch: "Branch:",
        filterGen: "Generation:",
        showingRows: "Showing:",
        thName: "Full Name & Lineage",
        thBranch: "Main Branch",
        thFather: "Father",
        thGen: "Gen",
        thChildren: "Children",
        thNotes: "Notes",
        thActions: "Actions",
        statHNames: "📊 Most Common Names",
        statHGens: "📈 Generation Distribution",
        statHBranches: "🌳 Branch Distribution",
        statHNotes: "📜 Documented Records & Dates",
        modalCardTitle: "Member Details",
        modalAddTitle: "Add New Member to Family Tree",
        lblNameAr: "Name (Arabic):",
        lblNameEn: "Name (English):",
        lblParent: "Father / Parent:",
        lblNotes: "Notes / Birth or Death:",
        btnAddSon: "Add Child to this Person",
        btnDelete: "Delete",
        btnCancel: "Cancel",
        btnSave: "Save Changes",
        searchPlaceholder: "Search by name, generation, or branch...",
        deleteConfirm: "Are you sure you want to delete this member? All their descendants will also be removed.",
        resetConfirm: "Are you sure you want to reset all data back to the original tree? Any unsaved edits will be lost."
      }}
    }};

    // Initialization
    window.addEventListener('DOMContentLoaded', () => {{
      loadSavedState();
      initTheme();
      initLanguage();
      renderAllViews();
      initPanZoom();
    }});

    // Load Data
    function loadSavedState() {{
      const savedData = localStorage.getItem(LS_DATA_KEY);
      if (savedData) {{
        try {{
          treeData = JSON.parse(savedData);
          rebuildFlatList();
        }} catch(e) {{
          console.error("Failed to load local storage data:", e);
          treeData = JSON.parse(JSON.stringify(ORIGINAL_TREE_DATA));
          rebuildFlatList();
        }}
      }} else {{
        treeData = JSON.parse(JSON.stringify(ORIGINAL_TREE_DATA));
        rebuildFlatList();
      }}
    }}

    function saveState() {{
      localStorage.setItem(LS_DATA_KEY, JSON.stringify(treeData));
      rebuildFlatList();
      renderAllViews();
    }}

    function rebuildFlatList() {{
      flatMembers = [];
      function traverse(node, parent = null, branchAr = 'الأصل', branchEn = 'Root') {{
        if (node.branch_ar) branchAr = node.branch_ar;
        if (node.branch_en) branchEn = node.branch_en;
        
        node.parent_id = parent ? parent.id : null;
        node.parent_name_ar = parent ? parent.name_ar : null;
        node.parent_name_en = parent ? parent.name_en : null;
        node.branch_ar = branchAr;
        node.branch_en = branchEn;

        if (parent && parent.lineage_ar) {{
          node.lineage_ar = `${{node.name_ar}} بن ${{parent.lineage_ar}}`;
          node.lineage_en = `${{node.name_en}} bin ${{parent.lineage_en}}`;
        }} else if (parent) {{
          node.lineage_ar = `${{node.name_ar}} بن ${{parent.name_ar}}`;
          node.lineage_en = `${{node.name_en}} bin ${{parent.name_en}}`;
        }} else {{
          node.lineage_ar = node.name_ar;
          node.lineage_en = node.name_en;
        }}

        flatMembers.push({{
          id: node.id,
          name_ar: node.name_ar,
          name_en: node.name_en,
          parent_id: node.parent_id,
          parent_name_ar: node.parent_name_ar,
          parent_name_en: node.parent_name_en,
          generation: node.generation,
          branch_ar: node.branch_ar,
          branch_en: node.branch_en,
          lineage_ar: node.lineage_ar,
          lineage_en: node.lineage_en,
          notes: node.notes || '',
          children_count: (node.children || []).length
        }});

        if (node.children) {{
          node.children.forEach(c => traverse(c, node, branchAr, branchEn));
        }}
      }}
      traverse(treeData);
      updateTopStats();
    }}

    function updateTopStats() {{
      document.getElementById('stat-total-count').textContent = flatMembers.length;
      const maxGen = Math.max(...flatMembers.map(m => m.generation));
      document.getElementById('stat-max-gen').textContent = maxGen;
    }}

    // Theme Management
    function initTheme() {{
      const savedTheme = localStorage.getItem(LS_THEME_KEY) || 'light';
      setTheme(savedTheme);
    }}

    function toggleTheme() {{
      const nextTheme = currentTheme === 'light' ? 'dark' : 'light';
      setTheme(nextTheme);
    }}

    function setTheme(theme) {{
      currentTheme = theme;
      document.body.setAttribute('data-theme', theme);
      document.getElementById('theme-icon').textContent = theme === 'dark' ? '☀️' : '🌙';
      localStorage.setItem(LS_THEME_KEY, theme);
    }}

    // Language Management
    function initLanguage() {{
      const savedLang = localStorage.getItem(LS_LANG_KEY) || 'ar';
      setLanguage(savedLang);
    }}

    function toggleLanguage() {{
      const nextLang = currentLanguage === 'ar' ? 'en' : 'ar';
      setLanguage(nextLang);
    }}

    function setLanguage(lang) {{
      currentLanguage = lang;
      localStorage.setItem(LS_LANG_KEY, lang);
      document.documentElement.lang = lang;
      document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
      document.body.className = `lang-${{lang}}`;
      document.getElementById('lang-btn').innerHTML = lang === 'ar' ? '🌐 <span>English</span>' : '🌐 <span>عربي</span>';
      
      applyTranslations();
      renderAllViews();
    }}

    function applyTranslations() {{
      const t = I18N[currentLanguage];
      document.getElementById('app-title').textContent = t.appTitle;
      document.getElementById('app-subtitle').textContent = t.appSubtitle;
      document.querySelectorAll('.t-add-member').forEach(el => el.textContent = t.addMember);
      document.querySelectorAll('.t-export').forEach(el => el.textContent = t.export);
      document.querySelectorAll('.t-import').forEach(el => el.textContent = t.import);
      document.querySelectorAll('.t-reset').forEach(el => el.textContent = t.reset);
      document.querySelectorAll('.t-stat-total').forEach(el => el.textContent = t.statTotal);
      document.querySelectorAll('.t-stat-gens').forEach(el => el.textContent = t.statGens);
      document.querySelectorAll('.t-stat-branches').forEach(el => el.textContent = t.statBranches);
      document.querySelectorAll('.t-stat-ancestor').forEach(el => el.textContent = t.statAncestor);
      document.querySelectorAll('.t-tab-tree').forEach(el => el.textContent = t.tabTree);
      document.querySelectorAll('.t-tab-branches').forEach(el => el.textContent = t.tabBranches);
      document.querySelectorAll('.t-tab-table').forEach(el => el.textContent = t.tabTable);
      document.querySelectorAll('.t-tab-stats').forEach(el => el.textContent = t.tabStats);
      document.querySelectorAll('.t-zoom-in').forEach(el => el.textContent = t.zoomIn);
      document.querySelectorAll('.t-zoom-out').forEach(el => el.textContent = t.zoomOut);
      document.querySelectorAll('.t-zoom-fit').forEach(el => el.textContent = t.zoomFit);
      document.querySelectorAll('.t-expand-all').forEach(el => el.textContent = t.expandAll);
      document.querySelectorAll('.t-collapse-branches').forEach(el => el.textContent = t.collapseBranches);
      document.querySelectorAll('.t-filter-branch').forEach(el => el.textContent = t.filterBranch);
      document.querySelectorAll('.t-filter-gen').forEach(el => el.textContent = t.filterGen);
      document.querySelectorAll('.t-showing-rows').forEach(el => el.textContent = t.showingRows);
      document.querySelectorAll('.t-th-name').forEach(el => el.textContent = t.thName);
      document.querySelectorAll('.t-th-branch').forEach(el => el.textContent = t.thBranch);
      document.querySelectorAll('.t-th-father').forEach(el => el.textContent = t.thFather);
      document.querySelectorAll('.t-th-gen').forEach(el => el.textContent = t.thGen);
      document.querySelectorAll('.t-th-children').forEach(el => el.textContent = t.thChildren);
      document.querySelectorAll('.t-th-notes').forEach(el => el.textContent = t.thNotes);
      document.querySelectorAll('.t-th-actions').forEach(el => el.textContent = t.thActions);
      document.querySelectorAll('.t-stat-h-names').forEach(el => el.textContent = t.statHNames);
      document.querySelectorAll('.t-stat-h-gens').forEach(el => el.textContent = t.statHGens);
      document.querySelectorAll('.t-stat-h-branches').forEach(el => el.textContent = t.statHBranches);
      document.querySelectorAll('.t-stat-h-notes').forEach(el => el.textContent = t.statHNotes);
      document.querySelectorAll('.t-modal-add-title').forEach(el => el.textContent = t.modalAddTitle);
      document.querySelectorAll('.t-lbl-name-ar').forEach(el => el.textContent = t.lblNameAr);
      document.querySelectorAll('.t-lbl-name-en').forEach(el => el.textContent = t.lblNameEn);
      document.querySelectorAll('.t-lbl-parent').forEach(el => el.textContent = t.lblParent);
      document.querySelectorAll('.t-lbl-notes').forEach(el => el.textContent = t.lblNotes);
      document.querySelectorAll('.t-btn-add-son').forEach(el => el.textContent = t.btnAddSon);
      document.querySelectorAll('.t-btn-delete').forEach(el => el.textContent = t.btnDelete);
      document.querySelectorAll('.t-btn-cancel').forEach(el => el.textContent = t.btnCancel);
      document.querySelectorAll('.t-btn-save').forEach(el => el.textContent = t.btnSave);
      
      const searchBox = document.getElementById('main-search');
      if (searchBox) searchBox.placeholder = t.searchPlaceholder;
    }}

    // Render Views
    function renderAllViews() {{
      renderTreeView();
      renderBranchesView();
      renderTableView();
      renderStatsView();
      populateParentSelects();
    }}

    // VIEW 1: Tree View
    function renderTreeView() {{
      const container = document.getElementById('tree-canvas');
      if (!container) return;

      function renderNode(node) {{
        const hasChildren = node.children && node.children.length > 0;
        const isCollapsed = collapsedNodes.has(node.id);
        const name = currentLanguage === 'ar' ? node.name_ar : node.name_en;
        const subName = currentLanguage === 'ar' ? node.name_en : node.name_ar;
        const genLabel = currentLanguage === 'ar' ? `الجيل ${{node.generation}}` : `Gen ${{node.generation}}`;

        let html = `<li id="li-${{node.id}}" class="${{isCollapsed ? 'collapsed' : ''}}">`;
        html += `
          <div class="tree-node level-${{node.generation}}" id="node-${{node.id}}" onclick="inspectMember('${{node.id}}')">
            <div class="node-name">${{name}}</div>
            <div class="node-sub">${{subName}}</div>
            <span class="node-badge">${{genLabel}}</span>
            ${{node.notes ? `<div style="font-size: 0.65rem; color: #f59e0b; margin-top:2px;">📌 ${{node.notes}}</div>` : ''}}
            ${{hasChildren ? `
              <div class="node-toggle" onclick="event.stopPropagation(); toggleNodeCollapse('${{node.id}}')">
                ${{isCollapsed ? '+' : '-'}}
              </div>
            ` : ''}}
          </div>
        `;

        if (hasChildren) {{
          html += '<ul>';
          node.children.forEach(child => {{
            html += renderNode(child);
          }});
          html += '</ul>';
        }}

        html += '</li>';
        return html;
      }}

      container.innerHTML = `<ul class="ft-tree">${{renderNode(treeData)}}</ul>`;
    }}

    function toggleNodeCollapse(nodeId) {{
      if (collapsedNodes.has(nodeId)) {{
        collapsedNodes.delete(nodeId);
      }} else {{
        collapsedNodes.add(nodeId);
      }}
      renderTreeView();
    }}

    function expandAllNodes() {{
      collapsedNodes.clear();
      renderTreeView();
    }}

    function collapseToGen(genLimit) {{
      collapsedNodes.clear();
      flatMembers.forEach(m => {{
        if (m.generation >= genLimit && m.children_count > 0) {{
          collapsedNodes.add(m.id);
        }}
      }});
      renderTreeView();
    }}

    // Zoom & Pan
    function zoomTree(delta) {{
      zoomScale = Math.max(0.25, Math.min(2.5, zoomScale + delta));
      updateCanvasTransform();
    }}

    function resetZoom() {{
      zoomScale = 1.0;
      updateCanvasTransform();
      const wrapper = document.getElementById('canvas-wrapper');
      wrapper.scrollLeft = (wrapper.scrollWidth - wrapper.clientWidth) / 2;
    }}

    function updateCanvasTransform() {{
      const canvas = document.getElementById('tree-canvas');
      canvas.style.transform = `scale(${{zoomScale}})`;
      document.getElementById('zoom-level-text').textContent = `${{Math.round(zoomScale * 100)}}%`;
    }}

    function initPanZoom() {{
      const wrapper = document.getElementById('canvas-wrapper');
      let isDown = false;
      let startX, startY, scrollLeft, scrollTop;

      wrapper.addEventListener('mousedown', (e) => {{
        if (e.target.closest('.tree-node') || e.target.closest('.node-toggle')) return;
        isDown = true;
        startX = e.pageX - wrapper.offsetLeft;
        startY = e.pageY - wrapper.offsetTop;
        scrollLeft = wrapper.scrollLeft;
        scrollTop = wrapper.scrollTop;
      }});

      wrapper.addEventListener('mouseleave', () => isDown = false);
      wrapper.addEventListener('mouseup', () => isDown = false);

      wrapper.addEventListener('mousemove', (e) => {{
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - wrapper.offsetLeft;
        const y = e.pageY - wrapper.offsetTop;
        const walkX = (x - startX) * 1.4;
        const walkY = (y - startY) * 1.4;
        wrapper.scrollLeft = scrollLeft - walkX;
        wrapper.scrollTop = scrollTop - walkY;
      }});

      // Mouse Wheel Zoom with Ctrl
      wrapper.addEventListener('wheel', (e) => {{
        if (e.ctrlKey) {{
          e.preventDefault();
          zoomTree(e.deltaY < 0 ? 0.1 : -0.1);
        }}
      }});
    }}

    // VIEW 2: Branches Explorer
    function renderBranchesView() {{
      const container = document.getElementById('branches-grid');
      if (!container) return;

      // Extract main branches at generation 3 or 4
      const mainBranches = [];
      function findBranches(node) {{
        if (node.generation === 4 || (node.generation === 3 && node.children.length > 0)) {{
          mainBranches.push(node);
        }} else if (node.children) {{
          node.children.forEach(findBranches);
        }}
      }}
      findBranches(treeData);

      let html = '';
      mainBranches.forEach(branch => {{
        const bName = currentLanguage === 'ar' ? branch.name_ar : branch.name_en;
        const bDesc = currentLanguage === 'ar' ? (branch.branch_ar || branch.name_ar) : (branch.branch_en || branch.name_en);
        
        let subCount = 0;
        function countSub(n) {{
          subCount++;
          if (n.children) n.children.forEach(countSub);
        }}
        countSub(branch);

        function renderSubTree(n) {{
          let itemHtml = `<li class="branch-tree-item">`;
          const nodeName = currentLanguage === 'ar' ? n.name_ar : n.name_en;
          itemHtml += `
            <button class="branch-node-btn" onclick="inspectMember('${{n.id}}')">
              <span>👤</span>
              <strong>${{nodeName}}</strong>
              ${{n.children && n.children.length ? `<span class="tag-badge">${{n.children.length}} أبناء</span>` : ''}}
            </button>
          `;
          if (n.children && n.children.length > 0) {{
            itemHtml += '<ul class="branch-tree-list">';
            n.children.forEach(c => itemHtml += renderSubTree(c));
            itemHtml += '</ul>';
          }}
          itemHtml += '</li>';
          return itemHtml;
        }}

        html += `
          <div class="branch-card">
            <div class="branch-header">
              <div>
                <div class="branch-title">${{bName}}</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">${{bDesc}}</div>
              </div>
              <span class="branch-count">${{subCount}} فرد</span>
            </div>
            <div class="branch-body">
              <ul class="branch-tree-list" style="border: none; padding: 0;">
                ${{renderSubTree(branch)}}
              </ul>
            </div>
          </div>
        `;
      }});

      container.innerHTML = html;
    }}

    // VIEW 3: Searchable Table / Directory
    function renderTableView() {{
      const tbody = document.getElementById('table-tbody');
      const branchSelect = document.getElementById('table-branch-filter');
      const genSelect = document.getElementById('table-gen-filter');
      if (!tbody) return;

      // Populate filters once
      const uniqueBranches = Array.from(new Set(flatMembers.map(m => currentLanguage === 'ar' ? m.branch_ar : m.branch_en)));
      const uniqueGens = Array.from(new Set(flatMembers.map(m => m.generation))).sort((a,b)=>a-b);

      branchSelect.innerHTML = `<option value="ALL">${{currentLanguage === 'ar' ? 'جميع الفروع' : 'All Branches'}}</option>` +
        uniqueBranches.map(b => `<option value="${{b}}">${{b}}</option>`).join('');

      genSelect.innerHTML = `<option value="ALL">${{currentLanguage === 'ar' ? 'جميع الأجيال' : 'All Generations'}}</option>` +
        uniqueGens.map(g => `<option value="${{g}}">${{currentLanguage === 'ar' ? `الجيل ${{g}}` : `Gen ${{g}}`}}</option>`).join('');

      filterTable();
    }}

    function filterTable() {{
      const tbody = document.getElementById('table-tbody');
      const branchVal = document.getElementById('table-branch-filter').value;
      const genVal = document.getElementById('table-gen-filter').value;
      const searchVal = document.getElementById('main-search').value.trim().toLowerCase();

      let filtered = flatMembers.filter(m => {{
        const b = currentLanguage === 'ar' ? m.branch_ar : m.branch_en;
        const matchesBranch = branchVal === 'ALL' || b === branchVal;
        const matchesGen = genVal === 'ALL' || m.generation.toString() === genVal;
        
        let matchesSearch = true;
        if (searchVal) {{
          const nameAr = m.name_ar.toLowerCase();
          const nameEn = m.name_en.toLowerCase();
          const lineageAr = (m.lineage_ar || '').toLowerCase();
          const lineageEn = (m.lineage_en || '').toLowerCase();
          matchesSearch = nameAr.includes(searchVal) || nameEn.includes(searchVal) || lineageAr.includes(searchVal) || lineageEn.includes(searchVal);
        }}
        return matchesBranch && matchesGen && matchesSearch;
      }});

      document.getElementById('table-count-badge').textContent = filtered.length;

      let html = '';
      filtered.forEach((m, idx) => {{
        const name = currentLanguage === 'ar' ? m.name_ar : m.name_en;
        const lineage = currentLanguage === 'ar' ? m.lineage_ar : m.lineage_en;
        const branch = currentLanguage === 'ar' ? m.branch_ar : m.branch_en;
        const father = currentLanguage === 'ar' ? (m.parent_name_ar || '-') : (m.parent_name_en || '-');

        html += `
          <tr>
            <td>${{idx + 1}}</td>
            <td>
              <strong>${{name}}</strong>
              <div style="font-size: 0.78rem; color: var(--text-muted);">${{lineage}}</div>
            </td>
            <td><span class="tag-badge">${{branch}}</span></td>
            <td>${{father}}</td>
            <td><span class="tag-badge">${{m.generation}}</span></td>
            <td>${{m.children_count}}</td>
            <td>${{m.notes || '-'}}</td>
            <td>
              <button class="btn btn-sm" onclick="inspectMember('${{m.id}}')">✏️ تعديل</button>
            </td>
          </tr>
        `;
      }});

      tbody.innerHTML = html;
    }}

    // VIEW 4: Statistics & Insights
    function renderStatsView() {{
      const nameFreqEl = document.getElementById('stats-freq-names');
      const genFreqEl = document.getElementById('stats-freq-gens');
      const branchFreqEl = document.getElementById('stats-freq-branches');
      if (!nameFreqEl) return;

      // Frequency of names
      const nameCounts = {{}};
      flatMembers.forEach(m => {{
        const key = currentLanguage === 'ar' ? m.name_ar : m.name_en;
        nameCounts[key] = (nameCounts[key] || 0) + 1;
      }});
      const sortedNames = Object.entries(nameCounts).sort((a,b) => b[1] - a[1]).slice(0, 10);
      const maxNameCount = sortedNames[0] ? sortedNames[0][1] : 1;

      nameFreqEl.innerHTML = sortedNames.map(([name, count]) => `
        <li class="freq-item">
          <span style="font-weight: 700; min-width: 90px;">${{name}}</span>
          <div class="freq-bar-bg">
            <div class="freq-bar-fill" style="width: ${{(count / maxNameCount) * 100}}%;"></div>
          </div>
          <span style="font-weight: 700; color: var(--primary);">${{count}} مرة</span>
        </li>
      `).join('');

      // Frequency of generations
      const genCounts = {{}};
      flatMembers.forEach(m => {{
        genCounts[m.generation] = (genCounts[m.generation] || 0) + 1;
      }});
      const sortedGens = Object.entries(genCounts).sort((a,b) => parseInt(a[0]) - parseInt(b[0]));
      const maxGenCount = Math.max(...Object.values(genCounts));

      genFreqEl.innerHTML = sortedGens.map(([gen, count]) => `
        <li class="freq-item">
          <span style="font-weight: 700; min-width: 90px;">${{currentLanguage === 'ar' ? `الجيل ${{gen}}` : `Gen ${{gen}}`}}</span>
          <div class="freq-bar-bg">
            <div class="freq-bar-fill" style="width: ${{(count / maxGenCount) * 100}}%;"></div>
          </div>
          <span style="font-weight: 700; color: var(--primary);">${{count}}</span>
        </li>
      `).join('');

      // Frequency of branches
      const branchCounts = {{}};
      flatMembers.forEach(m => {{
        const b = currentLanguage === 'ar' ? m.branch_ar : m.branch_en;
        branchCounts[b] = (branchCounts[b] || 0) + 1;
      }});
      const sortedBranches = Object.entries(branchCounts).sort((a,b) => b[1] - a[1]);
      const maxBranchCount = sortedBranches[0] ? sortedBranches[0][1] : 1;

      branchFreqEl.innerHTML = sortedBranches.map(([branch, count]) => `
        <li class="freq-item">
          <span style="font-weight: 700; min-width: 140px; font-size: 0.84rem;">${{branch}}</span>
          <div class="freq-bar-bg">
            <div class="freq-bar-fill" style="width: ${{(count / maxBranchCount) * 100}}%;"></div>
          </div>
          <span style="font-weight: 700; color: var(--primary);">${{count}}</span>
        </li>
      `).join('');
    }}

    // Navigation & Tabs
    function switchTab(tabId) {{
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));

      const targetBtn = event ? event.currentTarget : null;
      if (targetBtn) targetBtn.classList.add('active');

      const targetPanel = document.getElementById(`view-${{tabId}}`);
      if (targetPanel) targetPanel.classList.add('active');

      if (tabId === 'tree') {{
        setTimeout(resetZoom, 50);
      }}
    }}

    // Search Interaction
    function handleSearch(val) {{
      const query = val.trim().toLowerCase();
      
      // Update Table view
      filterTable();

      // Highlight in Tree View
      document.querySelectorAll('.tree-node').forEach(node => {{
        node.classList.remove('highlighted');
      }});

      if (!query) return;

      const matchedMembers = flatMembers.filter(m => {{
        return m.name_ar.toLowerCase().includes(query) ||
               m.name_en.toLowerCase().includes(query) ||
               (m.lineage_ar && m.lineage_ar.toLowerCase().includes(query)) ||
               (m.notes && m.notes.toLowerCase().includes(query));
      }});

      matchedMembers.forEach(m => {{
        const el = document.getElementById(`node-${{m.id}}`);
        if (el) {{
          el.classList.add('highlighted');
          // Uncollapse parents
          let curr = m;
          while (curr && curr.parent_id) {{
            collapsedNodes.delete(curr.parent_id);
            curr = flatMembers.find(f => f.id === curr.parent_id);
          }}
        }}
      }});

      if (matchedMembers.length > 0 && matchedMembers.length < 5) {{
        renderTreeView();
        // re-highlight after render
        matchedMembers.forEach(m => {{
          const el = document.getElementById(`node-${{m.id}}`);
          if (el) el.classList.add('highlighted');
        }});
      }}
    }}

    // Modal & CRUD Operations
    function populateParentSelects() {{
      const selectEdit = document.getElementById('edit-parent-id');
      const selectAdd = document.getElementById('add-parent-id');
      if (!selectEdit || !selectAdd) return;

      const options = flatMembers.map(m => {{
        const label = currentLanguage === 'ar' 
          ? `${{m.name_ar}} (${{m.lineage_ar || m.branch_ar}})` 
          : `${{m.name_en}} (${{m.lineage_en || m.branch_en}})`;
        return `<option value="${{m.id}}">${{label}}</option>`;
      }}).join('');

      selectEdit.innerHTML = `<option value="">${{currentLanguage === 'ar' ? '-- بدون أب (جذر) --' : '-- No Parent (Root) --'}}</option>` + options;
      selectAdd.innerHTML = options;
    }}

    function inspectMember(id) {{
      const member = flatMembers.find(m => m.id === id);
      if (!member) return;

      document.getElementById('edit-id').value = member.id;
      document.getElementById('edit-name-ar').value = member.name_ar;
      document.getElementById('edit-name-en').value = member.name_en;
      document.getElementById('edit-notes').value = member.notes || '';
      document.getElementById('edit-parent-id').value = member.parent_id || '';

      const lineage = currentLanguage === 'ar' ? member.lineage_ar : member.lineage_en;
      const branch = currentLanguage === 'ar' ? member.branch_ar : member.branch_en;
      document.getElementById('modal-lineage').innerHTML = `
        <div style="font-weight: 700; color: var(--primary); margin-bottom: 4px;">${{lineage}}</div>
        <div style="display: flex; gap: 8px;">
          <span class="tag-badge">${{branch}}</span>
          <span class="tag-badge">${{currentLanguage === 'ar' ? `الجيل ${{member.generation}}` : `Gen ${{member.generation}}`}}</span>
          <span class="tag-badge">${{member.children_count}} ${{currentLanguage === 'ar' ? 'أبناء' : 'Children'}}</span>
        </div>
      `;

      openModal('member-modal');
    }}

    function saveMemberEdit() {{
      const id = document.getElementById('edit-id').value;
      const nameAr = document.getElementById('edit-name-ar').value.trim();
      const nameEn = document.getElementById('edit-name-en').value.trim();
      const notes = document.getElementById('edit-notes').value.trim();
      const parentId = document.getElementById('edit-parent-id').value;

      if (!nameAr) {{
        alert(currentLanguage === 'ar' ? 'يرجى إدخال الاسم بالعربية' : 'Please enter the Arabic name');
        return;
      }}

      // Find node in tree
      let targetNode = null;
      function findNode(node) {{
        if (node.id === id) {{
          targetNode = node;
          return;
        }}
        if (node.children) node.children.forEach(findNode);
      }}
      findNode(treeData);

      if (targetNode) {{
        targetNode.name_ar = nameAr;
        targetNode.name_en = nameEn || nameAr;
        targetNode.notes = notes;
        
        // Handle parent change if different
        const currentParentId = targetNode.parent_id;
        if (parentId && parentId !== currentParentId && parentId !== targetNode.id) {{
          // Remove from old parent
          function removeNode(parent) {{
            if (!parent.children) return;
            const idx = parent.children.findIndex(c => c.id === id);
            if (idx !== -1) {{
              parent.children.splice(idx, 1);
            }} else {{
              parent.children.forEach(removeNode);
            }}
          }}
          removeNode(treeData);

          // Add to new parent
          function addToNewParent(node) {{
            if (node.id === parentId) {{
              if (!node.children) node.children = [];
              targetNode.generation = node.generation + 1;
              targetNode.parent_id = node.id;
              node.children.push(targetNode);
              return;
            }}
            if (node.children) node.children.forEach(addToNewParent);
          }}
          addToNewParent(treeData);
        }}

        saveState();
        closeModal('member-modal');
        showToast(currentLanguage === 'ar' ? 'تم حفظ التعديلات بنجاح' : 'Changes saved successfully');
      }}
    }}

    function openAddMemberModal() {{
      document.getElementById('add-name-ar').value = '';
      document.getElementById('add-name-en').value = '';
      document.getElementById('add-notes').value = '';
      openModal('add-modal');
    }}

    function openAddChildFromModal() {{
      const currentId = document.getElementById('edit-id').value;
      closeModal('member-modal');
      document.getElementById('add-name-ar').value = '';
      document.getElementById('add-name-en').value = '';
      document.getElementById('add-notes').value = '';
      document.getElementById('add-parent-id').value = currentId;
      openModal('add-modal');
    }}

    function confirmAddMember() {{
      const nameAr = document.getElementById('add-name-ar').value.trim();
      const nameEn = document.getElementById('add-name-en').value.trim() || nameAr;
      const parentId = document.getElementById('add-parent-id').value;
      const notes = document.getElementById('add-notes').value.trim();

      if (!nameAr) {{
        alert(currentLanguage === 'ar' ? 'يرجى كتابة الاسم بالعربية' : 'Please provide the Arabic name');
        return;
      }}
      if (!parentId) {{
        alert(currentLanguage === 'ar' ? 'يرجى اختيار الأب' : 'Please select a parent');
        return;
      }}

      const newId = 'member_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4);

      function attachChild(node) {{
        if (node.id === parentId) {{
          if (!node.children) node.children = [];
          node.children.push({{
            id: newId,
            name_ar: nameAr,
            name_en: nameEn,
            generation: node.generation + 1,
            notes: notes,
            children: []
          }});
          return true;
        }}
        if (node.children) {{
          for (let c of node.children) {{
            if (attachChild(c)) return true;
          }}
        }}
        return false;
      }}

      attachChild(treeData);
      saveState();
      closeModal('add-modal');
      showToast(currentLanguage === 'ar' ? 'تمت إضافة الفرد بنجاح' : 'New member added successfully');
    }}

    function deleteCurrentMember() {{
      const id = document.getElementById('edit-id').value;
      const t = I18N[currentLanguage];
      if (!confirm(t.deleteConfirm)) return;

      if (id === treeData.id) {{
        alert('لا يمكن حذف العقدة الجذرية للمشجرة!');
        return;
      }}

      function removeRecursive(parent) {{
        if (!parent.children) return false;
        const idx = parent.children.findIndex(c => c.id === id);
        if (idx !== -1) {{
          parent.children.splice(idx, 1);
          return true;
        }}
        for (let c of parent.children) {{
          if (removeRecursive(c)) return true;
        }}
        return false;
      }}

      removeRecursive(treeData);
      saveState();
      closeModal('member-modal');
      showToast(currentLanguage === 'ar' ? 'تم حذف الفرد' : 'Member deleted');
    }}

    // Export & Import & Reset
    function exportData() {{
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(treeData, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", `al_nada_family_tree_${{new Date().toISOString().slice(0,10)}}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
      showToast(currentLanguage === 'ar' ? 'تم تحميل ملف البيانات بنجاح' : 'JSON exported successfully');
    }}

    function importData(event) {{
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {{
        try {{
          const imported = JSON.parse(e.target.result);
          if (imported.name_ar && imported.children) {{
            treeData = imported;
            saveState();
            showToast(currentLanguage === 'ar' ? 'تم استيراد البيانات بنجاح' : 'JSON imported successfully');
          }} else {{
            alert(currentLanguage === 'ar' ? 'ملف غير صالح' : 'Invalid family tree format');
          }}
        }} catch(err) {{
          alert('Error parsing JSON: ' + err.message);
        }}
      }};
      reader.readAsText(file);
    }}

    function resetData() {{
      const t = I18N[currentLanguage];
      if (!confirm(t.resetConfirm)) return;

      localStorage.removeItem(LS_DATA_KEY);
      treeData = JSON.parse(JSON.stringify(ORIGINAL_TREE_DATA));
      collapsedNodes.clear();
      rebuildFlatList();
      renderAllViews();
      showToast(currentLanguage === 'ar' ? 'تمت استعادة الشجرة الأصلية' : 'Reset to original dataset');
    }}

    // UI Utilities
    function openModal(id) {{
      document.getElementById(id).classList.add('open');
    }}

    function closeModal(id) {{
      document.getElementById(id).classList.remove('open');
    }}

    function showToast(msg, icon = '✅') {{
      const toast = document.getElementById('toast');
      document.getElementById('toast-msg').textContent = msg;
      document.getElementById('toast-icon').textContent = icon;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 3000);
    }}
  </script>
</body>
</html>
"""

out_html_path = os.path.join(out_dir, "index.html")
with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML file successfully generated at: {out_html_path}")
print(f"File size: {len(html_content)} characters")
