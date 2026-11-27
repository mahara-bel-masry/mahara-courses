// Load the page in real Chrome and print what happened and when (milliseconds since navigation start).
import { chromium } from '@playwright/test';
const url = process.argv[2];
const browser = await chromium.launch({ channel: 'chrome' });
const ctx = await browser.newContext();
const page = await ctx.newPage();
const status = {}; // HTTP status of every response, by path
page.on('response', r => { status[new URL(r.url()).pathname] = r.status(); });
await page.goto(url, { waitUntil: 'load' });
await page.waitForTimeout(600); // let the first paint happen before we read the paint entries
const data = await page.evaluate(() => {
  const nav = performance.getEntriesByType('navigation')[0];
  const paints = Object.fromEntries(performance.getEntriesByType('paint').map(p => [p.name, Math.round(p.startTime)]));
  const res = performance.getEntriesByType('resource').map(r => ({ name: new URL(r.name).pathname, type: r.initiatorType, start: Math.round(r.startTime), end: Math.round(r.responseEnd) }));
  return { nav: { requestStart: Math.round(nav.requestStart), responseEnd: Math.round(nav.responseEnd), domContentLoaded: Math.round(nav.domContentLoadedEventEnd), load: Math.round(nav.loadEventEnd) }, paints, res };
});
data.status = status;
console.log(JSON.stringify(data, null, 2));
await browser.close();
