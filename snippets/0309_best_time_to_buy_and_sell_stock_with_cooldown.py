from typing import List


# DP
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 4 for _ in range(n)]

    dp[0][0] = -prices[0]  # poessess
    dp[0][1] = 0  # stay sold
    dp[0][2] = 0  # sell
    dp[0][3] = 0  # cooldown

    for i in range(1, n):
        dp[i][0] = max(
            dp[i - 1][0],  # stay poessess
            dp[i - 1][1] - prices[i],  # buy after stay sold
            dp[i - 1][3] - prices[i],  # buy after cooldown
        )
        dp[i][1] = max(
            dp[i - 1][1],  # stay sold
            dp[i - 1][3],  # stay cooldown
        )
        dp[i][2] = dp[i - 1][0] + prices[i]
        dp[i][3] = dp[i - 1][2]

    return max(dp[-1])


prices = [1, 2, 3, 0, 2]
print(maxProfit(prices))  # 3
