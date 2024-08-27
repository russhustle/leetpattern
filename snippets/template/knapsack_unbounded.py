from typing import List


# 1. Unbounded Knapsack - first loop on capacity
def knapsack_unbounded_1(
    weights: List[int], values: List[int], capacity: int
) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(capacity + 1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])

    return dp[capacity]


# 2. Unbounded Knapsack - first loop on items
def knapsack_unbounded_2(
    weights: List[int], values: List[int], capacity: int
) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(weights[i], capacity + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[capacity]


weights = [1, 4, 1, 2, 12]
values = [2, 10, 1, 2, 4]
capacity = 15

print(knapsack_unbounded_1(weights, values, capacity))  # 36
# [0, 2, 4, 6, 10, 12, 14, 16, 20, 22, 24, 26, 30, 32, 34, 36]
print(knapsack_unbounded_2(weights, values, capacity))  # 36
# [0, 2, 4, 6, 10, 12, 14, 16, 20, 22, 24, 26, 30, 32, 34, 36]
