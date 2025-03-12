from typing import List


# DFS
def islandPerimeterDFS(grid: List[List[int]]) -> int:
    # TC: O(m * n)
    # SC: O(m * n)

    visited = set()
    m, n = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        if (r, c) in visited or grid[r][c] == 0:
            return 0
        visited.add((r, c))
        perimeter = 0

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr not in range(m) or nc not in range(n) or grid[nr][nc] == 0:
                perimeter += 1
            else:
                perimeter += dfs(nr, nc)

        return perimeter

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                return dfs(r, c)
    return 0


def islandPerimeter(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    perimeter = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeterDFS(grid))  # 16
print(islandPerimeter(grid))  # 16
