"""
-   Return the minimum cost to reach the top of the stairs.

-   `dp[n]` stores the <u>minimum cost</u> to reach the `n-th` stair.
-   Formula: `dp[n] = cost[n] + min(dp[n - 1], dp[n - 2])`.
-   Initialize `dp[0] = cost[0]` and `dp[1] = cost[1]`.
-   Return `min(dp[-1], dp[-2])`.

-   Example: `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`

|  n  | `cost[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----: |
|  0  |     1     |     -     |     -     |    1    |
|  1  |    100    |     -     |     1     |   100   |
|  2  |     1     |     1     |    100    |    2    |
|  3  |     1     |    100    |     2     |    3    |
|  4  |     1     |     2     |     3     |    3    |
|  5  |    100    |     3     |     3     |   103   |
|  6  |     1     |     3     |    103    |    4    |
|  7  |     1     |    103    |     4     |    5    |
|  8  |    100    |     4     |     5     |   104   |
|  9  |     1     |     5     |    104    |    6    |
"""

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
