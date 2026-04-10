import sys
from pathlib import Path
import nbformat


NOTEBOOK = Path("assignment.ipynb")


def extract_code_cells(nb):
    return ["".join(cell.get("source", "")) for cell in nb.cells if cell.get("cell_type") == "code"]


def main():
    if not NOTEBOOK.exists():
        print("assignment.ipynb not found")
        sys.exit(1)

    nb = nbformat.read(NOTEBOOK, as_version=4)
    code_cells = extract_code_cells(nb)
    all_code = "\n\n".join(code_cells)

    required_snippets = [
        "def circle_stats(",
        "def format_name(",
        "def classify_triangle(",
        "def fibonacci(",
        "def fibonacci_sequence(",
        "def safe_divide(",
        "def batch_divide("
    ]

    missing = [snippet for snippet in required_snippets if snippet not in all_code]
    if missing:
        print("Missing required definitions:")
        for item in missing:
            print(f"- {item}")
        sys.exit(1)

    print("Visible structure checks passed.")


if __name__ == "__main__":
    main()
