import os
import subprocess
import sys
from pathlib import Path

TESTS_DIR = Path(__file__).parent / "tests"
SOLUTION = Path(__file__).parent / "Solution.py"


def parse_input(text: str) -> tuple[int, list[int]]:
    lines = text.strip().splitlines()
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    return n, arr


def parse_output(text: str) -> int:
    return int(text.strip())


def run_test(in_path: Path, out_path: Path) -> tuple[bool, str, str]:
    input_text = in_path.read_text()
    expected = parse_output(out_path.read_text())

    result = subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=input_text,
        capture_output=True,
        text=True,
    )
    actual_text = result.stdout.strip()

    try:
        actual = int(actual_text)
    except ValueError:
        return False, str(expected), repr(actual_text)

    passed = actual == expected
    return passed, str(expected), str(actual)


def main():
    pairs = sorted(
        (f.stem for f in TESTS_DIR.glob("*.in")), key=lambda s: int(s)
    )

    if not pairs:
        print("No test cases found in tests/")
        return

    passed_count = 0
    for stem in pairs:
        in_path = TESTS_DIR / f"{stem}.in"
        out_path = TESTS_DIR / f"{stem}.out"

        if not out_path.exists():
            print(f"Test {stem}: SKIP (no .out file)")
            continue

        passed, expected, actual = run_test(in_path, out_path)
        status = "PASS" if passed else "FAIL"
        if passed:
            passed_count += 1
            print(f"Test {stem}: {status}")
        else:
            print(f"Test {stem}: {status}  expected={expected}  got={actual}")

    total = len(pairs)
    print(f"\n{passed_count}/{total} passed")


if __name__ == "__main__":
    main()
