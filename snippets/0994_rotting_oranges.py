from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    q = deque()
    time, fresh = 0, 0
    m, n = len(grid), len(grid[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r, c])

    while q and fresh > 0:
        for _ in range(len(q)):
            row, col = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr in range(m) and nc in range(n) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh -= 1
        time += 1

    return time if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(orangesRotting(grid))
