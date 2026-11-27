# 1.1 sources (fetched 2026-11-27) and the sentences relied on

1. MDN script element https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script
   - "This Boolean attribute is set to indicate to a browser that the script is meant to be executed after the document has been parsed, but before firing DOMContentLoaded event." (defer)
   - "The defer attribute has no effect on module scripts — they defer by default."
   - "if a script element does not include type="module", async, or defer, then it blocks parsing, not rendering."
2. web.dev preload scanner https://web.dev/articles/preload-scanner
   - "A preload scanner's role is speculative, meaning that it examines raw markup in order to find resources to opportunistically fetch before the primary HTML parser would otherwise discover them."
   - "The browser also blocks parsing and rendering of the page when it encounters script elements without a defer or async attribute."
3. web.dev Adding interactivity with JavaScript https://web.dev/articles/critical-rendering-path/adding-interactivity-with-javascript
   - "JavaScript execution blocks on the CSSOM."
4. WHATWG HTML parsing 13.2.2 https://html.spec.whatwg.org/multipage/parsing.html
   - "This specification defines the parsing rules for HTML documents, whether they are syntactically correct or not." and "The error handling for parse errors is well-defined"
5. MDN How browsers work https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/How_browsers_work
   - DNS: "The first step when navigating to a web page is locating the page's assets." ; TCP: "the browser sets up a connection to the server via a TCP three-way handshake" ; TLS: "A full TLS 1.3 handshake takes one round trip to the server before the browser can send the content request; a full TLS 1.2 handshake takes two."
6. MDN ALPN https://developer.mozilla.org/en-US/docs/Glossary/ALPN
   - "Application-Layer Protocol Negotiation (ALPN) is a TLS extension (defined in RFC 7301) for identifying what application-layer protocol is negotiating the encrypted connection, without requiring additional round trips to do so."
7. MDN HTTP status https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
   - classes: Informational 100-199, Successful 200-299, Redirection 300-399, Client error 400-499, Server error 500-599
8. MDN Same-origin policy https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
   - "Modern browsers usually treat the origin of files loaded using the file:/// scheme as opaque origins. ... may trigger CORS errors."
9. MDN Critical rendering path https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Critical_rendering_path
   - "The critical rendering path includes the Document Object Model (DOM), CSS Object Model (CSSOM), render tree and layout."
10. web.dev Render-blocking CSS https://web.dev/articles/critical-rendering-path/render-blocking-css
   - "By default, CSS is treated as a render-blocking resource"
11. Chrome DevTools Network reference https://developer.chrome.com/docs/devtools/network/reference and Open Chrome DevTools https://developer.chrome.com/docs/devtools/open
Page names: item 3 is the web.dev page "Adding interactivity with JavaScript" (sentence "JavaScript execution blocks on the CSSOM."); item 2 is the web.dev article on the browser preload scanner (/articles/preload-scanner, the page title was not shown by the fetch tool).
