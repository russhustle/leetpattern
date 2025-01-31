from collections import deque
from typing import List


# BFS
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1
    if n == 1:
        return 1

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    q = deque([(0, 0, 1)])  # (row, column, distance)
    grid[0][0] = 1

    while q:
        r, c, d = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                if nr == nc == n - 1:
                    return d + 1
                q.append((nr, nc, d + 1))
                grid[nr][nc] = 1

    return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(grid))  # 4
