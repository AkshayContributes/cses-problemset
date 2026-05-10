def solve(nums: list[int], k: int) -> None:
    my_map: dict[int, int] = {}
    for i, num in enumerate(nums):
        if k - num in my_map:
            if k - num > num:
                print(i + 1, my_map[k - num] + 1)
            else:
                print(my_map[k - num] + 1, i + 1)
            return
        my_map[num] = i
    print("IMPOSSIBLE")


def main():
    _, k = map(int, input().split())
    nums = list(map(int, input().split()))
    solve(nums, k)


if __name__ == "__main__":
    main()
