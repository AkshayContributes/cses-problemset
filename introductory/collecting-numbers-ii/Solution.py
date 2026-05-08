from typing import List


def is_descent(item: int, pos: List[int], n: int) -> bool:
    if item < 1 or item >= n:
        return False
    return pos[item] > pos[item + 1]


def main():
    n, swaps = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    pos = [0] * (n + 2)
    for i, x in enumerate(arr):
        pos[x] = i

    descents = 0
    for x in range(1, n):
        if pos[x + 1] < pos[x]:
            descents += 1

    # breakpoint()
    for _ in range(swaps):
        i, j = list(map(int, input().split()))
        a, b = arr[i - 1], arr[j - 1]
        bound_set = {a - 1, a, b - 1, b}
        for item in bound_set:
            if is_descent(item, pos, n):
                descents -= 1

        arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]
        pos[a], pos[b] = pos[b], pos[a]
        for item in bound_set:
            if is_descent(item, pos, n):
                descents += 1

        print(descents + 1)


if __name__ == "__main__":
    main()
