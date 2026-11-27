import subprocess, tempfile, os
d = tempfile.mkdtemp()
os.chdir(d)
def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return (r.stdout + r.stderr).strip()
open("run.sh", "w").write("#!/bin/bash\necho done\n")
print(sh("./run.sh").split(":")[-1].strip())
sh("chmod +x run.sh")
print(sh("./run.sh"))
print(sh("stat -c %a run.sh"))
