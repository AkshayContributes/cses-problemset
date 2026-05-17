---
name: Candidate profile and trajectory
description: Running profile of the L5 candidate's strengths, recurring weaknesses, and per-problem signal ratings
type: project
---

Candidate is preparing for Google L5 with target 175/300 CSES problems by Nov 2026.

**Strengths observed:**
- Greedy and two-pointer pattern recognition (per CLAUDE.md and confirmed live).
- Clean final-state code structure: good function decomposition, early returns, idiomatic main guards.
- Self-corrects mid-session when bugs surface — listens to feedback and iterates.
- Correct algorithmic insight on construction problems (e.g., parity-interleave for Permutations).

**Recurring weaknesses to track:**
- First-pass execution: initial submissions often have off-by-one or control-flow fall-through bugs that get cleaned up across iterations. In a real L5 loop the first version needs to be closer to final.
- Python micro-idioms: redundant list comprehensions around iterables, occasional unused imports, dead defensive calls (e.g., `.strip()` on `" ".join(...)` output), `+= [a, b]` instead of `.append`.
- **Debug artifacts in `__main__` block** — has shipped `solve(n=7)` instead of calling `main()`, leaving a hardcoded test driver as the entry point. This is a category killer in real interviews; CLAUDE.md already flags this pattern as a known pitfall.
- Storing `str` values in working data structures rather than ints (defers conversion-at-output-time).

**Signal log:**
- 2026-05-08 — Permutations (introductory): **Hire**. Final code correct/optimal; lost Strong Hire on first-pass range bounds + redundant list comp on final.
- 2026-05-09 — Number Spiral (introductory): **Hire**. Correct on first pass, O(1) per query, clean. Gaps: `print()` in 10^5 loop (no buffered I/O reflex yet), redundant `list(map(...))`. Trajectory note: improvement on first-pass correctness vs Permutations.
- 2026-05-09 — Two Sets (introductory): **Hire** (final). Algorithm correct/optimal (n%4 parity guard + symmetric pairing) with strong constructive-proof reasoning in Problem.md. Initial submission shipped `solve(n=7)` as entry point and dead `.strip()` after `" ".join` — both cleaned up after one feedback round. Remaining style nits (str-in-list, `+= [a, b]` over `.append`/`.extend`) are non-blocking. Same trajectory pattern: final state is L5-clean, first pass needs work.
- 2026-05-10 — Sum of Two Values (sorting-and-searching): **Hire**. Optimal hash-map complement on first pass, all edge cases (self-index, duplicate-pair, no-solution, n=1) handled correctly. First-pass cleanliness clearly improved: no debug-driver-as-entry, no unused imports, type hints present. Single blocker for Strong Hire: dead value-ordering branch (`if k - num > num`) that adds code without changing behavior AND would not even sort by position if it were needed. Other nits: `my_map` naming, unused `n` parameter, renamed problem's `x` to `k`. New recurring weakness candidate: **adding unjustified defensive code** ("what if the judge wants sorted output") without verifying it's needed or that it does what it appears to do.
- 2026-05-10 — Missing Number (introductory): **Hire**. Closed-form `n(n+1)/2 - sum(nums)` on first pass, clean `solve`/`main` split with type hints, no artifacts. Problem is too easy to differentiate at L5 — code is essentially perfect for the bar it sets. Path to Strong Hire here is verbal: volunteer XOR alternative for overflow safety, mention O(1)-space streaming variant, name the C++/Java overflow caveat unprompted. Minor naming nit: `sum_of_n` reads as "sum of variable n" rather than "sum of 1..n". Trajectory note: first-pass quality continues to climb — three consecutive problems with no debug-driver-as-entry regressions.
- 2026-05-14 — Sum of Three Values (sorting-and-searching): **No Hire** (regression). Algorithm is canonical sort + fix-i + two-pointer with index preservation via `(value, original_index)` tuples, complexity O(n²) optimal. **Wrong-Answer bug:** `print("IMPOSSIBLE")` placed inside the outer `for i` loop under `if not found`, so it prints up to n times instead of once. A single dry-run on a no-solution input would have caught it. Also re-triggered the explicitly-flagged `sum`-shadowing builtin weakness from the review prompt. Breaks the four-problem Hire streak. Fix is trivial (return on success, single IMPOSSIBLE after the loop, drop the flag) but the signal is: candidate has no pre-submit dry-run discipline yet. New pattern: control-flow placement of fallback/IMPOSSIBLE-branch prints when using a found-flag idiom — strong recommendation is to teach `return`-on-success / `else`-clause-on-for-loop idioms.

**How to apply:** When reviewing future solutions, compare against this trajectory. Push hard on first-pass quality — that's the gap between Hire and Strong Hire for this candidate. Celebrate iteration wins but name the cost of needing them in a real interview. Newer focus area: Python performance idioms for high-t problems (buffered stdout, batched stdin). Always grep for the `__main__` block specifically — debug-driver-as-entry-point has happened more than once and is a Hire→No-Hire downgrade by itself. Scan targets: (1) dead/unmotivated branches — "what does this conditional buy me?"; (2) **fallback prints inside loops when a `found` flag is in play** — verify the print runs once, not per-iteration; (3) builtin shadows (`sum`, `min`, `max`, `list`, `id`, `input`) in any local scope.
