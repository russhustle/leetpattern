"""
-   Return the maximum profit you can achieve.
"""

from typing import List


# DP
def maxProfitDP1(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = -prices[0]
    dp[0][1] = 0

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

    return dp[-1][1]


# DP - Optimized
def maxProfitDP2(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    hold = -prices[0]
    profit = 0

    for i in range(1, n):
        hold = max(hold, profit - prices[i])
        profit = max(profit, hold + prices[i])

    return profit


# Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        profit += max(prices[i] - prices[i - 1], 0)

    return profit


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |     DP1    |  O(n)  |   O(n)  |
# |     DP2    |  O(n)  |   O(1)  |
# |   Greedy   |  O(n)  |   O(1)  |
# |------------|--------|---------|


prices = [7, 1, 5, 3, 6, 4]
print(maxProfitDP1(prices))  # 7
print(maxProfitDP2(prices))  # 7
print(maxProfitGreedy(prices))  # 7
