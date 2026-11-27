# What a browser sends, written by hand with curl against our local server.
curl -sv http://127.0.0.1:8099/ -o /dev/null 2>&1 | grep -E '^(\*   Trying|\* Connected|> |< )'
