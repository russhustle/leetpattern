from typing import List


# DFS
def closedIsland(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (
            r not in range(m)
            or c not in range(n)
            or grid[r][c] == 1
            or (r, c) in visited
        ):
            return

        grid[r][c] = 1
        visited.add((r, c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if (
                (r in [0, m - 1] or c in [0, n - 1])
                and grid[r][c] == 0
                and (r, c) not in visited
            ):
                dfs(r, c)

    island = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 0 and (r, c) not in visited:
                island += 1
                dfs(r, c)

    return island


grid = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
]
print(closedIsland(grid))  # 2
