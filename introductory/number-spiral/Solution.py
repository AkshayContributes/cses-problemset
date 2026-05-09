import sys


def solve(r: int, c: int) -> int:
    max_cord = max(r, c)
    target = max_cord * max_cord
    if max_cord % 2 == 0:
        target -= c - 1
        if max_cord == c:
            target -= max_cord - r
    else:
        target -= r - 1
        if max_cord == r:
            target -= max_cord - c

    return target


def main():
    n = int(input().strip())
    res: list[str] = []
    for _ in range(n):
        r, c = map(int, input().split())
        num = solve(r, c)
        res.append(str(num))
    sys.stdout.write("\n".join(res) + "\n")


if __name__ == "__main__":
    main()
