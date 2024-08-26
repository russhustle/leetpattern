from typing import List


# 1. Brute Force: O(n^2)
def maxProfitBF(prices: List[int]) -> int:
    # TC: O(n^2)
    # SC: O(1)
    maxProfit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            maxProfit = max(maxProfit, prices[j] - prices[i])

    return maxProfit


# 2. DP
def maxProfitDP(prices: List[int]) -> int:
    # TC: O(n)
    # SC: O(n)
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = -prices[0]  # buy
    dp[0][1] = 0  # sell

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], -prices[i])  # the lowest price to buy
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

    return dp[-1][1]


# 3. Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    # TC: O(n)
    # SC: O(1)
    maxProfit = 0
    seenMin = prices[0]

    for i in range(1, len(prices)):
        maxProfit = max(maxProfit, prices[i] - seenMin)
        seenMin = min(seenMin, prices[i])

    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfitBF(prices))  # 5
print(maxProfitDP(prices))  # 5
print(maxProfitGreedy(prices))  # 5
