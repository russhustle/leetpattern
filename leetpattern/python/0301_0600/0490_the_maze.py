from collections import deque
from typing import List


# BFS
def hasPathBFS(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    m, n = len(maze), len(maze[0])
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = deque([start])
    maze[start[0]][start[1]] = -1

    while q:
        r, c = q.popleft()
        if [r, c] == destination:
            return True

        for dr, dc in dirs:
            nr, nc = r, c

            while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] != 1:
                nr += dr
                nc += dc

            if maze[nr][nc] != -1:
                q.append([nr, nc])
                maze[nr][nc] = -1

    return False


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
start = [0, 4]
destination = [4, 4]
print(hasPathBFS(maze, start, destination))  # True
