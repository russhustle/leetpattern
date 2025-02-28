from typing import List


# Grid DFS
def colorBorder(
    grid: List[List[int]], row: int, col: int, color: int
) -> List[List[int]]:

    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    m, n = len(grid), len(grid[0])
    org = grid[row][col]
    visited = set()
    borders = set()

    def dfs(r, c):
        if (r, c) in visited:
            return

        visited.add((r, c))

        is_border = False
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == org:
                    dfs(nr, nc)
                elif (nr, nc) not in visited:
                    is_border = True
            else:
                is_border = True

        if is_border:
            borders.add((r, c))

    dfs(row, col)

    for r, c in borders:
        grid[r][c] = color

    return grid


grid = [[1, 2, 2], [2, 3, 2]]
row = 0
col = 1
color = 3
print(colorBorder(grid, row, col, color))  # [[1, 3, 3], [2, 3, 3]]
