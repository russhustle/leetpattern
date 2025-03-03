from typing import List


# DFS
def countSubIslandsDFS(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    m, n = len(grid2), len(grid2[0])
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(r, c, valid):
        grid2[r][c] = 0
        if grid1[r][c] == 0:
            valid = False
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
                valid = dfs(nr, nc, valid)
        return valid

    res = 0

    for i in range(m):
        for j in range(n):
            if grid2[i][j] == 1:
                if dfs(i, j, True):
                    res += 1

    return res


grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
]
print(countSubIslandsDFS(grid1, grid2))  # 3
