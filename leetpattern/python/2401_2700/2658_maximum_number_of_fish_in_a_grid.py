from typing import List


# Grid DFS
def findMaxFish(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    res = 0

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 0
        val = grid[r][c]
        grid[r][c] = 0

        return (
            val + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        )

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                res = max(res, dfs(i, j))

    return res


grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
print(findMaxFish(grid))  # 7
