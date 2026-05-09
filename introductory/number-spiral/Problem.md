# Number Spiral

A number spiral is an infinite grid whose upper-left square has number 1. The spiral fills the grid as shown below:

```
1  2  9  10 25
4  3  8  11 24
5  6  7  12 23
16 15 14 13 22
17 18 19 20 21
```

Your task is to find out the number at row $y$, column $x$.

## Input

The first line contains an integer $t$: the number of test cases.

After this, there are $t$ lines each containing two integers $y$ and $x$.

## Output

For each test case, print the number at row $y$, column $x$.

## Constraints

$$1 \le t \le 10^5$$
$$1 \le y, x \le 10^9$$

## Example

**Input:**
```
3
2 3
1 1
4 2
```

**Output:**
```
8
1
15
```
