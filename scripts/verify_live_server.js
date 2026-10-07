const http = require('http');

http.get('http://localhost:8080/index.html', (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    console.log('HTTP status:', res.statusCode);
    console.log('Total bytes:', data.length);
    console.log('Static toast message present:', data.includes('تمت العملية بنجاح'));
    console.log('Centered footer present:', data.includes('footer style="text-align: center;"'));
    console.log('direction ltr on tree-canvas present:', data.includes('direction: ltr !important'));
  });
}).on('error', (e) => {
  console.error('Fetch error:', e.message);
});
