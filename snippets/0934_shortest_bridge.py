from collections import deque
from typing import List


# BFS + DFS; Coloring
def shortestBridge(grid: List[List[int]]) -> int:
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c, queue):
        grid[r][c] = 2
        queue.append((r, c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr in range(n) and nc in range(n) and grid[nr][nc] == 1:
                dfs(nr, nc, queue)

    q = deque()
    found = False
    for r in range(n):
        if found:
            break
        for c in range(n):
            if grid[r][c] == 1:
                dfs(r, c, q)
                found = True
                break

    steps = 0
    while q:
        m = len(q)
        for _ in range(m):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(n) and nc in range(n):
                    if grid[nr][nc] == 1:
                        return steps
                    elif grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        steps += 1

    return -1


grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
print(shortestBridge(grid))  # 1
