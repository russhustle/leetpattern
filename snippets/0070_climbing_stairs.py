# DP
def climbStairs(n: int) -> int:
    # TC: O(n)
    # SC: O(n)
    if n <= 1:
        return n

    dp = [i for i in range(n + 1)]

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(climbStairs(10))  # 89
