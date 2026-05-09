def solve(n: int) -> None:
    if n == 1:
        print(1)
        return

    if n <= 3:
        print("NO SOLUTION")
        return

    print([i for i in range(2, n + 1, 2)] + [i for i in range(1, n + 1, 2)])


def main():
    n = int(input().strip())
    solve(n)


if __name__ == "__main__":
    main()
