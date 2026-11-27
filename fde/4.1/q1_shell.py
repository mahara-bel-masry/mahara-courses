import subprocess, tempfile, os
d = tempfile.mkdtemp()
os.chdir(d)
def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return r.stdout.strip()
sh("mkdir logs")
open("logs/app.log", "w").write("ok\nERROR disk\nok\nERROR net\n")
print(sh("ls logs"))
print(sh("grep ERROR logs/app.log"))
print(sh("grep -c ok logs/app.log"))
print(sh("grep ERROR logs/app.log | wc -l"))
