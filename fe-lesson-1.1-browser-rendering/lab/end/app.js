// Busy loop: keeps the page's main thread busy for about 1.5 seconds (a stand-in for a slow script).
const t0 = Date.now();
while (Date.now() - t0 < 1500) {}
document.querySelector('h1').textContent = 'script finished';
