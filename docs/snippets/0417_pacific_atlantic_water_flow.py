from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prevHeight):
        if (
            (r, c) in visit
            or r < 0
            or c < 0
            or r == ROWS
            or c == COLS
            or heights[r][c] < prevHeight
        ):
            return None

        visit.add((r, c))

        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])  # top
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # bottom

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])  # left
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # right

    return list(pac & atl)


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(pacificAtlantic(heights))
# [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]
