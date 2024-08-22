from typing import List


# Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        profit += max(prices[i] - prices[i - 1], 0)

    return profit


print(maxProfitGreedy([7, 1, 5, 3, 6, 4]))
