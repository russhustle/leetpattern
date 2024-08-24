from collections import deque
from typing import List


# 1. DFS
def pacificAtlanticDFS(heights: List[List[int]]) -> List[List[int]]:
    m, n = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visited, prevHeight):
        if (
            (r, c) in visited
            or r < 0
            or c < 0
            or r == m
            or c == n
            or heights[r][c] < prevHeight
        ):
            return None

        visited.add((r, c))

        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

    for c in range(n):
        dfs(0, c, pac, heights[0][c])  # top
        dfs(m - 1, c, atl, heights[m - 1][c])  # bottom

    for r in range(m):
        dfs(r, 0, pac, heights[r][0])  # left
        dfs(r, n - 1, atl, heights[r][n - 1])  # right

    return list(pac & atl)


# 2. BFS
def pacificAtlanticBFS(heights: List[List[int]]) -> List[List[int]]:
    m, n = len(heights), len(heights[0])
    pac, atl = set(), set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r, c, visited):
        q = deque([(r, c)])
        visited.add((r, c))

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (
                    nr in range(m)
                    and nc in range(n)
                    and heights[nr][nc] >= heights[row][col]
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc))

    for c in range(n):
        bfs(0, c, pac)  # top
        bfs(m - 1, c, atl)  # bottom

    for r in range(m):
        bfs(r, 0, pac)  # left
        bfs(r, n - 1, atl)  # right

    return list(pac & atl)


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(pacificAtlanticDFS(heights))
# [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]
print(pacificAtlanticBFS(heights))
# [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]
