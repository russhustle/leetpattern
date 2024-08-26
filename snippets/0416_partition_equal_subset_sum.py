from typing import List


def canPartition(nums: List[int]) -> bool:
    total_sum = sum(nums)

    if total_sum % 2 == 1 or len(nums) < 2:
        return False

    target = total_sum // 2

    dp = [0 for _ in range(target + 1)]

    for i in range(len(nums)):
        for j in range(target, nums[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

    return dp[target] == target


nums = [1, 5, 11, 5]
print(canPartition(nums))  # True
