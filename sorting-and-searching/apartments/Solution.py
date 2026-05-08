import sys
from typing import List


def solve(n: int, m: int, k: int, applicants: List[int], apartments: List[int]) -> int:
    #45 60, 60, 80
    applicants = sorted(applicants)
    #30 60 75
    apartments = sorted(apartments)
    count = 0
    apt_index, apl_index = 0, 0
    while apl_index < len(applicants) and apt_index < len(apartments):
        min_size, max_size = applicants[apl_index]-k, applicants[apl_index]+k
        # print(min_size, max_size, apartments[apt_index])
        while apt_index < len(apartments) and apartments[apt_index] < min_size:
            apt_index += 1
            
        if apt_index < len(apartments) and min_size <= apartments[apt_index] <= max_size:
            # print(min_size, max_size, apartments[apt_index])
            count += 1
            apt_index += 1
        apl_index += 1
    return count
        

            
        


def main():
    with open("tests.txt", "r") as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]

    i, test_num = 0, 1
    while i < len(lines):
        n, m, k = map(int, lines[i].split()); i += 1
        applicants = list(map(int, lines[i].split())); i += 1
        apartments = list(map(int, lines[i].split())); i += 1
        expected = int(lines[i]); i += 1
        result = solve(n, m, k, applicants, apartments)
        status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
        print(f"Test {test_num}: {status}")
        test_num += 1


if __name__ == "__main__":
    main()
