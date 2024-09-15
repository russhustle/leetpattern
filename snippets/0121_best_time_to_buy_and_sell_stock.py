from typing import List


# Brute Force
def maxProfitBF(prices: List[int]) -> int:
    max_profit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit


# DP
def maxProfitDP(prices: List[int]) -> int:
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = -prices[0]  # buy
    dp[0][1] = 0  # sell

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], -prices[i])  # the lowest price to buy
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

    return dp[-1][1]


# Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    max_profit = 0
    seen_min = prices[0]

    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - seen_min)
        seen_min = min(seen_min, prices[i])

    return max_profit


# Fast Slow Pointers
def maxProfitFS(prices: List[int]) -> int:
    max_profit = 0
    slow, fast = 0, 1

    while fast < len(prices):
        if prices[fast] > prices[slow]:
            max_profit = max(max_profit, prices[fast] - prices[slow])
        else:
            slow = fast
        fast += 1

    return max_profit


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Brute Force|  O(n^2)|  O(1)   |
# | DP         |  O(n)  |  O(n)   |
# | Greedy     |  O(n)  |  O(1)   |
# | Fast Slow  |  O(n)  |  O(1)   |
# |------------|--------|---------|


prices = [7, 1, 5, 3, 6, 4]
print(maxProfitBF(prices))  # 5
print(maxProfitDP(prices))  # 5
print(maxProfitGreedy(prices))  # 5
print(maxProfitFS(prices))  # 5
