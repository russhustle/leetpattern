def numDistinct(s: str, t: str) -> int:
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for _ in range((m + 1))]

    for i in range(m):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                # include and exclude s[i-1]
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]  # exclude s[i-1]

    return dp[-1][-1]


s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))  # 3
