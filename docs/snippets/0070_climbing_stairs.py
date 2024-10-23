# DP
def climbStairs(n: int) -> int:
    if n <= 1:
        return n

    dp = [i for i in range(n + 1)]

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |     DP      |      O(n)       |     O(n)     |
# |-------------|-----------------|--------------|

print(climbStairs(10))  # 89
