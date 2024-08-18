from typing import List
from collections import deque
from copy import deepcopy


# DFS
def numIslandsDFS(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    def dfs(grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
            return None

        grid[r][c] = "0"

        dfs(grid, r + 1, c)
        dfs(grid, r - 1, c)
        dfs(grid, r, c + 1)
        dfs(grid, r, c - 1)

    islands = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                dfs(grid, r, c)
                islands += 1

    return islands


# BFS
def numIslandsBFS(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    def bfs(r, c):
        q = deque()
        visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (
                    r in range(ROWS)
                    and c in range(COLS)
                    and grid[r][c] == "1"
                    and (r, c) not in visit
                ):
                    q.append((r, c))
                    visit.add((r, c))

    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    islands = 0

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1

    return islands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

print(numIslandsDFS(deepcopy(grid)))  # 1
print(numIslandsBFS(deepcopy(grid)))  # 1
