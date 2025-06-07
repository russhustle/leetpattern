"""
- Return the number of distinct ways to reach the top of the stairs.
- `dp[n]` stores the number of distinct ways to reach the `n-th` stair.
- Formula: `dp[n] = dp[n - 1] + dp[n - 2]`.
- Initialize `dp[0] = 0`, `dp[1] = 1`, and `dp[2] = 2`.
"""

from functools import cache


# DP
def climbStairsDP(n: int) -> int:
    if n <= 2:
        return n

    dp = [i for i in range(n + 1)]

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# DP (Optimized)
def climbStairsDPOptimized(n: int) -> int:
    if n <= 2:
        return n

    first, second = 1, 2

    for _ in range(3, n + 1):
        first, second = second, first + second

    return second


# Recursion
def climbStairsRecursion(n: int) -> int:
    @cache
    def dfs(i: int) -> int:
        if i <= 1:
            return 1
        return dfs(i - 1) + dfs(i - 2)

    return dfs(n)


# Greedy
def climbStairsGreedy(n: int) -> int:
    if n <= 2:
        return n

    p1, p2 = 1, 2

    for _ in range(3, n + 1):
        p1, p2 = p2, p1 + p2

    return p2


if __name__ == "__main__":
    assert climbStairsDP(10) == 89
    assert climbStairsDPOptimized(10) == 89
    assert climbStairsRecursion(10) == 89
    assert climbStairsGreedy(10) == 89
