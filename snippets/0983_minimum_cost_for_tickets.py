from typing import List


# DP
def mincostTickets(days: List[int], costs: List[int]) -> int:
    last = days[-1]
    dayset = set(days)
    dp = [0 for _ in range(last + 1)]

    for i in range(1, last + 1):
        if i not in dayset:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(
                dp[i - 1] + costs[0],
                dp[max(0, i - 7)] + costs[1],
                dp[max(0, i - 30)] + costs[2],
            )

    return dp[last]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(mincostTickets(days, costs))  # 11
