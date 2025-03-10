from collections import deque
from typing import List


# BFS (Multi-Source BFS)
def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    m, n = len(isWater), len(isWater[0])
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    q = deque()

    for i in range(m):
        for j in range(n):
            if isWater[i][j]:
                q.append((i, j))
                isWater[i][j] = 0
            else:
                isWater[i][j] = -1

    height = 1
    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and isWater[nr][nc] == -1:
                    isWater[nr][nc] = height
                    q.append((nr, nc))
        height += 1

    return isWater


isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
print(highestPeak(isWater))
# [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
