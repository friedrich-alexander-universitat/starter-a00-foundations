import traceback
import nbformat
from pathlib import Path

NOTEBOOK_PATH = Path("assignment.ipynb")


def _student_code_cells():
    nb = nbformat.read(NOTEBOOK_PATH, as_version=4)

    code_chunks = []
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue

        src = cell.source.strip()

        if src.startswith("# VISIBLE TEST"):
            continue
        if src.startswith("# METADATA"):
            continue

        code_chunks.append(cell.source)

    return code_chunks


def load_namespace():
    namespace = {}
    code = "\n\n".join(_student_code_cells())
    exec(code, namespace)
    return namespace


def safe_test(name, max_score, fn, env):
    try:
        score, message = fn(env)
        score = max(0, min(score, max_score))
        return {
            "name": name,
            "score": score,
            "max_score": max_score,
            "message": message,
        }
    except Exception as exc:
        traceback.print_exc()
        return {
            "name": name,
            "score": 0,
            "max_score": max_score,
            "message": f"Error during grading: {exc}",
        }


# -------- TASKS --------

def test_task_01(env):
    f = env.get("circle_stats")
    if not callable(f):
        return 0, "circle_stats missing"

    checks = [
        f(5) == (31.42, 78.54),
        f(1) == (6.28, 3.14),
        f(0) == (0.0, 0.0),
        isinstance(f(2), tuple) and len(f(2)) == 2,
    ]
    return sum(checks), "circle_stats checked"


def test_task_02(env):
    f = env.get("format_name")
    if not callable(f):
        return 0, "format_name missing"

    checks = [
        f("anna", "SMITH") == "Smith, Anna",
        f("  john  ", " doe ") == "Doe, John",
        f("ALICE", "wonderland") == "Wonderland, Alice",
        f(" bob", "BROWN ") == "Brown, Bob",
    ]
    return sum(checks), "format_name checked"


def test_task_03(env):
    f = env.get("classify_triangle")
    if not callable(f):
        return 0, "classify_triangle missing"

    checks = [
        f(3, 3, 3) == "equilateral",
        f(3, 3, 4) == "isosceles",
        f(3, 4, 5) == "scalene",
        f(1, 2, 10) == "invalid",
    ]
    return sum(checks), "triangle checked"


def test_task_04(env):
    fib = env.get("fibonacci")
    seq = env.get("fibonacci_sequence")

    if not callable(fib) or not callable(seq):
        return 0, "fibonacci functions missing"

    checks = [
        fib(0) == 0,
        fib(1) == 1,
        fib(7) == 13,
        seq(8) == [0, 1, 1, 2, 3, 5, 8, 13],
    ]
    return sum(checks), "fibonacci checked"


def test_task_05(env):
    safe_divide = env.get("safe_divide")
    batch_divide = env.get("batch_divide")

    if not callable(safe_divide) or not callable(batch_divide):
        return 0, "divide functions missing"

    checks = [
        safe_divide(10, 2) == 5.0,
        safe_divide(7, 0) is None,
        isinstance(safe_divide(10, 2), float),
        batch_divide([(10, 2), (7, 0), (9, 3)]) == [5.0, None, 3.0],
    ]
    return sum(checks), "division checked"


def run_all_tests():
    env = load_namespace()

    return [
        safe_test("Task 1", 4, test_task_01, env),
        safe_test("Task 2", 4, test_task_02, env),
        safe_test("Task 3", 4, test_task_03, env),
        safe_test("Task 4", 4, test_task_04, env),
        safe_test("Task 5", 4, test_task_05, env),
    ]
