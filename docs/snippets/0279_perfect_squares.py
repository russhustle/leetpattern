import math


def numSquares(n: int) -> int:
    dp = [float("inf") for _ in range(n + 1)]
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(n)) + 1):
            dp[i] = min(dp[i], dp[i - j**2] + 1)

    return dp[n]


n = 12
print(numSquares(n))  # 3
