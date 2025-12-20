from typing import List
from functools import cache


class Solution:
    # Recursive
    def minimumTotalRecursive(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @cache
        def dfs(i, j):
            if i == n - 1:
                return triangle[i][j]
            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]

        return dfs(0, 0)

    # Iterative
    def minimumTotalIterative(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


if __name__ == "__main__":
    solution = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert solution.minimumTotalRecursive(triangle) == 11
    assert solution.minimumTotalIterative(triangle) == 11
