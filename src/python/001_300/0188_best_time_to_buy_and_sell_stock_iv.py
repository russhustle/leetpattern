from typing import List


# DP
def maxProfit(k: int, prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * (2 * k + 1) for _ in range(n)]

    for j in range(1, 2 * k, 2):
        dp[0][j] = -prices[0]

    for i in range(1, n):
        for j in range(0, 2 * k - 1, 2):
            dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
            dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])

    return dp[-1][2 * k]


k = 2
prices = [2, 4, 1]
print(maxProfit(k, prices))  # 2
