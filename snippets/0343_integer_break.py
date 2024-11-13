def integerBreak(n: int) -> int:
    dp = [0 for _ in range(n + 1)]
    dp[2] = 1

    for i in range(3, n + 1):
        for j in range(2, i):
            dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)

    return dp[n]


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    DP       |      O(n^2)     |     O(n)     |
# |-------------|-----------------|--------------|

n = 8
print(integerBreak(n))  # 18
