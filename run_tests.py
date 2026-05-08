import subprocess
import sys
from pathlib import Path


def run_test(solution: Path, in_path: Path, out_path: Path) -> tuple[bool, str]:
    result = subprocess.run(
        [sys.executable, str(solution)],
        input=in_path.read_text(),
        capture_output=True,
        text=True,
    )
    expected_lines = out_path.read_text().strip().splitlines()
    actual_lines = result.stdout.strip().splitlines()

    if len(actual_lines) != len(expected_lines):
        return False, f"expected {len(expected_lines)} lines, got {len(actual_lines)}"

    for idx, (exp, act) in enumerate(zip(expected_lines, actual_lines), 1):
        if exp.strip() != act.strip():
            return False, f"line {idx}: expected {exp.strip()}, got {act.strip()}"

    return True, ""


def main():
    if len(sys.argv) > 1:
        problem_dir = Path(sys.argv[1])
    else:
        problem_dir = Path.cwd()

    tests_dir = problem_dir / "tests"
    solution = problem_dir / "Solution.py"

    if not solution.exists():
        print(f"No Solution.py found in {problem_dir}")
        sys.exit(1)

    if not tests_dir.exists():
        print(f"No tests/ directory found in {problem_dir}")
        sys.exit(1)

    stems = sorted((f.stem for f in tests_dir.glob("*.in")), key=lambda s: int(s))

    if not stems:
        print("No test cases found in tests/")
        return

    passed_count = 0
    for stem in stems:
        in_path = tests_dir / f"{stem}.in"
        out_path = tests_dir / f"{stem}.out"

        if not out_path.exists():
            print(f"Test {stem}: SKIP (no .out file)")
            continue

        passed, detail = run_test(solution, in_path, out_path)
        if passed:
            passed_count += 1
            print(f"Test {stem}: PASS")
        else:
            print(f"Test {stem}: FAIL  ({detail})")

    print(f"\n{passed_count}/{len(stems)} passed")


if __name__ == "__main__":
    main()
