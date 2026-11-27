// Local server. DELAY_CSS and DELAY_JS (milliseconds) slow down a file on purpose.
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve(process.argv[2] ?? 'site');
const delays = { '/style.css': Number(process.env.DELAY_CSS ?? 0), '/app.js': Number(process.env.DELAY_JS ?? 0) };
const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml' };
http.createServer((req, res) => {
  const p = req.url === '/' ? '/index.html' : req.url;
  const file = path.join(root, p);
  if (!file.startsWith(root) || !fs.existsSync(file)) { res.writeHead(404); res.end('not found'); return; }
  setTimeout(() => {
    res.writeHead(200, { 'content-type': types[path.extname(file)] ?? 'application/octet-stream' });
    res.end(fs.readFileSync(file));
  }, delays[p] ?? 0);
}).listen(Number(process.env.PORT ?? 8099), () => console.log('listening on', process.env.PORT ?? 8099));
