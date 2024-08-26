from collections import deque
from typing import List


# 1. DFS
def floodFillDFS(
    image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:

    original = image[sr][sc]
    m, n = len(image), len(image[0])

    if original == color:
        return image

    def dfs(r, c):
        if r not in range(m) or c not in range(n) or image[r][c] != original:
            return None

        image[r][c] = color

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    dfs(sr, sc)

    return image


# 2. BFS
def floodFillBFS(
    image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:

    original = image[sr][sc]
    m, n = len(image), len(image[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    if original == color:
        return image

    q = deque([(sr, sc)])

    while q:
        row, col = q.popleft()
        image[row][col] = color

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if nr in range(m) and nc in range(n) and image[nr][nc] == original:
                q.append((nr, nc))

    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1

print(floodFillDFS(image, sr, sc, 2))
# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
print(floodFillBFS(image, sr, sc, 2))
# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
