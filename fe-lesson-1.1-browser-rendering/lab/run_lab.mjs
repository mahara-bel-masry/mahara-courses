// Runs each lab page in real Chrome (file:// URL), evaluates the exact Console one-liner a learner would paste, and logs CDP network events.
import { chromium } from '@playwright/test';
import fs from 'node:fs';
const js = fs.readFileSync(new URL('./measure_console.js', import.meta.url), 'utf8');
const b = await chromium.launch({ channel: 'chrome' });
console.log('Chrome', b.version());
for (const v of ['head', 'defer', 'end']) {
  const ctx = await b.newContext(); const p = await ctx.newPage();
  const cdp = await ctx.newCDPSession(p); await cdp.send('Network.enable');
  const seen = []; cdp.on('Network.requestWillBeSent', e => seen.push(e.request.url.split('/').slice(-2).join('/')));
  await p.goto('file://' + new URL(`./${v}/index.html`, import.meta.url).pathname, { waitUntil: 'load' });
  await p.waitForTimeout(500);
  console.log(v, await p.evaluate(js), 'requests seen by CDP Network domain:', seen.join(', '));
  await ctx.close();
}
const ctx = await b.newContext(); const p = await ctx.newPage();
await p.goto('file://' + new URL('./broken.html', import.meta.url).pathname);
console.log('broken body DOM:', await p.evaluate(() => document.body.innerHTML.replace(/\n/g, '\\n')));
await b.close();
