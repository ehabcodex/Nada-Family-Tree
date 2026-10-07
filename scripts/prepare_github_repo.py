# -*- coding: utf-8 -*-
"""
Organize the project directory for clean GitHub publication
"""
import os
import shutil

base_dir = r"C:\Users\user\.gemini\antigravity\scratch\al_nada_family_tree"
data_dir = os.path.join(base_dir, "data")
scripts_dir = os.path.join(base_dir, "scripts")

os.makedirs(data_dir, exist_ok=True)
os.makedirs(scripts_dir, exist_ok=True)

# 1. Copy JSON files to data/
for f in ["family_tree.json", "family_members_flat.json"]:
    src = os.path.join(base_dir, f)
    dst = os.path.join(data_dir, f)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {f} to data/")

# 2. Move build/helper scripts to scripts/
helper_scripts = [
    "build_family_data.py",
    "generate_html.py",
    "sync_tree.py",
    "update_app.py",
    "add_user_mgmt.py",
    "build_users_page.py",
    "inject_users_js.py",
    "fix_engine_placement.py",
    "patch_crud_audit.py",
    "update_translations.py",
    "make_mobile_friendly.py",
    "verify_all.js"
]

for s in helper_scripts:
    src = os.path.join(base_dir, s)
    dst = os.path.join(scripts_dir, s)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        os.remove(src)
        print(f"Moved {s} to scripts/")

# 3. Remove temp files if present
for temp in ["diff_result.txt", "test_tree.html"]:
    p = os.path.join(base_dir, temp)
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed temp file {temp}")

print("Directory organized successfully!")
