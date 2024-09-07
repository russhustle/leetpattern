from collections import deque
from typing import List


# BFS
def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([(entrance[0], entrance[1], 0)])
    maze[entrance[0]][entrance[1]] = "+"

    while q:
        r, c, steps = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                if nr in [0, m - 1] or nc in [0, n - 1]:
                    return steps + 1
                q.append((nr, nc, steps + 1))
                maze[nr][nc] = "+"

    return -1


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
print(nearestExit(maze, entrance))  # 1
