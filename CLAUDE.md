# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running Tests

From the repo root, pass the problem directory as an argument:

```bash
python3 run_tests.py introductory/collecting-numbers
python3 run_tests.py sorting-and-searching/apartments
```

Or from inside a problem directory:

```bash
python3 ../../run_tests.py
```

## Formatting

```bash
ruff format .
```

VSCode is configured to auto-format Python on save via the `charliermarsh.ruff` extension (`.vscode/settings.json`).

## Structure

Each problem lives in `<category>/<problem-name>/` and contains:
- `Solution.py` — reads from stdin, writes to stdout
- `Problem.md` — problem statement
- `tests/` — `N.in` / `N.out` pairs (gitignored)

Solutions use `input()` (or `sys.stdin.readline` aliased to `input` for performance) and `print()` directly — no file I/O.

## Common Pitfalls

- **`input.split()` vs `input().split()`** — recurring bug; always call `input()` as a function before chaining `.split()`.
- **Debug artifacts** — remove `print`, `breakpoint`, and commented-out test blocks before considering a solution done.
- **Unused imports** — check for leftover `import sys` when `sys.stdin.readline` is not used.

## Code Review Role

When reviewing solutions, act as a Google L5 interviewer. For each solution evaluate:
- Correctness and edge case handling
- Time and space complexity (state it explicitly)
- Code cleanliness (no debug artifacts, unused imports, leftover comments)
- Whether the approach is optimal or if a better one exists

## Preparation Context

This repo is Google L5 interview prep. Target: **175 / 300 problems in 6 months** (May–Nov), then tackle the remainder after. Current progress: **4 / 175**.

Skip Geometry (low L5 relevance). All other categories count toward the target.

Month-by-month plan:
| Month | Focus |
|-------|-------|
| May | Finish Sorting & Searching + Introductory |
| Jun | Dynamic Programming (all 19) |
| Jul | Graph Algorithms Part 1 — BFS/DFS, topological sort, SCC |
| Aug | Graph Algorithms Part 2 — Dijkstra, MST + Range Queries start |
| Sep | Range Queries finish + Tree Algorithms |
| Oct | Mathematics (~20) + String Algorithms (~10) |
| Nov | Mock interviews + weak spots + targeted hard problems |

Priority order based on L5 interview frequency:
1. Dynamic Programming
2. Graph Algorithms (BFS/DFS, Dijkstra, Bellman-Ford)
3. Range Queries (prefix sums → segment trees → BITs)
4. Tree Algorithms (tree DP, LCA)

Current strengths: greedy algorithms, two-pointer pattern, optimal complexity on easy problems.
