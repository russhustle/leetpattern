from typing import List


# 1. DP
def maxProfitDP1(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 5 for _ in range(n)]

    dp[0][0] = 0  # no transaction
    dp[0][1] = -prices[0]  # buy 1
    dp[0][2] = 0  # sell 1
    dp[0][3] = -prices[0]  # buy 2
    dp[0][4] = 0  # sell 2

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = max(dp[i - 1][1], -prices[i])
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
        dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

    return dp[-1][4]


# 2. DP - Optimized
def maxProfitDP2(prices: List[int]) -> int:
    b1, b2 = float("inf"), float("inf")
    s1, s2 = 0, 0

    for price in prices:
        b1 = min(b1, price)
        s1 = max(s1, price - b1)
        b2 = min(b2, price - s1)
        s2 = max(s2, price - b2)

    return s2


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfitDP1(prices))  # 6
print(maxProfitDP2(prices))  # 6
