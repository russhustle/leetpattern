from typing import List


# Unbounded Knapsack - first loop on capacity
def knapsackUnboundedCapacity(
    weights: List[int], values: List[int], capacity: int
) -> int:
    n = len(weights)
    dp = [0 for _ in range(capacity + 1)]

    for i in range(capacity + 1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])

    return dp[-1]


# Unbounded Knapsack - first loop on items
def knapsackUnboundedItems(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [0 for _ in range(capacity + 1)]

    for i in range(n):
        for j in range(weights[i], capacity + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[-1]


# Unbounded Knapsack - Space Optimized
def knapsackUnbounded(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [0 for _ in range(capacity + 1)]

    for i in range(n):
        for j in range(weights[i], capacity + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[-1]
