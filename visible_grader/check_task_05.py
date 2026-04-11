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
    assert ns["safe_divide"](10, 2) == 5.0
    assert ns["batch_divide"]([(10, 2), (7, 0)]) == [5.0, None]
    print("Task 5 passed")
except Exception as e:
    print(f"Task 5 failed: {e}")
    sys.exit(1)
