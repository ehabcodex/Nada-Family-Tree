const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const assertions = {
  'Users tab in HTML': html.includes('id="tab-btn-users"'),
  'View users panel in HTML': html.includes('id="view-users"'),
  'User form modal in HTML': html.includes('id="user-form-modal"'),
  'Change password modal in HTML': html.includes('id="user-pwd-modal"'),
  'renderUsersPage function in JS': html.includes('function renderUsersPage'),
  'getUsersList function in JS': html.includes('function getUsersList'),
  'logActivity function in JS': html.includes('function logActivity'),
  'canUserEditBranch function in JS': html.includes('function canUserEditBranch'),
  'isSuperAdmin function in JS': html.includes('function isSuperAdmin'),
  'Default super admin ehab': html.includes("username: 'ehab'") && html.includes("role: 'super_admin'"),
  'Footer Ehab Nada present': html.includes('إعداد: إيهاب ندى')
};

console.log('--- TEST RESULTS ---');
let allPassed = true;
for (const [k, v] of Object.entries(assertions)) {
  console.log((v ? '✅ ' : '❌ ') + k);
  if (!v) allPassed = false;
}
if (!allPassed) process.exit(1);
console.log('All tests passed successfully!');
