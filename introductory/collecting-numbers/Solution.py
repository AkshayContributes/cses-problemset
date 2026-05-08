def main():
    n = int(input())
    arr = list(map(int, input().split()))

    pos = [0] * (n + 2)
    for i, x in enumerate(arr):
        pos[x] = i

    passes = 1
    for x in range(1, n):
        if pos[x + 1] < pos[x]:
            passes += 1

    print(passes)


if __name__ == "__main__":
    main()
