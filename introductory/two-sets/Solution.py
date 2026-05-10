def print_list(my_list: list[str]) -> None:
    print(len(my_list))
    print(" ".join(my_list))


def construct_sets(i: int, j: int) -> tuple[list[str], list[str]]:
    set1: list[str] = []
    set2: list[str] = []
    add_first = True
    while i < j:
        if add_first:
            set1 += [str(i), str(j)]
            add_first = False
        else:
            set2 += [str(i), str(j)]
            add_first = True

        i += 1
        j -= 1
    return set1, set2


def solve(n: int) -> None:
    if n % 4 not in (0, 3):
        print("NO")
        return

    set1: list[str] = []
    set2: list[str] = []
    if n % 4 == 3:
        set1, set2 = construct_sets(1, n - 1)
        set2.append(str(n))

    else:
        set1, set2 = construct_sets(1, n)

    print("YES")
    print_list(set1)
    print_list(set2)


def main():
    n = int(input())
    solve(n)


if __name__ == "__main__":
    main()
