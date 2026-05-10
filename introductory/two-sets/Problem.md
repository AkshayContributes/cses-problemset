# Two Sets

Your task is to divide the numbers $1, 2, \dots, n$ into two sets of equal sum.

## Input

The only input line contains an integer $n$.

## Output

Print "YES" if the division is possible, and "NO" otherwise.

If the division is possible, print the sizes of the sets and the elements of each set.

## Constraints

$$1 \le n \le 10^6$$

## Example

**Input:**
```
7
```

**Output:**
```
YES
4
1 2 4 7
3
3 5 6
```

1 2 3 4 5 6 7

n = 1
sum = 1 NP

n = 2
sum = 3 NP

n = 3
sum = 6 YES - 1, 2 and 3

n = 4
sum = 10 - 2 3 and 1, 4

n = 5 
sum = 15 np

n = 6
sum = 21 np
1 2 3 4 5 6 -> (1, 6) (2, 5) 


n = 7
sum = 28 [1, 2, 3, 4, 5, 6, 7] -> 

n = 8
sum = 36 [1 2 3 4 5 6 7, 8] -> [1, 8] [3, 6] | [2, 7], [4, 5]

n = 9
n = 1 2 3 4 5 6 7 8 9


n = 10
sum = 55

n = 11
sum = 66 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  -> (1, 11) (3, 9) | (2, 10), 

  ┌─────────┬──────────────┬──────────────┬───────────┐
  │ n mod 4 │ S = n(n+1)/2 │ Even or odd? │ Feasible? │
  ├─────────┼──────────────┼──────────────┼───────────┤
  │ 0       │ 10           │  even        │ yes       │                                
  ├─────────┼──────────────┼──────────────┼───────────┤
  │ 1       │ 15           │ odd          │ no        │
  ├─────────┼──────────────┼──────────────┼───────────┤
  │ 2       │ 21           │ odd          │ no        │
  ├─────────┼──────────────┼──────────────┼───────────┤
  │ 3       │ 28           │ even         │ yes       │
  └─────────┴──────────────┴──────────────┴───────────┘