# -*- coding: utf-8 -*-
"""
Script to integrate role/branch checks and audit logging into CRUD actions
"""
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update saveMemberEdit
old_save_member = """      if (targetNode) {
        targetNode.name_ar = nameAr;
        targetNode.name_en = nameEn || nameAr;
        targetNode.notes = notes;"""

new_save_member = """      if (targetNode) {
        if (!canUserEditBranch(targetNode.branch_ar)) {
          alert(currentLanguage === 'ar' 
            ? `عذراً، صلاحياتك كمحرر محصورة بفرع (${currentUser.branch || 'المحدد'}) فقط. لا يمكنك تعديل بيانات هذا الفرد لضمان دقة الأنساب.` 
            : `Editing restricted to branch: ${currentUser.branch}`);
          return;
        }

        const oldName = targetNode.name_ar;
        targetNode.name_ar = nameAr;
        targetNode.name_en = nameEn || nameAr;
        targetNode.notes = notes;"""

if old_save_member in content:
    content = content.replace(old_save_member, new_save_member)

# 2. Update saveMemberEdit logging
old_save_toast = """        saveState();
        closeModal('member-modal');
        showToast(currentLanguage === 'ar' ? 'تم حفظ التعديلات بنجاح' : 'Changes saved successfully');"""

new_save_toast = """        saveState();
        closeModal('member-modal');
        logActivity('تعديل بيانات فرد', `تم تعديل بيانات (${nameAr}) في (${targetNode.branch_ar || 'الشجرة'})`);
        showToast(currentLanguage === 'ar' ? 'تم حفظ التعديلات بنجاح' : 'Changes saved successfully');"""

if old_save_toast in content:
    content = content.replace(old_save_toast, new_save_toast)

# 3. Update confirmAddMember to check branch & log
old_add_parent_check = """      if (!parentId) {
        alert(currentLanguage === 'ar' ? 'يرجى اختيار الأب' : 'Please select a parent');
        return;
      }"""

new_add_parent_check = """      if (!parentId) {
        alert(currentLanguage === 'ar' ? 'يرجى اختيار الأب' : 'Please select a parent');
        return;
      }

      const parentMember = flatMembers.find(m => m.id === parentId);
      const parentBranch = parentMember ? parentMember.branch_ar : 'الأصل';
      if (!canUserEditBranch(parentBranch)) {
        alert(currentLanguage === 'ar' 
          ? `عذراً، صلاحياتك كمحرر محصورة بفرع (${currentUser.branch || 'المحدد'}) فقط. لا يمكنك إضافة أفراد في فرع (${parentBranch}) لضمان دقة الأنساب.` 
          : `Adding members restricted to branch: ${currentUser.branch}`);
        return;
      }"""

if old_add_parent_check in content:
    content = content.replace(old_add_parent_check, new_add_parent_check)

old_add_toast = """      attachChild(treeData);
      saveState();
      closeModal('add-modal');
      showToast(currentLanguage === 'ar' ? 'تمت إضافة الفرد بنجاح' : 'New member added successfully');"""

new_add_toast = """      attachChild(treeData);
      saveState();
      closeModal('add-modal');
      logActivity('إضافة فرد جديد', `تمت إضافة (${nameAr}) إلى الأب (${parentMember ? parentMember.name_ar : 'الأصل'}) في (${parentBranch})`);
      showToast(currentLanguage === 'ar' ? 'تمت إضافة الفرد بنجاح' : 'New member added successfully');"""

if old_add_toast in content:
    content = content.replace(old_add_toast, new_add_toast)

# 4. Update deleteCurrentMember for Super Admin requirement & logging
old_del_start = """    function deleteCurrentMember() {
      if (!isAuthorized()) {
        alert(I18N[currentLanguage].authRequired);
        return;
      }"""

new_del_start = """    function deleteCurrentMember() {
      if (!isAuthorized()) {
        alert(I18N[currentLanguage].authRequired);
        return;
      }

      if (!isSuperAdmin()) {
        alert(currentLanguage === 'ar' ? 'تنبيه: حذف أفراد من الشجرة يتطلب صلاحية المشرف العام.' : 'Deleting members requires Super Admin role.');
        return;
      }"""

if old_del_start in content:
    content = content.replace(old_del_start, new_del_start)

old_del_toast = """      removeRecursive(treeData);
      saveState();
      closeModal('member-modal');
      showToast(currentLanguage === 'ar' ? 'تم حذف الفرد' : 'Member deleted');"""

new_del_toast = """      const targetMember = flatMembers.find(m => m.id === id);
      removeRecursive(treeData);
      saveState();
      closeModal('member-modal');
      logActivity('حذف فرد من الشجرة', `تم حذف (${targetMember ? targetMember.name_ar : id}) وكافة ذريته`);
      showToast(currentLanguage === 'ar' ? 'تم حذف الفرد' : 'Member deleted');"""

if old_del_toast in content:
    content = content.replace(old_del_toast, new_del_toast)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Step 3: Branch permissions and audit logging integrated successfully into CRUD!')
