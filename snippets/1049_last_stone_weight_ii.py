from typing import List


def lastStoneWeightII(stones: List[int]) -> int:
    target = sum(stones) // 2

    dp = [0 for _ in range(target + 1)]

    for i in range(len(stones)):
        for j in range(target, stones[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

    result = (sum(stones) - dp[target]) - dp[target]

    return result


stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeightII(stones))  # 1
