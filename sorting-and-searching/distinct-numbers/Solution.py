def solve(arr: list[int]) -> int:
    return len(set(arr))


def main():
    _ = int(input())
    arr: list[int] = list(map(int, input().split()))
    print(solve(arr))


if __name__ == "__main__":
    main()
