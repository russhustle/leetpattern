def integerBreak(n: int) -> int:
    # Time complexity: O(n^2)
    # Space complexity: O(n)

    dp = [0 for _ in range(n + 1)]
    dp[2] = 1

    for i in range(3, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)

    return dp[n]


n = 10
print(integerBreak(n))  # 36
