from typing import List


def solve(n: int, max_wt: int, child_wts: List[int]) -> int:
    child_wts = sorted(child_wts)
    reqd_gondolas = 0
    i, j = 0, n - 1
    while i < j:
        if child_wts[i] + child_wts[j] <= max_wt:
            i += 1
            j -= 1
        else:
            j -= 1
        reqd_gondolas += 1
    return reqd_gondolas + 1 if i == j else reqd_gondolas


def main():
    n, max_wt = list(map(int, input().split()))
    child_wts = list(map(int, input().split()))
    print(solve(n, max_wt, child_wts))


if __name__ == "__main__":
    main()
