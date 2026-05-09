---
name: Python idiom nits to flag
description: Recurring Python style issues to call out in L5 reviews — list comprehensions wrapping iterables, range bound off-by-ones
type: feedback
---

When reviewing this candidate's Python solutions, flag these specific patterns:

1. `[i for i in range(...)]` — redundant list construction around an already-iterable `range`. Suggest splat directly: `print(*range(...))`.
2. Off-by-one on `range(a, b, step)` upper bounds, especially on parity-stride loops (`range(2, n, 2)` vs `range(2, n+1, 2)`).

**Why:** On the Permutations problem (2026-05-08 session), the candidate shipped both: range upper bounds were initially wrong and self-corrected mid-session, and the final solution still wrapped `range` in a list comprehension. These are micro-execution issues that lower a Strong Hire to a Hire on construction-style problems where algorithmic insight is small and bar shifts to coding crispness.

**How to apply:** On any Python solution, scan for `[x for x in <iterable>]` with no transformation and call it out. On any `range` with a non-1 step, mentally evaluate the last term and flag if it looks off. Don't let these slide as "minor" — in L5 loops they compound into a perception of imprecise coding.
