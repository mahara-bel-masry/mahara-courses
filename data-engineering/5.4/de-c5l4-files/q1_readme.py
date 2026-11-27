import re
R = "# Pipeline\n## Setup\npip install -r requirements.txt\n"
R += "## Run\npython etl.py\n"
R += "## Data\ndata/ is ignored\n"
open("README.md", "w").write(R)
t = open("README.md").read()
print(len(re.findall("^## ", t, re.M)))
print([x[3:] for x in t.split("\n") if x.startswith("## ")])
print("python etl.py" in t)
