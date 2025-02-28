from typing import List


# DP (House Robber)
def rob1(nums: List[int]) -> int:
    if len(nums) < 3:
        return max(nums)

    dp = [0 for _ in range(len(nums))]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


# DP (House Robber) Optimized
def rob2(nums: List[int]) -> int:
    f0, f1 = 0, 0

    for num in nums:
        f0, f1 = f1, max(f1, f0 + num)

    return f1


nums = [2, 7, 9, 3, 1]
print(rob1(nums))  # 12
print(rob2(nums))  # 12
