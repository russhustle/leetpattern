from collections import deque
from typing import List


# BFS
def maxDistance(grid: List[List[int]]) -> int:
    n = len(grid)
    res = -1
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    q = deque([[i, j] for i in range(n) for j in range(n) if grid[i][j] == 1])

    if len(q) == (n**2):
        return res

    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append([nr, nc])
        res += 1

    return res


grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
print(maxDistance(grid))  # 4
