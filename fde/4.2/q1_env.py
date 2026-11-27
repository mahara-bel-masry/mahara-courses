import os, subprocess, tempfile
d = tempfile.mkdtemp()
os.chdir(d)
SCRIPT = """#!/bin/bash
NAME=${1:-world}
echo "hello $NAME"
"""
open("hello.sh", "w").write(SCRIPT)
open(".env", "w").write("API_KEY=demo-key\n")
open(".gitignore", "w").write(".env\n")
def sh(cmd, env=None):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)
    return r.stdout.strip()
print(sh("bash hello.sh Ali"))
print(sh("bash hello.sh"))
print(sh("set -a; . ./.env; echo $API_KEY"))
print(sh("cat .gitignore"))
