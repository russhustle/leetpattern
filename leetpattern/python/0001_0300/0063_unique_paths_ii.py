from functools import cache
from typing import List


class UniquePathsWithObstacles:
    def memoization(self, obstacleGrid: List[List[int]]) -> int:
        """
        Approach: DFS with Memoization
        Time complexity: O(mn).
        Space complexity: O(mn).
        """

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(m - 1, n - 1)

    def dp_2d(self, obstacleGrid: List[List[int]]) -> int:
        """
        Approach: 2D Dynamic Programming
        Time complexity: O(mn).
        Space complexity: O(mn).
        """
        # edge cases
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # init dp
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

        # update dp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

    def dp_1d(self, obstacleGrid: List[List[int]]) -> int:
        """
        Approach: 1D Dynamic Programming
        Time complexity: O(mn).
        Space complexity: O(n).
        """
        n = len(obstacleGrid[0])
        dp = [0] * (n + 1)
        dp[1] = 1

        for row in obstacleGrid:
            for j, x in enumerate(row):
                if x == 0:
                    dp[j + 1] += dp[j]
                else:
                    dp[j + 1] = 0
        return dp[n]


if __name__ == "__main__":
    solution = UniquePathsWithObstacles()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert solution.dp_2d(obstacleGrid) == 2
    assert solution.memoization(obstacleGrid) == 2
    assert solution.dp_1d(obstacleGrid) == 2
