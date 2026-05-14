def solve(movies: list[list[int]]) -> int:
    count = 0
    movies = sorted(movies, key=lambda x: x[1])
    count = 0
    previous_end = 0
    for movie in movies:
        if movie[0] >= previous_end:
            count += 1
            previous_end = max(movie[1], previous_end)
    return count


def main():
    n = int(input())
    movies: list[list[int]] = []
    for _ in range(n):
        movie: list[int] = list(map(int, input().split()))
        movies.append(movie)
    print(solve(movies))


if __name__ == "__main__":
    main()
