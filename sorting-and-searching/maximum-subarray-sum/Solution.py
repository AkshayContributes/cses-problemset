def solve(n: int, arr: list[int]) -> int:
    sum, max_sum = 0, -100000000000
    for _, item in enumerate(arr):
        sum += item
        max_sum = max(sum, max_sum)
        sum = max(0, sum)
    return int(max_sum)


def main():
    n = int(input())
    arr: list[int] = list(map(int, input().split()))
    print(solve(n, arr))


if __name__ == "__main__":
    main()
