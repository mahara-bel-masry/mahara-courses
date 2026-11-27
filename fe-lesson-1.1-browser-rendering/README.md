# Front End Diploma, Lesson 1.1: How the browser renders a page (URL to pixels)

Files for the video. The scenario in the video (an online shop called "Nile Store") and its numbers are invented for teaching. All other numbers come from the logs in `logs/`.

## What you need
- For the lab (the part you do yourself): Chrome and a text editor like Notepad. Nothing else.
- For the demo scripts in `server/` (optional, only to reproduce my runs): Node, npm, Playwright and curl. The terminal is lesson 1.2 and npm and Node are lesson 1.3 of the diploma, so you do not need them for this lesson.

## Lab (Chrome only)
1. Open `lab/head/index.html`, `lab/defer/index.html` and `lab/end/index.html` in Chrome, one by one. Each has `index.html`, `style.css`, `app.js`. `app.js` keeps the page busy for about one and a half seconds (a stand-in for a slow script). The only difference between the three pages is the line of the `<script>` tag: in `head`, plain in the head; in `defer`, in the head with `defer`; in `end`, at the end of the body.
2. After the page loads, open the Console (Chrome DevTools doc: Control+Shift+J on Windows and Linux, Command+Option+J on Mac) and paste the measure line from `lab/measure_console_line.txt`. It prints first paint and DOMContentLoaded in milliseconds.
3. Open each page three times, close the tab between runs, write all three numbers.
4. `lab/broken.html`: write down the DOM you expect, open it, compare in the Elements tab.

Measure line (same text as `lab/measure_console_line.txt`):

    JSON.stringify({paint: performance.getEntriesByType('paint').map(p => [p.name, Math.round(p.startTime)]), domContentLoaded: Math.round(performance.getEntriesByType('navigation')[0].domContentLoadedEventEnd)})

## My runs (all on one machine, Chrome only)
- Versions: Chrome 157.0.8103.78, Playwright 1.65.1, Node 26.13.1 (`logs/versions.log`, `logs/versions_lab_chrome_only.log`).
- Lab pages, three runs (`logs/lab_chrome_only_run1.out` to `run3.out`), first paint in ms: head 1556, 1544, 1540; defer 40, 44, 44; end 1540, 76, 56. The `end` case was not stable and I have no explanation for it.
- Server runs, three runs per case (`logs/timeline_<case>_run1.out` to `run3.out`, made with `server/server.mjs` and `server/timeline.mjs`). Cases: normal, slow_css, head_blocking, head_defer, body_script_delay. The server delays the CSS or app.js by 1500 ms.
- `logs/favicon_status.out`: curl shows the server code answers 404 for a missing file (`/favicon.ico`) and 200 for `style.css`.
- `logs/dns_tls.out`, `logs/http_by_hand.out`, `logs/dom_fix.out`: output of `server/dns_tls.sh`, `server/http_by_hand.sh`, `server/dom_fix.mjs`.

## What I did not run
async scripts, network throttling, the Network tab screen with these numbers, the extra lab task (shorter loop), and Firefox or Safari. Those statements in the video are from documentation or are labelled as not tested.

## Run the demo scripts (optional)
Needs Node, Chrome, curl, and `npm i @playwright/test` inside `server/`. Run the commands from `server/`. For each case: terminal 1 starts the server, terminal 2 runs `node timeline.mjs http://127.0.0.1:8099/`, then stop the server. The logs in `logs/` were made this way, three runs per case.

| case (log name) | terminal 1 |
| --- | --- |
| normal | `node server.mjs ../demo-site/normal` |
| slow_css | `DELAY_CSS=1500 node server.mjs ../demo-site/normal` |
| head_blocking | `DELAY_JS=1500 node server.mjs ../demo-site/script-in-head` |
| head_defer | `DELAY_JS=1500 node server.mjs ../demo-site/script-defer` |
| body_script_delay | `DELAY_JS=1500 node server.mjs ../demo-site/normal` |

Other scripts: `sh dns_tls.sh`, `sh http_by_hand.sh` (server must be running on port 8099), `node dom_fix.mjs`. The 404 check: `curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8099/favicon.ico` with the server running (log: `logs/favicon_status.out`).
Note: `demo-site/normal` has the script at the end of the body.

## Sources (fetched 2026-11-27)
See `sources.md` for each link and the sentence I rely on.
