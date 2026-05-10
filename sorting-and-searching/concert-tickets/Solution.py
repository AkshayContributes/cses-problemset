import sys


def next_available(tickets: list[int], target: int) -> int:
    i, j, ans = 0, len(tickets) - 1, -1
    while i <= j:
        mid = (i + j) // 2
        if tickets[mid] <= target:
            ans = mid
            i = mid + 1
        else:
            j = mid - 1
    return ans


def solve(tickets: list[int], requests: list[int]):
    tickets = sorted(tickets)
    output: list[str] = []
    for request in requests:
        idx = next_available(tickets, request)
        if idx == -1:
            output.append(str(idx))
            continue
        output.append(str(tickets[idx]))
        tickets.pop(idx)
    result = "\n".join(output)
    print(result)


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    tickets = list(map(int, data[2 : 2 + n]))
    requests = list(map(int, data[2 + n : 2 + n + m]))
    solve(tickets, requests)


if __name__ == "__main__":
    main()
