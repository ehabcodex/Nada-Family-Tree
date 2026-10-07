const http = require('http');

http.get('http://localhost:8080/index.html', (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    console.log('HTTP status:', res.statusCode);
    console.log('Includes exportToPDF:', data.includes('exportToPDF()'));
    console.log('Includes btn-export-pdf:', data.includes('id="btn-export-pdf"'));
    console.log('All 10 generation levels in CSS:');
    let allOk = true;
    for (let i = 0; i <= 10; i++) {
      const ok = data.includes('.tree-node.level-' + i);
      if (!ok) allOk = false;
      console.log(`  Gen ${i} style: ${ok ? 'OK' : 'MISSING'}`);
    }
    console.log('All levels present:', allOk);
    console.log('Accordion generation badges:', data.includes('gen-badge-${node.generation}'));
    console.log('Table generation badges:', data.includes('gen-badge-${m.generation}'));
  });
}).on('error', (e) => {
  console.error('Error:', e.message);
});
