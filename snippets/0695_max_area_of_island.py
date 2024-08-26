from collections import deque
from typing import List


# 1. DFS
def maxAreaOfIslandDFS(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    visited = set()
    area = 0

    def dfs(r, c):
        if (
            r not in range(m)
            or c not in range(n)
            or grid[r][c] == 0
            or (r, c) in visited
        ):
            return 0

        visited.add((r, c))
        return (
            1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        )

    for r in range(m):
        for c in range(n):
            area = max(area, dfs(r, c))

    return area


# 2. BFS
def maxAreaOfIslandBFS1(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    area = 0

    def bfs(r, c):
        q = deque([(r, c)])
        subArea = 0

        while q:
            row, col = q.popleft()
            subArea += 1

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (
                    nr in range(m)
                    and nc in range(n)
                    and grid[nr][nc] == 1
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc))

        return subArea

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                area = max(area, bfs(r, c))

    return area


# 3. BFS + Grid
def numIslandsBFS2(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    area = 0

    def bfs(r, c):
        q = deque([(r, c)])
        subArea = 0

        while q:
            row, col = q.popleft()
            subArea += 1

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if nr in range(m) and nc in range(n) and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    grid[nr][nc] = 0

        return subArea

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                grid[r][c] = 0
                area = max(area, bfs(r, c))

    return area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
print(maxAreaOfIslandDFS(grid))  # 6
print(maxAreaOfIslandBFS1(grid))  # 6
print(numIslandsBFS2(grid))  # 6
