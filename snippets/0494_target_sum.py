from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:

    totalSum = sum(nums)

    if abs(target) > totalSum:
        return 0
    if (target + totalSum) % 2 == 1:
        return 0

    targetSum = (target + totalSum) // 2
    dp = [0] * (targetSum + 1)
    dp[0] = 1

    for i in range(len(nums)):
        for j in range(targetSum, nums[i] - 1, -1):
            dp[j] += dp[j - nums[i]]

    return dp[targetSum]


nums = [1, 1, 1, 1, 1]
target = 3
print(findTargetSumWays(nums, target))  # 5
