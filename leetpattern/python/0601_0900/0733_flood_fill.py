"""
- Replace all the pixels of the same color starting from the given pixel.
- In other words, find the connected component of the starting pixel and change the color of all the pixels in that component.
- Edge cases: If the starting pixel is already the target color, return the image as it is.
- **Flood Fill** is essentially a graph traversal algorithm (like BFS or DFS) applied to matrices (2D grids).
  It checks adjacent cells (up, down, left, right) of a starting point to determine whether they belong to the same region.
  Typically, it involves modifying or marking the cells that belong to the same connected component.

![flood_fill](../../assets/flood_fill_example.png)

![733](../../assets/0733.jpg)

|  1  |   1   |  1  |
| :-: | :---: | :-: |
|  1  | ==1== |  0  |
|  1  |   0   |  1  |

|  1  |   1   |  1  |
| :-: | :---: | :-: |
|  1  | ==2== |  0  |
|  1  |   0   |  1  |

|   1   | ==2== |  1  |
| :---: | :---: | :-: |
| ==2== | ==2== |  0  |
|   1   |   0   |  1  |

| ==2== | ==2== | ==2== |
| :---: | :---: | :---: |
| ==2== | ==2== |   0   |
| ==2== |   0   |   1   |
"""

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
