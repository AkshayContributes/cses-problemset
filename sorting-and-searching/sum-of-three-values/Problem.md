# Sum of Three Values

Given an array of n integers, find three values at distinct positions whose sum equals x.

## Input

The first line has two integers n and x: the array size and the target sum.

The second line has n integers $a_1, a_2, \ldots, a_n$: the array values.

## Output

Print three indices (1-indexed) of values that sum to x. If multiple solutions exist, any valid answer is accepted. Print `IMPOSSIBLE` if no solution exists.

## Constraints

- $1 \leq n \leq 5000$
- $1 \leq x, a_i \leq 10^9$

## Example

**Input:**
```
4 8
2 7 5 1
```

**Output:**
```
1 3 4
```
