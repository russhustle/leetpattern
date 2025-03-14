from collections import deque
from typing import List


# BFS
def orangesRotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    fresh = 0
    q = deque()
    dirs = [[1, 0], [0, 1], [0, -1], [-1, 0]]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append([i, j])
            elif grid[i][j] == 1:
                fresh += 1
    res = 0

    while q and fresh > 0:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    q.append([nr, nc])
                    grid[nr][nc] = 2
                    fresh -= 1
        res += 1

    return res if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
assert orangesRotting(grid) == 4
