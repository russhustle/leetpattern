from typing import List


# DFS
def maxMovesDFS(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    res = 0

    def dfs(r, c):
        nonlocal res
        res = max(res, c)
        if res == n - 1:
            return

        for k in r - 1, r, r + 1:
            if 0 <= k < m and grid[k][c + 1] > grid[r][c]:
                dfs(k, c + 1)
        grid[r][c] = 0

    for i in range(m):
        dfs(i, 0)

    return res


grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
print(maxMovesDFS(grid))  # 3
