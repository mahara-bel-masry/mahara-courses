# Real DNS lookup and TLS handshake lines for a public site (example.com).
getent hosts example.com | head -2
curl -sv https://example.com/ -o /dev/null 2>&1 | grep -E '^(\* (Connected|SSL connection|TLSv|ALPN|Server certificate:)|\*  subject|\* using HTTP)' | head -10
