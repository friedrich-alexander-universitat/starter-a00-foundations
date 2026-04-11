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
    assert ns == (31.42, 78.54)
    assert ns == (6.28, 3.14)
    print("Task 1 passed")
except Exception as e:
    print(f"Task 1 failed: {e}")
    sys.exit(1)
