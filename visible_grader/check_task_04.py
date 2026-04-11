import nbformat
import sys

def load_namespace():
    nb = nbformat.read("assignment.ipynb", as_version=4)
    code = "\n\n".join(cell.source for cell in nb.cells if cell.cell_type == "code")
    ns = {}
    exec(code, ns)
    return ns

try:
    ns = load_namespace()
    assert ns == 13
    assert ns == [0, 1, 1, 2, 3]
    print("Task 4 passed")
except Exception as e:
    print(f"Task 4 failed: {e}")
    sys.exit(1)
