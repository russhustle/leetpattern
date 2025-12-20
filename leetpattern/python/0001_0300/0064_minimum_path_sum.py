from functools import cache
from typing import List


# Iterative
def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # init
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i - 1][0]
    for j in range(1, n):
        dp[0][j] = grid[0][j] + dp[0][j - 1]

    # update
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


# Recursive
def minPathSumDFS(grid: List[List[int]]) -> int:
    INF = 10**18

    @cache
    def dfs(i, j):
        if i < 0 or j < 0:
            return INF
        if i == 0 and j == 0:
            return grid[i][j]
        return min(dfs(i, j - 1), dfs(i - 1, j)) + grid[i][j]

    return dfs(len(grid) - 1, len(grid[0]) - 1)


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(grid))  # 7
print(minPathSumDFS(grid))  # 7
