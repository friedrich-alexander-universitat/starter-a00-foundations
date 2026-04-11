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
    assert ns["format_name"]("anna", "SMITH") == "Smith, Anna"
    assert ns["format_name"]("  john  ", " doe ") == "Doe, John"
    print("Task 2 passed")
except Exception as e:
    print(f"Task 2 failed: {e}")
    sys.exit(1)
