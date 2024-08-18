from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    ROWS, COLS = len(grid), len(grid[0])
    visit = set()

    def dfs(r: int, c: int) -> int:
        if (
            r < 0
            or c < 0
            or r == ROWS
            or c == COLS
            or grid[r][c] == 0
            or (r, c) in visit
        ):
            return 0

        visit.add((r, c))
        return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

    area = 0
    for r in range(ROWS):
        for c in range(COLS):
            area = max(area, dfs(r, c))

    return area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
print(maxAreaOfIsland(grid))  # 6
