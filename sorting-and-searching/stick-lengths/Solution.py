def solve(n: int, arr: list[int]) -> int:
    arr = sorted(arr)
    target = arr[n // 2]
    cost = 0
    for i in range(n):
        cost += abs(target - arr[i])
    return cost


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))


if __name__ == "__main__":
    main()
