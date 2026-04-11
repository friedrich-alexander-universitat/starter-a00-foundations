import json
import sys
from tests import run_all_tests

TASK_MAP = {
    "task_01": "Task 1",
    "task_02": "Task 2",
    "task_03": "Task 3",
    "task_04": "Task 4",
    "task_05": "Task 5",
}


def main():
    results = run_all_tests()

    if len(sys.argv) > 1:
        task_key = sys.argv[1].strip()
        if task_key not in TASK_MAP:
            print(f"Unknown task: {task_key}")
            sys.exit(1)

        wanted_name = TASK_MAP[task_key]
        match = next((item for item in results if item["name"] == wanted_name), None)

        if match is None:
            print(f"Missing result for {wanted_name}")
            sys.exit(1)

        print(f'{match["name"]}: {match["score"]}/{match["max_score"]}')
        if match.get("message"):
            print(match["message"])

        print(json.dumps(match))

        if match["score"] == match["max_score"]:
            sys.exit(0)
        else:
            sys.exit(1)

    total_score = sum(item["score"] for item in results)
    max_score = sum(item["max_score"] for item in results)

    for item in results:
        print(f'{item["name"]}: {item["score"]}/{item["max_score"]}')
        if item.get("message"):
            print(item["message"])

    print(f"\nTOTAL: {total_score}/{max_score}")
    print(json.dumps({"score": total_score, "max_score": max_score}))
    sys.exit(0)


if __name__ == "__main__":
    main()
