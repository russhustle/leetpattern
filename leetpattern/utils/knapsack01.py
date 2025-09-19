from typing import List


# 01 Knapsack - Manual Initialization
def knapsack01Manual(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n)]

    for j in range(capacity + 1):
        if weights[0] <= j:
            dp[0][j] = values[0]

    for i in range(1, n):
        for j in range(1, capacity + 1):
            if weights[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],  # skip
                    dp[i - 1][j - weights[i]] + values[i],  # take
                )

    return dp[-1][-1]


# 01 Knapsack - Zero Initialization
def knapsack01(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],  # skip
                    dp[i - 1][j - weights[i - 1]] + values[i - 1],  # take
                )

    return dp[-1][-1]
