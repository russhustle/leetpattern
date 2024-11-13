from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    dp = [0 for _ in range(len(cost))]

    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    print(dp)
    return min(dp[-1], dp[-2])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))  # 6
