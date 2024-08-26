from pprint import pprint
from typing import List


# 01 Knapsack - Manual Initialization
def knapsack01_1(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)

    # DP table initialization
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
def knapsack01_2(weights: List[int], values: List[int], capacity: int) -> int:
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


weights = [1, 4, 1, 2, 12]
values = [2, 10, 1, 2, 4]
capacity = 15

print(knapsack01_1(weights, values, capacity))  # 15
# [[0, 2, 2, 2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2],
#  [0, 2, 2, 2, 10, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
#  [0, 2, 3, 3, 10, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],
#  [0, 2, 3, 4, 10, 12, 13, 14, 15, 15, 15, 15, 15, 15, 15, 15],
#  [0, 2, 3, 4, 10, 12, 13, 14, 15, 15, 15, 15, 15, 15, 15, 15]]

print(knapsack01_2(weights, values, capacity))  # 15
# [[0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#  [0, 2, 2, 2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2],
#  [0, 2, 2, 2, 10, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
#  [0, 2, 3, 3, 10, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],
#  [0, 2, 3, 4, 10, 12, 13, 14, 15, 15, 15, 15, 15, 15, 15, 15],
#  [0, 2, 3, 4, 10, 12, 13, 14, 15, 15, 15, 15, 15, 15, 15, 15]]
