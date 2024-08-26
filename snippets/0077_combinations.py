import itertools
from typing import List


# 1. Backtracking
def combine(n: int, k: int) -> List[List[int]]:
    path = []
    result = []

    def backtracking(start):
        if len(path) == k:
            result.append(path[:])
            return None

        for i in range(start, n + 1):
            path.append(i)
            backtracking(i + 1)
            path.pop()

    backtracking(start=1)

    return result


# 2. Itertools
def combineItertools(n: int, k: int) -> List[List[int]]:
    path = itertools.combinations(range(1, n + 1), k)
    return path


print(combine(4, 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(list(combineItertools(4, 2)))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
