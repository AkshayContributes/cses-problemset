import sys
from typing import List


def solve(n: int, m: int, k: int, applicants: List[int], apartments: List[int]) -> int:
    applicants = sorted(applicants)
    apartments = sorted(apartments)
    count = 0
    apt_index, apl_index = 0, 0
    while apl_index < len(applicants) and apt_index < len(apartments):
        min_size, max_size = applicants[apl_index] - k, applicants[apl_index] + k
        # print(min_size, max_size, apartments[apt_index])
        while apt_index < len(apartments) and apartments[apt_index] < min_size:
            apt_index += 1

        if (
            apt_index < len(apartments)
            and min_size <= apartments[apt_index] <= max_size
        ):
            # print(min_size, max_size, apartments[apt_index])
            count += 1
            apt_index += 1
        apl_index += 1
    return count


def main():
    n, m, k = list(map(int, input().split()))
    applicants = list(map(int, input().split()))
    apartments = list(map(int, input().split()))
    print(solve(n, m, k, applicants, apartments))


if __name__ == "__main__":
    main()
