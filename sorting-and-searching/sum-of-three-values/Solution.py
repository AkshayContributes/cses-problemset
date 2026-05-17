def solve(n: int, arr: list[int], x: int) -> None:
    paired_arr = [(item, i + 1) for i, item in enumerate(arr)]
    paired_arr = sorted(paired_arr)
    for i in range(n):
        j, k = i + 1, n - 1
        while j < k:
            total = paired_arr[j][0] + paired_arr[k][0] + paired_arr[i][0]
            if total > x:
                k -= 1
            elif total < x:
                j += 1
            else:
                print(paired_arr[i][1], paired_arr[j][1], paired_arr[k][1])
                return
    print("IMPOSSIBLE")


def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    solve(n, arr, x)


if __name__ == "__main__":
    main()
