from collections import defaultdict
from typing import List


# Flood Fill
def largestIsland(grid: List[List[int]]) -> int:
    n = len(grid)
    areas = defaultdict(int)  # {index: area}
    index = 2
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(r, c, index):
        area = 1
        grid[r][c] = index
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                area += dfs(nr, nc, index)
        return area

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                areas[index] = dfs(r, c, index)
                index += 1

    if not areas:
        return 1

    res = max(areas.values())

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                connected = set()
                area = 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                        connected.add(grid[nr][nc])

                for island in connected:
                    area += areas[island]
                res = max(res, area)

    return res


grid = [[1, 0], [0, 1]]
print(largestIsland(grid))  # 3
