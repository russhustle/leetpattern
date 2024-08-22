from typing import List


def floodFill(
    image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:
    original = image[sr][sc]
    if original == color:
        return image

    def dfs(r, c):
        if (
            r < 0
            or c < 0
            or r >= len(image)
            or c >= len(image[0])
            or image[r][c] != original
        ):
            return None

        image[r][c] = color

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    dfs(sr, sc)

    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1

print(floodFill(image, sr, sc, 2))
# [[2, 2, 2],
#  [2, 2, 0],
#  [2, 0, 1]]
