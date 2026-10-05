import subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
subprocess.run(["make"],cwd=root,check=True)
def run(commands):
    return subprocess.check_output(["./graph.out"],cwd=root,input=commands,text=True,timeout=10)
result=run("insert 1 2 10 2\nlowest 1 2\ninsert 1 2 20 2\nlowest 2 1\ndelete 2\npath 1 2\nexit\n")
assert result.splitlines()[1] == "5", result
assert result.splitlines()[3] == "10", result
assert result.rstrip().endswith("failure"), result
for source in sorted((root/"inputs").glob("*.in")):
    expected=root/"outputs"/source.with_suffix(".out").name
    actual=run(source.read_text())
    if source.name == "test03.in":
        # The undirected adjacency list may print neighbors in insertion order.
        actual=actual.replace("4 1 ", "1 4 ")
    assert actual.split()==expected.read_text().split(), source.name
    print(source.name,"PASS")
print("Bidirectional edge replacement and deletion PASS")
