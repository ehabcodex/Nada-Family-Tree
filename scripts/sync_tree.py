# -*- coding: utf-8 -*-
import json
import os

tree_path = r"C:\Users\user\.gemini\antigravity\scratch\al_nada_family_tree\family_tree.json"
with open(tree_path, "r", encoding="utf-8") as f:
    tree = json.load(f)

flat_list = []

def traverse(node, parent=None, branch_ar="الأصل", branch_en="Root"):
    if node.get("branch_ar"):
        branch_ar = node["branch_ar"]
    if node.get("branch_en"):
        branch_en = node["branch_en"]
        
    node["parent_id"] = parent["id"] if parent else None
    node["parent_name_ar"] = parent["name_ar"] if parent else None
    node["parent_name_en"] = parent["name_en"] if parent else None
    node["branch_ar"] = branch_ar
    node["branch_en"] = branch_en
    
    if parent and parent.get("lineage_ar"):
        node["lineage_ar"] = f"{node['name_ar']} بن {parent['lineage_ar']}"
        node["lineage_en"] = f"{node['name_en']} bin {parent['lineage_en']}"
    elif parent:
        node["lineage_ar"] = f"{node['name_ar']} بن {parent['name_ar']}"
        node["lineage_en"] = f"{node['name_en']} bin {parent['name_en']}"
    else:
        node["lineage_ar"] = node["name_ar"]
        node["lineage_en"] = node["name_en"]
        
    flat_list.append({
        "id": node["id"],
        "name_ar": node["name_ar"],
        "name_en": node["name_en"],
        "parent_id": node["parent_id"],
        "parent_name_ar": node["parent_name_ar"],
        "parent_name_en": node["parent_name_en"],
        "generation": node["generation"],
        "branch_ar": node["branch_ar"],
        "branch_en": node["branch_en"],
        "lineage_ar": node["lineage_ar"],
        "lineage_en": node["lineage_en"],
        "notes": node.get("notes", ""),
        "children_count": len(node.get("children", []))
    })
    
    for c in node.get("children", []):
        traverse(c, node, branch_ar, branch_en)

traverse(tree)

flat_path = r"C:\Users\user\.gemini\antigravity\scratch\al_nada_family_tree\family_members_flat.json"
with open(tree_path, "w", encoding="utf-8") as f:
    json.dump(tree, f, ensure_ascii=False, indent=2)

with open(flat_path, "w", encoding="utf-8") as f:
    json.dump(flat_list, f, ensure_ascii=False, indent=2)

print("Updated flat list and tree. Total members:", len(flat_list))
