"""
-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid with obstacles.

![63](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)
"""

from typing import List


# DP - 2D
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = 1
        else:
            break

    for j in range(n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = 1
        else:
            break

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(obstacleGrid))  # 2
# [[1, 1, 1],
#  [1, 0, 1],
#  [1, 1, 2]]
