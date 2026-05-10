def solve(n: int, nums: list[int]) -> int:
    sum_of_n = n * (n + 1) // 2
    sum_of_nums = sum(nums)
    return sum_of_n - sum_of_nums


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(n, nums))


if __name__ == "__main__":
    main()
