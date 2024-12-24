from typing import List


# DP - 2D
def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c):
        if dp[r][c]:
            return dp[r][c]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], dfs(nr, nc))
        dp[r][c] += 1
        return dp[r][c]

    res = float("-inf")
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))

    return res


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(longestIncreasingPath(matrix))  # 4
