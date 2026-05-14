def solve(events: list[list[int]]) -> int:
    events = sorted(events, key=lambda x: x[0])
    max_customers = 0
    customers = 0
    for event in events:
        customers += event[1]
        max_customers = max(customers, max_customers)
    return max_customers


def main():
    n = int(input())
    events: list[list[int]] = []
    for _ in range(n):
        event: list[int] = list(map(int, input().split()))
        events.append([event[0], 1])
        events.append([event[1], -1])
    print(solve(events))


if __name__ == "__main__":
    main()
