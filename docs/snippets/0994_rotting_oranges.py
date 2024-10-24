from collections import deque
from typing import List


# BFS
def orangesRotting(grid: List[List[int]]) -> int:
    # 1. Init
    q = deque()
    time, fresh = 0, 0
    m, n = len(grid), len(grid[0])
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # 2. Make a queue of rotten oranges and count fresh oranges
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r, c])

    # 3. BFS
    while q and fresh > 0:
        size = len(q)

        for _ in range(size):
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                q.append([nr, nc])
                fresh -= 1
        time += 1

    return time if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(orangesRotting(grid))
