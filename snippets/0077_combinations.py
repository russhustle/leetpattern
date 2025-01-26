import itertools
from typing import List


# Backtracking
def combine(n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return None

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])

    return res


# itertools
def combineItertools(n: int, k: int) -> List[List[int]]:
    path = itertools.combinations(range(1, n + 1), k)
    return path


print(combine(4, 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(list(combineItertools(4, 2)))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
