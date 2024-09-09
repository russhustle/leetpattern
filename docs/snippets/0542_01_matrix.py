from collections import deque
from typing import List


# BFS
def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = [[float("inf")] * n for _ in range(m)]
    q = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    return dist


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(updateMatrix(mat))
# [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
