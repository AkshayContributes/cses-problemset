# Sum of Two Values

You are given an array of $n$ integers, and your task is to find two values at distinct positions whose sum equals a target value $x$.

## Input

The first line contains two integers $n$ and $x$: the array size and target sum.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$: the array values.

## Output

Print two integers — the positions of the values that sum to $x$. If multiple solutions exist, any valid answer is acceptable. If no solution exists, print `IMPOSSIBLE`.

## Constraints

$$1 \le n \le 2 \cdot 10^5$$
$$1 \le x, a_i \le 10^9$$

## Example

**Input:**
```
4 8
2 7 5 1
```

**Output:**
```
2 4
```
