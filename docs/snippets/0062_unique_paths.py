def uniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1

    dp = [[1] * n] * m

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


print(uniquePaths(m=3, n=7))  # 28
