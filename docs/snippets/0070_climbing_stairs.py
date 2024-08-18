def climbStairs(n: int) -> int:
    if n < 2:
        return n

    dp = [i for i in range(n + 1)]

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 10
print(climbStairs(n))  # 89
