import nbformat
import sys

def load_namespace():
    nb = nbformat.read("assignment.ipynb", as_version=4)

    code_chunks = []
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue

        src = cell.source

        if src.strip().startswith("# VISIBLE TEST"):
            continue
        if src.strip().startswith("# METADATA"):
            continue

        code_chunks.append(src)

    code = "\n\n".join(code_chunks)
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
