"""
-   Return the maximum profit you can achieve with the given transaction fee.
"""

from typing import List


# 1. DP
def maxProfitDP(prices: List[int], fee: int) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 2 for _ in range(n)]

    dp[0][0] = -prices[0] - fee
    dp[0][1] = 0

    for i in range(1, n):
        dp[i][0] = max(
            dp[i - 1][0],  # hold
            dp[i - 1][1] - prices[i] - fee,  # buy
        )
        dp[i][1] = max(
            dp[i - 1][1],  # hold
            dp[i - 1][0] + prices[i],  # sell
        )

    return max(dp[-1])


# 2. Greedy
def maxProfitGreedy(prices: List[int], fee: int) -> int:
    n = len(prices)
    if n == 0:
        return 0

    buy = prices[0]
    profit = 0

    for i in range(1, n):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] > buy + fee:
            profit += prices[i] - buy - fee
            buy = prices[i] - fee

    return profit


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(maxProfitDP(prices, fee))  # 8
print(maxProfitGreedy(prices, fee))  # 8
