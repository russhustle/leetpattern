from collections import deque
from copy import deepcopy
from typing import List


# BFS
def numDistinctIslandsBFS(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    shapes = set()
    dirs = [[1, 0], [0, 1], [0, -1], [-1, 0]]

    def bfs(r, c):
        q = deque([(r, c)])
        shape = set()
        grid[r][c] = 0

        while q:
            row, col = q.popleft()
            shape.add((row - r, col - c))

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    grid[nr][nc] = 0

        return tuple(shape)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                shapes.add(bfs(i, j))

    return len(shapes)


# DFS
def numDistinctIslandsDFS(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    def dfs(r, c, org, shape):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
            return

        grid[r][c] = 0
        shape.add((r - org[0], c - org[1]))

        dfs(r - 1, c, org, shape)
        dfs(r + 1, c, org, shape)
        dfs(r, c - 1, org, shape)
        dfs(r, c + 1, org, shape)

    shapes = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                org = [i, j]
                shape = set()
                dfs(i, j, org, shape)
                shapes.add(tuple(shape))

    return len(shapes)


grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
print(numDistinctIslandsBFS(deepcopy(grid)))  # 3
print(numDistinctIslandsDFS(deepcopy(grid)))  # 3
