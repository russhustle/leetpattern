from collections import deque
from typing import List


# DFS
def floodFillDFS(
    image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:

    org = image[sr][sc]
    m, n = len(image), len(image[0])

    if org == color:
        return image

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != org:
            return None

        image[r][c] = color

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    dfs(sr, sc)

    return image


# BFS
def floodFillBFS(
    image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:

    org = image[sr][sc]
    m, n = len(image), len(image[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    if org == color:
        return image

    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        image[r][c] = color

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == org:
                q.append((nr, nc))

    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1

print(floodFillDFS(image, sr, sc, 2))
# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
print(floodFillBFS(image, sr, sc, 2))
# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
