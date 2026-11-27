import subprocess
LOG = "GET /a 200\nGET /b 500\nGET /a 200\nGET /c 404\nGET /b 500\n"
open("access.log", "w").write(LOG)
def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return r.stdout.strip()
print(sh("wc -l < access.log"))
print(sh("grep -c 500 access.log"))
print(sh("grep 500 access.log | wc -l"))
print(sh("cut -d' ' -f2 access.log | sort | uniq -c | sort -rn | head -1"))
