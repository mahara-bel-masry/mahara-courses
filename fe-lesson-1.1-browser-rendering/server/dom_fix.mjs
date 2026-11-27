// Feed the browser broken HTML and print the DOM it builds.
import { chromium } from '@playwright/test';
const broken = '<p>one<p>two<ul><li>a<li>b</ul><b>bold<i>both</b>italic</i>';
const browser = await chromium.launch({ channel: 'chrome' });
const page = await (await browser.newContext()).newPage();
await page.setContent(broken);
console.log('input :', broken);
console.log('output:', await page.evaluate(() => document.body.innerHTML));
await browser.close();
