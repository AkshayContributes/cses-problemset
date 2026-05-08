import subprocess
import sys
from pathlib import Path

TESTS_DIR = Path(__file__).parent / "tests"
SOLUTION = Path(__file__).parent / "Solution.py"


def run_test(in_path: Path, out_path: Path) -> tuple[bool, str]:
    input_text = in_path.read_text()
    expected_lines = out_path.read_text().strip().splitlines()

    result = subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=input_text,
        capture_output=True,
        text=True,
    )
    actual_lines = result.stdout.strip().splitlines()

    if len(actual_lines) != len(expected_lines):
        return False, (
            f"expected {len(expected_lines)} lines, got {len(actual_lines)}"
        )

    for idx, (exp, act) in enumerate(zip(expected_lines, actual_lines), 1):
        if exp.strip() != act.strip():
            return False, f"line {idx}: expected {exp.strip()}, got {act.strip()}"

    return True, ""


def main():
    stems = sorted(
        (f.stem for f in TESTS_DIR.glob("*.in")), key=lambda s: int(s)
    )

    if not stems:
        print("No test cases found in tests/")
        return

    passed_count = 0
    for stem in stems:
        in_path = TESTS_DIR / f"{stem}.in"
        out_path = TESTS_DIR / f"{stem}.out"

        if not out_path.exists():
            print(f"Test {stem}: SKIP (no .out file)")
            continue

        passed, detail = run_test(in_path, out_path)
        if passed:
            passed_count += 1
            print(f"Test {stem}: PASS")
        else:
            print(f"Test {stem}: FAIL  ({detail})")

    total = len(stems)
    print(f"\n{passed_count}/{total} passed")


if __name__ == "__main__":
    main()
