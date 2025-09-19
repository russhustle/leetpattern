from collections import deque
from functools import cache
from typing import List


# BFS - Topological Sort
def longestIncreasingPathBFS(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Calculate indegrees and initialize queue in one pass
    indegree = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[i][j]:
                    indegree[nr][nc] += 1

    # Start with cells that have no smaller neighbors
    queue = deque((i, j) for i in range(m) for j in range(n) if indegree[i][j] == 0)

    res = 0
    while queue:
        res += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    indegree[nr][nc] -= 1
                    if indegree[nr][nc] == 0:
                        queue.append((nr, nc))

    return res


# DP - 2D
def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    @cache
    def dfs(r, c):
        path = 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                path = max(path, dfs(nr, nc) + 1)
        return path

    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))

    return res


if __name__ == "__main__":
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    assert longestIncreasingPath(matrix) == 4
    assert longestIncreasingPathBFS(matrix) == 4
