import itertools
from typing import List


# 1. Backtracking
def combinationSum3(k: int, n: int) -> List[List[int]]:
    path, result = [], []

    def backtracking(start):
        if len(path) == k and sum(path) == n:
            result.append(path[:])
            return

        for i in range(start, 10):
            path.append(i)
            backtracking(i + 1)
            path.pop()

    backtracking(1)

    return result


# 2. Itertools
def combinationSum3Itertools(k: int, n: int) -> List[List[int]]:
    combinations = itertools.combinations(range(1, 10), k)
    result = []

    for i in combinations:
        if sum(i) == n:
            result.append(i)

    return result


print(combinationSum3(3, 7))  # [[1, 2, 4]]
print(combinationSum3Itertools(3, 7))  # [(1, 2, 4)]
