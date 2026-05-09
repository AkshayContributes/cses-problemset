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

**How to apply:** When reviewing future solutions, compare against this trajectory. Push hard on first-pass quality — that's the gap between Hire and Strong Hire for this candidate. Celebrate iteration wins but name the cost of needing them in a real interview. Newer focus area: Python performance idioms for high-t problems (buffered stdout, batched stdin). Always grep for the `__main__` block specifically — debug-driver-as-entry-point has happened more than once and is a Hire→No-Hire downgrade by itself.
