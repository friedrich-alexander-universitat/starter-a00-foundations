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
    assert ns["classify_triangle"](3, 3, 3) == "equilateral"
    assert ns["classify_triangle"](1, 2, 10) == "invalid"
    print("Task 3 passed")
except Exception as e:
    print(f"Task 3 failed: {e}")
    sys.exit(1)
