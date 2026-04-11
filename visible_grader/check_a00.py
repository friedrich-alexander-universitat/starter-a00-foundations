import nbformat
import sys

def load_functions():
    try:
        nb = nbformat.read("assignment.ipynb", as_version=4)
    except:
        print("❌ Cannot read notebook")
        return {}

    code = ""
    for cell in nb.cells:
        if cell.cell_type == "code":
            code += cell.source + "\n"

    namespace = {}
    try:
        exec(code, namespace)
    except Exception as e:
        print("❌ Error executing notebook:", e)
        return {}

    return namespace


def grade():
    ns = load_functions()
    score = 0

    # Task 1 (4 pts)
    try:
        if ns == (31.42, 78.54):
            score += 2
        if ns == (6.28, 3.14):
            score += 2
    except:
        pass

    # Task 2 (4 pts)
    try:
        if ns["format_name"]("anna", "SMITH") == "Smith, Anna":
            score += 2
        if ns["format_name"]("  john  ", " doe ") == "Doe, John":
            score += 2
    except:
        pass

    # Task 3 (4 pts)
    try:
        if ns["classify_triangle"](3,3,3) == "equilateral":
            score += 2
        if ns["classify_triangle"](1,2,10) == "invalid":
            score += 2
    except:
        pass

    # Task 4 (4 pts)
    try:
        if ns == 13:
            score += 2
        if ns == [0,1,1,2,3]:
            score += 2
    except:
        pass

    # Task 5 (4 pts)
    try:
        if ns["safe_divide"](10,2) == 5.0:
            score += 2
        if ns["batch_divide"]([(10,2),(7,0)]) == [5.0, None]:
            score += 2
    except:
        pass

    print(f"Score: {score}/20")

    if score < 20:
        sys.exit(1)


if __name__ == "__main__":
    grade()
