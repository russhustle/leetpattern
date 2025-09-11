from functools import cache
from typing import List

from leetpattern.utils import knapsack01


# Memoization
def canPartitionMemoization(nums: List[int]) -> bool:
    total = sum(nums)
    n = len(nums)

    if total % 2 == 1 or n <= 1:
        return False

    @cache
    def dfs(i, j):
        if i < 0:
            return j == 0
        return j >= nums[i] and dfs(i - 1, j - nums[i]) or dfs(i - 1, j)

    return dfs(n - 1, total // 2)


# DP - Knapsack 01
def canPartitionTemplate(nums: List[int]) -> bool:
    total = sum(nums)

    if total % 2 == 1 or len(nums) < 2:
        return False

    target = total // 2

    return knapsack01(nums, nums, target) == target


# DP - Knapsack 01
def canPartition(nums: List[int]) -> bool:
    total = sum(nums)

    if total % 2 == 1 or len(nums) < 2:
        return False

    target = total // 2

    dp = [0 for _ in range(target + 1)]

    for i in range(len(nums)):
        for j in range(target, nums[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

    return dp[target] == target


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(canPartitionTemplate(nums))  # True
    print(canPartition(nums))  # True
    print(canPartitionMemoization(nums))  # True
